---
title: 거버넌스 6축 비교 — Constitution · SKILL.md · SLEP · PDEP · AGENTS.md · PLANS.md
aliases:
- governance-axis-comparison
- 거버넌스 6축 비교
- 거버넌스 비교
- governance comparison
type: synthesis
category: comparison
tags:
- governance
- constitution
- agent-skills
- slep
- pdep
- agents-md
- exec-plans
- plans-md
- spec-driven-development
sources:
- '[[github-spec-kit]]'
- '[[anthropics-skills]]'
- '[[scikit-learn-scikit-learn]]'
- '[[pandas-dev-pandas]]'
- '[[openai-openai-cookbook]]'
- '[[openai-openai-agents-python]]'
related:
- '[[agent-skills]]'
- '[[harness]]'
- '[[spec-driven-development]]'
- '[[pdep]]'
- '[[bdfl]]'
- '[[vendor-neutral]]'
- '[[progressive-disclosure]]'
- '[[agent-stack-evolution]]'
- '[[matechat]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-stack-guide]]'
created: 2026-04-30
updated: 2026-04-30
inbound_count: 13
cited_by_count: 12
---

# 거버넌스 6축 비교 — Constitution · SKILL.md · SLEP · PDEP · AGENTS.md · PLANS.md

## 한줄 요약

> LLM 시대 OSS·메소드론에서 등장한 6가지 거버넌스 모델을 단일 매트릭스로 비교. **시간 단위(분~19년)**, **산출물 형태(메모/패키지/제안서/운영노트/ExecPlan)**, **변경 비용**의 3축에서 각자 다른 trade-off를 만든다. owner 입장에서 **회사 BI / 사이드 프로젝트 / 위키 자체**에 어느 거버넌스를 차용할지의 의사결정 입력.

## 왜 6축 비교가 필요한가

[[openai-openai-cookbook]] 후속 탐구 (b)가 명시: "**거버넌스 6축 비교 — Constitution / SKILL.md / SLEP / PDEP / AGENTS.md(살아있는) / PLANS.md(ExecPlan)** — 6 거버넌스의 시간 단위 / 산출물 / 검증 메커니즘 / 변경 비용 매트릭스." 위키의 [[harness]] · [[agent-skills]] · [[pdep]] · [[spec-driven-development]] 등 여러 페이지에 분산된 거버넌스 개념이 단일 비교 frame이 없었음.

## 6축 비교 매트릭스

| # | 거버넌스 | 출처 | 대상 | 시간 단위 | 산출물 | 변경 비용 |
|---|---|---|---|---|---|---|
| 1 | **Constitution** | [[github-spec-kit]] | 다중 에이전트 메소드론 강제 | 시간~일 | `constitution.md` (9 Articles) + `spec.md` + `plan.md` + `tasks.md` | 중간 (다중 명령 슬래시 통일) |
| 2 | **SKILL.md** | [[anthropics-skills]] | 자동 호출 LLM 에이전트 작업 패키지 | 단발 (트리거 시) | `SKILL.md` + scripts/references/assets | 낮음 (frontmatter만 갱신) |
| 3 | **SLEP** | [[scikit-learn-scikit-learn]] | API 컨트랙트 영구성 | **19년 누적** | SLEP 문서 + 1주+ 토론 + 2/3 다수결 | 매우 높음 (breaking change 강력 차단) |
| 4 | **PDEP** | [[pandas-dev-pandas]] | 분산 의사결정 + 로드맵 | 분기~연 | PDEP 문서 (RFC 형식) | 높음 (커뮤니티 합의 필수) |
| 5 | **AGENTS.md (살아있는)** | [[openai-openai-cookbook]] | LLM 협업 가이드 + 운영 발견 누적 | 즉시 (Recent Learnings 추가) | `AGENTS.md` + Recent Learnings 섹션 | 매우 낮음 (1줄 추가) |
| 6 | **PLANS.md (ExecPlan)** | [[openai-openai-cookbook]], [[openai-openai-agents-python]] | 단일 LLM 7시간+ 작업 living document | 시간 (작업 수명) | `PLANS.md` (NON-NEGOTIABLE 4 + Skeleton) | 매우 낮음 (작업 진행 중 갱신) |

