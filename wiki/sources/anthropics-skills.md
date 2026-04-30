---
title: "anthropics/skills — Anthropic 공식 Agent Skills 레퍼런스"
type: source
source_type: article
source_url: "https://github.com/anthropics/skills"
raw_path: "raw/articles/anthropics-skills/"
author: "Anthropic"
date_published: 2026-04
date_ingested: 2026-04-27
tags: [agent-skills, anthropic, skills, claude-code, marketplace, plugin, progressive-disclosure, skill-creator, mcp-builder, agentskills.io]
related:
  - "[[claude-code]]"
  - "[[agent-skills]]"
  - "[[slash-commands-vs-agent-skills]]"
  - "[[mcp]]"
  - "[[harness]]"
  - "[[context-engineering]]"
  - "[[token-economy]]"
confidence: high
inbound_count: 77
cited_by:
  - "[[agent-skills]]"
  - "[[agent-stack-evolution]]"
  - "[[anthropic]]"
  - "[[anthropics-claude-cookbooks]]"
  - "[[backend-fastapi-stack]]"
  - "[[claude-code]]"
  - "[[fastapi]]"
  - "[[fastapi-fastapi]]"
  - "[[flutter]]"
  - "[[flutter-flutter]]"
  - "[[github]]"
  - "[[github-spec-kit]]"
  - "[[harness]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[llm-wiki-pattern]]"
  - "[[mcp]]"
  - "[[openai-openai-cookbook]]"
  - "[[pandas-dev-pandas]]"
  - "[[scikit-learn]]"
  - "[[scikit-learn-scikit-learn]]"
  - "[[slash-commands-vs-agent-skills]]"
  - "[[spec-kit]]"
cited_by_count: 22
---

# anthropics/skills — Anthropic 공식 Agent Skills 레퍼런스

## 한줄 요약

> Anthropic이 직접 운영하는 Claude Code/Claude.ai/API용 **공식 예시 스킬 + 플러그인 마켓플레이스 + 표준 명세 진입점**. 17개 스킬(생산용 4 + 예시 12 + claude-api 1)을 단일 리포에 모아 "스킬을 만드는 스킬(skill-creator)"부터 진짜 운영 수준의 docx/pdf 스킬까지 전부 노출. SKILL.md 작성 패턴·progressive disclosure·triggering 최적화의 1차 레퍼런스.

## 핵심 내용

### 리포 구조 (단순)

```
anthropics/skills/
├── README.md                    # 마켓플레이스 등록 + 스킬 작성 가이드
├── .claude-plugin/
│   └── marketplace.json         # 3개 플러그인 정의
├── skills/                      # 17개 SKILL.md 예시
├── spec/agent-skills-spec.md    # → agentskills.io/specification 리다이렉트
├── template/SKILL.md            # 7줄 placeholder
└── THIRD_PARTY_NOTICES.md
```

핵심 통찰: **spec은 외부(agentskills.io)에 있고 리포 자체는 "구현 사례 + 배포 채널"** 두 역할만 한다. 스킬이 표준이 되는 과정에서 Anthropic이 자기 구현을 외부에 분리해 표준의 중립성을 확보한 흔적.

### 마켓플레이스 — 3개 플러그인 묶음

| 플러그인 | 라이선스 | 스킬 수 | 포함 스킬 |
|----------|---------|--------|-----------|
| **document-skills** | source-available | 4 | xlsx, docx, pptx, pdf — Claude의 문서 생성 기능을 실제로 구동하는 production 스킬 |
| **example-skills** | Apache 2.0 | 12 | algorithmic-art, brand-guidelines, canvas-design, doc-coauthoring, frontend-design, internal-comms, mcp-builder, skill-creator, slack-gif-creator, theme-factory, web-artifacts-builder, webapp-testing |
| **claude-api** | Apache 2.0 (추정) | 1 | claude-api — Claude API/SDK 사용 가이드 |

설치 명령:
```
/plugin marketplace add anthropics/skills
/plugin install document-skills@anthropic-agent-skills
/plugin install example-skills@anthropic-agent-skills
```

플러그인 네임스페이스: `document-skills:pdf`, `example-skills:skill-creator` 식으로 호출. [[claude-code]] 엔티티가 언급한 "Plugin namespace 충돌 없음"의 실증 사례.

### 17개 스킬을 4갈래로 분류 (Anthropic README 기준)

| 카테고리 | 대표 스킬 | 패턴적 가치 |
|----------|----------|-------------|
| **Document** | xlsx, docx, pptx, pdf | production 운영 중인 스킬 — 큰 reference + 다양한 scripts/ 번들 |
| **Creative & Design** | algorithmic-art, canvas-design, frontend-design, theme-factory | 짧은 SKILL.md + 시각 자료 풍부 |
| **Development & Technical** | mcp-builder, skill-creator, webapp-testing, web-artifacts-builder | multi-domain reference 패턴 |
| **Enterprise & Communication** | brand-guidelines, internal-comms, doc-coauthoring, slack-gif-creator | 회사 톤·정책 패키징 |

