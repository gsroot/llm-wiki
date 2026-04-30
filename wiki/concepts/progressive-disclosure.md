---
title: 점진적 공개 (Progressive Disclosure)
aliases:
- Progressive Disclosure
- progressive-disclosure
- 점진적 공개
- 단계적 공개
- 컨텍스트 lazy load
type: concept
category: ai
tags:
- progressive-disclosure
- LLM
- context
- agent-skills
- token-economy
- ux-design
- lazy-loading
related:
- '[[agent-skills]]'
- '[[harness]]'
- '[[token-economy]]'
- '[[context-engineering]]'
- '[[claude-code]]'
- '[[anthropics-skills]]'
- '[[flutter-flutter]]'
- '[[slash-commands-vs-agent-skills]]'
- '[[anthropics-claude-cookbooks]]'
- '[[openai-chatgpt-codex-guide]]'
- '[[rcif-prompt-pattern]]'
- '[[matechat]]'
- '[[c2spf-analytics]]'
source_count: 3
observed_source_refs: 9
inbound_count: 21
created: 2026-04-30
updated: 2026-04-30
cited_by_count: 12
---

# 점진적 공개 (Progressive Disclosure)

## 정의

**필요한 정보를 필요한 시점에만 노출**하는 인터페이스 설계 원칙. 1980년대 UX 디자인에서 유래(Jakob Nielsen이 정형화)했고, 2025~2026년 LLM 에이전트 시대에 들어 **컨텍스트 윈도우 압박을 구조적으로 해결하는 1차 표준**으로 재발견됐다.

핵심 발상: 모든 정보를 한 번에 보여주면 (a) 사용자는 압도되고 (b) LLM은 토큰이 폭발한다. 대신 **메타데이터·요약 → 본문 → 보조 자료** 같은 계층을 두고 트리거 조건이 충족될 때만 다음 계층을 로드한다.

## 왜 중요한가

LLM 에이전트의 컨텍스트 윈도우는 200K~1M 토큰으로 보이지만, 실제로는:

- **상시 점유 영역** (시스템 프롬프트, 도구 정의, 메모리 등)이 30~50K 토큰 즉시 차지
- 작업 진행에 따라 자연 누적되는 토큰이 모델 성능을 끌어내림 (long-context degradation)
- 가격·latency가 토큰 수에 선형 비례

[[agent-skills]] 표준이 progressive disclosure를 1급 메커니즘으로 명시한 이유: **17개 스킬 × 100단어 메타데이터 = 약 26K 토큰만 상시 점유**하면 17개 도메인을 잠재 활성화한 상태로 두고도 윈도우의 88%를 작업에 쓸 수 있다.

## 핵심 내용

### 3계층 표준 (Anthropic agent-skills)

[[anthropics-skills]] 공식 표준이 정의한 3-level structure:

| 계층 | 내용 | 로드 시점 | 일반적 크기 |
|---|---|---|---|
| **Metadata** | `name` + `description` | 항상 (세션 시작 시) | 약 100 단어 / 1,536자 cap |
| **SKILL.md body** | 본문 instructions | 트리거 시 1회 | <500 lines 권장 |
| **Bundled resources** | `scripts/`, `references/`, `assets/` | 필요 시만 / scripts는 호출만 | 무제한 |

핵심 원칙:
- **scripts는 컨텍스트에 들어가지 않는다** — LLM이 호출 인터페이스만 알고 실행. webapp-testing 스킬: `"DO NOT read the source until you try running the script first"`.
- **references는 LLM 판단으로 스킵** — multi-domain일 때 관련 variant만 로드.
- **description이 자동 호출 트리거** — "pushy"하게 작성해 undertrigger 보정.

### 4계층 변종 (Flutter rules-1k/4k/10k/full)

[[flutter-flutter]]는 [[anthropics-skills]] 3계층을 **AI 도구 시장 매트릭스에 자동 매칭하는 4계층**으로 확장:

| 계층 | 크기 | 매칭 도구 |
|---|---|---|
| `rules_1k` | 799 B | OpenAI Custom Instructions (1.5K cap), CodeRabbit (1K) |
| `rules_4k` | 3.5 KB | Copilot (4K) |
| `rules_10k` | 9.4 KB | Antigravity (12K) |
| `rules_full` | 30 KB | Claude Code (충분한 컨텍스트) |

각 도구가 가진 토큰 예산에 맞춰 **같은 가이드의 다른 압축률**을 자동 선택. progressive disclosure가 단일 사용자 trigger 기반이 아닌 **도구별 capacity-aware** 형태로 진화한 사례.

### LLM 외 사례 (UX 디자인)

전통 UX의 progressive disclosure:
- API 문서 — "Quickstart → Reference → Internal" 3계층
- IDE intellisense — 함수 시그니처는 hover 한 번, docstring은 두 번째 hover
- 모바일 앱 — "primary action은 즉시, secondary는 메뉴, tertiary는 settings"
- 데이터 대시보드 — "요약 차트 → drilldown → raw 행" 3-click 룰

