---
title: PandasAI — DataFrame을 자연어로 대화하는 라이브러리
type: source
source_type: github_repo
source_url: https://github.com/sinaptik-ai/pandas-ai
raw_path: raw/articles/sinaptik-ai-pandas-ai/
author: Sinaptik AI
date_published: 2023
date_ingested: 2026-04-28
related:
- '[[pandas-ai]]'
- '[[pandas]]'
- '[[polars]]'
- '[[duckdb]]'
- '[[langchain]]'
confidence: medium
tags:
- pandas-ai
- conversational-data
- litellm
- dataframe
- bi-chatbot
inbound_count: 8
aliases:
- PandasAI — DataFrame을 자연어로 대화하는 라이브러리
- Sinaptik Ai Pandas
- sinaptik ai pandas
cited_by:
  - "[[agent-frameworks-matrix]]"
  - "[[ml-ai]]"
  - "[[pandas-ai]]"
cited_by_count: 3
---

# PandasAI — DataFrame을 자연어로 대화하는 라이브러리

## 한 줄 요약

**"Chat with your database or your datalake (SQL, CSV, parquet)"** — pandas DataFrame에 `.chat("질문")` 메서드를 추가하는 어댑터. LiteLLM으로 다중 모델 지원. 23K+ stars.

## 5섹션 요약

### 1) 본질 — pandas의 "natural language extension"

```python
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

llm = LiteLLM(model="gpt-4.1-mini", api_key="...")
pai.config.set({"llm": llm})

df = pai.read_csv("data/companies.csv")
response = df.chat("What is the average revenue by region?")
```

→ 핵심은 **`df.chat(...)`** 한 줄. 사용자는 SQL/pandas 모르고도 분석 결과 획득.

### 2) 다중 LLM 지원 = LiteLLM 의존

PandasAI는 **자체 모델 추상화 없음** — `pandasai-litellm` 어댑터로 [LiteLLM](https://github.com/BerriAI/litellm)에 위임. **OpenAI/Anthropic/Gemini/Local 모두 지원**.

→ LangChain의 `init_chat_model`과 동일 사상: **모델 swap을 위해 LiteLLM 또는 LangChain partners 필요**.

### 3) 데이터 소스 다양성

```
SQL ──┐
CSV ──┼─→ pai.read_* → DataFrame.chat
Parquet─┤
PostgreSQL─┘
```

→ **데이터 레이어 수집 (Polars/DuckDB/PyArrow/Parquet)** 대상의 **자연어 인터페이스 어댑터**. PandasAI는 데이터 자체가 아닌 **대화형 어댑터** 카테고리.

### 4) 시각화 자동 생성

```python
df.chat("Plot the histogram of countries showing for each one the gdp...")
# → matplotlib 차트 자동 반환
```

→ **LLM이 코드를 생성·실행하여 차트 산출**. 보안상 sandbox/Docker 격리 필요 — README는 위험 명시.

### 5) Multiple DataFrames 비교

PandasAI는 **여러 DataFrame을 동시에 전달**받아 join/비교 질문 가능. 이는 BI 챗봇 시나리오에서 핵심:

```python
df1 = pai.read_csv("sales.csv")
df2 = pai.read_csv("customers.csv")
result = pai.chat([df1, df2], "Which customers spent the most this quarter?")
```

→ 석근님 c2spf-analytics에서 **여러 BigQuery 테이블 join 자연어 질의**가 핵심 use case. PandasAI는 이 특정 시나리오에 최적화.

## 결정적 인용

> "PandasAI is a Python library that makes it easy to ask questions to your data in natural language."
>
> "It helps non-technical users to interact with their data in a more natural way, and it helps technical users to save time, and effort when working with data."

## 한계

- **AGENTS.md 없음** — 6개 동기화 OSS 그룹에 미합류 (LangChain/LangGraph/DeepAgents/FastMCP/OpenAI Agents/PydanticAI 모두 보유)
- **Python 3.8~3.11만 지원** — 최신 Python 3.12+ 미지원, 다른 프레임워크보다 보수적
- **자체 모델 추상화 없음** — LiteLLM 종속

## 의의

- **BI 챗봇 PoC 1순위** — 적은 코드로 가장 빠른 NL2DataFrame 결과
- **LangGraph + DeepAgents의 보완재** — durable agent에 PandasAI를 도구로 wrap하여 결합 가능

## 출처

- README.md (203줄, ~5.7KB)
- https://github.com/sinaptik-ai/pandas-ai
- https://docs.pandas-ai.com
