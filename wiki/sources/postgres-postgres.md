---
title: "postgres/postgres — PostgreSQL 본체 GitHub 미러 (★20.7K, ML+미러 거버넌스, 30년 보수파)"
type: source
source_type: article
source_url: "https://github.com/postgres/postgres"
raw_path: "raw/articles/postgres-postgres/"
author: "PostgreSQL Global Development Group (PGDG)"
date_published: 2010-09-21
date_ingested: 2026-04-28
tags: [postgresql, postgres, sql, rdbms, oss, mailing-list-governance, github-mirror, sqlalchemy, c-language, object-relational, transactional, mvcc, fdw, jsonb, replication, pgdg, default-branch-master, no-pull-requests, pgvector, timescaledb]
related:
  - "[[sqlalchemy]]"
  - "[[alembic]]"
  - "[[fastapi]]"
confidence: high
inbound_count: 8
cited_by:
  - "[[append-only-log]]"
  - "[[backend-fastapi-stack]]"
  - "[[postgresql]]"
  - "[[query-optimization]]"
cited_by_count: 4
---

# postgres/postgres — PostgreSQL 본체 GitHub 미러

## 한줄 요약

> 30년차 ★20.7K 객체-관계형 DBMS의 사실상 표준. **GitHub은 미러일 뿐 — 실제 개발은 메일링 리스트(pgsql-hackers)와 자체 git** + 패치 제출은 [postgresql.org/wiki/Submitting_a_Patch](https://wiki.postgresql.org/wiki/Submitting_a_Patch) — Pull Request를 받지 않는 보수적 거버넌스. 본 위키에서 처음 다루는 **"OSS 거버넌스의 정반대 극단"** 사례 (메일링 리스트 + 1980년대식 패치 워크플로우 + 30년 안정성).

## 메타

- **Repository**: postgres/postgres (GitHub 미러)
- **별점/포크**: ★20,739 / fork 5,598 (수집일 2026-04-28 기준)
- **라이선스**: PostgreSQL License (BSD/MIT 호환, NOASSERTION으로 표시)
- **언어**: C
- **Python 패키지**: `psycopg` / `asyncpg` (드라이버, 본 저장소 외부)
- **창설일**: 1986 (UC Berkeley POSTGRES 프로젝트), GitHub 미러 2010-09-21
- **최종 push**: 2026-04-27
- **저장소 크기**: 735 MB
- **default branch**: `master`
- **공식 사이트**: [postgresql.org](https://www.postgresql.org)
- **문서**: [postgresql.org/docs](https://www.postgresql.org/docs/)
- **개발 ML**: pgsql-hackers / pgsql-general / pgsql-announce 등

## raw 파일 구조 (보관 6개 파일, 약 24KB)

```
raw/articles/postgres-postgres/
├── README.md (1KB) — 단순 안내 (실제 docs는 외부)
├── COPYRIGHT (1.2KB) — PostgreSQL License (BSD-style)
├── HISTORY_head100 (277B) — 외부 사이트 안내
├── doc_TODO_head50 — 향후 계획 일부
├── doc_MISSING_FEATURES — 명시 미지원 기능
└── doc_KNOWN_BUGS — 알려진 버그
```

**제외**: `src/` C 본체 (수백 MB), `doc/src/sgml/` 모든 SGML 문서 (방대), `contrib/` 확장, `config/`, `meson.build` 등 빌드 시스템.

**미러 한계**: GitHub 저장소 자체는 단순 미러로 이슈/PR을 받지 않음. 실제 운영 자료는 메일링 리스트 아카이브 / [wiki.postgresql.org](https://wiki.postgresql.org) / 공식 docs — 별도 회차로 분리 수집 후보.

## 핵심 내용

### 1. PostgreSQL 본체 = 1986년 Berkeley POSTGRES → 30년+ 진화

- **1986**: UC Berkeley Michael Stonebraker 교수 POSTGRES 프로젝트
- **1996**: SQL 지원 추가 → "PostgreSQL"로 이름 변경
- **1997~**: PostgreSQL Global Development Group (PGDG) 자체 개발
- **2026 (현재)**: PostgreSQL 17 (안정), 18 개발 중

30년+ 안정 진화로 OLTP 표준 자리. [[scikit-learn]] (19년) / [[sqlalchemy]] (21년)보다도 더 긴 역사.

### 2. GitHub 미러 정책 — "Pull Request 받지 않음"

저장소 description 명시:

> "Mirror of the official PostgreSQL GIT repository. Note that this is just a *mirror* - we don't work with pull requests on github. To contribute, please see https://wiki.postgresql.org/wiki/Submitting_a_Patch"

**현대 OSS 표준과 정반대 — Pull Request를 받지 않는다**:

- 패치 제출: 메일링 리스트 (pgsql-hackers)에 .patch 파일 첨부
- 리뷰: 메일 스레드에서 진행
- 머지: 커미터가 자체 git에 push → GitHub은 자동 미러
- 이슈 추적: 메일 스레드 + commitfest.postgresql.org

이는 anthropics/skills(3회차) 표준 정의 → openai-agents-python(14회차) 9개 SOP 스킬 같은 **"agent-skills 진화"의 정반대 극단** — PostgreSQL은 Linux 커널과 함께 **메일링 리스트 거버넌스의 보수파**.

### 3. PostgreSQL의 OSS 거버넌스 모델 (보수파 사례)

| 특징 | 보수파 (PostgreSQL / Linux Kernel) | 모던파 (anthropics-skills / openai-agents-python) |
|------|------|------|
| 패치 제출 | 메일링 리스트 + .patch 파일 | GitHub PR |
| 리뷰 | 메일 스레드 | GitHub UI |
| 이슈 추적 | 메일 스레드 + commitfest | GitHub Issues |
| 거버넌스 문서 | wiki.postgresql.org | AGENTS.md / SKILL.md |
| 결정 | Core Team (소수) + 메일링 합의 | BDFL / RFC / Constitution |
| 변화 속도 | 느림 (1년에 1 메이저) | 빠름 (월 1 메이저 가능) |
| 안정성 | 30년 | 1~5년 |

**둘 다 유효한 모델** — 도메인 특성에 따라 선택. 데이터베이스처럼 **다운타임 0 + 데이터 손실 0**이 절대 우선이면 보수파가 합리. AI 라이브러리처럼 빠른 진화가 우선이면 모던파가 합리.

### 4. PostgreSQL의 결정적 기능들 (위키 누적 라이브러리와의 연결)

- **MVCC** (Multi-Version Concurrency Control) — 읽기/쓰기 동시 락 없음
- **Transactional DDL** — Alembic Offline 모드의 핵심 (15회차)
- **JSONB** — 인덱싱 가능한 JSON, c2spf 게임 데이터 raw event 저장
- **Foreign Data Wrappers (FDW)** — postgres_fdw로 다른 PG / file_fdw / mysql_fdw 등 외부 데이터 join 가능
- **Logical Replication** — 게임 출시 시 read replica 자동 동기화
- **Window Functions / CTE** — 복잡한 분석 쿼리 (BigQuery보다 먼저 지원)
- **확장 시스템** — TimescaleDB / PostGIS / pgvector / pg_partman 등 50+ 확장

특히 **pgvector** 확장은 LLM RAG에 PostgreSQL을 직접 사용 가능하게 함 → 위키 누적 [[ml-ai]] 개념 페이지에 영향.

### 5. PostgreSQL License = BSD-style (PGDG 자체 라이선스)

`COPYRIGHT` 파일이 BSD 2-clause와 사실상 동일한 PGDG 자체 라이선스. **상업적 fork 자유** — 그래서 AWS RDS / Azure Database / Aiven / Supabase / Neon 등 클라우드 사업자가 모두 PostgreSQL을 자유롭게 fork.

### 6. 미러의 가치 — 코드 레퍼런스 + grep + git blame

GitHub 미러는 PR을 안 받지만 **다음 용도로는 매우 유용**:

- 코드 검색 (`gh search code --repo postgres/postgres`)
- 특정 함수/매크로 위치 파악
- git blame으로 히스토리 추적
- C 본체 학습
- 컨트리뷰터 통계

### 7. 본 위키의 PostgreSQL 통합 위치

[[fastapi]](9회차) 백엔드 → [[sqlalchemy]](본 회차)/[[alembic]](본 회차) → **PostgreSQL** 의 4단 스택:

```
FastAPI 엔드포인트
  ↓ (DI: Annotated[AsyncSession, Depends(get_db)])
SQLAlchemy ORM (Identity Map / Unit of Work)
  ↓ (asyncpg dialect)
PostgreSQL (MVCC / JSONB / FDW)
  ↑ (Alembic 마이그레이션, autogenerate)
```

c2spf-platform이 PostgreSQL OLTP 기반이라면 이 4단 스택이 완성됨.

## 인사이트

### Insight 1: 위키 첫 "메일링 리스트 거버넌스" 사례

본 위키 누적 거버넌스 사례:

| 모델 | 사례 | 비고 |
|------|------|------|
| BDFL | pandas / scikit-learn / sqlalchemy / fastapi | 1인 의사결정 |
| 표준 + 구현 분리 | anthropics-skills / spec-kit | 표준 정의 회사 + 외부 채택 |
| Core Team + RFC | scikit-learn SLEP / pandas PDEP | 소수 코어 합의 |
| 살아있는 운영 노트 | openai-cookbook / openai-agents-python | AGENTS.md "Recent Learnings" |
| 회사 차원 표준화 | Astral (uv·ruff·ty) | 한 회사 여러 제품 통일 |
| **메일링 리스트 + Core Team** | **PostgreSQL** | **30년 보수파 (본 회차 첫 사례)** |

PostgreSQL은 본 위키에서 처음 박는 **"메일링 리스트 + 본 미러 거버넌스"** 사례. 데이터베이스 같은 안정성 절대 우선 도메인의 모범 사례. 회사 BI 의사결정 시 도구 선택 기준에 **거버넌스 모델 매칭**도 고려.

### Insight 2: PostgreSQL = SQLAlchemy의 first-class 백엔드

[[sqlalchemy]](본 회차) dialect 시스템에서 PostgreSQL은 **레퍼런스 구현** 위치 — `sqlalchemy.dialects.postgresql` 최초 + 가장 풍부, 모든 PostgreSQL 고유 기능 (JSONB / Array / Range / Enum / GIN/GIST 인덱스)이 SQLAlchemy 1급 시민, async dialect (`postgresql+asyncpg`) 가장 안정적.

### Insight 3: pgvector — PostgreSQL의 LLM RAG 확장

`pgvector` 확장은 PostgreSQL을 **벡터 DB로 변환** — `vector(1536)` 타입 (OpenAI embedding 호환), HNSW / IVFFlat 인덱스, 일반 SQL과 함께 사용. 이로 [[ml-ai]] 개념의 RAG 구현 시 별도 벡터 DB(Pinecone/Weaviate/Qdrant) 없이 PostgreSQL만으로 가능.

### Insight 4: PGDG = Linux Foundation 같은 제품 거버넌스

PostgreSQL Global Development Group (PGDG)은 회사가 아니라 **컨센서스 그룹** — Core Team 6명 (2026 기준), 각 메이저 버전 = 1년 사이클 + 5년 LTS, 누구나 commitfest에 패치 제출 가능. 이는 [[numfocus]] 같은 nonprofit과는 또 다른 모델 — **순수 제품 운영 그룹**. 회사 BI 도구 선택 시 **PGDG가 사라질 가능성 ≈ 0**.

### Insight 5: GitHub 미러 = "현대 OSS 도구 친화" + "보수 거버넌스 보존"

PostgreSQL이 GitHub 미러를 두는 이유 — **개발자 친화 + 도구 친화**: gh CLI / git blame / 코드 검색이 GitHub에서만 잘 동작, AI 도구가 GitHub 저장소만 인덱싱. 그러나 패치 제출은 메일링 리스트 → 거버넌스 변경 없이 도구 친화 추가. **거버넌스 변경 vs 도구 친화** 분리 패턴.

### Insight 6: 30년 안정성의 비결 — Core Team 보수성 + 충분한 변화 속도

PostgreSQL은 Linux 커널처럼 **변화는 느리지만 0이 아님** — 1년에 1 메이저 버전 + 매 메이저마다 큰 기능. 30년 안정성의 비결: 메이저 1년 사이클 (예측 가능) + 5년 LTS + breaking change 매우 신중 + C 코어 + 확장 시스템 분리.

### Insight 7: SQL 표준 + PostgreSQL 확장 = 표준 + 사실상 표준

PostgreSQL은 SQL 표준에 가장 충실한 동시에 **표준에 없는 기능을 사실상 표준화** (JSONB / Array / RETURNING / COPY / 정규표현식). [[scikit-learn]] BaseEstimator처럼 **"우리가 만들면 표준이 된다"** 패턴.

## 인용 (raw에서 직접 발췌)

### README.md (전문)

> PostgreSQL Database Management System
>
> This directory contains the source code distribution of the PostgreSQL database management system.
> PostgreSQL is an advanced object-relational database management system that supports an extended subset of the SQL standard, including transactions, foreign keys, subqueries, triggers, user-defined types and functions. This distribution also contains C language bindings.

### COPYRIGHT — PostgreSQL License

> Permission to use, copy, modify, and distribute this software and its documentation for any purpose, without fee, and without a written agreement is hereby granted, provided that the above copyright notice and this paragraph and the following two paragraphs appear in all copies.

### GitHub 저장소 description

> Mirror of the official PostgreSQL GIT repository. Note that this is just a *mirror* - we don't work with pull requests on github.

## 후속 탐구

1. **PostgreSQL 공식 docs (postgresql.org/docs)** — 별도 회차로 핵심 챕터 (Tutorial / Internals / Server Programming) 수집
2. **wiki.postgresql.org** — 개발 거버넌스 / commitfest / submitting patch 워크플로우
3. **pgsql-hackers 메일링 아카이브** — 핵심 결정 분석 (예: JSONB 도입 토론)
4. **pgvector 확장 별도 수집** — LLM RAG 핵심 도구
5. **TimescaleDB 별도 수집** — 시계열 확장 (게임 데이터 BI 직결)
6. **psycopg / asyncpg 드라이버** — Python 측 PostgreSQL 인터페이스
7. **AWS RDS / Aurora / Aiven / Supabase 비교** — 클라우드 PostgreSQL 사업자

## 회사 BI 적용 가설

### 가설 1: c2spf-platform OLTP = PostgreSQL 표준화

게임 결제 / 사용자 / 메타 데이터 = PostgreSQL OLTP. 30년 안정성 + Transactional DDL + JSONB + pgvector. SQLAlchemy + Alembic + FastAPI 4단 스택의 종착지.

### 가설 2: pgvector로 위키 RAG 자체 구현

본 위키 (~93 페이지)를 PostgreSQL + pgvector에 적재 — 페이지 본문 + frontmatter → embedding → vector 컬럼. Claude Code MCP에서 직접 쿼리. 별도 벡터 DB 없이 PostgreSQL 1대로 모든 RAG 가능.

### 가설 3: TimescaleDB로 게임 데이터 시계열 분석

c2spf-analytics가 BigQuery에 의존하지만 시계열 분석은 TimescaleDB (PostgreSQL 확장)도 강력한 대안 — 같은 SQL로 OLAP + OLTP 통합. BigQuery 비용 < TimescaleDB 인프라 비용 비교 검토 가능.

### 가설 4: 메일링 리스트 거버넌스를 c2spf-analytics 자체 운영에 차용

c2spf-analytics 핵심 결정을 GitHub Discussions 대신 사내 메일 스레드 + 정기 리뷰로 — **장기 안정성 우선 도메인은 PostgreSQL 모델 차용 가치**.

## 메모

본 회차는 30년 거버넌스 보수파의 첫 위키 사례. agent-skills 8단계 진화의 모던파와 정반대 극단 — 본 위키 거버넌스 모델 비교에 결정적 한 축 추가. PostgreSQL 본체는 GitHub 미러로는 한계가 있어 **별도 회차로 공식 docs / wiki / pgvector 등 보강 필요**. 본 회차는 "거버넌스 모델 + 위키 통합 위치"를 박는 데 집중.
