---
title: SQLite
type: entity
entity_type: tool
tags:
- sqlite
- sql
- file-format
- 25회차
related:
- '[[postgresql]]'
- '[[duckdb]]'
- '[[redis]]'
- '[[duckdb-duckdb]]'
- '[[sqlalchemy-sqlalchemy]]'
- '[[sqlalchemy-alembic]]'
source_count: 3
observed_source_refs: 4
inbound_count: 11
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 5
---

# SQLite

## 개요

**SQLite**는 D. Richard Hipp가 만든 **세계에서 가장 널리 배포된 데이터베이스** — 모든 스마트폰 / 브라우저 / OS / 항공기 / 자동차 등에 임베드. C 단일 라이브러리 + 단일 파일 DB.

본 페이지는 **stub** — SQLite 자체는 raw 수집 대상이 아닌 상태에서 16회차 [[duckdb]] / [[pandas-vs-polars-vs-duckdb]] 종합 페이지가 비교 대상으로 참조하므로 정합성 stub으로 등록.

## 핵심 특성

| 항목 | 값 |
|---|---|
| 라이선스 | Public Domain |
| 언어 | C99 |
| 배포 형태 | 단일 라이브러리 + 단일 .sqlite 파일 |
| 트랜잭션 | ACID (full WAL 모드) |
| 동시성 | 단일 writer + 다중 reader (WAL) |
| 정체성 | "Application file format" — DB라기보다 application data file format |

## DuckDB / PostgreSQL 비교 (16회차 맥락)

| 차원 | SQLite | [[duckdb]] | [[postgresql]] |
|---|---|---|---|
| 워크로드 | OLTP (트랜잭션) | OLAP (분석) | OLTP (분석 가능) |
| 저장 | row-oriented | columnar | row + index |
| 임베디드 | ✅ | ✅ | ❌ |
| 단일 사용자 | ✅ 설계 | ✅ 설계 | ❌ 다중 사용자 |
| 본 위키 | stub (25회차) | 본격 (16회차) | 본격 (15회차) |

→ DuckDB가 "분석용 SQLite"라고 자기 정의 — SQLite의 임베디드 성공 모델을 OLAP로 가져온 게 DuckDB.

## 관련 개념

- [[duckdb]] — "분석용 SQLite" 자기 정의의 모델
- [[postgresql]] — 다중 사용자 OLTP 대안
- [[redis]] — 키-값 캐시·세션 저장 대안 (트랜잭션 없음)

## 출처

- [[duckdb-duckdb]] — "분석용 SQLite" 포지셔닝과 embedded OLAP 비교
- [[sqlalchemy-sqlalchemy]] — SQLite dialect/DBAPI 지원 맥락
- [[sqlalchemy-alembic]] — SQLite batch migration 제약과 마이그레이션 맥락

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[sqlite]]` 깨진 링크 발견. 29회차에 DuckDB/SQLAlchemy/Alembic source 기반으로 1차 보강.
- 본 위키에서 SQLite 본격 페이지가 부재하지만, [[duckdb]] / [[matechat|MateChat 사이드 프로젝트]] (Flutter Hive 사용) / [[backend-fastapi-stack]] 운영 시 PostgreSQL 부재 환경의 대안으로 자주 호출됨.
