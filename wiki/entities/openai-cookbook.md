---
title: openai-cookbook (OpenAI Cookbook)
aliases:
- OpenAI Cookbook
- OpenAI 쿡북
type: entity
entity_type: project
tags:
- openai-cookbook
- openai
- cookbook
- MIT
- jupyter-notebook
- registry-yaml
- agents-md
- plans-md
- exec-plans
- recent-learnings
- embeddings
- agents-SDK
- evals
- codex
- gpt-5
- gpt-oss
related:
- '[[openai]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[agent-patterns]]'
- '[[ml-ai]]'
- '[[anthropics-claude-cookbooks]]'
- '[[openai-openai-cookbook]]'
source_count: 1
observed_source_refs: 13
inbound_count: 37
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 15
---

# openai-cookbook (OpenAI Cookbook)

## 개요

`openai/openai-cookbook`은 [[openai]]가 2022-03부터 4년간 운영해온 공식 OpenAI API 활용 코드·기사 저장소다. ★73,042 / fork 12,325 (2026-04-27) / MIT 라이선스 / 주 언어 Jupyter Notebook. registry.yaml에 등록된 289개 콘텐츠와 115명 저자(authors.yaml)로 cookbook.openai.com 정적 사이트가 자동 생성된다. 본 위키 수집 대상이며, **AGENTS.md 안에 "Recent Learnings" 섹션을 둔 첫 메인스트림 살아있는 운영 노트** 사례로 [[agent-skills]] 외부 채택 7단계 진화의 7번째 단계를 박았다.

## 주요 특징

### 콘텐츠 구조

- **`articles/`** — 21개 narrative 기사 (PLANS.md / harmony format / 신뢰성 기법 / 문서 작성 원칙 등 메소드론 자료)
- **`examples/`** — 243개 카테고리 (agents_sdk / gpt-5 / evals / codex / chatgpt / voice_solutions / deep_research_api / responses_api / mcp / dalle / sora / multimodal / o-series / object_oriented_agentic_approach / partners / vector_databases / voice_solutions 등)
- **`images/`** — 다이어그램·스크린샷
- **`registry.yaml`** (3,180줄) — 모든 페이지 메타 단일 진실원
- **`authors.yaml`** (583줄) — 115명 저자 메타

### 거버넌스 3축

1. **AGENTS.md (5.5KB) — 살아있는 운영 노트**
 - 표준 7개 섹션 (Project Structure / Build/Test / Coding Style / Testing / Commit/PR / Metadata Workflow / Review Guidelines)
 - **`Recent Learnings`** 섹션이 결정적 차별점 — 6개 항목, 형식: "현상 → 대응 → 이유"
 - 다른 OSS의 정적 가이드(astral-sh/uv, scikit-learn, fastapi 등)와 본질적으로 다름
 - "These are considered priority 0 issues for this repo" — Review Guidelines가 코드 리뷰 우선순위 박는 단계로 진화

2. **PLANS.md (ExecPlans) — 7시간+ LLM 단일 작업 거버넌스**
 - `articles/codex_exec_plans.md` (16KB)에서 정의
 - NON-NEGOTIABLE 5 요건: 자기완결 / 살아있는 문서 / 초보자 구현 가능 / 관찰 가능한 동작 / 모든 용어 본문 정의
 - 3 모드: 작성(authoring) / 실행(implementing) / 토론(discussing)
 - 단일 fenced code block(md 라벨), 산문 우선

3. **registry.yaml + authors.yaml — 정적 사이트 자동화**
 - 새 콘텐츠 → registry 등록 → check_notebooks.py 검증 → PR 머지
 - cookbook.openai.com 페이지 1:1 대응
 - [[scikit-learn]] SLEP / [[pandas-dev]] PDEP가 표준 변경 거버넌스라면, registry.yaml은 콘텐츠 변경 거버넌스

### 콘텐츠 4년 진화 (registry 태그 빈도)

