---
title: "Apache Kafka"
type: entity
entity_type: tool
tags: [kafka, event-streaming, distributed-log, jvm, scala, zero-copy, sendfile, pagecache, pub-sub, asf, kraft, kip, confluent]
related:
  - "[[redis]]"
  - "[[postgresql]]"
  - "[[apache-arrow]]"
  - "[[apache-foundation]]"
  - "[[c2spf-analytics]]"
  - "[[apache-kafka]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 4
inbound_count: 33
created: 2026-04-28
updated: 2026-04-28
---

# Apache Kafka

## 개요

Apache Kafka는 **분산 이벤트 스트리밍 플랫폼** — 큰 회사의 모든 실시간 데이터 피드를 통합 처리하는 단일 플랫폼으로 설계됨. 2011년 LinkedIn에서 시작 (Jay Kreps + Neha Narkhede + Jun Rao), 2012년 ASF 인큐베이션, 2014년 Confluent 상용화. 2026년 현재 4.x stable + KRaft 모드.

라이센스: **Apache 2.0**. 거버넌스: ASF PMC (Project Management Committee) + Confluent (핵심 컨트리뷰터의 다수). JVM 기반 (Java 17/25 + Scala 2.13).

## 주요 특징

### 정체성 — "분산 데이터베이스 로그"

Kafka는 "메시지 큐"가 아니라 **데이터베이스의 WAL을 분산 시스템으로 일반화**한 것:
- **Topic** = 분산 append-only log
- **Partition** = log의 수평 파티션
- **Offset** = log 내 위치 (consumer가 추적)
- **Producer / Consumer** = pub-sub 인터페이스

### 5대 use case (design.md 모티베이션)

1. 고처리량 (실시간 로그 집계)
2. 큰 backlog 처리 (오프라인 시스템 주기적 로드)
3. 저지연 (전통 메시징)
4. 분산/파티션 처리 (파생 피드 생성)
5. 머신 실패 시 fault-tolerance

### 6대 핵심 설계 결정

#### 1. "Don't fear the filesystem!"

- 디스크 random write 100KB/sec vs sequential write 600MB/sec → **6000배 차이**
- Append-only log + sequential I/O = 모든 것의 기반
- "Sequential disk access can be faster than random memory access" (ACM Queue 인용)

#### 2. Pagecache 위임 (자체 캐시 없음)

- JVM heap 객체 오버헤드 + GC 회피
- 32GB 머신에서 28-30GB 캐시를 OS가 자동 관리
- 재시작 시 캐시 워밍 유지

#### 3. O(1) Persistent Queue

- BTree(O(log N)) 대신 append-only file + offset
- 데이터 양과 무관한 일정 성능
- 메시지 보존 1주일+ (재처리 가능)

#### 4. Zero-Copy (sendfile syscall)

- 일반: 디스크→pagecache→user buffer→socket buffer→NIC (4 copy + 2 syscall)
- sendfile: 디스크→pagecache→NIC (1 copy)
- TLS는 user-space라 sendfile 사용 불가 (한계)

#### 5. Message Set (Batching)

- Producer→broker, broker 내부, broker→consumer 모두 batch
- 표준 binary format을 producer/broker/consumer 공유 — 변환 없음
- 압축이 batch 단위 → JSON 필드명 같은 반복 패턴 압축률 극대화

#### 6. End-to-end Compression

- GZIP / Snappy / LZ4 / Zstd
- Producer가 압축 → broker는 검증만 → 디스크에 압축 상태 → consumer까지 압축 상태 전달
- 데이터센터 간 네트워크 대역폭 결정적 절약

### Streams + Connect = "응용 플랫폼"

| 컴포넌트 | 역할 |
|---------|------|
| **Kafka Streams** | in-process stream processing 라이브러리 (no cluster) |
| **Kafka Connect** | source/sink connector 플랫폼 (DB ↔ Kafka, Kafka ↔ DW) |

→ 단순 메시지 브로커 아닌 **데이터 파이프라인 OS**.

### KIP (Kafka Improvement Proposals)

PEP / PDEP / KEP 같은 절차적 의사결정 시스템. 대표 사례:
- **KIP-500**: ZooKeeper 의존 제거 → KRaft 모드 (2022 stable)
- **KIP-405**: Tiered Storage (cold tier → S3)
- **KIP-848**: 새 Consumer Rebalance Protocol

### 빌드 시스템

- Java 17 / 25 + Scala 2.13
- **Gradle**: `./gradlew jar`, `srcJar`, `aggregatedJavadoc`, `test`
- `release` param: clients/streams는 11, 나머지 17 (JVM 호환성)
- Test retry/coverage 도구 통합

