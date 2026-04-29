---
title: "Zero-copy"
type: concept
category: data-architecture
tags: [zero-copy, arrow, parquet, memory-model, performance, 25회차]
related:
  - "[[pyarrow]]"
  - "[[parquet]]"
  - "[[duckdb]]"
  - "[[polars]]"
source_count: 4
observed_source_refs: 0
inbound_count: 6
created: 2026-04-28
updated: 2026-04-29
---

# Zero-copy

## 정의

**Zero-copy** = 동일 메모리 표현을 변환·복사 없이 다른 라이브러리·프로세스에서 그대로 읽음. 16회차 [[pyarrow]]가 이 패턴의 표준.

본 페이지는 **stub** — 16회차 [[dataframe-ecosystem-evolution]] 등에서 인용되므로 정합성 stub.

## 본 위키 사례

| 도구 쌍 | zero-copy 가능 여부 |
|---|---|
| [[pyarrow]] ↔ [[polars]] | ✅ 양방향 |
| [[pyarrow]] ↔ [[duckdb]] | ✅ 양방향 |
| [[pyarrow]] ↔ [[pandas]] (pyarrow backend) | ✅ (pandas 2.0+ pyarrow dtype) |
| [[parquet]] 디스크 → [[pyarrow]] memory | ✅ mmap 가능 |
| Arrow IPC ↔ 다른 프로세스 | ✅ shared memory |

→ 16회차 핵심 발견: **"메모리 표준 = 디스크 표준" 통합** = Apache Arrow + Parquet 단일 자료형 모델이 변환 비용 0 보장.

## 회사 BI 응용

- BigQuery 결과 → Arrow (BigQuery Storage API) → DuckDB SQL → Polars 분석 → pandas ML 출력 = **5단계 변환 비용 0**
- 이는 16회차 [[dataframe-ecosystem-evolution]]의 "데이터 인프라 역사상 가장 성공적인 표준화" 결론의 실증

## 관련 개념

- [[pyarrow]] — zero-copy 표준 정의자
- [[parquet]] — 디스크 zero-copy 포맷
- [[duckdb]] / [[polars]] — Arrow 메모리 직접 사용 엔진
- [[append-only-log]] — Kafka의 zero-copy sendfile 시스템콜

## 출처

- [[apache-arrow]] — Arrow/Parquet의 메모리·디스크 표준과 zero-copy 교환
- [[duckdb-duckdb]] — Arrow/pandas/Polars 통합과 Parquet 직접 scan
- [[pola-rs-polars]] — Arrow 기반 컬럼 메모리 모델과 Lazy execution
- [[apache-kafka]] — sendfile/pagecache 기반 네트워크 zero-copy 설계

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[zero-copy]]` 깨진 링크 발견. 29회차에 기존 source 기반으로 1차 보강.
- 16회차 발견 = 1990년대 Linux sendfile() 시스템콜의 Apache Arrow 일반화.
