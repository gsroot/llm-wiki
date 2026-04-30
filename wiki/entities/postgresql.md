---
title: PostgreSQL
aliases:
- PostgreSQL
- 포스트그레스
- 포스트그레SQL
- postgres
type: entity
entity_type: tool
tags:
- postgresql
- postgres
- sql
- rdbms
- oss
- mailing-list-governance
- github-mirror
- sqlalchemy
- c-language
- object-relational
- transactional
- mvcc
- fdw
- jsonb
- replication
- pgdg
- pgvector
- timescaledb
- no-pull-requests
related:
- '[[sqlalchemy]]'
- '[[alembic]]'
- '[[fastapi]]'
- '[[python-packaging]]'
- '[[postgres-postgres]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 19
inbound_count: 77
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 29
---

# PostgreSQL

## 개요

30년차 (1986~) 객체-관계형 DBMS 사실상 표준 OLTP. **MVCC + Transactional DDL + JSONB + 50+ 확장 시스템 + BSD-style 라이선스**로 안정성·기능·자유 3박자. PostgreSQL Global Development Group (PGDG) 컨센서스 거버넌스. **본 위키 첫 "메일링 리스트 + GitHub 미러" 보수파 거버넌스** 사례 — Pull Request 받지 않음, 패치는 pgsql-hackers 메일링 리스트로 제출.

## 메타

- **공식 사이트**: [postgresql.org](https://www.postgresql.org)
- **GitHub 미러**: [postgres/postgres](https://github.com/postgres/postgres) (★20.7K, fork 5.6K)
- **라이선스**: PostgreSQL License (BSD/MIT 호환)
- **언어**: C
- **창설**: 1986 (UC Berkeley POSTGRES, Michael Stonebraker), GitHub 미러 2010-09-21
- **현재 버전**: PostgreSQL 17 (안정), 18 개발 중
- **거버넌스**: PGDG Core Team 6명 + 컨센서스
- **Python 드라이버**: `psycopg` / `asyncpg`

## 주요 특징

### 1. MVCC (Multi-Version Concurrency Control)

읽기/쓰기 동시 락 없음 — 분석 쿼리 실행 중에도 OLTP 정상 동작. 버전 관리로 읽기 일관성 보장.

### 2. Transactional DDL

DDL (CREATE/ALTER/DROP)도 트랜잭션 안에서 실행 가능 → 실패 시 롤백. [[alembic]] Offline 모드의 핵심.

### 3. JSONB

인덱싱 가능한 JSON 타입 — GIN 인덱스 + 연산자 (`->`, `->>`, `?`, `@>`). 회사 BI에서 게임 raw event 저장 + 쿼리 가능. NoSQL을 흡수.

### 4. 확장 시스템 (50+)

- **pgvector** — 벡터 DB (LLM RAG)
- **TimescaleDB** — 시계열 (게임 데이터)
- **PostGIS** — 지리정보
- **pg_partman** — 파티션 자동화
- **pg_stat_statements** — 쿼리 통계
- **citext** — 대소문자 무관 텍스트

확장이 일반 SQL과 함께 사용 가능 — **하나의 PostgreSQL이 여러 도메인 흡수**.

### 5. 메일링 리스트 거버넌스 (보수파)

| 특징 | PostgreSQL |
|------|------|
| 패치 제출 | pgsql-hackers ML + .patch 첨부 |
| 리뷰 | 메일 스레드 |
| 이슈 추적 | commitfest.postgresql.org |
| 거버넌스 문서 | wiki.postgresql.org |
| 결정 | Core Team + 컨센서스 |

GitHub은 단순 미러 — PR 받지 않음. **agent-skills 모던파의 정반대 극단**.

### 6. PostgreSQL License (BSD-style)

상업적 fork 자유 → AWS RDS / Azure Database / Aiven / Supabase / Neon 모두 PostgreSQL fork. [[redis]] 2024 라이선스 변경과 정반대 — **30년 라이선스 안정**.

### 7. SQL 표준 + 사실상 표준 확장

표준에 없지만 PostgreSQL이 정착시킨 기능 — JSONB / Array / RETURNING / COPY / 정규표현식. MySQL 8.0이 RETURNING 따라옴.

### 8. 1년 메이저 사이클 + 5년 LTS

- 매년 1 메이저 (예측 가능)
- 5년 LTS — 장기 운영 보장
- breaking change 매우 신중

## 관련 개념

- [[python-packaging]]: psycopg / asyncpg 드라이버

## 관련 엔티티

- [[sqlalchemy]]: 1순위 dialect (가장 풍부한 기능 노출)
- [[alembic]]: Transactional DDL 1급 활용
- [[fastapi]]: 백엔드 4단 스택의 DB 계층

## 의사결정 컨텍스트 (raw 인용)

> "30년차 ★20.7K 객체-관계형 DBMS의 사실상 표준. GitHub은 미러일 뿐 — 실제 개발은 메일링 리스트(pgsql-hackers)와 자체 git + 패치 제출은 Pull Request를 받지 않는 보수적 거버넌스. 본 위키에서 처음 다루는 'OSS 거버넌스의 정반대 극단' 사례 (메일링 리스트 + 1980년대식 패치 워크플로우 + 30년 안정성)."
> — [[postgres-postgres]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 백엔드 5단([[fastapi]] + [[pydantic]] + [[sqlalchemy]] + [[alembic]] + postgresql + [[redis]])의 데이터베이스 본진. [[matechat|MateChat 사이드 프로젝트]]·[[c2spf-analytics|c2spf 게임 데이터 BI]] 양쪽 채택. **메일링 리스트 거버넌스 + Pull Request 부재**는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 OSS 거버넌스 카탈로그 중 가장 보수적 모델 — [[bdfl]]·NumFOCUS·Astral 회사 표준화·CNCF 등과 함께 거버넌스 다양성을 보여주는 극단 사례.

## 출처

- [[postgres-postgres]] — GitHub 미러 1차 수집

## 메모

- 본 위키 첫 "메일링 리스트 거버넌스" 사례 — agent-skills 모던파 비교 축
- PostgreSQL 본체 = GitHub 미러 한계 → 공식 docs / wiki / pgvector / TimescaleDB 보강 필요
- pgvector로 본 위키 자체 RAG 구현 PoC 가능 (별도 벡터 DB 없이)
- c2spf-platform OLTP 표준화 — 30년 안정성 + JSONB + Transactional DDL + pgvector
- 라이선스 변경 위험 0 (30년 BSD-style 유지) — Redis 2024 사례와 대조
