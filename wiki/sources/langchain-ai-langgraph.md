---
title: langchain-ai/langgraph — Stateful agent orchestration framework
type: source
source_type: article
source_url: https://github.com/langchain-ai/langgraph
raw_path: raw/articles/langchain-ai-langgraph/
author: LangChain Inc.
date_published: 2024-01-01
date_ingested: 2026-04-28
tags:
- langgraph
- langchain-inc
- agent
- state-machine
- durable-execution
- pregel
- apache-beam
- networkx
related:
- '[[langgraph]]'
- '[[langchain]]'
- '[[agent-patterns]]'
- '[[ml-ai]]'
confidence: high
inbound_count: 17
aliases:
- Langchain Ai Langgraph
- langchain ai langgraph
- langchain-ai/langgraph — Stateful agent orchestration framework
cited_by:
  - "[[agent-frameworks-matrix]]"
  - "[[agent-patterns]]"
  - "[[agent-skills]]"
  - "[[langgraph]]"
  - "[[mcp]]"
  - "[[ml-ai]]"
cited_by_count: 6
---

# langchain-ai/langgraph — Stateful agent orchestration framework

## 한줄 요약

> **Pregel + Apache Beam + NetworkX 영감**의 low-level agent orchestration. Klarna/Replit/Elastic 등이 production에서 사용하는 **상태 기반 LLM 에이전트 그래프 프레임워크**.

## 핵심 내용

### 정체성
- **"Low-level orchestration framework for building stateful agents"**
- LangChain Inc.가 만들었으나 LangChain 없이 독립 사용 가능
- 단순 chain이 아닌 **그래프(노드 + 엣지 + 상태)** 추상화
- LangChain의 `create_agent`가 LangGraph 위에 빌드됨

### 핵심 가치 (5가지)
1. **Durable execution** — 실패에 대한 영속성, "where it left off"에서 재개
2. **Human-in-the-loop** — 실행 중 어느 시점에서든 상태 검사 + 수정
3. **Comprehensive memory** — short-term working memory + long-term cross-session memory
4. **Debugging with LangSmith** — 실행 경로 시각화 + 상태 전이 캡처 + 런타임 메트릭
5. **Production-ready deployment** — 장기 실행·상태 기반 워크플로우용 인프라

### 학술적 계보 (3가지 영감)
- **Pregel** ([Google research, 2010](https://research.google/pubs/pub37252/)) — 대규모 그래프 처리 시스템 (Bulk Synchronous Parallel)
- **Apache Beam** — 통합 batch + streaming 데이터 처리 모델
- **NetworkX** — Python의 표준 그래프 라이브러리 (public interface 영감)

### 모노레포 구조
```
libs/
├── checkpoint               # 베이스 인터페이스
├── checkpoint-postgres      # Postgres 구현
├── checkpoint-sqlite        # SQLite 구현
├── checkpoint-conformance   # 적합성 테스트
├── cli                      # 공식 CLI
├── langgraph                # 코어
├── prebuilt                 # 고수준 API (create_agent 등)
├── sdk-py                   # Python SDK (LangGraph Server API용)
└── sdk-js                   # JS/TS SDK
```

### 의존성 그래프
```
checkpoint
├── checkpoint-postgres
├── checkpoint-sqlite
├── prebuilt
└── langgraph

prebuilt
└── langgraph

sdk-py
├── langgraph
└── cli

sdk-js (standalone)
```

### Production 사용처 (README에서 명시)
- Klarna
- Replit
- Elastic
- 외 다수 ("companies shaping the future of agents")

### AGENTS.md = CLAUDE.md (동기화, 57줄)
- 매우 간결: "이 repo는 monorepo. libs/ 아래 각 라이브러리"
- PR 전 공통 명령: `make format` / `make lint` / `make test`
- 환경 변수 `TEST=path/to/test.py make test`로 특정 테스트 실행
- Sphinx-style 더블 백틱 금지 (`` ``code`` `` 사용 금지, 단일 ` 사용)

### License
- MIT

## 주요 인사이트

1. **그래프 추상화의 학술적 정당화**: LangGraph는 단순 "DAG 라이브러리"가 아니라 **Google Pregel + Apache Beam + NetworkX**의 종합. LLM 에이전트가 분산 시스템 패턴(BSP, 메시지 패싱)을 차용했다는 것은 **에이전트 = 분산 워커**라는 인식의 정착.
2. **Durable execution의 의미**: LangChain "chain"은 stateless였으나, LangGraph는 checkpoint(Postgres/SQLite) 기반 영속성을 1급으로 채택. 즉 **에이전트는 트랜잭션 비교 가능한 단위**가 됨. Temporal 같은 워크플로우 엔진과 수렴.
3. **`create_agent` = LangGraph 위의 LangChain**: LangChain v1의 `create_agent`는 사실 LangGraph의 `prebuilt` 패키지. 즉 LangGraph가 **저수준 엔진**, LangChain이 **고수준 통합** 역할 분담.
4. **NetworkX 영감의 친숙성**: 그래프 API가 NetworkX 스타일이라 Python 분석가에게 학습 곡선 낮음. [[scikit-learn]]·[[pandas]] 사용자도 빠르게 적응 가능.
5. **standalone JS SDK**: sdk-js만 의존성 그래프에서 standalone — 즉 JS는 백엔드 구독만 하면 되고, Python에서 그래프 정의 → JS에서 실행도 가능.

## 관련 엔티티/개념

- [[langgraph]] — 본 소스의 대상
- [[langchain]] — 형제 프레임워크 (LangGraph가 저수준)
- [[openai-agents-python]] — 직접 경쟁 (둘 다 stateful agent 프레임워크)
- [[agent-patterns]] — Anthropic 5 패턴 + OpenAI Agents SDK 6 패턴 + LangGraph는 "graph + state machine" 패턴 추가
- [[mcp]] — LangGraph도 MCP 통합 지원 (LangChain partners 경유)

## 인용할 만한 구절

> "LangGraph is inspired by Pregel and Apache Beam. The public interface draws inspiration from NetworkX. LangGraph is built by LangChain Inc, the creators of LangChain, but can be used without LangChain."
> — README.md (Acknowledgements)

> "Build agents that persist through failures and can run for extended periods, automatically resuming from exactly where they left off."
> — README.md (Durable execution)

## 메모

- LLM 인프라 수집 — agent-frameworks-matrix.md 1차 작성의 핵심 비교 대상.
- [[openai-agents-python]]과 LangGraph의 구분: OpenAI는 "ChatCompletions에 가까운 운영 SOP", LangGraph는 "Pregel-style state graph". 같은 영역(stateful agent)에 다른 메타포로 답함.
- Klarna 사용 사례: 핀테크 챗봇 + 결제 자동화 (실제 production 검증 강력).
