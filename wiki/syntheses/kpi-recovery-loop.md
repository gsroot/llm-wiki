---
title: KPI 측정값 회수 루프 — 의사결정 → 실측 → 위키 갱신 SOP
type: synthesis
category: operating-log
aliases:
- KPI 회수 루프
- kpi-recovery-loop
- 측정값 회수
- 의사결정 회수 SOP
tags:
- kpi
- matechat
- c2spf
sources:
- '[[seokgeun-kim-profile-2026]]'
- '[[mate-chat-project-wiki-2026]]'
related:
- '[[seokgeun-kim]]'
- '[[seokgeun-operating-profile-2026]]'
- '[[parental-leave-2026-operating-plan]]'
- '[[matechat-30day-validation-loop]]'
- '[[c2spf-ai-agent-adoption-candidates]]'
- '[[matechat]]'
- '[[c2spf-analytics]]'
- '[[portfolio]]'
created: 2026-04-29
updated: 2026-04-29
verification_required: true
last_verified: 2026-04-29
verification_notes: 본 SOP 자체 준수 여부를 분기별 회고에서 점검. 측정값 누락된 KPI 1건이라도 있으면 SOP 결함.
cited_by_count: 9
inbound_count: 14
---

# KPI 측정값 회수 루프 — 의사결정 → 실측 → 위키 갱신 SOP

> [!important] 메타 SOP — "사고 도구"가 되기 위한 마지막 적자
> 신설 (Codex 권고 P1 + 자체 평가 A의 결정적 발견). 평가에서 **"위키가 다음 의사결정 입력은 정리하나 지난 의사결정의 결과를 회수해 가설을 갱신하는 루프가 비어 있다"**가 핵심 결손으로 식별됨. 본 페이지는 그 루프를 메타 SOP로 정형화.
> 
> 한국어 표기: **KPI 측정값 회수 루프** 또는 **회수 SOP**.

## 언제 읽어야 하는가

- "왜 위키에 가설은 많은데 실측이 없나?" — 결손 진단 + 본 SOP의 존재 이유.
- "회수 누락을 어떻게 자동 감지하나?" — verification_required + last_verified 활용법.
- "어떤 회수 단위가 적절한가?" — 단기·중기·장기 회수 단위 표.
- "회수 결과를 어디에 갱신하나?" — 갱신 대상 파일 + 회고 로그 위치.

## 1. 결손 진단

종합 평가 보고서 핵심 발견:

> "MateChat 자작 SKILL 9개가 c2spf로 차용됐다는 가설이 박힌 후 시점까지 **실제 1개도 적용된 흔적이 없다**. KPI(D30 8% / 인간-인간 5회)도 측정값이 없다. 즉 위키가 '다음 의사결정의 입력'은 잘 정리하지만, '지난 의사결정의 결과'를 회수해서 가설을 갱신하는 루프가 비어 있다."

이 결손이 위키를 "잘 만든 사전 + 사고 도구 절반" 단계에서 멈추게 함. 본 SOP는 그 멈춤을 푼다.

## 2. 회수 의무 4가지 단계 (verification_required: true 자동화)

`verification_required: true` 필드를 가진 페이지는 다음 단계를 따라야 한다:

```
페이지 생성 시점:        "측정값 회수 일정 박힘"
└─ verification_notes 에 "무엇을 / 언제 / 어떻게" 명시 필수

회수 일정 도래 시점:     "측정값 입력 또는 회수 불가 사유 박힘"
└─ last_verified 갱신 + 결과 표 채움
└─ 회수 불가 사유는 "왜 미측정인지" 명시 (ex: "출시 지연", "데이터 접근 차단")

분기 회고 시점:           "회수율 점검"
└─ 모든 verification_required:true 페이지 중 last_verified 90일 초과 비율 측정
└─ wiki-lint check 7로 자동 알림

연 1회:                    "회수 SOP 자체 평가"
└─ 본 페이지의 SOP가 운영됐는가? 미준수 페이지 N건? 개선 1건?
```

## 3. 회수 단위 표

