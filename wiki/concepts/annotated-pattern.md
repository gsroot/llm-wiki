---
title: Annotated 패턴 (PEP 593) — Type-First Python의 단일 표현
aliases:
- Annotated
- PEP 593
- annotated-pattern
- Annotated 패턴
- Type Hints with Metadata
type: concept
category: backend
tags:
- annotated-pattern
- pep-593
- python
- type-hints
- pydantic
- fastapi
- sqlalchemy
- typer
- 백엔드
- type-first-python
related:
- '[[backend-python-fastapi]]'
- '[[python-packaging]]'
- '[[fastapi]]'
- '[[pydantic]]'
- '[[sqlalchemy]]'
- '[[fastapi-fastapi]]'
- '[[pydantic-pydantic]]'
- '[[sqlalchemy-sqlalchemy]]'
- '[[postgres-postgres]]'
- '[[backend-fastapi-stack]]'
- '[[c2spf-analytics]]'
- '[[matechat]]'
source_count: 4
created: 2026-04-30
updated: 2026-04-30
cited_by_count: 4
---

# Annotated 패턴 (PEP 593) — Type-First Python의 단일 표현

## 정의

**`typing.Annotated[T, metadata...]`** 는 Python의 타입 힌트에 **임의 메타데이터를 함께 박는 표준 메커니즘**. PEP 593 (Python 3.9+, 2020)로 정식 채택되어 2024~2026년에 들어 [[fastapi]]·[[pydantic]]·[[sqlalchemy]]·Typer·Strawberry GraphQL 등 주요 type-first Python 라이브러리의 1급 시그니처 표현이 됐다.

핵심 발상: 함수 시그니처의 **타입 정보 + 검증 규칙 + 라우팅 메타 + 직렬화 옵션**을 하나의 위치에 응축. 호출 인자의 디폴트값을 라이브러리 sentinel(`Query(...)`, `Path(...)` 등)으로 채우는 기존 패턴을 대체한다.

## 왜 중요한가

### owner 입장에서

- **[[c2spf-analytics]]**: FastAPI 기반 BI API의 모든 엔드포인트가 `Annotated`로 통일되면 (a) 함수 시그니처를 다른 컨텍스트(테스트, 문서)에서 재사용 가능, (b) Pydantic V2 Rust 직렬화 + SQLAlchemy 2.x ORM이 같은 `Annotated` 자산을 공유.
- **[[matechat]]**: API 응답 모델을 Pydantic V2 `Annotated[T, Field(...)]` 로 정형화 → OpenAPI 스키마 자동 생성 → 클라이언트(Flutter) 코드 자동 생성.

### 산업 전반

`Annotated`는 PEP 593 채택 후 **type-first Python의 사실상 표준**으로 정착. FastAPI v0.95 (2023) 이후 공식 권장, Pydantic V2 (2023) 이후 1급 지원, SQLAlchemy 2.0 (2023) 이후 ORM 매핑 통합. 현재 `def name(x: Annotated[T, M])` 가 **하나의 시그니처에 5개 도메인 메타(검증·라우팅·직렬화·문서·DB)를 박는 표준 위치**.

## 핵심 내용

### 기본 구조

```python
from typing import Annotated
from fastapi import Query

# Before (PEP 593 이전): 디폴트값에 sentinel
def search(q: str = Query(..., min_length=3)): ...

# After (PEP 593): Annotated 첫 인자가 타입, 나머지는 메타
def search(q: Annotated[str, Query(min_length=3)]): ...
```

차이는 미묘하지만 결정적: **첫 형식은 디폴트값 슬롯을 점령** (=다른 의미로 못 씀, 테스트에서 mock하면 의미 깨짐), **두 번째는 디폴트값 슬롯이 비어있어** 함수 시그니처가 순수 Python 의미 보존.

### 5개 라이브러리 채택 매트릭스

| 라이브러리 | `Annotated` 사용처 | 메타데이터 |
|---|---|---|
| **[[fastapi]]** | 라우트 함수 인자 | `Query`, `Path`, `Header`, `Cookie`, `Body`, `File`, `Depends` |
| **[[pydantic]]** | 필드 정의 | `Field(min_length=, ge=, le=, ...)`, `BeforeValidator`, `AfterValidator`, `Discriminator` |
| **[[sqlalchemy]]** (2.x ORM) | `Mapped[T]` 컬럼 | `mapped_column(...)`, `ForeignKey`, custom annotations |
| **Typer** | CLI 인자 | `Option`, `Argument`, `Help` |
| **Strawberry GraphQL** | 리졸버 인자 | `Strawberry.Field`, custom permissions |

→ 5개가 **모두 같은 메커니즘 (typing.Annotated)** 으로 도메인별 메타를 박음. 한 라이브러리의 사용 패턴을 익히면 다른 4개에 즉시 전이 가능.

### Combined `Annotated` (한 인자에 여러 라이브러리 메타 동시 박기)

```python
from typing import Annotated
from fastapi import Query
from pydantic import Field

def search(
    q: Annotated[
        str,
        Query(description="검색어"),  # FastAPI 라우팅 메타
        Field(min_length=3, max_length=100)  # Pydantic 검증 메타
    ]
): ...
```

`Annotated[T, M1, M2, M3]` 는 **타입 + 임의 N개 메타**를 받음. 라이브러리들은 자기 메타만 골라 처리하므로 충돌 없이 누적 가능.

### `RootModel` 회피 패턴

[[fastapi-fastapi]]의 공식 SKILL.md가 박은 권장:

