---
title: Agent Frameworks Matrix — 6 프레임워크 정량 비교 (2차, 18회차 6×N 확장)
type: synthesis
category: ai
tags:
- comparison
- agent-framework
- langgraph
- openai-agents-python
- fastmcp
- langchain
- deepagents
- crewai
- pydantic-ai
- pandas-ai
- decision-matrix
- durable-execution
- state-machine
- mcp
- 17회차
- 18회차
sources:
- '[[langchain-ai-langgraph]]'
- '[[langchain-ai-langchain]]'
- '[[langchain-ai-deepagents]]'
- '[[openai-openai-agents-python]]'
- '[[jlowin-fastmcp]]'
- '[[crewaiinc-crewai]]'
- '[[pydantic-pydantic-ai]]'
- '[[sinaptik-ai-pandas-ai]]'
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 18
inbound_count: 23
related:
- '[[agent-patterns]]'
- '[[mcp]]'
---

# Agent Frameworks Matrix — 6 프레임워크 정량 비교 (2차, 18회차 6×N 확장)

> **17회차 1차** — LangGraph + OpenAI Agents SDK 비교. **18회차 2차 확장** — DeepAgents / CrewAI / Pydantic AI / PandasAI 4개 추가 → **6 프레임워크 + FastMCP/LangChain 직교 layer 동시 매트릭스**.

## 1. 큰 그림 (18회차 확장)

이제 6개 agent 프레임워크 + 2개 직교 layer가 동일 매트릭스에 들어옴:

**상단 (Agent runtime/SDK):**
- **LangGraph**: "Pregel-style state graph" — 분산 워커 그래프, BSP, checkpoint
- **OpenAI Agents SDK**: "RunState + 11종 패턴 reference" — OpenAI 자체 운영 SOP
- **DeepAgents**: "harness — LangGraph 위 batteries-included 프리셋"
- **CrewAI**: "Crews + Flows" — role-playing + enterprise event-driven, **LangChain 독립**
- **Pydantic AI**: "type-safe agent" — 11가지 자기 강점, Capability 추상화
- **PandasAI**: "NL2DataFrame 어댑터" — 다른 5개와 다른 카테고리 (특화)

**직교 layer:**
- **FastMCP**: 도구 layer (모든 프레임워크가 의존)
- **LangChain**: 모델 추상화 + partners 생태계

## 2. 정량 비교 매트릭스 (6×N — 18회차 확장)

### 2-1. Agent runtime/SDK 6종 (수평 확장)

| 항목 | [[langgraph]] | [[openai-agents-python]] | [[deepagents]] | [[crewai]] | [[pydantic-ai]] | [[pandas-ai]] |
|------|---------------|--------------------------|----------------|------------|-----------------|----------------|
| **첫 릴리스** | 2024 | 2025-03 | 2025-09 | 2024 | 2024 | 2023 |
| **회사** | LangChain Inc. | OpenAI | LangChain Inc. | CrewAI Inc. | Pydantic Services | Sinaptik AI |
| **License** | MIT | MIT | MIT | MIT | MIT | MIT |
| **Stars (★)** | ~10K+ | ~25K | (신규, < 5K) | ~50K | ~16.7K | ~23.5K |
| **메타포** | state graph (Pregel) | RunState + 11패턴 | "harness" 프리셋 | Crews + Flows | type-safe agent | NL2DataFrame |
| **본질** | state machine 엔진 | multi-agent SDK | LangGraph 프리셋 | role-playing | type-safe SDK | DataFrame 어댑터 |
| **상태 모델** | 명시적 State graph | RunState (SCHEMA_VERSION) | LangGraph 상속 | Crew/Flow 자체 | type-hint graph | DataFrame |
| **영속성** | **checkpoint 1급** | RunState 직렬화 | LangGraph 상속 1급 | Crew Control Plane | **durable execution 1급** | (없음) |
| **HITL** | `interrupt()` 1급 | 3종 reference | LangGraph 상속 | Flow event 시스템 | **Tool Approval 1급** | (없음) |
| **Type-safety** | ★ | ★★ | ★ | ★ | **★★★ (압도적)** | ★ |
| **Model-agnostic** | ★★ (LC partners) | ★ (OpenAI 락인) | ★★ (LC) | ★★ (자체) | **★★★ (~25 provider)** | ★★★ (LiteLLM) |
| **Reference 패턴 수** | (그래프 자체) | **11종 (Anthropic 5 + OpenAI 6)** | 4종 도구 빌트인 | Crews/Flows 변형 | 11가지 자기 강점 | (특화) |
| **MCP 통합** | LC partners | `mcp>=1.19.0` | langchain-mcp-adapters | 직접 구현 | **1급 + A2A** | (간접) |
| **OSS+SaaS 듀얼** | LangSmith | OpenAI Platform | LangSmith | **Crew Control Plane** | **Pydantic Logfire** | (없음) |
| **monorepo** | libs/9개 | 단일 + 9 SOP 스킬 | libs/3개 | 단일 | 단일 | 단일 |
| **AGENTS.md=CLAUDE.md** | ✅ 57줄 | ✅ 12.9KB | ✅ 364줄 | ✗ | ✅ 10K byte-for-byte | ✗ |
| **언어** | Python + JS/TS | Python | Python + JS/TS | Python | Python | Python (3.8~3.11) |
| **Production 검증** | **Klarna/Replit/Elastic** | OpenAI 자체 | (신규) | 100K+ 인증 개발자 | Pydantic 팀 운영 | 다수 BI PoC |
| **학술적 계보** | Pregel·Apache Beam·NetworkX | ChatCompletions API | Anthropic SWE Agent 패턴 | (자체) | FastAPI/Pydantic 사상 | (어댑터) |
| **Capability/Harness** | ✗ | ✗ | "harness" 1급 | (Crews=harness 유사) | **Capability 1급** | ✗ |
| **YAML/JSON agent 정의** | ✗ | ✗ | ✗ | ✗ (코드 우선) | **✅ YAML/JSON** | ✗ |
| **OpenTelemetry** | LangSmith 경유 | OpenAI Platform | LangSmith | 자체 + OTel | **자체 OTel + Logfire** | ✗ |

