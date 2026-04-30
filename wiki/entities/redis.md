---
title: "Redis"
type: entity
entity_type: tool
tags: [redis, cache, in-memory-database, key-value-store, data-structure-server, message-broker, vector-databases, vector-search, json, time-series, antirez, single-thread, manifesto, valkey, license-change-2024, rdb, aof, redis-cluster]
aliases: [Redis, redis, 레디스]
related:
  - "[[fastapi]]"
  - "[[python-packaging]]"
  - "[[redis-redis]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 12
inbound_count: 53
created: 2026-04-28
updated: 2026-04-28
verification_required: true
last_verified: 2026-04-29
verification_notes: "Redis 라이선스(RSALv2/SSPL ↔ valkey 포크) + 8.0+ Vector Search 정식화 — 분기별 재검증"
cited_by_count: 26
---

# Redis

## 개요

17년차 ★74K **메모리 우선 자료구조 서버 + 캐시 + 메시지 브로커 + JSON 문서 DB + 벡터 쿼리 엔진**. Salvatore Sanfilippo (antirez) 2009 창작, **MANIFESTO 10항목**으로 철학 명문화 — "DSL for Abstract Data Types" / "Memory storage is #1" / "Single-threaded core" / "We optimize for joy". 2024년 BSD-3-Clause → SSPL/RSAL dual license 변경 → AWS fork **Valkey** 출시. 본 위키 첫 "철학 명문화" OSS + "라이선스 변경" 사례.

## 메타

- **저장소**: https://github.com/redis/redis
- **공식 사이트**: [redis.io](https://redis.io)
- **라이선스**: RSAL/SSPL dual (2024~), 이전 BSD 3-Clause
- **언어**: C
- **창설**: 2009-03-21 (17년차)
- **별점/포크**: ★74,041 / fork 24,588 (위키 누적 가장 큰 fork)
- **default branch**: `unstable`
- **fork**: Valkey (2024, BSD 3-Clause)

## 주요 특징

### 1. MANIFESTO 10항목 (희귀한 철학 명문화)

| # | 항목 |
|---|------|
| 1 | DSL for Abstract Data Types |
| 2 | Memory storage is #1 |
| 3 | Fundamental data structures for fundamental API |
| 4 | Code efficiency (Raspberry Pi 동작) |
| 5 | Code is like a poem |
| 6 | Against complexity |
| 7 | Threading is not a silver bullet |
| 8 | Two levels of API |
| 9 | We optimize for joy |
| 10 | Opportunistic programming (5% 코드로 95% 해결) |

### 2. 자료구조 1급 시민

Strings (binary-safe), Lists (linked), Hashes, Sets, Sorted Sets (skip list), Bitmaps, HyperLogLogs, Geospatial, **Streams** (log-like), JSON 문서. 명령 = 자료구조 자체 연산 (LPUSH / ZADD / HSET / XADD ...).

### 3. Single-Threaded Core + Cluster

- 단일 스레드 = 모든 명령 원자적 / 락 무관 / 코드 단순
- 수평 확장 = Redis Cluster (여러 인스턴스)
- I/O는 멀티스레드 일부 적용
- "한 사람이 며칠 만에 코드 전체 이해 가능" (MANIFESTO 6번)

### 4. RDB + AOF 영속성

- RDB — 주기적 스냅샷 (fork 사용)
- AOF — Append-Only File (fsync 정책: always/everysec/no)
- 둘 다 활성 가능

### 5. 5축 진화 (2024~)

저장소 description: "**cache, data structure server, document and vector query engine**"

- Cache (전통)
- Data structure server (전통)
- Document DB (JSON 모듈)
- **Vector query engine** (RediSearch + Vector) — pgvector 경쟁자
- Message broker (Pub/Sub + Streams)

### 6. 2024 라이선스 변경 → Valkey fork

- 2009~2024: BSD 3-Clause (완전 OSS)
- 2024~: RSAL/SSPL dual — 클라우드 사업자 사용 제한
- AWS fork → **Valkey** (BSD 3-Clause 유지)

[[postgresql]] 30년 BSD-style 라이선스 안정과 정반대 — **OSS 라이선스 변경 위험 사례**.

### 7. 보안 (TLS / ACL / protected-mode)

- TLS 1.2+ (서버-클라이언트 / 클러스터 노드)
- ACL (Redis 6.0+) — 사용자별 명령/키 권한
- protected-mode 디폴트 활성 (외부 접근 차단)

### 8. antirez = 시인 같은 BDFL

Salvatore Sanfilippo (antirez)가 17년 BDFL 후 2020년 lead 양도. MANIFESTO는 보존 — **창작자의 미적 비전이 라이브러리 핵심**. 위키 BDFL (pandas Wes / scikit-learn David / sqlalchemy Mike) 모두 기술 비전이지만, antirez는 **미적 / 철학적 비전**.

## 관련 개념

- [[python-packaging]]: redis-py 클라이언트

## 관련 엔티티

- [[fastapi]]: 캐시 / 세션 / 큐 통합 사용
- (별도 회차) Valkey — 2024 fork

## 의사결정 컨텍스트 (raw 인용)

> "17년차 ★74K 메모리 우선 자료구조 서버 + 캐시 + 메시지 브로커 + JSON 문서 DB + 벡터 쿼리 엔진. MANIFESTO 10항목으로 철학을 명문화한 OSS — 'Memory storage is #1' / 'Single-threaded core' / 'We optimize for joy'. 최근 description은 cache → 벡터 검색 / 실시간 데이터 엔진으로 진화."
> — [[redis-redis]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 백엔드 5단의 캐시·실시간 축. [[matechat|MateChat 사이드 프로젝트]] WebSocket 세션·실시간 알림 채택 + [[c2spf-analytics|c2spf 게임 데이터 BI]] 캐시 후보. **MANIFESTO 10항목**은 [[postgresql]] 메일링 리스트 거버넌스·[[bdfl]]과 함께 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 거버넌스 다양성 6번째 모델 — opinionated 디자인 철학의 명문화 사례. 2024 라이선스 변경 → Valkey fork 분기.

## 출처

- [[redis-redis]] — 본 저장소 1차 수집 (15회차, 2026-04-28)

## 메모

- 본 위키 첫 "철학 명문화" + "라이선스 변경 사례" — 거버넌스 모델 7번째 축
- Valkey 별도 수집 후보 (라이선스 변경 후 OSS 측 fork)
- pgvector vs Redis Vector PoC 가능 (본 위키 RAG 인프라)
- 회사 BI c2spf 적용 — 게임 리더보드 (Sorted Set), 사용자 세션 (Hash), 일일 활성 (HyperLogLog), 알림 (Streams)
- antirez 블로그 (antirez.com) 17년 BDFL 회고 1차 자료
