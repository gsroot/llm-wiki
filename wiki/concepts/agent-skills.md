---
title: "Agent Skills (SKILL.md 패키지)"
type: concept
category: ai
tags: [agent-skills, skills, claude-code, anthropic, progressive-disclosure, agentskills.io, skill-creator, harness, 패키지레이어, claude-cookbooks, custom-skills, spec-kit, codex-skills, multi-agent-adoption, library-self-hosted-skill, fastapi, vendor-neutral, dart-skills-lint, flutter, token-budget-tiers, openai, openai-cookbook, openai-agents-python, agents-md-living, recent-learnings, exec-plans, 9-sop-skills, skill-chaining, agents-md-claude-md-mirror, pydantic-ai, prometheus, grafana, sentry, anti-fragmentation, hierarchical-agents-md, pr-pattern-agents-md, nextjs, vercel, skill-indexing, LLM-pr-marker, open-code, code-distribution, 18회차, 19회차, 22회차]
related:
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[anthropic]]"
  - "[[mcp]]"
  - "[[harness]]"
  - "[[context-engineering]]"
  - "[[token-economy]]"
  - "[[llm-wiki-pattern]]"
  - "[[autonomous-research-loop]]"
  - "[[spec-kit]]"
  - "[[spec-driven-development]]"
  - "[[github]]"
  - "[[fastapi]]"
  - "[[tiangolo]]"
  - "[[flutter]]"
  - "[[google]]"
  - "[[openai]]"
  - "[[openai-cookbook]]"
  - "[[openai-agents-python]]"
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[deepagents]]"
  - "[[fastmcp]]"
  - "[[pydantic-ai]]"
  - "[[prometheus]]"
  - "[[grafana]]"
  - "[[sentry]]"
  - "[[observability]]"
  - "[[nextjs]]"
  - "[[shadcn-ui]]"
  - "[[vercel]]"
source_count: 16
observed_source_refs: 47
inbound_count: 152
created: 2026-04-27
updated: 2026-04-29
---

# Agent Skills (SKILL.md 패키지)

## 정의

**Agent Skill** = `SKILL.md` 1개 파일(YAML frontmatter + 마크다운 지침서)을 중심으로 옵션 자원(`scripts/`, `references/`, `assets/`)을 같이 묶어 LLM 에이전트가 동적으로 로드하는 **재사용 가능한 작업 패키지**.

핵심은 **자동 호출**(LLM이 description을 보고 스스로 트리거 결정), **progressive disclosure**(필요한 만큼만 컨텍스트에 로드), **재사용성**(여러 프로젝트·세션·환경에서 동일한 작동).

[agentskills.io](https://agentskills.io) 오픈 표준이고, [[claude-code]]·Claude.ai·Claude API가 모두 이 표준을 따른다. Anthropic의 Custom Commands는 2026년에 Skills로 **공식 통합**됨 (`.claude/commands/*.md`는 호환성 유지, **Skills가 권장**).

## 왜 중요한가

석근 입장에서:

1. **위키 조회·BI 작업·개인 비서**의 모든 반복 워크플로우를 한 형식(`SKILL.md`)으로 묶을 수 있음 → 단일 멘탈 모델
2. **자동 호출**이 RAG의 본질에 가까움 — 사용자가 "관련 위키 있어?"라고 묻기 전에 LLM이 알아서 위키를 봄 ([[llm-wiki-pattern]] 발전형)
3. **progressive disclosure**가 컨텍스트 윈도우 압박을 구조적으로 푸는 첫 표준 — 17개 스킬 메타가 26K 토큰만 점유
4. [[harness]]의 4층 레이어 중 "패키지 레이어"의 단일 표준 구현

이 개념은 [[harness]], [[mcp]], [[claude-code]]와 함께 위키의 숨은 5번째 축을 이룬다. 네 노드를 한 번에 비교해야 할 때는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]를 진입점으로 쓴다.

## 핵심 내용

### 3-Level Progressive Disclosure

스킬 콘텐츠는 3개 레벨로 분리되어 LLM이 필요한 만큼만 로드:

| 레벨 | 내용 | 로드 시점 | 예산 가이드 |
|------|------|----------|-------------|
| 1. **Metadata** | `name` + `description` (frontmatter) | **항상** 컨텍스트 | ~100 단어, description 1,536자 cap |
| 2. **SKILL.md body** | 마크다운 본문 (워크플로우·예시·휴리스틱) | 트리거 시 | <500 lines 권장 |
| 3. **Bundled resources** | `scripts/`, `references/`, `assets/` | LLM 판단으로 필요 시만 | 무제한 (scripts는 호출만 하면 컨텍스트 0) |

