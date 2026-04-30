---
title: "redis/redis — In-Memory Data Structure Server (★74K, 17년차 MANIFESTO 10항목 철학 + 단일 스레드 + Vector Search 전환)"
type: source
source_type: article
source_url: "https://github.com/redis/redis"
raw_path: "raw/articles/redis-redis/"
author: "Salvatore Sanfilippo (antirez 원저자) + Redis Labs"
date_published: 2009-03-21
date_ingested: 2026-04-28
tags: [redis, cache, in-memory-database, key-value-store, data-structure-server, message-broker, message-queue, no-sql, real-time, vector-databases, vector-search, json, time-series, distributed-systems, antirez, rdb, aof, redis-cluster, single-thread, manifesto, valkey, license-change-2024]
related:
  - "[[fastapi]]"
  - "[[python-packaging]]"
confidence: high
inbound_count: 9
cited_by:
  - "[[append-only-log]]"
  - "[[backend-fastapi-stack]]"
  - "[[event-driven-architecture]]"
  - "[[redis]]"
  - "[[streaming]]"
cited_by_count: 5
---

# redis/redis — In-Memory Data Structure Server

## 한줄 요약

> 17년차 ★74K **메모리 우선 자료구조 서버 + 캐시 + 메시지 브로커 + JSON 문서 DB + 벡터 쿼리 엔진**. **MANIFESTO 10항목**으로 철학을 명문화한 보기 드문 OSS — "DSL for Abstract Data Types" / "Memory storage is #1" / "Single-threaded core" / "We optimize for joy" — 6번째 (복잡성 거부)와 9번째 (즐거움 최적화)가 30년+ Linux/Postgres 보수파와는 또 다른 **"opinionated 디자인 철학"**. 최근 description은 cache → 벡터 검색 / 실시간 데이터 엔진으로 진화 명시.

## 메타

- **Repository**: redis/redis
- **별점/포크**: ★74,041 / fork 24,588 (수집일 2026-04-28 기준, 위키 누적 가장 큰 fork 수)
- **라이선스**: NOASSERTION (Redis Source Available License v2 / Server Side Public License — 2024 라이선스 변경 전 BSD 3-Clause, 변경 이후 dual license)
- **언어**: C
- **창설일**: 2009-03-21 (17년차)
- **최종 push**: 2026-04-28 (수집일 당일까지 활발)
- **저장소 크기**: 211 MB
- **default branch**: `unstable`
- **Topics**: cache, caching, database, distributed-systems, in-memory, in-memory-database, json, key-value, key-value-store, message-broker, message-queue, no-sql, nosql, open-source, real-time, realtime, redis, time-series, vector-databases, vector-search

## raw 파일 구조 (보관 6개 파일, 약 68KB)

```
raw/articles/redis-redis/
├── README.md (39KB) — 광범 안내 (인스톨, 빌드, 런타임 옵션, 신호 처리, 코드 구조)
├── MANIFESTO (6.9KB) ★ Redis 철학 10항목 — 본 회차 결정적 자료
├── CONTRIBUTING.md (7.2KB) — 패치 제출 가이드
├── RELEASENOTES_head200 (627B) — 외부 위치 안내
├── SECURITY.md (3.7KB) — 보안 정책
└── TLS.md (3.6KB) — TLS 설정
```

**제외**: `src/` C 본체, `deps/` 의존성, `modules/` 모듈 시스템, `tests/`, `redis.conf` / `sentinel.conf`, `utils/`, `00-RELEASENOTES` 본체.

## 핵심 내용

### 1. MANIFESTO 10항목 — Redis 철학 (희귀한 OSS 명문화 철학)

본 회차 결정적 자료. 10항목 요약:

