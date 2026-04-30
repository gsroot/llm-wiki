---
title: anthropics/claude-cookbooks — Claude API · Agent SDK · Managed Agents 실습 노트북 모음
type: source
source_type: article
source_url: https://github.com/anthropics/claude-cookbooks
raw_path: raw/articles/anthropics-claude-cookbooks/
author: Anthropic
date_published: 2026-04
date_ingested: 2026-04-27
tags:
- claude-cookbooks
- anthropic
- claude-agent-SDK
- agent-patterns
- prompt-caching
- tool-use
- RAG
- mcp
- skills
related:
- '[[claude-code]]'
- '[[agent-skills]]'
- '[[anthropics-skills]]'
- '[[mcp]]'
- '[[harness]]'
- '[[context-engineering]]'
- '[[token-economy]]'
- '[[karpathy-autoresearch]]'
confidence: high
inbound_count: 65
aliases:
- Anthropics Claude Cookbooks
- anthropics claude cookbooks
- anthropics/claude-cookbooks — Claude API · Agent SDK · Managed Agents 실습 노트북 모음
cited_by:
  - "[[agent-patterns]]"
  - "[[agent-skills]]"
  - "[[agent-stack-evolution]]"
  - "[[anthropic]]"
  - "[[anthropics-skills]]"
  - "[[astral-sh-uv]]"
  - "[[claude-agent-sdk]]"
  - "[[claude-code]]"
  - "[[claude-managed-agents]]"
  - "[[context-engineering]]"
  - "[[github-spec-kit]]"
  - "[[harness]]"
  - "[[karpathy-autoresearch]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[mcp]]"
  - "[[openai-cookbook]]"
  - "[[openai-openai-agents-python]]"
  - "[[openai-openai-cookbook]]"
  - "[[pandas-dev-pandas]]"
  - "[[prompt-cache]]"
  - "[[rag]]"
  - "[[spec-driven-development]]"
  - "[[token-economy]]"
cited_by_count: 23
---

# anthropics/claude-cookbooks — Claude API · Agent SDK · Managed Agents 실습 노트북 모음

## 한줄 요약

> Anthropic이 직접 운영하는 **Claude API/SDK 실습 노트북 카탈로그** (★41,654 / fork 4,643). 14개 디렉토리에 걸쳐 "Building Effective Agents" 5 패턴 구현, Agent SDK 6단계 튜토리얼, Managed Agents 8개 운영 시나리오, Skills 3종 실습, RAG/멀티모달/툴 사용/캐싱 등 ~100개 노트북을 단일 리포에 정리. [[anthropics-skills]]가 "배포 채널"이라면 이쪽은 "**실습/레퍼런스 채널**" — `registry.yaml` 한 파일로 노트북 메타를 카탈로그화하고 `/notebook-review` / `/model-check` / `/link-review` 슬래시 커맨드를 CI와 로컬에서 동시에 돌리는 운영 표준이 핵심.

## 메타

