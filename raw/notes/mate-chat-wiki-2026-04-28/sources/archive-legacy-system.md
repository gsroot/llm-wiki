---
title: "레거시 시스템 아카이브"
type: source
source_path: docs/_archive/
date_ingested: 2026-04-07
tags: [legacy, firebase, migration, historical]
related:
  - "../sources/10-remaster-overview.md"
  - "../concepts/vendor-independence.md"
  - "../concepts/layered-architecture.md"
  - "../entities/database-schema.md"
  - "../entities/auth-system.md"
  - "../entities/websocket-manager.md"
---

# 레거시 시스템 아카이브

> **Historical Context**: 이 문서는 Firebase 기반 레거시 시스템(리마스터 이전)의 8개 설계 문서를 통합 정리한 것이다.
> 현재 시스템(FastAPI + PostgreSQL)과는 아키텍처가 완전히 다르며, 마이그레이션 의사결정의 맥락을 이해하기 위한 참고 자료로만 활용해야 한다.
>
> **Deprecated 기획 요소** (아래 언급되지만 현재 기획에서는 미적용):
> - 챗봇 생성 시 -10 클로버 차감, 챗봇 삭제 시 +2 클로버 환불 → 현재 챗봇 생성/삭제는 무료
> - "Private" 채팅방을 한국어로 "비공개 채팅방"으로 표기 → 현재 사용자 노출 용어는 "1:1 채팅방"

## 원본 문서 목록

| 번호 | 문서 | 핵심 내용 |
|------|------|----------|
| 01 | app-overview | 앱 컨셉, 타겟 사용자, 비즈니스 모델 |
| 02 | features-analysis | 기능 상세 분석 (인증, 소셜, 채팅, AI, 결제) |
| 03 | user-flow | 전체 사용자 플로우, 페이지 네비게이션 구조 |
| 04 | data-models | Firestore 컬렉션 구조, Dart 데이터 모델 |
| 05 | backend-analysis | Cloud Functions 분석, 7개 함수 |
| 06 | tech-stack-legacy | Flutter 패키지, Firebase 서비스, 외부 연동 |
| 17 | migration-strategy | Strangler Fig 마이그레이션, 4단계 계획 |
| 18 | improvement-points | 레거시 문제점, 리마스터 개선 목표 |

---

## 1. 레거시 아키텍처 개요

### 기술 스택

| 영역 | 기술 |
|------|------|
| 프론트엔드 | Flutter 3.x + Riverpod 2.x |
| 백엔드 | Firebase Cloud Functions (Python 3.x) |
| 데이터베이스 | Firestore (NoSQL) |
| 인증 | Firebase Auth (Google, Facebook, Email/Password) |
| 스토리지 | Firebase Storage |
| 실시간 통신 | Firestore 실시간 스트림 |
| 푸시 알림 | FCM (토픽 + 토큰 기반) |
| AI | OpenAI gpt-4o-mini |
| 결제 검증 | Google Play Developer API v3 |
| 리전 | asia-northeast3 (서울) |

### 데이터 흐름 (레거시)

```
Flutter App → Firestore SDK (직접 접근) → Firestore DB
Flutter App → Cloud Functions (HTTP) → OpenAI / Google Play API
Firestore Trigger → Cloud Functions → FCM 푸시
```

> **Historical note**: 레거시 시스템에서는 Flutter 앱이 Firestore에 직접 접근했다. 비즈니스 로직이 클라이언트와 Cloud Functions에 분산되어 있었으며, 이것이 리마스터의 주요 동기 중 하나였다.

---

## 2. Firestore 데이터 구조

레거시 시스템은 17개 이상의 Firestore 루트 컬렉션과 다수의 서브컬렉션으로 구성되었다.

### 주요 컬렉션

| Firestore 경로 | 현재 PostgreSQL 테이블 | 변환 방식 |
|---------------|----------------------|----------|
| `profiles/{userId}` | users | 직접 매핑 |
| `personal_settings/{userId}` | users (컬럼 병합) | 필드 병합 |
| `personal_assets/{userId}` | users.clover_balance | 필드 병합 |
| `chat_rooms/{id}` | chat_rooms | 직접 매핑 |
| `chat_messages/{roomId}/messages/{msgId}` | chat_messages | 플랫화 |
| `my_chat_rooms/{userId}/rooms/{roomId}` | chat_room_members | 정규화 |
| `following/{userId}/following/{targetId}` | follows | 정규화 |
| `follower/{userId}/follower/{followerId}` | follows (역방향) | 단일 테이블로 통합 |
| `mates/{userId}/mates/{mateId}` | mates | 정규화 |
| `mate_req_received/sent` | mate_requests | 단일 테이블로 통합 |
| `blocks/{userId}/blocked/{blockedId}` | blocks | 정규화 |
| `chatbots/{id}` | chatbots | 직접 매핑 |
| `chatbot_usage/{id}` | chatbots (컬럼 병합) | 필드 병합 |
| `notifications/{receiverId}/messages/{id}` | notifications | 플랫화 |
| `invite_received/sent` | chat_room_invites | 단일 테이블로 통합 |
| `user_reports/{id}` | user_reports | 직접 매핑 |