| # | 항목 | 핵심 |
|---|------|------|
| 1 | DSL for Abstract Data Types | 키 = 바이너리 안전 문자열, 값 = 자료구조 (List = linked list / Sorted Set 등) |
| 2 | Memory storage is #1 | 메모리에 저장. 디스크는 옵션. 10k 키든 4천만 키든 비슷한 성능 |
| 3 | Fundamental data structures for fundamental API | "외계인도 알 수 있는 자료구조"의 추상화 |
| 4 | Code efficiency | Raspberry Pi에서도 동작 + 환경 영향 최소 |
| 5 | Code is like a poem | "셰익스피어가 단테로 마무리하지 않는다" — 외부 코드 통합에 신중 |
| 6 | Against complexity | "한 명이 며칠 만에 코드 전체를 이해할 수 있어야 함" |
| 7 | Threading is not a silver bullet | 단일 스레드 + Cluster로 수평 확장 |
| 8 | Two levels of API | 분산 가능 API + 멀티키 API 분리 (옵션) |
| 9 | We optimize for joy | "코드 작성에 즐거움이 없으면 멈춰라" |
| 10 | Opportunistic programming | "5%의 코드로 95%의 문제 해결" |

이 철학들이 **30년+ Linux/Postgres 보수파**와는 다른 차원의 OSS 거버넌스 — 기술 스펙이 아니라 **창작 철학**. 본 위키 누적 거버넌스 사례에 또 다른 축 추가.

### 2. Single-Threaded Core — Redis의 결정적 디자인 선택

MANIFESTO 7번 — "Threading is not a silver bullet." 단일 스레드 + Redis Cluster (수평 확장). 장점 — 데이터 락 무관 / NUMA 친화 / persist-by-fork 안정성 / 각 인스턴스 메모리 작음. I/O는 멀티스레드 적용 가능. **단순 = 빠름** 철학의 모범.

### 3. 자료구조 = 1급 시민

Strings (binary-safe), Lists (linked), Hashes (field-value), Sets, Sorted Sets (skip list), Bitmaps, HyperLogLogs, Geospatial, Streams (log-like), JSON 문서.

각 자료구조의 명령 = SQL의 SELECT/INSERT가 아니라 **자료구조 자체의 연산** (LPUSH / RPOP / ZADD / ZRANGEBYSCORE / SADD / HSET ...). **PostgreSQL이 SQL 표준 + 확장이라면 Redis는 자료구조 추상 + 분산**.

### 4. Vector Search 진화 — 17년차 캐시 → AI 인프라

저장소 description 명시:

> "For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine."

**vector query engine** 명시 + Topics에 `vector-databases` / `vector-search` 포함. Redis가 **pgvector**(PostgreSQL 확장)의 경쟁자로 진화. 회사 BI에서 LLM RAG 시 PostgreSQL + pgvector 또는 Redis + RediSearch 모듈 둘 다 가능.

### 5. 라이선스 변경 (2024) — Source Available

GitHub의 license 필드는 NOASSERTION. 2024년 BSD 3-Clause → **Redis Source Available License v2 (RSAL) / Server Side Public License (SSPL) dual license**로 변경:

- 이전 (2009~2024): BSD 3-Clause (완전 OSS)
- 이후 (2024~): RSAL/SSPL dual — 클라우드 호스팅 사업자 (AWS ElastiCache 등) 사용 제한
- AWS는 fork → **Valkey** 출시 (2024 BSD 3-Clause)

이는 [[postgresql]](본 회차) BSD-style + AWS RDS의 자유로운 fork 모델과 정반대. 회사 BI 도구 선택 시 라이선스 미래 변경 위험 고려 필요.

### 6. RDB + AOF — 영속성 옵션

Redis 메모리 우선이지만 디스크 영속성도 지원 — RDB (주기적 스냅샷, fork 사용) / AOF (모든 쓰기 명령 로그, fsync 정책 always/everysec/no). 둘 다 활성 가능 — RDB로 빠른 시작 + AOF로 최신 상태 복구.

### 7. 보안 + TLS — 회사 BI 운영 핵심

- TLS 1.2+ 지원 (서버-클라이언트 / 클러스터 노드 간)
- ACL (Access Control List) — Redis 6.0+ 사용자별 명령/키 권한
- AUTH 명령 — 비밀번호 인증
- protected-mode — 외부 접근 자동 차단 (디폴트)
- bind 설정 — 인터페이스 제한

회사 BI 적용 시 protected-mode + ACL + TLS 3종 강제. 결제 데이터 캐시는 Redis 별도 인스턴스 + 더 엄격한 ACL.

## 인사이트

### Insight 1: MANIFESTO = 위키 첫 "철학 명문화" OSS 사례

