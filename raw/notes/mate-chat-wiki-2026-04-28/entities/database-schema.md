---
title: "데이터베이스 스키마"
type: entity
source_count: 1
tags: [database, postgresql, schema, sqlalchemy, alembic]
related:
  - ../sources/13-database-schema.md
  - ../sources/archive-legacy-system.md
  - ../entities/api-endpoints.md
  - ../concepts/soft-delete.md
  - ../concepts/repository-pattern.md
---

# 데이터베이스 스키마

## Overview

Mate Chat은 PostgreSQL 17를 사용하며, SQLAlchemy 2.0 (async) ORM과 Alembic 마이그레이션으로 24개 테이블 (23개 활성 + 1개 deprecated)을 관리한다. 원래 Firestore NoSQL 구조에서 관계형 데이터베이스로 전환되었으며, 정규화와 통합을 통해 효율적인 스키마로 재설계되었다.

> **Historical note**: 레거시 Firestore에서는 17개 이상의 루트 컬렉션과 다수의 서브컬렉션을 사용했다. following/follower, mate_req_sent/received, invite_sent/received 같은 양방향 관계가 각각 별도 컬렉션으로 중복 관리되었으며, personal_settings/personal_assets가 users와 분리되어 있었다. 리마스터에서 이를 정규화된 24개 테이블 (23개 활성 + 1개 deprecated)로 통합했다. Firestore → PostgreSQL 전체 매핑은 [레거시 시스템 아카이브](../sources/archive-legacy-system.md#2-firestore-데이터-구조) 참조.

## Architecture/Structure

### 도메인별 테이블 그룹

```
┌──────────────────────────────────────────────────────┐
│                   인증 & 사용자 (5)                     │
│  users / user_sessions / email_verifications          │
│  password_resets / auth_methods                        │
├──────────────────────────────────────────────────────┤
│                     소셜 (5)                           │
│  follows / mates / mate_requests / blocks              │
│  follow_logs                                           │
├──────────────────────────────────────────────────────┤
│                     채팅 (7)                            │
│  chat_rooms / chat_room_members / chat_messages        │
│  chat_room_invites / chat_room_bots                    │
│  chat_room_bot_settings / chat_room_member_logs        │
├──────────────────────────────────────────────────────┤
│                      AI (1)                             │
│  chatbots                                               │
├──────────────────────────────────────────────────────┤
│                     기타 (6)                            │
│  notifications / clover_transactions                    │
│  device_tokens / user_reports / data_export_requests    │
│  translations                                           │
└──────────────────────────────────────────────────────┘
```

### 관계 다이어그램

- `users` 테이블이 중심 엔티티로, 대부분의 테이블이 `user_id` FK로 참조
- `chatbots`는 `chat_rooms.primary_chatbot_id`, `chat_room_bots.chatbot_id`, `chat_messages.chatbot_id`로 참조
- `chat_rooms`는 `chat_room_members`, `chat_messages`, `chat_room_invites`, `chat_room_bots`와 1:N 관계

## Key Details

### 1. 인증 & 사용자 그룹

#### users (사용자)

핵심 엔티티. 프로필, 인증, 설정, 자산 정보를 통합 관리한다.

| 컬럼 | 타입 | 설명 |
|------|------|------|
| id | UUID (PK) | `gen_random_uuid()` |
| email | VARCHAR(255) UNIQUE | 이메일 |
| nickname | VARCHAR(100) | 닉네임 |
| introduction | TEXT | 자기소개 |
| country_code | VARCHAR(3) | ISO 3166-1 국가 코드 |
| languages | VARCHAR(10)[] | 언어 코드 배열 (GIN 인덱스) |
| gender | VARCHAR(20) | CHECK: male/female/other |
| age | INTEGER | 나이 |
| profile_image_url | TEXT | 프로필 이미지 URL |
| provider | VARCHAR(50) | 인증 제공자: google/apple/email |
| provider_id | VARCHAR(255) | OAuth 제공자 사용자 ID |
| password_hash | VARCHAR(255) | 이메일 인증 시 비밀번호 해시 |
| email_verified | - | 이메일 인증 여부 (운영 추가) |
| profile_visibility | VARCHAR(20) | everyone/mates/only_me |
| notification_enabled | BOOLEAN | 알림 설정 |
| clover_balance | INTEGER | 클로버 잔액 (>= 0) |
| created_at / updated_at / deleted_at | TIMESTAMPTZ | 타임스탬프 (soft delete) |

**인덱스**: email, country_code (partial), languages (GIN, partial), created_at

#### user_sessions (사용자 세션)

Refresh Token을 관리한다. 기기별 세션 추적이 가능하다.

- `refresh_token_hash`: 토큰의 해시값 저장 (원본 저장 안 함)
- `device_info` (JSONB): 기기 정보
- `expires_at`: 만료 시간 (6개월)
- UNIQUE 제약: (user_id, refresh_token_hash)

#### email_verifications / password_resets (운영 추가)

이메일 인증 토큰(24시간 만료)과 비밀번호 재설정 토큰(1시간 만료)을 관리한다.

### 2. 소셜 그룹

#### follows (팔로우)

단방향 팔로우 관계. UNIQUE(follower_id, following_id)로 중복 방지, self-follow CHECK 제약.

#### mates (Mate 관계)

양방향 친구 관계. 수락 시 양쪽 모두 레코드가 생성된다. UNIQUE(user_id, mate_id).

#### mate_requests (Mate 요청)

상태 머신: pending -> accepted/rejected. `responded_at` 타임스탬프. pending 상태에 partial 인덱스.

#### blocks (차단)

차단 관계. 차단 시 관련 소셜 관계(팔로우, 메이트)가 서비스 레벨에서 정리된다.

### 3. 채팅 그룹

#### chat_rooms (채팅방)

4가지 유형을 `type` ENUM + `is_ai_room` 불리언 조합으로 구분:

| 유형 | type | is_ai_room | 설명 |
|------|------|-----------|------|
| 공개 | open | false | 누구나 검색/참여 |
| 메이트 그룹 | mate | false | 메이트 전용, 초대 기반 |
| 사용자 1:1 | private | false | DM |
| AI 1:1 | private | true | AI 챗봇 대화 |

- `creator_id`, `manager_id`: 생성자/관리자 FK
- `primary_chatbot_id`: AI 방의 주 챗봇
- `tags`: VARCHAR(50)[] 배열 (GIN 인덱스)
- Soft delete 지원

#### chat_room_members (채팅방 멤버)

- `notification_enabled`: 방별 알림 설정
- `last_read_at`: 읽음 위치 추적
- `unread_count`: 안 읽은 메시지 수
- `left_at`: NULL이면 활성 멤버 (partial 인덱스)
- UNIQUE(room_id, user_id)

#### chat_messages (채팅 메시지)

- `message_type`: 0(일반), 1(이미지), 2(시스템), 3(AI 생각중)
- `is_ai_message` + `chatbot_id`: AI 메시지 식별
- `attachments` (JSONB): 미디어 첨부
- 복합 인덱스: (room_id, created_at DESC) 역순 정렬
- 전문 검색: GIN 인덱스 on `to_tsvector('simple', content)`

#### chat_room_invites (채팅방 초대)

상태 머신: pending -> accepted/rejected. UNIQUE(room_id, invitee_id).

#### chat_room_bots (운영 추가)

하이브리드 AI 채팅을 위해 채팅방에 봇을 추가. trigger_prefix, context_window 설정.

### 4. AI 그룹

#### chatbots (AI 챗봇)

- `instructions`: 시스템 프롬프트
- `model`: 기본 'gpt-4o-mini'
- `is_public`: 공개/비공개
- `usage_count` / `paid_usage_count`: 사용 통계
- Soft delete 지원

### 5. 기타 그룹

#### notifications (알림)

6가지 ENUM 타입: follow, mate_request, mate, invite, force_exit, chat. `read_at`, `clicked_at`으로 상태 추적. `data` (JSONB)에 딥링크 등 추가 데이터.

#### clover_transactions (클로버 거래)

ENUM 타입: purchase, ai_chat, creator_earning, welcome_bonus, welcome_bonus_expiration. `chatbot_create`, `chatbot_delete`는 legacy로 스키마에는 남아 있으나 현재 기획에서 미사용. `amount` (양수: 획득, 음수: 소비), `balance_after` (거래 후 잔액).

#### device_tokens (디바이스 토큰)

FCM 푸시 알림 토큰. platform: ios/android/web. UNIQUE(token).

#### user_reports (사용자 신고)

상태 머신: pending -> reviewed -> resolved. `evidence_urls` 배열, `admin_notes`.

#### translations (번역 캐시)

UGC(사용자 생성 콘텐츠) 필드의 번역 결과를 영속적으로 캐싱한다.

- `entity_type` / `entity_id` / `field_name`: 번역 대상 엔티티 식별
- `source_hash`: 원본 텍스트 해시 (변경 감지)
- `source_locale` / `target_locale`: 언어 코드
- `translated_text`: 번역 결과
- `status`: pending / completed / failed / stale
- `quality_score`: 번역 품질 점수
- UNIQUE 제약: (entity_type, entity_id, field_name, source_hash, target_locale)

## Dependencies

- **PostgreSQL 17**: 데이터베이스 엔진
- **SQLAlchemy 2.0+ (async)**: ORM
- **Alembic**: 마이그레이션 관리 (13개 마이그레이션 파일)
- **asyncpg**: PostgreSQL async 드라이버

### 파일 위치

- 모델 정의: `app/models/` (24개 SQLAlchemy 모델)
- 마이그레이션: `migrations/` (13개 파일)
- DB 설정: `app/core/database.py`

## Known Issues

1. **WebSocket DB 풀 점유**: WebSocket 연결이 DB 풀 슬롯을 연결 수명 동안 점유하여 pool_size 주의 필요
2. **설계 문서와 운영 차이**: 설계 문서는 16개 테이블이지만 운영은 24개 테이블(23개 활성 + 1개 deprecated)로 확장됨 (auth_methods, follow_logs, chat_room_bot_settings, chat_room_member_logs, data_export_requests 등 추가)
3. **ai_chat_sessions의 JSONB 히스토리**: 대화가 길어지면 JSONB 크기가 커질 수 있음

## Related

- [API 엔드포인트](../entities/api-endpoints.md) -- 각 테이블에 대응하는 API
- [Repository 패턴](../concepts/repository-pattern.md) -- 데이터 접근 계층 설계
- [Soft Delete 패턴](../concepts/soft-delete.md) -- deleted_at 컬럼 전략
- [소스: 데이터베이스 스키마 설계](../sources/13-database-schema.md)