> **Historical note**: Firestore의 서브컬렉션 기반 구조에서는 following/follower, mate_req_sent/received, invite_sent/received가 각각 별도 컬렉션이었다. PostgreSQL 리마스터에서 이를 단일 테이블 + FK 관계로 정규화했다.

### 레거시 데이터 모델 특징

- **Profile ID**: Firebase Auth UID를 그대로 사용 (현재: 자체 정수 ID + UUID)
- **Country**: 별도 객체(`{code, name}`)로 저장 (현재: `country_code` 단일 필드)
- **인증 제공자**: `google`, `facebook`, `password` (현재: `google`, `email`, 향후 `apple`)
- **메시지 타입**: 숫자 코드 `0`(일반), `3`(AI 생각중) (현재: `text`, `system` enum)
- **채팅방 멤버**: `memberIds` 배열로 채팅방 문서에 직접 저장 (현재: `chat_room_members` 관계 테이블)

---

## 3. Cloud Functions (레거시 백엔드)

레거시 백엔드는 7개의 Cloud Functions로 구성되었다.

### Firestore 트리거 (2개)

| 함수 | 트리거 | 용도 |
|------|--------|------|
| `send_chat_notification` | `on_document_created` chat_messages | 채팅 메시지 FCM 푸시 |
| `send_app_notification` | `on_document_created` notifications | 인앱 알림 FCM 푸시 |

### HTTP 함수 (5개)

| 함수 | 용도 | 비용 |
|------|------|------|
| `root` | 헬스 체크 | - |
| `create_chatbot` | 챗봇 생성 | ~~-10 클로버~~ *(legacy, 현재 무료)* |
| `read_chatbots` / `read_chatbot` | 챗봇 조회 | - |
| `update_chatbot` / `delete_chatbot` | 챗봇 수정/삭제 | ~~삭제 시 +2 클로버 환불~~ *(legacy, 현재 환불 없음)* |
| `send_chat` | AI 채팅 | -5 클로버 (사용자), +1 클로버 (크리에이터) |
| `do_post_purchase_process` | 인앱 결제 검증 | - |

> **Historical note**: 레거시에서는 사용자 CRUD, 소셜 관계, 채팅방 관리 등 대부분의 데이터 조작을 클라이언트에서 Firestore에 직접 수행했다. 서버 사이드 로직은 AI 채팅, 결제 검증, 푸시 알림 등 외부 서비스 연동이 필요한 경우에만 Cloud Functions를 사용했다. 현재 시스템에서는 모든 비즈니스 로직이 FastAPI 서버를 경유한다 (83개 API 엔드포인트).

---

## 4. 마이그레이션 의사결정

### 왜 Firebase를 떠났는가

문서 18 (improvement-points)에서 식별한 핵심 문제:

**아키텍처 문제**:
- Firestore 직접 접근으로 인한 보안 취약 (Security Rules가 `allow read, write: if true`로 설정)
- 비즈니스 로직이 Flutter 앱과 Cloud Functions에 분산
- 스키마리스 DB로 인한 데이터 일관성 보장 어려움
- 비정규화된 중복 데이터의 동기화 문제

**보안 문제**:
- 서버 측 입력 검증 부재 (클라이언트 측 검증만 존재)
- 세션 관리 한계 (강제 로그아웃, 다중 디바이스 관리 불가)
- Firestore/Storage Security Rules가 모든 접근을 허용하는 상태

**성능 문제**:
- Firestore 복합 쿼리 제한 (JOIN 불가)
- 문서 전체 가져오기로 인한 불필요한 데이터 전송
- 서버 측 캐싱 불가 (클라이언트 캐시만 존재)
- 컬렉션별 실시간 리스너 과다

**유지보수 문제**:
- Firebase 에뮬레이터 설정 복잡 → 테스트 부재
- Firestore 동적 스키마 → 타입 안정성 부족
- 벤더 락인 → 비용 증가 리스크

### 마이그레이션 전략: Strangler Fig Pattern

문서 17에서 4단계 점진적 전환 전략을 수립했다:

1. **Phase 1 — 신규 시스템 구축**: FastAPI + PostgreSQL + WebSocket 인프라 구축
2. **Phase 2 — 데이터 마이그레이션**: Firestore → PostgreSQL 데이터 이전 (의존성 순서대로)
3. **Phase 3 — 프론트엔드 전환**: Flutter 앱의 Firebase SDK → Dio HTTP + WebSocket 전환
4. **Phase 4 — 운영 전환**: DNS 전환, 모니터링, 기존 시스템 종료

