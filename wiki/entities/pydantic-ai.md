---
title: Pydantic AI
aliases:
- Pydantic AI
- 파이단틱 AI
type: entity
entity_type: tool
related:
- '[[pydantic]]'
- '[[langchain]]'
- '[[langgraph]]'
- '[[fastmcp]]'
- '[[openai-agents-python]]'
- '[[crewai]]'
- '[[deepagents]]'
- '[[agent-patterns]]'
- '[[agent-skills]]'
- '[[pydantic-pydantic-ai]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 2
inbound_count: 28
created: 2026-04-28
updated: 2026-04-28
tags:
- pydantic-ai
- type-safe-agent
- model-agnostic
- durable-execution
- mcp
- a2a
- logfire
- agents-md
- claude-md
cited_by_count: 14
---

# Pydantic AI

**Pydantic Validation을 만든 팀이 직접 출시한 type-safe agent framework** — "GenAI Agent Framework, the Pydantic way". 16.7K+ stars, MIT, **AGENTS.md = CLAUDE.md byte-for-byte (10K)**, 11가지 자체 강점.

## 기본 정보

- **저장소**: [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- **언어**: Python
- **License**: MIT
- **PyPI**: `pip install pydantic-ai`
- **회사**: Pydantic Services Inc. (Samuel Colvin)
- **공식 docs**: [ai.pydantic.dev](https://ai.pydantic.dev)
- **SaaS**: Pydantic Logfire ([pydantic.dev/logfire](https://pydantic.dev/logfire))

## 본질 — "FastAPI feeling for GenAI"

> "We built Pydantic AI with one simple aim: **to bring that FastAPI feeling to GenAI app and agent development**."

핵심 사상: Pydantic Validation은 **OpenAI SDK, Google ADK, Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor의 validation layer**. 이 layer를 만든 팀이 직접 agent framework로 위로 올라옴 → "원천에서 직접 시작".

## 11가지 자체 강점

| # | 강점 | 의의 |
|---|------|------|
| 1 | Built by the Pydantic Team | validation layer 원천 |
| 2 | Model-agnostic | ~25개 provider 지원 |
| 3 | Seamless Observability | Pydantic Logfire (OTel) |
| 4 | Fully Type-safe | Rust 사상 ("if it compiles, it works") |
| 5 | Powerful Evals | 시스템적 성능 평가 |
| 6 | Extensible by Design | composable Capability + YAML/JSON 정의 |
| 7 | MCP, A2A, and UI | MCP + Agent2Agent + UI event stream |
| 8 | HITL Tool Approval | 도구별 승인 게이트 |
| 9 | **Durable Execution** | LangGraph 12번째 패턴 합류 |
| 10 | Streamed Outputs | 즉시 검증 streaming |
| 11 | **Graph Support** | type-hint 기반 graph |

→ 강점 9·11번이 LangGraph의 핵심 영역(durable + graph)을 직접 커버. **12번째 패턴은 이제 LangGraph + Pydantic AI 양강 구도**.

## 6번째 AGENTS.md=CLAUDE.md 동기화

```bash
diff raw/articles/pydantic-pydantic-ai/AGENTS.md raw/articles/pydantic-pydantic-ai/CLAUDE.md
# (no output — identical 10K)
```

동기화 OSS 6개 그룹 합류:
1. langchain (292줄)
2. langgraph (57줄)
3. deepagents (364줄)
4. fastmcp (168줄, symlink)
5. openai-agents-python (12.9KB)
6. **pydantic-ai (10K, byte-for-byte)** ← 신규

## "Capability" 새 추상화

```python
search_capability = Capability(
    tools=[web_search, web_fetch],
    instructions="Search authoritative sources first",
)
agent = Agent(model="anthropic:claude-sonnet-4-6", capabilities=[search_capability])
```

→ DeepAgents의 "harness"보다 **fine-grained**: 도구만이 아닌 hooks/instructions/settings 번들. [Pydantic AI Harness](https://ai.pydantic.dev/harness/overview) 별도 제공.

## 대안 / 비교

| 도구 | 메타포 | type-safety | durable | model-agnostic |
|------|--------|-------------|---------|----------------|
| **Pydantic AI** | type-safe agent | ★★★ | ★★★ | ★★★ |
| [[langgraph]] | state graph | ★ | ★★★ | ★★ (LangChain 경유) |
| [[deepagents]] | harness | ★ | ★★★ (LangGraph 경유) | ★★ |
| [[crewai]] | Crews+Flows | ★ | ★★ | ★★ |
| [[openai-agents-python]] | RunState+11패턴 | ★★ | ★★ | ★ (OpenAI 락인) |
| [[fastmcp]] | MCP server | ★★ | N/A | N/A |

→ **Pydantic AI는 type-safety가 압도적**. Rust 사용자/static analysis 선호 팀에 적합.

## 통합

- **모델**: ~25개 provider 자체 통합 (LiteLLM/LangChain 의존 없음)
- **관측**: Pydantic Logfire (OTel SaaS) — 자체 SaaS
- **MCP**: 1급 지원
- **A2A**: Agent2Agent 표준 통합
- **UI**: event stream 표준

## 사용 예

```python
from pydantic_ai import Agent
from pydantic import BaseModel

class WeatherReport(BaseModel):
    city: str
    temp_c: float
    summary: str

agent = Agent(
    'anthropic:claude-sonnet-4-6',
    output_type=WeatherReport,
    instructions='Return weather as JSON matching the schema',
)
result = agent.run_sync('서울 날씨 알려줘')
print(result.output.temp_c)
```

→ **structured output이 1급**. dict/JSON 파싱 코드 없이 즉시 BaseModel 인스턴스.

## 의사결정 컨텍스트 (raw 인용)

> "GenAI Agent Framework, the Pydantic way — Pydantic Validation을 만든 팀이 직접 출시한 type-safe agent framework. 16.7K+ stars, MIT, AGENTS.md = CLAUDE.md byte-for-byte 동기화 (10K), 11가지 자체 강점 명시."
> — [[pydantic-pydantic-ai]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] type-safe agent 영역. [[pydantic]] 본진 팀 + [[fastapi]]와 같은 타입 힌트 우선 패턴. [[matechat|MateChat 사이드 프로젝트]] 39 SKILL 운영에서 type-safe orchestration 후보. **AGENTS.md=CLAUDE.md byte-for-byte 동기화**는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 [[agent-skills]] 8단계 진화 핵심 사례 — [[ruff]]·[[uv]]·[[langchain]]·[[fastmcp]]와 같은 동기화 모델.

## 출처

- [[pydantic-pydantic-ai]] — Pydantic AI

## 관련

- [[pydantic]] — 모회사 Pydantic Services Inc.
- [[langgraph]] — 12번째 패턴 양강
- [[fastmcp]] — MCP 직교 통합
- [[openai-agents-python]] — 동급 SDK
- [[agent-patterns]] — 11가지 자기 강점 = 평가 축
