---
title: "microsoft/ai-agents-for-beginners — 12+ Lessons AI 에이전트 입문"
type: source
source_type: article
source_url: "https://github.com/microsoft/ai-agents-for-beginners"
raw_path: "raw/articles/microsoft-ai-agents-for-beginners/"
author: "Microsoft Cloud Advocates"
date_published: 2024-11-28
date_ingested: 2026-04-27
tags: [AI-agents, microsoft, microsoft-for-beginners, microsoft-agent-framework, azure-ai-foundry, mcp, a2a, nlweb, context-engineering, agent-memory]
related:
  - "[[microsoft]]"
  - "[[microsoft-for-beginners]]"
  - "[[mcp]]"
  - "[[context-engineering]]"
  - "[[harness]]"
  - "[[autonomous-research-loop]]"
confidence: high
---

# microsoft/ai-agents-for-beginners — 12+ Lessons AI 에이전트 입문

## 한줄 요약

> Microsoft Cloud Advocates의 AI 에이전트 입문 커리큘럼 — Microsoft Agent Framework(MAF) + Azure AI Foundry Agent Service V2 위에서 12+ lesson으로 디자인 패턴(Tool Use, Agentic RAG, Planning, Multi-Agent, Metacognition) → 운영(Production, Memory, Browser Use) → 최신 프로토콜(MCP/A2A/NLWeb, Context Engineering)까지를 한 카탈로그에 묶은 진행형 시리즈.

## 메타

- 라이선스: MIT
- 별 59,691 (2026-04-27 기준)
- 첫 커밋 2024-11-28 — 5개 시리즈 중 가장 최신, 즉 "현재 진행형" 토픽 묶음
- 기본 백엔드: Microsoft Agent Framework (MAF) + Azure AI Foundry Agent Service V2
- 대안 백엔드: MiniMax 등 OpenAI-호환 (대형 컨텍스트 204K 모델)
- 코드 위치: `code_samples/` 디렉토리에 lesson별 Python 노트북

## Lesson 카탈로그

| # | Lesson | 위키 연결 |
|---|--------|----------|
| 01 | Intro to AI Agents and Use Cases | — |
| 02 | Exploring AI Agentic Frameworks | — |
| 03 | Agentic Design Patterns | — |
| 04 | Tool Use Design Pattern | [[mcp]] (function calling 일반화) |
| 05 | Agentic RAG | [[context-engineering]] (동적 검색) |
| 06 | Building Trustworthy AI Agents | — |
| 07 | Planning Design Pattern | [[autonomous-research-loop]] (계획→실행→검증 루프) |
| 08 | Multi-Agent Design Pattern | [[harness]] (다중 에이전트 협업) |
| 09 | Metacognition Design Pattern | [[autonomous-research-loop]] (자기 평가) |
| 10 | AI Agents in Production | [[harness]] |
| **11** | **Agentic Protocols (MCP, A2A, NLWeb)** | **[[mcp]] (raw 보관)** |
| **12** | **Context Engineering for AI Agents** | **[[context-engineering]] (raw 보관)** |
| **13** | **Managing Agentic Memory** | **[[context-engineering]] (raw 보관)** |
| 14 | Microsoft Agent Framework | [[microsoft-for-beginners]] |
| 15 | Computer Use Agents (Browser Use) | — |
| Coming Soon | Deploying Scalable / Local / Securing | — |

## 핵심 시사점

### 1. Agentic Protocols 11 — MCP / A2A / NLWeb 3종 묶음

[[mcp]]가 단독이 아니라 자매 프로토콜과 함께 카탈로그화됨:

- **MCP (Model Context Protocol)**: LLM ↔ 도구·데이터. 3 primitives (**Tools**, **Resources**, **Prompts**) + Hosts/Clients/Servers 아키텍처
- **A2A (Agent-to-Agent)**: 에이전트 ↔ 에이전트. 다른 조직·환경·스택에 걸친 협업
- **NLWeb (Natural Language Web)**: 자연어 인터페이스를 모든 웹사이트로

**MCP의 3가지 이점** (lesson 11에서 명문화):
1. Dynamic Tool Discovery (vs static API integrations)
2. Interoperability Across LLMs
3. Standardized Security (인증 표준 통일)

기존 [[mcp]] 위키 페이지는 "도구 호출" 단계에 머물러 있었으므로 이 lesson으로 보강 필요.

