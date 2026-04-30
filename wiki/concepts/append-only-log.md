---
title: "Append-only Log"
aliases: [Append-only Log, 어펜드 로그, append log]
type: concept
category: data-architecture
tags: [append-only-log, wal, kafka, log-structured, sequential-io, 25회차]
related:
  - "[[kafka]]"
  - "[[postgresql]]"
  - "[[redis]]"
source_count: 4
observed_source_refs: 4
inbound_count: 14
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 8
---

# Append-only Log

## 정의

**Append-only Log** = 데이터를 끝에만 추가하고 절대 수정·삭제하지 않는 자료구조. 디스크 sequential I/O 활용 → SSD/HDD 모두에서 random write 대비 10~100배 빠름.

본 페이지는 **stub** — 16회차 [[kafka]] / 15회차 [[postgresql]] / 19회차 [[sentry]] 등 다수 페이지에서 인용되므로 정합성 stub.

## 본 위키 사례

| 시스템 | append-only 활용 | 위키 회차 |
|---|---|---|
| [[kafka]] | Topic = append-only log of records | 16 |
| [[postgresql]] | WAL (Write-Ahead Log) | 15 |
| [[redis]] | AOF (Append-Only File) 지속화 모드 | 15 |
| Cassandra / RocksDB | LSM-Tree (Log-Structured Merge) | (미수집) |
| Git | object database = content-addressed append-only | (미수집) |
| [[parquet]] | row group append + footer rewrite | 16 |
| [[event-driven-architecture]] | Event Sourcing의 자료구조 | 25 |

## 16회차 "디스크는 친구" 사상

[[kafka]] design.md 511줄의 결론:
- 디스크 sequential write = 메모리 random access 수준 속도
- 페이지 캐시는 OS가 자동 관리 → 자체 캐시 구현보다 OS pagecache 위임이 효율적
- SSD 시대에도 여전히 sequential I/O가 우월 (write amplification 감소)

## 회사 BI 응용

- BigQuery 자체가 append-only 컬럼 스토어 (DML은 새 row group 생성, 기존 미변경)
- Kafka → BigQuery 적재 = 두 append-only 시스템 간 자연스러운 흐름

## 관련 개념

- [[kafka]] — 표준 사례
- [[postgresql]] WAL — DB 트랜잭션 로그
- [[event-driven-architecture]] — append-only가 메시지 자료구조
- [[zero-copy]] — sendfile() = append-only log → consumer 직접 전송

## 출처

- [[apache-kafka]] — Kafka design 문서의 append-only log, pagecache, sequential I/O 설계
- [[postgres-postgres]] — WAL 기반 트랜잭션 로그와 MVCC 맥락
- [[redis-redis]] — AOF(Append-Only File) 지속화 모드
- [[apache-arrow]] — Parquet/Arrow 계열의 append-friendly 컬럼 저장 맥락

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[append-only-log]]` 깨진 링크 발견. 29회차에 기존 16/15회차 source 기반으로 1차 보강.
- LSM-Tree (Cassandra/RocksDB/SQLite WAL): append-only + compaction = 다른 변종.
