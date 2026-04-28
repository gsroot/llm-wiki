---
title: "데이터베이스 스키마 설계"
type: source
source_path: docs/13-database-schema.md
date_ingested: 2026-04-07
tags: [database, postgresql, schema, migration, erd]
related:
  - ../entities/database-schema.md
  - ../concepts/repository-pattern.md
  - ../concepts/soft-delete.md
---

# 데이터베이스 스키마 설계 (요약)

## 문서 목적

Firestore NoSQL 구조를 PostgreSQL 관계형 데이터베이스로 변환한 전체 스키마를 정의하는 설계 문서이다.

## 핵심 내용

### 테이블 구성 (16개 테이블)

설계 문서 기준 16개 테이블이 정의되어 있으며, 실제 운영에서는 추가 테이블(email_verifications, password_resets, chat_room_bots, chatbot_mates)을 포함하여 20개 테이블로 운영된다.

| 도메인 | 테이블 | 설명 |
|--------|--------|------|
| 인증/사용자 | users | 사용자 프로필, 인증, 설정, 자산 통합 |
| 인증/사용자 | user_sessions | Refresh Token 관리 |
| 소셜 | follows | 팔로우 관계 (단방향) |
| 소셜 | mates | Mate 관계 (양방향) |
| 소셜 | mate_requests | Mate 요청 상태 관리 |
| 소셜 | blocks | 차단 관계 |
| 채팅 | chat_rooms | 채팅방 (open/mate/private + AI) |
| 채팅 | chat_room_members | 채팅방 멤버십 |
| 채팅 | chat_messages | 메시지 (일반, AI, 시스템) |
| 채팅 | chat_room_invites | 채팅방 초대 |
| AI | chatbots | AI 챗봇 정의 |
| AI | ai_chat_sessions | AI 대화 세션 히스토리 |
| 기타 | notifications | 알림 (6가지 타입) |
| 기타 | user_reports | 사용자 신고 |
| 기타 | clover_transactions | 가상 화폐 거래 내역 |
| 기타 | device_tokens | FCM 푸시 토큰 |

### 주요 설계 결정

1. **UUID Primary Key**: 모든 테이블에서 `gen_random_uuid()` 사용
2. **Soft Delete**: users, chat_rooms, chat_messages, chatbots에 `deleted_at` 컬럼
3. **ENUM 타입**: `chat_room_type`, `notification_type`, `transaction_type` 3개 PostgreSQL ENUM
4. **GIN 인덱스**: 배열(languages, tags) 및 전문 검색(content)에 GIN 인덱스 활용
5. **Partial 인덱스**: `WHERE deleted_at IS NULL`, `WHERE status = 'pending'` 등 조건부 인덱스로 성능 최적화
6. **Self-reference 방지**: follows, mates, blocks, mate_requests에 자기 참조 CHECK 제약

### Firestore 마이그레이션 매핑

- 1:1 변환: profiles -> users, chat_rooms, chatbots, user_reports
- 통합: personal_settings, personal_assets -> users 컬럼으로 통합
- 정규화: 서브컬렉션(following/follower, mates, blocks 등) -> 독립 테이블
- 플랫화: chat_messages 서브컬렉션 -> 단일 테이블

### 채팅방 분류 체계

`type` 필드(open/mate/private)와 `is_ai_room` 불리언의 조합으로 4가지 채팅방 유형을 구분한다.

## 관련 문서

- [데이터베이스 스키마 엔티티](../entities/database-schema.md)
- [Soft Delete 패턴](../concepts/soft-delete.md)