- **저장소**: [anthropics/claude-cookbooks](https://github.com/anthropics/claude-cookbooks)
- **라이선스**: MIT
- **언어**: Python (Jupyter notebooks)
- **별/포크**: 41,654 / 4,643 (2026-04-27 기준)
- **최근 push**: 2026-04-25 (활발히 유지보수)
- **패키지 매니저**: uv (pyproject.toml + uv.lock 371KB)
- **린터/포매터**: ruff (line length 100, double quotes, native Jupyter 지원)
- **CI**: pre-commit hooks + GitHub Actions (`/notebook-review` 등 슬래시 커맨드를 CI가 그대로 호출)

## 디렉토리 카탈로그

총 14개 주제 디렉토리 + 메타 파일들로 구성. 각 디렉토리 README는 `raw/articles/anthropics-claude-cookbooks/` 에 보관.

| 디렉토리 | 핵심 주제 | 노트북 수 | 비고 |
|----------|----------|---------|------|
| `patterns/agents/` | "Building Effective Agents" 5 패턴 | 3 | Erik Schluntz & Barry Zhang 블로그의 reference 구현 |
| `claude_agent_sdk/` | Claude Agent SDK 튜토리얼 시리즈 | 6 | research → chief of staff → observability → SRE |
| `managed_agents/` | [[claude-managed-agents|Claude Managed Agents]] (CMA) | 8 | Anthropic의 hosted runtime, 세션 영속 + HITL |
| `skills/` | Agent Skills 실습 (introduction → financial → custom) | 3 | document-skills(xlsx/pptx/pdf/docx) production 사용 |
| `tool_use/` | 도구 사용 패턴 | 13 | memory_cookbook, automatic-context-compaction, parallel_tools 등 |
| `capabilities/` | 핵심 능력 가이드 | 6 | classification, RAG, contextual-embeddings, summarization, text-to-sql, knowledge-graph |
| `multimodal/` | 비전·이미지 | 6 | best_practices, crop_tool, sub_agents, charts/PPT 해석 |
| `extended_thinking/` | Extended thinking | 2 | with_tool_use 변형 포함 |
| `misc/` | 운영 기법 | 14 | prompt_caching, batch_processing, JSON mode, evals, citations, session_memory_compaction |
| `third_party/` | 외부 통합 | 8 폴더 | Pinecone, MongoDB, VoyageAI, Wikipedia, LlamaIndex, Deepgram, ElevenLabs, WolframAlpha |
| `observability/` | 사용량/비용 API | 1 | usage_cost_api |
| `finetuning/` | Bedrock 파인튜닝 | 1 | finetuning_on_bedrock |
| `coding/` | 코딩 워크플로우 | 1 | prompting_for_frontend_aesthetics |
| `tool_evaluation/` | tool 자체 평가 | 1 | tool_evaluation + evaluation.xml |

## 핵심 1 — `patterns/agents/` "Building Effective Agents" 5 패턴

Anthropic이 [공식 블로그](https://anthropic.com/research/building-effective-agents)로 정의한 **에이전트 워크플로우 5종**의 reference 구현. 위키에서 가장 무거운 추가가 이쪽으로 가야 하는 이유: 이 5분류가 사실상 "현재 LLM 에이전트 카테고리의 표준 분류"가 되어가고 있음.

| 패턴 | 종류 | 핵심 아이디어 |
|------|------|-------------|
| **Prompt Chaining** | Basic | 단일 작업을 순차 서브태스크로 분해, 각 단계가 이전 결과 위에 빌드 |
| **Routing** | Basic | 입력 특성에 따라 전용 LLM 경로를 동적으로 선택 |
| **Parallelization** | Basic | 독립 서브태스크를 여러 LLM에 분산해 동시 처리 |
| **Orchestrator-Workers** | Advanced | 오케스트레이터가 동적으로 서브태스크 생성 + 워커들 조율 |
| **Evaluator-Optimizer** | Advanced | 한 LLM이 출력 생성, 다른 LLM이 평가/피드백 → 반복 개선 |

수록 노트북: `basic_workflows.ipynb` (앞 3개), `evaluator_optimizer.ipynb`, `orchestrator_workers.ipynb`.

## 핵심 2 — `claude_agent_sdk/` 6단계 튜토리얼

Anthropic이 "Claude Code의 raw agentic power를 SW 외 도메인에 풀어놓는다"는 명시적 비전으로 만든 튜토리얼 시리즈. 각 노트북이 다음 단계로 빌드.

| 노트북 | 빌드되는 에이전트 | 신규 도입 기법 |
|--------|-----------------|--------------|
| `00_The_one_liner_research_agent` | 자율 조사 에이전트 | `query` async iter, WebSearch, Read 멀티모달, ClaudeSDKClient |
| `01_The_chief_of_staff_agent` | 스타트업 CEO용 비서 | CLAUDE.md 영속 컨텍스트, output styles, plan mode, custom slash commands, hooks(컴플라이언스), 서브에이전트, Bash 통합 |
| `02_The_observability_agent` | DevOps 모니터링 | Git MCP(13+ tools), GitHub MCP(100+ tools), CI/CD 분석 |
| `03_The_site_reliability_agent` | SRE 자동 대응 | 자체 MCP 서버(JSON-RPC subprocess), Prometheus PromQL, read-write remediation, PreToolUse safety hooks, PagerDuty/Confluence 옵션 통합 |
| `04_migrating_from_openai_agents_sdk` | 마이그레이션 | OpenAI Agents SDK → Claude Agent SDK 변환 |
| `05_Building_a_session_browser` | 세션 브라우저 | 세션 로그 시각화 |

내포된 메시지: **"Claude Code = Claude의 raw agentic power를 위한 bare-metal harness"** 라는 자기 정의(README의 "minimal yet complete and sophisticated interface")를 명시적으로 박아둠. [[harness]] 개념의 anthropic-side 정통 정의.

## 핵심 3 — `managed_agents/` [[claude-managed-agents|Claude Managed Agents]] (CMA)

Anthropic의 **hosted runtime for stateful, tool-using agents**. 에이전트와 sandboxed 환경을 한 번 정의하면 세션마다 파일/툴 상태/대화가 영속.

엔트리포인트: `CMA_iterate_fix_failing_tests.ipynb` (do→observe→fix 루프) — agent / environment / session, file mounts, streaming event loop를 모두 도입.

| 노트북 | 학습 포인트 |
|-------|-----------|
| `data_analyst_agent` | CSV → narrative HTML 보고서 (pandas + plotly) |
| `slack_data_bot` | 위 에이전트를 Slack 봇으로 wrap, 멘션 시 in-thread 응답 + 멀티턴 |
| `sre_incident_responder` | 페이저 알림 → 세션 시작 → PR 생성 → human approval 후 머지 |
| `CMA_iterate_fix_failing_tests` | 입문 — 모든 API shape 도입 |
| `CMA_orchestrate_issue_to_pr` | issue→fix→PR→CI→review→merge, 모의 `gh` CLI 사용 |
| `CMA_explore_unfamiliar_codebase` | 낯선 코드 그라운딩 + 의도된 stale-doc 트랩 |
| `CMA_gate_human_in_the_loop` | 비용 승인 등 HITL — `decide` / `escalate` custom tool |
| `CMA_prompt_versioning_and_rollback` | 서버사이드 프롬프트 버전 관리 — v1 평가 → v2 출시 → 회귀 감지 → 롤백 |
| `CMA_operate_in_production` | MCP 툴셋, vault per-end-user 자격 증명, `session.status_idled` 웹훅 패턴 |

`stream_until_end_turn` 헬퍼가 utilities 모듈에 추출되어 있음 — gate 노트북만 예외(`requires_action` idle bounce 처리 때문에 인라인).

## 핵심 4 — `skills/` Agent Skills 실습 3종

[[anthropics-skills]] 리포가 **스킬 카탈로그/마켓플레이스**라면, 이쪽은 **스킬 사용법을 익히는 노트북**.

| 노트북 | 다루는 내용 |
|--------|-----------|
| `01_skills_introduction` | Skills 아키텍처, 베타 헤더 3개(`code-execution-2025-08-25`, `files-api-2025-04-14`, `skills-2025-10-02`), Excel/PPT/PDF 첫 생성 |
| `02_skills_financial_applications` | 실제 재무 데이터(financial_statements.csv 등) → 대시보드/포트폴리오/리포트, CSV→Excel→PPT→PDF 크로스포맷 |
| `03_skills_custom_development` | 재무 비율 계산기, 브랜드 가이드라인 스킬, 재무 모델링 suite 직접 구축 |

`custom_skills/` 디렉토리에 3개 실제 커스텀 스킬 사례가 들어있음(analyzing-financial-statements, applying-brand-guidelines, creating-financial-models). [[agent-skills]] 페이지의 progressive disclosure 설명을 BI 도메인 사례로 완성.

## 핵심 5 — Anthropic의 노트북 운영 표준

CLAUDE.md에 박혀 있는 **Anthropic 자체의 표준 운영 패턴**. 우리 위키 운영에도 직접 차용 가치 있음.

### 1. 슬래시 커맨드 = CI = 로컬

```
/notebook-review    # 노트북 품질 종합 점검
/model-check        # Claude 모델 ID가 최신인지 검증
/link-review        # 변경된 파일의 링크 검증
```

세 커맨드는 `.claude/commands/`에 정의되어 있고, **Claude Code(로컬)와 GitHub Actions(CI)가 같은 정의를 호출**한다. "로컬에서 통과 = CI에서 통과" 보장 패턴 — Microsoft for-beginners의 단일 운영체계와 같은 발상이지만, 여기는 슬래시 커맨드가 그 "단일 채널" 역할.

### 2. 모델 ID 정책 (CLAUDE.md "Key Rules")

- **Always** non-dated alias 사용: `claude-sonnet-4-6`, `claude-haiku-4-5`, `claude-opus-4-6`
- **Never** dated ID: `claude-sonnet-4-6-20250514` 같은 건 금지
- **Bedrock**은 별개 형식: `anthropic.claude-opus-4-6-v1`, global endpoint는 `global.` prefix
- Bedrock pre-Opus 4.6 모델은 dated ID 필수

### 3. registry.yaml — 노트북 카탈로그 단일 진실원

```yaml
- title: Build a data analyst agent with Claude Managed Agents
  description: ...
  path: managed_agents/data_analyst_agent.ipynb
  authors: [charmaine, jyan-anthropic]
  date: '2026-04-08'
  categories: [Agent Patterns, Tools]
```

새 노트북 추가 = registry.yaml에 1 entry. 카테고리는 비공개 enum이지만 `Agent Patterns`, `Tools`, `RAG & Retrieval`, `Multimodal`, `Integrations`, `Observability`, `Evals` 등이 추출 가능.

### 4. authors.yaml — 기여자 메타

GitHub username → {name, website, avatar} 매핑. 별도 파일로 분리해 registry는 username만 들고 있게 함 — 정규화의 흔적.

### 5. 노트북 출력 정책

> "Notebook outputs are intentionally kept in this repository as they demonstrate expected results for users."

CONTRIBUTING.md 명시. 기대 결과를 노트북 자체가 들고 다니게 함 — RAG 학습 데이터로서의 가치를 의식한 결정.

## 주요 인사이트

### 1. "skills 리포 ↔ cookbooks 리포" 분업 구조 명료

| 리포 | 역할 | 단위 | 라이선스 |
|------|------|------|----------|
| [[anthropics-skills]] | 배포 채널 (마켓플레이스 + 표준 스킬 17개) | SKILL.md 패키지 | source-available + Apache 2.0 혼합 |
| **claude-cookbooks** | 실습 채널 (~100 노트북 + 카탈로그) | Jupyter notebook | MIT |

두 리포가 합쳐 "Anthropic 표준 스택" — 위키에서 [[claude-code]] / [[agent-skills]] / [[claude-agent-sdk]] / [[claude-managed-agents]] 4개 엔티티가 짝을 이룸.

### 2. Building Effective Agents 5 패턴이 위키 빈자리

[[karpathy-autoresearch]]는 "자율 연구 루프 1종"이 reference. 그러나 일반화된 에이전트 워크플로우 분류는 위키에 아직 없음. **Anthropic의 5 패턴은 [[autonomous-research-loop]]보다 한 단계 위의 분류 체계** — 자율 연구 루프는 "Evaluator-Optimizer + Orchestrator-Workers의 도메인 특화 합성"으로 자리매김 가능.

### 3. Memory Cookbook이 [[context-engineering]] "Memories" 항목의 코드 레퍼런스

`tool_use/memory_cookbook.ipynb` (615줄 마크다운 추출) — Microsoft lesson 13의 7가지 메모리 타입(Working/Short-term/Long-term/Persona/Episodic/Entity/Structured RAG)을 **실제 코드 인터페이스로 구현하는 방법**. context-engineering.md에 raw 보관 사실 + 한 단락 추가.

### 4. Prompt Caching이 [[token-economy]] 직결 보강

`misc/prompt_caching.ipynb` — 5분 / 1시간 TTL 캐시, breakpoint 4개 한도, 1024 토큰 최소 단위, 캐시 적중 시 입력 비용 0.1× 등 토큰 경제학의 운영 핸들. 위키에 코드 사례가 없었음.

### 5. Chief of Staff Agent — 석근 관심사 직결

README의 "AI Chief of Staff for a startup CEO" 시나리오가 석근의 **"개인 비서 AI 서비스 개발"** 관심사에 정확히 매핑. CLAUDE.md 영속 + output styles + plan mode + custom slash commands + hooks(audit trail) + subagent orchestration의 **모든 Claude Code 운영 기법을 한 노트북에 압축**.

### 6. Managed Agents = "에이전트의 백엔드 hosting"

서버사이드 프롬프트 버전 관리, vault-backed 자격 증명, session 영속, status_idled 웹훅 — 이건 **에이전트의 PaaS 추상화**. SaaS로 에이전트를 배포할 때의 표준 인프라 패턴이 여기 박혀 있음. 이는 회사 BI에서 에이전트화 검토 시 직접 비교 대상.

## 위키 갱신 포인트

| 페이지 | 갱신 내용 |
|--------|----------|
| [[claude-code]] | "raw agentic power의 bare-metal harness" 인용 + Agent SDK / Managed Agents 시퀀스 추가 |
| [[agent-skills]] | skills/ 노트북 3종 + custom_skills 사례 → "스킬 사용법 학습 경로" 보강 |
| [[mcp]] | Observability Agent / SRE Agent / CMA_operate_in_production이 MCP를 실제 운영에 어떻게 쓰는지 |
| [[harness]] | "minimal yet complete and sophisticated interface" 자기 정의 인용, claude_agent_sdk가 harness를 SW 외 도메인으로 푸는 예 |
| [[context-engineering]] | memory_cookbook + automatic-context-compaction + session_memory_compaction 3종 코드 사례 |
| [[token-economy]] | prompt_caching.ipynb의 5분/1시간 TTL · 4 breakpoint 한도 · 1024 토큰 최소 등 운영 핸들 |
| 신규 [[anthropic]] | organization 페이지 — Microsoft 페이지와 균형 |
| 신규 [[claude-agent-sdk]] | tool 페이지 — Agent SDK 자체의 자리 |
| 신규 [[agent-patterns]] | concept 페이지 — Building Effective Agents 5 패턴 |

## 석근 직결 활용 시나리오

1. **개인 비서 AI**: `01_The_chief_of_staff_agent.ipynb`를 직접 따라 한 번 돌려보고, CLAUDE.md / output styles / hooks / subagent를 본인 워크플로우에 매핑.
2. **회사 BI에 에이전트 도입 검토**: `data_analyst_agent.ipynb` (CSV → HTML 보고서) + `slack_data_bot.ipynb`을 Pseudo-PoC로 사용. CMA의 vault-backed credentials 패턴이 사내 BI의 다중 테넌트 자격 증명 분리에 그대로 적용 가능.
3. **토큰 비용 최적화**: `prompt_caching.ipynb` 한 번 읽고 [[token-economy]] 한 페이지 갱신.
4. **자체 위키 운영 표준 도입**: `/notebook-review`·`/model-check`·`/link-review` 같은 슬래시 커맨드를 llm-wiki에도 만들 수 있음. CLAUDE.md "lint" 워크플로우의 코드화 자연스러운 연장.
5. **Building Effective Agents 5 패턴 학습**: `patterns/agents/`의 3 노트북 → `synthesis` 페이지 1개로 나만의 정리.

## 인용할 만한 구절

> "What makes Claude Code special isn't just code understanding; it's the ability to (...) These capabilities have made Claude Code the closest thing to a 'bare metal' harness for Claude's raw agentic power: a minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead."
> — `claude_agent_sdk/README.md`

> "Claude Managed Agents is Anthropic's hosted runtime for stateful, tool-using agents. You define an agent and a sandboxed environment once, then run them in sessions that persist files, tool state, and conversation across turns."
> — `managed_agents/README.md`

> "Notebook outputs are intentionally kept in this repository as they demonstrate expected results for users."
> — `CONTRIBUTING.md`

## 메모

- raw 보관 17개 파일(3,410 lines): 루트 메타 5종(README/CLAUDE.md/CONTRIBUTING.md/Makefile/pyproject.toml) + 디렉토리 README 5종(patterns·sdk·managed·skills·capabilities) + 카탈로그 메타 2종(registry.yaml·authors.yaml) + 핵심 노트북 마크다운 추출 5종(basic-workflows·research-agent·chief-of-staff·memory-cookbook·prompt-caching). 거대 ipynb 본체는 보관 제외(3MB+ 멀티모달 스크린샷 등) — 본질은 마크다운에 다 있음.
- 후속 탐구 후보: (a) Building Effective Agents 5 패턴 별도 concept 페이지 분리, (b) claude_agent_sdk + managed_agents 둘 다 entity로 만든 뒤 [[claude-code]] / [[anthropic]]과의 관계 그래프 정리, (c) `/notebook-review` 같은 lint 슬래시 커맨드를 llm-wiki에 적용.
- 저장소가 4월 25일에도 push되는 활발한 상태 — 향후 cookbook 추가 시 registry.yaml만 다시 가져와도 카탈로그 갱신 가능.
