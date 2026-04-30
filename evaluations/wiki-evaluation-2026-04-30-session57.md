---
title: "llm-wiki 56회차 종합 평가 보고서"
type: evaluation
session: 56
session_evaluated_at: 56
report_for_session: 57
date: 2026-04-30
evaluator: "Claude Code (4축 병렬 sub-agent)"
overall_score: 87.1
axes:
  A_information_quality: 89.8
  B_structural_connectivity: 88.5
  C_obsidian_vault: 79.0
  D_rag_utility: 91.0
prior_evaluations:
  - session: 54
    self_score: 84.5
    external_codex_score: 88
related_wiki_pages:
  - "[[index]]"
  - "[[tag-vocabulary-audit-2026-04-29]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[seokgeun-stack-guide]]"
---

# llm-wiki 56회차 종합 평가 보고서 (2026-04-30)

> 본 문서는 위키 콘텐츠가 아닌 **위키 자체에 대한 메타-평가 문서**다. `wiki/`(LLM 관리 콘텐츠)와 분리해 `evaluations/` 경로에 저장한다.

## 평가 프레임워크

owner(김석근)의 위키 이중 목적 — ① Obsidian 볼트(개인 지식 관리) + ② RAG 컨텍스트 소스(LLM 작업 보조) — 를 분리해 4축 병렬 sub-agent가 **독립** 평가했다 (점수 공유·교차 영향 차단 / 54회차 검증된 프레임 재사용).

| 축 | 평가 차원 | 점수 |
|---|---|---:|
| **A. 정보 품질** | 정확성·깊이·도메인 커버리지·시의성·독창성·자가 일관성·의사결정 가치 (7기준) | **89.8 / 100** |
| **B. 구조 연결성** | hub-spoke 균형·교차 축 edge·bidirectional 추적·깊이 균형·중심성 분포·진입점·redirect (7기준) | **88.5 / 100** |
| **C. Obsidian 볼트 사용성** | alias 커버리지·tag vocabulary·Graph view·백링크·구조·검색·모바일 (7기준) | **79.0 / 100** |
| **D. RAG 활용성** | 자기서술성·메타데이터·청크 적합성·citation chain·메타 격리·출처·답변 정책 실행성 (7기준) | **91.0 / 100** |
| **종합 (산술 평균)** | | **87.1 / 100** |

> 54회차 자체평가 84.5 / Codex 외부평가 88 대비 자체 평가 +2.6p 상승 — 51·52·53·55회차 P0/P1 backlog 8건 반영의 ROI가 실제 점수로 반영됨.

---

## 축별 평가 요약

### A. 정보 품질 (89.8) — 횡단 종합과 재현 가능 정량의 결합

**강점**: 단일 도메인 OSS 문서가 만들 수 없는 횡단 종합 5종 (OSS 거버넌스 10모델 카탈로그·AGENTS.md 13단계 진화·dataframe 18년 진화사·5축 harness 거버넌스 비교·6×N agent framework 매트릭스). `portfolio.md` Layer 3 STAR 표가 모든 정량 주장에 재현 명령(`git log`·`find`·GCP `evaluation_dashboard`)을 박은 것이 백미.

**약점**: 5축 비중 44.6%로 LLM 인프라 메타 layer가 비대 / owner 일상 카테고리(가족·생활·독서·자기개발) 거의 부재 — `parental-leave-2026-operating-plan` 1건뿐. CLAUDE.md 카테고리 가이드와 실제 페이지 구현 불일치.

### B. 구조 연결성 (88.5) — 그래프 골격은 견고, 측정 인공물이 약점

**강점**: 5축 hub-to-hub 25/25 비대각 셀 모두 edge ≥ 6 (단절 0). lint 12종 무결점 + redirect 처리 모범(`mate-chat`).