```python
# Before: Pydantic RootModel
from pydantic import RootModel
class TagList(RootModel[list[str]]): ...

# After: Annotated + Body
from typing import Annotated
from fastapi import Body
async def create(tags: Annotated[list[str], Body(min_length=1)]): ...
```

`RootModel` 같은 wrapper 클래스를 만들 필요 없이 `Annotated` 한 줄로 해결. 코드 양 50% 감소.

### Pydantic V2의 `BeforeValidator` / `AfterValidator`

```python
from typing import Annotated
from pydantic import BaseModel, BeforeValidator

def lowercase(v: str) -> str:
    return v.lower()

class User(BaseModel):
    email: Annotated[str, BeforeValidator(lowercase)]
```

검증 함수를 타입 힌트에 직접 박음. **타입과 검증이 한 위치**, 별도 `@validator` 데코레이터 불필요.

### SQLAlchemy 2.x ORM 매핑

```python
from typing import Annotated
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String

# 재사용 가능한 type alias
str_30 = Annotated[str, mapped_column(String(30))]

class User(DeclarativeBase):
    name: Mapped[str_30]  # String(30) 컬럼 자동 매핑
    email: Mapped[str_30]  # 같은 alias 재사용
```

타입 alias로 **컬럼 정의 패턴을 재사용**. 30 char string이 100군데 등장해도 한 줄 정의.

## 안티패턴

| 안티패턴 | 문제 | 회피 |
|---|---|---|
| 디폴트값 sentinel 패턴 (`q: str = Query(...)`) 사용 | 함수 시그니처가 라이브러리 종속, 테스트·재사용 시 의미 깨짐 | `Annotated[str, Query(...)]` 로 마이그레이션 |
| `Annotated` 안에 lambda 박기 | 타입 체커가 lambda 추론 어려움 | 명명된 함수 사용 (`BeforeValidator(lowercase)`) |
| `Annotated[T]` 단일 인자 | 메타가 없으면 `Annotated`를 쓰는 의미 없음 | 메타가 정말 없으면 그냥 `T` |
| 같은 `Annotated[T, M]` 패턴을 100군데 복붙 | DRY 위반 | type alias로 재사용 (`UserName = Annotated[str, ...]`) |
| `RootModel` 사용 | 클래스 wrapper 비용 | `Annotated[list[T], Body(...)]` |

## owner 활용 시나리오

### [[c2spf-analytics]] FastAPI 마이그레이션

기존 `def search(q: str = Query(..., min_length=3))` → `def search(q: Annotated[str, Query(min_length=3)])` 일괄 변환. ROI:
- 함수 시그니처 의미 보존 (테스트에서 mock 가능)
- Pydantic V2 검증 + FastAPI 라우팅 + Strawberry GraphQL 미래 도입 시 같은 자산 재사용
- type checker(pyright/mypy) 호환성 향상

### [[matechat]] API 모델 표준화

Flutter 클라이언트가 받는 모든 응답 모델을 `Annotated[T, Field(...)]` 로 정형화. OpenAPI 스키마 자동 생성 → Dart 코드 자동 생성 (openapi-generator).

### type alias 라이브러리 사내 표준화

```python
# common/types.py
KoreanString = Annotated[str, Field(pattern=r"[가-힣]+")]
EmailStr = Annotated[str, BeforeValidator(lowercase), Field(pattern=email_regex)]
PositiveInt = Annotated[int, Field(gt=0)]
```

회사 BI에서 100+ 모델이 같은 도메인 타입을 공유 → 한 줄 정의로 일관성.

## 관련 개념

- [[backend-python-fastapi]] — `Annotated` 강제는 FastAPI 권장 5대 컨벤션 중 하나. 본 페이지가 그 패턴의 단일 진실원.
- [[python-packaging]] — PEP 593 + PEP 723 등 Python 표준화 노력의 일부. PEP는 별도 거버넌스 (CPython BDFL → Steering Council).
- [[harness]] — type-first 패턴은 LLM 에이전트의 도구 시그니처 정의에도 적용 (function calling JSON schema 자동 생성).

## 출처

- [[fastapi-fastapi]] — `.agents/skills/fastapi/SKILL.md` 가 `Annotated[T, Path/Query/Depends(...)]` 강제. 디폴트 인자 패턴 금지 명시. 5대 코딩 컨벤션 중 1번.
- [[pydantic-pydantic]] — V2 (2023~) 1급 지원. `Field`, `BeforeValidator`, `AfterValidator`, `Discriminator` 모두 `Annotated` 메타. PEP 727 (annotation-based types)에 영향.
- [[sqlalchemy-sqlalchemy]] — 2.x ORM에서 `Mapped[Annotated[T, mapped_column(...)]]` 매핑. type alias 재사용 패턴.
- [[postgres-postgres]] — c2spf-platform OLTP 대상. SQLAlchemy + Alembic + FastAPI 4단 스택의 종착지에서 `Annotated` 통일이 완성됨.

## 열린 질문

- **PEP 727** (annotation-based types) 진행 상황. Pydantic이 표준화에 미친 영향이 어디까지 갈지.
- **Strawberry GraphQL** vs FastAPI: GraphQL 도입 시 `Annotated` 메타가 Field/Resolver 양쪽에서 호환될지.
- **Pydantic V1 → V2 마이그레이션**: 회사 BI에 V1 잔존 코드가 있다면 `Annotated` 도입 비용 vs 효익 비교.
- **`Annotated` 메타가 너무 많아질 때** (3+ 라이브러리 동시 사용) 가독성이 무너지는 임계점은?
