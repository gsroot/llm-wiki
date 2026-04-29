---
title: "PandasAI"
type: entity
entity_type: tool
related:
  - "[[pandas]]"
  - "[[polars]]"
  - "[[duckdb]]"
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[sinaptik-ai-pandas-ai]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
tags: [pandas-ai, nl2dataframe, conversational-data, litellm, sinaptik-ai, bi-chatbot, 18회차]
---

# PandasAI

**DataFrame을 자연어로 대화하는 라이브러리** — pandas DataFrame에 `.chat("질문")` 메서드를 추가하는 어댑터. LiteLLM으로 다중 모델 지원. 23.5K+ stars, MIT.

## 기본 정보

- **저장소**: [sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai)
- **언어**: Python (3.8~3.11)
- **License**: MIT
- **PyPI**: `pip install pandasai pandasai-litellm`
- **회사**: Sinaptik AI
- **공식 docs**: [docs.pandas-ai.com](https://docs.pandas-ai.com)

## 역할 — "natural language extension"

```python
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

llm = LiteLLM(model="gpt-4.1-mini", api_key="...")
pai.config.set({"llm": llm})

df = pai.read_csv("data/companies.csv")
response = df.chat("What is the average revenue by region?")
```

핵심 가치: **`df.chat(...)` 한 줄로 NL2DataFrame**. 비기술 사용자도 분석 결과 획득.

## 데이터 소스 다양성

```
SQL ──┐
CSV ──┼─→ pai.read_*() → DataFrame.chat()
Parquet─┤
PostgreSQL─┘
```

→ 16회차 데이터 레이어 ([[polars]], [[duckdb]], [[parquet]], [[pyarrow]])의 **자연어 인터페이스 어댑터**.

## 시각화 자동 생성

```python
df.chat("Plot the histogram of countries showing for each one the gdp...")
# → matplotlib 차트 자동 반환
```

→ LLM이 코드 생성·실행. **sandbox/Docker 격리 권장**.

## 한계

| 한계 | 영향 |
|------|------|
| **AGENTS.md/CLAUDE.md 없음** | 18회차 6개 동기화 OSS 그룹 미합류 |
| **Python 3.8~3.11만 지원** | 최신 3.12+ 사용자 호환성 문제 |
| **자체 모델 추상화 없음** | LiteLLM 종속 (단점이자 장점) |
| **LLM이 코드 실행** | sandbox 필요, 보안 위험 |

## 대안 / 비교

| 도구 | 영역 | 장점 | 단점 |
|------|------|------|------|
| **PandasAI** | NL2DataFrame 어댑터 | 적은 코드, BI PoC 1순위 | 의존성 보수적 |
| [[langchain]] + tool | NL2BI 일반 에이전트 | 풍부한 생태계 | 코드 양 많음 |
| [[deepagents]] | LangGraph 기반 | durable execution | 무거움 |
| [[duckdb]] (직접) | SQL 쿼리 | 빠름, 검증 가능 | NL 인터페이스 직접 구현 필요 |

→ PandasAI는 **PoC/프로토타입 단계 BI 챗봇**에 최적. 운영 단계는 LangGraph + checkpoint로 마이그레이션 권장.

## 통합

- **모델**: LiteLLM 경유 (OpenAI/Anthropic/Gemini/Local)
- **데이터**: pandas/SQL/Parquet/CSV 모두
- **시각화**: matplotlib

## 사용 예 (BI 챗봇)

```python
import pandasai as pai
from pandasai_litellm.litellm import LiteLLM

llm = LiteLLM(model="anthropic:claude-haiku-4-5", api_key="...")
pai.config.set({"llm": llm})

sales = pai.read_csv("sales.csv")
users = pai.read_csv("users.csv")
result = pai.chat([sales, users], "Which user segment spent the most this quarter?")
```

→ 석근님 c2spf-analytics에서 **여러 테이블 join 자연어 질의** PoC에 적합.

## 의사결정 컨텍스트 (raw 인용)

> "Chat with your database or your datalake (SQL, CSV, parquet) — pandas DataFrame에 .chat('질문') 메서드를 추가하는 어댑터. LiteLLM으로 다중 모델 지원."
> — [[sinaptik-ai-pandas-ai]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] BI 자연어 인터페이스 영역. [[c2spf-analytics|c2spf 게임 데이터 BI]] BigQuery 기반 분석에서 비개발자 셀프서비스 후보 (df.chat 패턴). [[matechat|MateChat 사이드 프로젝트]] 채팅 분석 모듈에서 BigQuery 결과 자연어 질의 후보. [[pandas]] 본진 + [[langchain]] 위에 빌드. NL2SQL의 사실상 표준이자 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 BI ↔ LLM 브리지 사례.

## 출처

- [[sinaptik-ai-pandas-ai]] — PandasAI (18회차)

## 관련

- [[pandas]] — 어댑터 대상
- [[polars]], [[duckdb]] — 대안 데이터프레임
- [[langchain]], [[langgraph]] — 운영 단계 마이그레이션 후보
