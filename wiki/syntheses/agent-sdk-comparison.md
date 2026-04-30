---
title: Agent SDK 비교 — OpenAI Agents SDK ↔ Claude Agent SDK
aliases:
- agent-sdk-comparison
- OpenAI vs Claude Agent SDK
- Agent SDK 비교
type: synthesis
category: ai
tags:
- agent-sdk
- openai-agents-python
- claude-agent-SDK
- agent-frameworks
- comparison
- multi-agent
- python
- mcp
sources:
- '[[openai-openai-agents-python]]'
- '[[anthropics-claude-cookbooks]]'
- '[[openai-openai-cookbook]]'
- '[[anthropics-skills]]'
related:
- '[[openai-agents-python]]'
- '[[claude-agent-sdk]]'
- '[[claude-managed-agents]]'
- '[[agent-patterns]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[vendor-neutral]]'
- '[[mcp]]'
- '[[matechat]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-stack-guide]]'
- '[[agent-stack-evolution]]'
- '[[agent-frameworks-matrix]]'
created: 2026-04-30
updated: 2026-04-30
inbound_count: 12
cited_by_count: 11
---

# Agent SDK 비교 — OpenAI Agents SDK ↔ Claude Agent SDK

## 한줄 요약

> 2025~2026년 두 양대 LLM 제공자가 공식 출하한 Python 멀티 에이전트 SDK. **OpenAI Agents SDK**(★25K, 1년 14 메이저 버전)는 명시적 패턴 reference + 9개 운영 SOP + Public API positional compatibility로 **API 표면이 풍부**한 반면, **Claude Agent SDK**(Claude Code의 raw agentic power 추출)는 6단계 튜토리얼 + Subagent + Hooks + MCP 통합으로 **운영 기법이 깊다**. 단순 "어느 게 더 강한가" 비교가 아니라 — owner의 도구 선택을 결정하는 **3축 트레이드오프**를 가시화한다.

## 왜 비교 synthesis가 필요한가

[[openai-openai-agents-python]] 후속 탐구 8번이 명시: "OpenAI Agents SDK ↔ [[claude-agent-sdk]] 비교 분석 — 같은 시기 한 쌍으로 종합 분석 (별도 synthesis 페이지 후보)". owner 입장에서 두 SDK 중 어느 쪽을 daily driver로 둘지, 어느 쪽을 회사 BI에 차용할지 의사결정할 때 표준 비교 frame이 필요.

## 메타 비교 (2026-04 기준)

| 축 | OpenAI Agents SDK | Claude Agent SDK |
|---|---|---|
| **저장소** | openai/openai-agents-python (★25,440) | (Claude Agent SDK는 SDK 패키지 + cookbooks가 reference) |
| **PyPI** | `openai-agents` v0.14.6 | (Anthropic 패키지) |
| **창설** | 2025-03-11 (1년 1개월차) | 2025년 (Claude Code의 SDK 추출) |
| **라이선스** | MIT | (Anthropic 라이선스) |
| **Python** | >=3.10 ~ 3.14 | (Python SDK) |
| **메이저 버전 케이던스** | 약 26일에 1 메이저 버전 | (안정화 단계) |
| **제공자 컨셉** | "OpenAI 공식 멀티 에이전트 SDK" | "Claude Code의 raw agentic power를 SW 외 도메인에 풀어놓는 SDK" |

## 3축 트레이드오프

### 1. API 표면적 vs 운영 기법 깊이

| 차원 | OpenAI Agents SDK | Claude Agent SDK |
|---|---|---|
| **메인 진입점** | `Runner` / `AgentRunner` (`run.py` 92KB) | `query` async iter / `ClaudeSDKClient` / `ClaudeAgentOptions` |
| **에이전트 정의** | `Agent` 클래스 (`agent.py` 42KB) — instructions, tools, model_settings, guardrails | `ClaudeAgentOptions` — 시스템 프롬프트 + 도구 + 권한 + hooks 한 묶음 |
| **상태 모델** | `RunState` (`run_state.py` 129KB) — `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES` | 세션 영속은 [[claude-managed-agents]]가 별도 hosting |
| **도구 시스템** | `tool.py` 72KB — function tools, tool guardrails, tool identity | Bash, Read (멀티모달), Edit, Write, WebSearch + MCP |
| **API 표면적** | **매우 풍부** (50+ 파일, dataclass·overload·type-safe) | **얇고 강력** — Claude Code 기법이 옵션화 |

