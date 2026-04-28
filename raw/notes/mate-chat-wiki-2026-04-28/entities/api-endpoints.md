---
title: "API 엔드포인트"
type: entity
source_count: 1
tags: [api, rest, fastapi, endpoints, jwt]
related:
  - ../sources/14-api-design.md
  - ../entities/database-schema.md
  - ../concepts/api-versioning.md
  - ../concepts/pydantic-schema-design.md
  - ../concepts/repository-pattern.md
---

# API 엔드포인트

## Overview

Mate Chat 백엔드는 FastAPI 기반 RESTful API로 구성되며, 설계 문서 기준 44개, 실제 운영 기준 114개의 엔드포인트를 제공한다. 모든 API는 `/v1` 접두사를 사용하고, JWT Bearer 토큰으로 인증한다. 실시간 메시징은 WebSocket으로 별도 처리한다.

## Architecture/Structure

### 계층 구조

```
클라이언트 요청
    │
    ▼
Router (app/api/v1/router.py)
    │
    ├── endpoints/app_config.py      (1개)
    ├── endpoints/auth.py            (21개)
    ├── endpoints/users.py           (14개)
    ├── endpoints/social.py          (21개)
    ├── endpoints/chats.py           (27개)
    ├── endpoints/websocket.py       (1개)
    ├── endpoints/chatbots.py        (9개)
    ├── endpoints/clover.py          (5개)
    ├── endpoints/notifications.py   (8개)
    ├── endpoints/uploads.py         (1개)
    ├── endpoints/reports.py         (3개)
    ├── endpoints/translations.py    (1개)
    └── endpoints/dev.py             (2개)
    │
    ▼
Middleware (Rate Limit → Metrics → Logging)
    │
    ▼
Service Layer → Repository Layer → Database
```

### 응답 형식

**성공 응답**:
```json
{
  "data": { ... },
  "meta": { "page": 1, "per_page": 20, "total": 100 }
}
```

**에러 응답**:
```json
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Invalid input data",
    "details": [{ "field": "email", "message": "Invalid email format" }]
  }
}
```

## Key Details

### 1. 인증 API (`/auth/`)

| 메서드 | 경로 | 설명 | 인증 |
|--------|------|------|------|
| POST | `/auth/oauth` | OAuth 로그인 (Google) | 불필요 |
| POST | `/auth/register` | 이메일 회원가입 | 불필요 |
| POST | `/auth/login` | 이메일 로그인 | 불필요 |
| POST | `/auth/refresh` | 토큰 갱신 | 불필요 |
| POST | `/auth/logout` | 로그아웃 | 필요 |
| GET | `/auth/verify-email` | 이메일 인증 | 불필요 |
| POST | `/auth/forgot-password` | 비밀번호 재설정 요청 | 불필요 |
| GET/POST | `/auth/reset-password` | 비밀번호 재설정 폼/처리 | 불필요 |

- Rate Limit: 10/분
- OAuth: Google ID 토큰 검증 후 JWT 발급
- JWT: Access Token (7일) + Refresh Token (6개월)

### 2. 사용자 API (`/users/`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/users/me` | 내 프로필 조회 |
| PATCH | `/users/me` | 프로필 수정 |
| POST | `/users/me/profile-image` | 프로필 이미지 업로드 (max 5MB) |
| GET | `/users/{user_id}` | 사용자 조회 (visibility 적용) |
| GET | `/users/explore` | 사용자 탐색 (국가/언어/성별/나이 필터) |
| DELETE | `/users/me` | 계정 삭제 |

- 탐색 페이지네이션: offset 기반 (page, per_page, max 100)

### 3. 소셜 API

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/users/{id}/follow` | 팔로우 |
| DELETE | `/users/{id}/follow` | 언팔로우 |
| GET | `/users/me/followers` | 팔로워 목록 |
| GET | `/users/me/following` | 팔로잉 목록 |
| POST | `/users/{id}/mate-request` | Mate 요청 |
| POST | `/mate-requests/{id}/respond` | Mate 요청 응답 (accept/reject) |
| GET | `/users/me/mate-requests/received` | 받은 요청 목록 |
| GET | `/users/me/mates` | Mate 목록 |
| POST | `/users/{id}/block` | 차단 |
| DELETE | `/users/{id}/block` | 차단 해제 |

- 쿨다운: 메이트 해제 후 24시간, 팔로우 해제 후 1시간
- 차단 시 팔로우/메이트 관계 자동 정리

### 4. 채팅 API (`/chat-rooms/`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/chat-rooms` | 채팅방 생성 (open/mate) |
| GET | `/chat-rooms` | 내 채팅방 목록 |
| GET | `/chat-rooms/explore` | 공개 채팅방 탐색 |
| GET | `/chat-rooms/{id}` | 채팅방 상세 |
| PATCH | `/chat-rooms/{id}` | 채팅방 수정 |
| DELETE | `/chat-rooms/{id}` | 채팅방 삭제 |
| POST | `/chat-rooms/{id}/join` | 공개방 참여 |
| DELETE | `/chat-rooms/{id}/members/me` | 채팅방 나가기 |
| GET | `/chat-rooms/{id}/messages` | 메시지 조회 (커서 기반) |
| POST | `/chat-rooms/{id}/messages` | 메시지 전송 (REST) |
| POST | `/chat-rooms/{id}/invites` | 초대 보내기 |
| GET | `/users/me/chat-room-invites` | 받은 초대 목록 |
| POST | `/chat-room-invites/{id}/respond` | 초대 응답 |
| POST | `/chat-rooms/dm/{target_user_id}` | 1:1 DM 생성 |

