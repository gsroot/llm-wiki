---
title: "MateChat 사업 검증 카탈로그"
type: synthesis
category: guide
aliases: [MateChat 사업 검증, matechat-business-validation, MateChat BizVal, 사업 검증 sub-cluster, 4축 사업 검증]
sources:
  - "[[matechat-30day-validation-loop]]"
  - "[[seokgeun-matechat-validation]]"
  - "[[mate-chat-project-wiki-2026]]"
  - "[[seokgeun-mate-chat]]"
related:
  - "[[matechat]]"
  - "[[matechat-30day-validation-loop]]"
  - "[[seokgeun-mate-chat]]"
  - "[[seokgeun-kim]]"
  - "[[seokgeun-operating-profile-2026]]"
  - "[[parental-leave-2026-operating-plan]]"
  - "[[portfolio]]"
  - "[[llm-infra-meta-cluster]]"
created: 2026-04-29
updated: 2026-04-29
tags: [matechat, 사업검증, business-validation, 4축, 출시후, post-launch, retention, conversion, marketing, 49회차]
verification_required: true
last_verified: 2026-04-29
verification_notes: "v1.0.0 출시 직후부터 측정 시작. 출시 전까지는 측정 SOP·예상 KPI·실험 설계 패턴만 채운 가설 카탈로그. 실측값은 [[matechat-30day-validation-loop]] D+1~D+30 갱신, 그 이후는 본 페이지 영역별 표에 기록."
---

# MateChat 사업 검증 카탈로그

> [!important] 4축 사업 검증 sub-cluster — 49회차 P0-4 신설
> [[matechat|MateChat 사이드 프로젝트]] 4축은 48회차까지 기술 페이지(SKILL 39·아키텍처·QA)에 편중되었고, 사용자 검증·리텐션·결제 전환·마케팅 실험·출시 후 회고 같은 **사업 검증 영역이 비어 있었다**. 본 페이지는 외부 평가(Codex 49회차)가 지적한 4축의 빈자리를 5 영역 측정 SOP + 실험 설계 패턴 + 회고 포맷의 메타 카탈로그로 채운다.
>
> **현재 시점**: v1.0.0 Google Play 출시 직전 QA 단계. 본 페이지의 모든 측정 SOP는 출시 직후 Day 0부터 적용 가능하도록 가설 단계에서 정의되어 있다. 실측값은 출시 후 회수.

## 언제 읽어야 하는가

- "사용자 검증·리텐션·결제 전환·마케팅·회고를 어떻게 측정하나?" — 5 영역 표 직행.
- "출시 후 첫 30일은 [[matechat-30day-validation-loop]], 그 이후는?" — 본 페이지 D31~D365 horizon.
- "사용자 인터뷰·결제 전환 funnel·마케팅 실험은 어떤 형식으로?" — 영역별 SOP 섹션.
- "분기·연간 회고는 어떻게 작성하나?" — 회고 템플릿 섹션.

## 0. 30day-loop과의 관계

| 비교 축 | [[matechat-30day-validation-loop]] (30일 검증 루프) | 본 페이지 (사업 검증 카탈로그) |
|---|---|---|
| **시간 horizon** | D+1 ~ D+30 (단기) | D+31 ~ D+365 + 연간 (중장기) |
| **scope** | 4 핵심 KPI Go/No-Go | 5 영역 측정 SOP + 실험 설계 |
| **목적** | D30 Go/Iterate/Pivot 의사결정 도구 | 영역별 측정·실험·회고 메타 카탈로그 |
| **상태** | 출시 직후 일별 갱신 | 영역별 분기·연간 갱신 |

→ 30day-loop이 "출시 직후 응급실"이라면, 본 페이지는 "출시 후 1년의 항해 지도".

## 1. 사용자 검증 (User Validation)

### 1.1 측정 SOP