| 시대 | 대표 태그 | 빈도 |
|---|---|---|
| 2022~ RAG 폭발 | embeddings | 99 |
| 2022 초기 davinci | completions | 94 |
| 2024 GPT Actions | gpt-actions-library | 29 |
| 2023 Function Calling | functions | 27 |
| 2024 평가 인프라 | evals | 22 |
| 2024 ChatGPT Workspace | chatgpt | 33 |
| 2025 Responses API | responses | 32 |
| 2025 Agents SDK | agents-sdk | 16 |
| 2025 gpt-oss | gpt-oss | 13 |
| 2025 Codex / Reasoning | codex / reasoning | 8 / 12 |

### 핵심 articles/ 7편 (위키 수집 범위)

- `chatgpt-agents-sales-meeting-prep.md` — ChatGPT Workspace Agents 빌드
- `codex_exec_plans.md` — ★ PLANS.md 메소드론
- `how_to_work_with_large_language_models.md` — LLM 입문서 (Instruction/Completion/Scenario/Demonstration)
- `openai-harmony.md` — gpt-oss 5 roles + 3 channels 대화 포맷
- `related_resources.md` — LangChain·LlamaIndex·learnprompting 등 외부 큐레이션
- `techniques_to_improve_reliability.md` — CoT(18→79%) / Self-consistency / Tree of Thoughts
- `what_makes_documentation_good.md` — ★ 8 원칙 (skim 친화 / 단순 문장 / 약어 풀어쓰기 / take-aways up front)

## 관련 개념

- [[agent-skills]]: AGENTS.md 외부 채택 7단계 진화 7번째 사례 (살아있는 첫 사례)
- [[harness]]: PLANS.md ExecPlan 6번째 거버넌스 축
- [[agent-patterns]]: examples/agents_sdk/ — Anthropic 5 패턴의 OpenAI 측 비교 대상
- [[ml-ai]]: 가장 대표적 LLM API 검색 가능 사례 데이터베이스
- [[prompt-cache]]: Prompt_Caching101.ipynb / 201.ipynb 직접 사례
- [[context-engineering]]: examples/agents_sdk/session_memory.ipynb (Sessions API)
- [[mcp]]: examples/mcp/ + tag mcp 8건
- [[spec-driven-development]]: PLANS.md vs spec-kit Constitution 비교

## 출처

- [[openai-openai-cookbook]] — 본 저장소 1차 수집 (raw 11파일, 약 100KB) — AGENTS.md / registry.yaml / authors.yaml / articles/ 7편 + 메타.

## 논쟁/모순

> [!warning] 논쟁/모순
> - (없음)

## 메모

- **회사 BI 적용 시나리오**: 게임 데이터 분석 후보 기능(예: 플레이어 행동 임베딩 클러스터링)을 도입할 때 cookbook의 같은 태그 ipynb를 raw 다운로드 → 회사 데이터로 재현 → "Recent Learnings"의 같은 영역 함정 사전 확인. cookbook = 검색 가능한 사례 데이터베이스.
- **본 위키 차용 후보**:
 - `wiki/registry.yaml` 신설 후 `wiki/index.md` 자동 생성 PoC
 - `templates/style-guide.md` 신설, OpenAI 8 원칙 + 한국어 컨벤션 통합
 - `wiki/AGENTS.md` 또는 CLAUDE.md에 "Recent Learnings" 섹션 신설
 - `python .github/scripts/check_notebooks.py` 패턴 → `lint` 워크플로우 차용
- **변경 추적**: 2026-04-26 푸시 → 2026-04-27 수집. 향후 lint 시 registry.yaml diff 자동 인지 후속 후보.
- **Anthropic 측 대비**: [[anthropics-claude-cookbooks]]는 같은 카테고리이나, 콘텐츠 규모 차이가 크고 거버넌스 모델이 다름. 두 cookbook 비교는 OpenAI vs Anthropic 양 산맥의 메타 비교에 1차 자료.
