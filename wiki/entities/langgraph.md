---
title: "LangGraph"
type: entity
entity_type: tool
tags: [langgraph, langchain-inc, agent, state-machine, durable-execution, pregel, apache-beam, networkx, checkpoint, 17회차, 에이전트]
related:
  - "[[langchain]]"
  - "[[openai-agents-python]]"
  - "[[agent-patterns]]"
  - "[[ml-ai]]"
  - "[[postgresql]]"
  - "[[langchain-ai-langgraph]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# LangGraph

## 개요

**Low-level orchestration framework for building stateful agents** — Google Pregel + Apache Beam + NetworkX의 종합. LangChain Inc.가 개발했으나 LangChain 없이 독립 사용 가능. **Klarna / Replit / Elastic** 등이 production에서 사용하는 stateful agent의 사실 표준 그래프 프레임워크.

## 주요 특징

### 학술적 계보 (3가지 영감)
- **Pregel** ([Google research, 2010](https://research.google/pubs/pub37252/)) — Bulk Synchronous Parallel 그래프 처리
- **Apache Beam** — batch + streaming 통합 모델
- **NetworkX** — Python 표준 그래프 라이브러리 (public interface 영감)

### 5가지 핵심 가치
1. **Durable execution** — 실패 복구, "where it left off" 재개
2. **Human-in-the-loop** — 어느 시점이든 상태 검사·수정
3. **Comprehensive memory** — short-term + long-term memory
4. **Debugging with LangSmith** — 시각화·상태 전이 추적
5. **Production-ready deployment** — long-running stateful workflow 인프라

### 모노레포 구조
```
libs/
├── checkpoint               # 베이스 인터페이스
├── checkpoint-postgres      # Postgres 구현
├── checkpoint-sqlite        # SQLite 구현
├── checkpoint-conformance
├── cli                      # 공식 CLI
├── langgraph                # 코어
├── prebuilt                 # 고수준 API (create_agent)
├── sdk-py                   # Python SDK
└── sdk-js                   # JS/TS SDK (standalone)
```

### Production 사용처
- **Klarna** — 핀테크 챗봇 + 결제 자동화
- **Replit** — 코드 어시스턴트
- **Elastic** — 검색 엔진 통합

### 기술 스택
- 언어: Python 3.10+ (별도 langgraph.js)
- 의존성: [[uv]]
- Checkpoint: [[postgresql]] / SQLite
- 관측성: LangSmith (선택)

### 거버넌스
- **회사**: LangChain Inc.
- **License**: MIT
- **AGENTS.md = CLAUDE.md** (57줄)

## 관련 개념

- [[langchain]]: LangGraph 위에 빌드된 고수준 통합 (LangChain v1 `create_agent`)
- [[openai-agents-python]]: 직접 경쟁 (둘 다 stateful agent 프레임워크, 다른 메타포)
- [[agent-patterns]]: Anthropic 5 + OpenAI Agents 6 + LangGraph "graph + state machine" 패턴
- [[postgresql]] / [[redis]]: Checkpoint backend (durable execution)
- [[mcp]]: LangChain partners 경유 MCP 통합
- [[fastapi]]: LangGraph Server API의 백엔드

## 의사결정 컨텍스트 (raw 인용)

> "Pregel + Apache Beam + NetworkX 영감의 low-level agent orchestration. Klarna/Replit/Elastic 등이 production에서 사용하는 상태 기반 LLM 에이전트 그래프 프레임워크."
> — [[langchain-ai-langgraph]] 한줄 요청

[[seokgeun-stack-guide]] stateful agent 프레임워크 영역. [[matechat]] 채팅 분석 모듈의 multi-step orchestration 후보. [[langchain]] 산하 + [[deepagents]]가 LangGraph Native로 빌드. **상태 기반 그래프 + durable execution** 패턴은 [[llm-infra-meta-cluster]] 5축의 [[harness]] 진화 사례 — [[crewai]]·[[pydantic-ai]]와 함께 6 프레임워크 매트릭스 비교됨([[agent-frameworks-matrix]]).

## 출처

- [[langchain-ai-langgraph]] — 17회차 수집, README + AGENTS.md (139줄)

## 메모

- **vs OpenAI Agents SDK**: LangGraph는 "Pregel-style state graph" 메타포, OpenAI는 "ChatCompletions에 가까운 운영 SOP". 같은 영역에 다른 모델로 답함. 분석가/엔지니어 선호도에 따라 선택.
- **vs Temporal**: LangGraph durable execution은 Temporal 워크플로우와 수렴 — 즉 LLM 에이전트가 분산 워크플로우 시스템과 통합되는 방향.
- **석근님 BI 적용**: 게임 사용자 분석 챗봇 (자연어 → SQL → 시각화)을 LangGraph state machine으로 빌드 가능. checkpoint-postgres로 대화 영속성.
- 향후 위키 확장: Pregel 논문 별도 페이지, Apache Beam entity, NetworkX entity, LangGraph Studio.