**판단**: API surface로 학습할 게 많다 = OpenAI 우세. 단순 진입 + Claude Code 검증된 패턴 그대로 = Claude 우세.

### 2. 패턴 명시성 vs 자율성

| 차원 | OpenAI Agents SDK | Claude Agent SDK |
|---|---|---|
| **Anthropic 5 패턴 reference** | `examples/agent_patterns/` 7개 .py (Prompt Chaining/Routing/Parallelization/Orchestrator-Workers/Evaluator-Optimizer) | [[anthropics-claude-cookbooks]] `patterns/agents/` 3 노트북 (basic_workflows, evaluator_optimizer, orchestrator_workers) |
| **OpenAI 확장 패턴** | **9 .py 추가** — Guardrails 3종 (input/output/streaming), Human-in-the-loop 3종, Forced tool use, Agent-as-tool 4종 변형 | (HITL은 [[claude-managed-agents]]에서 등장) |
| **튜토리얼 깊이** | `docs/` 14 핵심 문서 (tools.md 38KB, running_agents.md 27KB) | `claude_agent_sdk/` 6단계 튜토리얼 (research → chief of staff → observability → SRE) |
| **자율성 강조** | tool_choice 강제, guardrail tripwire, structured 출력 | "minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead" |

**판단**: 명시적 패턴 학습 = OpenAI 우세 (16 .py reference 구현). 자율 에이전트의 통제 + 감수성 = Claude 우세 (raw agentic power 비유).

### 3. 거버넌스 + 운영 SOP

| 차원 | OpenAI Agents SDK | Claude Agent SDK |
|---|---|---|
| **AGENTS.md = CLAUDE.md** | 12,900B 양쪽 byte-for-byte 미러링 ([[vendor-neutral]] 패턴 8단계) | (Claude Code 자체 CLAUDE.md 사용) |
| **PLANS.md / ExecPlans** | 5,485B 자체 SDK용 NON-NEGOTIABLE 4 (self-contained / living / outcome-focused / explicit acceptance) | (별도 PLANS 패턴 미명시) |
| **운영 SOP 스킬** | **`.agents/skills/` 9개 SKILL.md** (code-change-verification, openai-knowledge, implementation-strategy, pr-draft-summary, runtime-behavior-probe 13.4KB ★ 등) — 스킬 chaining 명시 | Claude Code의 subagent + skill 시스템 ([[agent-skills]] 표준) |
| **API 호환성 정책** | **Public API Positional Compatibility** — dataclass 필드 순서를 호환성 계약으로 격상 | (별도 정책 미명시) |
| **Codex CLI 통합** | `.codex/hooks.json` Stop 훅 → `uv run python stop_repo_tidy.py` | (해당 없음) |
| **llms.txt** | `docs/llms.txt` (6.8KB) + `docs/llms-full.txt` (15KB) 양 변형 | (별도 채택 미확인) |

**판단**: 거버넌스 풀스택 채택 = OpenAI 우세 (자기 본체에 9개 SOP + ExecPlan + AGENTS.md 풀스택 적용). [[claude-code]]의 운영 기법 깊이 + [[anthropics-skills]] 표준 1차 출하 = Claude 우세.

## 어느 쪽을 owner가 채택해야 하나

### 기준 매트릭스

| owner 시나리오 | OpenAI 우세 | Claude 우세 |
|---|---|---|
| **[[matechat]] 39 SKILL 운영** | (Codex 통합 시) | ✓ Claude Code 직속, 1급 SKILL 표준 |
| **[[c2spf-analytics]] BI에 에이전트 도입** | ✓ Public API positional + RunState 직렬화로 production 운영 친화 | (Anthropic API + CMA hosted 옵션) |
| **개인 비서 AI 일상** | (Agents SDK 직접 사용) | ✓ Chief of Staff 노트북 ([[anthropics-claude-cookbooks]] 01번)이 정확히 매핑 |
| **명시적 멀티 에이전트 패턴 학습** | ✓ 11종 reference 구현 (Anthropic 5 + OpenAI 6 확장) | (3 노트북만, 깊이 < 표면적) |
| **운영 SOP 패키지화** | ✓ 9개 SKILL.md SOP 학습 reference | (자기 SKILL 작성 시 anthropics-skills의 17 사례 참조) |
| **자율성 + 컨텍스트 압축** | (`extended_thinking/` 별도) | ✓ Plan mode + Output styles + Hooks의 자연 통합 |

### 권고

