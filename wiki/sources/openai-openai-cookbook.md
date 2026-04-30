---
title: openai/openai-cookbook — OpenAI API 활용 코드·기사 4년 모음 + 살아있는 AGENTS.md
type: source
source_type: article
source_url: https://github.com/openai/openai-cookbook
raw_path: raw/articles/openai-openai-cookbook/
author: OpenAI (community resource)
date_published: 2022-03-11
date_ingested: 2026-04-27
tags:
- openai-cookbook
- openai
- prompt-engineering
- embeddings
- agents-SDK
- codex
- gpt-5
- gpt-oss
- evals
- agents-md
- plans-md
- exec-plans
- registry-yaml
- jupyter-notebook
- MIT-license
- recent-learnings
related:
- '[[openai]]'
- '[[openai-cookbook]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[agent-patterns]]'
- '[[spec-driven-development]]'
- '[[ml-ai]]'
- '[[prompt-cache]]'
- '[[context-engineering]]'
- '[[mcp]]'
- '[[agent-stack-evolution]]'
confidence: high
inbound_count: 39
cited_by:
- '[[agent-patterns]]'
- '[[agent-skills]]'
- '[[agent-stack-evolution]]'
- '[[anthropics-claude-cookbooks]]'
- '[[anthropics-skills]]'
- '[[astral-sh-uv]]'
- '[[claude-code]]'
- '[[fastapi-fastapi]]'
- '[[flutter-flutter]]'
- '[[github-spec-kit]]'
- '[[harness]]'
- '[[llm-infra-meta-cluster]]'
- '[[mcp]]'
- '[[microsoft-data-science-for-beginners]]'
- '[[ml-ai]]'
- '[[openai]]'
- '[[openai-cookbook]]'
- '[[openai-openai-agents-python]]'
- '[[pandas-dev-pandas]]'
cited_by_count: 19
aliases:
- Openai Cookbook
- openai cookbook
- openai-cookbook
- openai/openai-cookbook — OpenAI API 활용 코드·기사 4년 모음
- openai/openai-cookbook — OpenAI API 활용 코드·기사 4년 모음 + 살아있는 AGENTS.md
---

# openai/openai-cookbook — OpenAI API 활용 코드·기사 4년 모음

> [!tldr] 한 화면 요약 (모바일·RAG 첫 청크용)
> [[openai|OpenAI]] 공식 4년차 레시피 모음 (★73K, 289 콘텐츠, 115 저자). **위키적 핵심**: `AGENTS.md`에 **"Recent Learnings"** 섹션 = 가이드를 살아있는 운영 노트로 운영하는 첫 메인스트림 사례 + `PLANS.md`(ExecPlan) = 단일 LLM 작업 7시간+ 가능케 하는 6번째 거버넌스 축. 본문 316줄.

## 한줄 요약

> OpenAI 공식이 운영하는 4년차 ★73K 레시피 모음(289개 콘텐츠 / 115명 저자)으로, **AGENTS.md 안에 "Recent Learnings" 섹션을 두어 가이드를 살아있는 운영 노트로 운영하는 첫 메인스트림 사례**이며, `PLANS.md`(ExecPlan) 패턴은 단일 LLM 작업 7시간+를 가능케 하는 6번째 거버넌스 축이다.

## 메타

- **Repository**: openai/openai-cookbook
- **별점/포크**: ★73,042 / fork 12,325 (수집일 2026-04-27 기준)
- **라이선스**: MIT
- **주 언어**: Jupyter Notebook
- **창설**: 2022-03-11 (4년차)
- **최근 푸시**: 2026-04-26 (수집 직전 활발)
- **홈페이지**: https://cookbook.openai.com (정적 사이트, registry.yaml에서 자동 생성)
- **콘텐츠 규모**: registry.yaml 3,180줄 / 289개 등록 항목 (articles 21 + examples 243 + 기타 25)
- **저자 풀**: authors.yaml 583줄 / 115명 (OpenAI 직원·파트너·커뮤니티)
- **연도별 콘텐츠 분포**: 2022년 27 / 2023년 97 / 2024년 63 / 2025년 86 / 2026년 16 (2023년이 LLM 폭발기로 최다)
- **수집 범위**: 루트 메타 + 핵심 가이드 7편 (raw 11파일, 약 100KB). 거대한 `examples/` (243개 ipynb, 다수 1MB+) 본체는 제외하고 메소드론·거버넌스 자료에 집중.

## 핵심 내용