### 거버넌스 — ASF PMC + Confluent 이중

ASF PMC가 공식 운영, 하지만 핵심 컨트리뷰터 다수가 Confluent 직원. → **OSS PMC + 상용 회사** 패턴 ([[redis]] Inc, [[postgresql]] EnterpriseDB와 동일).

## 라이센스 / 의존성

- **Apache 2.0**
- JVM (Java 17/25)
- Scala 2.13 (only supported version)
- ZooKeeper (~3.x까지) → **KRaft** (4.x 표준)

## 관련 개념

- [[event-driven-architecture]]: Kafka가 산업 표준 인프라
- [[append-only-log]]: Kafka의 핵심 자료구조 (= [[postgresql]] WAL의 일반화)
- [[zero-copy]]: sendfile syscall 활용
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 게임 서버 이벤트 → Kafka → BigQuery 패턴

## 관련 엔티티

- [[redis]]: 같은 "데이터 인프라" 영역. Redis Streams가 단일 노드 Kafka 같음. RESP vs Kafka 프로토콜
- [[postgresql]]: WAL이 같은 append-only log 패턴. Kafka는 그 추상의 분산 일반화
- [[apache-arrow]]: 같은 ASF 산하. Kafka 메시지 payload로 Arrow IPC 사용 사례 증가
- [[apache-foundation]]: 거버넌스 주체 (별도 엔티티 후보)
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 잠재 채택자

## 의사결정 컨텍스트 (raw 인용)

> "Apache Kafka는 분산 이벤트 스트리밍 플랫폼 — '디스크는 느리다'를 정면으로 부정하고 filesystem + pagecache + sendfile의 OS 메커니즘을 그대로 채택해 단일 클러스터에서 GB/s 처리량을 달성. design.md 자체가 분산 시스템 설계의 교과서."
> — [[apache-kafka]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 이벤트 스트리밍 표준. [[c2spf-analytics]] 게임 이벤트 수집 인프라 후보 + [[matechat|MateChat 사이드 프로젝트]] 채팅 이벤트 스트리밍 후보. **'디스크는 느리다'를 부정**하는 design.md는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 분산 시스템 설계 학습 자료. [[append-only-log]]·[[event-driven-architecture]]·[[streaming]] 개념 페이지의 출처 + [[zero-copy]] 패턴 사례.

## 출처

- [[apache-kafka]] — apache/kafka GitHub 저장소 (README + design.md 511줄 + design-index 통합 수집)

## 논쟁/모순

> [!warning] 논쟁/모순
> - **JVM 의존 = 무거움**: Java 17 + Scala 2.13. 메모리/시작 시간 트레이드오프 → Redpanda(C++), Pulsar(C++/Java)가 라이트 진영. Kafka는 표준 호환성 우위
> - **Confluent vs OSS Kafka**: 일부 기능(Schema Registry, ksqlDB)이 Confluent Community License — Apache 2.0과 별개. [[redis]] 2024 라이센스 변경처럼 향후 충돌 가능성
> - **ZooKeeper → KRaft 전환**: 4.x에서 ZK 모드 deprecated. 운영 클러스터 마이그레이션 비용 큼
> - **TLS + sendfile 충돌**: 보안 vs 성능 트레이드오프. 내부 클러스터는 비TLS, 외부는 TLS 분리 패턴
> - **Tiered Storage 성숙도**: KIP-405 안정성 검증 진행 중. S3 cold tier 사용 시 latency variance 모니터링 필수


## 메모

- **회사 BI 가설**: [[c2spf-analytics]] 게임 서버 이벤트 → Kafka → BigQuery streaming insert 패턴이 일반적. 현재 도입 여부 확인 필요
- **design.md 직접 읽기 권장**: 511줄, ~30분. 분산 시스템 면접/학습의 표준 reading. **위키 외부 링크 1순위**
- **신규 클러스터 권장 구성** (2026):
  - Java 25 LTS
  - KRaft 모드 (ZooKeeper 없음)
  - Tiered Storage (cold tier)
  - mTLS + ACL
- **Confluent Kafka vs Apache Kafka 라이센스 매트릭스**: 향후 별도 엔티티/synthesis 후보
- **이름 표기**: "Apache Kafka" (공식), "Kafka" (일상). 본 위키는 둘 다 사용
- **Jay Kreps**: 창립자 → Confluent CEO. "I Heart Logs" 책 + 블로그가 Kafka 사상 정리
- **후속 후보**: `concepts/event-driven-architecture.md`, `concepts/append-only-log.md`, Confluent 별도 엔티티