- **owner daily driver**: [[claude-code]] (CLI 통합) → 자연스럽게 Claude Agent SDK 친화. **현재 default**.
- **회사 BI 에이전트화**: c2spf-analytics에 차용 시 OpenAI 측 9개 SOP 스킬을 4개(code-change-verification / openai-knowledge / docs-sync / pr-draft-summary)로 매핑 직접 차용 가능. (참조: [[openai-openai-agents-python]] "회사 BI 적용 가설" 가설 1)
- **둘 다 사용**: matechat은 Claude, c2spf 데이터 분석은 OpenAI Agents SDK PoC. [[vendor-neutral]] 패턴(`.agents/` + 미러링)으로 자산을 공유 가능.

## 거버넌스 자기 채택 = "메소드론과 본체의 한 묶음"

OpenAI 측의 두 자료가 결정적: [[openai-openai-cookbook]]은 **메소드론 정의 단** (PLANS.md/ExecPlan, AGENTS.md "Recent Learnings", registry.yaml 콘텐츠 거버넌스). [[openai-openai-agents-python]]은 **본체 단** (그 메소드론을 자기 핵심 SDK 운영에 풀스택 적용). **두 리포가 같은 회사**라는 점이 살아있는 거버넌스의 결정적 증거.

Claude 측은 다른 분할: [[anthropics-skills]] (표준 정의자 측) + [[anthropics-claude-cookbooks]] (실습 채널) + [[claude-agent-sdk]] (SDK 본체) — 3 layer 분리. OpenAI보다 **더 명확히 "표준 / 실습 / SDK"가 분리**됐지만, 거버넌스 자체 채택 깊이는 OpenAI보다 얕다 (PLANS.md 같은 명시 메소드론 미공개).

## 5 패턴 + 6 확장 = 11종 reference 구현 매트릭스

[[agent-patterns]]에 이미 통합되어 있지만, 본 비교에서 SDK 단위 매핑을 명시:

| 패턴 | OpenAI 파일 (`examples/agent_patterns/`) | Claude reference |
|---|---|---|
| **Prompt Chaining** | `deterministic.py` (2.6KB) | `basic_workflows.ipynb` |
| **Routing** | `routing.py` (2.5KB) | 동일 노트북 |
| **Parallelization** | `parallelization.py` (1.7KB) | 동일 노트북 |
| **Orchestrator-Workers** | `agents_as_tools.py` 4 변형 (10.1KB 합) | `orchestrator_workers.ipynb` |
| **Evaluator-Optimizer** | `llm_as_a_judge.py` (2.9KB) | `evaluator_optimizer.ipynb` |
| **Guardrails** ★ | `input_guardrails.py` + `output_guardrails.py` + `streaming_guardrails.py` (9.4KB) | (Claude는 별도 클래스 미공개, 직접 구현) |
| **Human-in-the-loop** ★ | `human_in_the_loop.py` 3 변형 (11.3KB) | [[claude-managed-agents]] CMA의 HITL 노트북 |
| **Forced tool use** ★ | `forcing_tool_use.py` (3.6KB) | (Claude는 tool_choice 직접 지원) |

→ **OpenAI는 패턴을 SDK 본체와 한 묶음**으로 출하, **Claude는 패턴을 cookbook + SDK + Managed Agents 3 층으로 분산**.

## 열린 질문

- 두 SDK의 호환성 레이어가 등장할까? (예: agentskills.io 같은 표준이 SDK 단위로도 등장)
- [[langgraph]] / [[pydantic-ai]] 같은 vendor-neutral 프레임워크가 양쪽을 wrap하는 추세 강화?
- 회사 BI에서 한쪽만 채택할지, 둘 다 채택해 작업별 분기할지의 ROI 비교 — 현재 가설은 후자.
- Anthropic이 본격 Agent SDK 출하 시 Claude Code의 raw agentic power 추출이 명시적 ExecPlan/거버넌스로 진화할까? (현재는 cookbook이 유일한 명시 채널)

## 메모

- 2026-04-30 시점 단일 snapshot. 두 SDK 모두 빠르게 진화 중 — 6개월 후 재검증 필요.
- 본 synthesis는 [[agent-frameworks-matrix]] (LangChain/LangGraph/CrewAI/DeepAgents/Pydantic AI 비교)와 보완 관계. 그쪽은 vendor-neutral 프레임워크 비교, 본 페이지는 vendor 1차 SDK 비교.
- owner의 sub-cluster 활용: 본 비교가 [[seokgeun-stack-guide]] "32 OSS" 카탈로그의 OpenAI 측 / Anthropic 측 sub-cluster 결정 시 직접 입력.