### 1. AGENTS.md = "살아있는 운영 노트" 패턴 (★ 핵심 발견)

5,561 bytes의 `AGENTS.md`가 표준 7개 섹션을 모두 갖추되, 다른 사례와 결정적으로 다른 부분이 **"Recent Learnings"** 섹션이다 (6개 항목, 본문 약 25%).

```markdown
## Recent Learnings

- **`uv run` can inherit the wrong virtualenv in this repo** -> Clear `VIRTUAL_ENV`...
- **Realtime eval shared imports can resolve the wrong module under pytest** -> ...
- **Run-level grades can be overweighted by long simulations** -> ...
- **Synthetic-audio scaffold requests can pick the wrong harness** -> ...
- **Task-specific single-turn grading can outgrow the shared crawl schema** -> ...
- **Synthetic learner audio can sound like eval scaffolding** -> ...
```

각 항목 형식: **현상** → **대응** → **이유**. 모두 실제 작업 중 발견된 함정·솔루션이며, 가이드(정적)가 아니라 **운영 일지(살아있는)** 성격이다.

이는 [[anthropics-skills]] SKILL.md (정적 패키지) / [[fastapi-fastapi]] `.agents/skills/fastapi/SKILL.md` (정적 컨벤션) / [[astral-sh-uv]] AGENTS.md (정적 single source) / [[scikit-learn]] AGENTS.md (정적 AI disclosure) / [[flutter-flutter]] vendor-neutral `.agents/` (정적 자산) 5 사례 모두와 본질적으로 다른 6번째 사례 — **AGENTS.md를 살아있는 작업기억으로 운영**.

### 2. PLANS.md / ExecPlans = 6번째 거버넌스 축

`articles/codex_exec_plans.md` (16.5KB)에서 소개되는 패턴:

- **목적**: Codex / `gpt-5.2-codex`가 단일 프롬프트로 **7시간+ 작업**을 수행하도록 만드는 메타 문서.
- **구조**: `AGENTS.md`에 한 줄 (`When writing complex features..., use an ExecPlan from .agent/PLANS.md`) + `.agent/PLANS.md` 본체.
- **3 모드**: ① 작성(authoring) ② 실행(implementing) ③ 토론(discussing) — 같은 ExecPlan을 모드별로 다르게 다룸.
- **NON-NEGOTIABLE 5 요건**:
 1. 자기완결 (self-contained) — 외부 컨텍스트 0% 가정
 2. 살아있는 문서 (living) — 진행 따라 revise
 3. 초보자가 처음부터 끝까지 구현 가능
 4. 단순 코드 변경 아닌 **관찰 가능한 동작** 결과물
 5. 모든 전문 용어를 본문에서 직접 정의
- **포맷 강제**: 단일 fenced code block 안 (md 라벨), 산문 우선, 체크리스트는 Progress 섹션에서만 허용.

이는 [[github-spec-kit]] Constitution(헌법형) / [[anthropics-skills]] SKILL.md(자동 호출 트리거형) / [[pandas-dev-pandas]] PDEP(분산 의사결정형)와 다른 **명세 + 진행 + 학습 단일 파일** 모델. 7시간 작업 가능성이 차별 지표.

### 3. registry.yaml + authors.yaml 메타데이터 거버넌스

cookbook.openai.com 정적 사이트는 `registry.yaml` 한 파일에서 모든 페이지가 생성된다. 새 콘텐츠 추가 워크플로우:

1. `examples/<topic>/` 또는 `articles/`에 ipynb·md 추가
2. `registry.yaml`에 항목 등록 (title, path, slug, description, date, authors, tags)
3. `authors.yaml`에 저자 메타 추가 (name, website, avatar) — 없으면 GitHub 프로필에서 자동
4. `python .github/scripts/check_notebooks.py` 검증
5. PR 템플릿 체크리스트 통과 후 머지

이는 [[scikit-learn]] SLEP / [[pandas-dev]] PDEP가 **표준 변경**에 사용하는 거버넌스라면, registry.yaml은 **콘텐츠 변경**에 적용되는 거버넌스 — 같은 "표준화 분리" 정신의 다른 응용.

### 4. 콘텐츠 4년 진화 — 태그 분포로 본 OpenAI API 발자취

registry.yaml 태그 빈도 (상위 25개):

