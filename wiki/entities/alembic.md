---
title: "Alembic (sqlalchemy/alembic)"
type: entity
entity_type: tool
tags: [alembic, migration, sqlalchemy, python, ddl, transactional-ddl, autogenerate, branch-merging, sql-script-output, batch-migration, sqlite-batch, mike-bayer, postgresql, mysql, sqlite, oracle, mssql, offline-migration, cookbook]
related:
  - "[[sqlalchemy]]"
  - "[[postgresql]]"
  - "[[fastapi]]"
  - "[[python-packaging]]"
  - "[[uv]]"
  - "[[sqlalchemy-alembic]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 8
inbound_count: 29
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 12
---

# Alembic (sqlalchemy/alembic)

## 개요

[[sqlalchemy]] 진영 사실상 표준 마이그레이션 도구 (★4.1K, Mike Bayer 동일 BDFL). **`--autogenerate`로 모델-DB 차분 자동 검출 → 후보 마이그레이션 생성** + **transactional DDL** + **SQL 스크립트 출력 (오프라인 모드)** + **branch merging (Git 머지 모델)**. corporate 환경 (DBA 권한 분리) ↔ 자동화 양립.

## 메타

- **저장소**: https://github.com/sqlalchemy/alembic
- **PyPI**: `alembic`
- **라이선스**: MIT
- **언어**: Python
- **창설**: 2018-11-27 (GitHub 미러)
- **별점/포크**: ★4,099 / fork 330
- **저장소 크기**: 4.6 MB

## 주요 특징

### 1. 5가지 핵심 기능

1. ALTER 문 발행
2. upgrade/downgrade 양방향 스크립트
3. Sequential 실행 + DAG 구조
4. Transactional DDL (PostgreSQL / MSSQL)
5. Minimalist 스크립트 (`alter_column()`, `rename_table()`, ...)

### 2. `--autogenerate` — 모델-DB 차분 자동

[[sqlalchemy]] `MetaData.reflect()`를 정면 활용 — 현재 DB ↔ Python 모델 비교 → 차분 → 마이그레이션 코드 자동 생성. 초벌 후 개발자 수정 필수, 그러나 grunt work 0.

### 3. Offline Mode — DBA 권한 분리 환경 대응

```
alembic upgrade head --sql > migration.sql
```

DBA가 SQL 텍스트 검토 → 프로덕션 적용. **corporate 환경** 핵심 기능. 회사 BI c2spf-platform 결제 DB 마이그레이션 직접 적용 가능.

### 4. Branch Merging — DAG 모델

- `alembic branches` — 현재 HEAD 분기
- `alembic merge <branches>` — 빈 머지 마이그레이션 생성
- `down_revision` 튜플로 다중 부모

Git 머지와 동일 모형. 다중 개발자 동시 마이그레이션 충돌 자동 해결.

### 5. SQLite Batch — ALTER 미지원 우회

`with op.batch_alter_table('users'):`로 임시 테이블 → 데이터 복사 → 원본 삭제 → 이름 변경 자동화.

### 6. Cookbook — 실전 패턴

`docs/cookbook.rst` — 데이터 마이그레이션 / 동적 환경 변수 / multi-database / 마이그레이션 체이닝 등 실전 코드. [[openai-cookbook]] cookbook 패턴의 마이그레이션 도메인 적용.

### 7. env.py = SQLAlchemy 환경과 1:1 매핑

`alembic init` → `env.py` + `alembic.ini` + 마이그레이션 폴더. `env.py`가 SQLAlchemy 엔진 + 메타 연결 → autogenerate 가능 이유.

## 관련 개념

- [[python-packaging]]: PyPI 표준 패키지

## 관련 엔티티

- [[sqlalchemy]]: 자매 도구 (Mike Bayer 동일 BDFL), MetaData reflect 활용
- [[postgresql]]: Transactional DDL 1급 지원

## 의사결정 컨텍스트 (raw 인용)

> "SQLAlchemy 진영의 사실상 표준 마이그레이션 도구 (★4.1K, Mike Bayer 작성). --autogenerate로 모델-DB 차분 자동 검출 → 후보 마이그레이션 생성 + transactional DDL + SQL 스크립트 출력(오프라인 모드) + branch merging으로 corporate 환경(DBA 권한 분리) ↔ 자동화 모두 대응."
> — [[sqlalchemy-alembic]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 백엔드 5단([[fastapi]] + [[pydantic]] + [[sqlalchemy]] + alembic + [[postgresql]] + [[redis]])의 마이그레이션 축. [[matechat|MateChat 사이드 프로젝트]] backend 실제 채택 + [[c2spf-analytics|c2spf 게임 데이터 BI]] 후보. **transactional DDL + branch merging**이 multi-환경 운영(DBA 권한 분리·CI/CD 통합) 양쪽 시나리오 대응 — [[backend-fastapi-stack]] 종합 분석 참조.

## 출처

- [[sqlalchemy-alembic]] — 본 저장소 1차 수집 (15회차, 2026-04-28)

## 메모

- Offline Mode = corporate 환경 핵심 — c2spf 결제 DB DBA 검토 워크플로우 직접 적용
- Branch DAG = Django Migration보다 먼저 정착
- BigQuery / DuckDB dialect Alembic 통합은 별도 분석 후보
- 회사 BI BigQuery 100+ 테이블 자동 동기화 자체 도구 PoC 가설 (Alembic의 reflection 차분 패턴 차용)