이게 [[token-economy]] + [[context-engineering]]을 구조적으로 결합한 패턴. 위키의 "index → source → raw" 3단 구조와 동형.

### Anatomy of a Skill

```
skill-name/
├── SKILL.md (필수)
│   ├── --- YAML frontmatter ---
│   ├── name: skill-name
│   ├── description: 무엇을 하는지 + 언제 쓰는지 (자동 호출 판정 기준)
│   ├── ---
│   └── # 본문 (Markdown)
│
└── (선택)
    ├── scripts/    # 결정론적 작업 — 컨텍스트 안 들어감, 호출만
    ├── references/ # 도메인별 상세 — LLM이 필요할 때만 Read
    └── assets/     # 출력 자원 (템플릿, 폰트, 이미지)
```

### 14개 Frontmatter 필드 (요약)

| 필드 | 필수 | 핵심 역할 |
|------|------|----------|
| `name` | No (디렉토리명) | 소문자·하이픈, 64자 |
| `description` | **권장** | 자동 호출 판정 기준. 1,536자 cap, **front-load 키워드** |
| `when_to_use` | No | description 보강 |
| `argument-hint` | No | 자동완성 힌트 |
| `disable-model-invocation` | No | true면 자동 호출 차단 |
| `user-invocable` | No | false면 `/` 메뉴에서 숨김 (Claude만 사용) |
| `allowed-tools` | No | 권한 요청 없이 쓸 수 있는 툴 |
| `model` / `effort` | No | 이 스킬 활성 시 모델·노력 수준 |
| `context: fork` | No | 서브에이전트 격리 실행 |
| `agent` | No | fork 시 사용할 에이전트 (`Explore`, `Plan`, ...) |
| `paths` | No | 자동 호출 제한 glob 패턴 |
| `hooks` | No | 수명주기 hook |
| `shell` | No | 동적 injection 셸 |

### 호출 제어 매트릭스

| 설정 | 사용자 호출 | Claude 자동 호출 | 컨텍스트 로드 |
|-----|-----------|----------------|-------------|
| 기본값 | ✅ | ✅ | description 상시, 본문은 호출 시 |
| `disable-model-invocation: true` | ✅ | ❌ | 호출 시에만 전부 |
| `user-invocable: false` | ❌ | ✅ | description 상시, 본문은 호출 시 |

### Skill 저장 위치 (우선순위)

```
Enterprise > Personal (~/.claude/skills/) > Project (.claude/skills/) > Plugin
```

- **Enterprise**: 조직 강제 (`managed`)
- **Personal**: 개인 도구의 기본 선택 — 모든 프로젝트에서 자동 사용
- **Project**: `.claude/skills/` — 팀 공유 시 Git 커밋
- **Plugin**: `plugin-name:skill-name` 네임스페이스로 충돌 방지. [[anthropics-skills]] 마켓플레이스가 표준 사례

### Skill content lifecycle

- 호출 시 SKILL.md 본문이 conversation에 **한 메시지로** 삽입, 세션 끝까지 남음
- 후속 턴에 다시 읽지 **않음** → "언젠가 지켜야 할 규칙"을 표준 지침 스타일로 써야 함 (일회성 단계 X)
- Auto-compaction 시 가장 최근 호출된 skill들만 최대 25,000 토큰 예산 안에서 복원
- 큰 스킬 또는 다수 호출 후엔 오래된 것 탈락 가능 → re-invoke로 복원

## description 작성 원칙 (Anthropic skill-creator 기준)

핵심: **"undertrigger 경향" 보정을 위해 의도적으로 "pushy"하게 쓴다**.

### 4가지 룰

1. **무엇을 + 언제 둘 다**: "what" 만 있는 description은 자동 호출 안 됨
2. **Pushy하게**: "use this skill whenever the user mentions X, Y, or Z, even if they don't explicitly ask"
3. **Front-load 키워드**: 1,536자 capped — 앞에 핵심어 배치
4. **near-miss 케이스 고려**: 비슷한 다른 스킬이 있을 때 어떤 차별 키워드로 자기를 호출시킬지 명시

### Bad → Good

