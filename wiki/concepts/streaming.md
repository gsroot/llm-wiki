---
title: Streaming (데이터 스트리밍)
aliases:
- Streaming
- 스트리밍
type: concept
category: data-architecture
tags:
- streaming
- kafka
- polars
- pubsub
- real-time
related:
- '[[kafka]]'
- '[[polars]]'
- '[[duckdb]]'
- '[[redis]]'
- '[[apache-kafka]]'
- '[[pola-rs-polars]]'
- '[[duckdb-duckdb]]'
- '[[redis-redis]]'
source_count: 4
observed_source_refs: 4
inbound_count: 7
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 6
---

# Streaming

## 정의

**Streaming** = 무한 데이터 흐름을 작은 단위(마이크로배치 또는 이벤트별)로 처리. 배치(batch, 유한 데이터 일괄 처리)의 반대. 본 위키에서는 (a) 메시지 스트리밍 ([[kafka]]) + (b) 분석 엔진 스트리밍 모드 ([[polars]] / [[duckdb]]) 두 의미로 사용.

본 페이지는 **stub** — [[dataframe-ecosystem-evolution]] / [[kafka]] 등에서 인용되므로 정합성 stub.

## 두 가지 streaming 의미

### (a) 메시지 스트리밍 (인프라)

| 도구 | 정체성 | 시점 |
|---|---|---|
| [[kafka]] | 분산 이벤트 로그 | 16 |
| [[redis]] Streams | Redis 5+ 내장 | 15 |
| Pulsar / RabbitMQ | 대안 | (미수집) |

### (b) 분석 엔진 스트리밍 모드 (in-memory)

| 도구 | 사용 | 시점 |
|---|---|---|
| [[polars]] | `scan_csv.collect(streaming=True)` — 메모리 부족 데이터 처리 | 16 |
| [[duckdb]] | 큰 Parquet/CSV 자동 streaming | 16 |
| [[pyarrow]] | Dataset.scan | 16 |

## 회사 BI 응용

- (a) 게임 이벤트 → Kafka → BigQuery 적재 (실시간 분석)
- (b) BigQuery 결과 다운로드 후 Polars streaming으로 메모리 절약

## 관련 개념

- [[kafka]] — 분산 메시지 스트리밍 표준
- [[polars]] / [[duckdb]] — 분석 엔진 streaming 모드
- [[redis]] Streams — 경량 대안
- [[append-only-log]] — Kafka의 핵심 자료구조

## 출처

- [[apache-kafka]] — event streaming과 append-only topic 설계
- [[pola-rs-polars]] — LazyFrame/streaming execution의 데이터프레임 맥락
- [[duckdb-duckdb]] — 대용량 Parquet/CSV scan과 vectorized execution
- [[redis-redis]] — Redis Streams와 Pub/Sub의 경량 스트리밍 맥락

## 메모

- stub 사유: 점검에서 `[[streaming]]` 깨진 링크 발견. 기존 source 기반으로 1차 보강.
- "디스크는 친구" 사상의 streaming 변종 — sequential I/O + 페이지 캐시 활용으로 메모리 한계 회피.