## 6축의 본질적 분기 — 정적 vs 살아있는

처음 4축(Constitution·SKILL.md·SLEP·PDEP)은 **정적 거버넌스**: 한 번 박힌 가이드/제안/계약은 거버넌스 의식(다수결·검토 등)을 통과해야 변경된다. 5~6축(AGENTS.md 살아있는·PLANS.md)은 **살아있는 거버넌스**: 작업 진행 중 발견을 즉시 누적하고, 계약은 실시간으로 진화한다.

| 축 | 정적 / 살아있는 | 핵심 메커니즘 |
|---|---|---|
| Constitution | 정적 | 메소드론 강제 (Phase -1 Gates, Constitutional Compliance) |
| SKILL.md | 정적 | 자동 호출 + progressive disclosure |
| SLEP | 정적 | 1주+ 토론 + 2/3 다수결 |
| PDEP | 정적 | RFC 검토 + 커뮤니티 합의 |
| AGENTS.md (살아있는) | **살아있는** | Recent Learnings 누적 (현상 → 대응 → 이유) |
| PLANS.md | **살아있는** | NON-NEGOTIABLE 4 + Living Sections (Progress, Surprises, Decision Log, Outcomes) |

이 분기점이 [[openai-openai-cookbook]] 발견의 핵심 — 1~6 진화의 진짜 변곡점.

## 시간 단위 스펙트럼

```
즉시 ───── 시간 ───── 일 ───── 주 ───── 분기 ───── 연 ───── 19년
  │           │         │        │         │         │           │
AGENTS.md   PLANS.md  Constitution  PDEP   PDEP    PDEP        SLEP
(Recent)   (ExecPlan) (constitution.md)
SKILL.md(트리거 시 단발)
```

- **즉시 ~ 시간**: Constitution / SKILL.md / AGENTS.md(살아있는) / PLANS.md — LLM 에이전트 작업 단위
- **주 ~ 분기**: PDEP — 라이브러리 표준 변경 단위
- **연 ~ 19년**: SLEP — API 컨트랙트 영구성 단위

owner 입장에서 **시간 단위가 자기 작업 수명과 매칭되는 거버넌스 선택**이 ROI 결정.

## 검증 메커니즘 비교

| 거버넌스 | 검증 메커니즘 | 강제력 |
|---|---|---|
| Constitution | Phase -1 Gates, `[NEEDS CLARIFICATION]` 마커, TDD Red 단계 강제 | 강함 (메소드론 자동) |
| SKILL.md | description 기반 자동 호출 / 20개 trigger 검증 쿼리 (skill-creator) | 약함 (under-trigger 위험) |
| SLEP | `pytest sklearn` 공통 테스트 헬퍼가 컨트랙트 위반 자동 검출 | 매우 강함 (테스트 통합) |
| PDEP | RFC 검토 + community discussion + 인계 메타-필드 (e.g., `pdep-13` deprecation policy) | 중간 (휴먼 검토) |
| AGENTS.md (살아있는) | (자동 검증 미공개, 휴먼 누적) | 약함 (Recent Learnings는 휴먼 큐레이션) |
| PLANS.md | Explicit acceptance (행동/명령/관찰 가능 출력) | 중간 (NON-NEGOTIABLE 4 자체검증) |

## owner 차용 매트릭스

