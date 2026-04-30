---
title: DeepAgents — LangGraph 위의 batteries-included agent harness
type: source
source_type: github_repo
source_url: https://github.com/langchain-ai/deepagents
raw_path: raw/articles/langchain-ai-deepagents/
author: LangChain Inc.
date_published: 2025-09
date_ingested: 2026-04-28
related:
- '[[langchain]]'
- '[[langgraph]]'
- '[[deepagents]]'
- '[[agent-skills]]'
- '[[agent-patterns]]'
confidence: high
tags:
- langchain
- langgraph
- deepagents
- agent-harness
- planning
- filesystem
- sub-agents
- claude-code-pattern
inbound_count: 16
aliases:
- DeepAgents — LangGraph 위의 batteries-included agent harness
- Langchain Ai Deepagents
- langchain ai deepagents
cited_by:
  - "[[agent-frameworks-matrix]]"
  - "[[agent-patterns]]"
  - "[[agent-skills]]"
  - "[[deepagents]]"
  - "[[ml-ai]]"
  - "[[openai-agents-python]]"
cited_by_count: 6
---

# DeepAgents — LangGraph 위의 batteries-included agent harness

## 한 줄 요약

LangChain Inc.의 **opinionated, ready-to-run agent** — `create_deep_agent` 한 줄로 planning + filesystem + shell + sub-agents 4종 도구 셋업 완료. **Claude Code/Cursor와 같은 코딩 에이전트 패턴을 LangGraph 위에 패키징**.

## 5섹션 요약

### 1) 본질 — "batteries-included" agent harness

> "Deep Agents is an agent harness. **An opinionated, ready-to-run agent out of the box**. Instead of wiring up prompts, tools, and context management yourself, you get a working agent immediately."

DeepAgents의 메타포: 프레임워크가 아닌 **harness** (마구). 사용자는 개념·도구·프롬프트를 일일이 묶지 않고, 이미 마구를 채운 말을 받는다.

### 2) 4종 빌트인 도구

| 도구군 | 함수 | 영감 |
|--------|------|------|
| **Planning** | `write_todos` | Anthropic SWE Agent (TodoWrite) |
| **Filesystem** | `read_file`, `write_file`, `edit_file`, `ls`, `glob`, `grep` | Claude Code 표준 도구 |
| **Shell** | `execute` (sandbox) | Cursor/Claude Code |
| **Sub-agents** | `task` (격리 컨텍스트) | Anthropic Agent Skills + sub-agent 패턴 |
| Smart defaults | 도구 사용법 가르치는 프롬프트 | (자체) |
| Context management | 자동 요약, 큰 출력은 파일 저장 | (자체) |

→ **이 4가지가 Anthropic이 발표한 Claude Code의 "에이전트 운영 5요소"와 일치**. DeepAgents는 그 패턴을 **OSS로 재현**.

### 3) LangGraph Native — "frame을 두 번 안 만든다"

> "`create_deep_agent` returns a compiled **LangGraph graph**. Use it with streaming, Studio, checkpointers, or any LangGraph feature."

→ DeepAgents는 별도 런타임을 안 만들었다. **LangGraph 위의 프리셋**. 따라서:
- `langgraph.checkpoint.postgres.PostgresSaver`로 **durable execution 자동 획득**
- LangGraph Studio로 디버깅
- streaming/interrupt/HITL 모두 그대로 사용

### 4) Monorepo 구조 (`libs/`)

AGENTS.md 364줄에 모노레포 가이드 명시:

```
deepagents/
├── libs/
│   ├── deepagents/   # 코어 라이브러리
│   ├── cli/          # Deep Agents CLI (코딩 에이전트 터미널)
│   └── evals/        # 평가 프레임워크
└── docs/
```

**Deep Agents CLI** (`libs/cli/`): "A pre-built coding agent in your terminal — similar to Claude Code or Cursor — powered by any LLM." → LangChain Inc.가 자체 코딩 에이전트 CLI를 OSS로 출시. Claude Code 직접 경쟁.

### 5) AGENTS.md = 사실상 CLAUDE.md (7번째 동기화 사례)

DeepAgents AGENTS.md는 364줄로 **monorepo 구조 + 개발 표준 + CI/CD + 부가 자료** 기록. CLAUDE.md 별도 없음 — agents 디렉토리 단일 진실 원천(SSOT) 채택. 발견된 6개 동기화 사례:

1. langchain-ai/langchain (292줄)
2. langchain-ai/langgraph (57줄)
3. langchain-ai/deepagents (364줄) ← 신규
4. jlowin/fastmcp (168줄, symlink)
5. openai/openai-agents-python (12.9KB)
6. pydantic/pydantic-ai (10K, byte-for-byte)

→ **AGENTS.md=CLAUDE.md 동기화는 이제 LLM 프레임워크 OSS의 "기본"이 되었다**.

## 결정적 인용

> "Use it with streaming, Studio, checkpointers, or any LangGraph feature."
>
> "MCP is supported via `langchain-mcp-adapters`."
>
> "A pre-built coding agent in your terminal — similar to Claude Code or Cursor."

## 의의

- **DeepAgents = LangGraph의 application layer** — agent-frameworks-matrix.md에서 "프레임워크"가 아닌 "프레임워크 위의 프리셋"이라는 새 카테고리 등장.
- **Claude Code 패턴의 OSS화** — Anthropic 비공개 Claude Code의 에이전트 운영 패턴이 OSS에 외삽됨.
- **DeepAgents CLI = 코딩 에이전트 시장 진출** — Claude Code/Cursor/Aider/Codex CLI에 LangChain의 카운터파트 등장.

## 출처

- README.md (134줄)
- AGENTS.md (364줄, monorepo 가이드)
- https://github.com/langchain-ai/deepagents
- https://docs.langchain.com/oss/python/deepagents/overview
