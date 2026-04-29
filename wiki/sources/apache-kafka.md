---
title: "apache/kafka (Kafka 저장소)"
type: source
source_type: article
source_url: "https://github.com/apache/kafka"
raw_path: "raw/articles/apache-kafka/"
author: "Apache Software Foundation + Confluent"
date_published: 2011-01-25
date_ingested: 2026-04-28
tags: [kafka, event-streaming, distributed-log, jvm, scala, zero-copy, sendfile, pagecache, pub-sub, asf, kraft, kip]
related:
  - "[[kafka]]"
  - "[[redis]]"
  - "[[postgresql]]"
  - "[[apache-foundation]]"
confidence: high
cited_by:
  - "[[apache-foundation]]"
  - "[[append-only-log]]"
  - "[[c2spf-analytics]]"
  - "[[dataframe-ecosystem-evolution]]"
  - "[[event-driven-architecture]]"
  - "[[kafka]]"
  - "[[streaming]]"
  - "[[zero-copy]]"
---

# apache/kafka (Kafka 저장소)

## 한줄 요약

> Apache Kafka는 **분산 이벤트 스트리밍 플랫폼** — "디스크는 느리다"를 정면으로 부정하고 **filesystem + pagecache + sendfile**의 OS 메커니즘을 그대로 채택해 단일 클러스터에서 GB/s 처리량을 달성. design.md 자체가 분산 시스템 설계의 교과서.

## 핵심 내용

### 정체성 (README + design.md Motivation)

Kafka는 "메시지 큐"가 아니라 **데이터베이스 로그를 분산 시스템으로 일반화**한 것. 큰 회사의 모든 실시간 데이터 피드를 통합 처리하는 **단일 플랫폼**으로 설계.

design.md(511줄)는 다음 5개 use case를 동시에 만족시킨다고 선언:
1. 고처리량 (실시간 로그 집계)
2. 큰 backlog 처리 (오프라인 시스템 주기적 로드)
3. 저지연 (전통 메시징)
4. 분산/파티션 처리 (파생 피드)
5. 머신 실패 시 fault-tolerance

### 핵심 결정 1: 디스크 = 친구 (Don't fear the filesystem!)

design.md의 가장 유명한 절. 통념 부정:
- 디스크 random write 100KB/sec vs sequential write 600MB/sec → **6000배 차이**
- 모던 OS의 read-ahead/write-behind가 sequential을 알아서 최적화
- "Sequential disk access can be faster than random memory access" (ACM Queue 인용)
- → **Append-only log + sequential read/write**가 모든 것의 기반

### 핵심 결정 2: pagecache 위임 = "OS가 cache 관리자"

JVM 위에서 객체 캐시를 직접 만들면:
1. 객체 메모리 오버헤드 2배+ (Java)
2. GC가 in-heap 데이터 증가에 따라 느려짐

→ Kafka는 **자체 캐시를 만들지 않음**. 모든 데이터는 즉시 OS pagecache로 → 32GB 머신에서 28-30GB 캐시를 GC 페널티 없이 자동 사용. 재시작 시에도 캐시 워밍 유지.

### 핵심 결정 3: O(1) Persistent Queue

전통 메시징 시스템은 BTree (O(log N)) → 디스크 seek 비용. Kafka는 **append-only log + offset**으로 모든 작업 O(1):
- 데이터 양과 무관한 일정 성능
- 7200rpm SATA 1TB 디스크가 SSD보다 3배 싸고 3배 큼 — 충분
- 메시지 보존 기간을 1주일로 둘 수 있음 (재처리 가능)

### 핵심 결정 4: Zero-Copy (sendfile)

데이터 흐름의 핵심 최적화:

| 일반 경로 (4 copy + 2 syscall) | sendfile 경로 (1 copy) |
|------|------|
| 디스크→pagecache→user buffer→socket buffer→NIC | 디스크→pagecache→NIC |

→ TLS는 user-space 라이브러리라 sendfile 사용 안 됨 (현재). 비TLS 경로에서 네트워크 한계 도달.

### 핵심 결정 5: Message Set (Batching)

작은 IO를 큰 IO로 묶음 — 클라이언트→브로커 / 브로커 내부 / 브로커→소비자 모두에서:
- 네트워크 패킷 크기 ↑
- 디스크 sequential ↑
- CPU cache 활용 ↑

표준화된 binary message format 공유 → producer/broker/consumer 사이 변환 없음. **압축은 batch 단위** → JSON 필드명 같은 반복 패턴이 압축률 극대화.

### 핵심 결정 6: 압축 (GZIP, Snappy, LZ4, Zstd)

End-to-end batch compression:
- Producer가 batch 압축 → 서버는 검증만 → 디스크에 압축 상태로 저장 → 소비자에게 압축 상태로 전송 → 소비자가 압축 해제
- 데이터센터 간 네트워크 대역폭 절약 결정적

