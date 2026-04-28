---
title: "Agent Frameworks Matrix — LangGraph vs OpenAI Agents SDK (1차)"
type: synthesis
category: ai
tags: [comparison, agent-framework, langgraph, openai-agents-python, fastmcp, langchain, decision-matrix, durable-execution, state-machine, mcp, 17회차]
sources:
  - "[[langchain-ai-langgraph]]"
  - "[[langchain-ai-langchain]]"
  - "[[openai-openai-agents-python]]"
  - "[[jlowin-fastmcp]]"
created: 2026-04-28
updated: 2026-04-28
---

# Agent Frameworks Matrix — LangGraph vs OpenAI Agents SDK (1차)

> **17회차 1차 작성** — LangGraph + OpenAI Agents SDK 정량 비교. **18회차에서 DeepAgents / Crew AI / Pydantic AI / Pandas AI 추가 예정**.

## 1. 큰 그림

같은 영역(stateful LLM agent 프레임워크)에 **두 가지 다른 메타포**:

- **LangGraph**: "Pregel-style state graph" — 분산 워커 그래프, BSP, checkpoint
- **OpenAI Agents SDK**: "ChatCompletions에 가까운 운영 SOP" — RunState + 11종 패턴 reference

**FastMCP**는 둘 다와 직교. **LangChain**은 LangGraph 위의 고수준 통합.

## 2. 정량 비교 매트릭스

| 항목 | [[langgraph]] | [[openai-agents-python]] | [[fastmcp]] | [[langchain]] |
|------|---------------|--------------------------|-------------|---------------|
| **첫 릴리스** | 2024 | 2024 | 2024 | 2022-10 |
| **회사** | LangChain Inc. | OpenAI | PrefectHQ | LangChain Inc. |
| **License** | MIT | MIT | Apache 2.0 | MIT |
| **본질** | state graph 엔진 | multi-agent SDK | MCP 프레임워크 | agent platform |
| **Stars (★)** | ~10K+ | ~25K | ~15K+ | ~80K+ |
| **메타포** | **Pregel + Apache Beam + NetworkX** | **ChatCompletions + RunState** | **MCP + Servers/Apps/Clients** | **chains + agents + integrations** |
| **상태 모델** | 명시적 State graph | RunState (CURRENT_SCHEMA_VERSION) | 컴포넌트별 (`FastMCPComponent.key`) | 추상화 다층 |
| **영속성** | **checkpoint Postgres/SQLite 1급** | RunState 직렬화 | 전송 layer 외부 | LangGraph 경유 |
| **Human-in-the-loop** | **상태 그래프 어디서든 interrupt** | 3종 reference 구현 | 호스트 클라이언트가 처리 | LangGraph 경유 |
| **Reference 패턴 수** | (그래프 자체) | **11종** (Anthropic 5 + OpenAI 6) | 3-pillars (Servers/Apps/Clients) | LangGraph 경유 |
| **MCP 통합** | LangChain partners 경유 | `mcp>=1.19.0` 디폴트 | **본체** | partners/anthropic 경유 |
| **monorepo** | libs/9개 | 단일 패키지 + 9 SOP 스킬 | 단일 패키지 | libs/7개 |
| **AGENTS.md=CLAUDE.md** | ✅ 57줄 | ✅ 12.9KB byte-for-byte | ✅ symlink 168줄 | ✅ 292줄 |
| **OSS+SaaS 듀얼** | LangSmith | OpenAI Platform | **Prefect Horizon** | LangSmith |
| **언어** | Python + JS/TS (sdk-js) | Python | Python | Python + JS/TS |
| **의존성** | uv | uv | uv | uv |
| **Production 검증** | **Klarna/Replit/Elastic 명시** | OpenAI 자체 운영 | 일일 100만 다운로드, MCP 70% | LangSmith deployments |
| **학술적 계보** | Pregel·Apache Beam·NetworkX | ChatCompletions API | MCP spec | (없음) |

