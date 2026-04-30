---
title: MateChat 출시 후 실측 ledger
type: synthesis
category: operating-log
aliases:
- MateChat 실측 ledger
- matechat-launch-metrics-ledger
- MateChat 출시 KPI ledger
- launch ledger
sources:
- '[[seokgeun-matechat-validation]]'
- '[[mate-chat-project-wiki-2026]]'
- '[[seokgeun-mate-chat]]'
related:
- '[[matechat]]'
- '[[matechat-30day-validation-loop]]'
- '[[matechat-business-validation]]'
- '[[seokgeun-mate-chat]]'
- '[[seokgeun-kim]]'
- '[[portfolio]]'
- '[[llm-infra-meta-cluster]]'
created: 2026-04-29
updated: 2026-04-29
tags:
- matechat
- post-launch
- retention
- conversion
- 4축
verification_required: true
last_verified: 2026-04-29
verification_notes: v1.0.0 Google Play 출시 직후 D+1부터 컬럼 채우기 시작. 30day-loop과 달리 본 페이지는 의사결정 SOP가 아닌 raw 측정값 저장소. D+30 이후도 D+90/D+180/D+365 이정표 컬럼 유지. 출시 전까지는 빈 표·컬럼 정의·측정 출처만 박혀 있는 골격 단계.
cited_by_count: 9
inbound_count: 13
---

# MateChat 출시 후 실측 ledger

> [!important] raw 실측값 저장소 — P0-4 신설 (Codex 권고 합집합)
> [[matechat|MateChat 사이드 프로젝트]] v1.0.0 출시 후 회수되는 KPI 실측값을 한 페이지에 모아 두는 raw ledger. 의사결정·메타 분석은 [[matechat-30day-validation-loop]](D+1~D+30 SOP) 와 [[matechat-business-validation]](D+31~D+365 5영역 카탈로그)이 담당하고, 본 페이지는 **숫자만 박는 단순 데이터 페이지**다.
>
> **현재 시점**: v1.0.0 Google Play 출시 직전 QA 단계. 모든 셀이 빈칸 또는 `-` 상태. 출시 D+0부터 채우기 시작.
>
> **분리 이유**: 측정 SOP·의사결정 도구·raw 데이터를 한 페이지에 섞으면 RAG가 "측정 방법" 질문에 raw 0값 표를 답으로 회수하거나, "현재 retention 얼마?" 질문에 측정 SOP를 답으로 돌려준다. 페이지 분리로 RAG 질의-답변 매핑 명확화.

## 언제 읽어야 하는가

- "MateChat의 D+7 / D+30 / D+90 retention 실측 얼마?" — 1번 표 직행.
- "출시 후 인간-인간 메시지 비율은 회복됐나?" — 2번 표.
- "결제 funnel 단계별 전환율은?" — 3번 표.
- "사용자 인터뷰는 누구·언제 했나?" — 5번 표.

## 1. Retention ledger (이정표별 코호트)

D+1·D+7·D+30·D+90·D+180·D+365 시점 retention 실측. 코호트는 출시 후 첫 7일간 가입자.

| 이정표 | 측정일 | 코호트 N | 활성 사용자 | retention % | 비고 |
|---|---|---|---|---|---|
| D+1 | TBD | - | - | - | 첫 24시간 재방문 |
| D+7 | TBD | - | - | - | 1주 후 |
| D+30 | TBD | - | - | - | 1개월 후 (Go/No-Go 트리거) |
| D+90 | TBD | - | - | - | 분기 회고 입력 |
| D+180 | TBD | - | - | - | 반기 회고 입력 |
| D+365 | TBD | - | - | - | 연간 회고 입력 |

측정 출처: PostgreSQL `users.last_login_at` 컬럼 + 가입일 기준 코호트 쿼리.

## 2. 인간-인간 메시지 비율 ledger

"AI가 사람 연결을 도왔다"의 직접 증거. 첫 7일 내 인간-인간 메시지 5회 이상 사용자 비율.

