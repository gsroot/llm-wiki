---
title: "Async-First"
type: concept
source_count: 2
tags: [async, asyncio, performance, python, fastapi]
related:
  - "../entities/fastapi-app.md"
  - "../entities/postgresql.md"
  - "../concepts/layered-architecture.md"
---

# Async-First

## Definition

모든 I/O 바운드 작업을 비동기(async/await)로 처리하는 설계 원칙이다. 동기 함수 사용을 금지하고, 논블로킹 I/O를 통해 높은 동시 처리량을 확보한다.

## How It Works in Mate Chat

### 백엔드

- **코드 규칙**: 모든 함수에 `async def` 사용 (sync 함수 금지, 외부 라이브러리 제외)
- **DB 연결**: SQLAlchemy asyncio 모드 + asyncpg 드라이버 -> `AsyncSession`
- **HTTP 클라이언트**: httpx (비동기) -- OAuth 토큰 검증 등 외부 API 호출
- **WebSocket**: FastAPI 네이티브 비동기 WebSocket 처리
- **ASGI 서버**: uvicorn

### 프론트엔드 (Flutter/Dart)

- Dart의 `Future`/`async-await` 패턴 활용
- Riverpod의 `AsyncValue`로 비동기 상태 관리
- WebSocket 스트림 기반 실시간 이벤트 처리

## Trade-offs

**장점**:
- 단일 프로세스에서 높은 동시 연결 처리 (WebSocket에 필수)
- I/O 대기 시간 동안 다른 요청 처리 가능
- FastAPI + asyncpg 조합으로 고성능 달성

**단점**:
- CPU 바운드 작업에는 이점 없음 (별도 워커 필요)
- 비동기 코드의 디버깅 복잡성 증가
- WebSocket이 DB 풀 슬롯을 장기 점유하는 문제 발생

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- async 네이티브 프레임워크
- [Layered Architecture](../concepts/layered-architecture.md) -- 모든 계층에 async 적용