| Bad | Good |
|-----|------|
| "Format this data" | "ok so my boss just sent me this xlsx file (its in my downloads, called something like 'Q4 sales final FINAL v2.xlsx') and she wants me to add a column that shows the profit margin as a percentage. The revenue is in column C and costs are in column D" |
| "How to build a fast dashboard" | "How to build a simple fast dashboard. Use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any kind of company data, even if they don't explicitly ask for a 'dashboard.'" |

### description 최적화 자동화 루프

`skill-creator`의 별도 skill에 정의된 자동 최적화:

1. **20개 trigger 검증 쿼리** 작성 (should-trigger 8-10 + should-not-trigger 8-10)
2. **60% train / 40% test split**
3. 각 쿼리 3회 실행해 trigger rate 측정
4. Claude가 description 개선안 제안 → 재검증
5. 최대 5 iteration, **test score**로 best 선정 (overfit 방지)

`run_loop.py` 스크립트 1줄로 실행. 위키 SKILL.md description 튜닝에 그대로 차용 가능.

## Skill vs Slash Command

[[slash-commands-vs-agent-skills]]에서 자세히 다뤘지만 핵심만:

| 기능 | `.claude/commands/*.md` | `.claude/skills/*/SKILL.md` |
|------|------------------------|----------------------------|
| `/name` 호출 | ✅ | ✅ |
| **자동 호출** | ❌ | ✅ |
| **supporting files** | ❌ | ✅ |
| **`context: fork`** | ❌ | ✅ |
| **`paths`** | ❌ | ✅ |
| Frontmatter 호환 | ✅ | ✅ |

Anthropic 공식 권장: **모든 신규는 Skills로 시작**. Custom Commands는 호환성 유지만.

## SKILL.md 패턴 4가지 (anthropics/skills 사례 기준)

### 1. 풍부한 메타-스킬 (skill-creator, 33KB)

자기 자신을 만드는 데 필요한 모든 것을 본문에 — 다만 reference·agents·assets·scripts·eval-viewer로 분리해 본문은 핵심 워크플로우만.

### 2. Multi-domain reference 분리 (mcp-builder, 9KB)

본문은 4단계 워크플로우만, 도메인별 상세는 `references/python_mcp_server.md`, `references/node_mcp_server.md`, `references/evaluation.md`로 분리. **LLM이 필요한 변종만 Read**.

### 3. 짧고 강한 단일 SKILL.md (frontend-design, 4.4KB)

본문이 짧으면 supporting files 없이도 강력. 휴리스틱·금기·예시만 응축. ALWAYS/NEVER 대신 **이유 설명**으로 도덕적 권위 확보.

### 4. 스크립트 블랙박스 (webapp-testing, 3.9KB)

`scripts/with_server.py`를 **읽지 말고 호출만 하라**고 명시. 도구가 컨텍스트 안 들어와 진짜 progressive disclosure 실현. [[token-economy]] 정수.

## 실전 적용 (석근 시나리오)

### A. 위키 조회 SKILL 강화

현재 `~/.claude/skills/wiki/SKILL.md`가 운영 중 ([[slash-commands-vs-agent-skills]] 참조). 보강 후보:

- description 재작성 (pushy 원칙) + 20개 trigger 검증 쿼리로 확인
- `references/query-patterns.md` 분리 (질의 유형별 접근법)
- `scripts/wiki-stats.sh` 추가 (index 통계, recent 5개 등 동적 injection)
- `paths: ["**/*.md"]`로 자동 호출 조건 제한 (코드 작업 중에는 방해 X)

### B. BI 쿼리 패턴 SKILL

컴투스플랫폼 BI에서 반복되는 쿼리 패턴(KPI 조회, 코호트 분석, retention)을 `bi-query-patterns/SKILL.md`로 묶기. `references/`에 BigQuery 슬롯 최적화·MMP 데이터 조인 패턴.

### C. 개인 비서 AI 핵심 SKILL.md

[[autonomous-research-loop]] 응용 — `personal-assistant/SKILL.md`를 자율 진화시키는 루프. 메트릭은 LLM-as-judge 만족도. skill-creator의 5단계 루프를 그대로 차용.

### D. 위키 자체에 templates/skill.md 추가

기존 entity/concept/source/synthesis 4종 템플릿 + skill 1종 추가 검토. SKILL.md를 위키 자산으로 관리하면 회사 맥북·집 윈도우 양쪽에서 sync 가능.

