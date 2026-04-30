---
title: Spec-Driven Development (SDD)
aliases:
- Spec-Driven Development
- SDD
- 스펙 기반 개발
type: concept
category: ai
tags:
- spec-driven-development
- sdd
- spec-kit
- prd
- prompt-engineering
- constitution
- harness
- methodology
related:
- '[[spec-kit]]'
- '[[github]]'
- '[[harness]]'
- '[[agent-patterns]]'
- '[[claude-code]]'
- '[[agent-skills]]'
- '[[context-engineering]]'
- '[[autonomous-research-loop]]'
- '[[github-spec-kit]]'
source_count: 1
observed_source_refs: 10
inbound_count: 36
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 15
---

# Spec-Driven Development (SDD)

## 정의

**사양(specification)이 코드를 생성하는 원본 자산**이라는 명제를 도구로 강제한 개발 메소드론. 전통 소프트웨어 개발에서 사양은 코드를 위한 비계(scaffolding)였다 — 한 번 코드를 짜고 나면 폐기됐다. SDD는 이를 뒤집어 **코드를 사양의 표현(expression)**으로 보고, "디버깅 = 사양 수정", "리팩토링 = 명료성 위한 재구조화", "새 기능 = 사양 재방문 후 재생성"으로 작업 단위를 재정의한다.

[[github]]의 [[spec-kit]]가 이 메소드론의 **표준 도구**. 9개 슬래시 명령으로 4단계(헌법 → 사양 → 계획 → 태스크) 워크플로우를 30+ AI 코딩 에이전트에 동일 설치한다.

## 왜 중요한가

세 가지 기술 트렌드의 교차점에서 등장:

1. **AI 자연어→코드 임계점 통과** — 사양이 충분히 정확하면 LLM이 동작 코드를 생성. PRD↔Code 사이의 "전통적 간극"이 메소드론 차원에서 닫힘
2. **소프트웨어 복잡도의 지수적 증가** — 수십 개 서비스·프레임워크·의존성을 정합성 있게 유지하려면 매뉴얼 관리 한계
3. **변경 속도 가속** — 피벗이 예외가 아니라 일상. 사양 변경 → 자동 재생성으로 변화를 disruption이 아닌 normal workflow로 흡수

위키 관점에서 SDD가 중요한 이유:

- **[[harness]] 개념의 반대 극단을 제공** — [[autoresearch]] (7KB program.md = 최소 하네스) ↔ SDD (9 슬래시 + 5 템플릿 + 9 Articles 헌법 = 완전 표준화 하네스). 양극이 박히면 하네스 스펙트럼이 완성됨
- **프롬프트 엔지니어링이 어디까지 갈 수 있는가의 답 중 하나** — 템플릿이 LLM을 "창의적 작가"에서 "규율 있는 사양 엔지니어"로 강제 변환
- **메소드론 자체가 결과물** — Microsoft "단일 운영체계", Anthropic "표준-구현 분리", Karpathy "최소 하네스"에 이어 GitHub의 차별 명제

## 핵심 내용

### 1. The Power Inversion (권력 역전)

`spec-driven.md`가 박은 SDD의 도덕적 명제:

| 전통 모델 | SDD 모델 |
|---------|---------|
| 코드가 진실의 원천 | 사양이 진실의 원천 |
| 사양은 구현을 안내 | 사양이 구현을 생성 |
| 디버깅 = 코드 수정 | 디버깅 = 사양 수정 |
| 리팩토링 = 코드 재구조화 | 리팩토링 = 사양 명료화 |
| 새 기능 = 코드 추가 | 새 기능 = 사양 재방문 → 재생성 |
| 유지보수 = 코드 진화 | 유지보수 = 사양 진화 |

자연어가 development의 lingua franca가 되고 코드는 last-mile.

### 2. 6 Core Principles

`spec-driven.md`의 "Core Principles" 섹션:

