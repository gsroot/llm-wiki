---
title: "MateChat 30일 검증 루프"
type: synthesis
category: guide
aliases: [MateChat 30일 검증, matechat-30day-validation-loop, 30일 알파 검증, MateChat 알파 KPI]
tags: [matechat, 30일검증, alpha-validation, kpi, 검증루프, retention, conversion, post-launch, 48회차]
sources:
  - "[[seokgeun-mate-chat]]"
  - "[[seokgeun-matechat-validation]]"
  - "[[mate-chat-project-wiki-2026]]"
related:
  - "[[matechat]]"
  - "[[matechat-business-validation]]"
  - "[[matechat-launch-metrics-ledger]]"
  - "[[seokgeun-kim]]"
  - "[[seokgeun-operating-profile-2026]]"
  - "[[parental-leave-2026-operating-plan]]"
created: 2026-04-29
updated: 2026-04-29
verification_required: true
last_verified: 2026-04-29
verification_notes: "출시 D+30 시점에 KPI 실측값 회수 + Go/Iterate/Pivot 의사결정 박힘. 출시 전까지 가설 단계."
---

# MateChat 30일 검증 루프

> [!important] 실행형 hub — 출시 후 30일간 일별 KPI 회수 SOP
> 48회차 신설 (Codex 권고 P1). [[matechat|MateChat 사이드 프로젝트]] v1.0.0 출시 D+1 ~ D+30 동안 일별 측정·주별 회고·D30 의사결정의 절차를 박는다. 측정값이 비어 있으면 **Go/Iterate/Pivot 의사결정 자체가 불가능** — 47회차까지 비어 있던 회수 루프를 채우는 것이 본 페이지의 핵심.
> 
> 한국어 표기: **MateChat 30일 검증 루프** 또는 **알파 검증**.

## 언제 읽어야 하는가

- "출시 직후 매일 무엇을 확인해야 하나?" — 일별 KPI 표 직행.
- "주간·30일 종합 의사결정은 어떻게 내리는가?" — Go/Iterate/Pivot 트리거 섹션.
- "어떤 KPI가 진짜 중요한가?" — 핵심 KPI 4가지 (D30/인간-인간 5회/paying user/K-factor).
- "사용자 인터뷰는 언제·어떻게 하나?" — 인터뷰 SOP 섹션.

## 1. 핵심 KPI 4가지 (Go/No-Go 결정 기준)

| KPI | D30 목표 | 의미 | 측정 출처 |
|---|---|---|---|
| **D30 retention** | 8%+ | 30일 후에도 주 1회 이상 사용 | PostgreSQL 로그인 로그 |
| **인간-인간 메시지 5회 (첫 7일)** | 50%+ 사용자 | "AI가 사람 연결 도왔다"의 직접 증거 | WebSocket 메시지 로그 |
| **Paying user 누적** | 10명+ | 클로버 IAP 결제 사용자 | IAP 검증 로그 |
| **Organic K-factor** | 0.3+ | 초대로 인한 신규 가입 비율 | 가입 referrer 추적 |

이 4개 중 **2개 이상 미달**이면 D30에 Pivot 검토 자동 트리거.

## 2. 일별 측정 표 (D+1 ~ D+30)

매일 오전 30분 내에 다음 표를 갱신 — 가능하면 위키가 아닌 별도 spreadsheet (회수 후 본 페이지 요약 갱신):

| 일 | DAU | 신규 | AI 메시지 수 | 인간-인간 메시지 수 | 클로버 결제 | 이슈 / CS |
|---|---|---|---|---|---|---|
| D+1 | | | | | | |
| D+2 | | | | | | |
| ... | | | | | | |
| D+30 | | | | | | |

기록 원칙: **숫자가 0이어도 0이라고 적는다**. 빈칸은 측정 누락 = 의사결정 불가.

## 3. 주간 회고 (D+7 / D+14 / D+21 / D+28)

각 주말 30분, 다음 5개 질문에 직접 답:

1. **이번 주 신규 사용자 패턴**: 어디서 왔나? 어떤 기대로 왔나?
2. **이탈 사용자 패턴**: 언제 떠났나? 마지막 행동은?
3. **놀라운 사용 패턴**: 가설에 없던 사용법이 보였나?
4. **CS 이슈 1위**: 가장 자주 들어온 문의 / 버그?
5. **다음 주 1개 실험**: 가설 1개 + 측정 방법 1개

## 4. 사용자 인터뷰 SOP

### 대상 (D+7 / D+14 / D+21 각 1회씩)

- **유지 사용자**: D+7까지 4일 이상 사용 → 1명
- **이탈 사용자**: D+3까지 사용 후 3일 미접속 → 1명
- **결제 사용자**: 클로버 결제 1건 이상 → 1명 (D+14 이후)

### 방식

- 텍스트 30분 (일정 보존, 부담 없음) 또는 음성 15분
- 보상: 클로버 1,000개 (약 $5 가치)
- 인터뷰 노트는 raw/notes/matechat-interviews/ 에 보존, 본 페이지에 요약만

### 질문 5개 (변형 가능)

1. MateChat을 어떻게 알게 됐나요?
2. 처음 들어와서 무엇을 했나요?
3. AI 메이트와 대화한 후 어떤 느낌이었나요?
4. 다른 사용자와 메시지를 주고받은 경험이 있나요? 있다면 어땠나요?
5. 다른 친구에게 추천한다면 어떤 말로 소개할 건가요?

## 5. D30 의사결정 트리

```
Q: 핵심 KPI 4개 중 몇 개가 목표 충족?
├─ 4개 모두 → Go: v1.1 로드맵 + 마케팅 시작
├─ 3개 → Iterate: 미달 KPI 1개 집중 1개월
├─ 2개 → 신중 Iterate: 인터뷰 5건 추가 + 1개월 재시도
└─ 1개 이하 → Pivot 검토:
   ├─ 페르소나 재정의 / 채널 변경 시도
   └─ 또는 closed alpha 종료 + minimal 운영
```

## 6. Pivot 시나리오 (1개 이하 충족 시)

- **페르소나 변경**: "외로운 AI 의존자" → "외국 워홀러" / "이주민" 으로 재타게팅
- **포지셔닝 변경**: "사람 연결" → "AI 동반 일기" 같은 솔로 포커스
- **채널 변경**: Google Play organic → 특정 커뮤니티 (예: 워홀러 카페) 직접 모집
- **종료**: 출시 자체를 학습 자산으로 보존하고 다음 사이드 후보로 전환

## 출처

- [[seokgeun-mate-chat]] — 39 SKILL 분포 + 출시 직전 상태 (44회차 정정)
- [[seokgeun-matechat-validation]] — 검증 가설 + 페르소나 정의
- [[mate-chat-project-wiki-2026]] — 출시 직전 프로젝트 스냅샷

## 열린 질문

- 클로버 보상 인터뷰가 답변 편향을 만들지 않을까? (대안: 무보상 정성 후기)
- DAU 측정에 다중 기기 사용자 중복 카운트 보정이 필요한가?
- D30 의사결정에 owner 본인의 번아웃 신호([[parental-leave-2026-operating-plan]] 트리거 섹션)도 포함해야 하나?
