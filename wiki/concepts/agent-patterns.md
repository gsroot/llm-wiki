---
title: "Building Effective Agents — 5 패턴"
type: concept
category: ai
tags: [agent-patterns, building-effective-agents, anthropic, prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, agent, workflow, spec-kit, sdd, pre-composed-patterns, openai, openai-cookbook, openai-agents-python, agents-SDK, exec-plans, guardrails, human-in-the-loop, forced-tool-use, 11-patterns, langgraph, pregel, state-machine, durable-execution, 12-patterns, pydantic-ai, deepagents, crewai, 18회차, 에이전트]
related:
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[anthropic]]"
  - "[[autonomous-research-loop]]"
  - "[[harness]]"
  - "[[anthropics-claude-cookbooks]]"
  - "[[mcp]]"
  - "[[spec-kit]]"
  - "[[spec-driven-development]]"
  - "[[github]]"
  - "[[openai]]"
  - "[[openai-cookbook]]"
  - "[[openai-agents-python]]"
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[deepagents]]"
  - "[[crewai]]"
  - "[[pydantic-ai]]"
source_count: 7
observed_source_refs: 22
inbound_count: 66
created: 2026-04-27
updated: 2026-04-28
---

# Building Effective Agents — 5 패턴

## 정의

[[anthropic]] (Erik Schluntz · Barry Zhang)이 [공식 블로그](https://anthropic.com/research/building-effective-agents)에서 정의한 **에이전트 워크플로우 5가지 표준 분류**. 각 패턴이 cost·latency를 작업 성능과 trade-off하는 방식이 명확히 다르다. 위키에서는 이 5분류를 자율 에이전트 설계의 1차 분류 체계로 채택.

## 왜 중요한가

LLM 에이전트 시대 직전까지 "프롬프트 엔지니어링"이 분류 단위였다. 에이전트 시대에 들어서며 **여러 LLM 호출을 어떻게 묶을 것인가**가 새 분류 단위가 됐고, Anthropic의 5 패턴이 사실상 표준 분류로 자리잡고 있다. 위키에서 [[autonomous-research-loop]] · [[harness]] · 향후 들어올 모든 에이전트 페이지가 이 5 패턴 위에 올라간다.

## 핵심 내용

### Basic Building Blocks (3종)

#### 1. Prompt Chaining (프롬프트 체인)

**아이디어**: 단일 작업을 순차 서브태스크로 분해, 각 단계가 이전 결과 위에 빌드.

```
입력 → LLM 1 (계획) → LLM 2 (초안) → LLM 3 (검토·정제) → 출력
```

**Trade-off**: latency 증가 ↔ 각 단계 단순화로 정확도 향상.

**적용 사례**: 마크다운 → 슬라이드 변환, 긴 문서 요약 → 핵심 인사이트 추출 → SNS 포스팅 변환.

#### 2. Routing (라우팅)

**아이디어**: 입력 특성을 보고 전용 LLM 경로를 동적으로 선택.

```
입력 → Router LLM → {LLM-A | LLM-B | LLM-C} → 출력
```

**Trade-off**: 추가 분류 호출 1회 ↔ 각 경로의 모델/프롬프트를 도메인 최적화 가능.

**적용 사례**: 고객 지원 — refund 문의/기술 문의/일반 질의에 따라 다른 LLM 호출. 모델 선택(쉬운 건 Haiku, 어려운 건 Opus).

#### 3. Parallelization (병렬화)

**아이디어**: 독립 서브태스크를 여러 LLM에 동시 분산.

```
            ┌→ LLM 1 ─┐
입력 ───────┼→ LLM 2 ─┼─→ aggregator → 출력
            └→ LLM 3 ─┘
```

**두 변종**:
- **Sectioning** — 작업을 독립 부분으로 쪼개 병렬 처리 (예: 리뷰 N 측면 평가)
- **Voting** — 같은 작업을 여러 번 실행해 다수결/평균 (예: 코드 보안성 다중 평가)

**Trade-off**: 비용 N배 ↔ wall-clock 시간 단축 + 다양성 확보.

**적용 사례**: 이해관계자 영향 분석 (각 stakeholder별 병렬 LLM), 다관점 코드 리뷰.

### Advanced Workflows (2종)

#### 4. Orchestrator-Workers

**아이디어**: 오케스트레이터 LLM이 **동적으로** 서브태스크를 생성하고 워커 LLM들을 조율, 결과를 합성.

```
입력 → Orchestrator LLM ─┬→ Worker A → ┐
                          ├→ Worker B → ├─→ Synthesizer → 출력
                          └→ Worker C → ┘
       (서브태스크 동적 결정)
```

**Parallelization과의 차이**: Parallelization은 **사전에 알려진** 서브태스크를 분산. Orchestrator는 **런타임에 서브태스크를 결정**.

**Trade-off**: 오케스트레이터 호출 + 워커 호출 N개 + synthesizer = 비용 큼 ↔ 사전에 분해 불가능한 복잡 작업 처리.

**적용 사례**: 복잡 코딩 task (변경 대상 파일을 스캔 후 결정), 자율 연구 (다음 검색 쿼리를 결정).

#### 5. Evaluator-Optimizer

**아이디어**: 한 LLM이 출력 생성, 다른 LLM이 평가/피드백 → 반복 개선.

```
입력 → Generator LLM → 출력 후보
         ↑                    ↓
      (수정)         Evaluator LLM (acceptable?)
         ↑                    ↓
         └────── feedback ─────
                              ↓ (yes)
                            출력 확정
```

**Trade-off**: 반복 횟수 × 비용 ↔ 자체 검증으로 품질 ceiling 상승.

**적용 사례**: 번역 품질 개선, 복잡 검색 답변 정제, **자율 연구 루프**.

## 5 패턴의 위계

| 분류 | 패턴 수 | 호출 흐름 |
|------|--------|----------|
| Basic | 3 | 정적 (사전 결정) |
| Advanced | 2 | 동적 (런타임 결정) |

Advanced 2개의 핵심: **런타임에 흐름을 결정한다**. 이게 사람들이 "에이전트답다"고 부르는 특징.

## 12번째 패턴: State-Machine + Durable Execution (17회차 추가)

[[langgraph]]가 정립한 **Pregel-style state graph + checkpoint persistence** 패턴은 5 패턴 + OpenAI 확장 6의 외곽에 위치. 핵심 차이:

| 축 | 기존 11 패턴 | LangGraph state machine |
|----|--------------|-------------------------|
| **상태 모델** | LLM 호출의 stateless 합성 | **명시적 상태 그래프** (노드+엣지+공유 상태) |
| **영속성** | 세션 스코프 | **checkpoint(Postgres/SQLite)로 디스크 영속** |
| **재개** | 재시작 = 재실행 | **"where it left off"에서 정확히 재개** |
| **Human-in-the-loop** | OpenAI 확장 6에서 등장 | **상태 그래프 어디서든 interrupt → 검사 → 수정 → 재개** |
| **메타포** | LLM 호출의 그래프 | **분산 워커 그래프 (Pregel BSP)** |

**즉 12번째 패턴 = "에이전트는 트랜잭션 단위"**. Temporal/Cadence 같은 분산 워크플로우 엔진과 LLM 에이전트의 수렴이 이 패턴의 본질.

**Reference 구현**: [[langgraph]] `prebuilt` 패키지의 `create_react_agent` + `checkpoint-postgres` 조합이 표준. LangChain v1 `create_agent`도 이 위에 빌드됨.

**OSS Agents (Klarna/Replit/Elastic) 사용 사례**: stateful 챗봇 + 결제 자동화 + 코드 어시스턴트. 즉 production-critical 트랜잭션 도메인에서 채택률 우위.

### 12번째 패턴 양강 구도 (18회차 추가)

[[pydantic-ai]]도 README의 11가지 자기 강점 중 9번에서 **Durable Execution 1급 지원** 명시:

> "preserve their progress across transient API failures and application errors or restarts, and handle long-running, asynchronous, and human-in-the-loop workflows with production-grade reliability"

→ **12번째 패턴은 이제 [[langgraph]] 단독이 아닌 [[langgraph]] + [[pydantic-ai]] 양강 구도**. 차이점:

| 축 | LangGraph | Pydantic AI |
|----|-----------|-------------|
| 본질 | state graph 1급 | type-safe agent 1급 (durable이 11 강점 중 하나) |
| Type-safety | ★ | ★★★ |
| Graph | (자체) | type-hint 기반 graph (11번 강점) |
| YAML/JSON 정의 | ✗ | ✅ |
| Production | Klarna/Replit/Elastic | Pydantic 팀 자체 운영 |

→ **Rust/static analysis 선호 팀 = Pydantic AI, LangChain 생태계 = LangGraph**.

[[deepagents]] (18회차)는 LangGraph 위 프리셋으로서 **12번째 패턴을 자동 상속**. 따라서 12번째 패턴 채택 OSS는 이제 3개: LangGraph + Pydantic AI + DeepAgents.

## [[autonomous-research-loop]]과의 관계

[[autoresearch]] (Karpathy) 같은 자율 연구 루프는 **Evaluator-Optimizer + Orchestrator-Workers의 도메인 특화 합성**:

| autoresearch 요소 | 5 패턴 매핑 |
|------------------|-------------|
| 시간 예산 안에서 다음 실험을 결정 | Orchestrator-Workers (실험 = 워커) |
| `val_bpb` 메트릭으로 결과 평가 → 다음 실험 방향 결정 | Evaluator-Optimizer (메트릭이 evaluator) |
| `program.md` 자율 진화 | Evaluator-Optimizer (program.md가 generator의 산출물 + evaluator의 입력) |

즉 [[autonomous-research-loop]]은 **5 패턴의 추상화 위에 "메트릭 객관성 + 시간 예산 + Simplicity 기준"이라는 도메인 제약을 추가한 합성 패턴**.

## 실전 적용

### A. 회사 BI에서

| 작업 | 패턴 |
|------|------|
| 일간 KPI 보고서 생성 | Prompt Chaining (데이터 → 차트 → 코멘트 → 슬라이드) |
| 사용자 문의 라우팅 (대시보드 / 데이터 / 권한) | Routing |
| 동일 쿼리에 대한 다중 데이터 출처 검증 | Parallelization (Voting) |
| 신규 지표 정의 — 어떤 테이블·조인이 필요한지 동적 결정 | Orchestrator-Workers |
| SQL 쿼리 자동 정정 (실행 결과 보고 다시 작성) | Evaluator-Optimizer |

### B. 개인 비서 AI에서

- **Chief of Staff Agent** ([[anthropics-claude-cookbooks]]의 01번 노트북) = Orchestrator-Workers + Evaluator-Optimizer 합성
- 일정 조율 = Routing (참석자별 선호 라우팅)
- 자료 조사 = Orchestrator-Workers (다음 검색을 LLM이 결정) + Evaluator-Optimizer (만족도 미달 시 재검색)

### C. [[claude-agent-sdk]]에서의 구현

5 패턴 모두 `query()` 또는 `ClaudeSDKClient` + 서브에이전트 조합으로 구현 가능. cookbook의 `patterns/agents/basic_workflows.ipynb` (앞 3개) + `evaluator_optimizer.ipynb` + `orchestrator_workers.ipynb`가 reference.

## 안티패턴

| 패턴 | 문제 | 회피 |
|------|------|------|
| 5 패턴 무관하게 단일 거대 프롬프트로 전부 해결 | 검증 불가, 토큰 폭발, 디버깅 지옥 | 패턴별 분해 후 재합성 |
| Orchestrator-Workers를 작은 작업에 사용 | 오케스트레이션 오버헤드가 작업보다 큼 | 정적 분해 가능하면 Parallelization |
| Evaluator-Optimizer 무한 루프 | iteration cap 부재 | 최대 N회 + 시간 예산 강제 (autoresearch 패턴) |
| Routing의 분류 LLM이 너무 비쌈 | Router 비용 > 도메인 LLM 비용 | Router는 Haiku, 워커는 Sonnet/Opus |

## 관련 개념

- [[harness]]: 5 패턴 모두 4층 하네스 안에서 구현 — Orchestrator-Workers는 통제 레이어 부담이 큼
- [[autonomous-research-loop]]: 5 패턴 합성의 도메인 특화
- [[claude-agent-sdk]]: 5 패턴의 reference 구현 진입로
- [[claude-code]]: 5 패턴이 Claude Code 안에서는 subagent + plan mode + hooks 조합으로 모두 표현 가능
- [[token-economy]]: Parallelization · Orchestrator-Workers는 비용이 N배. token economy 시점에서 가장 신중해야 할 패턴

## 출처

- [[anthropics-claude-cookbooks]] — `patterns/agents/` 3개 노트북 (basic_workflows, evaluator_optimizer, orchestrator_workers) + 원조 블로그 "Building Effective Agents" (Schluntz·Zhang) 링크
- [[openai-openai-cookbook]] — Anthropic 5 패턴의 **OpenAI 측 reference 구현**. `examples/agents_sdk/` 디렉토리에 직접 매핑되는 노트북: `parallel_agents.ipynb` (59KB) = Parallelization Sectioning, `evaluate_agents.ipynb` (106KB) = Evaluator-Optimizer, `multi-agent-portfolio-collaboration/` = Orchestrator-Workers, `dispute_agent.ipynb` (21KB) + `Orchestrating_agents.ipynb` (31KB) = Routing + Orchestrator-Workers 합성. 또한 [[openai-cookbook]] PLANS.md / ExecPlans 패턴은 5 패턴 외부의 **6번째 거버넌스 패턴**(7시간+ 단일 LLM 작업 living document). registry.yaml `agents-sdk` 태그 16건 + `agents` 12건이 OpenAI 측 에이전트 워크플로우 사례 데이터베이스
- [[github-spec-kit]] — 5 패턴을 **메소드론으로 사전 합성한 결과물**. `/speckit.constitution → specify → plan → tasks → implement` 정적 5단계 = Prompt Chaining. `/speckit.clarify`/`/speckit.analyze` = Evaluator-Optimizer (사용자/LLM이 evaluator). `tasks.md`의 `[P]` 마커 = Parallelization Sectioning. 커뮤니티 확장 "Agent Assign" = Routing. 복잡 spec의 plan 동적 결정 = Orchestrator-Workers. 사용자가 직접 패턴 선택할 필요 없이 [[spec-driven-development]] 단계만 따라가면 5 패턴이 자동 합성됨
- [[langchain-ai-langgraph]] — **12번째 패턴 (State-Machine + Durable Execution) 정립**. Pregel + Apache Beam + NetworkX 학술 계보 위에 build. checkpoint(Postgres/SQLite) 기반 durable execution이 LLM 에이전트를 "트랜잭션 단위"로 격상. Klarna/Replit/Elastic이 production. LangChain v1 `create_agent`가 이 위에 빌드. (17회차 추가)
- [[pydantic-pydantic-ai]] — **12번째 패턴 양강 합류** (18회차 추가). Pydantic AI가 README 11가지 강점 중 9번에 durable execution 1급 명시. type-safety ★★★ + Graph Support 11번 강점 + YAML/JSON agent 정의로 LangGraph와 차별화. 이제 12번째 패턴은 [[langgraph]] + [[pydantic-ai]] 양강 구도. [[langchain-ai-deepagents]]는 LangGraph 위 프리셋으로 12번째 패턴 자동 상속.
- [[crewaiinc-crewai]] — **CrewAI Crews + Flows 듀얼 메타포** (18회차 추가). Crews(role-playing 자율 협업) + Flows(enterprise event-driven 정밀 제어)는 LangGraph의 "graph + production runtime" 듀얼과 대응. CrewAI는 LangChain 명시적 독립.
- [[openai-openai-agents-python]] — **Anthropic 5 패턴 + OpenAI 6 확장 = 11종 reference 구현의 본체 단 풀스택 매핑**. [[openai]] 공식 1년차 SDK(★25K, v0.14.6)가 `examples/agent_patterns/`에 16개 .py로 11종 패턴을 SDK 본체와 한 묶음으로 박음 (cookbook이 sample 노트북이라면 본 SDK는 API 안정성 보장된 reference). **Anthropic 5 패턴 직접 매핑 (7파일)**: `deterministic.py`(2.6KB)=Prompt Chaining / `routing.py`(2.5KB)=Routing / `parallelization.py`(1.7KB)=Parallelization / `agents_as_tools.py`(2.7KB)+`agents_as_tools_streaming.py`(2.2KB)+`agents_as_tools_conditional.py`(5.2KB)+`agents_as_tools_structured.py`(2.0KB)=Orchestrator-Workers + 4종 변형 / `llm_as_a_judge.py`(2.9KB)=Evaluator-Optimizer. **OpenAI 확장 6 패턴 (9파일)**: (가) **Guardrails 3종** — `input_guardrails.py`(3.7KB) / `output_guardrails.py`(2.4KB) / `streaming_guardrails.py`(3.3KB) — 빠른 모델로 검증 후 느린 모델 보호 (latency 최적화 + tripwire 메커니즘으로 즉시 중단). (나) **Human-in-the-loop 3종** — `human_in_the_loop.py`(4.0KB, 승인 플로우) / `human_in_the_loop_custom_rejection.py`(3.8KB, 거절 시 커스텀 에러) / `human_in_the_loop_stream.py`(3.5KB, 스트림 변형) — RunState 일시정지·재개 메커니즘 ([[claude-managed-agents]] CMA의 HITL과 평행 패턴). (다) **Forced tool use** — `forcing_tool_use.py`(3.6KB, tool_choice 강제). 추가로 SDK는 **9개 운영 SOP 스킬 (`.agents/skills/`)**과 PLANS.md ExecPlans 메소드론을 자기 운영에 풀스택 박음. 회사 BI 응용 가설: Guardrails 3종은 BigQuery 쿼리 실행 전 비용 검증 + tripwire에 직접 차용 가능, HITL 3종은 게임 데이터 BI 승인 워크플로우(GMV 영향 큰 분석 결과)에 직접 매핑

## 열린 질문

- 5 패턴 외에 추가 분류가 등장할 가능성? (예: ReAct, MCTS 기반 에이전트는 5 패턴의 변종인가 별개인가?)
- Multi-agent 시스템 (서로 다른 페르소나의 에이전트들이 협업)은 5 패턴 중 어디?
- Evaluator-Optimizer의 evaluator가 사람일 때(HITL) 같은 패턴인가 별개 분류인가?
- 회사 BI에 도입 시 가장 ROI가 높은 패턴은? (가설: Routing — 모델 선택 자동화로 비용 즉시 절감)