1. **Specifications as the Lingua Franca** — 사양이 1차 산출물, 코드는 표현
2. **Executable Specifications** — 사양은 동작 시스템을 생성할 만큼 정확·완전·명료해야
3. **Continuous Refinement** — 일관성 검증은 1회 게이트가 아닌 지속적 프로세스
4. **Research-Driven Context** — 연구 에이전트가 라이브러리·성능·조직 제약을 사양 과정 내내 조사
5. **Bidirectional Feedback** — 운영 데이터(메트릭·인시던트)가 사양 진화에 반영
6. **Branching for Exploration** — 같은 사양에서 다른 최적화 목표(성능·유지보수성·UX·비용)로 다중 구현 분기

### 3. SDD의 4 + 5 단계 (spec-kit 표현)

| 핵심 4단계 | 명령 | 산출 |
|----------|------|------|
| 1. 헌법 수립 | `/speckit.constitution` | `.specify/memory/constitution.md` (9 Articles) |
| 2. 사양 작성 | `/speckit.specify` | `specs/[NNN-branch]/spec.md` |
| 3. 계획 수립 | `/speckit.plan` | `plan.md` + `research.md` + `data-model.md` + `contracts/` |
| 4. 태스크 분해 | `/speckit.tasks` | `tasks.md` (`[P]` 병렬 마커) |
| 5. 실행 | `/speckit.implement` | TDD 코드 + 테스트 |

| 보조 4단계 | 명령 | 역할 |
|----------|------|------|
| 마커 해소 | `/speckit.clarify` | `[NEEDS CLARIFICATION]` 사용자 질의 |
| 일관성 분석 | `/speckit.analyze` | spec/plan/tasks 교차 검증 |
| 체크리스트 생성 | `/speckit.checklist` | 도메인별 (보안·접근성·성능…) |
| 발행 | `/speckit.taskstoissues` | GitHub Issues 자동 생성 |

### 4. 9 Articles Constitution — 불변 아키텍처 DNA

| Article | 강제 사항 |
|---------|----------|
| **I. Library-First** | 모든 기능은 standalone 라이브러리로 시작 |
| **II. CLI Interface Mandate** | 모든 라이브러리는 CLI 노출 (stdin/args/files → stdout/JSON) |
| **III. Test-First Imperative** | NON-NEGOTIABLE — Red 단계 확인 전 어떤 구현 코드도 작성 금지 |
| **VII. Simplicity** | 초기 구현은 ≤3 프로젝트 |
| **VIII. Anti-Abstraction** | 프레임워크 직접 사용 (래핑 금지), 단일 모델 표현 |
| **IX. Integration-First Testing** | 실제 DB·서비스 사용, mock 회피, contract test 의무 |

**Constitutional Evolution**: 변경 시 (a) rationale 명시, (b) 유지보수자 승인, (c) 후방 호환 평가가 의무.

위키 관점: Article III(Test-First) + Article VII(Simplicity) + Article I(Library-First)는 게임 데이터 BI에 즉시 ROI 있는 원칙. 회사 프로젝트 코딩 스타일·CLAUDE.md에 이 3개만이라도 차용하면 SDD의 80%.

### 5. Template-Driven Quality — 7가지 LLM 출력 제약 메커니즘

`spec-driven.md`가 명시적으로 박은 통찰: **템플릿이 곧 LLM 출력 제약 메커니즘**.

1. **조기 구현 디테일 차단** — `✅ WHAT/WHY · ❌ tech stack/APIs/code structure`
2. **불확실성 마커 의무** — `[NEEDS CLARIFICATION: 구체적 질문]` 강제
3. **체크리스트 = 단위 테스트** — 사양 자체에 `Requirement Completeness` 체크박스 박힘
4. **Constitutional Compliance Gates** — Phase -1 Gates가 Article별로 체크
5. **계층적 디테일 관리** — 본문은 high-level, 코드 샘플은 `implementation-details/` 분리
6. **테스트 우선 강제** — 파일 생성 순서: `contracts/ → test files → source files`
7. **추측 기능 차단** — `No speculative or "might need" features`

이 7개 누적이 LLM을 "**창의적 작가 → 규율 있는 사양 엔지니어**"로 강제 전환.

### 6. SDD가 사용하는 5 패턴 합성

[[agent-patterns]]의 5 패턴이 SDD 워크플로우에 어떻게 박혀 있나:

