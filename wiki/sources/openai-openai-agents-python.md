---
title: openai/openai-agents-python — OpenAI Agents SDK 본체 + AGENTS.md=CLAUDE.md 동기화 + 9개 운영 SOP 스킬
type: source
source_type: article
source_url: https://github.com/openai/openai-agents-python
raw_path: raw/articles/openai-openai-agents-python/
author: OpenAI (Agents Team)
date_published: 2025-03-11
date_ingested: 2026-04-28
tags:
- openai-agents-python
- openai
- openai-agents
- agents-SDK
- python
- multi-agent
- agent-framework
- agent-skills
- agents-md
- plans-md
- exec-plans
- vendor-neutral
- codex
- mcp
- uv
- pyright
- MIT-license
- agent-patterns
- guardrails
- human-in-the-loop
- handoffs
- streaming
- runtime-behavior-probe
- implementation-strategy
related:
- '[[openai]]'
- '[[openai-agents-python]]'
- '[[openai-cookbook]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[agent-patterns]]'
- '[[spec-driven-development]]'
- '[[ml-ai]]'
- '[[mcp]]'
- '[[agent-stack-evolution]]'
- '[[uv]]'
- '[[python-packaging]]'
confidence: high
inbound_count: 47
aliases:
- Openai Agents Python
- openai agents python
- openai-agents-python
- openai/openai-agents-python — OpenAI Agents SDK 본체
- openai/openai-agents-python — OpenAI Agents SDK 본체 + AGENTS.md=CLAUDE.md 동기화 + 9개 운영 SOP 스킬
cited_by:
  - "[[agent-frameworks-matrix]]"
  - "[[agent-patterns]]"
  - "[[agent-sdk-comparison]]"
  - "[[agent-skills]]"
  - "[[agent-stack-evolution]]"
  - "[[anthropics-claude-cookbooks]]"
  - "[[astral-sh-uv]]"
  - "[[governance-axis-comparison]]"
  - "[[harness]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[mcp]]"
  - "[[ml-ai]]"
  - "[[openai]]"
  - "[[openai-agents-python]]"
  - "[[openai-openai-cookbook]]"
  - "[[python]]"
  - "[[vendor-neutral]]"
cited_by_count: 17
---

# openai/openai-agents-python — OpenAI Agents SDK 본체

> [!tldr] 한 화면 요약 (모바일·RAG 첫 청크용)
> [[openai|OpenAI]] 공식 멀티 에이전트 Python SDK (★25K, v0.14.6). **위키적 핵심**: `AGENTS.md = CLAUDE.md` byte-for-byte 동기화 + `.agents/skills/` 9개 SOP 스킬 + `examples/agent_patterns/` 16개 매핑 = [[agent-skills]] 외부 채택 8단계 진화의 첫 "본격 운영 SOP" 사례. [[openai-cookbook]] 패턴이 본체 SDK에 풀스택 적용된 거버넌스 자기 채택 결정적 증거. 본문 366줄.

## 한줄 요약

> OpenAI 공식 1년차 ★25K 멀티 에이전트 Python SDK(v0.14.6, MIT)로, **`AGENTS.md = CLAUDE.md` 동기화 패턴 + `.agents/skills/` 9개 운영 SOP 스킬 + `examples/agent_patterns/` 16개 패턴 매핑**의 3중 채택을 통해 [[openai-cookbook]]에서 권한 거버넌스 패턴을 자기 핵심 SDK 저장소에 풀스택 적용한 증거 — agent-skills 외부 채택 8단계 진화의 8번째이자 첫 "9개 본격 운영 SOP" 사례.

## 메타

