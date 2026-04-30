---
title: "Apache Software Foundation"
type: entity
entity_type: organization
tags: [apache-software-foundation, asf, oss-governance, pmc, vendor-neutral, 25회차]
related:
  - "[[kafka]]"
  - "[[parquet]]"
  - "[[pyarrow]]"
source_count: 2
observed_source_refs: 6
inbound_count: 13
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 4
---

# Apache Software Foundation (ASF)

## 개요

**Apache Software Foundation**은 1999년 설립된 미국 비영리 재단. **vendor-neutral OSS 거버넌스의 가장 큰 표준 모델 (PMC = Project Management Committee)**. 350+ 탑레벨 프로젝트, 8000+ 컨트리뷰터.

본 페이지는 **stub** — ASF 자체가 raw 수집 대상이 아닌 상태에서 16회차 [[kafka]] / [[parquet]] / [[pyarrow]] / dataframe-ecosystem-evolution 종합이 거버넌스 모델로 참조하므로 정합성 stub으로 등록.

## 16회차 발견 (본 위키 인용 맥락)

[[dataframe-ecosystem-evolution]]에서 **8번째 OSS 거버넌스 모델 = ASF PMC**로 명시:
- 단일 회사 흡수 불가 구조 (CLA + 위원회 합의 + 의장 순환)
- 다른 거버넌스 모델과의 차이점:
  - vs Anthropic/OpenAI 사내 (단일 회사 일방 통제)
  - vs Pydantic (BDFL)
  - vs Astral (회사 통제)
  - vs Community / Poimandres (분산 메인테이너)
  - vs NumFOCUS (보조 재정 후원만)
  - vs LangChain Inc. (회사 + OSS 듀얼)
  - vs CNCF (재단이지만 graduate 후 자율)
  - vs Open Code ([[shadcn-ui]] 의도적 fragmentation)

## ASF 산하 본 위키 인용 OSS

| OSS | 회차 | 본 위키 페이지 |
|---|---|---|
| Apache Kafka | 16 | [[kafka]] |
| Apache Arrow | 16 | [[pyarrow]] |
| Apache Parquet | 16 | [[parquet]] |
| (참고) Apache Spark | 미수집 | — |
| (참고) Apache Airflow | 미수집 | — |

## 16회차 핵심 발견 ("디스크는 친구")

[[kafka]] design.md 511줄의 사상이 ASF 산하 데이터 인프라 전체로 일반화:
- Kafka WAL / Parquet column chunk / Arrow immutable / Spark Shuffle 모두 sequential I/O + pagecache 위임
- 16회차 [[dataframe-ecosystem-evolution]] 핵심 결론

## CNCF와의 비교 (양대 vendor-neutral 재단)

| 항목 | ASF | CNCF |
|---|---|---|
| 영역 | 데이터·JVM·웹 | 클라우드 네이티브 |
| 거버넌스 모델 | PMC (위원회 합의) | TOC (graduate 후 자율) |
| 본 위키 사례 | 16회차 [[kafka]] / [[parquet]] / [[pyarrow]] | 19회차 [[prometheus]] |
| 위키 회차 | 16 | 21 (=19) |

## 관련 개념

- [[kafka]], [[parquet]], [[pyarrow]] — ASF 산하 본 위키 OSS 3종
- [[dataframe-ecosystem-evolution]] — ASF PMC 8번째 거버넌스 발견의 종합 페이지

## 출처

- [[apache-kafka]] — Apache Kafka와 ASF PMC 거버넌스 맥락
- [[apache-arrow]] — Apache Arrow/Parquet와 ASF 데이터 표준 맥락

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[apache-foundation]]` 깨진 링크 발견. 29회차에 기존 Apache Kafka/Arrow source 기반으로 1차 보강.
- 후속: ASF Way (메일링 리스트 / 위원회 / 의장 순환 / brand neutral) 운영 모델을 회사 BI OSS 기여 시 차용 가능 — 단, ASF 가입은 까다롭고 시간 소요.
