---
title: "Pydantic 스키마 설계"
type: concept
source_count: 2
tags: [pydantic, validation, schema, fastapi, serialization]
related:
  - ../entities/api-endpoints.md
  - ../entities/database-schema.md
  - ../concepts/repository-pattern.md
---

# Pydantic 스키마 설계

## Definition

Pydantic 스키마는 FastAPI에서 요청(Request) 및 응답(Response) 데이터의 구조와 유효성을 선언적으로 정의하는 데이터 모델이다. 런타임에 자동으로 타입 검증, 직렬화/역직렬화를 수행하며, OpenAPI 문서를 자동 생성한다.

## How It Works in Mate Chat

### 스키마 구조

`app/schemas/` 디렉토리에 10개의 Pydantic 스키마 파일이 존재하며, 도메인별로 분리되어 있다.

### 요청/응답 분리 패턴

각 도메인에서 목적별로 스키마를 분리한다:

- **Create 스키마**: 생성 요청 (예: `ChatRoomCreate`)
- **Update 스키마**: 수정 요청, Optional 필드 (예: `UserUpdate`)
- **Response 스키마**: API 응답 (예: `UserResponse`, `ChatMessageResponse`)

### 응답 엔벨로프

모든 API 응답은 일관된 엔벨로프 형식을 따른다:

```python
# 단건 응답
{ "data": { ... } }

# 목록 응답 (페이지네이션 포함)
{ "data": [...], "meta": { "page": 1, "per_page": 20, "total": 100 } }

# 에러 응답
{ "error": { "code": "...", "message": "...", "details": [...] } }
```

### 유효성 검증 사례

API 설계 문서에서 확인되는 검증 규칙:

- **이메일**: 형식 검증 (`Invalid email format`)
- **프로필 이미지**: 최대 5MB, jpg/png만 허용
- **페이지네이션**: `per_page` 최대 100
- **메시지**: `limit` 최대 100
- **gender**: male/female/other만 허용
- **profile_visibility**: everyone/mates/only_me만 허용

### Pydantic과 SQLAlchemy 모델 관계

```
SQLAlchemy Model (DB 계층)
    ↕ 변환
Pydantic Schema (API 계층)
```

SQLAlchemy 모델은 데이터베이스 테이블을 표현하고, Pydantic 스키마는 API 입출력을 표현한다. Repository 계층에서 SQLAlchemy 모델을 Pydantic 스키마로 변환한다.

## Trade-offs

### 장점

- **자동 검증**: 잘못된 요청을 422 응답으로 즉시 거부
- **자동 문서화**: Swagger/ReDoc에 스키마가 자동 반영
- **타입 안전성**: IDE 자동완성과 mypy 타입 체크 지원
- **직렬화 제어**: 응답에서 민감한 필드(password_hash 등) 제외 가능

### 단점

- **이중 모델 관리**: SQLAlchemy 모델과 Pydantic 스키마를 별도 유지
- **변환 비용**: 매 요청마다 직렬화/역직렬화 수행
- **스키마 폭발**: Create/Update/Response 등 목적별 스키마가 많아짐 (10개 파일)

## Related

- [API 엔드포인트](../entities/api-endpoints.md) -- 스키마를 사용하는 API
- [데이터베이스 스키마](../entities/database-schema.md) -- Pydantic과 매핑되는 DB 모델
- [Repository 패턴](../concepts/repository-pattern.md) -- 스키마 변환이 일어나는 계층
