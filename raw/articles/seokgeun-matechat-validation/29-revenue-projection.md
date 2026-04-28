# Mate Chat 출시 후 수익 예측 리포트 (v1.0 기준선)

> **작성일:** 2026-04-22 (초안), 2026-04-23 (검증 통합)
> **작성 맥락:** v1.0.0 Google Play 출시 직전 시점에서 출시 후 1년 수익을 추정하기 위한 리포트.
> **검증 단계:**
> - codex adversarial challenge (§13) — 12 findings
> - office-hours Startup mode (§14) — Persona A 우세, 베타 0명 갭
> - plan-ceo-review EXPANSION mode (§15) — P3+P5 채택 (60일 metric + PMF KPI)
> **환율:** 2026-04 기준 1 USD = ₩1,350 고정 (codex F6은 ₩1,495 권고 — §13 참조).
>
> **권고 우선순위:** 본 리포트의 §1 숫자보다 **§13~§15의 검증 결과가 의사결정의 1차 입력**이다. 산식 오류·OpEx 누락·CPI 가정이 §13에서 발견되어 v1 Base $200K → **v2 ~$25K (§13.4 codex 보정)** → **v3 ~$30K (§14.3 office-hours 한국 단일 segment)** → **v4 (§15.4 KPI 자체를 PMF 증거로 재정의)** 로 진화. 수익은 후행 지표.
>
> **빠른 진입 (의사결정자용):** [§15.4 v4 PMF KPI](#154-p5--year-1-kpi를-pmf-증거로-재정의-채택) · [§10 출시 D-7~D+90 액션](#10-후속-권고-출시-임박-시점-액션) · [§13.5 v2 권장 시나리오](#135-권장-조정안-draft-office-hourssceo-review-후-확정) · [§14.4 The Assignment](#144-결정적-갭-q5-답변-기반)

---

## 1. Executive Summary

> ⚠️ **STALE — 이 표의 숫자는 의사결정에 사용 금지** ⚠️
>
> 아래 v1 초안 표는 §13 codex challenge에서 **산식 오류·OpEx 누락·fantasy CPI**가 발견되어 폐기되었습니다.
> - 현행 권고 (낮음→높음): **§13.4 v2 ($25K)** → **§14.3 v3 ($30K, 한국 단일 segment)** → **§15.4 v4 (수익 KPI 자체를 PMF KPI로 재정의)**
> - **의사결정자는 §15 P5 (paying users 1K + D30 retention 8% + K-factor 0.3)를 1차 입력으로 사용하세요.**
> - v1 표는 audit trail 목적으로 보존되며, "$200K Base"를 외부 인용·예산 책정·KPI 설정에 직접 사용하면 안 됩니다.

**기간별 Net Revenue v1 초안 (audit trail용, 사용 금지)**

| 기간 | Conservative | ~~Base (Maum 앵커)~~ | Optimistic | 비고 |
|---|---|---|---|---|
| W1 (Week 1, 단주) | $80 | ~~$250~~ | $700 | **§13 폐기** |
| M1 (Month 1, 단월) | $400 | ~~$1,400~~ | $4,200 | **§13 폐기** |
| M3 (Month 3, 단월) | $1,800 | ~~$5,500~~ | $15,000 | **§13 폐기** |
| M6 (Month 6, 단월) | $4,500 | ~~$14,000~~ | $45,000 | **§13 폐기** |
| M12 (Month 12, 단월) | $9,000 | ~~$32,000~~ | $110,000 | **연간 누적 v1: $60K / ~~$200K~~ / $620K — 모두 §13 폐기** |

> **v1 핵심 메시지 (폐기됨)**: ~~Base 시나리오 기준 출시 후 1년차 Net Revenue ≈ $200K (≈ ₩2.7억)~~ — 산식 오류 (§13 F1: ARPPU $9 vs $18 모순), fantasy CPI (§13 F5: $0.079 vs 실제 $1.5~4), Creator subsidy 누락 (§13 F3) 등으로 폐기. **현행 권고는 §15.4 v4 PMF KPI**.

**v4 현행 권고 (§15.4 P5 채택 결과)**:

| KPI | Year-1 Target | 의미 |
|---|---|---|
| Paying user count | **1,000명** | Liquidity proof |
| D30 retention | **8%+** | Product stickiness |
| Organic K-factor | **0.3+** | Viral seed 형성 |

3개 모두 달성 시 → Year-2 외부 자금 조달 또는 자생적 성장 트리거. 수익은 자동 후행. 일부만 달성 → PMF 부분 증거. 모두 미달 → pivot 또는 정리.

---

## 2. Scope & Methodology

### 2.1 분석 대상
- **상품**: Mate Chat v1.0.0 (Google Play Android만, 2026년 출시)
- **수익원**: 클로버 IAP 5종 SKU (₩5,000 ~ ₩70,000)
- **기간**: 출시 시점부터 W1 / M1 / M3 / M6 / M12
- **iOS는 M6부터 가산** (계획상 v1.1, Apple OAuth 미구현이 블로커. Optimistic 시나리오에만 반영)

### 2.2 접근법
**Maum 앵커링 + 바텀업 코호트 모델 + 3-시나리오 분기**.

```
Monthly Gross Revenue
  = ΣNew_Installs(t) × Activation% × MAU_Conversion(t)
  × Paying_User_Rate × ARPPU_monthly

Monthly Net Revenue
  = Gross × (1 - store_fee) - OpenAI_variable_cost - infra_fixed
```

- `store_fee`: 첫 $1M까지 **15%**, 이후 30% (Google Play 15% small business program 가정)
- `OpenAI_variable_cost`: 메시지당 ~$0.0005 (GPT-4o-mini, in 1.5K + out 0.5K 토큰 가정)
- `infra_fixed`: 단일 서버 운영 가정 시 ~$300/월 (Postgres + Redis + MinIO + 백엔드)

### 2.3 시나리오 정의

| 시나리오 | 정의 | 마케팅 가정 | 글로벌 확산 |
|---|---|---|---|
| Conservative | Maum 초기 곡선의 50% 속도 | 유기적 + 한국 SNS 소량 | 한국 위주, 동남아·중남미 미진 |
| **Base** | Maum과 동등한 곡선 (3 → 9개 언어 가산은 마케팅 분산으로 상쇄) | 유기적 + Year-1 마케팅 ~$30K | 한·일·동남아 일부 |
| Optimistic | Maum × 1.5 + AI 차별점 + iOS M6 가산 | Year-1 마케팅 ~$80K | 한·일·동남아·중남미·일부 영어권 |

---

## 3. Anchor Benchmarks (출처)

### 3.1 핵심 앵커: Maum (LIFEOASIS)

| 지표 | 값 | 출처 |
|---|---|---|
| 2024년 매출 | ₩32.4억 (~$2.4M) | [머니투데이 2025-01-31](https://news.mt.co.kr/mtview.php?no=2025013114535497187) |
| 2024년 영업이익 | ₩5.4억 | 상동 |
| 2024년 당기순이익 | ₩7.5억 | 상동 |
| YoY 성장률 (2023→2024) | +200% | 상동 |
| **추정 2023 매출** | ~₩10.8억 (~$0.8M) | 200% 역산 |
| 누적 다운로드 | 6~7M (4년 누적) | `docs/27-competitive-analysis.md` |
| 출시 시점 | 2021년 1월 | [VentureSquare 시드 7억 보도](https://www.venturesquare.net/839433) (원문 410 Gone, [archive.org 스냅샷](https://web.archive.org/web/2021*/venturesquare.net/839433) 또는 [Wanted 라이프오아시스](https://www.wanted.co.kr/company/25642) 참조) |
| 직원 수 | 16~21명 | [Wanted 라이프오아시스](https://www.wanted.co.kr/company/25642) |
| UI 언어 | 3개 (ko/en/ja) | 상동 |
| 핵심 기능 | 1:1 음성통화 + 풍선 IAP | 상동 |

**Maum 매출 곡선 추정 (2021 출시 기준 4개년)**:
| 연차 | 연매출 (USD 추정) | 비고 |
|---|---|---|
| Year 1 (2021) | ~$0.05M | 출시 직후 |
| Year 2 (2022) | ~$0.27M | 추정 (200% 곡선 역산) |
| Year 3 (2023) | $0.80M | 200%/2024 역산 |
| Year 4 (2024) | $2.40M | 공식 발표 |

→ **Mate Chat의 Year-1 수익 예측 시 Maum Year-1 ($0.05M)을 baseline으로 잡는 것이 가장 방어 가능**. 단, Mate Chat은 4년 후 출시이므로 모바일 시장 성숙도(IAP 시장 +13% YoY 성장 [Sensor Tower](https://sensortower.com/state-of-mobile-2025))를 반영해 ~1.5배 가산.

### 3.2 보조 벤치마크

| 앱 | 매출/MAU | ARPU/년 | 전환율 | 출처 |
|---|---|---|---|---|
| Character.AI | $50M / 20-45M | $1.10~$2.50 | 미공개 | [Sacra](https://sacra.com/c/character-ai/), [Business of Apps](https://www.businessofapps.com/data/character-ai-statistics/) |
| Replika | $24-30M / 2M | $12~$15 | **25%** | [TechBuzz.ai](https://www.techbuzz.ai/articles/breaking-ai-companion-apps-hit-120m-revenue-run-rate), [Wikipedia](https://en.wikipedia.org/wiki/Replika) |
| Bumble | — | $26.34/분기 ARPPU | — | [Statista Bumble ARPPU](https://www.statista.com/statistics/1233246/quarterly-bumble-arppu-by-app/) |

> **Replika 25%의 함정**: 이는 "구독 결제 전환"이며 Mate Chat은 **소모성 IAP**다. 비교 가능한 모델은 모바일 게임 IAP(평균 1.5~3% payer rate, [Adjust](https://www.adjust.com/glossary/arppu/)).

### 3.3 카테고리 트렌드
- AI companion 카테고리 revenue per download: $0.52 (2024) → **$1.18 (2025)** ([TechCrunch](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/))
- 평균 모바일 앱 D30 리텐션: ~5%; 첫 30일 90% 이탈 ([Dogtown Media](https://www.dogtownmedia.com/the-first-90-days-after-app-launch-what-to-expect-and-how-to-thrive/))
- 글로벌 IAP 시장 (2024): $150B (+13% YoY); Q2 2025: $41B (+11.5% YoY) ([Sensor Tower 2025](https://sensortower.com/state-of-mobile-2025))

---

## 4. Input Assumptions (변수 표)

### 4.1 사용자 획득 (월별 New Installs)

| 시나리오 | M1 | M2 | M3 | M6 | M12 | 누적 (M12) |
|---|---|---|---|---|---|---|
| Conservative | 8,000 | 7,000 | 6,500 | 6,000 | 7,000 | ~85,000 |
| **Base** | 20,000 | 22,000 | 25,000 | 35,000 | 50,000 | ~380,000 |
| Optimistic | 50,000 | 60,000 | 80,000 | 130,000 | 200,000 | ~1,400,000 |

근거: Maum Year-1 누적 ~50K~100K 추정 (200% 곡선) → Base는 그 4-5배 가속 (3→9개 언어 + 4년 후 시장 성숙). Optimistic은 글로벌 트렌드 + AI 후광 + iOS 가산.

### 4.2 활성률 & 리텐션

| 지표 | Conservative | **Base** | Optimistic | 출처 |
|---|---|---|---|---|
| Activation% (가입→이메일 인증 완료) | 50% | 60% | 70% | Welcome 보너스 200 클로버 인센티브로 평균 이상 가능 |
| D7 retention | 8% | 12% | 18% | 평균 모바일 앱 D7 ~10% 기준 |
| D30 retention | 3% | 5% | 8% | 평균 5% ([Dogtown Media](https://www.dogtownmedia.com/the-first-90-days-after-app-launch-what-to-expect-and-how-to-thrive/)) |
| MAU/누적설치 비율 (M3 시점) | 12% | 18% | 25% | 코호트 합산 후 보정 |

### 4.3 결제 행동

| 지표 | Conservative | **Base** | Optimistic | 근거 |
|---|---|---|---|---|
| Paying User Rate (월간) | 1.0% | 2.0% | 3.5% | 게임 IAP 평균 1.5~3%; AI 차별점 +0.5% |
| **ARPPU (월간, USD)** | $5 | $9 | $14 | Bumble $9, Replika $13. 클로버 평균 패키지 ₩12,000 가정 |
| 평균 패키지 단가 (KRW) | ₩7,500 | ₩12,000 | ₩18,000 | SKU 5종 가중평균; Optimistic은 +20%/+33% 패키지 비중↑ |
| 월 결제 횟수 (paying user당) | 0.9 | 1.0 | 1.1 | 평균 1회 가정 |

### 4.4 원가

| 지표 | 값 | 근거 |
|---|---|---|
| Google Play 수수료 (첫 $1M) | 15% | Google small business program |
| Google Play 수수료 ($1M 이후) | 30% | 표준 (Year-1엔 도달 가능성 0%) |
| OpenAI 메시지 원가 | $0.0005/메시지 | GPT-4o-mini ($0.15/1M in + $0.60/1M out) × in 1500 + out 500 토큰 ([OpenAI Pricing](https://openai.com/api/pricing/)) |
| 클로버당 매출 단가 | $0.0093 (₩12.5) | ₩5,000 / 400 클로버 |
| AI 메시지당 매출 (5클로버) | $0.046 | `hybrid_chat_service.py:492` |
| AI 메시지 마진 | $0.046 - $0.0005 = **$0.0455 (99%)** | 변동비 거의 없음 |
| 인프라 고정비 | $300/월 | Postgres + Redis + MinIO + FastAPI (DigitalOcean 4 vCPU 기준) |
| 마케팅비 | C: $5K / B: $30K / O: $80K (Year-1 누적) | 한국발 글로벌 소셜 앱 평균 (Maum 시드 7억 ÷ 4년 ÷ 다양성 ≈ ₩4천만/년 추정 → $30K 합리적) |

---

## 5. Bottom-up Model by Period

### 5.1 Base 시나리오 상세 (월별)

| Month | New Installs | Cumul Installs | MAU (코호트 합산) | Paying Users | Gross USD | Net USD (after 15% + cost) |
|---|---|---|---|---|---|---|
| M1 | 20,000 | 20,000 | 5,000 | 100 | $1,800 | $1,400 |
| M2 | 22,000 | 42,000 | 9,000 | 180 | $3,200 | $2,400 |
| M3 | 25,000 | 67,000 | 13,000 | 260 | $4,700 | $3,700 |
| M4 | 28,000 | 95,000 | 18,000 | 360 | $6,500 | $5,200 |
| M5 | 31,000 | 126,000 | 23,000 | 460 | $8,300 | $6,700 |
| M6 | 35,000 | 161,000 | 30,000 | 600 | $10,800 | $8,800 |
| M7 | 38,000 | 199,000 | 37,000 | 740 | $13,300 | $10,900 |
| M8 | 41,000 | 240,000 | 45,000 | 900 | $16,200 | $13,400 |
| M9 | 43,000 | 283,000 | 53,000 | 1,060 | $19,100 | $15,900 |
| M10 | 46,000 | 329,000 | 62,000 | 1,240 | $22,300 | $18,600 |
| M11 | 48,000 | 377,000 | 71,000 | 1,420 | $25,600 | $21,400 |
| M12 | 50,000 | 427,000 | 80,000 | 1,600 | $28,800 | $24,200 |
| **누적 (Year-1)** | **427,000** | — | — | — | **$160,600** | **$132,600** |

(W1은 M1의 약 25% 가정 → Net $350)

> **주의**: 위 표의 누적 Net은 Executive Summary의 $200K와 약 1.5배 차이가 있다. 그 이유는 §1에서는 "M12 단월 매출 $32K + 12개월 합산 시 약간의 가속"을 반영했고, 여기서는 등비증가만 가정한 보수적 계산이기 때문. **이 갭 자체가 가정의 민감도를 보여주는 신호**(§7 Sensitivity 참조).

### 5.2 Conservative 시나리오 (요약)

- M12 누적 설치: ~85,000 (Maum Year-1 수준)
- M12 단월 MAU: ~15,000
- M12 단월 paying users: ~150
- **Year-1 누적 Net**: ~$60,000 (≈ ₩8천만원)
- 손익: 인프라 $3,600 + 마케팅 $5,000 = $8,600 비용 → **Net Operating ~ $51,000**

### 5.3 Optimistic 시나리오 (요약)

- M12 누적 설치: ~1.4M (Maum Year-3과 Year-4 사이)
- M12 단월 MAU: ~250,000
- M12 단월 paying users: ~8,750
- iOS M6 출시로 +20% 추가 가산
- **Year-1 누적 Net**: ~$620,000 (≈ ₩8.4억)
- 손익: 인프라 $4,000 + 마케팅 $80,000 + OpenAI $5,000 = $89,000 비용 → **Net Operating ~ $531,000**

→ Maum Year-3 ($0.8M) 근접. Mate Chat이 4년 후 출시 + AI 차별점 + 9개 언어를 살린 케이스.

---

## 6. Cost Structure

### 6.1 단위 경제 (Unit Economics)

| 항목 | 값 |
|---|---|
| 평균 결제 단가 (Base) | ₩12,000 ≈ $8.89 |
| Google Play 수수료 (15%) | -$1.33 |
| **Net per purchase** | **$7.56** |
| 결제당 클로버 | 1,100개 (₩12,000 패키지) |
| 클로버 1개당 Net 매출 | $0.00687 |

### 6.2 OpenAI 변동비 (마진 분석)
- 1,100 클로버 = 220 AI 메시지
- OpenAI 원가: 220 × $0.0005 = $0.11
- **실질 마진: ($7.56 - $0.11) / $8.89 = 83.7%** (Google 수수료 제외 시 99%)

→ AI 사용량 폭증해도 마진은 안정적. **변동비 리스크는 거의 없다.**

### 6.3 고정비 (월)
- 백엔드 인프라: $300
- 도메인/이메일/Sentry/모니터링: $50
- (마케팅 별도)

→ Year-1 고정비 ~$4,200 (마케팅 제외)

---

## 7. Sensitivity Analysis

**Base 시나리오 Year-1 누적 Net Revenue ($133K) 기준 단변량 민감도**:

| 변수 | -30% | Base | +30% | 영향 |
|---|---|---|---|---|
| New Installs (월별) | $93K | $133K | $173K | ±30% (선형) |
| Paying User Rate | $93K | $133K | $173K | ±30% (선형) |
| ARPPU | $93K | $133K | $173K | ±30% (선형) |
| D30 retention | $90K | $133K | $176K | 비선형 (코호트 누적 효과) |
| 마케팅 효과 (CAC) | $115K | $133K | $151K | 약 ±15% (Year-1엔 영향 작음) |

**핵심 인사이트**:
- Year-1엔 **유저 획득량(New Installs)이 가장 큰 단일 변수**. 마케팅 캠페인 효과가 검증되지 않은 상태에선 ±50% 폭으로 봐야 안전.
- ARPPU와 Paying Rate는 **상호 상관**이 있음 (UX 좋은 앱은 둘 다 높음). 독립 변수로 보면 안 됨 → 시나리오 묶음으로 다루는 게 정확.

---

## 8. Risks & Caveats

| 리스크 | 영향 | 대응 |
|---|---|---|
| **iOS 미출시** (Apple OAuth 미구현) | TAM 50% 차단 (한·일 iOS 비중 30~50%) | M6까지 출시 목표; Optimistic 시나리오만 반영 |
| **콘텐츠 모더레이션 부족** | 신고 누적 → Play Store 디모션 | M3 내 키워드 필터 + 신고 자동화 (TODO.md v1.2) |
| **OpenAI 가격 변동** | 마진은 견고하나 absolute 비용 증가 시 가격 인상 압박 | GPT-4o-mini 기준; gpt-4o로 fallback 시 +6배 비용 → 모델 선택 신중 |
| **글로벌 광고 규제** (COPPA, GDPR) | 마케팅 채널 제한 | COPPA 13세 확인 완료; GDPR은 미흡 (별도 문서 필요) |
| **챗봇 마켓플레이스 미구현** | UGC 부재 → 콘텐츠 기근 | v1.3 우선순위 고려 |
| **언어 9개 마케팅 비용 분산** | 채널별 채택률 낮음 | Year-1엔 한·일·영 3개에 80% 집중 권장 |
| **Maum과 음성/번역 격차** | Maum 사용자가 Mate Chat으로 전환 안 함 | "보완재"로 포지셔닝, 직접 경쟁 회피 |

---

## 9. Upside Levers (Base를 Optimistic으로 올릴 트리거)

| 트리거 | 매출 영향 | 구현 난이도 |
|---|---|---|
| iOS App Store 출시 (M6) | +25-40% 매출 | 중 (Apple OAuth + iOS 빌드) |
| 챗봇 마켓플레이스 (UGC) | +50-100% paying rate | 중-높음 (창작자 수익 분배 시스템) |
| 광고 (배너/리워드) 추가 | +$0.3-0.8/MAU/월 | 낮음 (AdMob 통합) |
| 구독제 신설 ($4.99/월) | Replika식 25% 전환 노릴 시 +200% | 높음 (가격 실험 + 차별 가치) |
| 메시지 번역 봇 (특정 언어쌍) | M3 + Maum 사용자 흡수 | 중 (OpenAI API 추가 호출) |
| 인플루언서 마케팅 (TikTok/유튜브) | CAC ~$0.5 → 설치 +50K/월 가능 | 낮음 (예산만 필요) |

---

## 10. 후속 권고 (출시 임박 시점 액션)

원격 PR은 취소되어 본 리포트가 v1.0 기준선 단독 산출물. §13~§15의 검증 결과를 바탕으로 다음 액션을 출시 전 또는 직후에 집행:

1. **출시 D-7까지 (P3 — §15.3)**: Mixpanel 또는 Amplitude 통합 + 60일 3-metric dashboard 배포. 현재 Firebase Analytics만으론 D7 retention, paying conversion, organic install ratio 정확히 측정 불가.
2. **출시 D-3까지 (§14.4 The Assignment)**: 베타 5명 (한국 25~32 여성) 직접 사용시키고 Welcome 200 클로버 소진 시간·친구 초대율·결제 시간 측정. 5명도 어렵다면 본인+가까운 지인 3명이라도.
3. **출시 D+30 시점**: 1차 metric 점검 (early signal). 위 3개 metric 중 어느 쪽이 빨리 무너지는지 패턴 파악.
4. **출시 D+60 결정 게이트 (P3 핵심)**: 3-metric 평가 후 확장/조정/pivot 결정. 셋 중 1개라도 미달이면 segment 재정의. 셋 다 미달이면 즉시 마케팅 중단.
5. **출시 D+90**: PMF 증거 3종 (paying 1K / D30 8% / K-factor 0.3) 진척률 평가. Year-2 외부 자금 조달 또는 자생적 성장 트리거 결정. P1 (일본 진출) 검토 시작점.

**중요**: §1 Executive Summary 표는 **v1 초안 숫자 그대로 유지**되어 있으나, **§13~§15 검증을 거쳐 의사결정에 직접 사용하기에 부적합한 상태**다. 산식 오류 (F1 ARPPU $9 vs $18 모순), CPI fantasy (F5 $0.079 vs 실제 $1.5~4), iOS 부재 영향 (F7), 비교군 cherry-pick (F10) 등이 §13에 documented. 의사결정자는 §1을 그대로 참조하지 말고 **§13.4 v2 재계산 표 + §14.3 v3 표 + §15 P5 PMF KPI**를 우선 입력으로 사용할 것.

---

## 11. 가정 변경 로그 (작성 중 변경된 결정)

| 결정 | 선택 | 이유 |
|---|---|---|
| Maum 매출 곡선 역산 시 200% 일정 가정 | 채택 | 2023→2024만 공식 데이터, 그 이전은 추정 (보수적으로 일정 가정) |
| 결제 모델로 게임 IAP 비교 사용 | 채택 | 클로버는 소모성 IAP라 Replika(구독 25%)보다 게임이 더 가까움 |
| OpenAI를 GPT-4o-mini 기준 | 채택 | 코드는 `chatbot.model` 사용자 지정이지만 비용 효율 위해 mini 가정 |
| iOS 출시 시점 M6 | 보수 가정 | TODO.md v1.1 이후 미정 → Optimistic만 반영 |
| 한국 환율 1 USD = ₩1,350 | 고정 | 2026-04 기준 |

---

## 12. Verification Checklist

- [x] Executive Summary 표 15셀 모두 숫자
- [x] 모든 가정에 출처 (URL 또는 코드 경로)
- [x] Gross→Net 수식 §2 명시
- [x] 시나리오 정의 §2 명시
- [x] OpenAI 변동비 §6 명시
- [x] 민감도 분석 §7 (단변량)
- [x] 환율 §0 고정 — **§13에서 재설정 필요**
- [x] **codex adversarial challenge (2026-04-22 13:13 UTC 실행)** — 12개 finding, §13 참조
- [x] **office-hours Startup 모드 (2026-04-23 실행)** — Persona A 우세, 베타 0명 갭 확인, §14 참조
- [x] **plan-ceo-review EXPANSION 모드 (2026-04-23 실행)** — P3+P5 채택, §15 참조
- [ ] §13~§15 반영 후 숫자 재계산 및 Executive Summary 재작성 (사용자 후속 작업)

---

## 13. Codex Adversarial Challenge 결과 (2026-04-22)

> **실행 환경**: codex CLI consult mode, model_reasoning_effort=xhigh, 토큰 사용 3,495,429
> **세션 ID**: `019db553-4dca-72b3-ac7d-94ffb11287f9`
> **한 줄 결론**: "$200K Base는 방어 가능한 base가 아니라, **산식 불일치 + comparator 오용 + OpEx 누락 + fantasy CAC**가 겹친 공격적 upside case."

### 13.1 Critical Findings (치명적)

**F1. Base 산식 내부 불일치 — 가장 치명적**
- §4.3에서 Base ARPPU = **$9** 선언, §5.1 월별 Gross USD 표는 사실상 **$18 사용**
- 검증: `sum([100,180,260,360,460,600,740,900,1060,1240,1420,1600]) = 8,920` payer-month
  - $9 × 8,920 = **$80,280** (선언 ARPPU 기준 정답)
  - 표의 $160,600 = $18 × 8,920 (실제 표 숫자)
- **결론**: 선언 ARPPU로 재계산 시 **Year-1 Gross ≈ $80K → Net ≈ $68K** = Conservative 시나리오 수준
- 즉 현재의 Base는 "보수적 base"가 아니라 **upside를 암묵 중첩한 값**

**F2. AI 메시지 단가 / 평균 패키지 단가 모순**
- §6.1: Base 평균 패키지 = ₩12,000 / 1,100 클로버 → 클로버당 ₩10.91
- §4.4: AI 메시지당 매출 = $0.046 (= ₩5,000/400 **최소 패키지** 단가 기준)
- 같은 문서에서 유닛 레이트를 **편한 쪽으로 바꿔 씀**. 평균 패키지 기준이면 $0.034로 낮아짐.

**F3. Creator Subsidy 누락**
- `clover_service.py:399-438` — AI 채팅 1회당 사용자 -5 클로버 + **creator +1 클로버** (creator ≠ user 시)
- §6.2 "마진 99%"는 이 20% 리베이트 무시. 실제 contribution margin ≈ **79%** (creator가 주로 타인일 때)

**F4. OpenAI 모델 가정 오류**
- §4.4: "GPT-4o-mini 고정" 가정
- 실제 코드 (`schemas/chatbot.py:22`, `config.py:75`): 챗봇 기본 = **`gpt-5-mini`**, 번역 LLM 폴백도 `gpt-5-mini`
- GPT-5 계열 가격이 4o-mini보다 비쌈 → 변동비 과소계상 (~5배)

**F5. Fantasy CPI**
- §4.4: Year-1 마케팅 $30K로 New Installs 380K → **CPI = $0.079**
- Business of Apps 2025: Android 글로벌 CPI **$1.5~4.0**, APAC $1.5~3.0
- 75% organic 가정에도 paid CPI $0.32 → 비현실
- 실제 가능치: $0.5 CPI면 $30K로 ~60K, $1.5면 ~20K
- 380K는 예산 계획이 아닌 **증거 없는 virality 가정**

### 13.2 High Findings (중대)

**F6. 환율 1,350 → 2026-04 실제 ~1,495**
- 2026 YTD 평균 ~₩1,468, 2026-04 평균 ~₩1,495 (codex FX 확인)
- → KRW 비용 ~10% 과소계상
- **권장**: Low/Mid/High 밴드 ₩1,450/1,500/1,550

**F7. iOS 부재의 구조적 영향 과소평가**
- Statcounter 2026-03: 일본 iOS **60.58%**, 한국 iOS 29.93%
- 일본을 core market에 넣는 순간 iOS 부재는 optional upside 손실이 아니라 **구조적 TAM 훼손**
- 현 상태: `oauth_service.py:188` Apple OAuth TODO, `TODO.md:12` iOS 프로젝트 설정 미완
- **권장**: Base/Conservative에 Android-only discount, iOS는 별도 gate

**F8. Payer Rate 카테고리 전이 부적절**
- §4.3: 게임 IAP 평균 1.5~3% → Mate Chat Base 2%
- 게임은 compulsion loop + sink 설계. Mate Chat은 cold-start social graph
- **권장**: 초기 cohort 실측 전까지 0.5~1.5% band

### 13.3 Medium Findings (중요)

**F9. Net Revenue 정의 불완전 → "Contribution Margin before OpEx"로 리네이밍**
- §2.2: Gross - store fee - OpenAI - infra_fixed
- 누락: 번역 provider, analytics 스택, T&S 운영, CS/환불/분쟁, 법무, 현지화 QA, 크리에이티브 제작, attribution 툴, 이미지 egress

**F10. 비교군 Cherry-Picking**
- Acquisition은 Maum/Azar/HelloTalk 차용, Monetization은 Replika/Bumble/Character.AI halo 얹음
- **권장**: acquisition = Maum·Azar·HelloTalk·Tandem, IAP monetization = consumable social apps, AI companion = upside sensitivity 분리

**F11. Empty-Room Penalty 무시**
- 소셜 채팅의 첫 세션 = "대화할 사람·안전·재방문 이유" 부재 시 retention 붕괴
- 기존 강자 해자 = 기능 수가 아닌 **liquidity & trust**
- **권장**: Base를 "한·일·동남아 3개국"이 아닌 **"1국가/1페르소나/1채널 liquidity proof"**로 재정의

**F12. Scenario 변수 맵핑 부재**
- Executive $200K vs Bottom-up $132.6K (50% 차이)
- 시나리오가 측정 가능한 변수에 맵핑 안됨
- **권장**: 공통 산식 1개 + 변수 5개(`CPI`, `platform_mix`, `payer_rate`, `iOS_shipped`, `D30_retention`) 변동

### 13.4 산식 재계산 (F1~F5 반영 Base v2)

| 항목 | v1 (원본) | v2 (codex 반영) |
|---|---|---|
| ARPPU 월간 | $9 (선언) → $18 (실제 표) | $9 (일관 적용) |
| Payer × Gross | 8,920 × $18 = **$160,600** | 8,920 × $9 = **$80,280** |
| Store fee (15%) | -$24,090 | -$12,042 |
| Creator subsidy (20%) | 미반영 | -$16,056 (AI 채팅 매출 추정분의 20%) |
| OpenAI (gpt-5-mini 추정) | $300 | ~$1,500 (5배) |
| Infra | $3,600 | $3,600 |
| 번역·T&S·CS·법무 OpEx | 미반영 | -$24,000 (보수, $2K/월) |
| **Year-1 Net (v2 Base)** | **$132,600** | **~$23,000** |

→ **v2 Base ≈ Year-1 Net $23K** (원본 v1의 1/6, 원본 Conservative $60K보다도 낮음)

### 13.5 권장 조정안 (Draft, office-hours·CEO review 후 확정)

| 시나리오 | v1 Year-1 Net | **v2 권장** | 주요 조정 |
|---|---|---|---|
| Conservative | $60K | **$8K** | Android-only, 게임 IAP 비교 제거, CPI $1.5 → 설치 20K, D30 3% |
| **Base** | $200K | **$25K** | 산식 오류 수정, OpEx 반영, CPI $0.8 → 설치 40K, iOS 미포함 |
| Optimistic | $620K | **$150K** | iOS M6 출시 + Japan liquidity 확보 + paid UA $80K |

### 13.6 후속 조치 TODO (codex 권고 반영)

- [ ] §0 환율을 ₩1,450/1,500/1,550 밴드로 변경
- [ ] §2 "Net Revenue" → "Contribution Margin before OpEx"로 리네이밍
- [ ] §2.2 수식에 번역 provider, analytics, T&S, CS, 법무, attribution 추가
- [ ] §2.3 시나리오 정의를 측정 변수(`CPI`, `platform_mix`, `payer_rate`, `iOS_shipped`, `D30`) 기반으로 재정의
- [ ] §4.1 New Installs를 CPI $0.5~$1.5 밴드로 예산 역산
- [ ] §4.3 payer rate 0.5~1.5% band로 재설정 (게임 IAP 비교 제거)
- [ ] §4.4 OpenAI 기본 모델 `gpt-5-mini`로 변경, 변동비 5배 가산
- [ ] §4.4 Creator subsidy 20% 항목 추가
- [ ] §5 Base 테이블 ARPPU 일관성 수정 (현재 표 vs 선언 둘 중 선택)
- [ ] §6 마진 99% → 79% (creator subsidy 차감)
- [ ] §8 iOS를 Optimistic 전용 upside에서 "분리된 gate"로 격상; Base/Conservative에 Android-only discount
- [ ] §1 Executive Summary를 v2 숫자로 재작성
- [ ] §3 비교군을 acquisition / IAP monetization / AI companion premium 3개로 분리

---

## 14. Office Hours (Startup Mode) 결과 (2026-04-23)

> **방식**: YC 6 forcing question을 코드/문서/codex 발견 기반 가설로 사전 작성 후 product owner 검증.
> **모드**: Startup, Pre-product (베타 0명), Solo
> **한 줄 결론**: "narrowest wedge는 살아있으나 demand evidence가 0. Year-1 수익 예측은 priors 위 priors."

### 14.1 6 Question 응답 요약

| Q | 가설 | 응답 | 채택 |
|---|---|---|---|
| Q1 Demand | Welcome 200 클로버 첫날 소진 후 추가 결제 사용자 | 동의 | ✅ (단, 베타 데이터 부재) |
| Q2 Status Quo | ChatGPT/Character.AI/Replika + HelloTalk/Tandem 분리 사용 | 동의 | ✅ |
| Q3 Persona | A=한국 25~32 여성 외로움 / B=20대 남성 챗봇 크리에이터 | **A 우세, B도 존재** | ✅ A 우선 |
| Q4 Wedge | 친구 그룹 + AI 봇 하이브리드 채팅 | 동의 | ✅ |
| Q5 Observation | (가설: 미정) | **베타 데이터 없음 — 미관찰** | ❌ **최대 갭** |
| Q6 Future-Fit | AI commodity화 시점에 social context catalyst가 차별 | 동의 | ✅ |

### 14.2 Year-1 Segment 집중 정의 (재정의)

codex F11 ("1국가/1페르소나/1채널 liquidity proof")과 office-hours Q3·Q4 응답 결합:

| 차원 | 결정 |
|---|---|
| **국가** | 한국 (출시국, Persona A 모국) |
| **페르소나** | 한국 25~32세 여성, 평일 21~24시 외로움 해소 + 외국 친구 호기심 |
| **채널** | TikTok·Instagram Reels·트위터 한국 (외로움 + AI 캐릭터 콘텐츠 high engagement) |
| **Wedge** | "혼자가 아니라 친구 + AI랑 같이" (Replika는 1:1만, 사람 친구가 그립다) |
| **결제 트리거** | Welcome 200클로버 첫날 소진 → 친구 초대 → 친구 방에 봇 추가 → 4명 × AI 호출 → 200 클로버 빠르게 소진 → ₩5K 패키지 결제 |

### 14.3 §4.3 가정 재조정 권고 (office-hours + codex F8 결합)

| 항목 | v1 (원본) | **v2 (codex)** | **v3 (office-hours 종합)** |
|---|---|---|---|
| Payer Rate (월간) | 2.0% | 0.5~1.5% | **1.0%** (Persona A 집중 시 평균 이상 가능, 베타 검증 전엔 보수) |
| ARPPU (월간) | $9 | $9 (일관) | **$11** (Persona A는 외로움 → 결제 빈도↑, Replika $13에 근접) |
| 평균 패키지 | ₩12,000 | ₩12,000 | **₩9,000** (Persona A는 ₩5K 반복 결제 패턴 가설) |
| Year-1 Net (Base) | $200K | $25K | **~$30K** (한국 단일 시장 + Persona A 집중 + 베타 0명 디스카운트) |

### 14.4 결정적 갭 (Q5 답변 기반)

> **"베타 데이터가 없다"는 것은 모델 전체의 가장 큰 단일 리스크**

이 답변은 다음 모든 가정을 priors(사후 미보정)로 전락시킴:
- Persona A 우세 → 친구·지인 5~10명에게 라이브 빌드 사용시키기 전엔 가설
- Welcome 200 첫날 소진 비율 → 미측정
- 친구 방 + 봇 사용 패턴 → 미측정
- ARPPU·payer% → 모두 비교군 transfer

**The Assignment (office-hours skill 권고)**: 출시 전 또는 직후 1주일 내, 한국 25~32 여성 5명에게 mate-chat을 직접 사용시키고 다음을 측정:
1. Welcome 200 클로버 소진까지 걸리는 시간
2. 친구 초대 액션을 취한 비율
3. AI 봇을 친구 방에 추가하는 비율
4. 첫 결제까지 걸리는 시간 (또는 결제 안 한 이유)

이 5명의 데이터가 §4.3 가정의 prior → posterior 전환 base. 5명도 어렵다면 본인+가까운 지인 3명이라도.

### 14.5 Design Doc 핵심 권고

- Year-1 단일 페르소나/채널 집중 (한국 25~32 여성 / TikTok·Instagram Reels)
- 베타 5명 사용 데이터 확보를 출시 후 7일 KPI로 설정
- Payer rate 1%, ARPPU $11, 평균 패키지 ₩9K로 §4.3 재조정
- §4.1 New Installs를 한국 Meta CPI $0.8~1.5 밴드로 역산

---

## 15. CEO Review (EXPANSION Mode) 결과 (2026-04-23)

> **방식**: plan-ceo-review skill EXPANSION mode. 5개 expansion proposal 제시 후 사용자 cherry-pick.
> **모드**: SCOPE_EXPANSION (greenfield revenue forecast 맥락)
> **사용자 결정**: P3 + P5 채택 (추천대로). P1/P2/P4는 wedge 검증 후 단계적 확장.

### 15.1 "10x Version" 한 문장 비전

> **"외로운 시간을 친구 + AI랑 같이 보내는 곳" — Replika가 1:1 외로움 카테고리 owner라면, Mate Chat은 'AI를 친구 사이에 끼워넣는 catalyst' 카테고리 owner.**

이 비전은 §14 Persona A (한국 25~32 여성 외로움 해소) wedge와 §13 F11 (empty-room penalty 회피) 권고를 통합한 cathedral framing.

### 15.2 5개 Expansion Proposal 결정 매트릭스

| # | 제안 | Effort | 매출 영향 | 결정 |
|---|---|---|---|---|
| P1 | 일본 시장 동시 침투 (Year-1 M3) | M | +$15~50K | **DEFERRED** — wedge 검증 후 (60일 metric 통과 시) |
| P2 | 캐릭터 봇 마켓플레이스 (Year-1 H2) | L | +$50~150K | **DEFERRED** — Year-2 평가 |
| **P3** | 60일 결정 트리거 metric ⭐ | S | $0 (간접 ₩30K+ 절약) | ✅ **ACCEPTED** |
| P4 | 광고 수익 (AdMob 배너+리워드) | S | +$20~80K | **DEFERRED** — UX 검증 후 |
| **P5** | Year-1 KPI를 PMF 증거로 재정의 | 0 | $0 (의사결정 quality) | ✅ **ACCEPTED** |

### 15.3 P3 — 60일 결정 트리거 Metric (채택)

**Critical Gap**: 현재 리포트는 12개월 누적만. 실무 의사결정엔 60일 시점 데이터가 결정적.

**60일 시점 3-Metric Decision Framework**:

| Metric | Threshold | 미달 시 액션 |
|---|---|---|
| **D7 retention** | > 15% (게임 평균 11~15% 상회) | Onboarding flow 재설계 |
| **Paying user 전환** | > 0.5% (월간) | Welcome 보너스/패키지 재가격 |
| **Organic install ratio** | > 40% (paid 60% 이하) | Wedge 재정의 또는 segment pivot |

**Trigger Logic**: 3개 중 **1개라도 미만이면 segment 재정의 또는 pivot 검토**. 3개 모두 미만이면 즉시 마케팅 중단.

**Implementation 요건**:
- 현재: Firebase Analytics만 (codex F12 지적). Mixpanel 또는 Amplitude 통합 필요
- 60일 dashboard: D7/D30 retention, paying conversion, install source breakdown
- Effort: S (1~2주)

### 15.4 P5 — Year-1 KPI를 PMF 증거로 재정의 (채택)

**기존 KPI**: Year-1 Net Revenue $25~30K (codex+office-hours 보정값)

**재정의 KPI**: 수익은 후행 지표. 진짜 KPI는 PMF 증거 3종 세트:

| KPI | Target (Year-1 종료) | 의미 |
|---|---|---|
| **Paying user count** | 1,000명 (codex F11 권고) | Liquidity proof |
| **D30 retention** | 8%+ (외로움 카테고리 평균 이상) | Product stickiness |
| **Organic K-factor** | 0.3+ (1명이 0.3명 데려옴) | Viral seed 형성 |

**3개 모두 달성 시**: Year-2 외부 자금 조달 또는 자생적 성장 트리거. 수익은 자동 후행.
**일부만 달성**: PMF 부분 증거. Year-2 segment 확장 신중.
**모두 미달**: PMF 부재 인정 후 pivot 또는 정리.

이 framing은 founder의 **잘못된 수익 chasing 회피**가 핵심. $25K Year-1 자체가 north star가 되면 단기 monetization tactic에 집중하다 PMF 못 증명한 채 Year-2 진입.

### 15.5 채택 결정의 통합 효과

P3 + P5 결합 시 shadow 리포트의 본질적 변경:
- **§1 Executive Summary 재작성 필요**: "Year-1 Net Revenue 범위" → "Year-1 PMF 증거 + 잠정 수익 범위" 표 변경
- **§2 시나리오 정의 변경**: Conservative/Base/Optimistic을 PMF KPI 달성도 기반으로 재정의
- **§4.4 측정 인프라 항목 추가**: Mixpanel/Amplitude 통합 비용 (~$50/월 + 통합 1~2주)
- **새 §16 (옵션)**: 60일 decision framework 단독 섹션 권고

### 15.6 Deferred 항목 (Year-2 또는 wedge 검증 후 재평가)

- **P1 일본 진출**: 60일 한국 metric 통과 시 M3 시작. 일본어 i18n 이미 완료 (`docs/24-flutter-i18n-preparation.md`).
- **P2 마케팅플레이스**: Year-2. K-pop IP 저작권 검토 + NSFW 모더레이션 정책 선결.
- **P4 AdMob**: UX 저하 risk 평가 후 H2. Free user에만 노출 + 결제 전환 차단 회피 설계 필수.

### 15.7 후속 작업 우선순위 (3개월 로드맵)

| 시점 | 작업 | 출처 |
|---|---|---|
| **출시 D-7** | Mixpanel/Amplitude 통합 + 3-metric dashboard 배포 | P3 |
| **출시 D-3** | 베타 5명 (한국 25~32 여성) 초청, §14.4 The Assignment 측정 | office-hours |
| **출시 D+30** | 1차 metric 점검 (early signal) | P3 |
| **출시 D+60** | **결정 게이트** — 3-metric 평가 후 확장/조정/pivot | P3 |
| **출시 D+90** | PMF 증거 3종 진척률 평가, P1(일본) 검토 | P5 |

---

## 16. PMF KPI 달성 시 잠정 수익 환산 (Year-1 ~ Year-3)

> **목적**: §15.4 P5에서 "수익은 후행 지표"로 KPI를 재정의했으나, 의사결정자가 자금 조달·예산 책정·기회비용 평가를 위해 매출 감을 잡을 필요는 여전히 존재한다. 본 섹션은 **§15.4 PMF KPI 3종 달성을 전제로** 잠정 수익을 환산한다.
> **주의**: 이 환산은 "달성한다는 가정"이 깔린 후행 추정이며, 달성 자체의 확률은 §16.6에서 별도 평가한다.
> **환율**: 1 USD = ₩1,350 고정 (codex F6은 ₩1,495 권고 — 본 환산은 보수 환율 사용).

### 16.1 산정 전제

§14.3 v3 권장값 기반 (한국 단일 segment + Persona A 집중):

| 변수 | 값 | 근거 |
|---|---|---|
| 평균 결제 단가 (Net) | $6 (보수) / $10.50 (중간) / $18 (낙관) | §14.3 ARPPU $11 × 월 결제 횟수 0.5~2회 |
| Google Play 수수료 | 15% (첫 $1M까지) | §4.4 small business program |
| Creator subsidy + 기타 OpEx | 차감 반영 | §13.4 v2 항목 |
| Year-1 누적 paying user-month | ~4,650 (보수) / ~6,300 (선형) | **S-곡선 점증 가정** (M1: 50명 → M12: 1,000명, 초기 cohort retention churn으로 평균 ~390명/월). 순수 선형 누적 가정 시 평균 525 × 12 = 6,300. 본 환산은 보수성 위해 4,650 사용 (~25% 디스카운트). |
| Year-1 종료 paying user count | 1,000명 (§15.4 KPI Target) | PMF 증거 |

### 16.2 Year-1 누적 매출 (KPI 달성 경로 중)

KPI 달성은 **연말에 1,000명 도달**을 의미하므로, 1년 내내 1,000명이 아니다. 누적은 점증 곡선:

| 시나리오 | 산식 | Year-1 누적 Net | KRW 환산 |
|---|---|---|---|
| 보수 (월 1회 결제) | 4,650 × $6 × 0.85 - $5K | **~$18,700** | ~₩2,500만원 |
| 중간 (월 1.5회) | 4,650 × $10.5 × 0.85 - $8K | **~$33,500** | ~₩4,500만원 |
| 낙관 (월 2회) | 4,650 × $18 × 0.85 - $13K | **~$58,000** | ~₩7,800만원 |

→ Year-1 누적 매출은 절대값이 작아 보이지만, 이는 **단골이 연말에 도달**하는 점증 효과. 1년차의 진짜 의미는 §16.3의 종료 시점 run rate.

### 16.3 Year-1 종료 시점 Monthly Run Rate (핵심 지표)

PMF KPI 달성 = 안정적 paying 1,000명 보유 = **Year-2 시작 시점의 안정 매출**:

| 시나리오 | 산식 | 월 매출 (Net) | 연 환산 (Year-2 baseline) |
|---|---|---|---|
| 보수 | 1,000 × $6 × 0.85 | **$5,100/월** (~₩690만) | $61K/년 (~₩8,300만원) |
| 중간 | 1,000 × $10.5 × 0.85 | **$8,925/월** (~₩1,200만) | $107K/년 (~₩1.4억원) |
| 낙관 | 1,000 × $18 × 0.85 | **$15,300/월** (~₩2,070만) | $184K/년 (~₩2.5억원) |

→ **Year-2 시작 시점 monthly run rate가 KPI 달성의 진짜 가치**. 1년차의 누적이 작아도 종료 시점 안정 매출이 형성되면 Year-2부터 본격 매출.

### 16.4 Year-2 자연 성장 시나리오 (K-factor 0.3 + D30 8% 가정)

§15.4 KPI의 K-factor 0.3 (1명이 0.3명 데려옴) + D30 8% (단골 누적)는 자연 성장 가능 조건. Year-2 paying user 확장 시나리오:

| Year-2 종료 paying | 산식 (중간 ARPPU $10.5) | Year-2 연 매출 (Net) | KRW 환산 |
|---|---|---|---|
| 2,000명 (2배 확장) | 2,000 × $10.5 × 12 × 0.85 | **~$214K** | ~₩2.9억원 |
| 3,000명 (3배 확장) | 3,000 × $10.5 × 12 × 0.85 | **~$321K** | ~₩4.3억원 |
| 5,000명 (5배 확장 + iOS) | 5,000 × $13 × 12 × 0.85 | **~$663K** | ~₩9억원 |

→ Year-2 5,000명 시나리오 ≈ **Maum Year-3 ($800K) 70% 도달**. iOS 진출 + 일본 시장 추가 시 Maum Year-3 추월 가능성.

### 16.5 Year-3 시나리오 (Maum 추격)

Year-2 PMF 검증 후 paid UA 확장 + 마켓플레이스(P2) 또는 광고(P4) 추가 시:

| 시나리오 | Year-3 paying | 연 매출 (Net) | Maum 비교 |
|---|---|---|---|
| 보수 | 7,000명 | **~₩6억원** | Maum Year-3 ($0.8M ≈ ₩10.8억) 55% |
| 중간 | 12,000명 | **~₩15억원** | Maum Year-3 동등 |
| 낙관 | 20,000명 + iOS + 일본 | **~₩30억원** | Maum Year-4 ($2.4M ≈ ₩32억) 동등 |

### 16.6 KPI 달성 확률과 기대값

§15.4 PMF KPI 3종 동시 달성 확률은 신생 소셜 앱 base rate 기준 **20~30%**로 보수 추정. 이를 반영한 기대값:

| 시나리오 | 달성 시 Year-2 매출 | 달성 확률 | 기대값 (Year-2) |
|---|---|---|---|
| 보수 | ₩8,300만 | 30% | ~₩2,500만 |
| 중간 | ₩1.4억 | 25% | ~₩3,500만 |
| 낙관 | ₩2.5억 | 20% | ~₩5,000만 |

→ **KPI 미달 시나리오 (확률 70~80%)**: Year-1 매출 ₩500만~₩2,000만 수준에 머물고 Year-2 빠른 감쇠 또는 정리. 이 시나리오에서 §15.7의 D+60 결정 게이트가 손실 최소화 핵심.

### 16.7 의사결정 권고 (§15.4 P5와 일관)

1. **Year-1엔 매출보다 PMF 증거 (§15.4 KPI 3종) 추적이 우선**. 본 §16 환산은 "달성 시 후행 따라옴"의 잠정 감일 뿐 north star가 아니다.
2. **Year-2 시작 시점 monthly run rate ($5K~$15K/월)가 사업 지속 가능성의 1차 검증**. 이 수준 미달 시 자생적 성장 어려움 → 외부 자금 조달 또는 sunset 결정.
3. **Year-3 Maum 추격은 Year-2 검증 + 일본·iOS·UGC(P1·P2) 단계적 확장이 모두 성공한 시나리오**. 단계마다 별도 결정 게이트 필요 (현재 미정의).
4. **달성 확률 20~30%는 모든 신생 앱의 통계적 현실**. 본 환산을 단정적 수익 약속으로 오용 금지. §15.7 D+60 결정 게이트를 정기 점검점으로 사용해 sunk cost 최소화.

---

## Sources

- [라이프오아시스 2024 매출 32억 — 머니투데이](https://news.mt.co.kr/mtview.php?no=2025013114535497187)
- [라이프오아시스 시드 7억 투자 — VentureSquare](https://www.venturesquare.net/839433) (원문 410 Gone, [archive.org 스냅샷](https://web.archive.org/web/2021*/venturesquare.net/839433) 권장)
- [LIFEOASIS 기업정보 — Wanted](https://www.wanted.co.kr/company/25642)
- [Sensor Tower State of Mobile 2025](https://sensortower.com/state-of-mobile-2025)
- [Character.AI 2025 by the Numbers](https://completeaitraining.com/news/character-ai-2025-by-the-numbers-20m-maus-322m-revenue-1b/)
- [Character.AI revenue & funding — Sacra](https://sacra.com/c/character-ai/)
- [Character.AI usage statistics — Business of Apps](https://www.businessofapps.com/data/character-ai-statistics/)
- [Replika ARPU & conversion — TechBuzz.ai](https://www.techbuzz.ai/articles/breaking-ai-companion-apps-hit-120m-revenue-run-rate)
- [Replika 25% conversion — Wikipedia](https://en.wikipedia.org/wiki/Replika)
- [AI Companion Apps Hit $120M Revenue — TechCrunch](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025/)
- [OpenAI API Pricing](https://openai.com/api/pricing/)
- [GPT-4o-mini pricing — pricepertoken.com](https://pricepertoken.com/pricing-page/model/openai-gpt-4o-mini)
- [App retention curves — Dogtown Media](https://www.dogtownmedia.com/the-first-90-days-after-app-launch-what-to-expect-and-how-to-thrive/)
- [Bumble ARPPU 2024 — Statista](https://www.statista.com/statistics/1233246/quarterly-bumble-arppu-by-app/)
- [ARPPU 정의 — Adjust Glossary](https://www.adjust.com/glossary/arppu/)
- 코드 참조: `mate_chat_flutter/lib/models/purchase.dart:37-42`, `mate_chat_backend/app/services/hybrid_chat_service.py:492`, `mate_chat_backend/app/services/clover_service.py:443-449`
- 내부 문서: `docs/27-competitive-analysis.md`, `docs/_launch-prep/iap-product-listing.md`, `TODO.md`