## 안티패턴

| 패턴 | 문제 | 해결 |
|------|------|------|
| description이 "what"만 있음 | 자동 호출 안 됨 | "when" 추가, pushy |
| SKILL.md 500줄 초과, hierarchy 없음 | 매 호출마다 거대 본문 로드 | references로 분리 |
| 같은 helper script를 매번 LLM이 새로 작성 | 토큰 낭비, 비결정성 | scripts/에 번들 |
| ALWAYS/NEVER 대문자 도배 | 설명 부재로 LLM이 이유 모름 → 일반화 실패 | "왜 중요한지" 한 줄 추가 |
| disable-model-invocation을 모든 스킬에 적용 | 자동 호출 = Skills 핵심 가치 폐기 | 사이드이펙트 있는 스킬에만 적용 |

## 관련 개념

- [[claude-code]]: Skills 기능 제공 주 제품 (CLI/IDE/Web/iOS)
- [[mcp]]: 도구 통합 프로토콜 — Skills의 `allowed-tools` 정의 시 MCP 서버 도구 호출 가능
- [[harness]]: Skills = "패키지 레이어"의 단일 표준 구현. 4층 레이어 분류로 매핑
- [[context-engineering]]: progressive disclosure가 이 개념의 모범
- [[token-economy]]: 메타 100w 상시 + 본문 lazy + scripts 호출-만 = 토큰 경제학 적용
- [[llm-wiki-pattern]]: 위키 조회를 SKILL.md로 패키징하는 게 "RAG처럼 활용하기"의 본질
- [[autonomous-research-loop]]: skill-creator의 자기 진화 루프 = program.md 자율 진화의 변종

## 출처

