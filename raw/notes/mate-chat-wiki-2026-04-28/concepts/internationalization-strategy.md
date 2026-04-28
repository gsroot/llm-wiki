---
title: "Internationalization Strategy"
type: concept
source_count: 4
tags: [i18n, l10n, strategy, locale, global]
related:
  - "../entities/i18n-system.md"
  - "../sources/24-flutter-i18n-preparation.md"
  - "../sources/25-localization-glossary.md"
  - "../sources/launch-prep.md"
  - "../concepts/app-store-optimization.md"
  - "../synthesis/launch-readiness.md"
---

# Internationalization Strategy

## Definition

Mate Chat의 국제화 전략은 **한국어를 source of truth로 유지하면서, Flutter gen-l10n 파이프라인으로 단계적으로 지원 언어를 확장**하는 접근이다. 영어를 중간 언어로 사용하지 않고, 한국어 원문에서 각 언어로 직접 번역한다.

## How It Works in Mate Chat

### 3계층 국제화 구조

1. **Flutter 앱 UI**: ARB 파일 기반 `gen-l10n`, 9개 locale (141개 키 완료, ~1,031개 하드코딩 잔존)
2. **백엔드 푸시 알림**: Python 딕셔너리 기반 템플릿, 11개 언어 완료
3. **스토어 메타데이터**: Play Console에서 별도 관리, 영어/한국어 준비 완료

### 언어 확장 로드맵

- Phase 1 (출시일): 9개 언어 -> ~70개국 네이티브 지원
- Phase 1.5 (+1~2개월): +fr, de -> ~100개국
- Phase 2 (+3~4개월): +ar(RTL), th, tr -> ~120개국
- Phase 3 (+6개월): +hi, it, ru -> ~128개국
- 나머지: 영어 fallback

### 제품 용어 일관성

Mate, Clover, AI Chatbot 등 핵심 제품 용어는 임의 번역 금지. 용어집(`docs/25-localization-glossary.md`)에서 locale별 표기를 고정하고, 신규 문자열 추가 시 용어집 충돌을 사전 확인한다.

### 신규 문자열 워크플로우

ko 원문 작성 -> `app_ko.arb` 추가 -> 8개 locale 번역 -> `flutter gen-l10n` -> 검증 (키 수, placeholder, 길이) -> 스모크 QA

## Trade-offs

| 결정 | 이점 | 비용 |
|------|------|------|
| 한국어 source of truth | 원문 품질 직접 제어, 한국어 UX 최적 | 영어 우선 워크플로우 대비 번역 속도 저하 가능 |
| RTL 1차 제외 | QA 비용 절감, 출시 속도 확보 | 아랍어권 잠재 시장 미접근 (Phase 2에서 해소 예정) |
| 제품 용어 고정 | 브랜드 일관성 | locale별 자연스러움 일부 희생 |
| 영어 fallback 전체 국가 오픈 | 최대 도달 범위 | 비영어/비지원 언어 사용자 경험 저하 |
| gen-l10n 파이프라인 | Flutter 표준, 타입 안전, 컴파일 타임 검증 | ARB 파일 수동 관리, fallback stub 필요 |

## Related

- [i18n 시스템](../entities/i18n-system.md)
- [앱 스토어 최적화](../concepts/app-store-optimization.md)
- [출시 준비 종합](../synthesis/launch-readiness.md)