| 측정 | 출처 | 빈도 |
|---|---|---|
| MAU (Monthly Active Users) | PostgreSQL 로그인 로그 — distinct user 30일 윈도우 | 주 1회 |
| 신규 가입 funnel (다운로드 → 가입 → 첫 메시지) | Google Play Console + 자체 가입 로그 + WebSocket 첫 메시지 timestamp | 일 1회 (출시 D+30 이후 주 1회) |
| 인간-인간 메시지 vs AI 메시지 비율 | WebSocket 메시지 로그의 `role`·`recipient_type` 필드 | 일 1회 |
| 메시지/세션 평균 길이 | 동일 로그 + 세션 윈도우 정의 | 주 1회 |

### 1.2 사용자 인터뷰 SOP

- **빈도**: D30 시점 5명, 분기별 5명, 연 1회 종합 5명 (총 25명/년 목표)
- **참여자 풀**: D30 retention 충족 사용자 + paying user 우선
- **포맷**: 30분 1:1 zoom·전화. 녹취 동의 후 owner 1인 진행. 후기는 `wiki/raw/notes/matechat-interview-{YYYY-MM-DD}.md`에 저장 후 본 페이지 영역별 인사이트로 통합.
- **질문 5개 고정**:
  1. "MateChat을 처음 알게 된 경로는?"
  2. "마지막으로 사용한 시점·상황은?"
  3. "AI 도움이 가장 컸던 한 순간이 있다면?"
  4. "친구/지인에게 추천한 적이 있나? 왜/왜 안 했나?"
  5. "유료 결제(클로버) 의향과 그 이유는?"

### 1.3 가설 vs 측정 매트릭스 (출시 전 가설)

| 가설 | 출시 전 owner 신뢰도 | 측정 시점 |
|---|---|---|
| MateChat 사용자의 50%는 D7에 인간-인간 메시지 5회 이상 도달 | 60% | D7~D14 |
| AI가 인간 연결 매개체라는 사용 모드가 현실에서 작동 | 70% | D30 인터뷰 |
| 한국어 owner UX가 비한국어권에서도 통한다 | 30% | D90 글로벌 사용자 비중 |

## 2. 리텐션 (Retention)

### 2.1 코호트 리텐션 표

| 코호트 | D+1 | D+7 | D+14 | D+30 | D+60 | D+90 | D+180 | D+365 |
|---|---|---|---|---|---|---|---|---|
| 출시 첫 주 | | | | | | | | |
| D+30 ~ D+60 신규 | — | | | | | | | |
| D+60 ~ D+90 신규 | — | — | | | | | | |
| (분기별 추가) | — | — | — | | | | | |

→ 측정 출처: PostgreSQL 가입 timestamp + 로그인 timestamp의 cohort SQL.

### 2.2 리텐션 의사결정 트리거

- **D30 retention < 5%** → Pivot 검토 (사용 모드 가설 자체가 틀림)
- **D30 retention 5~8%** → Iterate (UX 한 영역 집중 개선 후 D60 재측정)
- **D30 retention 8% 이상** → Go (마케팅·결제 전환 본격 가동)
- **D90 retention < D30의 50%** → 콘텐츠/사용자간 활동 부재 의심, 인터뷰 5명 추가
- **D365 retention 1% 도달** → "장기 hub 사용자" 군 형성, paid plan 설계 검토

## 3. 결제 전환 (Conversion)

### 3.1 결제 funnel

| 단계 | 측정 | 출시 전 가설 |
|---|---|---|
| 결제 가능 진입 (free → paywall 노출) | 클로버 IAP `paywall_view` 이벤트 | 가입자의 30%가 D30 내 paywall 1회 이상 노출 |
| paywall → 결제 시도 (Buy 클릭) | `purchase_attempt` 이벤트 | paywall 노출자의 5% |
| 결제 완료 (Google Play IAP 검증 통과) | IAP 영수증 검증 로그 | 시도자의 80% |
| 7일 환불률 | Google Play Console 환불 리포트 | 5% 이내 |
| paying user 재결제 (구독형이면) | IAP 갱신 이벤트 | D60에 첫 결제자의 60% 이상 |

### 3.2 가격 실험 패턴

