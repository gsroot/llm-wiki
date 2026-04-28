---
title: "Repository 패턴"
type: concept
source_count: 2
tags: [pattern, architecture, data-access, sqlalchemy]
related:
  - ../entities/database-schema.md
  - ../entities/api-endpoints.md
  - ../concepts/pydantic-schema-design.md
---

# Repository 패턴

## Definition

Repository 패턴은 데이터 접근 로직을 비즈니스 로직으로부터 분리하는 설계 패턴이다. 데이터 저장소(데이터베이스, API, 파일 등)에 대한 접근을 일관된 인터페이스 뒤에 캡슐화하여, 비즈니스 로직이 저장소의 구체적인 구현에 의존하지 않도록 한다.

## How It Works in Mate Chat

Mate Chat 백엔드는 3계층 아키텍처를 사용한다:

```
Endpoint (Controller)
    │
    ▼
Service (비즈니스 로직)
    │
    ▼
Repository (데이터 접근)
    │
    ▼
SQLAlchemy AsyncSession → PostgreSQL
```

### 백엔드 구현

- **Repository 계층** (`app/repositories/`, 6개 파일): SQLAlchemy를 사용한 CRUD 연산 캡슐화
- **Service 계층** (`app/services/`, 15개 파일): 비즈니스 규칙 적용, 복수 Repository 조합
- **Endpoint 계층** (`app/api/v1/endpoints/`): HTTP 요청 처리, FastAPI Depends로 의존성 주입

### Flutter 구현

Flutter 앱에서도 동일한 패턴을 적용한다:

- **Repository 계층** (`lib/repositories/`, 7개 파일): Dio HTTP 클라이언트를 통한 API 호출 캡슐화
- **Provider/Notifier** (Riverpod): 상태 관리 및 비즈니스 로직
- **Widget**: UI 표현

### 의존성 주입

백엔드에서 FastAPI의 `Depends`를 활용하여 Repository와 Service를 주입한다:

```python
# Endpoint에서 Service 주입
async def create_chat_room(
    data: ChatRoomCreate,
    service: ChatService = Depends(get_chat_service),
    current_user: User = Depends(get_current_user)
) -> ChatRoomResponse:
    return await service.create_room(data, current_user)
```

## Trade-offs

### 장점

- **테스트 용이성**: Repository를 mock으로 교체하여 Service 단위 테스트 가능
- **관심사 분리**: SQL 쿼리 변경이 비즈니스 로직에 영향 없음
- **일관된 인터페이스**: 프론트엔드/백엔드 모두 동일한 패턴으로 데이터 접근
- **Firestore -> PostgreSQL 전환 용이**: Repository 계층만 교체하여 마이그레이션 수행

### 단점

- **보일러플레이트 증가**: 단순 CRUD에도 Repository-Service-Endpoint 3개 파일 필요
- **간접 참조 비용**: 단순 쿼리에서도 여러 계층을 거침
- **과도한 추상화 위험**: 6개 Repository로 20개 테이블을 관리하므로, 일부 Repository가 비대해질 수 있음

## Related

- [데이터베이스 스키마](../entities/database-schema.md) -- Repository가 접근하는 테이블
- [API 엔드포인트](../entities/api-endpoints.md) -- Repository를 사용하는 API
- [Pydantic 스키마 설계](../concepts/pydantic-schema-design.md) -- Repository 입출력 타입
