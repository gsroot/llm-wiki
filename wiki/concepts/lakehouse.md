---
title: "Lakehouse"
aliases: [Lakehouse, 레이크하우스, data-lakehouse]
type: concept
category: data-architecture
tags: [lakehouse, data-warehouse, data-lake, parquet, delta-lake, iceberg, 25회차]
related:
  - "[[parquet]]"
  - "[[duckdb]]"
  - "[[polars]]"
  - "[[pyarrow]]"
source_count: 3
observed_source_refs: 3
inbound_count: 8
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 4
---

# Lakehouse

## 정의

**Lakehouse** = Data Lake (저렴 객체 스토리지 + 다양한 포맷) + Data Warehouse (트랜잭션 + 스키마 + SQL) 통합 아키텍처. Databricks가 2020년 정립한 용어.

본 페이지는 **stub** — 16회차 [[dataframe-ecosystem-evolution]] 등에서 데이터 인프라 진화 맥락으로 인용되므로 정합성 stub.

## 3대 오픈 lakehouse 포맷

| 포맷 | 발원 | 특징 |
|---|---|---|
| **Delta Lake** | Databricks | ACID + 시간 여행 + Spark 최적화 |
| **Apache Iceberg** | Netflix → ASF | hidden partitioning + 스키마 진화 + 멀티 엔진 (Trino/Spark/Flink/DuckDB) |
| **Apache Hudi** | Uber → ASF | upsert + CDC 친화 |

→ 모두 [[parquet]] 위에 메타데이터 layer를 얹은 패턴.

## 본 위키 인용 맥락

- 16회차 [[parquet]] / [[pyarrow]]: lakehouse 포맷의 공통 저장 표준
- 16회차 [[duckdb]]: Iceberg 직접 읽기 지원 (DuckDB 1.0+)
- 16회차 [[polars]]: Delta Lake 통합

## 회사 BI 응용

컴투스플랫폼 BigQuery는 closed lakehouse 변종 (Google 자체 storage + 메타데이터). 오픈 lakehouse(Iceberg/Delta)로 마이그레이션 시 **벤더 락인 회피 + 멀티 엔진 분석** 가능.

## 관련 개념

- [[parquet]] — lakehouse 공통 저장 포맷
- [[duckdb]] / [[polars]] — lakehouse 읽기 엔진
- [[pyarrow]] — 메모리 표준

## 출처

- [[apache-arrow]] — Parquet/Arrow가 lakehouse 포맷의 공통 저장·메모리 기반이 되는 맥락
- [[duckdb-duckdb]] — Parquet/S3/Iceberg 계열을 로컬 SQL로 읽는 Lakehouse Lite 패턴
- [[pola-rs-polars]] — Delta Lake/Parquet scan과 Lazy execution 맥락

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[lakehouse]]` 깨진 링크 발견. 29회차에 기존 source 기반으로 1차 보강했지만, Delta Lake / Iceberg / Hudi 직접 source는 아직 미수집.
- 후속: Iceberg / Delta Lake 별도 entity 또는 비교 종합 페이지 — 회사 BI 마이그레이션 검토 시 가치 큼.
