---
title: "DeepAgents"
type: entity
entity_type: tool
related:
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[fastmcp]]"
  - "[[agent-skills]]"
  - "[[agent-patterns]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
tags: [deepagents, langchain-AI, langgraph-native, agent-harness, planning, filesystem, sub-agents, claude-code-pattern, 18회차]
---

# DeepAgents

LangChain Inc.의 **batteries-included agent harness** — `create_deep_agent()` 한 줄로 Anthropic Claude Code 스타일 에이전트(planning + filesystem + shell + sub-agents)를 LangGraph 위에 즉시 패키징.

## 기본 정보

- **저장소**: [langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)
- **언어**: Python (JS/TS 별도: [deepagentsjs](https://github.com/langchain-ai/deepagentsjs))
- **License**: MIT
- **PyPI**: `pip install deepagents`
- **CLI**: `libs/cli/` — Claude Code/Cursor 대항 코딩 에이전트 터미널
- **모노레포**: `libs/{deepagents, cli, evals}` 3개

## 역할 — "프레임워크 위의 프리셋"

DeepAgents는 새로운 agent runtime이 아닌, **LangGraph 위에 4종 도구를 빌트인한 프리셋**:

```python
from deepagents import create_deep_agent

agent = create_deep_agent()  # 한 줄로 ready
result = agent.invoke({"messages": [...]})
# create_deep_agent returns a compiled LangGraph graph
```

따라서:
- LangGraph의 모든 기능 (streaming, Studio, checkpointers, HITL) 자동 상속
- `langgraph.checkpoint.postgres.PostgresSaver`로 **durable execution 무료**
- MCP 통합도 `langchain-mcp-adapters` 경유

## 빌트인 도구 4종

| 도구군 | 함수 | Claude Code 대응 |
|--------|------|-------------------|
| Planning | `write_todos` | TodoWrite |
| Filesystem | `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep` | Read/Write/Edit/Glob/Grep |
| Shell | `execute` (sandbox) | Bash |
| Sub-agents | `task` (격리 컨텍스트) | Agent (subagent_type) |

→ **Anthropic Claude Code의 비공개 패턴을 OSS로 외삽**.

## 대안 / 비교

| 도구 | 메타포 | LangGraph 의존 |
|------|--------|----------------|
| **DeepAgents** | "harness" — 마구를 채운 말 | ✅ Native |
| [[langgraph]] | "state graph" — 직접 그래프 작성 | (자체) |
| [[openai-agents-python]] | "RunState + 11종 패턴" | ✗ |
| [[crewai]] | "Crews + Flows" | ✗ (독립) |
| [[pydantic-ai]] | "type-safe agent + 11 강점" | ✗ |
| [[fastmcp]] | "MCP 서버 빌드" | ✗ (직교) |

→ DeepAgents는 **LangChain 진영에서 가장 빠른 시작점**. LangGraph 직접 작성하기 부담스러울 때 사용.

## 통합

- **LangGraph (직접)**: returns compiled graph
- **LangChain init_chat_model**: `model=init_chat_model("openai:gpt-4o")`
- **MCP**: `langchain-mcp-adapters`
- **LangSmith**: 디버깅/관측

## 사용 예 (석근님 c2spf-analytics 시나리오)

```python
from deepagents import create_deep_agent
from langchain.chat_models import init_chat_model

agent = create_deep_agent(
    model=init_chat_model("anthropic:claude-sonnet-4-6"),
    tools=[query_bigquery, plot_metrics],
    system_prompt="너는 게임 데이터 BI 어시스턴트다. ...",
)
result = agent.invoke({"messages": [{"role": "user", "content": "DAU 추세를 분석해줘"}]})
```

→ planning + filesystem이 빌트인이라 **분석 결과를 자동으로 파일로 저장**. checkpointer 추가하면 대화 영속성 자동 획득.

## 출처

- [[langchain-ai-deepagents]] — DeepAgents (18회차)

## 관련

- [[langchain]] — 모회사 LangChain Inc.
- [[langgraph]] — DeepAgents의 런타임
- [[agent-skills]] — Claude Code agent skills 패턴
- [[agent-patterns]] — 12번째 패턴 (state-machine + durable execution)
