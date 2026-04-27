---
title: "github/spec-kit — Spec-Driven Development 툴킷 (Specify CLI · 9개 슬래시 명령 · 30+ 에이전트 통합)"
type: source
source_type: article
source_url: "https://github.com/github/spec-kit"
raw_path: "raw/articles/github-spec-kit/"
author: "GitHub"
date_published: 2026-04-24
date_ingested: 2026-04-27
tags: [spec-kit, github, spec-driven-development, sdd, specify-cli, slash-command, agent-skills, claude-code, copilot, gemini, codex, cursor, constitution, prd, prompt-engineering, harness, agent-patterns]
related: [[github]], [[spec-kit]], [[spec-driven-development]], [[claude-code]], [[claude-agent-sdk]], [[agent-skills]], [[harness]], [[agent-patterns]], [[anthropic]], [[anthropics-skills]], [[anthropics-claude-cookbooks]], [[context-engineering]]
confidence: high
---

# github/spec-kit — Spec-Driven Development 툴킷 (Specify CLI · 9개 슬래시 명령 · 30+ 에이전트 통합)

## 한줄 요약

> GitHub이 직접 운영하는 **Spec-Driven Development(SDD) 메타-하네스** (★91,131 / fork 7,877, 2026-04-24 v0.8.1). "코드가 사양을 보좌하는" 전통 모델을 뒤집어 **사양이 실행 가능한 산출물 — 코드를 생성하는 원본 자산**이 되도록 강제. `specify` CLI 한 번 실행으로 30+ AI 코딩 에이전트(Claude Code, Copilot, Cursor, Gemini, Codex, Qwen, Windsurf, Goose 등)에 9개 슬래시 명령(`/speckit.constitution`·`/speckit.specify`·`/speckit.clarify`·`/speckit.plan`·`/speckit.tasks`·`/speckit.analyze`·`/speckit.checklist`·`/speckit.implement`·`/speckit.taskstoissues`)과 5개 템플릿(spec·plan·tasks·constitution·checklist)을 동일하게 설치. Codex CLI는 `--integration-options="--skills"`로 [[agent-skills]] 패키지 형태로 배포되어 표준 위에 표준이 얹힘.

## 메타