## 3. 12 패턴 매핑 비교

### Anthropic 5 패턴
| 패턴 | LangGraph | OpenAI Agents SDK |
|------|-----------|---------------------|
| Prompt Chaining | `StateGraph` 순차 노드 | `examples/agent_patterns/deterministic.py` |
| Routing | conditional edge | `examples/agent_patterns/routing.py` |
| Parallelization | `Send()` API | `examples/agent_patterns/parallelization.py` |
| Orchestrator-Workers | sub-graph + `Send()` | `examples/agent_patterns/agents_as_tools.py` (4종 변형) |
| Evaluator-Optimizer | conditional loop | `examples/agent_patterns/llm_as_a_judge.py` |

### OpenAI 확장 6 패턴
| 패턴 | LangGraph | OpenAI Agents SDK |
|------|-----------|---------------------|
| Input Guardrail | input validation node | `input_guardrails.py` |
| Output Guardrail | output validation node | `output_guardrails.py` |
| Streaming Guardrail | streaming + interrupt | `streaming_guardrails.py` |
| HITL (approval) | `interrupt()` API | `human_in_the_loop.py` |
| HITL (rejection) | conditional + interrupt | `human_in_the_loop_custom_rejection.py` |
| Forced tool use | `tool_calls` 강제 | `forcing_tool_use.py` |

### LangGraph 12번째 패턴 (17회차 추가)
| 패턴 | LangGraph (네이티브) | OpenAI Agents SDK |
|------|---------------------|---------------------|
| **State-Machine + Durable Execution** | **checkpoint(Postgres/SQLite)** + `interrupt()` 1급 | RunState 직렬화로 부분 지원 |

→ **12번째 패턴은 LangGraph가 사실상 정의한 영역**. OpenAI Agents SDK는 RunState로 **부분 지원**하나 production checkpoint backend는 미내장.

## 4. 의사결정 트리

```
Q1: 프로젝트가 OpenAI 모델만 사용할 계획인가?
  YES → OpenAI Agents SDK (가장 단순, 가이드 풍부)
  NO ↓

Q2: 모델 swap (OpenAI/Anthropic/Google/local) 필요한가?
  YES → LangChain + LangGraph
  NO ↓

Q3: durable execution / checkpoint persistence 필수인가?
  YES → LangGraph (1급)
  NO ↓

Q4: MCP 서버를 우선 만들고 싶은가?
  YES → FastMCP (다른 프레임워크와 직교)
  NO → OpenAI Agents SDK (가장 빠른 시작)
```

## 5. 핵심 결정 요인

| 요인 | LangGraph | OpenAI Agents SDK | FastMCP | LangChain |
|------|-----------|---------------------|---------|-----------|
| **모델 다양성** | ★★★ (LangChain partners) | ★ (OpenAI only) | N/A | ★★★ |
| **학습 곡선** | ★★ (그래프 추상화) | ★★★ (직관적) | ★★★ (decorator) | ★ (다층 추상화) |
| **Production 검증** | ★★★ (Klarna/Replit) | ★★ (OpenAI 자체) | ★★★ (70% 점유) | ★★ |
| **Durable execution** | ★★★ | ★★ | N/A | LangGraph 경유 |
| **MCP 통합 깊이** | ★★ (partners) | ★★ (디폴트) | ★★★ | ★★ |
| **HITL 가이드** | ★★★ (interrupt 1급) | ★★★ (3종 reference) | ★ (호스트 위임) | LangGraph 경유 |
| **Vendor 락인 위험** | ★ (LangSmith 선택) | ★★★ (OpenAI 락인) | ★ (호스트 무관) | ★ (LangSmith 선택) |
| **PR/거버넌스** | LangChain Inc. | OpenAI | PrefectHQ | LangChain Inc. |
| **AGENTS.md=CLAUDE.md** | ✅ | ✅ | ✅ | ✅ |