| 순위 | 태그 | 빈도 | 의미 |
|---|---|---|---|
| 1 | embeddings | 99 | 2022~ Ada/text-embedding-3 시대 RAG 폭발 |
| 2 | completions | 94 | 초기 davinci-003 시대 잔재 |
| 3 | chatgpt | 33 | 2024~ workspace agents 카테고리 |
| 4 | responses | 32 | 2025 Responses API 출시 후 |
| 5 | gpt-actions-library | 29 | 2024 GPT Actions 시대 |
| 6 | functions | 27 | 2023 Function Calling 출시 |
| 7 | evals | 22 | 2024 평가 인프라 본격화 |
| 8 | agents-sdk | 16 | 2025 Agents SDK 출시 |
| 9 | vision | 15 | GPT-4V 이후 |
| 10 | fine-tuning | 14 | DPO·SFT 등 |
| 11 | tiktoken | 13 | 토큰 카운팅 도구 |
| 12 | open-models | 13 | gpt-oss 시리즈 |
| 13 | gpt-oss | 13 | 2025 첫 오픈 가중치 모델 |
| 14 | reasoning | 12 | o-series 추론 모델 |
| 15 | audio | 12 | Realtime / TTS / Whisper |
| 16 | agents | 12 | 일반 에이전트 |
| 17 | mcp | 8 | 2025 [[mcp]] 채택 |
| 18 | codex | 8 | Codex CLI · ExecPlan |
| 19 | gpt-5 | 7 | 2025~ GPT-5 시리즈 |
| 20 | tracing | 5 | Agents SDK 트레이싱 |

태그 분포는 **OpenAI API 4년 진화의 정확한 화석 기록**이다. 회사 BI에서 어떤 OpenAI 기능을 채택할지 의사결정할 때 "비슷한 사례가 cookbook에 몇 개 있는가"가 중요한 신호.

### 5. articles/ 핵심 7편 (수집 범위)

| 파일 | 크기 | 핵심 |
|---|---|---|
| `chatgpt-agents-sales-meeting-prep.md` | 14KB | ChatGPT Workspace Agents 빌드 — 캘린더/SharePoint/웹검색 통합. 2026-04-22 최신 |
| `codex_exec_plans.md` | 16KB | ★ PLANS.md 메소드론 (위 §2) |
| `how_to_work_with_large_language_models.md` | 8KB | LLM 입문서 — Instruction/Completion/Scenario/Demonstration 4 모드 |
| `openai-harmony.md` | 29KB | gpt-oss harmony format — 5 roles (system/developer/user/assistant/tool) + 3 channels (final/analysis/commentary) |
| `related_resources.md` | 9KB | LangChain, LlamaIndex, Haystack, Outlines, LMQL, learnprompting.org 등 외부 도구·강의 큐레이션 |
| `techniques_to_improve_reliability.md` | 42KB | CoT(18%→79%) / Self-consistency(57%→74%) / Tree of Thoughts / STaR 등 신뢰성 기법 종합 |
| `what_makes_documentation_good.md` | 9KB | ★ 위키 운영 원칙 차용 가치 매우 높음 |

### 6. `what_makes_documentation_good.md` — 위키 운영 차용 가치

OpenAI가 자체 문서 작성에 사용하는 8가지 원칙:

1. **Make docs easy to skim** — 섹션 제목, 짧은 단락, 토픽 선두 배치
2. **Write well** — 단순 문장, 좌분지 회피, 데모스트라티브 대명사 회피
3. **Be broadly helpful** — 약어 풀어쓰기 (RAG → retrieval-augmented generation), 초심자 우선
4. **Break up your docs into sections** — Conceptual / How-to / Reference 구분
5. **Don't bury the lede** — Take-aways up front, 결론 먼저
6. **Show, don't tell** — 코드 예제 self-contained, 의존성 최소화
7. **Be consistent** — Title Case, terminal commas, 명명 컨벤션
8. **Be careful with code** — API 키 절대 코드에 박지 말 것 (`OPENAI_API_KEY` env)

이 원칙들은 본 위키의 source / entity / concept 페이지 작성 스타일에 직접 적용 가능하며, 특히 "informative section titles" 원칙은 현재 `## 핵심 내용` 같은 추상 제목을 `## OpenAI Cookbook은 4년간 어떻게 진화했나` 같은 구체 제목으로 바꿀 후속 점검 후보.

### 7. 평가(evals) + 에이전트(agents-sdk) 인프라

`examples/agents_sdk/` 디렉토리는 OpenAI Agents SDK 실전 코드:

