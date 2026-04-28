---
title: "구글 플레이스토어 등록정보"
type: source
source_path: docs/23-google-play-store-listing.md
date_ingested: 2026-04-07
tags: [play-store, aso, store-listing, localization]
related:
  - "../sources/24-flutter-i18n-preparation.md"
  - "../sources/25-localization-glossary.md"
  - "../sources/launch-prep.md"
  - "../entities/google-play-store.md"
  - "../concepts/app-store-optimization.md"
---

# 구글 플레이스토어 등록정보

## 핵심 요약

Mate Chat의 Google Play Store 등록에 필요한 앱 이름, 간단한 설명, 자세한 설명을 한국어와 영어로 정리한 문서이다. ASO(App Store Optimization) 키워드 전략과 다국어 스토어 현지화 후속 계획을 포함한다.

## 주요 내용

### 앱 정보

- **앱 이름**: 메이트챗(MateChat)
- **패키지명**: `com.mate.mate_chat_flutter`
- **간단한 설명(ko)**: "전 세계 친구와 채팅하고 나만의 AI 메이트를 만들어보세요." (33자)
- **간단한 설명(en)**: "Global chat, new friends, and your own AI Mate" (47자)

### ASO 핵심 키워드

실시간 채팅, 소셜 메시징, AI 챗봇, 글로벌 채팅, GPT-4, 하이브리드 채팅, 메이트, 팔로우

### 강조 차별점 5가지

1. AI 챗봇 크리에이터 (경쟁 앱에 없는 고유 기능)
2. 하이브리드 AI 채팅 (사람 + AI 동시 대화)
3. 글로벌 인연 탐색 (국가/언어 필터링)
4. 웰컴 보너스 (무료 200 클로버)
5. 크리에이터 이코노미 (만든 AI로 보상 획득)

### 다국어 스토어 현지화

- 우선 대상: en, ja, zh-Hans, zh-Hant, es, id, vi, pt-BR (8개 locale)
- 별도 현지화 필요 자산: 앱 이름, 설명, 스크린샷 텍스트, 프로모션 문구, 업데이트 노트
- 앱 내 용어(Mate, Clover, AI Chatbot)를 스토어 카피에서도 일관되게 사용해야 함

## 시사점

- 스토어 메타데이터는 앱 내 i18n과 별도 운영이 필요하며, 앱 업데이트 시 함께 갱신해야 한다.
- Apple OAuth 출시, 푸시 알림 출시 등 기능 추가 시 설명 업데이트가 필요하다.