## 6. "조합" 시나리오 (권장)

### 시나리오 A — 회사 BI 챗봇 (석근님 c2spf-analytics)

```python
# LangGraph state graph + FastMCP server + LangChain integrations
import fastmcp
from langgraph.checkpoint.postgres import PostgresSaver
from langgraph.graph import StateGraph
from langchain.chat_models import init_chat_model

# 1) FastMCP: BigQuery·Grafana·Sentry를 MCP server로 wrap
mcp_server = fastmcp.FastMCP("BI-Tools")

@mcp_server.tool
def query_bigquery(sql: str) -> dict: ...

# 2) LangGraph: 분석 챗봇을 state machine으로
checkpointer = PostgresSaver(...)
graph = StateGraph(...).add_node(...).add_edge(...).compile(checkpointer=checkpointer)

# 3) LangChain: 모델 swap (gpt-5 / claude / local)
model = init_chat_model("openai:gpt-5.4")  # 또는 anthropic:sonnet-4.6
```

→ 3개 프레임워크 **상호보완**: FastMCP=도구, LangGraph=흐름, LangChain=모델.

### 시나리오 B — OpenAI-only 빠른 PoC

```python
from agents import Agent, Runner

agent = Agent(
    name="Reporter",
    instructions="...",
    tools=[...],
    input_guardrails=[...],
)
result = await Runner.run(agent, "...")
```

→ OpenAI Agents SDK 단독. 11종 패턴 reference 직접 활용.

### 시나리오 C — 개인 비서 MCP

```python
from fastmcp import FastMCP
mcp = FastMCP("Personal Assistant")

@mcp.tool
def search_notion(query: str) -> str: ...
```

→ FastMCP 단독. Cursor/Claude Code 클라이언트 sandbox.

## 7. 18회차 추가 예정

다음 회차에서 매트릭스에 추가될 4개 프레임워크:

- **DeepAgents** ([[langchain]] 산하) — plan + subagents + 파일시스템, 복잡 작업
- **Crew AI** — 다중 에이전트 협업의 또 다른 프레임워크
- **Pandas AI** — DataFrame에 자연어 인터페이스
- **Pydantic AI** — Pydantic 모델 기반 LLM 에이전트

## 8. 결론 (17회차 시점)

**LangGraph + OpenAI Agents SDK는 같은 영역의 두 메타포**. 셋 다 사용이 정답에 가까움:

- **OpenAI Agents SDK**: 11종 패턴 reference + OpenAI 락인을 감수할 수 있는 PoC
- **LangGraph**: durable + multi-vendor + production-grade
- **FastMCP**: 모든 프레임워크가 의존하는 도구 layer

**석근님 c2spf-analytics 권장**: 게임 데이터 BI 챗봇은 **LangGraph state machine + FastMCP BI 도구 + LangChain 모델 추상화** 3-layer가 reference. checkpoint-postgres로 대화 영속성, MCP로 BigQuery/Grafana 연결, LangChain init_chat_model로 OpenAI/Anthropic 동시 실험.

## 출처

- [[langchain-ai-langgraph]] — LangGraph (17회차 수집)
- [[openai-openai-agents-python]] — OpenAI Agents Python SDK (14회차)
- [[jlowin-fastmcp]] — FastMCP (17회차)
- [[langchain-ai-langchain]] — LangChain (17회차)
- [[agent-patterns]] — 12 패턴 (Anthropic 5 + OpenAI 6 + LangGraph 1)
- [[mcp]] — Model Context Protocol

## 후속 작업

- 18회차에서 DeepAgents/Crew AI/Pandas AI/Pydantic AI 6×N 매트릭스로 확장
- 실제 c2spf-analytics PoC 코드 작성 → BigQuery NL2SQL state machine reference
- Temporal vs LangGraph durable execution 정량 비교 (별도 문서)