- `app_assistant_voice_agents.ipynb` (1.8MB) — 음성 어시스턴트
- `evaluate_agents.ipynb` (106KB) — 에이전트 평가
- `parallel_agents.ipynb` (59KB) — 병렬 에이전트
- `session_memory.ipynb` (63KB) — 세션 메모리(컨텍스트 엔지니어링)
- `multi-agent-portfolio-collaboration/` — 멀티 에이전트
- `sandboxed-code-migration/` — 샌드박스 코드 마이그레이션
- `voice_agents_audio/`, `voice_agents_knowledge/` — 음성 에이전트 변형들

`examples/evals/realtime_evals/` 는 AGENTS.md "Recent Learnings"의 4개 항목이 직접 다루는 영역 — 운영 노트가 코드와 직접 연결.

## 주요 인사이트

### 인사이트 1 — AGENTS.md 외부 채택 7단계 진화 완성

[[agent-stack-evolution]] 종합 분석에 새 단계 추가:

1. **[[anthropics-skills]]** — 표준 정의 (정적 SKILL.md 패키지)
2. **[[github-spec-kit]]** — Codex Skills 외부 도구 통합 (메소드론 어댑터)
3. **[[fastapi-fastapi]]** — 라이브러리 self-hosted SKILL.md (정적 컨벤션)
4. **[[astral-sh-uv]]** — `CLAUDE.md → AGENTS.md` 듀얼 지침서 (정적 single source)
5. **[[scikit-learn]]** — AI disclosure 강제 (정적 거버넌스)
6. **[[flutter-flutter]]** — vendor-neutral `.agents/skills/` (정적 자산)
7. **** — **살아있는 AGENTS.md** (Recent Learnings 운영 노트)

진화의 변곡점이 7번째에서 발생: 1~6번까지 모두 **정적 가이드**였다면, OpenAI는 **운영 중 발견을 즉시 AGENTS.md에 반영**한다. 이는 가이드가 한번 쓰면 변하지 않는 규칙이 아니라 살아있는 작업기억이라는 새로운 모드.

### 인사이트 2 — PLANS.md = 6번째 거버넌스 축

[[harness]] 개념의 5축 (autoresearch 최소 / spec-kit 표준화 / scikit-learn 컨트랙트 / flutter 자산 / anthropics-skills SKILL.md)에 6번째 축 추가:

| 거버넌스 모델 | 대상 | 시간 단위 | 산출물 |
|---|---|---|---|
| autoresearch (Karpathy) | 자율 메트릭 게임 | 분~시간 | 단일 파일 메트릭 |
| spec-kit (GitHub) | 다중 에이전트 표준화 | 시간~일 | Constitution + 슬래시 명령 |
| scikit-learn (커뮤니티) | API 컨트랙트 영구성 | 19년 | SLEP 문서 |
| flutter (Google) | 다중 도구 토큰 매트릭스 | 11년 | rules-1k/4k/10k/full |
| anthropics-skills (Anthropic) | 자동 호출 트리거 | 단발 | SKILL.md 정적 패키지 |
| **openai-cookbook PLANS.md** | **단일 LLM 7시간+ 작업** | **시간** | **자기완결 living document** |

PLANS.md의 차별 지표는 **시간 기반 검증** — 7시간 단일 프롬프트로 "지금까지 LLM이 완료할 수 없던 규모의 작업을 완료"가 가능한가? 의 직접적 답.

### 인사이트 3 — registry.yaml = 콘텐츠 거버넌스의 자동화

본 위키의 `wiki/index.md`도 같은 역할이지만, **수동 갱신**. registry.yaml은 정적 사이트 생성기에 의해 자동 검증되며, `check_notebooks.py`로 빌드 단계에서 등록 누락을 차단한다. 후속 차용 후보:

- 본 위키 `index.md`도 frontmatter에서 자동 생성 가능 (Obsidian Bases 또는 별도 스크립트)
- `python .github/scripts/check_notebooks.py` 패턴을 본 위키 `lint` 워크플로우에 차용 — 등록 누락 자동 검출

### 인사이트 4 — `what_makes_documentation_good.md` = 위키 스타일 가이드 후보

본 위키 `templates/source.md` 등은 추상적 섹션 제목(`## 핵심 내용`)을 사용한다. OpenAI 원칙 "Prefer titles with informative sentences over abstract nouns"를 적용하면, 모든 위키 페이지의 가독성을 두 배로 높일 수 있다. 하지만 31개 source 페이지 일괄 변환은 작업량이 크므로 후속 점검 후보.

### 인사이트 5 — gpt-oss + harmony format = OpenAI의 첫 오픈 가중치

