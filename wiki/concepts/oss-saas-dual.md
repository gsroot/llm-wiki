---
title: "OSS+SaaS 듀얼 모델"
type: concept
category: oss-governance
tags: [oss-saas-dual, governance, business-model, langchain, polars, crewai, 25회차]
related:
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[polars]]"
  - "[[duckdb]]"
  - "[[fastmcp]]"
  - "[[crewai]]"
source_count: 5
created: 2026-04-28
updated: 2026-04-29
---

# OSS+SaaS 듀얼 모델

## 정의

**OSS+SaaS 듀얼 모델** = 동일 회사가 (a) 오픈소스 라이브러리 + (b) 상용 호스팅·플랫폼 SaaS를 동시 운영해 OSS 채택을 SaaS 매출로 전환하는 비즈니스 모델. 18회차 [[agent-frameworks-matrix]]에서 식별된 거버넌스 패턴.

본 페이지는 **stub** — 17/18회차 다수 OSS에서 인용되므로 정합성 stub.

## 18회차까지 누적된 사례 5+1개

| # | OSS | SaaS | 회사 |
|---|---|---|---|
| 1 | [[polars]] | Polars Cloud | Polars Inc. |
| 2 | [[duckdb]] | MotherDuck | DuckDB Labs (DuckDB Foundation 분리) |
| 3 | [[langchain]] / [[langgraph]] | LangSmith / LangGraph Cloud | LangChain Inc. |
| 4 | [[fastmcp]] | FastMCP Cloud (관리형 MCP 서버) | Prefect (Jeremiah Lowin) |
| 5 | [[crewai]] | app.crewai.com / Crew Control Plane | crewAIInc |
| 6 | Pydantic | Pydantic Logfire (관측성 SaaS) | Pydantic Services |

## 듀얼 모델 vs 다른 거버넌스

| 모델 | 회사·재단 | OSS와 SaaS 관계 |
|---|---|---|
| **OSS+SaaS 듀얼** | OSS = 오픈, SaaS = 상용 | 같은 회사 통제 |
| 단일 회사 (Anthropic/OpenAI) | OSS는 보조, SaaS가 주력 | API/모델 자체가 SaaS |
| 재단 (ASF/CNCF/NumFOCUS) | 회사 흡수 불가 | SaaS 별도 회사 (Confluent / Databricks 등) |
| Open Code ([[shadcn-ui]]) | 의존성 없음 | SaaS 부재 (디자인 자산만) |

## 라이선스 전략 변화

- **단순 MIT/Apache** (대다수): OSS 제한 없음, SaaS 가격으로만 수익
- **AGPL** ([[grafana]]): 사외 SaaS 시 소스 공개 의무 → AWS 등 클라우드 fork 방지
- **BSL → 자동 OSS** ([[sentry]]): 4년 유예 후 Apache-2.0 자동 전환
- **RSALv2/SSPL** ([[redis]] 8.0+): DBaaS 운영자 대상 — 자체 사용은 무관

## 회사 BI 응용

- BigQuery는 closed lakehouse SaaS, MotherDuck (DuckDB SaaS)으로 일부 BI 워크로드 분산 가능 — 비용 절감 + 벤더 락인 회피
- LangSmith는 회사 LLM 워크플로우 관측성에 직접 도입 가능

## 관련 개념

- [[langchain]] / [[langgraph]] / [[polars]] / [[duckdb]] / [[fastmcp]] / [[crewai]] — 듀얼 모델 사례
- [[agent-frameworks-matrix]] — 18회차 듀얼 모델 식별 종합 페이지

## 출처

- [[langchain-ai-langchain]] — LangChain OSS와 LangSmith/LangGraph Platform의 회사형 듀얼 모델
- [[pola-rs-polars]] — Polars OSS와 Polars Cloud
- [[duckdb-duckdb]] — DuckDB Foundation/Labs와 MotherDuck 분리
- [[jlowin-fastmcp]] — FastMCP OSS와 FastMCP Cloud
- [[crewaiinc-crewai]] — CrewAI OSS와 Crew Control Plane

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[oss-saas-dual]]` 깨진 링크 발견. 29회차에 기존 source 기반으로 1차 보강.
- 후속: 듀얼 모델 매출 비교 데이터 수집 (Confluent / Databricks / LangChain Inc 등 IPO 자료) → 비즈니스 모델 평가 종합 페이지.
