---
title: "openai-agents-python (OpenAI Agents SDK)"
type: entity
entity_type: tool
tags: [openai-agents-python, openai-agents, openai, agents-SDK, python, multi-agent, agent-framework, MIT-license, mcp, uv, pyright, ruff, agents-md, plans-md, exec-plans, agent-skills, codex, handoffs, guardrails, human-in-the-loop, runtime-behavior-probe, implementation-strategy, run-state, schema-version, 18회차]
related:
  - "[[openai]]"
  - "[[openai-cookbook]]"
  - "[[agent-skills]]"
  - "[[harness]]"
  - "[[agent-patterns]]"
  - "[[mcp]]"
  - "[[uv]]"
  - "[[python-packaging]]"
  - "[[claude-agent-sdk]]"
  - "[[agent-stack-evolution]]"
  - "[[langgraph]]"
  - "[[deepagents]]"
  - "[[crewai]]"
  - "[[pydantic-ai]]"
  - "[[fastmcp]]"
  - "[[openai-openai-agents-python]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 24
inbound_count: 63
created: 2026-04-28
updated: 2026-04-28
---

# openai-agents-python (OpenAI Agents SDK)

## 개요

OpenAI 공식 **Python 멀티 에이전트 프레임워크**. 2025-03-11 창설, MIT 라이선스, ★25,440 / fork 3,883, PyPI 패키지명 `openai-agents` v0.14.6 (1년 사이 14 메이저 버전). 기능적으로는 [[claude-agent-sdk]]·[[claude-managed-agents]]의 OpenAI 측 평행 제품. 거버넌스적으로는 본 위키의 **[[agent-skills]] 외부 채택 8단계 진화의 8번째 사례**이자 **9개 운영 SOP 스킬을 명문화한 첫 메인스트림 라이브러리**.

## 메타

- **저장소**: https://github.com/openai/openai-agents-python
- **공식 문서**: https://openai.github.io/openai-agents-python/
- **PyPI**: `openai-agents` v0.14.6
- **라이선스**: MIT
- **Python 버전**: >=3.10 (3.10/3.11/3.12/3.13/3.14 지원)
- **창설**: 2025-03-11 (1년 1개월차)
- **최종 push**: 2026-04-27
- **저장소 크기**: 28.7 MB
- **유형**: 라이브러리 + 프레임워크
- **핵심 의존성**: `openai>=2.26`, `pydantic>=2.12`, `mcp>=1.19`, `websockets>=15`, `griffelib>=2`

## 주요 특징

### 1. 핵심 SDK 구조

`src/agents/` 단일 패키지, 50+ 파일. 가장 큰 모듈:

- `run_state.py` (129KB) — RunState 직렬화 + `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES`
- `run.py` (92KB) — `Runner` / `AgentRunner` 메인 진입점
- `tool.py` (72KB) — 도구 시스템
- `agent.py` (42KB) — Agent 클래스
- `result.py` (39KB), `items.py` (33KB), `run_context.py` (20KB)

서브디렉토리: `mcp/`, `memory/`, `models/`, `realtime/`, `voice/`, `tracing/`, `sandbox/`, `extensions/`, `handoffs/`, `run_internal/`, `util/`. 11개 도메인 통합 패키지.

### 2. 9개 운영 SOP 스킬 (`.agents/skills/`)

`AGENTS.md`가 각 스킬을 `$skill-name` 명령형으로 호출:

| 스킬 | 트리거 | 호출 정책 |
|------|--------|--------|
| `$code-change-verification` | src/tests/examples/build config 변경 시 | 자동 |
| `$openai-knowledge` | OpenAI API 작업 시 | OpenAI Developer Docs MCP 통합 |
| `$implementation-strategy` | runtime/exported API 변경 전 | 호환성 boundary 결정 |
| `$pr-draft-summary` | 중간~큰 코드 변경 종료 | 자동 (skip 명시 가능) |
| `$runtime-behavior-probe` | 사용자 명시 호출 | manual-only, 13.4KB ★ |
| `$docs-sync` | 문서·코드 sync 필요 시 | 자동 |
| `$examples-auto-run` | examples/ 검증 시 | 자동 |
| `$final-release-review` | 릴리스 전 종합 검토 | `find_latest_release_tag.sh` 보유 |
| `$test-coverage-improver` | 커버리지 개선 시 | 자동 |