`articles/openai-harmony.md` (29KB)는 OpenAI가 처음 공개한 오픈 가중치 모델 `gpt-oss`의 자체 대화 포맷 명세서. 5 roles + 3 channels 구조는 [[anthropics-claude-cookbooks]]의 Claude Conversation 포맷과 비교 분석 가치. 특히 `analysis` 채널의 안전성 표준 약화 ("do not adhere to the same safety standards as final messages")는 CoT 직접 노출 리스크를 명문화한 첫 사례.

### 인사이트 6 — 회사 BI에서 cookbook을 "검증 데이터셋"으로 활용

회사 BI에서 OpenAI API를 도입할 때 의사결정 절차:

1. 후보 기능(예: embeddings 기반 클러스터링) 결정
2. registry.yaml에서 같은 태그(`embeddings`, `clustering`) 검색 — 99 + 알파 사례
3. 가장 최근 / 가장 큰 ipynb를 raw 다운로드 후 회사 데이터로 재현
4. AGENTS.md "Recent Learnings"에서 같은 영역 함정 사전 확인
5. 도입 결정 시 `chatgpt-agents-sales-meeting-prep` 같은 enterprise 사례를 직접 차용

이는 [[scikit-learn]]의 `examples/` 디렉토리 / [[microsoft-data-science-for-beginners]]의 lesson 구조와 같은 활용 패턴. cookbook은 **검색 가능한 사례 데이터베이스**.

### 인사이트 7 — 한국어 fine-tuning 사례 직접 존재

`articles/gpt-oss/fine-tune-korean.ipynb` (45.9KB) — gpt-oss를 한국어 task에 fine-tune하는 노트북. 한국어 생성 BI 후속 후보가 있다면 직접 참조할 1차 자료.

## 관련 엔티티/개념

- [[openai]]: 본 저장소 운영 주체 (조직)
- [[openai-cookbook]]: 본 저장소 자체 (프로젝트)
- [[agent-skills]]: AGENTS.md 외부 채택 7단계 진화 7번째 사례
- [[harness]]: PLANS.md ExecPlan 6번째 거버넌스 축
- [[agent-patterns]]: examples/agents_sdk/ — Anthropic 5 패턴의 OpenAI 구현 비교 가능
- [[spec-driven-development]]: PLANS.md vs spec-kit Constitution 비교
- [[ml-ai]]: OpenAI = 가장 대표적 LLM 제공자, embeddings/fine-tuning/Agents SDK
- [[prompt-cache]]: examples/Prompt_Caching101.ipynb / 201.ipynb 직접 사례
- [[context-engineering]]: examples/agents_sdk/session_memory.ipynb (Sessions API)
- [[mcp]]: examples/mcp/ + tag mcp 8건
- [[agent-stack-evolution]]: 5축 종합 분석에 OpenAI 7번째 사례 추가 가치
- [[anthropics-claude-cookbooks]]: 직접적 비교 대상 (Anthropic vs OpenAI 양대 산맥)
- [[karpathy]]: OpenAI 공동 창립자, "Let's build GPT" 강의가 related_resources에 인용됨
- [[scikit-learn]]: AGENTS.md 5번째 사례 vs 본 사례 7번째
- [[astral-sh-uv]]: AGENTS.md "Recent Learnings"에 직접 언급(`uv run` virtualenv 함정)

## 인용할 만한 구절

> "Every ExecPlan must be fully self-contained. Self-contained means that in its current form it contains all knowledge and instructions needed for a novice to succeed."
> — `articles/codex_exec_plans.md`, NON-NEGOTIABLE 첫 번째 요건

> "Every ExecPlan is a living document. Contributors are required to revise it as progress is made..."
> — 같은 글, 두 번째 요건. PLANS.md = living document 패턴의 명문화.

> "Prefer titles with informative sentences over abstract nouns. For example, if you use a title like 'Results', a reader will need to hop into the following text to learn what the results actually are. In contrast, if you use the title 'Streaming reduced time to first token by 50%', it gives the reader the information immediately."
> — `articles/what_makes_documentation_good.md`. 본 위키 스타일 가이드 후속 점검의 직접 근거.

> "Avoid abbreviations. Write things out. The cost to experts is low and the benefit to beginners is high. Instead of IF, write instruction following. Instead of RAG, write retrieval-augmented generation (or my preferred term: the search-ask procedure)."
> — 같은 글. 본 위키의 약어(BDFL/PDEP/CMA) 처리 방침과 직접 연결.