| 패턴 | SDD에서의 사용 |
|------|--------------|
| **Prompt Chaining** | 4 + 5단계 정적 분해 (constitution → specify → plan → tasks → implement) |
| **Evaluator-Optimizer** | `/speckit.clarify`(사용자 = evaluator), `/speckit.analyze`(LLM = evaluator) |
| **Parallelization** | `tasks.md`의 `[P]` 마커가 독립 태스크 병렬 처리 |
| **Routing** | (커뮤니티 확장 "Agent Assign") — 태스크별 전문 에이전트 라우팅 |
| **Orchestrator-Workers** | 복잡 spec에서 plan을 동적 결정 |

즉 SDD는 **5 패턴을 사전 합성한 메소드론**. 사용자가 직접 패턴 선택할 필요 없이 단계만 따라가면 됨.

### 7. 3가지 개발 단계

| 단계 | 초점 | 주요 활동 |
|-----|------|---------|
| **0-to-1 (Greenfield)** | 처음부터 생성 | 고수준 요구사항 → 사양 → 계획 → 프로덕션 앱 |
| **Creative Exploration** | 병렬 구현 | 다양한 솔루션, 다중 기술 스택·아키텍처, UX 패턴 실험 |
| **Iterative Enhancement (Brownfield)** | 기존 시스템 현대화 | 기능 반복 추가, 레거시 현대화, 프로세스 적응 |

## 실전 적용

### A. 위키 자체에 spec-kit 적용 (메타)

`templates/commands/`에 LLM 지침서로 4개 명령 추가:

- `/wiki-ingest` — 새 raw source를 받아 wiki/sources/ 요약 생성 (CLAUDE.md "수집 워크플로우"의 코드화)
- `/wiki-lint` — 깨진 링크·고아 페이지·모순 검출 (CLAUDE.md "점검 워크플로우"의 코드화)
- `/wiki-synthesize` — 다중 source를 종합한 syntheses 페이지 작성
- `/wiki-query` — 위키 조회 + 인용 (현재 `~/.claude/skills/wiki/SKILL.md`와 통합 검토)

각 명령은 `templates/commands/specify.md` 스타일의 LLM 지침서 — frontmatter + body로 워크플로우를 강제.

### B. 회사 BI에 SDD 시범 도입

새 지표 정의 / 새 대시보드 작성 같은 **0→1 작업**에 SDD 시범 적용:

1. `/speckit.constitution` — BI 운영 원칙 (정합성 우선, 데이터 라인age, 캐시 정책)
2. `/speckit.specify` — 지표 정의 PRD (HOW 금지: BigQuery·차트 라이브러리 언급 안 함)
3. `/speckit.clarify` — `[NEEDS CLARIFICATION: 집계 단위? 일별/주별? 시간대?]`
4. `/speckit.plan` — BigQuery 슬롯 사용·재집계 정책·캐시 TTL 결정
5. `/speckit.tasks` — 쿼리 작성·테스트 데이터·차트 컴포넌트로 분해

실패해도 "BI 작업에 SDD가 적합한가" 데이터 확보. **vibe coding과 SDD의 ROI 경계**가 BI 도메인에서 어디에 있는지가 후속 탐구 대상.

### C. 9 Articles만 차용

전체 spec-kit 도입이 부담이면 **9 Articles 헌법만** 회사 프로젝트에 차용:

- Article I (Library-First) — 컴투스플랫폼 모듈을 standalone 패키지로 분리
- Article III (Test-First) — TDD를 진짜 Red→Green→Refactor 강제
- Article VII (Simplicity) — 프로젝트 ≤3 제한, future-proofing 금지
- Article IX (Integration-First) — Mock보다 실제 DB·서비스로 테스트

이 4개만 적용해도 코드 품질 80% 개선 기대 — 프롬프트 엔지니어링 없이도 인간 개발자에게 직접 효용.

### D. 개인 비서 AI에 적용

[[anthropics-claude-cookbooks]]의 `01_The_chief_of_staff_agent.ipynb` + spec-kit 합성:

