---
title: "In-App Purchase (IAP)"
type: entity
source_count: 3
tags: [iap, clover, monetization, google-play, payment]
related:
  - "../entities/google-play-store.md"
  - "../sources/launch-prep.md"
  - "../sources/26-global-launch-readiness.md"
  - "../synthesis/launch-readiness.md"
---

# In-App Purchase (IAP)

## Overview

Mate Chat의 수익 모델은 가상화폐 **클로버(Clover)**의 인앱 결제 판매이다. 소모성 일회 구매(managed product) 방식으로, 5개 번들 상품을 제공한다. 경쟁사 Maum(풍선), Azar(젬)와 유사한 아시아/중동 시장에서 검증된 모델이다.

## Architecture/Structure

### 상품 구조

| 상품 ID | 기본 클로버 | 보너스 | 총 클로버 | 보너스율 | 티어 |
|---------|------------|--------|----------|---------|------|
| `clover_bundle_70000` | 5,600 | 2,400 | 8,000 | +43% | Diamond |
| `clover_bundle_45000` | 3,600 | 1,200 | 4,800 | +33% | Gold |
| `clover_bundle_25000` | 2,000 | 400 | 2,400 | +20% | Silver |
| `clover_bundle_12000` | 1,000 | 100 | 1,100 | +10% | Bronze |
| `clover_bundle_5000` | 400 | 0 | 400 | - | Basic |

### 다국어 상품 정보

8개 언어(ko, en, ja, zh-Hans, zh-Hant, es, id, vi, pt-BR)로 상품 이름과 설명이 준비되어 있다. 상품 ID에 `_bundleUiMeta` 맵 키가 매칭되어야 한다.

### 검증 흐름

- 백엔드: `app/services/clover_service.py`, `app/services/iap_verification_service.py`
- Google Play Developer API: `purchases.products.get()` 호출로 영수증 검증
- Apple StoreKit 2 Server API: `/inApps/v2/transactions/{transactionId}` (미구현)
- 이중 지출 방지: 검증된 영수증의 `orderId`/`transactionId`를 DB에 저장

## Key Details

- 클로버 사용처: AI 채팅, 프리미엄 기능
- Welcome 보너스: 이메일 인증 시 200 클로버 (3일 만료)
- 보너스/구매 분리 추적 (`usage_count`, `paid_usage_count`)
- Play Console 등록 경로: 수익 창출 > 제품 > 인앱 상품

## Dependencies

- Google Play Developer API (`google-api-python-client`)
- Apple StoreKit 2 Server API (미구현, iOS 출시 시 필요)
- PostgreSQL `clover_transactions` 테이블

## Known Issues

- Apple IAP 검증 미구현 (iOS 미출시)
- IAP bypass 설정은 프로덕션에서 비활성화 확인됨 (`config.py:117`)
- 구독 모델 미도입 (현재 소모성만, 경쟁사는 구독 $7~$20/월)

## Related

- [Google Play Store](../entities/google-play-store.md)
- [출시 준비 종합](../synthesis/launch-readiness.md)