| 적용 영역 | 우선 차용 거버넌스 | 이유 |
|---|---|---|
| **[[matechat]] 39 SKILL 운영** | **SKILL.md** | 이미 채택, 자동 호출 + progressive disclosure 적용 중 |
| **[[c2spf-analytics]] BI 분기 분석** | **PLANS.md (ExecPlan)** | 1 분석가 + LLM 7시간+ 단일 작업이 분기 분석 코호트 작업과 매핑 (참조: [[openai-openai-agents-python]] 가설 2) |
| **위키 운영 가이드** | **AGENTS.md (살아있는)** | CLAUDE.md를 AGENTS.md로 vendor-neutral화 + Recent Learnings 섹션 추가로 ingest 함정·솔루션 누적 |
| **회사 BI 외부 API 호환성** | **SLEP-style** | 외부 소비자 보호. dataclass·Pydantic 모델 필드 순서를 호환성 계약으로 격상 (참조: [[openai-openai-agents-python]] Public API Positional Compatibility) |
| **회사 BI 신규 지표 정의 거버넌스** | **PDEP-style** | RFC 검토 + 합의 필수, 광범위 영향 작업에 적합 |
| **분석 작업 메소드론 통일** | **Constitution / SDD** | spec → plan → tasks → implement 4단계가 분석 워크플로우 표준화에 직접 매핑 |

## 정적·살아있는 혼합 모델 — 향후 가능성

[[openai-openai-cookbook]]이 **AGENTS.md 안에 7개 정적 섹션 + Recent Learnings 1 살아있는 섹션**을 두는 것이 본질적 혼합. 이는 정적·살아있는의 **층위 분리** — 표준 컨벤션은 정적으로, 운영 발견은 살아있게.

owner 위키에 차용 시:
- `CLAUDE.md` (현재) → 정적 부분 (CLAUDE.md 또는 AGENTS.md)
- 새 `RECENT_LEARNINGS.md` (또는 frontmatter 섹션) → 살아있는 부분
- 둘이 합쳐 단일 거버넌스 진실원

## 6축이 모두 다루지 못하는 영역

- **데이터 거버넌스**: 6축 모두 코드/메소드론 거버넌스. BI 데이터 자체의 schema 변경·KPI 정의 변경 거버넌스는 별도 (PDEP가 가장 가깝지만 데이터 도메인 미공개).
- **퍼포먼스 거버넌스**: 모델 성능 회귀 차단은 [[autonomous-research-loop]]의 `val_bpb` 메트릭 게임이 더 가까움. 6축은 거버넌스 자체를 메트릭으로 강제하지 않음.
- **보안 거버넌스**: API 키 관리·secret rotation 같은 영역은 6축 외부.

→ owner 위키는 6축 + 별도 (a) 데이터 schema 거버넌스 + (b) 메트릭 거버넌스를 결합해야 풀스택.

## 5축 진화 = 1축~5축 → 6축 합류

본 거버넌스 6축은 [[harness]] 본문의 5축 (autoresearch / spec-kit / scikit-learn / flutter / anthropics-skills)에 OpenAI cookbook PLANS.md를 6축으로 합류한 결과. [[harness]] 페이지가 본 비교의 source. 본 synthesis는 거버넌스 단위에 집중해 시간 단위·검증 메커니즘 매트릭스를 명시.

## 열린 질문

- **혼합 모델이 표준이 될까?** 정적 SKILL.md + 살아있는 Recent Learnings의 owner 위키 차용이 ROI를 정당화할 시점은?
- **회사 BI에 6축 중 몇 개를 동시 도입 가능?** 가설: 3개 (PLANS.md / SKILL.md / AGENTS.md 살아있는). SLEP/PDEP은 외부 API에만, Constitution은 분석 작업에만.
- **거버넌스 자체의 거버넌스**: 6축이 모두 자기 변경에는 어떤 거버넌스를 쓰는가? (메타-거버넌스 회귀)

## 메모

- 본 synthesis는 [[harness]] · [[agent-skills]] · [[pdep]] · [[spec-driven-development]] · [[agent-stack-evolution]]의 부분 합집합. 단일 비교 frame이 빠진 자리를 채움.
- 6축 모두 owner의 직접 영향권 (matechat, c2spf, 위키)에 매핑 가능.
- 6개월 후 재검증 시 7~8축 진화 가능성 (예: Self-modifying ExecPlan, Multi-agent constitutional compliance 등).