> "These are considered priority 0 issues for this repo, in addition to the normal priority for possible issues."
> — `AGENTS.md` Review Guidelines. AGENTS.md가 코드 리뷰 우선순위까지 박는 단계로 진화.

## 메모

### 후속 탐구 후보

- (a) **synthesis: AGENTS.md 6단계 → 7단계 진화 종합** — [[agent-stack-evolution]]에 OpenAI "살아있는 운영 노트" 단계를 7번째로 박고, 정적 vs 살아있는 가이드의 트레이드오프 (Anthropic 표준화 정적 vs OpenAI 즉시 반영 살아있음) 비교.
- (b) **synthesis: 거버넌스 6축 비교 — Constitution / SKILL.md / SLEP / PDEP / AGENTS.md(살아있는) / PLANS.md(ExecPlan)** — 6 거버넌스의 시간 단위 / 산출물 / 검증 메커니즘 / 변경 비용 매트릭스.
- (c) **examples/Prompt_Caching101.ipynb + 201.ipynb 단독 수집** → [[prompt-cache]] 페이지 정량 데이터 보강 (현재 Anthropic 중심).
- (d) **examples/agents_sdk/session_memory.ipynb 단독 수집** → [[context-engineering]] 페이지에 OpenAI Sessions API 사례 추가.
- (e) **articles/openai-harmony.md 단독 수집** → 신규 개념 페이지 `harmony-format` 또는 기존 페이지 보강 (5 roles + 3 channels는 일반적 LLM 대화 모델로 추상화 가치).
- (f) **위키 자체 스타일 가이드 도입** — `templates/style-guide.md` 신설, OpenAI 8 원칙 + 본 위키 한국어 컨벤션 통합. 모든 source/concept 제목을 informative sentences로 점검.
- (g) **registry.yaml 패턴 차용** — 본 위키 `wiki/registry.yaml` 신설 후 `wiki/index.md` 자동 생성 PoC.
- (h) **회사 BI에 c2spf-cookbook 신설** — registry.yaml + authors.yaml + check_notebooks.py 패턴을 사내 BI 분석 노트북 모음에 차용. 컴투스플랫폼 게임 데이터 분석 case study database.
- (i) **articles/techniques_to_improve_reliability.md 단독 수집** → 신규 개념 `reliability-techniques` 또는 [[ml-ai]] 보강 (CoT / Self-consistency / Tree of Thoughts 등 13개 기법).
- (j) **gpt-oss 한국어 fine-tuning 노트북 (`articles/gpt-oss/fine-tune-korean.ipynb`) 단독 수집** → 한국어 BI 응용 ROI 평가.

### 회사 적용 가설

- **c2spf-analytics에 PLANS.md 도입 가설**: c2spf의 분기/연간 대형 분석 작업(예: 게임 출시 전후 코호트 분석)에 PLANS.md ExecPlan 패턴을 적용하면, 단일 분석가가 LLM 협업으로 7시간+ 작업을 수행 가능. NON-NEGOTIABLE 5 요건 중 "관찰 가능한 동작"은 BI 대시보드 또는 보고서 산출물로 매핑 자연스러움. 후속 PoC 후보.
- **AGENTS.md "Recent Learnings" 본 위키 차용**: 본 위키 자체에 `wiki/AGENTS.md` (또는 CLAUDE.md 보강)에 "Recent Learnings" 섹션을 신설하고, ingest에서 발견된 함정·솔루션을 누적. 누적 시 위키 운영 자체의 메타 메모.

### 미수집 / 추가 가치 영역

- `examples/` 디렉토리 본체 243개 ipynb (수십 MB) — 실 코드는 회사 BI 적용 시점에 cherry-pick.
- `examples/codex/` (Codex CLI 사례 다수) — 본 위키의 [[claude-code]] / [[github-spec-kit]] 비교 대상.
- `examples/mcp/` — [[mcp]] 페이지 보강 후보.
- `examples/evals/` — [[autonomous-research-loop]] OpenAI eval 인프라 비교.
- `images/` — 1.6MB 이미지 다수 (필요 시 회사 BI 슬라이드용).
- `.github/scripts/check_notebooks.py` — 검증 도구 (registry.yaml 차용 시 참조).

### 변경 추적 가치

- 2026-04-26 푸시 → 2026-04-27 수집. 케이던스 매우 높음 (몇 개월 단위 빅 콘텐츠 + 매주 소규모 PR). [[astral-sh-uv]]와 같은 수준의 변경 추적 가치 — 향후 lint 시 registry.yaml diff 자동 인지 후속 후보.