- **저장소**: [github/spec-kit](https://github.com/github/spec-kit)
- **라이선스**: MIT
- **언어**: Python (Specify CLI)
- **별/포크**: 91,131 / 7,877 (2026-04-27 기준)
- **최근 push**: 2026-04-24 (v0.8.1 릴리스)
- **공식 문서**: <https://github.github.io/spec-kit/>
- **Topic**: ai, copilot, development, engineering, prd, spec, spec-driven
- **설치**: `uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z`

## SDD 4단계 + 보조 5명령 (총 9개 슬래시 명령)

`templates/commands/*.md` 9개 파일이 모든 통합 에이전트에 공통으로 설치됨. 각 명령은 마크다운 본문 + frontmatter로 정의된 LLM 지침서.

### 핵심 4단계 (병합·축약 불가)

| 단계 | 슬래시 명령 | 입력 | 산출 | 핵심 강제 |
|------|------------|------|------|----------|
| 1. **헌법 수립** | `/speckit.constitution` | 자유 텍스트 (원칙 키워드) | `.specify/memory/constitution.md` | 9개 Article 골격 강제 |
| 2. **사양 작성** | `/speckit.specify` | 자유 텍스트 (무엇·왜) | `specs/[NNN-branch]/spec.md` + 새 git branch | "HOW 금지" + `[NEEDS CLARIFICATION]` 마커 강제 |
| 3. **계획 수립** | `/speckit.plan` | 자유 텍스트 (기술 스택) | `plan.md`, `research.md`, `data-model.md`, `contracts/`, `quickstart.md` | Pre-Implementation Gates (Simplicity·Anti-Abstraction·Integration-First) |
| 4. **태스크 분해** | `/speckit.tasks` | (자동) | `tasks.md` | `[P]` 병렬 마커, contract→test→implementation 순서 강제 |
| 5. **실행** | `/speckit.implement` | (자동) | 코드 + 테스트 | TDD Red 단계 검증 후만 구현 |

### 보조 4명령 (품질·운영)

| 명령 | 역할 |
|------|------|
| `/speckit.clarify` | spec 안의 `[NEEDS CLARIFICATION]` 마커를 사용자에게 질문해 해소 |
| `/speckit.analyze` | spec/plan/tasks 간 일관성 분석 — 누락·모순 검출 |
| `/speckit.checklist` | 도메인별 체크리스트 자동 생성 (보안·접근성·성능 등) |
| `/speckit.taskstoissues` | `tasks.md` → GitHub Issues 자동 변환 |

## 핵심 1 — "Power Inversion": 사양이 코드를 생성한다

`spec-driven.md`의 첫 단락이 SDD의 도덕적 명제를 박는다:

> "For decades, code has been king. Specifications served code—they were the scaffolding we built and then discarded once the 'real work' of coding began. (...) Spec-Driven Development (SDD) inverts this power structure. Specifications don't serve code—code serves specifications. The PRD isn't a guide for implementation; it's the source that generates implementation."

**달라진 것**: AI가 자연어 사양에서 직접 동작 코드를 만들 수 있게 되며 PRD ↔ Code 사이의 "**전통적인 간극**"이 메소드론 차원에서 닫혔다는 주장. 코드는 "특정 언어·프레임워크에서의 사양 표현"이 됨. 디버깅 = 사양 수정. 리팩토링 = 명료성 위한 재구조화. 새 기능 추가 = 사양 재방문 후 재생성.

**위키 관점에서 중요한 함의**: [[harness]]가 "에이전트의 작업장 전체 구조"라면, SDD는 그 작업장을 **사양 중심으로 강제 정렬한 메타-하네스**. spec-kit는 이 정렬을 9개 슬래시 명령으로 코드화한 기성품.

## 핵심 2 — 5개 템플릿의 "프롬프트 엔지니어링 정수"

`spec-driven.md`의 후반부가 명시적으로 박은 통찰: **템플릿이 곧 LLM 출력 제약 메커니즘**이다. 7가지 제약 메커니즘이 모든 템플릿에 박혀 있음.

### 템플릿 목록

| 템플릿 | 줄 수 | 핵심 강제 |
|--------|------|----------|
| `spec-template.md` | 128 | "WHAT/WHY only, NO HOW" + `[NEEDS CLARIFICATION]` 마커 의무 |
| `plan-template.md` | 104 | Phase -1 Gates (Simplicity·Anti-Abstraction·Integration-First) |
| `tasks-template.md` | 251 | TDD 강제, `[P]` 병렬 표시, file path 명시 |
| `constitution-template.md` | 50 | 9개 Article 골격 |
| `checklist-template.md` | 40 | 자체 검증 체크박스 패턴 |

### 7가지 제약 메커니즘 (`spec-driven.md` "Template-Driven Quality" 발췌)

1. **조기 구현 디테일 차단** — "✅ WHAT/WHY · ❌ tech stack/APIs/code structure" 라인을 spec 템플릿 첫머리에 박음
2. **불확실성 마커 의무** — `[NEEDS CLARIFICATION: 구체적 질문]` 패턴이 사용자 프롬프트에서 언급되지 않은 모든 항목에 강제 ("don't guess")
3. **체크리스트 = 단위 테스트** — 사양 자체가 "Requirement Completeness" 체크박스를 들고 다님 (`No [NEEDS CLARIFICATION] markers remain`, `Requirements are testable and unambiguous`)
4. **Constitutional Compliance Gates** — Phase -1 Gates가 Article 별로 체크: `Using ≤3 projects?` (Simplicity), `Using framework directly?` (Anti-Abstraction), `Contract tests written?` (Integration-First)
5. **계층적 디테일 관리** — `IMPORTANT: This implementation plan should remain high-level and readable. Any code samples (...) must be placed in the appropriate implementation-details/ file` — 본문이 코드 덤프되지 않게 강제
6. **테스트 우선 강제** — `File Creation Order: 1. contracts/ → 2. test files → 3. source files`
7. **추측 기능 차단** — `No speculative or "might need" features. All phases have clear prerequisites and deliverables`

이 7개가 누적되면 LLM이 "창의적 작가"에서 "**규율 있는 사양 엔지니어**"로 전환된다는 주장. 위키 관점: Microsoft for-beginners의 "단일 운영체계" 사상과 동형이지만, 여기는 **메소드론 자체가 결과물**.

## 핵심 3 — 9 Articles Constitution: 불변 아키텍처 DNA

`spec-driven.md` "Constitutional Foundation"이 박은 9개 Article. `.specify/memory/constitution.md`에 보관되며 모든 plan generation에서 읽힘.

| Article | 강제 사항 |
|---------|----------|
| **I. Library-First Principle** | 모든 기능은 standalone 라이브러리로 시작 (애플리케이션 코드 직접 구현 금지) |
| **II. CLI Interface Mandate** | 모든 라이브러리는 CLI 노출 (stdin/args/files 입력, stdout 출력, JSON 지원) |
| **III. Test-First Imperative** | **NON-NEGOTIABLE** — Red 단계 확인 전 어떤 구현 코드도 작성 금지 |
| **VII. Simplicity** | 초기 구현은 ≤3 프로젝트 |
| **VIII. Anti-Abstraction** | 프레임워크 직접 사용 (래핑 금지), 단일 모델 표현 |
| **IX. Integration-First Testing** | 실제 DB·서비스 사용, mock 회피, contract test 의무 |

(IV·V·VI는 조직 정책에 따라 바뀌는 슬롯 — `constitution-template.md`가 골격만 제공)

**Constitutional Evolution**: 변경 시 (a) rationale 명시, (b) 유지보수자 승인, (c) 후방 호환 평가가 의무 (`Section 4.2: Amendment Process`).

## 핵심 4 — 30+ 에이전트 통합 아키텍처

`AGENTS.md`가 박은 핵심: 각 에이전트는 `src/specify_cli/integrations/<key>/` 자기-내장 서브패키지. 5가지 base class 중 하나를 상속.

| Base Class | 출력 형식 | 사례 |
|-----------|----------|------|
| `MarkdownIntegration` | `.md` 슬래시 명령 | Claude Code, Cursor, Windsurf |
| `TomlIntegration` | `.toml` | Gemini CLI |
| `YamlIntegration` | `.yaml` recipe | Goose |
| **`SkillsIntegration`** | `speckit-<name>/SKILL.md` 패키지 | **Codex CLI (`--integration-options="--skills"`)** |
| `IntegrationBase` (직접) | 커스텀 출력 | Copilot (companion files) |

### Codex CLI = SKILL.md 패키지 모드 (위키 핵심)

Codex CLI 통합은 다른 모든 에이전트와 다르게 [[agent-skills]] 표준을 따른다:

```bash
specify init . --integration codex --integration-options="--skills"
```

이 한 줄이 `.codex/skills/speckit-specify/SKILL.md`, `.codex/skills/speckit-plan/SKILL.md`, … 9개 패키지를 생성. 각 패키지는 [[anthropics-skills]]가 정의한 frontmatter + body + (optional) scripts·references·assets 구조를 그대로 따름.

**위키적 의미**: spec-kit은 [[agent-skills]] 표준의 **첫 대규모 외부 채택 사례**. anthropics/skills가 "표준 + 카탈로그", anthropics/claude-cookbooks가 "실습 채널"이라면 spec-kit는 "**표준의 외부 적용 사례**".

### 슬래시 vs Skills 모드 차이

| 모드 | 호출 | 자동 호출 | 컨텍스트 |
|------|------|----------|---------|
| 슬래시 명령 (대부분) | `/speckit.specify ...` | ❌ | 호출 시 본문 전체 로드 |
| Skills 모드 (Codex) | `$speckit-specify ...` 또는 자연어 자동 | ✅ | progressive disclosure |

## 핵심 5 — 4층 Override Stack

`README.md`의 "Resolution Order" 섹션이 박은 패키지 우선순위:

| 우선순위 | 레이어 | 경로 |
|---------|--------|------|
| ⬆ 1 | **Project-Local Overrides** | `.specify/templates/overrides/` |
| 2 | **Presets** — 작동 *방식* 커스터마이즈 | `.specify/presets/templates/` |
| 3 | **Extensions** — 새 *능력* 추가 | `.specify/extensions/templates/` |
| ⬇ 4 | **Spec Kit Core** — 기본 SDD 명령·템플릿 | `.specify/templates/` |

- **Templates**는 런타임 해결 (top-down 첫 매치)
- **Extension/Preset commands**는 install-time 해결 (`.claude/commands/`에 직접 쓰임)
- **Extensions ≠ Presets**: Extensions는 "새 명령·워크플로우 추가" (Jira 통합, V-Model traceability), Presets는 "기존 출력 형식 변경" (규제 산업 spec 형식, 도메인 용어, 다국어)

`extensions/catalog.community.json`에 40+ 커뮤니티 확장 등재. 카테고리: `docs`, `code`, `process`, `integration`, `visibility`. Effect: `Read-only`, `Read+Write`.

## 핵심 6 — `specs/[NNN-branch]/` 디렉토리 구조

`/speckit.specify`가 자동 생성하는 표준 디렉토리:

```
specs/003-chat-system/
├── spec.md             # 사양 (WHAT/WHY)
├── plan.md             # 구현 계획 (HOW의 high-level)
├── research.md         # 기술 조사 (라이브러리 비교, 벤치마크)
├── data-model.md       # 데이터 모델
├── contracts/          # API/이벤트 계약 (test 먼저)
├── quickstart.md       # 검증 시나리오
└── tasks.md            # 실행 가능 태스크 리스트 (`[P]` 병렬 마커 포함)
```

자동 생성되는 것: 브랜치명(`003-chat-system`), 번호(`003`은 다음 사용 가능 번호 자동 스캔, 999 넘으면 4자리 확장).

이 폴더 구조 자체가 "**사양 중심 모노레포**"의 단위. PR 1 = feature 1 = 한 번호 디렉토리.

## 주요 인사이트

### 1. spec-kit = 메타-하네스 (하네스의 하네스)

[[harness]]가 "에이전트의 작업장 전체 구조"라면, spec-kit는 **그 작업장을 SDD 메소드론으로 강제 정렬한 메타-하네스**. 4층 레이어 매핑:

| 하네스 레이어 | spec-kit에서의 모양 |
|--------------|-------------------|
| 지식 | `constitution.md` + `spec.md` + `plan.md` + 5 템플릿의 frontmatter 지침 |
| 도구 | bash, git, GitHub CLI, MCP (Extensions로 추가 통합) |
| 패키지 | 9개 슬래시 명령 (또는 Codex의 SKILL.md 9개 패키지) |
| 통제 | Phase -1 Gates, `[NEEDS CLARIFICATION]` 마커, Constitutional Compliance, TDD Red 단계 강제 |

[[autoresearch]] (Karpathy, 7KB program.md)가 "최소 하네스"의 극단이라면, spec-kit는 "**완전 표준화 하네스**"의 반대 극단. 양극이 같은 페이지에 박히면 [[harness]] 페이지의 스펙트럼이 완성됨.

### 2. spec-kit이 Building Effective Agents 5 패턴을 어떻게 사용하나

[[agent-patterns]]의 5 패턴이 SDD 워크플로우에서 명시적 사용:

| spec-kit 단계 | 사용 패턴 | 이유 |
|--------------|----------|------|
| `/speckit.constitution` → `/speckit.specify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement` | **Prompt Chaining** (Basic) | 정적 5단계 분해, 각 단계 출력이 다음 단계 입력 |
| `/speckit.clarify` (사용자에게 질문 → 사양 수정) | **Evaluator-Optimizer** (Advanced) | LLM이 spec 평가 → 마커 발견 → 사용자 = evaluator |
| `/speckit.analyze` (spec·plan·tasks 일관성 검증) | **Evaluator-Optimizer** | 다른 단계 결과를 evaluator가 교차 검증 |
| `tasks.md`의 `[P]` 병렬 그룹 실행 | **Parallelization** (Sectioning) | 독립 태스크를 동시 처리 |
| (커뮤니티) "Agent Assign" 확장 — 태스크별 전문 에이전트 라우팅 | **Routing** | 태스크 특성에 따라 전용 에이전트 선택 |
| 복잡 spec에서 plan을 동적으로 결정 | **Orchestrator-Workers** | plan 자체가 동적 분해 |

즉 spec-kit는 5 패턴을 **메소드론으로 사전 합성한 결과물**. 사용자가 직접 패턴 선택할 필요 없이 단계만 따라가면 됨.

### 3. Codex Skills 모드 = [[anthropics-skills]] 표준의 첫 외부 채택

[[anthropics-skills]] 페이지의 "Plugin namespace" 섹션이 예측한 것: **표준이 외부 채택을 받을 때 마켓플레이스가 형성된다**. spec-kit의 Codex 통합이 그 첫 사례. SKILL.md frontmatter (`name`, `description`, `when_to_use`, `allowed-tools`)와 progressive disclosure (SKILL.md body + scripts/ + references/) 모두 그대로 사용.

이는 "[[agent-skills]] = Anthropic-only" 가설을 명확히 깸. agentskills.io 표준이 GitHub 공식 도구의 통합 형식 중 하나가 됨.

### 4. Microsoft·Anthropic·Karpathy·GitHub 4축 비교

[[agent-stack-evolution]]가 박은 3축 비교에 spec-kit를 추가하면:

| 진영 | 핵심 명제 | 결과물 |
|------|---------|--------|
| Microsoft for-beginners | "Cloud Advocates 단일 운영체계로 모든 학습 콘텐츠를 정렬" | 5개 커리큘럼 + co-op-translator |
| Anthropic | "표준은 분리하고(agentskills.io) 구현은 cookbook과 marketplace로 푼다" | anthropics/skills + anthropics/claude-cookbooks |
| Karpathy | "최소 하네스(program.md 한 장)로 자율 진화시킨다" | autoresearch + nanochat |
| **GitHub spec-kit** | "**메소드론 자체를 도구로 만들어 30+ 에이전트에 동일 설치**" | spec-kit (CLI + 9 명령 + 5 템플릿) |

GitHub의 차별점: **메소드론 표준화 + 다중 에이전트 호환**. 이는 GitHub이 "다양한 AI 코딩 도구의 신경전" 위에서 메타-층을 잡으려는 시도로 읽힘 (GitHub Copilot이 자기 도구지만 30개 다른 도구도 동등 지원).

### 5. 위키 운영 직접 차용 후보 — `templates/commands/*.md` 패턴

이 위키가 현재 `templates/`에 entity·concept·source·synthesis·lesson 5종을 가지고 있다. spec-kit의 `templates/commands/*.md` 9종과 비교하면:

- **공통**: 마크다운 + frontmatter, "출력 형식 강제"
- **차이**: spec-kit는 "**LLM 워크플로우 지침서**" (executive prompts), 우리 위키는 "**사람용 작성 가이드**"

후속 탐구: 위키에 `templates/commands/` 디렉토리 신설, `/wiki-ingest`, `/wiki-lint`, `/wiki-synthesize` 같은 슬래시 명령을 spec-kit 스타일로 LLM 지침서화. 현재 CLAUDE.md의 워크플로우 섹션을 그대로 옮기면 될 듯.

### 6. "Vibe coding" 단어 명시 거부

README의 첫 줄이 도발적: "**An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch.**"

GitHub이 "vibe coding"을 명시적 안티-패턴으로 박음. SDD가 그것의 답. 위키 관점: 석근의 "바이브 코딩" 선호 스택과 직접 충돌하는 명제 — 후속 탐구로 "어떤 작업에 SDD가 ROI가 있고 어떤 작업에 vibe coding이 더 빠른가" 정리 필요.

## 위키 갱신 포인트

| 페이지 | 갱신 내용 |
|--------|----------|
| 신규 [[github]] | organization 페이지 — Microsoft·Anthropic과 균형 |
| 신규 [[spec-kit]] | tool/project 페이지 — Specify CLI 자체의 자리 |
| 신규 [[spec-driven-development]] | concept 페이지 — SDD 메소드론 |
| [[claude-code]] | spec-kit이 `.claude/commands/`에 9개 명령 자동 설치 — 통합 사례 추가 |
| [[agent-skills]] | Codex Skills 모드를 "표준의 첫 외부 채택" 사례로 추가, [[spec-kit]] 링크 |
| [[harness]] | spec-kit를 "메타-하네스"의 표본으로 추가 (autoresearch 최소 하네스의 반대 극단) |
| [[agent-patterns]] | spec-kit 단계별 5 패턴 매핑 표 추가 |

## 석근 직결 활용 시나리오

1. **위키 자체에 spec-kit 적용 (메타)**: `templates/commands/`에 `/wiki-ingest`, `/wiki-lint`, `/wiki-synthesize`, `/wiki-query` 4개 명령 추가. 현재 CLAUDE.md 워크플로우의 코드화. spec-kit의 `specify init . --integration claude --here`로 스캐폴드 가져온 후 위키 도메인에 맞게 override.
2. **회사 BI에 SDD 시범 도입**: 새 지표 정의 / 새 대시보드 작성 같은 0→1 작업에 `/speckit.constitution` (BI 원칙) → `/speckit.specify` (지표 정의 PRD) → `/speckit.plan` (BigQuery·차트·캐시 결정) → `/speckit.tasks` 실험. 실패해도 "BI 작업에 SDD가 적합한가"의 데이터 확보.
3. **개인 비서 AI 시드**: `01_The_chief_of_staff_agent.ipynb` ([[anthropics-claude-cookbooks]]) + spec-kit 합성. Constitution = 비서의 운영 원칙 (응답 톤·사생활 경계·자동 실행 한계), `specs/`에 사용 시나리오별 spec.md 누적. SDD는 단발 명령 모델보다 비서의 long-term consistency에 유리.
4. **`/speckit.constitution`만 차용**: 9 Articles 골격을 회사 프로젝트에 도입. Test-First (Article III) + Library-First (Article I) + Simplicity (Article VII)는 게임 데이터 BI에 직접 ROI.
5. **포트폴리오 페이지 시드 — SDD로 본인 이력 작성**: `/speckit.specify`에 "5년 경력 백엔드/풀스택 BI 개발자 포트폴리오"를 입력하면 `[NEEDS CLARIFICATION]` 마커가 빠진 정보를 잡아낸다. 이력서 작성의 메타-체크리스트.

## 인용할 만한 구절

> "Spec-Driven Development inverts this power structure. Specifications don't serve code—code serves specifications. The Product Requirements Document (PRD) isn't a guide for implementation; it's the source that generates implementation."
> — `spec-driven.md`, "The Power Inversion"

> "The templates transform the LLM from a creative writer into a disciplined specification engineer, channeling its capabilities toward producing consistently high-quality, executable specifications that truly drive development."
> — `spec-driven.md`, "Template-Driven Quality"

> "Article III: Test-First Imperative — This is NON-NEGOTIABLE: All implementation MUST follow strict Test-Driven Development. No implementation code shall be written before: 1. Unit tests are written 2. Tests are validated and approved by the user 3. Tests are confirmed to FAIL (Red phase)"
> — `spec-driven.md`, "The Nine Articles of Development"

> "An open source toolkit that allows you to focus on product scenarios and predictable outcomes instead of vibe coding every piece from scratch."
> — `README.md`, 표제 직하

> "Most agents expose spec-kit as `/speckit.*` slash commands; Codex CLI in skills mode uses `$speckit-*` instead."
> — `README.md`, "Establish project principles"

## 메모

- raw 보관 32개 파일: 루트 메타 6종(README·spec-driven·AGENTS·CHANGELOG·DEVELOPMENT·CONTRIBUTING) + docs 5종(index·quickstart·installation·upgrade·local-development) + 5 템플릿(spec/plan/tasks/constitution/checklist) + 9 슬래시 명령 정의(analyze·checklist·clarify·constitution·implement·plan·specify·tasks·taskstoissues) + workflows 3종(README·ARCHITECTURE·speckit-workflow.yml) + presets 2종(README·ARCHITECTURE) + integrations 2종(README·catalog.json). Specify CLI Python 소스(`src/specify_cli/`)는 보관 제외 (메소드론은 이미 마크다운에 다 있음).
- v0.8.1 릴리스가 3일 전(2026-04-24). 활발한 변경 — CHANGELOG.md 1,368줄.
- 후속 탐구: (a) `templates/commands/*.md` 9개를 1:1로 분석해 LLM 지침서 작성 패턴 추출 → 위키 자체 `/wiki-*` 명령 작성 reference, (b) `extensions/catalog.community.json` 40+ 확장 중 BI/문서화 관련만 별도 정리, (c) `specify init` Python CLI 코드 한 번 읽어 base class 5종 동작 차이 확인.
- Codex Skills 모드의 `$speckit-*` prefix 호출 표기는 [[agent-skills]] 페이지에 명시 안 된 새 운영 패턴. agent-skills.md 갱신 시 반영.