**스킬 간 호출 (skill chaining)** 명시 — 예: `$implementation-strategy`가 `$final-release-review/scripts/find_latest_release_tag.sh` 호출.

### 3. AGENTS.md = CLAUDE.md 동기화 패턴

루트의 `AGENTS.md`(12,900B)와 `CLAUDE.md`(12,900B)가 byte-for-byte 동일. [[uv]]의 `@AGENTS.md` import 패턴과 [[flutter]]의 `.agents/` 심볼릭 링크 패턴의 중간 — **양쪽 동일 파일 미러링**. Claude Code/Codex/vendor-neutral 도구 어느 쪽이든 100% 동일 정보 보장.

### 4. PLANS.md ExecPlan (5,485B)

[[openai-cookbook]] `articles/codex_exec_plans.md`(16KB)를 응축. NON-NEGOTIABLE 4 (자기완결 / 살아있는 / Outcome-focused / Explicit acceptance) + Living Sections 4 (Progress / Surprises & Discoveries / Decision Log / Outcomes & Retrospective). multi-step / 1시간 이상 작업 시 필수.

### 5. examples/agent_patterns/ — 11종 패턴 reference 구현 (16개 .py)

**Anthropic 5패턴** ([[agent-patterns]]):
- `deterministic.py` (prompt-chaining), `routing.py`, `parallelization.py`
- `agents_as_tools*.py` 4종 (orchestrator-workers + 변형)
- `llm_as_a_judge.py` (evaluator-optimizer)

**OpenAI 6확장**:
- Guardrails 3종 (input/output/streaming) — tripwire 메커니즘
- Human-in-the-loop 3종 (base/custom_rejection/stream) — RunState 일시정지·재개
- Forced tool use (tool_choice 강제)

### 6. Codex CLI 통합 (`.codex/`)

- `config.toml` — `codex_hooks = true`
- `hooks.json` — Stop 훅: `uv run python stop_repo_tidy.py`

OpenAI Codex가 자체 SDK 개발 운영에 사용되는 첫 명시 사례.

### 7. 도구 스택 정착

- **uv** ([[astral-sh-uv]]) — `uv.lock` 831KB, `uv sync` / `uv run python`
- **ruff** (Astral) — `make format` / `make lint`
- **pyright** (Microsoft) — `pyrightconfig.json`, `make typecheck` (mypy 아님)
- **MkDocs** — `mkdocs.yml` 15.4KB
- **MCP** — `mcp>=1.19.0` 디폴트 의존성

### 8. Public API Positional Compatibility

dataclass 필드 순서를 호환성 계약으로 격상한 첫 명시 사례. `RunConfig`, `FunctionTool`, `AgentHookContext` 등 public 생성자의 positional argument 의미 보존 + 새 필드는 끝에만 추가.

## 관련 개념

- [[agent-skills]]: 8번째 외부 채택 사례 (9개 SOP 스킬 명문화)
- [[harness]]: PLANS.md ExecPlan + 9개 운영 스킬로 SDK 본체 운영
- [[agent-patterns]]: Anthropic 5패턴 + OpenAI 6확장 = 11종 reference 구현
- [[mcp]]: `mcp>=1.19.0` 디폴트 의존성, `docs/mcp.md` 18.8KB 자체 가이드
- [[uv]]: `uv.lock` 831KB, Makefile 명령 전체가 `uv` 기반
- [[python-packaging]]: 본 SDK가 `openai-agents` 0.14.6 PyPI 패키지

## 관련 엔티티

- [[openai]]: 운영 주체 (조직)
- [[openai-cookbook]]: 메소드론 정의 (가이드 단), 본 SDK는 본체 단
- [[claude-agent-sdk]]: Anthropic 측 평행 제품 (비교 대상)
- [[claude-managed-agents]]: Anthropic의 hosted 변형 vs OpenAI agents-python의 self-hosted