| 회수 종류 | 측정 단위 | 회수 주기 | 갱신 위치 |
|---|---|---|---|
| **MateChat 출시 KPI** | D30 / paying user / K-factor / 인간-인간 5회 | 일별 (D+1~30) → 주별 (D+30~90) → 월별 | [[matechat-30day-validation-loop]] |
| **c2spf SKILL PoC 결과** | 도입 KPI (롤백·핫픽스·일관성) | PoC 종료 시점 (4주 후) | [[c2spf-ai-agent-adoption-candidates]] 진행 추적 표 |
| **육아휴직 시간 예산 실측** | 영역별 실제 사용 시간 | 월별 회고 | [[parental-leave-2026-operating-plan]] 회수 체크리스트 |
| **위키 자체 메타 KPI** | 페이지 수 / lint 통과율 / 5축 인바운드 분포 | 주기 단위 | [[seokgeun-operating-profile-2026]] |
| **번아웃 신호** | 정지 트리거 발동 횟수 + 회복 기간 | 주별 + 월별 | [[parental-leave-2026-operating-plan]] 비상 정지 트리거 |

## 4. 회수 의무가 있는 페이지 식별 (현재 상태)

`verification_required: true` 페이지:

- [[matechat]] — Google Play 출시 상태
- [[c2spf-analytics]] — 회사 시스템 운영 상태
- [[seokgeun-stack-guide]] — OSS 라이브러리 버전
- [[seokgeun-operating-profile-2026]] — 운영 키워드
- [[seokgeun-mate-chat]] — 39 SKILL 분류
- [[seokgeun-kim-profile-2026]] — 가족·번아웃 상태
- [[langchain]]·[[openai]]·[[fastmcp]]·[[redis]]·[[sentry]] — OSS 변동
- [[parental-leave-2026-operating-plan]]
- [[matechat-30day-validation-loop]]
- [[c2spf-ai-agent-adoption-candidates]]
- [[kpi-recovery-loop]] (본 페이지)

## 5. 회수 자동화 (wiki-lint 확장 권고)

현재 lint check 7은 `last_verified` 90일 초과 시 경고만. P1-6에서 다음을 추가 권고:

```python
# wiki-lint.py 확장
def check_recovery_completeness(pages):
    """verification_required:true 페이지의 본문에 측정값 표가 있는데
    표 셀이 비어 있으면 결함 (회수 누락)."""
    for p in pages:
        if not p.frontmatter.get("verification_required"):
            continue
        body = p.body
        # "| - |" 형태의 빈 셀이 있는 measurement 표 검출
        empty_cells = count_empty_measurement_cells(body)
        if empty_cells > 5:
            yield Defect(p.path, f"측정값 표 빈 셀 {empty_cells}건 — 회수 누락")
```

## 6. SOP 자체 평가 (분기별)

매 분기 마지막 주에 점검:

- [ ] verification_required:true 페이지 중 last_verified 90일 초과 비율 (목표 < 10%)
- [ ] 측정값 표가 있는 페이지 중 빈 셀 비율 (목표 < 30%)
- [ ] 본 페이지가 1회 이상 인용됐는가 (다른 회수 페이지에서)
- [ ] 신규 verification_required 페이지 N건 (분기 평균 > 1건이면 위키가 살아 있다는 신호)
- [ ] **결정적 점검**: 지난 분기 의사결정 1건의 실측 결과가 위키 어딘가에 박혔는가? (예: "P0-X 작업의 효과 측정")

## 출처

- [[seokgeun-kim-profile-2026]] — owner의 가설 → 검증 사고 패턴
- [[mate-chat-project-wiki-2026]] — KPI 정의가 박힌 출처

## 열린 질문

- 회수 자동화 lint를 어디까지 확장할까? (빈 셀 검출 / 표 미존재 검출 / 회수 일정 도래 알림)
- 회수 결과가 stale한 경우 (예: D30 결과를 D+90까지 안 박음) 자동 deprecation 처리?
- 본 SOP가 운영된 후 12개월 시점에 재평가 — 정말 사고 도구로 진화했는지 외부 평가(Codex+자체) 4축 보고서 재실행