- **A/B 가격 테스트**: 출시 D+90 전까지는 단일 가격(클로버 단가) 고정. D+90 이후 50:50 소규모 A/B 실험 가능 — 단 paying user 누적 100명+ 도달 후.
- **페이월 위치 실험**: AI 메시지 N회 후 vs 인간-인간 메시지 N회 후 vs 첫 인터랙션 후 — 3가지 위치를 D+120 ~ D+150 1주씩 순환 실험.
- **무료 한도 실험**: 일별 메시지 한도, 친구 수 한도 — D+180 이후 사용 패턴 확정 후 도입 검토.

## 4. 마케팅 실험 (Marketing)

### 4.1 채널 카탈로그 (출시 전 가설 우선순위)

| 채널 | 출시 전 가설 우선순위 | 측정 KPI | 비용 (월 KRW) |
|---|---|---|---|
| 인스타그램 organic | 1 | 팔로워 / 게시물 reach / 프로필 클릭 → 다운로드 conversion | 0 (시간만) |
| TikTok organic | 2 | 영상 view / share / bio 링크 클릭 | 0 (시간만) |
| Naver 블로그 / 카페 | 3 | 페이지뷰 / 댓글 / referrer 다운로드 | 0 |
| Google Ads (검색 / UAC) | 4 (paying user 100명 후) | CPI / D7 retention by source | 100k~500k |
| Meta Ads | 5 (UAC 데이터 회수 후) | 동일 | 100k~500k |
| 인플루언서 협업 | 6 (D+180 후) | 게시물 reach / referrer 가입 / paying user 비율 | 협상 |

### 4.2 실험 설계 원칙

- **한 번에 한 채널만** 변경 — 인과 추적 가능성 보존.
- **최소 2주 측정** 후 채택/포기 결정.
- **referrer 추적 의무**: 가입 시 `referrer` 필드 + UTM 파라미터 동시 수집. PostgreSQL `users.referrer` 컬럼 + Google Play install referrer.
- **유료 광고 진입 조건**: paying user 누적 100명 + organic D30 retention 8%+ 둘 다 충족 후. 그 전엔 product-market fit 미증명 상태에서 광고비 지출 = 노이즈.

## 5. 출시 후 회고 (Post-launch Retrospectives)

### 5.1 회고 주기

| 주기 | 출력물 | 위키 위치 |
|---|---|---|
| 일 (D+1 ~ D+30) | 일별 KPI 표 | [[matechat-30day-validation-loop]] |
| 주 (D+7 / D+14 / D+21 / D+28) | 주간 회고 4건 | 동일 |
| 월 (D+30 / D+60 / D+90 / ...) | 월별 회고 | 본 페이지 § 5.2 |
| 분기 (D+90 / D+180 / D+270 / D+365) | 분기 회고 + 인터뷰 5명 종합 | 본 페이지 § 5.3 |
| 연 (D+365) | 연간 회고 + 다음 1년 plan | 본 페이지 § 5.4 |

### 5.2 월별 회고 템플릿 (D+30 이후 매월)

```
## D+{N*30} 월별 회고 ({YYYY-MM-DD})

### 정량 (자동 회수)
- MAU: __
- D30 retention (이번 달 신규 코호트): __%
- paying user 누적: __
- 누적 매출 KRW: __

### 정성 (owner 작성, 30분 내)
- 가장 잘된 1건:
- 가장 못된 1건:
- 다음 달 단 하나의 실험:

### 의사결정
- Go / Iterate / Pivot:
- 다음 달 시간 예산 (MateChat / c2spf / 가족·육아):
```

### 5.3 분기 회고 추가 항목

월별 템플릿 + 다음 5개:
- 인터뷰 5명 종합 인사이트 (3 bullet)
- 마케팅 채널 ROI 분기 비교
- 가격·페이월 실험 결과 (해당 시)
- portfolio (이력서·면접) 활용 지점 (해당 시)
- [[seokgeun-operating-profile-2026]] 시간 예산 재할당 결정

### 5.4 연간 회고 추가 항목

