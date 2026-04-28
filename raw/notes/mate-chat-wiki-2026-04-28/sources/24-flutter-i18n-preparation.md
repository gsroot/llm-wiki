---
title: "Flutter 국제화 적용 상태"
type: source
source_path: docs/24-flutter-i18n-preparation.md
date_ingested: 2026-04-07
tags: [i18n, l10n, flutter, arb, locale]
related:
  - "../sources/25-localization-glossary.md"
  - "../sources/26-global-launch-readiness.md"
  - "../entities/i18n-system.md"
  - "../concepts/internationalization-strategy.md"
---

# Flutter 국제화 적용 상태

## 핵심 요약

한국어를 기준 원문(source of truth)으로 유지하면서 Flutter 표준 `gen-l10n` 구조로 9개 locale을 지원하는 국제화 체계를 구축한 문서이다. 인프라는 완성되었으나 하드코딩 문자열이 약 1,031개 잔존한다.

## 지원 Locale (9개)

ko, en, ja, zh_Hans, zh_Hant, es, id, vi, pt_BR

### 선정 근거

- ko: 기준 원문, 한국 출발 서비스
- en: 글로벌 기본 커버리지
- ja, zh-Hans, zh-Hant: 동아시아 인접 시장
- es: 대규모 확장성과 상업성
- id, vi: 동남아 모바일 시장
- pt-BR: 브라질 수익성
- RTL 언어(아랍어 등)는 UI 검증 비용으로 1차 제외

## 적용 구조

- 기준 원문: `lib/l10n/app_ko.arb` (141개 번역 키)
- 생성기: `flutter gen-l10n`, output class `L`
- 접근: `context.l10n`
- Fallback stub: `app_zh.arb`, `app_pt.arb` (생성기 호환용, 사용자 노출 아님)
- Locale 정책: `lib/l10n/app_locale.dart`에서 9개만 노출

## 하드코딩 문자열 잔존 현황

| 영역 | 미추출 수 |
|------|----------|
| 채팅 | ~244 |
| 설정 | ~197 |
| 챗봇 | ~166 |
| 인증 | ~145 |
| 소셜 | ~123 |
| 프로필 | ~110 |
| 결제 | ~46 |
| **합계** | **~1,031** |

## 번역 키 설계 원칙

- 공통: `common.*`, 기능/화면: `feature.screen.elementPurpose`
- placeholder 사용 (연결 문자열 지양)
- ICU plural 적용: `commonMemberCount`, `relativeTimeMinutesAgo`, `relativeTimeHoursAgo`

## 주요 리스크

- 하드코딩 문자열이 여전히 약 1,031개 잔존
- 한국어 어순 전제 문구의 placeholder 재배치 필요 가능성
- 긴 번역문에 의한 카드/배지/설정 영역 레이아웃 깨짐 가능성
- RTL 미대응