위키 누적 OSS 거버넌스 모델 (5축):

1. BDFL (pandas / scikit-learn / sqlalchemy / fastapi)
2. 표준 + 구현 분리 (anthropics-skills / spec-kit)
3. Core Team + RFC (SLEP / PDEP)
4. 살아있는 운영 노트 (openai-cookbook / openai-agents-python)
5. 메일링 리스트 (PostgreSQL)
6. **철학 명문화 (Redis)** — **본 회차 첫 사례**

MANIFESTO는 단순 "기여 가이드"나 "RFC"가 아니라 **창작 의도와 미적 가치**를 명시. "We optimize for joy" 같은 항목은 기술 라이브러리 README에서 매우 희귀.

### Insight 2: Single-Threaded = 단순함의 절대 신봉

MANIFESTO 6번 ("Against complexity") + 7번 ("Threading not silver bullet")이 일관 — 단일 스레드 = 락 없음 = 코드 단순. Redis Cluster = 수평 확장 (수직 확장 포기). "한 사람이 며칠에 코드 전체 이해 가능."

이는 [[postgresql]] (본 회차) MVCC 멀티스레드 / [[scikit-learn]] joblib 멀티프로세스와 완전 다른 디자인 선택.

### Insight 3: 자료구조 1급 시민 = SQL 추상의 정반대

[[postgresql]] / [[sqlalchemy]] = 관계형 추상 → SQL 명령. **Redis = 자료구조 추상** → 자료구조 명령. 회사 BI에서 — 게임 리더보드 (Sorted Set) / 사용자 세션 (Hash) / 알림 큐 (Stream) / 일일 활성 유저 (HyperLogLog). 각 자료구조가 PostgreSQL 테이블 + 인덱스 + 쿼리보다 직관적인 도메인이 많음.

### Insight 4: 라이선스 변경 (2024) = OSS 변동성 사례

Redis 2024 라이선스 변경은 OSS 역사상 큰 사건 — Elasticsearch (2021) / MongoDB (2018) / CockroachDB (2024)와 같은 흐름. 회사 BI 도구 선택 기준에 **라이선스 변경 위험** 추가:

- BSD/MIT 라이선스 → 변경 가능
- Foundation 거버넌스 (Linux/Apache Foundation) → 변경 어려움
- **Valkey (Redis fork)** = OSS 공동체의 fork 패턴

c2spf-platform Redis 사용 시 Valkey로 마이그레이션 가능성도 검토 — 동일 프로토콜.

### Insight 5: Redis 5축 = 캐시 + DB + 큐 + JSON + Vector

저장소 description의 5축 — Cache / Data structure server / Document DB (JSON 모듈) / Vector query engine (RediSearch + Vector) / Message broker (Pub/Sub + Streams).

회사 BI에서 보통 1~2축만 사용 (캐시 + 자료구조)이지만, **vector** 축 추가 시 LLM RAG 인프라 통합 가능 — 별도 벡터 DB 회피.

### Insight 6: antirez (Salvatore Sanfilippo) = 시인 같은 BDFL

MANIFESTO 5번 — "Code is like a poem"는 antirez 본인 저작. 그는 Redis 17년 BDFL 후 2020년 lead 자리 양도. 그러나 MANIFESTO는 그대로 유지 — **창작자의 미적 가치를 후속 팀이 보존**. 위키 누적 BDFL (pandas Wes / scikit-learn David / sqlalchemy Mike)은 모두 기술 비전이지만, antirez는 **미적 / 철학적 비전**.

### Insight 7: 단순함 + 자료구조 = 학습 가치

Redis는 다른 라이브러리와 다른 **학습 가치** — 개념이 적음 (자료구조 7~10개 + 명령 200~300개) / 즉시 사용 / 명령 직관적 / "한 사람이 며칠 만에 전체 이해". 신규 입사자 + AI 에이전트 모두 PostgreSQL/SQLAlchemy 같은 깊은 추상보다 Redis가 빠르게 도입 가능.

## 인용 (raw에서 직접 발췌)

### MANIFESTO — 1번 DSL for Abstract Data Types

> Redis is a DSL (Domain Specific Language) that manipulates abstract data types and implemented as a TCP daemon. Commands manipulate a key space where keys are binary-safe strings and values are different kinds of abstract data types.

