---
title: "Clover 가상 화폐 시스템"
type: entity
source_count: 3
tags: [clover, virtual-currency, iap, monetization]
related:
  - ../entities/in-app-purchase.md
  - ../entities/database-schema.md
  - ../sources/launch-prep.md
  - ../sources/19-implementation-status.md
---

# Clover 가상 화폐 시스템

## Overview

Mate Chat의 가상 화폐 시스템이다. 클로버(Clover)는 AI 채팅, 프리미엄 기능 등에 사용되는 소모성 가상 화폐로, 인앱 결제(IAP)로 구매하거나 Welcome 보너스로 획득할 수 있다. 아시아/중동 시장에서 검증된 소모성 가상화폐 모델(Maum의 풍선, Azar의 젬과 유사)을 채택했다.

## Architecture/Structure

### 획득 경로

- **Welcome 보너스**: 이메일 인증 완료 시 200 클로버 지급 (3일 만료)
- **인앱 결제**: Google Play / App Store를 통한 5개 번들 상품 구매

### 사용처

- AI 챗봇 대화 (클로버 차감)
- 크리에이터 수익 (클로버 획득)

### 거래 타입

`clover_transactions` 테이블의 ENUM 타입으로 관리:

| 타입 | 설명 |
|------|------|
| `purchase` | IAP 구매 |
| `ai_chat` | AI 채팅 사용 |
| `creator_earning` | 크리에이터 수익 |
| `welcome_bonus` | Welcome 보너스 지급 |
| `welcome_bonus_expiration` | Welcome 보너스 만료 차감 |
| `chatbot_create` *(legacy, 미사용)* | 초기 기획에서 챗봇 생성 시 차감 — 현재 적용되지 않음 |
| `chatbot_delete` *(legacy, 미사용)* | 초기 기획에서 챗봇 삭제 시 환불 — 현재 적용되지 않음 |

- `amount`: 양수(획득), 음수(소비)
- `balance_after`: 거래 후 잔액

### 보너스/구매 분리 추적

- `usage_count`: 전체 사용량
- `paid_usage_count`: 유료 구매분 사용량

## Key Details

- **잔액 관리**: `users.clover_balance` 컬럼 (>= 0 CHECK 제약)
- **IAP 검증**: Google Play Developer API로 영수증 검증, 이중 지출 방지 (`orderId` DB 저장)
- **Apple IAP**: 미구현 (iOS 미출시)
- **API 엔드포인트**: `app/api/v1/endpoints/clover.py` (5개 API)
- **서비스**: `app/services/clover_service.py`, `app/services/iap_verification_service.py`

### API 엔드포인트

| 엔드포인트 | 설명 |
|-----------|------|
| `GET /clover/balance` | 잔액 조회 |
| `GET /clover/transactions` | 거래 내역 조회 |
| `POST /clover/purchase` | IAP 구매 검증 및 클로버 지급 |
| `POST /clover/use` | 클로버 사용 |
| `GET /clover/products` | 상품 목록 조회 |

## Dependencies

- **PostgreSQL**: `clover_transactions` 테이블, `users.clover_balance`
- **Google Play Developer API**: IAP 영수증 검증
- **Apple StoreKit 2 Server API**: 미구현

## Known Issues

- Apple IAP 검증 미구현 (iOS 미출시)
- 구독 모델 미도입 (현재 소모성만)
- Welcome 보너스 만료 처리 로직 확인 필요

## Related

- [In-App Purchase](../entities/in-app-purchase.md) -- 5개 번들 상품 상세, 검증 흐름
- [Database Schema](../entities/database-schema.md) -- clover_transactions 테이블 구조
