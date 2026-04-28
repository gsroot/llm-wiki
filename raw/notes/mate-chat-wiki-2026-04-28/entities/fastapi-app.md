---
title: "FastAPI Application"
type: entity
source_count: 3
tags: [backend, python, fastapi, async, rest-api, websocket]
related:
  - "../entities/postgresql.md"
  - "../entities/redis.md"
  - "../entities/minio.md"
  - "../entities/sentry.md"
  - "../concepts/layered-architecture.md"
  - "../concepts/async-first.md"
---

# FastAPI Application

## Overview

Mate Chat의 백엔드 애플리케이션 서버이다. Firebase Cloud Functions를 대체하여 REST API와 WebSocket 실시간 통신을 단일 프레임워크에서 처리한다. Python 3.13 기반이며, uvicorn ASGI 서버 위에서 실행된다.

## Architecture/Structure

```
app/
├── main.py                 # 앱 진입점
├── core/
│   ├── config.py          # pydantic-settings 설정
│   ├── security.py        # JWT, 인증/보안
│   ├── database.py        # AsyncSession, 연결 풀
│   └── rate_limiters.py   # Redis 기반 Rate Limiting
├── api/v1/
│   ├── endpoints/         # 10개 엔드포인트 모듈 (83개 API)
│   ├── router.py          # 라우터 통합
│   └── websocket.py       # WebSocket 엔드포인트
├── models/                # 20개 SQLAlchemy 모델
├── schemas/               # 10개 Pydantic 스키마
├── services/              # 15개 서비스 클래스 (비즈니스 로직)
├── repositories/          # 6개 리포지토리 (데이터 접근)
├── websocket/             # 연결 관리자 + Pub/Sub
└── middleware/            # Rate Limit, Metrics, Logging
```

## Key Details

- **선택 이유**: Python 기반(기존 경험), 비동기 네이티브, 자동 OpenAPI 문서화, Pydantic 통합, WebSocket 지원
- **83개 API 엔드포인트**: auth(13), users(7), social(15), chats(16), websocket(1), chatbots(13), clover(5), notifications(5), uploads(1), dev(2)
- **의존성 주입**: FastAPI Depends를 통해 DB 세션, 현재 사용자, 서비스 인스턴스 주입
- **미들웨어 체인**: Rate Limiting -> Metrics -> Logging -> 요청 처리
- **API 문서**: Swagger UI (`/docs`), ReDoc (`/redoc`) 자동 생성

## Dependencies

- **런타임**: Python 3.13+, uvicorn
- **ORM**: SQLAlchemy 2.0 (async) + asyncpg
- **검증**: Pydantic v2
- **인증**: python-jose (JWT), passlib (bcrypt)
- **HTTP 클라이언트**: httpx (OAuth 검증용)
- **AI**: OpenAI SDK
- **로깅**: structlog
- **모니터링**: Sentry SDK
- **패키지 관리**: uv (pip 사용 금지)

## Known Issues

- WebSocket 연결이 DB 풀 슬롯을 연결 수명 동안 점유 (pool_size 주의 필요)
- Apple OAuth 미구현 (iOS 출시 시 필요)
- Redis Pub/Sub 분산 배포 미구현 (단일 서버에서만 동작)

## Related

- [PostgreSQL](../entities/postgresql.md) -- 주 데이터 저장소
- [Redis](../entities/redis.md) -- 캐시, Rate Limiting, Pub/Sub
- [MinIO](../entities/minio.md) -- 파일 저장소
- [Docker Infrastructure](../entities/docker-infrastructure.md) -- 컨테이너 배포
- [Sentry](../entities/sentry.md) -- 에러 추적 및 APM
- [Layered Architecture](../concepts/layered-architecture.md) -- 계층 구조 패턴