### 2. Context Engineering 12 — 5가지 컨텍스트 타입 + 6가지 전략 + 4가지 실패 모드

**Context Types (5)**:
1. **Instructions** — 시스템 메시지, few-shot, 도구 설명 (프롬프트 엔지니어링과 겹침)
2. **Knowledge** — 사실, RAG 검색 결과, 장기 메모리
3. **Tools** — 외부 함수·API·MCP 서버 정의 + 결과
4. **Conversation History** — 진행중인 대화
5. **User Preferences** — 학습된 사용자 취향

**Planning Strategies**:
1. Define Clear Results (완료 시 세계의 모습 정의)
2. Map the Context (필요 정보의 위치 매핑)
3. Create Context Pipelines (가져오는 방법: RAG, MCP, 도구)

**Practical Strategies (6)**:
1. **Agent Scratchpad** — 단일 세션 내 노트 (컨텍스트 윈도우 외부 파일/객체)
2. **Memories** — 다중 세션에 걸친 저장
3. **Compressing Context** — 요약·트리밍
4. **Multi-Agent Systems** — 각 에이전트가 별도 컨텍스트 윈도우
5. **Sandbox Environments** — 코드/대용량 처리는 외부에서 실행 후 결과만 회수
6. **Runtime State Objects** — 서브태스크별 상태 컨테이너

**4가지 실패 모드 + 처방**:
| 실패 | 증상 | 처방 |
|------|------|------|
| Context Poisoning | 할루시네이션이 컨텍스트에 박혀 반복 인용 | validation + quarantine |
| Context Distraction | 누적 정보로 집중력 분산 | 주기적 summarization |
| Context Confusion | 도구가 너무 많아 잘못된 호출 | RAG over tool descriptions, **<30 도구** |
| Context Clash | 모순 정보 누적 | pruning + offloading |

### 3. "Coming Soon"이 명시된 진행형 카탈로그

Deploying Scalable Agents / Local Agents / Securing Agents 3개가 "Coming Soon"으로 노출 — 시리즈 자체가 살아있는 문서임을 보여주는 운영 신호. anthropics/skills의 spec 분리(agentskills.io)와 비슷한 의도: 카탈로그를 닫지 않는다.

### 4. 14번 = "Microsoft Agent Framework" 자체 강의

자사 프레임워크(MAF)를 14번 lesson에 별도 단원으로 배치 — "쓰는 법"보다 "왜 다른 프레임워크와 다른가"를 가르치는 자가 인용 구조. 자사 도구 마케팅과 자체 학습 자료의 경계가 흐릿한 Microsoft DevRel의 운영 패턴.

## 석근에게 가장 가치있는 lesson

- **11 (Agentic Protocols)** — [[mcp]] 보강의 핵심 자료, raw에 보관
- **12 (Context Engineering)** — [[context-engineering]] 보강의 핵심 자료, raw에 보관
- 13 (Agentic Memory) — 개인 비서 AI(석근의 관심 영역) 직결
- 04 (Tool Use), 05 (Agentic RAG) — BI 워크플로우 적용 검토

## 관련 엔티티/개념

- [[microsoft]] / [[microsoft-for-beginners]]
- [[mcp]] — lesson 11이 정확화·보강 (3 primitives, 3 benefits)
- [[context-engineering]] — lesson 12가 보강 (5 types, 6 strategies, 4 failures)
- [[harness]] — lesson 08(Multi-Agent), 10(Production)이 직결
- [[autonomous-research-loop]] — lesson 07(Planning), 09(Metacognition)이 같은 발상

## 인용

> "Context Engineering is the practice of making sure the AI Agent has the right information to complete the next step of the task. The context window is limited in size, so as agent builders we need to build systems and processes to manage adding, removing, and condensing the information in the context window."
> — Lesson 12

> "MCP works across different LLMs, providing flexibility to switch core models to evaluate for better performance."
> — Lesson 11

## 메모

- 같은 시리즈 내 [[microsoft-generative-ai-for-beginners]]의 17번 lesson(AI Agents)이 입문, 이쪽이 12+ lesson 본격 시리즈. 둘이 사실상 단일 학습 경로.
- 개인 비서 AI 만드는 석근에게는 13(Memory) → 12(Context Engineering) → 11(Protocols) 순으로 학습 경로 추천.
- 후속 탐구: 13 lesson도 raw에 추가 보관 검토 — Agentic Memory 패턴이 [[context-engineering]]의 "Memories" strategy를 구현 수준으로 확장.
