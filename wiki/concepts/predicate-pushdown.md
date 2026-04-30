---
title: "Predicate Pushdown"
type: concept
category: query-optimization
tags: [predicate-pushdown, sql-optimization, parquet, duckdb, polars, 25회차]
related:
  - "[[duckdb]]"
  - "[[polars]]"
  - "[[parquet]]"
  - "[[pyarrow]]"
source_count: 3
observed_source_refs: 3
inbound_count: 10
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 6
---

# Predicate Pushdown

## 정의

**Predicate Pushdown** = `WHERE` 조건(predicate)을 가능한 한 데이터 소스 가까이로 밀어 내려 (push down) 불필요한 데이터 읽기·전송을 차단하는 쿼리 최적화 기법. SQL 옵티마이저의 핵심 룰 중 하나.

본 페이지는 **stub** — 16회차 [[duckdb]] / [[polars]] / [[parquet]] 등에서 인용되므로 정합성 stub.

## 동작 예시 (Parquet 분석)

```sql
SELECT user_id, revenue FROM 'data.parquet' WHERE date = '2026-04-28';
```

**naive 실행**: 전체 Parquet 읽기 → 메모리에서 WHERE 필터링
**predicate pushdown**: Parquet 메타데이터의 row group min/max 통계 → 해당 date 범위 row group만 읽기 → I/O 90%+ 절감

## 본 위키 사례

| 엔진 | predicate pushdown 지원 |
|---|---|
| [[duckdb]] | ✅ Parquet / CSV / Iceberg / Delta 모두 |
| [[polars]] | ✅ Lazy mode 자동 (scan_parquet) |
| [[pyarrow]] Dataset | ✅ filters= 인자 |
| [[pandas]] (pyarrow backend) | 부분 (pyarrow read_parquet 단계만) |
| BigQuery | ✅ 자동 + clustering / partitioning 활용 |

## 회사 BI 응용

- BigQuery `WHERE date = '...'` 쿼리는 partitioned table에서 자동 pushdown — 비용 90%+ 절감
- 로컬 분석에서 Polars/DuckDB로 로컬 Parquet 읽을 때도 동일 효과

## 관련 개념

- [[parquet]] — predicate pushdown의 핵심 메타데이터 보유 (row group min/max)
- [[duckdb]] / [[polars]] — pushdown 표준 지원 엔진
- [[query-optimization]] — 상위 개념

## 출처

- [[duckdb-duckdb]] — Parquet/CSV scan과 SQL optimizer의 pushdown 맥락
- [[pola-rs-polars]] — LazyFrame logical plan 최적화와 scan 단계 pushdown
- [[apache-arrow]] — Parquet row group metadata와 columnar scan 기반

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[predicate-pushdown]]` 깨진 링크 발견. 29회차에 기존 source 기반으로 1차 보강.
- Projection pushdown(불필요한 컬럼 제거)과 함께 columnar 쿼리 최적화의 양대 축.
