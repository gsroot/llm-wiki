---
title: Query Optimization
aliases:
- Query Optimization
- 쿼리 최적화
type: concept
category: database
tags:
- query-optimization
- sql
- predicate-pushdown
related:
- '[[postgresql]]'
- '[[duckdb]]'
- '[[polars]]'
- '[[postgres-postgres]]'
- '[[duckdb-duckdb]]'
- '[[pola-rs-polars]]'
source_count: 3
observed_source_refs: 3
inbound_count: 6
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 5
---

# Query Optimization

## 정의

**Query Optimization** = SQL 또는 데이터프레임 쿼리를 의미는 동일하되 실행 비용은 더 낮은 등가 형태로 변환하는 일련의 룰·통계 기반 변환. 모든 OLTP/OLAP DB의 핵심.

본 페이지는 **stub** — [[postgresql]] / [[duckdb]] / [[polars]] 등에서 인용되므로 정합성 stub.

## 5대 표준 최적화 룰

| 룰 | 설명 | 본 위키 사례 |
|---|---|---|
| **[[predicate-pushdown]]** | WHERE를 데이터 소스로 밀기 | [[duckdb]], [[polars]] |
| **Projection pushdown** | SELECT 컬럼만 읽기 (columnar 핵심) | [[parquet]] 자동 |
| **Join reordering** | 작은 테이블 먼저 | [[postgresql]] genetic algorithm |
| **Constant folding** | 상수식 컴파일 시 계산 | 모든 옵티마이저 |
| **Common subexpression elimination** | 중복 식 1회 계산 | LLVM 스타일 |

## 본 위키 엔진별 옵티마이저

| 엔진 | 옵티마이저 |
|---|---|
| [[postgresql]] | cost-based + genetic (10+ 조인 시) |
| [[duckdb]] | rule-based + statistics |
| [[polars]] | logical plan rewriter (Lazy mode) |
| BigQuery | Dremel + slot-based 분산 |

## 회사 BI 응용

- BigQuery 쿼리 EXPLAIN 결과 읽기는 BI 개발자 핵심 기술
- Polars `lf.explain` / DuckDB `EXPLAIN ANALYZE`로 로컬에서도 옵티마이저 동작 검증 가능

## 관련 개념

- [[predicate-pushdown]] — 핵심 룰 중 하나
- [[postgresql]] / [[duckdb]] / [[polars]] — 본 위키 옵티마이저 엔진
- [[parquet]] — 컬럼 메타데이터로 옵티마이저 보조

## 출처

- [[postgres-postgres]] — cost-based optimizer와 PostgreSQL query planner 맥락
- [[duckdb-duckdb]] — OLAP vectorized executor와 SQL optimizer
- [[pola-rs-polars]] — LazyFrame logical plan optimizer

## 메모

- stub 사유: 점검에서 `[[query-optimization]]` 깨진 링크 발견. 기존 source 기반으로 1차 보강.
- 후속: BigQuery slot 기반 분산 실행과 Postgres genetic 옵티마이저 비교 종합 페이지 검토.
