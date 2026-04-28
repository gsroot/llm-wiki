---
title: "Layered Architecture"
type: concept
source_count: 2
tags: [architecture, design-pattern, layered, separation-of-concerns]
related:
  - "../entities/fastapi-app.md"
  - "../concepts/async-first.md"
  - "../sources/12-system-architecture.md"
---

# Layered Architecture

## Definition

시스템을 명확한 책임 경계를 가진 계층으로 분리하는 아키텍처 패턴이다. 각 계층은 하위 계층에만 의존하며, 상위 계층의 존재를 알지 못한다.

## How It Works in Mate Chat

Mate Chat은 4개 시스템 계층과 3개 애플리케이션 내부 계층으로 구성된다.

### 시스템 계층 (외부 -> 내부)

1. **Client Layer**: Flutter 앱 (Dio, WebSocket 클라이언트)
2. **Application Layer**: FastAPI (REST API + WebSocket Server + Service Layer)
3. **Data Layer**: PostgreSQL, Redis, MinIO
4. **External Services**: OpenAI, Google/Apple OAuth

### 애플리케이션 내부 계층

1. **API/Router 계층**: 엔드포인트 정의, 요청 파싱, JWT 검증
2. **Service 계층**: 비즈니스 로직 수행 (15개 서비스 클래스)
3. **Repository 계층**: 데이터 접근 추상화 (6개 리포지토리)

요청 흐름: Router -> Deps (DI) -> Service -> Repository -> DB

### 의존성 주입

FastAPI의 `Depends`를 통해 DB 세션, 현재 사용자, 서비스 인스턴스를 각 엔드포인트에 주입한다.

## Trade-offs

**장점**:
- 관심사 분리로 유지보수 용이
- 계층별 독립 테스트 가능
- 비즈니스 로직(Service)이 인프라(Repository)에서 분리

**단점**:
- 단순 CRUD에도 Service/Repository를 거쳐야 하는 boilerplate
- 계층 간 데이터 변환 오버헤드 (Model <-> Schema)

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 이 패턴의 구현체
- [Async-First](../concepts/async-first.md) -- 모든 계층에 적용된 비동기 원칙