| 이정표 | 측정일 | 첫 7일 N+ HH 메시지 사용자 | 전체 N+ 사용자 | 비율 % | 비고 |
|---|---|---|---|---|---|
| D+7 | TBD | - | - | - | 출시 직후 첫 코호트 |
| D+30 | TBD | - | - | - | 1개월 후 코호트 비교 |
| D+90 | TBD | - | - | - | 분기 회고 |

측정 출처: WebSocket 메시지 로그에서 sender_id·receiver_id·is_ai 컬럼 집계.

## 3. 결제 funnel ledger (클로버 IAP)

| funnel 단계 | 측정일 | 누적 N | 직전 단계 대비 % | 비고 |
|---|---|---|---|---|
| 결제 화면 진입 | TBD | - | - | 결제 페이지 view |
| 상품 선택 | TBD | - | - | item_select |
| 결제 시도 | TBD | - | - | clover invoke |
| 결제 완료 | TBD | - | - | IAP receipt 검증 통과 |
| 7일 환불 | TBD | - | - | refund 요청 |

측정 출처: IAP 검증 로그 + 클라이언트 funnel 이벤트.

## 4. K-factor ledger (organic 초대)

| 이정표 | 측정일 | 초대 발송 | 초대 가입 | K-factor | 비고 |
|---|---|---|---|---|---|
| D+30 | TBD | - | - | - | 첫 코호트 K-factor |
| D+90 | TBD | - | - | - | 분기 |
| D+180 | TBD | - | - | - | 반기 |

측정 출처: 가입 referrer 추적 (deep link or 코드).

## 5. 사용자 인터뷰 ledger

| | 일시 | 인터뷰이 ID | 사용 패턴 | 핵심 인사이트 | 액션 |
|---|---|---|---|---|---|
| 1 | TBD | - | - | - | - |
| 2 | TBD | - | - | - | - |
| 3 | TBD | - | - | - | - |

기록 원칙: 인사이트 1건당 1행. 액션 컬럼에는 후속 PR·SOP 갱신·사이드 프로젝트 백로그로의 파급 명시.

## 6. 회고 트리거 (이정표 도달 시)

| 이정표 | 회고 대상 페이지 | 트리거 조건 |
|---|---|---|
| D+30 | [[matechat-30day-validation-loop]] | D+30 도달 — 4 핵심 KPI 평가 + Go/Iterate/Pivot 결정 |
| D+90 | [[matechat-business-validation]] 분기 영역 | 분기 회고 입력 |
| D+180 | [[matechat-business-validation]] 반기 영역 | 반기 회고 입력 |
| D+365 | [[matechat-business-validation]] 연간 영역 + [[seokgeun-operating-profile-2026]] | 연간 회고 + 진로 의사결정 입력 |

## 7. 다른 ledger 페이지와의 관계

본 페이지는 **raw 데이터 저장소**. 의사결정·메타 분석은 다음 페이지로 분리:

- [[matechat-30day-validation-loop]]: D+1~D+30 일별 측정 SOP + 의사결정 도구. 본 ledger의 D+1·D+7·D+30 셀이 채워지면 30day-loop이 그 값으로 Go/Iterate/Pivot 판정.
- [[matechat-business-validation]]: D+31 이후 중장기 5 영역(retention/conversion/marketing/회고/인터뷰) 메타 카탈로그. 본 ledger의 D+90·D+180·D+365 셀이 채워지면 카탈로그의 영역별 표에 인용.
- [[matechat]]: 4축 hub. 본 ledger의 핵심 숫자(D+30 retention·paying user 누적·인터뷰 차수)를 hub 본문에 시점 라벨링과 함께 인용.

## 8. 운영 원칙

1. **빈칸 금지**. 측정 누락은 `-` 또는 `0`으로 명시. 빈칸은 "아직 시점 도달 전"의 의미로만 허용.
2. **시점 라벨**. 모든 셀 갱신 시 "측정일" 컬럼 ISO 8601 (`YYYY-MM-DD`) 박기. RAG가 stale 위험 판정 가능하게.
3. **frontmatter `last_verified` 동기화**. 표를 갱신할 때 `last_verified`도 같은 날로 갱신.
4. **측정 출처 변경 시**: 출처 컬럼 또는 `verification_notes`에 변경 사유 기록. 측정 방법이 바뀌면 이전 시점 값과 직접 비교 금지.
