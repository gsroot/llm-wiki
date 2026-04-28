---
title: "API 설계"
type: source
source_path: docs/14-api-design.md
date_ingested: 2026-04-07
tags: [api, rest, jwt, rate-limiting, http]
related:
  - ../entities/api-endpoints.md
  - ../concepts/api-versioning.md
  - ../concepts/pydantic-schema-design.md
---

# API 설계 (요약)

## 문서 목적

Mate Chat 백엔드의 RESTful API 전체 설계를 정의하는 문서이다. 기본 URL, 인증 방식, 응답 형식, 각 도메인별 엔드포인트 명세를 포함한다.

## 핵심 내용

### 기본 사양

| 항목 | 값 |
|------|------|
| Base URL | `https://api.matechat.com/v1` |
| 프로토콜 | HTTPS (TLS 1.3) |
| 인증 | Bearer Token (JWT) |
| 형식 | JSON (UTF-8) |
| 버전 관리 | URL path 기반 (`/v1/`) |

### 응답 형식

- **성공**: `{ "data": {...}, "meta": { page, per_page, total } }`
- **에러**: `{ "error": { "code": "...", "message": "...", "details": [...] } }`
- HTTP 상태 코드: 200, 201, 204, 400, 401, 403, 404, 409, 422, 429, 500

### 엔드포인트 구성 (설계 문서 기준)

| 도메인 | 엔드포인트 수 | 주요 경로 |
|--------|-------------|----------|
| 인증 | 3개 | `/auth/oauth`, `/auth/refresh`, `/auth/logout` |
| 사용자 | 5개 | `/users/me`, `/users/{id}`, `/users/explore` |
| 소셜 | 10개 | `/users/{id}/follow`, `/users/{id}/mate-request`, `/mate-requests/{id}/respond` |
| 채팅 | 11개 | `/chat-rooms`, `/chat-rooms/{id}/messages`, `/chat-rooms/{id}/invites` |
| AI 챗봇 | 7개 | `/chatbots`, `/chatbots/{id}/chat` |
| 알림 | 4개 | `/notifications`, `/device-tokens` |
| 결제 | 3개 | `/products/clovers`, `/purchases/verify` |
| 신고 | 1개 | `/users/{id}/report` |

실제 운영에서는 이메일 인증, 비밀번호 재설정, 하이브리드 AI 등 추가 엔드포인트를 포함하여 총 83개로 확장되었다.

### Rate Limiting

| 엔드포인트 | 제한 |
|-----------|------|
| 인증 API | 10/분 |
| 일반 API | 100/분 |
| 메시지 전송 | 30/분 |
| AI 채팅 | 20/분 |

응답 헤더: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

### 주요 설계 패턴

1. **커서 기반 페이지네이션**: 메시지 조회에서 `before` 파라미터 + `has_more` 응답
2. **오프셋 기반 페이지네이션**: 목록 조회에서 `page`, `per_page` 파라미터 + `meta.total`
3. **RESTful 리소스 설계**: 관계는 중첩 경로(`/users/{id}/follow`), CRUD는 HTTP 메서드로 표현
4. **비실시간/실시간 분리**: REST 메시지 전송과 WebSocket 실시간 전송 병행

## 관련 문서

- [API 엔드포인트 엔티티](../entities/api-endpoints.md)
- [API 버전 관리](../concepts/api-versioning.md)
- [Pydantic 스키마 설계](../concepts/pydantic-schema-design.md)