**약점**: 비-메타 194 페이지의 `cited_by_count` 분포가 **계단형 양극화** (0: 87건 / 1-5: 0건 / 6+: 107건). 87건 0인 이유는 `wiki-lint.py --update` 자동 갱신 대상이 source + 5축 hub 11개로 한정된 측정 갭. 51회차 RAG 답변 정책 §1 권장 필드(`cited_by_count`)가 콘텐츠 페이지 절반에 의미 없는 값.

### C. Obsidian 볼트 사용성 (79.0) — hub층은 모범, 일반층이 못 따라옴

**4축 중 최저 점수.** 5축 hub만 보면 A급(95점), 위키 전체 vault로 보면 B+. 격차의 원인:
- alias 침투율 31/199 (15.6%) — concepts 12.5%·entities 18.4%
- tag vocabulary 한·영 의도 중복 7쌍 미해소 (`agent`/`에이전트` 16:16 등 — 56회차 audit가 진단만 하고 정리 미완)
- `.obsidian/graph.json` `colorGroups: []` — 5축 시각 구분 없음
- `cited_by_count` 정수 캐시 9페이지만 적용

### D. RAG 활용성 (91.0) — 4축 중 최강, 51·47·46·43회차 누적 인프라의 결과

**강점**: 메타 페이지 격리 100% (lint check #10 0건) / source 페이지 cited_by 양방향 100% (47회차 인프라) / 청크 적합성 97.5% (50~500줄 권장 범위). 4 RAG 시뮬레이션 질의 모두 ★★★★ 이상 — 51회차 답변 정책 5개 규칙이 wiki 구조 자체로 강제 가능.

**약점**: `cited_by_count`가 syntheses 17개·entities 일부에 미적용 (53회차 도입 직후) / `llm-infra-meta-cluster`·`portfolio` 두 5축 hub에 `verification_required` 누락.

---

## 교차 축 공통 발견 (다중 평가자가 동일 페이지·문제 지적)

> 한 축에서만 발견된 약점은 우선순위 낮음. **여러 평가자가 동일 결함을 독립 발견**한 항목이 진짜 우선순위 — 아래 7건이 합집합.

| # | 결함 | 발견 축 | 심각도 | 처리 위치 |
|---|---|---|---|---|
| **F1** | `agent-skills.md` line 277-278 byte-for-byte 중복 단락 (1,800자) | A | High | P0 |
| **F2** | `llm-infra-meta-cluster.md` frontmatter `sources_count` 오타 (단복수 혼용 — 다른 페이지는 `source_count`) | A, C | High | P0 |
| **F3** | `cited_by_count` 자동 갱신 대상 협소 (synthesis 17개 + entity 일부 미적용) → `cited_by_count=0` 87건 측정 갭 → 51회차 RAG 정책 §1 수치 비교 일관 적용 불가 | B, C, D | **Critical** | P0 |
| **F4** | `llm-infra-meta-cluster` 5축 cap-hub인데 `verification_required` 누락 (OSS 거버넌스 변동성 가장 높음) + `inbound_count: 0` 측정 누락 | B, D | High | P0 |
| **F5** | 5축 비중 44.6% + 1·3축 얇음 (1축 11.6% / 3축 9.2%) — owner 일상 축 부재로 5축 메타 layer 비대 인상 | A, B | Medium | P1 |
| **F6** | 3축 단일 hub(`seokgeun-stack-guide` 인바운드 155) sub-hub 부재 — 32 OSS를 6분류로 나누지만 분류별 1-hop 진입점 없음 | A, B | Medium | P1 |
| **F7** | 한·영 tag 중복 7쌍 (`agent`/`에이전트`, `백엔드`/`backend`, `포트폴리오`/`portfolio`, `하네스`/`harness`, `matechat`/`mate-chat`/`메이트챗`, `석근`/`seokgeun-kim`, `데이터분석`/`data-analysis`) — 정책 "병기"가 실제로는 "양쪽 자라남"이 됨 | C (56회차 audit 진단 미완) | High | P1 |

---

## 통합 P0/P1/P2 백로그 (57회차 후속)

### P0 — 즉시 수정 (5건)

1. **`wiki/concepts/agent-skills.md` line 277-278 중복 단락 제거** (5분, 정보 품질 +2)
2. **`wiki/syntheses/llm-infra-meta-cluster.md` frontmatter 정정**:
   - `sources_count` → `source_count` (단복수 통일)
   - `verification_required: true` + `last_verified: 2026-04-30` + `verification_notes: "10개 OSS 거버넌스 변동 — 분기별 재카탈로그"` 추가
   - `inbound_count` 자동 갱신 누락 원인 조사
3. **`scripts/wiki-lint.py --update` 자동 갱신 범위 확장** — `cited_by_count` 갱신 대상을 source + 5축 hub 11개 → **모든 비-메타 페이지(synthesis·entity·concept 포함)**로. 측정 갭 87건 해소 → RAG 답변 정책 §1 일관 적용 가능. (Critical)
4. **`.obsidian/graph.json` `colorGroups` 5축 추가** — 4줄 JSON: `tag:#포트폴리오 OR path:portfolio*`, `tag:#matechat`, `tag:#agent-skills OR tag:#harness OR tag:#mcp OR tag:#claude-code` 등으로 5축 시각 구분.
5. **lint check #14 신설**: 비-메타 페이지에서 `cited_by_count` 누락 시 정보 보고 (53회차 정책 정합화).

### P1 — 다음 1~2회차 (5건)

6. **한·영 tag 중복 7쌍 canonical 결정** — 56회차 audit synthesis(`tag-vocabulary-audit-2026-04-29.md`)에 결정 기록 + bulk 정정.
7. **3축 sub-hub 3개 신설** — `backend-stack-sub-hub`, `dataframe-stack-sub-hub`, `agent-stack-sub-hub`. seokgeun-stack-guide 단일 페이지 155 인바운드를 4 hub로 분산 (60·40·30·25 목표).
8. **개인·생활 축 보강** (1축) — `reading-log-2026` synthesis, `health-routine` entity 등 2~3개로 owner 일상 비중 회복.
9. **상위 빈도 concept 10개 alias 추가** — `python`, `fastapi`, `pandas`, `flutter`, `openai`, `claude-code`, `langchain`, `langgraph`, `pydantic`, `bigquery`. 약 30분.
10. **`portfolio.md` `verification_required` 추가** — 5축 hub 일관성 차원.

### P2 — 장기 (4건)

11. **영양실조 entity 19개에 owner 컨텍스트 callout** — `tanstack`·`radix-ui`·`vercel`·`memex` 등 50~62줄 페이지에 `> [!note]` 한 줄.
12. **장문 source progressive disclosure** — `flutter-flutter`(421줄)·`openai-openai-agents-python`(364줄)·`seokgeun-mate-chat`(317줄)에 Top 30줄 요약 + 본문 fold.
13. **synthesis 22개 alias 일괄 침투** — hub 외 9개 미적용 페이지 보강.
14. **Bases view 신설** — `wiki/_bases/hubs.base` 또는 frontmatter base로 "5축 hub" / "변동성 entity (last_verified < 90d)" / "redirect 격리" 3개 view 자동화.

---

## 한 줄 종합 평가

**87.1 / 100 — RAG 활용성(91)이 4축 중 최강이며 51회차 답변 정책 5개 규칙을 위키 구조 자체로 강제 가능한 수준에 도달했으나, Obsidian 볼트(79)는 5축 hub층(95급)과 일반 페이지층의 격차로 평균이 80을 못 넘는 상태. 핵심 병목은 (1) `cited_by_count` 측정 갭 87건 (Critical) (2) 5축 비대로 인한 owner 일상 축 부재 (3) 3축 단일 hub 비대 — 셋 다 인프라적으로 해결 가능하며 57회차 P0 5건만 처리해도 89~90점대 진입.**