LLM 에이전트의 progressive disclosure는 이 UX 원칙을 **토큰 단위로 다시 정형화**한 것.

## 안티패턴

| 안티패턴 | 문제 | 회피 |
|---|---|---|
| 1KB 미만 metadata 안에 본문 전체 압축 | description이 progressively 로드 안 됨, 트리거 신뢰도 ↓ | description은 "언제 쓰는지 + 무엇을 하는지"만, 본문은 body로 |
| 모든 references를 본문에 인라인 | 트리거 시 토큰 폭발 | multi-domain은 variant별 reference 분리 |
| scripts/ 안에 LLM이 매번 helper를 직접 작성 | 토큰·시간 모두 낭비, 일관성 ↓ | 자주 쓰는 helper는 scripts/에 번들, 호출만 |
| description 없이 "Use this skill"만 적힘 | 트리거 안 됨 (undertrigger) | trigger 조건 명시 + 약간 "pushy"한 어조 |

## owner 활용 시나리오

### [[matechat]] 39 SKILL 작성

각 SKILL.md를 다음 3계층으로 설계:
- **frontmatter description** (100 단어): "사용자가 X를 묻거나 Y 데이터가 필요한 상황에 자동 활성화"
- **본문** (<500줄): 단계별 instructions + RCIF 4요소 ([[rcif-prompt-pattern]])
- **scripts/references/** : SKILL chaining 용 helper, 별도 파일

### [[c2spf-analytics]] BI 대시보드

UX의 progressive disclosure 적용:
- 1단계: 일간 KPI 카드 (5개 숫자, 즉시 표시)
- 2단계: 클릭 시 weekly trend 차트
- 3단계: drill-down 시 raw event 행

### [[claude-code]] subagent

`.claude/agents/<name>.md` 작성 시:
- **description** — 트리거 조건 (Claude가 자동 위임할지 판단)
- **본문 prompt** — 작업 정의
- **tools 제한** — `allowed-tools` 로 도구 capability를 미리 좁힘 (= 컨텍스트 미리 줄이기)

## 관련 개념

- [[agent-skills]] — progressive disclosure를 1급 메커니즘으로 박은 표준. 본 개념의 가장 정형화된 응용.
- [[token-economy]] — progressive disclosure는 토큰 경제학의 운영 핸들. 메타 100w 상시 + 본문 lazy + scripts는 호출만 = 토큰 경제학 적용 사례.
- [[context-engineering]] — "필요 범위만 컨텍스트에 로드" 원칙의 모범. progressive disclosure는 그 구현 패턴.
- [[harness]] — 4층 하네스의 "패키지 레이어"가 progressive disclosure를 가장 깊게 활용. flutter rules 4계층은 patternization의 정수.
- [[rcif-prompt-pattern]] — RCIF의 4요소도 본질적으로 progressive disclosure (Role·Context·Instruction·Format을 점진적으로 채워가며 작성).

## 출처

- [[anthropics-skills]] — 3계층 표준 (Metadata / SKILL.md body / Bundled resources). [[claude-code]] / Claude.ai / API에서 공식 채택. skill-creator 스킬이 trigger 검증 20-쿼리 루프로 description 최적화.
- [[flutter-flutter]] — 4계층 변종 (rules-1k/4k/10k/full). AI 도구 시장 매트릭스에 자동 매칭하는 capacity-aware progressive disclosure 첫 사례.
- [[slash-commands-vs-agent-skills]] — Custom Commands → Skills 통합 경위에서 progressive disclosure를 Skill의 결정적 우위 4가지 중 하나로 명시.
- [[anthropics-claude-cookbooks]] — `skills/` 노트북 3종이 progressive disclosure를 BI 도메인(financial dashboards) 사례로 완성. webapp-testing 스킬이 "DO NOT read scripts" 원칙 명시.
- [[openai-chatgpt-codex-guide]] — 송영옥, ChatGPT & Codex 실무 활용 가이드 6장(Custom GPTs 작성)에서 description "pushy" + supporting files lazy load 원칙을 사용자 측에서 적용하는 사례로 등장.

## 열린 질문

- LLM 에이전트의 4계층/5계층 변종이 추가로 등장할까? (예: `rules_500b` 마이크로 계층, 또는 `rules_dynamic` 작업 종류별 자동 압축)
- progressive disclosure를 **자동 압축 LLM 후처리기**로 구현할 수 있을까? (사람이 작성한 30K 본문을 1K/4K/10K 자동 생성)
- [[matechat]] SKILL chaining에서 SKILL이 다른 SKILL을 호출할 때 progressive disclosure가 어떻게 작동하나? (호출된 SKILL의 metadata만 로드 vs 본문까지 로드)