- 메시지 페이지네이션: 커서 기반 (`before` 파라미터, `has_more` + `next_cursor`)
- 메시지 전송 Rate Limit: 30/분

### 5. WebSocket (`/ws/`)

| 경로 | 설명 |
|------|------|
| `ws://host/v1/ws/chat/{room_id}?token={jwt}` | 실시간 채팅 |

메시지 타입: message, typing, read, ping/pong

### 6. AI 챗봇 API (`/chatbots/`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/chatbots` | 챗봇 생성 |
| GET | `/chatbots/me` | 내 챗봇 목록 |
| GET | `/chatbots/explore` | 공개 챗봇 탐색 |
| GET | `/chatbots/{id}` | 챗봇 상세 |
| PATCH | `/chatbots/{id}` | 챗봇 수정 |
| DELETE | `/chatbots/{id}` | 챗봇 삭제 |
| POST | `/chatbots/{id}/chat` | AI 대화 (-5 클로버) |
| POST | `/chatbots/{id}/mate` | 챗봇 메이트 추가 |
| DELETE | `/chatbots/{id}/mate` | 챗봇 메이트 해제 |

- AI 채팅 Rate Limit: 20/분
- 클로버 비용: AI 대화 시 5 클로버 차감 (생성/삭제는 무료)

### 7. 알림 API (`/notifications/`)

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/notifications` | 알림 목록 (unread_only 필터) |
| POST | `/notifications/{id}/read` | 단건 읽음 |
| POST | `/notifications/read-all` | 전체 읽음 |
| GET | `/notifications/unread-count` | 미읽음 수 |
| POST | `/device-tokens` | 디바이스 토큰 등록 |

### 8. 결제 API

| 메서드 | 경로 | 설명 |
|--------|------|------|
| GET | `/products/clovers` | 상품 목록 |
| POST | `/purchases/verify` | 구매 검증 (Google Play / App Store) |
| GET | `/users/me/clover-transactions` | 거래 내역 |

### 9. 신고 API

| 메서드 | 경로 | 설명 |
|--------|------|------|
| POST | `/users/{id}/report` | 사용자 신고 |

### Rate Limiting 요약

| 대상 | 제한 | 응답 헤더 |
|------|------|----------|
| 인증 API | 10/분 | X-RateLimit-* |
| 일반 API | 100/분 | X-RateLimit-* |
| 메시지 전송 | 30/분 | X-RateLimit-* |
| AI 채팅 | 20/분 | X-RateLimit-* |
| 글로벌 | 60/분 | X-RateLimit-* |

초과 시 429 Too Many Requests 반환.

## Dependencies

- **FastAPI 0.117.1+**: 웹 프레임워크
- **Pydantic**: 요청/응답 스키마 검증
- **JWT (PyJWT)**: 토큰 생성/검증
- **Redis**: Rate Limiting 카운터 저장

### 파일 위치

- 라우터: `app/api/v1/router.py`
- 엔드포인트: `app/api/v1/endpoints/`
- 스키마: `app/schemas/` (10개 Pydantic 스키마)
- 서비스: `app/services/` (15개 서비스)
- 미들웨어: `app/middleware/`

## Known Issues

1. **설계 문서 vs 운영 차이**: 설계 44개 -> 운영 114개 엔드포인트 (이메일 인증, 하이브리드 AI, COPPA 등 추가)
2. **Apple OAuth 미구현**: iOS App Store 출시 시 필요
3. **Rate Limiting 수치 차이**: 설계 문서(100/분)와 운영 설정(60/분 글로벌)에 차이 존재

## Related

- [데이터베이스 스키마](../entities/database-schema.md) -- API가 조회/수정하는 테이블
- [API 버전 관리](../concepts/api-versioning.md) -- URL 기반 버전 전략
- [Pydantic 스키마 설계](../concepts/pydantic-schema-design.md) -- 요청/응답 검증
- [Repository 패턴](../concepts/repository-pattern.md) -- 데이터 접근 계층
- [소스: API 설계](../sources/14-api-design.md)