### 4개 SKILL.md 사례 분석

#### 1. skill-creator (33KB) — 가장 풍부한 메타-스킬

"스킬을 만드는 스킬." 5단계 핵심 루프:
1. **Capture Intent** — 사용자가 원하는 트리거·출력 포맷·테스트 케이스 필요성을 인터뷰
2. **Interview & Research** — 엣지 케이스, 의존성을 미리 묻고 컨텍스트 확보
3. **Write SKILL.md** — name + description + 본문. **description은 의도적으로 "pushy"하게** ("undertrigger 경향" 보정)
4. **Test & Evaluate** — `evaluation viewer`(`generate_review.py`)로 with-skill / baseline 비교, benchmark 집계
5. **Improve & Iterate** — feedback 데이터 읽고 일반화·간결화·이유 설명·반복 작업 번들링

핵심 원칙 인용:
> "Today's LLMs are *smart*. When given a good harness [they] can go beyond rote instructions."
> "Rather than put in fiddly overfitty changes, ... try branching out and using different metaphors."

description 최적화 별도 루프: 20개 trigger 검증 쿼리(should-trigger 8-10 + should-not-trigger 8-10) → 60/40 train/test split → 5회 자동 iteration.

#### 2. mcp-builder (9KB) — multi-domain reference 패턴

`SKILL.md`는 4단계 워크플로우만 정리하고, 상세는 `reference/python_mcp_server.md`, `reference/node_mcp_server.md`, `reference/evaluation.md`로 분리. **"Claude는 관련 reference만 필요할 때 읽는다"는 progressive disclosure의 모범**.

> "When a skill supports multiple domains/frameworks, organize by variant"

#### 3. frontend-design (4.4KB) — 짧고 강한 가이드

"AI slop 미학을 피하라" 같은 강한 메시지를 SKILL.md 단일 파일에 응축. progressive disclosure의 다른 극단 — **본문이 짧으면 supporting files 없이도 작동**. "BOLD aesthetic direction"·"Maximalism vs minimalism"·"Never converge" 같은 휴리스틱이 핵심.

#### 4. webapp-testing (3.9KB) — 스크립트 블랙박스 패턴

`scripts/with_server.py`를 **읽지 말고 호출만** 하라고 명시:
> "DO NOT read the source until you try running the script first ... These scripts can be very large and thus pollute your context window."

[[token-economy]] 원칙의 깔끔한 적용 — 도구는 컨텍스트에 들이지 말고 호출 인터페이스만 노출.

### Skill 작성 표준 (Anthropic 공식 기준)

#### 3-level Progressive Disclosure
1. **Metadata** (name + description) — 항상 컨텍스트, 약 100 단어
2. **SKILL.md body** — 트리거 시 로드, **<500 lines 권장**
3. **Bundled resources** (`scripts/`, `references/`, `assets/`) — 필요 시만 로드, **scripts는 실행만 하면 컨텍스트에 안 들어감**

#### Anatomy
```
skill-name/
├── SKILL.md (필수)
│   ├── YAML frontmatter (name, description 필수)
│   └── Markdown instructions
└── (선택) scripts/, references/, assets/
```

#### description 작성 원칙
- **Pushy하게**: "undertrigger 경향" 보정. "use this skill whenever the user mentions X, Y, or Z"
- **언제 쓰는지 + 무엇을 하는지** 둘 다 포함
- 1,536자 cap

#### 4가지 안티 패턴
1. SKILL.md가 500줄 넘는데 hierarchy 없음 → references로 분리
2. description이 "what"만 있고 "when"이 없음
3. 매 호출마다 같은 helper script를 LLM이 새로 작성 → scripts/에 번들
4. ALWAYS/NEVER로 도배 → "왜 중요한지" 설명으로 대체

## 주요 인사이트

### 1. spec 분리 = 표준 오너십 분리

`spec/agent-skills-spec.md`가 agentskills.io로 리다이렉트되는 건 우연이 아니다. **Anthropic이 SKILL.md 표준의 단일 운영자가 되는 걸 의도적으로 피했다**. 리포는 "Anthropic의 구현 사례"고, 표준은 별도 도메인. [[mcp]]가 Anthropic 발이지만 modelcontextprotocol.io에서 운영되는 패턴과 동일.

### 2. document-skills가 "source-available, not open source" 인 이유