### 빌드 시스템

- **Java 17 / 25** + **Scala 2.13** (single supported version)
- Gradle 빌드: `./gradlew jar`, `srcJar`, `aggregatedJavadoc`, `test`
- `release` 파라미터: clients/streams는 11, 나머지는 17 (호환성)
- Test retry/coverage 도구 통합 (`maxTestRetries`, `enableTestCoverage`)

### docs/ 구조

10개 디렉토리: apis / configuration / **design** / documentation / getting-started / images / implementation / kafka-connect / operations / security / streams. → 도메인 주도 분리.

## 주요 인사이트

### 1. design.md = 분산 시스템 설계의 교과서

511줄의 design.md는 다음을 모두 다룸: 모티베이션, 영속성(disk fear), 효율성(zero-copy/batching/compression), producer/consumer push-pull, semantics(at-least-once/exactly-once), replication, log compaction, quotas. **단일 문서로 분산 시스템 학습 가능** — Kafka의 진짜 가치는 이 문서.

### 2. "디스크는 빠르다" 명제의 산업적 검증

Kafka가 등장(2011)하기 전까지 "메시지 큐는 메모리 우선"이 상식. Kafka가 OS의 sequential I/O + pagecache 메커니즘을 신뢰하자 통념이 깨짐. → 이후 [[duckdb]]/[[postgresql]]/[[redis]] WAL 모두 동일 원리 강화.

### 3. Apache Software Foundation 거버넌스 + Confluent 이중 구조

Kafka는 ASF의 PMC가 운영하지만, 핵심 컨트리뷰터의 다수가 Confluent 직원 — [[redis]] Inc, [[postgresql]] EnterpriseDB, [[polars]] Polars Cloud와 동일 패턴. **OSS PMC + 상용 회사**가 공존하는 거버넌스 8번째 사례.

### 4. KIP (Kafka Improvement Proposals)

PEP/PDEP/KEP 같은 절차적 의사결정 시스템. KIP-500이 ZooKeeper 의존 제거 → KRaft 모드 (2022 stable)로 이어짐. **거버넌스 산출물 시스템 사례 추가**.

### 5. Streams + Connect = "Kafka 위 응용 플랫폼"

Kafka는 단순 메시지 브로커가 아님:
- **Kafka Streams**: stream processing 라이브러리 (in-process, no cluster)
- **Kafka Connect**: source/sink connector 플랫폼 (DB → Kafka, Kafka → DW)

→ "데이터 파이프라인 OS" 포지션. [[redis]] modules와 같은 패턴.

### 6. JVM 의존성 = trade-off

Kafka는 Java 17/25 + Scala 2.13 — JVM 무거움이 단점. 하지만:
- pagecache 위임으로 GC 영향 최소화 (heap을 적게 씀)
- Java 생태계 호환성 (Spring, Flink, Spark)
- Confluent의 산업 채택

대안: Redpanda(C++), Apache Pulsar(C++/Java) — 라이트 진영. Kafka는 표준 + 호환성 우위.

## 관련 엔티티/개념

- [[kafka]]: 본 소스의 메인 엔티티
- [[redis]]: 같은 데이터 인프라 영역 — Redis Streams가 단일 노드 Kafka 같음. RESP vs Kafka 프로토콜
- [[postgresql]]: WAL이 같은 append-only log 패턴. 한 단계 더 추상화한 것이 Kafka log
- [[apache-foundation]]: 거버넌스 주체 (별도 엔티티 후보)
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 회사 BI에서 게임 이벤트 스트림 → BigQuery ingestion에 Kafka가 표준 패턴

## 인용할 만한 구절

> "Don't fear the filesystem!"
> — design.md (47줄, 절 제목)

> "Sequential disk access can in some cases be faster than random memory access!"
> — design.md (51줄, ACM Queue 인용)

> "We designed Kafka to be able to act as a unified platform for handling all the real-time data feeds a large company might have."
> — design.md (Motivation)

## 메모

- **KRaft 전환**: ZooKeeper 의존 제거가 KIP-500부터 시작 → 3.x stable. 신규 도입 시 KRaft 모드 권장
- **Confluent vs Open Source Apache Kafka**: 라이센스 구조가 [[redis]] 2024 변경처럼 충돌 가능성 — Confluent의 일부 기능은 별도 라이센스. 추적 가치
- **회사 BI 적용**: [[c2spf-analytics|c2spf 게임 데이터 BI]] 게임 서버 이벤트 → Kafka → BigQuery 패턴이 일반적. 현재 도입 여부 확인 후 위키에 반영
- **Java 17/25 양립**: Java 25 LTS 채택 진행 중 — 2026 시점 신규 클러스터는 25 권장
- **design.md 직접 읽기 권장**: 511줄, 약 30분 → 분산 시스템 면접/학습의 표준 reading. 책 한 권 분량을 압축