- **Constitution**: 비서의 운영 원칙 (응답 톤·사생활 경계·자동 실행 한계)
- `specs/`: 사용 시나리오별 spec.md 누적 (이메일 분류·일정 조율·문서 요약)
- 각 시나리오마다 헌법 준수 확인 → long-term consistency 확보

SDD는 단발 명령 모델보다 **비서의 일관성**에 유리. CLAUDE.md 1장으로는 부족한 "구체적 시나리오별 정책"이 specs/에 누적됨.

## 안티패턴

| 패턴 | 문제 | 회피 |
|------|------|------|
| 모든 작업에 SDD 강제 적용 | 5분짜리 버그 픽스에 헌법·사양·계획은 과잉 | 0→1 작업과 안정성 임계 작업에만 |
| `/speckit.specify` 단계에서 기술 스택 언급 | 사양이 구현에 종속 | "WHAT/WHY only" 원칙 강제, 위반 시 spec.md 다시 |
| `[NEEDS CLARIFICATION]` 마커를 LLM이 추측으로 채움 | 잘못된 가정이 plan/tasks까지 전파 | `/speckit.clarify`를 반드시 거침 |
| 9 Articles를 단순히 복붙해 둠 | 헌법이 죽은 문서가 됨 | Article별 Phase-1 Gate를 plan-template에 박아 매번 검증 |
| spec.md를 한 번 쓰고 끝 | "Living Documentation" 원칙 위반 | 운영 메트릭·인시던트 → 사양 갱신 루프 |
| Vibe coding의 자유도를 SDD가 모두 죽임 | 창의적 탐색 단계 봉쇄 | "Creative Exploration" 단계에서 다중 plan 분기 사용 |

## 관련 개념

- [[spec-kit]]: SDD를 강제하는 도구 (메소드론 자체와 도구의 관계)
- [[github]]: SDD 메소드론을 표준화한 조직
- [[harness]]: SDD = 메타-하네스 (하네스 스펙트럼의 표준화 극단)
- [[agent-patterns]]: SDD가 5 패턴을 사전 합성한 결과물
- [[autonomous-research-loop]]: SDD의 반대 — 사양보다 메트릭 객관성과 시간 예산이 통제
- [[context-engineering]]: spec.md/plan.md/constitution.md 분리 보관 = "specification으로서의 컨텍스트 엔지니어링"
- [[claude-code]] / [[agent-skills]]: SDD 9개 명령의 배포 채널 (slash command + Codex skills)

## 출처

- [[github-spec-kit]] — spec-kit `spec-driven.md` 412줄이 SDD 메소드론의 정통 정의 + `templates/` 5종 + `templates/commands/` 9종이 메소드론의 코드화

## 열린 질문

- **SDD vs vibe coding의 ROI 경계는 어디인가?** GitHub은 vibe coding을 명시적 안티-패턴으로 박았지만, 5분 prototype·창의 탐색 단계에는 SDD가 과잉. 작업 유형별 ROI 매트릭스 미정.
- **9 Articles의 보편성?** Library-First·CLI Mandate가 모든 도메인에 적용되나? 프론트엔드 React 컴포넌트는 Article II(CLI 노출) 어떻게 적용?
- **Living Documentation의 운영 비용?** 운영 메트릭 → 사양 자동 갱신 루프가 실제로 돌아가는 사례가 spec-kit 외부에 있나? 메트릭→사양 변환을 LLM이 하나, 사람이 하나?
- **다중 spec.md 사이의 정합성?** specs/001-X/, specs/002-Y/, specs/003-Z/가 누적될 때 cross-spec 모순은 어떻게 검출? `/speckit.analyze`가 단일 spec 내부 일관성만 보는데, 다중 spec 사이는?
- **SDD가 작은 팀에 ROI 있나?** GitHub 같은 대조직의 메소드론을 1-3인 팀에 적용하면 오버헤드가 본질을 압도하나?
- **Constitution amendment의 빈도?** "불변" 원칙이라지만 실제로 얼마나 자주 수정되는가? amendment process가 실제 spec-kit 운영에서 얼마나 쓰이고 있나?
