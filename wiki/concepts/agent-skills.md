---
title: "Agent Skills (SKILL.md 패키지)"
type: concept
category: ai
tags: [agent-skills, skills, claude-code, anthropic, progressive-disclosure, agentskills.io, skill-creator, harness, 패키지레이어, claude-cookbooks, custom-skills, spec-kit, codex-skills, multi-agent-adoption]
related: [[claude-code]], [[claude-agent-sdk]], [[anthropic]], [[mcp]], [[harness]], [[context-engineering]], [[token-economy]], [[llm-wiki-pattern]], [[autonomous-research-loop]], [[spec-kit]], [[spec-driven-development]], [[github]]
source_count: 4
created: 2026-04-27
updated: 2026-04-27
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

## 열린 질문

- **위키 SKILL.md의 메트릭**: 자동 호출 정확도(trigger rate)는 측정 가능하지만, **호출 후 답변 품질**은 어떻게 평가? LLM-as-judge로 충분한가?
- **Plugin namespace 충돌**: 같은 이름의 스킬이 여러 플러그인에 존재할 때 우선순위는? Enterprise > Personal > Project > Plugin이 명확하지만, 같은 레벨 안에서는?
- **Skill 자동 진화**: skill-creator의 description 최적화 루프를 본문(body)까지 확장 가능한가? 아니면 본문 변경은 사람이 검토해야 하는가?
- **위키와의 양방향성**: SKILL.md가 위키 페이지를 Read하는 건 가능. 위키 페이지가 SKILL.md를 참조 인용하는 건? (지금 이 페이지가 그 첫 시도)
- **Cross-skill composition**: 한 스킬이 다른 스킬을 호출하는 패턴은 표준에 정의되어 있는가? skill-creator는 자기 안에서 grader·comparator·analyzer 서브에이전트를 spawn하는데, 이게 일반화되는가?