- **Repository**: openai/openai-agents-python
- **별점/포크**: ★25,440 / fork 3,883 (수집일 2026-04-28 기준)
- **라이선스**: MIT
- **언어**: Python (>=3.10, 3.10~3.14 지원)
- **PyPI 패키지**: `openai-agents` v0.14.6 (1년 사이 14 메이저 버전)
- **창설일**: 2025-03-11 (1년 1개월차)
- **최종 push**: 2026-04-27 (수집일 전일까지 활발)
- **저장소 크기**: 28.7 MB (uv.lock 831KB 포함)
- **Topics**: agents, ai, framework, llm, openai, python
- **공식 문서**: [openai.github.io/openai-agents-python/](https://openai.github.io/openai-agents-python/)
- **번역**: 일본어(`docs/ja`), 한국어(`docs/ko`), 중국어(`docs/zh`) — 자동 생성, 직접 수정 금지
- **핵심 의존성**: `openai>=2.26`, `pydantic>=2.12`, `mcp>=1.19`, `websockets>=15`, `griffelib>=2`

## raw 파일 구조 (보관 36개 파일, 약 250KB)

```
raw/articles/openai-openai-agents-python/
├── README.md (6.0KB)
├── AGENTS.md (12.9KB) ★ 9개 스킬 + ExecPlan + Public API Positional 정책
├── CLAUDE.md (12.9KB) ← AGENTS.md와 완전 동일 (동기화 패턴)
├── PLANS.md (5.5KB) ★ NON-NEGOTIABLE 5요건 + ExecPlan Skeleton
├── LICENSE (1.1KB, MIT)
├── Makefile (1.8KB) — make sync/format/lint/typecheck/tests/coverage/snapshots-fix
├── pyproject.toml (5.7KB)
├── pyrightconfig.json (469B) — pyright 사용 (mypy 아님)
├── mkdocs.yml (15.4KB)
├── docs/ (14개 핵심 문서)
│   ├── agents.md (16.9KB), index.md, quickstart.md
│   ├── tools.md (37.9KB) ★ 가장 큼
│   ├── handoffs.md, guardrails.md, mcp.md (18.8KB), tracing.md
│   ├── context.md, multi_agent.md, running_agents.md (27.1KB), sandbox_agents.md
│   └── llms.txt (6.8KB) ★ llms.txt 표준 채택
├── .codex/ (Codex CLI 통합 ★)
│   ├── config.toml — `codex_hooks = true`
│   └── hooks.json — Stop 훅에서 `uv run python stop_repo_tidy.py`
├── .agents-skills/ (9개 SKILL.md, 통합 46.3KB)
│   ├── runtime-behavior-probe_SKILL.md (13.4KB) ★ 가장 큼
│   ├── final-release-review_SKILL.md (8.0KB)
│   ├── pr-draft-summary_SKILL.md (5.7KB)
│   ├── implementation-strategy_SKILL.md (4.5KB)
│   ├── docs-sync_SKILL.md (4.3KB)
│   ├── examples-auto-run_SKILL.md (3.2KB)
│   ├── test-coverage-improver_SKILL.md (2.7KB)
│   ├── code-change-verification_SKILL.md (2.5KB)
│   └── openai-knowledge_SKILL.md (1.9KB)
├── examples-readmes/agent_patterns_README.md (4.5KB)
└── src_agents__init__.py (15KB) — public surface
```

**제외**: `examples/`의 16개 .py 본체 (별도 raw 보관 X — 매핑 표만 본 페이지에 정리), `tests/`, `docs/scripts/`, `site/`, 9개 스킬 각각의 `agents/`·`scripts/`·`references/` 서브디렉토리, `uv.lock`(831KB), `src/agents/` 본체 (`run_state.py` 129KB / `run.py` 92KB / `tool.py` 72KB / `agent.py` 42KB 등 50+ 파일).

## 핵심 내용

### 1. AGENTS.md = CLAUDE.md — "양쪽 동일 내용" 동기화 패턴 (vendor-neutral 단순화)

루트의 `AGENTS.md`(12,900B)와 `CLAUDE.md`(12,900B)가 **byte-for-byte 동일**. uv가 `CLAUDE.md → @AGENTS.md` 1줄 import 패턴을 쓴 반면, openai-agents-python은 양쪽을 같은 내용으로 유지. Claude Code는 `CLAUDE.md`를, OpenAI Codex CLI는 `AGENTS.md`를, vendor-neutral 도구도 어느 쪽이든 작동. **한 진실원의 두 파일 미러링**.

이는 **agent-skills 외부 채택 8단계 진화의 8번째**:

| # | 저장소 | 패턴 | 발견 시점 |
|---|--------|------|------|
| 1 | anthropics/skills | 표준 정의 (SKILL.md 패키지) | |
| 2 | github/spec-kit | 메소드론 어댑터 + Codex Skills 통합 | |
| 3 | fastapi/fastapi | 라이브러리 self-hosted SKILL.md | |
| 4 | astral-sh/uv | `CLAUDE.md = @AGENTS.md` import (1줄) | |
| 5 | scikit-learn/scikit-learn | SLEP + AGENTS.md (965B) AI disclosure | |
| 6 | flutter/flutter | vendor-neutral `.agents/` + agentskills.io | |
| 7 | openai/openai-cookbook | AGENTS.md "Recent Learnings" 살아있는 운영노트 | |
| **8** | **openai/openai-agents-python** | **AGENTS.md=CLAUDE.md 동기화 + 9개 운영 SOP 스킬** | **(현재)** |

### 2. `.agents/skills/` 9개 운영 SOP — `$skill-name` 명령형 호출

`.agents/skills/` 안에 9개 SKILL.md. AGENTS.md "Mandatory Skill Usage" 섹션이 각 스킬을 `$skill-name` 명령형으로 호출. **트리거 조건과 스킵 조건을 모두 명시**.

| 스킬 | 크기 | 트리거 조건 | 비고 |
|------|------|--------|------|
| `$code-change-verification` | 2.5KB | `src/agents/`, `tests/`, `examples/`, `pyproject.toml`/`Makefile`/`mkdocs.yml`/CI 변경 시 | docs-only/repo-meta 변경은 스킵 |
| `$openai-knowledge` | 1.9KB | OpenAI API/Responses/Realtime/Agents SDK/ChatGPT Apps SDK 작업 시 | OpenAI Developer Docs MCP 서버 사용 |
| `$implementation-strategy` | 4.5KB | runtime/exported APIs/외부 config/persisted schema/wire protocol 변경 전 | 호환성 boundary 결정 |
| `$pr-draft-summary` | 5.7KB | 중간~큰 코드 변경 종료 시 | trivial/conversation-only/repo-meta는 스킵 |
| `$runtime-behavior-probe` | 13.4KB ★ | **manual-only** (사용자 명시적 호출 시) | edge case/undocumented 동작 검증 |
| `$docs-sync` | 4.3KB | 문서·코드 동기화 필요 시 | — |
| `$examples-auto-run` | 3.2KB | examples/ 자동 실행 검증 | — |
| `$final-release-review` | 8.0KB | 릴리스 직전 종합 검토 | `find_latest_release_tag.sh` 스크립트 보유 |
| `$test-coverage-improver` | 2.7KB | 커버리지 개선 작업 | — |

각 스킬은 자체 `agents/`(sub-agent prompts), 일부는 `scripts/`·`references/`·`templates/` 서브디렉토리까지 보유. **스킬 간 호출(skill chaining)도 명시** — 예: `$implementation-strategy`는 내부에서 `$final-release-review`의 `find_latest_release_tag.sh` 스크립트를 호출. 이는 spec-kit Codex Skills의 단방향 통합보다 한 단계 발전된 형태.

### 3. PLANS.md — Codex ExecPlan을 자기 SDK 운영에 직접 박음

[[openai-cookbook]] 발견된 `articles/codex_exec_plans.md`(16KB) 메소드론을 본 저장소가 **5,485B로 응축하여 자체 PLANS.md로 내장**. 4가지 NON-NEGOTIABLE 요건:

- **Self-contained / beginner-friendly**: 모든 용어 정의, 외부 링크 가정 금지
- **Living document**: Progress, Surprises & Discoveries, Decision Log, Outcomes & Retrospective 4개 섹션을 작업 중 갱신
- **Outcome-focused**: 사용자가 변경 후 무엇을 할 수 있는지 + 어떻게 작동하는지 관찰 가능
- **Explicit acceptance**: 행동/명령/관찰 가능한 출력으로 성공 증명

언제 ExecPlan을 쓰나 — **multi-step / multi-file / 신규 기능·리팩터 / 1시간 이상 예상 작업 시 필수**. AGENTS.md "ExecPlans" 섹션이 PLANS.md를 명시 호출. **cookbook이 가설로 제시한 PLANS.md 패턴이 OpenAI 자체 SDK 운영에 풀스택 적용된 증거**.

### 4. examples/agent_patterns/ — Anthropic 5패턴 + OpenAI 6확장 = 16개 reference 구현

| 카테고리 | Anthropic 명칭 | OpenAI 파일 | 비고 |
|----------|----------------|--------|------|
| **Prompt chaining** | prompt-chaining | `deterministic.py` (2.6KB) | 단계별 작업 분해 |
| **Routing** | routing | `routing.py` (2.5KB) | 언어 기반 라우팅 |
| **Parallelization** | parallelization | `parallelization.py` (1.7KB) | 병렬 실행 후 best 선택 |
| **Orchestrator-Workers** | orchestrator-workers | `agents_as_tools.py` (2.7KB) | 4종 변형 |
| | | `agents_as_tools_streaming.py` (2.2KB) | + `on_stream` 변형 |
| | | `agents_as_tools_conditional.py` (5.2KB) | 조건부 |
| | | `agents_as_tools_structured.py` (2.0KB) | `Agent.as_tool` |
| **Evaluator-Optimizer** | evaluator-optimizer | `llm_as_a_judge.py` (2.9KB) | feedback loop |
| **Guardrails** ★ | (없음, OpenAI 확장) | `input_guardrails.py` (3.7KB) | 입력 검증 + tripwire |
| | | `output_guardrails.py` (2.4KB) | 출력 검증 |
| | | `streaming_guardrails.py` (3.3KB) | 스트리밍 |
| **Human in the loop** ★ | (없음, OpenAI 확장) | `human_in_the_loop.py` (4.0KB) | 승인 플로우 |
| | | `human_in_the_loop_custom_rejection.py` (3.8KB) | 거절 시 커스텀 에러 |
| | | `human_in_the_loop_stream.py` (3.5KB) | 스트림 변형 |
| **Forced tool use** ★ | (없음, OpenAI 확장) | `forcing_tool_use.py` (3.6KB) | tool_choice 강제 |

**총 16개 .py = Anthropic 5패턴(7파일) + OpenAI 확장 6패턴(9파일)**. cookbook의 sample 노트북이 산발적이었다면, 본 저장소는 SDK 본체와 한 묶음으로 박혀 있어 **사실상 OpenAI 측 reference 구현**으로 기능. [[agent-patterns]] 페이지에 OpenAI 확장 3종(Guardrails/Human-in-the-loop/Forced tool use)을 명시 추가 대상.

### 5. SDK 코어 모듈 구조 (`src/agents/`)

50+ 파일의 단일 패키지 구조. 가장 큰 파일들:

| 파일 | 크기 | 역할 |
|------|------|------|
| `run_state.py` | 129KB | RunState 직렬화 + `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES` 거버넌스 |
| `run.py` | 92KB | `Runner` / `AgentRunner` 메인 진입점 |
| `tool.py` | 72KB | 도구 시스템 |
| `agent.py` | 42KB | Agent 클래스 |
| `result.py` | 39KB | 결과 처리 |
| `items.py` | 33KB | RunItem 타입 + 변환 |
| `run_context.py` | 20KB | 컨텍스트 |
| `function_schema.py` | 16KB | 함수 스키마 추론 |
| `_tool_identity.py` | 17KB | 도구 식별 |
| `usage.py` | 13KB | 사용량 추적 |
| `retry.py` | 12KB | 재시도 |
| `run_config.py` | 11KB | 실행 설정 |
| `apply_diff.py` | 11KB | 코드 편집 도구 |
| `guardrail.py` | 10KB | 가드레일 |
| `model_settings.py` | 8.4KB | 모델 설정 |
| `agent_tool_input.py` | 8.4KB | 도구 입력 |
| `tool_guardrails.py` | 8.3KB | 도구 가드레일 |

서브디렉토리: `mcp/`, `memory/`, `models/`, `realtime/`, `voice/`, `tracing/`, `sandbox/`, `extensions/`, `handoffs/`, `run_internal/`, `util/`. AGENTS.md는 `run.py`가 비대해지면 `run_internal/run_loop.py`·`turn_resolution.py`·`tool_execution.py`·`session_persistence.py`로 리팩터하라고 명시.

### 6. Codex CLI 통합 (`.codex/`)

```
.codex/
├── config.toml (95B)  — codex_hooks = true
├── hooks.json (275B)  — Stop 훅: uv run python stop_repo_tidy.py
└── hooks/             — stop_repo_tidy.py 실제 스크립트 위치
```

**Codex가 자체 라이브러리 개발 운영에 사용**되는 첫 명시 사례. Stop 훅은 작업 종료 시 자동으로 repo 정리(임시 파일 삭제 등). cookbook codex_exec_plans.md 메소드론이 본 저장소 운영에 박힌 두 번째 증거 (PLANS.md + Codex 훅).

### 7. Public API Positional Compatibility 정책

AGENTS.md가 명시:

> "Treat the parameter and dataclass field order of exported runtime APIs as a compatibility contract. For public constructors (for example `RunConfig`, `FunctionTool`, `AgentHookContext`), preserve existing positional argument meaning. Do not insert new constructor parameters or dataclass fields in the middle of existing public order."

이는 **dataclass 필드 순서를 호환성 계약으로 격상**한 첫 명시 사례. 일반 Python 라이브러리는 dataclass 필드 순서를 비명시적 관행으로 취급하지만, 본 저장소는 release 태그 이후 변경에는 명시 정책 적용. **API positional compatibility는 회사 BI 외부 API에도 그대로 차용 가능**한 패턴.

## 인사이트

### Insight 1: AGENTS.md=CLAUDE.md 양쪽 동일 — 가장 단순한 vendor-neutral 적응

uv는 `CLAUDE.md`에 `@AGENTS.md` 한 줄만 두고 import. flutter는 `.agents/`를 진실원으로 삼고 `.claude/skills` 심볼릭 링크. **openai-agents-python은 둘 다 같은 12,900B 내용을 그대로 유지**. 가장 단순한 패턴이지만 **에이전트 도구가 어느 쪽을 읽더라도 100% 동일한 정보**를 보장.

함의: 외부 도구 추가 시(예: Cursor의 `.cursorrules`, GitHub Copilot의 `.github/copilot-instructions.md`) 같은 내용을 추가 미러링하는 N-way 동기화로 확장 가능. 자동 동기화 스크립트(make hook 등)가 없다면 휴먼 동기화 부담은 단점.

### Insight 2: 9개 운영 SOP 스킬 — agent-skills 표준의 본격적 운영 채택

flutter 3개 스킬이 "표준 채택자가 정의자의 위치 컨벤션을 누른 첫 사례"였다면, openai-agents-python 9개는 **실무 운영 워크플로우 전체를 SKILL.md로 명문화한 첫 사례**:

- 코드 변경 검증 (`code-change-verification`)
- API 호환성 결정 (`implementation-strategy`)
- 외부 지식 조회 (`openai-knowledge` — MCP 서버 통합)
- PR 마무리 (`pr-draft-summary`)
- 문서 동기화 (`docs-sync`)
- 예제 자동 실행 (`examples-auto-run`)
- 릴리스 검토 (`final-release-review`)
- 테스트 커버리지 개선 (`test-coverage-improver`)
- 런타임 동작 검증 (`runtime-behavior-probe`) — 가장 큰 SKILL (13.4KB)

각 스킬은 trigger·skip·workflow·output expectation을 명시하여 **에이전트가 읽고 즉시 실행 가능한 표준 운영 절차**. spec-kit이 9개 슬래시 명령(`/specify`, `/plan` 등)을 SDD 메소드론으로 정의했다면, OpenAI는 9개 스킬을 SDK 개발 SOP로 정의한 평행 사례.

### Insight 3: examples/agent_patterns/ — Anthropic 5패턴 + OpenAI 6확장

[[agent-patterns]] 종합 분석에 OpenAI 확장 3종 명시 추가 필요:

- **Guardrails (3종)**: input/output/streaming. 빠른 모델로 검증 후 느린 모델 보호 (latency 최적화 + tripwire 메커니즘)
- **Human-in-the-loop (3종)**: 승인 플로우 / 거절 커스텀 에러 / 스트리밍. RunState 일시정지·재개 메커니즘 (= [[claude-managed-agents]] CMA의 human-in-the-loop와 평행 패턴)
- **Forced tool use**: tool_choice 매개변수로 강제 호출

cookbook의 sample 노트북과 달리 SDK 본체와 함께 패키지되어 **API 안정성 보장된 reference 구현**으로 기능.

### Insight 4: PLANS.md self-application — 메소드론과 본체의 한 묶음

cookbook 발견된 ExecPlan 메소드론을 본 저장소가 자체 운영에 풀스택 적용:

- AGENTS.md → "Use an ExecPlan when work is multi-step..." 명시 호출
- PLANS.md → 5,485B로 응축 (cookbook 16KB의 ⅓), 같은 NON-NEGOTIABLE 4 + Living Sections 4
- `.codex/hooks.json` → Codex 훅으로 자동 실행

**메소드론을 정의한 곳(cookbook)과 본체에서 채택한 곳(agents-python)이 같은 회사**라는 점이 살아있는 거버넌스의 결정적 증거. 회사 BI 적용 시 PLANS.md를 분석 SOP에 차용한다면 같은 묶음 패턴으로 가져갈 수 있음.

### Insight 5: 1년 14 메이저 버전 (v0.14.6) — 빠른 반복 + 호환성 정책

2025-03-11 창설 → 2026-04-28 현재 v0.14.6. **약 26일에 1 메이저 버전**. 이는 cookbook(289개 콘텐츠 / 4년)의 누적·정적 모델과 정반대로, 본 SDK는 빠른 반복·잦은 API 진화 모델. 그래서:

- AGENTS.md "Public API Positional Compatibility" 정책으로 호환성 boundary 명시
- `RunState`의 `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES`로 직렬화 버전 관리
- `implementation-strategy` 스킬이 release 태그 기준으로만 breaking change 판단 (`branch-local churn` 무시)

빠른 반복 + 호환성 정책의 두 축이 **1년 14 메이저 버전이 가능한 비밀**.

### Insight 6: pyright + uv + ruff = Astral·Microsoft 도구 스택 정착

본 저장소가 사용:

- **uv**: `uv.lock` 831KB, `uv sync` / `uv run python` Makefile 명령
- **ruff** (Astral): `make format` / `make lint`
- **pyright** (Microsoft): `pyrightconfig.json`, `make typecheck` (mypy 아님)
- **MkDocs**: `mkdocs.yml` 15.4KB로 문서 사이트
- **MCP**: `mcp>=1.19.0` 의존성 명시

OpenAI 공식 SDK가 **Astral 도구 스택(uv + ruff)을 채택**한 첫 메인스트림 사례. fastapi 디폴트 스택과 동일한 방향. **pyright를 mypy 대신 채택**한 점은 결정적 — Microsoft도 OpenAI도 동일한 정적 타입 검사기 표준에 수렴.

### Insight 7: llms.txt 표준 채택 (`docs/llms.txt` 6.8KB + `docs/llms-full.txt` 15KB)

llms.txt는 LLM이 사이트를 빠르게 색인할 수 있도록 마크다운으로 사이트 구조를 요약하는 표준 (llmstxt.org). 본 저장소가 두 변형 모두 채택:

- `llms.txt` (6.8KB): 핵심 페이지 링크만
- `llms-full.txt` (15KB): 전체 콘텐츠 인라인

**MkDocs와 같은 사람용 사이트와 LLM용 색인 양쪽 운영** — agent-skills/AGENTS.md가 코드베이스 안 에이전트용이라면, llms.txt는 외부 에이전트가 본 SDK 문서를 활용할 때의 진입점. 회사 BI Confluence/Notion/MkDocs에도 차용 가능.

## 인용 (raw에서 직접 발췌)

### AGENTS.md — 9개 스킬 호출 정책 (Mandatory Skill Usage)

> Run `$code-change-verification` before marking work complete when changes affect runtime code, tests, or build/test behavior. ... You can skip `$code-change-verification` for docs-only or repo-meta changes (for example, `docs/`, `.agents/`, `README.md`, `AGENTS.md`, `.github/`), unless a user explicitly asks to run the full verification stack.

### AGENTS.md — Public API Positional Compatibility

> Treat the parameter and dataclass field order of exported runtime APIs as a compatibility contract. For public constructors (for example `RunConfig`, `FunctionTool`, `AgentHookContext`), preserve existing positional argument meaning. Do not insert new constructor parameters or dataclass fields in the middle of existing public order.

### PLANS.md — NON-NEGOTIABLE 4 + Skeleton

> Self-contained and beginner-friendly: define every term; include needed repo knowledge; avoid assuming prior plans or external links.
> Living document: revise Progress, Surprises & Discoveries, Decision Log, and Outcomes & Retrospective as work proceeds while keeping the plan self-contained.
> Outcome-focused: describe what the user can do after the change and how to see it working; the plan must lead to demonstrably working behavior, not just code edits.
> Explicit acceptance: state behaviors, commands, and observable outputs that prove success.

### `.agents/skills/runtime-behavior-probe/SKILL.md` — 3가지 게이트

> Before a live probe, apply three lightweight gates:
> - Destination gate. Use only a live destination that is clearly allowed for the task.
> - Intent gate. Run the live probe only when the user explicitly wants runtime verification on that integration, or explicitly approves it after you propose the probe.
> - Data gate. If the probe will read environment variables, mutate remote state, incur material cost, or exercise non-public or user data, name the exact variable names or data class and get explicit approval first.

### `.agents/skills/implementation-strategy/SKILL.md` — Default implementation stance

> Prefer deletion or replacement over aliases, overloads, shims, feature flags, and dual-write logic when the old shape is unreleased. ... If review feedback claims a change is breaking, verify it against the latest release tag and actual external impact before accepting the feedback.

## 후속 탐구

1. **`agents/` 서브디렉토리 9개 본체 수집** — 9개 스킬 각각의 sub-agent 프롬프트가 어떤 패턴인지
2. **`src/agents/run_state.py` (129KB) 전수 분석** — `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES` 패턴이 회사 BI 캐시·세션 직렬화에 적용 가능한지
3. **examples/agent_patterns/ 16개 .py 본체 수집** — 11종 패턴 reference 구현 코드 차용 가능성 (특히 Guardrails 3종 / HITL 3종)
4. **`docs/tools.md` (37.9KB) 단독 수집** — 가장 큰 단일 문서, 도구 시스템 전체 가이드
5. **MCP 1.19 의존성 추적** — 본 저장소가 [[mcp]] 1.19를 디폴트 채택. mcp 문서 1.19 변경점 수집
6. **examples/financial_research_agent/, customer_service/, research_bot/** — 도메인별 reference agent 사례 분석 (회사 BI에 차용 가능 도메인 식별)
7. **번역 시스템 (`docs/scripts/translation`)** — co-op-translator와 다른 번역 파이프라인 비교
8. **OpenAI Agents SDK ↔ [[claude-agent-sdk]] 비교 분석** — 같은 시기 한 쌍으로 종합 분석 (별도 synthesis 페이지 후보)
9. **agentskills.io 표준 본 저장소 명시 채택 여부 확인** — flutter 명시 인용 vs OpenAI는 명시 안 함 (사실상 채택)
10. **PLANS.md ExecPlan 차용 PoC** — c2spf-analytics 분기 분석 작업에 ExecPlan 양식 1건 적용해보기

## 회사 BI 적용 가설

### 가설 1: 9개 스킬 중 4개를 c2spf-analytics에 차용

| OpenAI 스킬 | c2spf-analytics 적용 |
|------|------|
| `$code-change-verification` | BigQuery SQL 변경 시 `dbt test` + `pytest` + linter 자동 실행 SOP |
| `$docs-sync` | 대시보드 변경 시 README/Confluence 자동 갱신 SOP |
| `$runtime-behavior-probe` | 새 BigQuery 쿼리 배포 전 dry-run + `EXPLAIN` + 샘플 데이터 검증 매트릭스 |
| `$pr-draft-summary` | 게임 데이터 BI PR 작성 시 결과 메트릭 변화 자동 요약 |

전체 9개 중 BI 도메인에 직접 매핑되는 4개. 도입 ROI: PR 작성·코드 검증·문서 동기화 시간 50%↓ 추정.

### 가설 2: PLANS.md ExecPlan을 분기 대형 분석에 적용

cookbook에서 가설로 제시했던 PLANS.md 패턴이 OpenAI 자체 SDK에서 풀스택 적용된 증거()로 신뢰도 상승. c2spf-analytics 분기 코호트 분석 1건에 ExecPlan 양식 적용 PoC. 단일 분석가 + LLM 협업으로 7시간+ 단일 작업 가능성 검증.

### 가설 3: API Positional Compatibility를 Analytics API에 적용

c2spf-analytics가 외부 (그라파나 / 다른 팀 / 외부 클라이언트)에 노출하는 dataclass·Pydantic 모델·API 응답 필드 순서를 OpenAI agents-python 정책처럼 "release 이후는 호환성 계약" 명시. 게임 데이터 BI 외부 소비자 보호 + 빠른 반복 양립 가능.

## 메모

[[openai-openai-cookbook]]의 후속이자 한 쌍. cookbook이 "OpenAI는 살아있는 운영 노트 패턴 + PLANS.md 메소드론 도입"이라고 박았다면, **그 정의자가 자기 핵심 SDK 운영에 풀스택 적용**한 직접 증거. 두 자료로 OpenAI의 거버넌스 통합이 명확해짐:

- **가이드 단**: cookbook (메소드론 + Recent Learnings)
- **본체 단**: agents-python (9개 SOP 스킬 + PLANS.md + AGENTS.md=CLAUDE.md + Codex 훅)

다음 후보:
- [[anthropics-claude-cookbooks]] 14 디렉토리 본체 단독 수집 (Claude SDK 측 reference)
- OpenAI Apps SDK / ChatGPT Apps 별도 저장소 (현재 별도)
- agents-python의 9개 sub-agent prompts 단독 수집 (이번 raw 수집에서 의도적 제외)
- agentskills.io 표준 자체 (vendor-neutral 표준 정의자 측 자료)