xlsx/docx/pptx/pdf는 Claude.ai의 실제 문서 생성을 구동하는 production 코드. **Apache 2.0으로 풀면 경쟁사가 그대로 가져갈 수 있다.** 그래서 "참고는 가능, fork·재배포는 라이선스로 통제." Anthropic의 비즈니스 라인이 어디서 시작되는지 보여주는 신호.

### 3. skill-creator의 자기참조 구조

**스킬 작성을 가르치는 스킬이 다시 SKILL.md 형식**으로 쓰여 있고, **자기 자신을 평가·개선하는 검증 루프를 SKILL.md 안에서 주도**. 이게 [[autonomous-research-loop]]의 program.md와 같은 자기 진화 패턴이다. 다만 autoresearch는 "코드를 진화"시키고 skill-creator는 "지침서를 진화"시키는 차이.

### 4. progressive disclosure는 [[token-economy]] + [[context-engineering]]의 결합

- 메타데이터 100단어가 17개 스킬 × 1,536자 cap = 약 26K 토큰만 상시 점유
- 본문은 트리거된 스킬만 로드 (평균 4-5KB)
- scripts는 호출만 — 컨텍스트 0
- references는 LLM이 "이건 안 봐도 됨" 판단하면 스킵

이걸 17개 스킬 단위로 운영하는 것 자체가 **컨텍스트 윈도우를 17개의 잠재 도메인으로 분할 구획화**하는 기법.

### 5. 위키에 직접 응용 가능한 패턴

| anthropic/skills 패턴 | 이 위키에서의 대응 |
|----------------------|-------------------|
| skill-creator의 5단계 루프 | 새 위키 페이지 작성 워크플로우 (CLAUDE.md "수집 워크플로우") |
| mcp-builder의 reference 분리 | `wiki/syntheses/`가 SKILL.md 본문, `wiki/sources/`가 references |
| webapp-testing의 "scripts는 읽지 마라" | 위키 조회 시 raw/articles는 본문 로드 금지, 요약 페이지만 |
| description "pushy" 원칙 | `~/.claude/skills/wiki/SKILL.md`의 description 재작성 후보 |

## 관련 엔티티/개념

- [[claude-code]]: Skills 기능 제공 주 제품, `/plugin marketplace add anthropics/skills`로 설치
- [[agent-skills]]: 이 소스로 정의되는 신규 개념 페이지 — 표준·구조·운영 원칙
- [[slash-commands-vs-agent-skills]]: 통합 경위와 비교 (이 소스의 사전조사)
- [[mcp]]: 도구 통합 프로토콜. mcp-builder 스킬이 직접 다룸
- [[harness]]: 스킬 = "패키지 레이어"로서 하네스의 4층 중 하나
- [[context-engineering]]: progressive disclosure가 컨텍스트 엔지니어링의 모범
- [[token-economy]]: 100w 메타 + 본문 lazy load + scripts는 호출만 = 토큰 경제학 적용 사례
- [[autonomous-research-loop]]: skill-creator의 자기 진화 루프와 program.md 자율 진화의 공통 구조

## 인용할 만한 구절

> "Skills are folders of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks."
> — README

> "The skill description field is the primary triggering mechanism. ... please make the skill descriptions a little bit 'pushy'."
> — skill-creator/SKILL.md

> "Today's LLMs are *smart*. They have good theory of mind and when given a good harness can go beyond rote instructions and really make things happen. ... If you find yourself writing ALWAYS or NEVER in all caps, or using super rigid structures, that's a yellow flag."
> — skill-creator/SKILL.md

> "DO NOT read the source until you try running the script first and find that a customized solution is absolutely necessary. These scripts can be very large and thus pollute your context window."
> — webapp-testing/SKILL.md

> "When a skill supports multiple domains/frameworks, organize by variant ... Claude reads only the relevant reference file."
> — skill-creator/SKILL.md

## 메모

- 수집 시점 raw 보존: README.md, marketplace.json, template-skill.md, spec-redirect.md, skill-creator-skill.md (33KB), mcp-builder-skill.md (9KB), frontend-design-skill.md, webapp-testing-skill.md → `raw/articles/anthropics-skills/`
- **개인 활용 후속 탐구**:
  1. 현재 운영 중인 `~/.claude/skills/wiki/SKILL.md`의 description을 "pushy" 원칙으로 재작성. 20개 trigger 검증 쿼리로 확인
  2. **개인 비서 AI 서비스 설계 시 skill-creator의 5단계 루프**를 그대로 차용 가능 — Anthropic이 "billions a year"로 검증한 워크플로우
  3. 이 위키에 `templates/skill.md` 추가 검토 (기존 entity/concept/source/synthesis 4종 + skill 1종)
- Partner Skills 섹션이 향후 확장 가능성 시그널 — Notion이 첫 사례. 컴투스플랫폼 BI 스킬을 만든다면 이 패턴이 모범.