> **Historical note**: 실제 마이그레이션은 레거시 데이터 이전 없이 "클린 스타트"로 진행되었다. 기존 사용자 데이터를 이전하는 대신, 새 시스템에서 처음부터 시작하는 방식을 택했다 (앱이 출시 전이었으므로 가능했음).

### 기술 선택 근거

| 영역 | 레거시 | 현재 | 전환 이유 |
|------|--------|------|----------|
| 백엔드 | Cloud Functions | FastAPI | 비즈니스 로직 중앙화, 자체 호스팅 |
| DB | Firestore | PostgreSQL | ACID 트랜잭션, JOIN, FK 제약 |
| 인증 | Firebase Auth | JWT + OAuth | 세션 제어, 강제 로그아웃, 유연한 클레임 |
| 실시간 | Firestore 스트림 | WebSocket | 이벤트 기반, 타이핑/읽음 표시, 온라인 상태 |
| 스토리지 | Firebase Storage | MinIO | S3 호환, 벤더 독립성 |
| 캐시 | 없음 | Redis | 서버 측 캐싱, Rate Limiting |
| 모니터링 | Crashlytics | Sentry | 서버 측 에러 추적, structlog |
| 폰트 | NanumSquareRound | Pretendard | 한국어 최적화 |
| 디자인 | 다크 블루 테마 | Material Design 3 + shadcn/ui | 모던 UI |
| OAuth | Google + Facebook | Google (+ Apple 예정) | Facebook 제거, Apple 추가 예정 |

---

## 5. 레거시에서 유지된 것

마이그레이션 과정에서 변경 없이 유지된 핵심 요소:

- **앱 컨셉**: 글로벌 소셜 메시징 + AI 챗봇 플랫폼
- **핵심 기능 범위**: 소셜 관계(Follow/Mate), 채팅방 3종(Private/Mate/Open), AI 챗봇
- **클로버 경제**: 챗봇 생성(-10), AI 채팅(-5), 크리에이터 수익(+1)
- **9개 언어 지원**: en, ko, ja, es, fr, ru, zh_Hans, zh_Hant, zh
- **Flutter + Riverpod**: 프론트엔드 프레임워크와 상태 관리 유지
- **OpenAI 통합**: GPT 모델 기반 AI 채팅
- **FCM 푸시 알림**: Firebase Cloud Messaging은 유일하게 잔존하는 Firebase 종속

---

## 6. 리마스터에서 추가/개선된 것

레거시에 없었으나 리마스터에서 새로 도입된 기능과 개선 사항:

| 카테고리 | 신규/개선 항목 |
|----------|---------------|
| 실시간 | 타이핑 인디케이터, 읽음 표시, 온라인 상태 추적 |
| 채팅 | 하이브리드 AI 채팅 (일반 채팅방에 봇 추가, @멘션 트리거) |
| 소셜 | 쿨다운 시스템 (Mate 24시간, Follow 1시간) |
| 인증 | 이메일 인증 플로우, 비밀번호 재설정, Welcome 보너스(200 클로버) |
| 보안 | JWT 기반 세션 관리, Rate Limiting, structlog, Sentry |
| 인프라 | Docker 컨테이너화, Redis 캐싱, MinIO 객체 스토리지 |
| 테스트 | 113개 테스트 함수 (레거시: 테스트 0개) |
| 결제 | Apple App Store IAP 검증 (Google Play와 병행) |
| 봇 | 챗봇 메이트 시스템 (AI와 친구 관계), 전용 1:1 AI 채팅방 |

---

## 7. 교훈 (Lessons Learned)

레거시 → 리마스터 전환 과정에서 얻은 주요 교훈:

1. **서버리스 ≠ 만능**: Firebase의 "코드 없이 DB 접근"은 프로토타이핑에 유리하지만, 보안과 비즈니스 로직 관리가 어려워진다.
2. **Security Rules의 한계**: Firestore Security Rules로 복잡한 접근 제어를 구현하면 유지보수가 극히 어렵다. 결국 `allow: true`로 방치되는 결과를 초래했다.
3. **스키마리스의 대가**: NoSQL의 유연성은 초기 개발 속도를 높이지만, 데이터 일관성 문제가 누적된다.
4. **벤더 종속성**: Firebase 에코시스템에 깊이 종속되면 기술 선택의 자유도가 급격히 낮아진다.
5. **테스트 인프라의 중요성**: Firebase 에뮬레이터의 복잡한 설정이 테스트 작성을 가로막았다. 표준 pytest로 전환 후 113개 테스트를 확보했다.
