---
title: "SQLAlchemy (sqlalchemy/sqlalchemy)"
type: entity
entity_type: tool
tags: [sqlalchemy, python, sql, orm, core, unit-of-work, identity-map, data-mapper, declarative, async, sqlmodel, alembic, mike-bayer, postgresql, mysql, sqlite, dialect, dbapi, type-coercion, connection-pool, 2-0-style, annotated-mapped, bdfl]
related:
  - "[[fastapi]]"
  - "[[postgresql]]"
  - "[[alembic]]"
  - "[[pydantic]]"
  - "[[python-packaging]]"
  - "[[uv]]"
  - "[[sqlalchemy-sqlalchemy]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 10
inbound_count: 33
created: 2026-04-28
updated: 2026-04-28
---

# SQLAlchemy (sqlalchemy/sqlalchemy)

## 개요

21년차 ★11.8K Python SQL 툴킷·ORM. **Core (SQL 표현 + DBAPI) / ORM (Identity Map + Unit of Work + Data Mapper) 이중 레이어** 구조로 raw SQL 자유와 객체 ORM 자동화 양립. Mike Bayer (zzzeek) 1인 BDFL 21년 운영. 2.0 (2023) 통합 API + async 1급 시민 + Annotated `Mapped[...]` 매핑 → [[pydantic]] / [[fastapi]]와 단일 타입 체인 통합.

## 메타

- **저장소**: https://github.com/sqlalchemy/sqlalchemy
- **공식 사이트**: [sqlalchemy.org](https://www.sqlalchemy.org)
- **PyPI**: `SQLAlchemy`
- **라이선스**: MIT
- **언어**: Python
- **창설**: 2005~ (실제), 2018-11-27 (GitHub 미러)
- **별점/포크**: ★11,800 / fork 1,677
- **저장소 크기**: 102 MB
- **BDFL**: Mike Bayer (zzzeek)

## 주요 특징

### 1. Core + ORM 이중 레이어

| 레이어 | 역할 |
|--------|------|
| **Core** | SQL 표현 + DBAPI + 스키마 메타 + 커넥션 풀 + 타입 강제 |
| **ORM** | Identity Map + Unit of Work + Data Mapper |

ORM은 옵션 — Core만으로 SQL 빌더 + 타입 안전 가능.

### 2. ORM 패턴 — Identity Map / Unit of Work / Data Mapper

- **Identity Map** — 한 Session 내 동일 PK = 동일 Python 객체
- **Unit of Work** — Session 변경 누적 → flush 시 한 번에 커밋
- **Data Mapper** — 비즈니스 객체와 DB 매핑 분리 (Active Record 반대)

### 3. SQLAlchemy 2.0 unified API + Annotated

```python
class User(Base):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
```

- `select(...)` 통합 API (1.x Query 폐기)
- `AsyncSession` + `AsyncEngine` 1급 시민
- PEP 593 Annotated 채택 → [[pydantic]] V2 / [[fastapi]] DI와 통합

### 4. dialect 시스템

PostgreSQL / MySQL / SQLite / Oracle / MSSQL / **BigQuery / DuckDB / ClickHouse** 등 10+ 백엔드. 새 dialect 작성 가이드 (`README.dialects.rst`). **OLTP + OLAP 같은 코드** 가능.

### 5. composite + natural PK 1급 시민

surrogate (auto-increment id) 외에 (game_id, user_id, date) 같은 composite PK / natural PK 자유. Django ORM과 정반대.

### 6. 21년 BDFL = 일관성

Mike Bayer 21년 1인 lead. NumFOCUS 같은 후원 없이 순수 OSS + 컨설팅. 단점 — 버스 인자 1.

### 7. Database Introspection ↔ Generation 양방향

`MetaData.reflect()`로 현재 DB → 메타, 같은 메타에서 CREATE 문 생성. [[alembic]] autogenerate의 핵심.

### 8. Glossary = 도메인 표준 어휘

`docs/glossary.rst`가 ORM 도메인 용어의 사실상 표준 사전 (Unit of Work / Identity Map / Lazy/Eager Load 등).

## 관련 개념

- [[python-packaging]]: PyPI 표준 패키지
- [[agent-stack-evolution]]: BDFL 1인 거버넌스 모델

## 관련 엔티티

- [[alembic]]: 자매 마이그레이션 도구 (Mike Bayer 동일)
- [[postgresql]]: 1순위 dialect
- [[fastapi]]: 의존성 주입 통합 (`Annotated[AsyncSession, Depends(get_db)]`)
- [[pydantic]]: SQLModel로 통합 가능

## 의사결정 컨텍스트 (raw 인용)

> "21년차 ★11.8K Python SQL 툴킷·ORM. Core(SQL 구성/DBAPI 추상)와 ORM(Unit of Work · Identity Map · Data Mapper) 이중 레이어 구조로 raw SQL 자유와 객체 ORM 자동화를 양립시킨 사실상 표준 — Mike Bayer 1인 BDFL 거버넌스 + Python 표준 진영의 fastapi / SQLModel / alembic와 묶이는 백엔드 표준 의존성."
> — [[sqlalchemy-sqlalchemy]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 백엔드 5단의 ORM 축. [[matechat|MateChat 사이드 프로젝트]] backend + [[c2spf-analytics|c2spf 게임 데이터 BI]] 후보. **Core/ORM 이중 레이어**가 raw SQL 성능 추구와 객체 추상화 생산성 양쪽 시나리오 대응. [[alembic]]과 같은 Mike Bayer 1인 BDFL 거버넌스 — [[postgresql]]의 메일링 리스트 거버넌스와 대비되는 또 다른 보수적 모델.

## 출처

- [[sqlalchemy-sqlalchemy]] — 본 저장소 1차 수집 (15회차, 2026-04-28)

## 메모

- SQLAlchemy + Pydantic + FastAPI = 단일 Annotated 타입 체인 (Type-First Python Backend)
- SQLModel (Tiangolo) 별도 수집 후보 — SQLAlchemy + Pydantic 통합 라이브러리
- 회사 BI 적용 — c2spf 메타 (PostgreSQL ORM) + 분석 (BigQuery Core) 같은 코드로 처리
- Mike Bayer blog (zzzeek.org) 21년 BDFL 인사이트 1차 자료