분기 회고 + 다음 5개:
- 1년 누적 정량 ledger (모든 코호트 retention 표)
- 1년 누적 매출 vs 비용 P&L
- 1인 사업화 의사결정: B2C 단독 / B2B 컨설팅 병행 / OSS 전환 / 운영 종료 — [[seokgeun-operating-profile-2026]]·[[parental-leave-2026-operating-plan]]과 연동
- 다음 1년 owner 시간 예산 plan
- 다음 1년 위키 운영 plan ([[llm-infra-meta-cluster]] 5축 변동 예측)

## 6. 미측정 영역 ledger

본 페이지가 정의한 SOP 중 출시 전 시점에 **0이 아닌 측정값을 가진 항목은 0건**이다. 즉 본 페이지 전체가 가설 카탈로그.

| 영역 | 첫 측정 예정 시점 | 첫 갱신자 |
|---|---|---|
| 사용자 검증 (1.1 표) | D+1 | owner 자동 — PostgreSQL 쿼리 |
| 인터뷰 (1.2) | D+30 ~ D+45 | owner 수동 — 5명 일정 잡기 |
| 코호트 리텐션 (2.1) | D+30 첫 측정, D+60부터 정식 | owner 자동 — cohort SQL |
| 결제 funnel (3.1) | D+1 (paywall 노출 즉시) | owner 자동 — IAP 로그 |
| 가격 A/B (3.2) | D+90 후 | owner 수동 — 실험 설계 |
| 마케팅 organic (4.1) | D+1 즉시 | owner 수동 — 게시물 작성 |
| 유료 광고 (4.1) | D+90 ~ D+180 | owner 수동 — 진입 조건 충족 후 |
| 월별 회고 (5.2) | D+30 첫 작성 | owner — 30분 내 |
| 분기 회고 (5.3) | D+90 | 동일 |
| 연간 회고 (5.4) | D+365 | 동일 |

## 7. 본 페이지의 위키 위상

본 페이지는 4축 [[matechat|MateChat]] hub의 **사업 검증 메타 sub-cluster**다. 5축 [[llm-infra-meta-cluster|LLM 인프라 메타 클러스터]]가 "어떻게 운영되는가"의 메타였다면, 본 페이지는 "어떻게 검증되는가"의 메타.

| sub-cluster | 위치 | 다루는 영역 |
|---|---|---|
| [[matechat-project-knowledge-map]] | 4축 entity 맵 | 프로젝트 지식 지도 |
| [[matechat-chat-analysis-module]] | 기술 entity | 채팅 분석 SKILL |
| [[matechat-30day-validation-loop]] | 4축 단기 검증 | D+1 ~ D+30 KPI 회수 SOP |
| **본 페이지** (matechat-business-validation) | **4축 중장기 검증** | **D+31 ~ D+365 + 연간 카탈로그** |

→ 49회차 P0-4 신설로 4축이 기술/검증/사업 3 sub-cluster 균형을 갖춤.

## 출처

- [[matechat-30day-validation-loop]] — 단기 KPI 회수 SOP (48회차 신설). 본 페이지의 D+1~D+30 부분이 이 페이지에 위임됨.
- [[seokgeun-matechat-validation]] — owner 자체 검증 메모.
- [[mate-chat-project-wiki-2026]] — MateChat 프로젝트 위키 2026-04-28 스냅샷.
- [[seokgeun-mate-chat]] — 4축 owner-side entity.

## 메모

- 본 페이지 신설 동기는 49회차 외부 평가(Codex)가 "4축이 기술 페이지에 편중되어 사용자 검증/리텐션/결제 전환/마케팅 실험/출시 후 회고가 묻힐 위험"이라고 지적한 결함을 채우는 것.
- 출시 직후 D+1부터 본 페이지 § 6 미측정 영역 ledger의 항목들이 하나씩 채워질 예정. 각 영역 표·코호트 표는 출시 직후 첫 갱신 시 본 페이지 본문에 직접 기록.
- 본 페이지가 인바운드 5+ 도달 시 — matechat·seokgeun-mate-chat·matechat-30day-validation-loop·seokgeun-operating-profile-2026·portfolio 5개에서 인용되면 — 4축 사업 검증 sub-cluster가 위키 그래프상 정착했다는 직접 증거.