- [[anthropics-skills]] — Anthropic 공식 Agent Skills 레퍼런스 (마켓플레이스, skill-creator, mcp-builder 등 17개 스킬)
- [[slash-commands-vs-agent-skills]] — Anthropic 공식 문서 기반 Custom Commands 통합 경위·비교 분석
- [[anthropics-claude-cookbooks]] — `skills/` 디렉토리 3 노트북(introduction → financial → custom development) + `custom_skills/` 사례 3종(analyzing-financial-statements, applying-brand-guidelines, creating-financial-models). progressive disclosure 설명을 BI 도메인 사례로 완성하는 reference
- [[github-spec-kit]] — **agent-skills 표준의 첫 외부 채택 사례**. [[spec-kit]]의 Codex CLI 통합(`SkillsIntegration` base class)이 `--integration-options="--skills"` 플래그로 9개 슬래시 명령을 `.codex/skills/speckit-*/SKILL.md` 패키지 형태로 배포. SKILL.md frontmatter (`name`, `description`, `when_to_use`, `allowed-tools`)와 progressive disclosure (body + scripts/ + references/) 구조를 그대로 사용 → "agent-skills = Anthropic-only" 가설 명확히 깸. [[github]]가 [[anthropics-skills]] 표준을 GitHub 공식 도구의 통합 형식 중 하나로 채택
- [[fastapi-fastapi]] — **agent-skills 표준의 첫 라이브러리 self-hosted 사례**. [[fastapi]] v0.136.1이 `fastapi/.agents/skills/fastapi/SKILL.md` (10.4KB) + `references/{dependencies,streaming,other-tools}.md`를 라이브러리 디렉토리 안에 번들링. frontmatter `name: fastapi` + `description: FastAPI best practices and conventions...`로 LLM이 "FastAPI 코드 작성 시" 자동 호출되도록 유도. 본문은 `Annotated` 강제·`def` 디폴트·`ORJSONResponse` deprecation·라우터 prefix 위치·Asyncer/SQLModel/HTTPX 추천 등 코딩 컨벤션을 명시. → 외부 채택 3단계 진화 완성: ① anthropics/skills(표준 정의) → ② github/spec-kit(외부 도구 통합) → ③ **fastapi/fastapi(라이브러리 self-hosted, 자기 코드 사용법을 자기가 출하)**. README는 사람용·SKILL.md는 에이전트용이라는 OSS 분업이 메인스트림에서 명시화됨
- [[openai-openai-cookbook]] — **agent-skills 외부 채택 7단계 진화의 7번째 단계 — 첫 "살아있는 운영 노트" 사례**. [[openai]]가 4년차 cookbook(★73K, 289 콘텐츠)의 `AGENTS.md`(5.5KB)에 표준 7개 섹션을 모두 갖추되, **`Recent Learnings`** 섹션을 두어 운영 중 발견된 함정·솔루션을 누적한다. 6개 항목 형식: "현상 → 대응 → 이유" (예: "`uv run` can inherit the wrong virtualenv → Clear `VIRTUAL_ENV` → Avoids misleading mismatch warnings"). 추가로 `articles/codex_exec_plans.md`에서 정의된 **PLANS.md / ExecPlans** 패턴은 단일 LLM 작업 7시간+를 가능케 하는 "자기완결 living document" 거버넌스 — `AGENTS.md`에 `When writing complex features, use an ExecPlan` 한 줄을 박아 ExecPlan 문서를 자동 호출 트리거로 연결. 7단계 진화 도식: ① anthropics/skills(표준 정의 정적) → ② github/spec-kit(외부 도구 통합 정적) → ③ fastapi(라이브러리 self-hosted 정적) → ④ astral-sh/uv(듀얼 지침서 정적) → ⑤ scikit-learn(AI disclosure 정적) → ⑥ flutter(vendor-neutral 자산 정적) → ⑦ **openai-cookbook(살아있는 운영 노트 + ExecPlan)**. 1~6 모두 정적 가이드, 7번째에서 처음으로 **운영 중 발견을 즉시 가이드에 반영**하는 작업기억 모드로 진화. 또한 `registry.yaml`(3,180줄, 289 항목) + `authors.yaml`(583줄, 115명) + `python .github/scripts/check_notebooks.py` 검증 도구로 **콘텐츠 거버넌스 자동화** — SLEP/PDEP가 표준 변경 거버넌스라면 registry.yaml은 콘텐츠 변경 거버넌스
- [[flutter-flutter]] — **agent-skills 표준의 vendor-neutral 채택 사례 (4단계)**. [[flutter]] (Google, ★176K 11년차 OSS)가 `.agents/skills/{find-release, rebuilding-flutter-tool, upgrade-browser}/SKILL.md` 3종을 두고, **`.claude/skills` → `../.agents/skills` 심볼릭 링크**로 멀티 벤더 forwarding. `.agents/skills/README.md`가 5개 채택 요건 중 "**Standard Compliance: must follow https://agentskills.io/specification**"를 명시 — Anthropic 폐쇄 표준이 아닌 오픈 표준임을 공인. 자체 검증 도구 `dart_skills_lint`(--check-trailing-whitespace, --check-absolute-paths, --check-relative-paths, --fix)로 SKILL.md를 코드 자산으로 취급. 또한 `docs/rules/`에 `rules.md(30K) → 10k → 4k → 1k` **4계층 토큰 예산 룰**을 두고 도구별 한계(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K) 매트릭스에 자동 매칭 — progressive disclosure를 토큰 단위로 더 세분화. → 외부 채택 4단계 진화 완성: ① anthropics/skills(표준 정의) → ② github/spec-kit(메소드론 → 다중 에이전트 어댑터) → ③ fastapi/fastapi(라이브러리 self-hosted) → ④ **flutter/flutter(대규모 OSS asset → vendor-neutral 위치 + 다중 에이전트 forwarding + 토큰 예산 다층화)**. **표준 채택자가 표준 정의자의 위치 컨벤션을 누르고 자체 결정**한 첫 사례 — `.agents/`가 `.claude/`를 누른다
- [[langchain-ai-langchain]] / [[langchain-ai-langgraph]] / [[jlowin-fastmcp]] — **agent-skills 외부 채택 9단계 진화의 9번째 — 첫 "패턴 확산 (3개 동시 채택)" 사례** (17회차). 17회차 수집한 LangChain (292줄) / LangGraph (57줄) / FastMCP (168줄, symlink) 모두 `AGENTS.md = CLAUDE.md` 동기화 패턴을 채택. 8단계 [[openai-openai-agents-python]]에서 첫 미러링 패턴이 정립됐다면, 17회차에서 **3개 독립 OSS가 동시에 같은 컨벤션 채택** = LLM 협업 표준이 한 회사 내부 패턴이 아닌 **업계 표준으로 빠르게 수렴 중** 증거. LangChain은 `monorepo libs/` + uv + ruff/mypy/pytest 통합 가이드, LangGraph는 매우 간결 (`make format/lint/test` + `TEST=path` 변수), FastMCP는 prek (Ruff+Prettier+ty) + bot review 메타-가이던스 + release 네이밍 규칙. 9단계 진화 도식: ① anthropics/skills(표준 정의) → ② spec-kit → ③ fastapi → ④ uv → ⑤ scikit-learn → ⑥ flutter → ⑦ openai-cookbook(living) → ⑧ openai-agents-python(미러링) → ⑨ **langchain/langgraph/fastmcp 동시 채택 (업계 표준 수렴)**. 1~8이 단발 사례라면 9는 패턴 자체의 확산 — 이로써 AGENTS.md = CLAUDE.md는 **OpenAI 사내 패턴이 아닌 다국적 OSS 협업 컨벤션**으로 격상. 또한 FastMCP의 `Be constructively skeptical of bot review comments`는 **bot review 시대의 메타-가이던스** 첫 등장 — CodeRabbit/Codex/claude-bot이 일상화된 시대의 워크플로우 진화
- [[langchain-ai-langchain]] / [[langchain-ai-langgraph]] / [[jlowin-fastmcp]] — **agent-skills 외부 채택 9단계 진화의 9번째 — 첫 "패턴 확산 (3개 동시 채택)" 사례** (17회차). 17회차 수집한 LangChain (292줄) / LangGraph (57줄) / FastMCP (168줄, symlink) 모두 `AGENTS.md = CLAUDE.md` 동기화 패턴을 채택. 8단계 [[openai-openai-agents-python]]에서 첫 미러링 패턴이 정립됐다면, 17회차에서 **3개 독립 OSS가 동시에 같은 컨벤션 채택** = LLM 협업 표준이 한 회사 내부 패턴이 아닌 **업계 표준으로 빠르게 수렴 중** 증거. LangChain은 `monorepo libs/` + uv + ruff/mypy/pytest 통합 가이드, LangGraph는 매우 간결 (`make format/lint/test` + `TEST=path` 변수), FastMCP는 prek (Ruff+Prettier+ty) + bot review 메타-가이던스 + release 네이밍 규칙. 9단계 진화 도식: ① anthropics/skills(표준 정의) → ② spec-kit → ③ fastapi → ④ uv → ⑤ scikit-learn → ⑥ flutter → ⑦ openai-cookbook(living) → ⑧ openai-agents-python(미러링) → ⑨ **langchain/langgraph/fastmcp 동시 채택 (업계 표준 수렴)**. 1~8이 단발 사례라면 9는 패턴 자체의 확산 — 이로써 AGENTS.md = CLAUDE.md는 **OpenAI 사내 패턴이 아닌 다국적 OSS 협업 컨벤션**으로 격상. 또한 FastMCP의 `Be constructively skeptical of bot review comments`는 **bot review 시대의 메타-가이던스** 첫 등장 — CodeRabbit/Codex/claude-bot이 일상화된 시대의 워크플로우 진화
- [[langchain-ai-deepagents]] / [[pydantic-pydantic-ai]] — **agent-skills 외부 채택 10단계 진화의 10번째 — "패턴 확산 가속 (6 OSS 동시 표준)" 사례** (18회차). 18회차 수집한 DeepAgents (AGENTS.md 364줄, monorepo libs/{deepagents,cli,evals}) + Pydantic AI (AGENTS.md = CLAUDE.md byte-for-byte 10K 동기화) 추가로 이제 6개 LLM OSS가 동시에 `AGENTS.md = CLAUDE.md` 동기화 채택 — LangChain/LangGraph/DeepAgents/FastMCP/OpenAI Agents Python/Pydantic AI. CrewAI/PandasAI 미채택은 **LangChain 진영 + OpenAI/Pydantic 진영 vs 독립 진영의 거버넌스 분기점** 시사. 9단계가 "3개 OSS 동시"라면 10단계는 "6개로 확산" — 이제 AGENTS.md=CLAUDE.md는 **LLM 프레임워크 OSS의 사실상 표준**. 또한 DeepAgents의 monorepo 구조(`libs/{deepagents, cli, evals}`)는 LangGraph(libs/9개), LangChain(libs/7개)과 같은 "LLM 프레임워크 monorepo libs/" 명명 컨벤션 수렴. Pydantic AI는 더 나아가 **YAML/JSON 기반 agent 정의** 1급 지원 → "agent를 코드 없이 SKILL.md처럼 packaging" 가능성 시사 — agent-skills의 **다음 진화 방향 (코드 없는 agent 패키지)**으로의 단서. 10단계 진화 도식: ①anthropics/skills → ②spec-kit → ③fastapi → ④uv → ⑤scikit-learn → ⑥flutter → ⑦openai-cookbook → ⑧openai-agents-python → ⑨langchain/langgraph/fastmcp 동시 → ⑩ **deepagents/pydantic-ai 합류 = 6 OSS 표준화**
- [[vercel-next.js]] — **agent-skills 외부 채택 12단계 진화 — "양대 변종 동시 등장 (skills hub + LLM PR HTML 마커)"** (22회차). 22회차 수집한 [[nextjs]] (Vercel, ★139K)가 22KB / 446줄짜리 AGENTS.md (= CLAUDE.md symlink, 3번째 사례)에서 양대 변종을 단일 OSS에서 동시 발견: ① **`$skill` 인덱싱 (skills hub)** — `$pr-status-triage`, `$flags`, `$dce-edge`, `$react-vendoring`, `$runtime-debug`, `$authoring-skills` 6개 SKILL.md를 `$<name>` syntax로 참조. AGENTS.md가 거대 hub로 진화하고 세부 SOP는 `.agents/skills/<name>/SKILL.md`로 분리. (8단계 OpenAI Agents Python의 `$skill-name` 명령형 호출 패턴이 인덱싱 패턴으로 진화), ② **HTML PR 마커** (`<!-- NEXT_JS_LLM_PR -->`) — PR 본문에 의무 삽입, LLM 생성 PR을 자동 식별·집계하기 위한 거버넌스 신호 발신기 (AGENTS.md가 PR 봇/거버넌스와 연결되는 첫 사례). 추가로 Anti-pattern 명시 + Secret redaction 의무화 + Task 분해 검증 의무화. 22회차 양극화 가설 보강 — 5개 프론트 OSS 중 Next.js만 채택 (1/5 = 20%) vs 21회차 운영 3/5 = 60%, **프론트 진영 채택률은 운영의 1/3**. shadcn-ui/ui는 새로운 거버넌스 모델 "Open Code (10번째)" 기여 — npm install이 아닌 CLI 코드 분배 (의도적 fragmentation). 12단계 진화 도식: ①~⑪ 동일 → ⑫ **next.js 단일 OSS에서 skills hub + LLM PR 마커 양대 변종 동시 등장**. 1~11이 "패턴 등장 + 확산"이었다면, 12단계는 **AGENTS.md가 단순 가이드를 넘어 (a) skills 디렉토리 인덱스 (b) PR 봇 거버넌스 신호 발신기로 진화**. 향후 13단계 후보: AGENTS.md 자동 생성/갱신 메타-도구, multi-OSS AGENTS.md 동기화 표준, AGENTS.md를 IDE/에이전트가 직접 enforce하는 런타임 가드.
- [[prometheus-prometheus]] / [[grafana-grafana]] / [[getsentry-sentry]] — **agent-skills 외부 채택 11단계 진화 — "운영/Observability 진영 확산 + 4가지 변종 동시 등장"** (19회차). 19회차 수집한 운영 진영 5개 OSS 중 3개([[prometheus]] / [[grafana]] / [[sentry]])가 동시에 AGENTS.md 채택 — LLM 프레임워크 진영을 넘어 운영 진영으로 표준 확산 결정적 증거. 이전 1~10단계가 "한 가지 패턴(byte-for-byte sync 또는 skill 모음)의 확산"이었다면, 11단계는 **4가지 새 변종 동시 등장**: ① **PR-패턴 가이드** (Prometheus 148줄, "최근 merge된 PR로부터 maintainer 선호 패턴 추출" — 가장 데이터 기반, 가장 유지비 낮음), ② **`@AGENTS.md` redirect CLAUDE.md** (Grafana/Sentry, CLAUDE.md를 1줄로 축소해 SSOT를 AGENTS.md로 일원화), ③ **계층화 AGENTS.md** (Grafana 2-tier: docs/ + alerting/, Sentry 4-tier: src/ + tests/ + static/ + 루트 — 모노레포 영역별 다른 컨벤션 → 디렉토리에 분산), ④ **Anti-fragmentation 명문화** (Sentry "Do not add to CLAUDE.md or Cursor rules" — AI agent별 룰 파일 drift 방지). 추가로 Grafana는 **`<!-- version: 2.0.0 -->`** 주석으로 AGENTS.md 자체 버저닝 첫 도입. Docker/Moby + GitHub Actions는 미채택 → "애플리케이션 코드에 가까운 운영 OSS는 적극 채택, 인프라 코어 OSS는 신중" 양극화. 9번째 거버넌스 모델 추가 = **CNCF graduated** (Prometheus, Linux Foundation 산하). 11단계 진화 도식: ①~⑩ 동일 → ⑪ **prometheus/grafana/sentry 합류 = 9 OSS 표준화 + 4 변종 동시 등장 + 운영 진영 확산**. 향후 12단계 후보: AGENTS.md를 자동 생성/갱신하는 메타-도구(현재는 사람이 직접 작성), workflow YAML/Dockerfile 등 코드 외 자산에 대한 LLM 가이드 표준.