### 2-2. 직교 layer (FastMCP / LangChain)

| 항목 | [[fastmcp]] | [[langchain]] |
|------|-------------|---------------|
| 본질 | MCP 프레임워크 | 모델 추상화 + 통합 platform |
| 의존 관계 | 6개 모두와 직교 | LangGraph/DeepAgents의 모델 layer |
| Production | MCP 70% 점유, 일일 100만 다운로드 | partners 거대 생태계 |
| AGENTS.md=CLAUDE.md | ✅ symlink 168줄 | ✅ 292줄 |
| OSS+SaaS | Prefect Horizon | LangSmith |

## 2-3. 18회차 횡단 발견 (5가지)

1. **AGENTS.md=CLAUDE.md 동기화 = 6개 OSS 표준** — LangChain/LangGraph/DeepAgents/FastMCP/OpenAI Agents/Pydantic AI 모두 채택. CrewAI/PandasAI 미채택 (LangChain 진영 + OpenAI/Pydantic 진영 vs 독립 진영의 거버넌스 분기점)
2. **5번째 OSS+SaaS 듀얼** — Crew Control Plane 추가 (Polars/DuckDB/LangChain/FastMCP/CrewAI). Pydantic Logfire는 6번째.
3. **12번째 패턴(durable execution) 양강 구도** — LangGraph + Pydantic AI. DeepAgents는 LangGraph 상속.
4. **type-safety 차원의 압도적 우위** — Pydantic AI만 ★★★. 다른 프레임워크는 type-hint를 보조 도구로만 사용.
5. **YAML/JSON agent 정의** — Pydantic AI 단독. **코드 없는 agent 정의**는 Pydantic AI만 1급 지원 (다른 프레임워크는 모두 코드 우선).

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

## 4. 의사결정 트리 (18회차 6×N 갱신)

```
Q1: NL2DataFrame BI PoC를 만들고 싶은가?
  YES → PandasAI (df.chat() 한 줄, 가장 빠름)
  NO ↓

Q2: type-safety가 최우선인가? (Rust/static analysis 선호)
  YES → Pydantic AI (★★★, 11가지 강점, YAML/JSON 정의)
  NO ↓

Q3: role-playing 멀티 에이전트 협업이 도메인에 맞나?
  YES → CrewAI (Crews + Flows, LangChain 독립)
  NO ↓

Q4: LangGraph를 직접 작성하기 부담스럽고 Claude Code 같은 코딩 에이전트 만들고 싶은가?
  YES → DeepAgents (한 줄로 4종 도구 빌트인)
  NO ↓

Q5: 프로젝트가 OpenAI 모델만 사용할 계획인가?
  YES → OpenAI Agents SDK (11종 패턴 reference)
  NO ↓

Q6: 모델 swap (OpenAI/Anthropic/Google/local) + durable execution 필수인가?
  YES → LangGraph (1급) + LangChain init_chat_model
  NO ↓

Q7: MCP 서버를 우선 만들고 싶은가?
  YES → FastMCP (다른 프레임워크와 직교)
  NO → OpenAI Agents SDK (가장 빠른 일반 시작)
```

## 5. 핵심 결정 요인 (6 프레임워크 + 2 직교 layer)