### MANIFESTO — 5번 Code is like a poem

> Code is like a poem; it's not just something we write to reach some practical result. Sometimes people that are far from the Redis philosophy suggest using other code written by other authors (frequently in other languages) in order to implement something Redis currently lacks. But to us this is like if Shakespeare decided to end Enrico IV using the Paradiso from the Divina Commedia.

### MANIFESTO — 6번 Against complexity

> We're against complexity. We believe designing systems is a fight against complexity. ... One of the main Redis goals is to remain understandable, enough for a single programmer to have a clear idea of how it works in detail just reading the source code for a couple of weeks.

### MANIFESTO — 9번 We optimize for joy

> We optimize for joy. We believe writing code is a lot of hard work, and the only way it can be worth is by enjoying it. When there is no longer joy in writing code, the best thing to do is stop. To prevent this, we'll avoid taking paths that will make Redis less of a joy to develop.

### 저장소 description — 5축 진화

> For developers, who are building real-time data-driven applications, Redis is the preferred, fastest, and most feature-rich cache, data structure server, and document and vector query engine.

## 후속 탐구

1. **Valkey (Redis fork)** 별도 수집 — 라이선스 변경 후 OSS 측 fork 분석
2. **redis.conf / sentinel.conf 설정** 분석 — 운영 옵션 1차 자료
3. **RediSearch / RedisJSON / RedisGraph 모듈** 별도 분석
4. **Redis Cluster 깊이 분석** — slot / resharding / failover 메커니즘
5. **antirez 블로그 (antirez.com)** — Redis 창작 17년 회고
6. **Redis Streams 별도 분석** — Kafka 대안 (16회차 데이터 회차에서 비교)
7. **Python 클라이언트 redis-py** 별도 분석

## 회사 BI 적용 가설

### 가설 1: c2spf-analytics 캐시 + 세션 + 리더보드 표준화

| 용도 | Redis 자료구조 | 비고 |
|------|------|------|
| BigQuery 결과 캐시 | String (TTL) | 분석 쿼리 비용 절감 |
| 사용자 세션 | Hash | FastAPI 의존성 주입 |
| 게임 리더보드 | Sorted Set | ZADD / ZRANGEBYSCORE |
| 일일 활성 유저 카운트 | HyperLogLog | 메모리 효율 |
| 실시간 알림 | Streams (XADD/XREAD) | Pub/Sub 대안 |

### 가설 2: Redis MANIFESTO 형식의 c2spf-analytics 자체 매니페스토

Redis 10항목처럼 c2spf-analytics MANIFESTO 작성 — 데이터 정확성 #1 / 느린 분석은 비용이 아닌 신호 / 읽기 전용 권장 + 쓰기는 책임 등. 본 위키 CLAUDE.md와 비슷한 형식.

### 가설 3: pgvector vs Redis Vector 비교 PoC

본 위키 RAG 인프라로 pgvector vs Redis Vector 비교 — 인덱스 빌드 시간 / 쿼리 latency / 메모리 사용 / 운영 복잡도. 회사 BI 결정 자료.

### 가설 4: 라이선스 변경 위험 사전 평가

c2spf 사용 OSS 라이선스 trail 정기 점검 — Redis 2024 변경 같은 사건이 다른 도구에서도 발생 가능. 라이선스 변경 시 fork 후보 사전 파악 (Redis → Valkey, MongoDB → Percona / FerretDB 등).

## 메모

본 회차는 백엔드 코어 6개 중 마지막. **MANIFESTO 10항목 + 단일 스레드 + 자료구조 추상**이 PostgreSQL과 함께 본 회차의 두 큰 발견. agent-skills 진화 8단계 + Astral 회사 차원 표준화에 이어 본 회차에서 **PostgreSQL** = "메일링 리스트 보수파" (6번째 거버넌스 모델), **Redis** = "MANIFESTO 철학 명문화" (7번째 거버넌스 모델) 2개 새 거버넌스 모델 추가. 본 회차 종합 페이지 [[backend-fastapi-stack]]에서 6개 항목을 통합 분석하면 **단일 백엔드 도메인 안에서 7개 거버넌스 모델이 공존하는 사례**가 박힘.