- [[openai-openai-agents-python]] — **agent-skills 외부 채택 8단계 진화의 8번째 — 첫 "9개 본격 운영 SOP" 사례**. [[openai]] 공식 1년차 멀티 에이전트 Python SDK(★25K, v0.14.6)가 `.agents/skills/` 안에 9개 SKILL.md를 명문화: `code-change-verification`(2.5KB) / `openai-knowledge`(1.9KB) / `implementation-strategy`(4.5KB) / `pr-draft-summary`(5.7KB) / `runtime-behavior-probe`(13.4KB ★) / `docs-sync`(4.3KB) / `examples-auto-run`(3.2KB) / `final-release-review`(8.0KB) / `test-coverage-improver`(2.7KB). AGENTS.md "Mandatory Skill Usage" 섹션이 각 스킬을 **`$skill-name` 명령형 호출**로 트리거 + 정확한 트리거 조건과 스킵 조건 명시. 각 스킬은 자체 `agents/`(sub-agent prompts), 일부는 `scripts/`·`references/`·`templates/`까지 보유. **스킬 간 호출 (skill chaining)** 명시 — 예: `$implementation-strategy`가 내부에서 `$final-release-review/scripts/find_latest_release_tag.sh` 호출 (spec-kit Codex Skills의 단방향 통합보다 한 단계 발전). 추가로 **`AGENTS.md = CLAUDE.md` byte-for-byte 동일 동기화 패턴** (12,900B 양쪽 미러링, uv `@AGENTS.md` import와 flutter `.agents/` 심볼릭 링크의 중간 — 가장 단순한 vendor-neutral 적응). 8단계 진화 도식: ① anthropics/skills → ② spec-kit → ③ fastapi → ④ uv → ⑤ scikit-learn → ⑥ flutter → ⑦ openai-cookbook(살아있는 운영 노트) → ⑧ **openai-agents-python(9개 운영 SOP 스킬 + AGENTS.md=CLAUDE.md 미러링 + 스킬 체이닝)**. 1~7이 가이드/표준/메소드론 사례라면, 8번째는 처음으로 **실무 운영 워크플로우 전체를 SKILL.md로 풀스택 명문화**. cookbook(가이드 단)이 정의한 패턴을 본 SDK(본체 단)가 자기 운영에 풀스택 적용한 **거버넌스 자기 채택 (self-adoption)** 결정적 증거 — 같은 회사(OpenAI)에서 메소드론과 본체를 한 묶음으로 운영

## 열린 질문

- **위키 SKILL.md의 메트릭**: 자동 호출 정확도(trigger rate)는 측정 가능하지만, **호출 후 답변 품질**은 어떻게 평가? LLM-as-judge로 충분한가?
- **Plugin namespace 충돌**: 같은 이름의 스킬이 여러 플러그인에 존재할 때 우선순위는? Enterprise > Personal > Project > Plugin이 명확하지만, 같은 레벨 안에서는?
- **Skill 자동 진화**: skill-creator의 description 최적화 루프를 본문(body)까지 확장 가능한가? 아니면 본문 변경은 사람이 검토해야 하는가?
- **위키와의 양방향성**: SKILL.md가 위키 페이지를 Read하는 건 가능. 위키 페이지가 SKILL.md를 참조 인용하는 건? (지금 이 페이지가 그 첫 시도)
- **Cross-skill composition**: 한 스킬이 다른 스킬을 호출하는 패턴은 표준에 정의되어 있는가? skill-creator는 자기 안에서 grader·comparator·analyzer 서브에이전트를 spawn하는데, 이게 일반화되는가?
