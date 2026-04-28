---
title: "로컬라이제이션 용어집 및 운영 가이드"
type: source
source_path: docs/25-localization-glossary.md
date_ingested: 2026-04-07
tags: [l10n, glossary, terminology, translation]
related:
  - "../sources/24-flutter-i18n-preparation.md"
  - "../entities/i18n-system.md"
  - "../concepts/internationalization-strategy.md"
---

# 로컬라이제이션 용어집 및 운영 가이드

## 핵심 요약

Mate Chat Flutter 앱의 다국어 운영 시 제품 용어의 locale별 일관성 유지와 신규 문자열 추가 절차 표준화를 위한 문서이다.

## 제품 용어집

| 용어 | 원칙 | en 표기 | 비고 |
|------|------|---------|------|
| 메이트 | 제품 용어 유지, 일반 명사 번역 금지 | Mate | ja만 `メイト`, 나머지 `Mate` |
| 클로버 | `Clover` 고정, 통화/포인트 치환 금지 | Clover | 동사(구매, 충전 등)만 현지화 |
| 공식 | `Official` 계열 유지 | Official | 실제 의미 확정 필요 (큐레이션 vs 인증) |
| 웰컴 보너스 | welcome bonus 계열 유지 | Welcome Bonus | 마케팅 과장보다 기능 이해 우선 |
| AI 챗봇 | `AI Chatbot` 고정 | AI Chatbot | assistant/character/bot 혼용 금지 |

## 신규 문자열 추가 워크플로우

1. 한국어 기준 원문 작성
2. `app_ko.arb`에 키 + metadata 추가
3. placeholder/줄바꿈/formatting 확정
4. 용어집 충돌 확인
5. 8개 대상 locale 번역 추가
6. `flutter gen-l10n` 실행
7. 검증 (키 수, placeholder, 줄바꿈, 길이, zh_Hans/zh_Hant 차이, pt_BR 자연스러움)

## 운영 원칙

- 한국어가 source of truth
- 영어를 중간 언어로 사용하지 않음
- 제품 용어는 임의 번역 금지
- 모호한 문맥은 추측하지 않고 source 개선 후보로 등록
- locale 추가/수정 후 생성 코드와 QA를 함께 갱신