| 요인 | LangGraph | OpenAI Agents | DeepAgents | CrewAI | Pydantic AI | PandasAI | FastMCP | LangChain |
|------|-----------|---------------|------------|--------|-------------|----------|---------|-----------|
| **모델 다양성** | ★★★ | ★ | ★★ | ★★ | **★★★** | ★★★ (LiteLLM) | N/A | ★★★ |
| **학습 곡선** | ★★ | ★★★ | ★★★ (한 줄) | ★★ | ★★ | **★★★ (df.chat)** | ★★★ | ★ |
| **Production 검증** | ★★★ | ★★ | ★ (신규) | ★★★ | ★★ | ★★ | ★★★ | ★★ |
| **Durable execution** | ★★★ | ★★ | ★★★ (LG 경유) | ★★ | **★★★** | ✗ | N/A | LG 경유 |
| **MCP 통합 깊이** | ★★ | ★★ | ★★ | ★★ | **★★★ (+A2A)** | ✗ | ★★★ | ★★ |
| **HITL 가이드** | ★★★ | ★★★ | ★★★ (LG 경유) | ★★ | ★★★ | ✗ | ★ | LG 경유 |
| **Type-safety** | ★ | ★★ | ★ | ★ | **★★★** | ★ | ★★ | ★ |
| **Vendor 락인 위험** | ★ (LangSmith 선택) | ★★★ (OpenAI) | ★ | ★ | ★ | ★ | ★ | ★ |
| **AGENTS.md=CLAUDE.md** | ✅ | ✅ | ✅ | ✗ | ✅ | ✗ | ✅ | ✅ |
| **OSS+SaaS 듀얼** | ✅ | ✅ | ✅ | ✅ | ✅ | ✗ | ✅ | ✅ |

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

## 7. 결론 (18회차 6×N 시점)

6 프레임워크가 **3개 그룹**으로 자연스럽게 나뉨:

### 그룹 A — LangChain 진영 (3개)
- **LangChain**: 모델 layer + partners 통합
- **LangGraph**: state machine + durable execution **1급**
- **DeepAgents**: LangGraph 위 batteries-included 프리셋

### 그룹 B — 독립 진영 (2개)
- **OpenAI Agents SDK**: 11종 패턴 reference, OpenAI 락인
- **CrewAI**: Crews + Flows, **LangChain 명시적 독립**

### 그룹 C — 특수 진영 (2개)
- **Pydantic AI**: type-safe + Capability + YAML/JSON 정의 (다른 5개와 차별)
- **PandasAI**: NL2DataFrame 어댑터 (다른 카테고리)

### 직교 layer (2개)
- **FastMCP**: 도구 layer (모든 프레임워크가 의존)
- **LangChain**: 그룹 A에 속하나 독립 사용 가능

## 8. 석근님 c2spf-analytics 권장 (18회차 갱신)

이전 권장: LangGraph + FastMCP + LangChain 3-layer

**18회차 갱신 권장 — 단계별 마이그레이션**:

```
Stage 1 (PoC, 1주):
  PandasAI + LiteLLM
  → df.chat() 한 줄로 BigQuery → NL2 결과 즉시 검증

Stage 2 (개발, 1개월):
  Pydantic AI + Logfire
  → BaseModel structured output, A2A로 다른 시스템과 통신
  → durable execution 1급 → 운영 안정성

Stage 3 (운영, 분기):
  LangGraph + FastMCP + LangChain init_chat_model
  → checkpoint-postgres로 대화 영속성
  → MCP로 BigQuery/Grafana/Sentry 연결
  → 모델 swap (Claude ↔ GPT) A/B 실험
```

→ **각 단계별 권장 프레임워크가 다름** — 정답이 하나가 아닌 단계별 진화 모델.

## 출처

- [[langchain-ai-langgraph]] — LangGraph (17회차)
- [[langchain-ai-langchain]] — LangChain (17회차)
- [[langchain-ai-deepagents]] — DeepAgents (18회차)
- [[openai-openai-agents-python]] — OpenAI Agents SDK (14회차)
- [[jlowin-fastmcp]] — FastMCP (17회차)
- [[crewaiinc-crewai]] — CrewAI (18회차)
- [[pydantic-pydantic-ai]] — Pydantic AI (18회차)
- [[sinaptik-ai-pandas-ai]] — PandasAI (18회차)
- [[agent-patterns]] — 12 패턴 (Anthropic 5 + OpenAI 6 + LangGraph 1)
- [[mcp]] — Model Context Protocol

## 후속 작업

- 19/20/21회차로 운영(Docker/Prometheus/Grafana/Sentry) + 프론트(Riverpod/Next.js/Tanstack/Zustand/Shadcn) + 마무리
- 실제 c2spf-analytics PoC 코드 작성 → BigQuery NL2SQL Pydantic AI reference
- Temporal vs LangGraph vs Pydantic AI durable execution 3자 정량 비교
