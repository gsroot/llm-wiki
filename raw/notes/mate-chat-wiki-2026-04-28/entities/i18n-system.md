---
title: "i18n System"
type: entity
source_count: 3
tags: [i18n, l10n, flutter, arb, locale, translation]
related:
  - "../sources/24-flutter-i18n-preparation.md"
  - "../sources/25-localization-glossary.md"
  - "../sources/launch-prep.md"
  - "../entities/google-play-store.md"
  - "../concepts/internationalization-strategy.md"
---

# i18n System

## Overview

Mate Chat Flutter 앱의 국제화 시스템이다. 한국어를 source of truth로, Flutter 표준 `gen-l10n` 파이프라인을 사용하여 9개 locale을 지원한다. 백엔드 푸시 알림은 별도 i18n 모듈(`app/i18n/push_notifications.py`)로 11개 언어를 지원한다.

## Architecture/Structure

### Flutter 앱 i18n

```
lib/l10n/
  app_ko.arb          <- 기준 원문 (141개 키)
  app_en.arb
  app_ja.arb
  app_zh_Hans.arb
  app_zh_Hant.arb
  app_es.arb
  app_id.arb
  app_vi.arb
  app_pt_BR.arb
  app_zh.arb           <- gen-l10n fallback stub
  app_pt.arb           <- gen-l10n fallback stub
  app_locale.dart      <- 9개 locale 정책, 정규화, timeago 매핑
  l10n.dart            <- context.l10n 접근 확장
```

- 설정: `l10n.yaml` (`template-arb-file: app_ko.arb`, `output-class: L`)
- 생성: `flutter gen-l10n`
- 접근: `context.l10n.키이름`
- locale 선택: 저장된 앱 언어 tag 기반, `localeResolutionCallback`

### 백엔드 푸시 알림 i18n

- 파일: `app/i18n/push_notifications.py`
- 11개 언어: ko, en, ja, zh, zh_Hans, zh_Hant, es, pt, pt_BR, id, vi
- 7개 알림 타입 지원
- `DeviceToken.locale` 기반 사용자 언어 조회, 영어 fallback

### 번역 키 설계

- 공통: `common.*`
- 기능별: `feature.screen.elementPurpose`
- ICU plural 적용: `commonMemberCount`, `relativeTimeMinutesAgo`, `relativeTimeHoursAgo`
- placeholder 사용 (연결 문자열 지양)

## Key Details

### 제품 용어 고정 규칙

| 용어 | 규칙 |
|------|------|
| 메이트(Mate) | 제품 용어 유지, 일반 명사 번역 금지 |
| 클로버(Clover) | 고정, 동사만 현지화 |
| 공식(Official) | Official 계열 유지 |
| AI 챗봇(AI Chatbot) | 고정, assistant/bot 혼용 금지 |

### 스모크 테스트 우선 화면

구매 확인 다이얼로그, 신고 경고 카드, 웰컴 보너스 토스트, 언어 설정 안내문

## Dependencies

- `flutter_localizations`, `intl` 패키지
- `timeago` 패키지 (locale 등록)
- `lib/core/utils/date_formatter.dart` (locale 기반 포맷)

## Known Issues

- 하드코딩 한국어 문자열 ~1,031개 잔존 (채팅 244, 설정 197, 챗봇 166, 인증 145, 소셜 123, 프로필 110, 결제 46)
- 백엔드 에러 메시지/fallback 문자열 한국어 하드코딩 (영어 전환 필요)
- RTL 언어 미대응
- 긴 번역문에 의한 레이아웃 깨짐 가능성
- `languageSettingsAvailableLabel` 등 키 이름 리팩터링 후보 존재

## Related

- [국제화 전략](../concepts/internationalization-strategy.md)
- [Google Play Store](../entities/google-play-store.md)