## 18회차 형제 프레임워크 비교 (cross-reference)

| 프레임워크 | 메타포 | OpenAI Agents SDK 대비 |
|------------|--------|------------------------|
| [[langgraph]] | state graph + Pregel | durable execution 1급, 모델-agnostic |
| [[deepagents]] | "harness" + LangGraph 위 프리셋 | 4종 빌트인 도구 (Claude Code 패턴) |
| [[crewai]] | Crews + Flows 듀얼 | role-playing 자연스러움, LangChain 독립 |
| [[pydantic-ai]] | type-safe agent + 11 강점 | type-safety 압도적, model-agnostic |
| [[fastmcp]] | MCP 서버 빌드 | 직교 (SDK가 아닌 도구 layer) |

→ OpenAI Agents SDK는 **11종 패턴 reference + OpenAI 락인 + RunState 직렬화**가 차별점. 18회차에서 6×N agent-frameworks-matrix.md로 정량 비교.

## 의사결정 컨텍스트 (raw 인용)

> "OpenAI 공식 1년차 ★25K 멀티 에이전트 Python SDK(v0.14.6, MIT). AGENTS.md = CLAUDE.md 동기화 + .agents/skills/ 9개 운영 SOP 스킬 + examples/agent_patterns/ 16개 패턴 매핑의 3중 채택을 통해 openai-cookbook에서 권한 거버넌스 패턴을 자기 핵심 SDK 저장소에 풀스택 적용한 증거 — agent-skills 외부 채택 8단계 진화의 8번째이자 첫 '9개 본격 운영 SOP' 사례."
> — [[openai-openai-agents-python]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] OpenAI agent 본진. [[pydantic]] 디폴트 + [[mcp]]·[[uv]]·[[ruff]] 채택. [[matechat|MateChat 사이드 프로젝트]] 39 SKILL 운영의 OpenAI 진영 multi-agent 후보. **9개 운영 SOP 스킬 + AGENTS.md=CLAUDE.md + 16개 패턴 매핑 3중 채택**은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 [[agent-skills]] 8단계 진화 정점 사례 — [[langchain]]·[[crewai]]·[[pydantic-ai]]와 함께 [[agent-frameworks-matrix]] 비교됨.

## 출처

- [[openai-openai-agents-python]] — 본 SDK 저장소 1차 수집 (14회차, 2026-04-28)
- [[langchain-ai-deepagents]] — 18회차 비교 대상 추가
- [[crewaiinc-crewai]] — 18회차 비교 대상 추가
- [[pydantic-pydantic-ai]] — 18회차 비교 대상 추가

## 논쟁/모순

> [!warning] 논쟁/모순
> - (없음)


## 메모

- **1년 14 메이저 버전 (v0.14.6)** — 약 26일에 1 메이저 버전. cookbook(289개 / 4년)의 정적 누적 모델과 정반대로 빠른 반복·잦은 API 진화. Public API Positional Compatibility + RunState `CURRENT_SCHEMA_VERSION`이 이를 가능하게 함.
- **회사 BI 적용 가능 영역**:
  - `examples/financial_research_agent/`, `customer_service/`, `research_bot/` 도메인 reference (BI 도메인 매핑)
  - 9개 스킬 중 4개 (`code-change-verification`, `docs-sync`, `runtime-behavior-probe`, `pr-draft-summary`)를 c2spf-analytics SOP에 차용
  - `RunState` 직렬화 패턴을 BI 캐시·세션 직렬화에 응용
- **다음 수집 후보**:
  - 9개 스킬의 `agents/` sub-agent 프롬프트 본체 (별도 회차)
  - `examples/agent_patterns/` 16개 .py 본체 (11종 패턴 코드)
  - `docs/tools.md` 37.9KB 단독 수집
  - `mcp>=1.19.0` 변경점 (mcp 1.x 별도 회차)
- **별도 운영 저장소** (본 회차 미수집):
  - openai/agents.md — AGENTS.md 표준 정의 자체
  - openai/codex — Codex CLI 본체
  - openai/openai-python — OpenAI 공식 Python SDK (본 Agents SDK가 의존)
