---
title: "Python"
type: entity
entity_type: language
tags: [python, language, dynamic-typing, gil, asyncio, 23회차]
related:
  - "[[fastapi]]"
  - "[[uv]]"
  - "[[pydantic]]"
  - "[[sqlalchemy]]"
  - "[[pandas]]"
  - "[[polars]]"
  - "[[duckdb]]"
  - "[[scikit-learn]]"
  - "[[langchain]]"
  - "[[openai-agents-python]]"
source_count: 8
observed_source_refs: 8
inbound_count: 14
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 10
---

# Python

## 개요

**Python**은 1991년 Guido van Rossum이 발표한 **고수준 동적 언어**. 석근의 **주 언어**이자 본 위키 백엔드/데이터/ML/LLM 스택의 공통 호스트.

본 페이지는 **stub** — CPython 저장소(python/cpython)는 raw 수집 대상이 아니지만, 위키 절반 이상의 엔티티가 `[[python]]` 참조 후보로 정합성을 위해 등록.

## 본 위키에서 Python 위에 빌드된 도구

| 영역 | 도구 |
|---|---|
| **백엔드** | [[fastapi]], [[sqlalchemy]], [[alembic]], [[redis]] (클라이언트), [[pydantic]] |
| **데이터** | [[pandas]], [[polars]] (Rust+Py), [[duckdb]] (C+++Py), [[pyarrow]] |
| **ML 클래식** | [[scikit-learn]], [[lightgbm]] |
| **LLM 인프라** | [[langchain]], [[langgraph]], [[fastmcp]], [[deepagents]], [[crewai]], [[pandas-ai]], [[pydantic-ai]] |
| **OpenAI** | [[openai-agents-python]] |
| **도구 체인** | [[uv]] (패키지/환경), [[ruff]] (린터/포매터) |

## 핵심 진화 축 (위키 통합 시각)

| 시기 | 트렌드 | 본 위키 인용 OSS |
|---|---|---|
| 2008~ | 데이터 분석 표준화 | [[pandas]] |
| 2014~ | ML 표준화 | [[scikit-learn]] |
| 2016~ | 비동기 (asyncio) | [[fastapi]] |
| 2018~ | 타입 힌트 + 검증 | [[pydantic]] |
| 2020~ | Rust 가속 | [[ruff]], [[uv]], [[polars]] |
| 2023~ | LLM 에이전트 | [[langchain]], [[langgraph]], [[openai-agents-python]] 등 |

## 관련 개념

- [[fastapi]] — 본 위키의 Python 백엔드 핵심
- [[uv]] / [[ruff]] — Astral의 Python 도구 체인 혁신
- [[dataframe-ecosystem-evolution]] — Pandas → PyArrow → Polars → DuckDB의 Python 데이터 표준 진화
- [[backend-fastapi-stack]] — Python 백엔드 6단 표준
- [[agent-frameworks-matrix]] — Python LLM 에이전트 프레임워크 6×N 비교

## 출처

- [[fastapi-fastapi]] — Python ASGI 백엔드 표준
- [[pydantic-pydantic]] — Python type/validation 체인
- [[sqlalchemy-sqlalchemy]] — Python ORM/SQL toolkit
- [[astral-sh-uv]] — Python 패키징/환경 관리
- [[astral-sh-ruff]] — Python lint/format 도구 체인
- [[pandas-dev-pandas]] — Python 데이터프레임 표준
- [[scikit-learn-scikit-learn]] — Python ML 표준 API
- [[openai-openai-agents-python]] — Python LLM agent SDK

## 메모

- 23회차 stub 사유: 위키 ~30개 엔티티가 Python 위에 빌드되어 `[[python]]` 참조. 29회차에 백엔드/데이터/ML/LLM source 8개 기반으로 1차 보강.
- 위키 안에서 Python의 위치 = "보이지 않는 호스트". 모든 백엔드/데이터/ML/LLM 페이지가 암묵적으로 Python을 가정.
- 후속 작업: Python 3.13 GIL 옵션화(PEP 703) + free-threaded build의 본 위키 도구 영향 추적.
