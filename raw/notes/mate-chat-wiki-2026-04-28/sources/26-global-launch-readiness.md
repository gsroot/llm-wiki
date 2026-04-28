---
title: "글로벌 출시 준비 상태 진단"
type: source
source_path: docs/26-global-launch-readiness.md
date_ingested: 2026-04-07
tags: [launch, readiness, global, blockers, iap, moderation, legal]
related:
  - "../sources/24-flutter-i18n-preparation.md"
  - "../sources/27-competitive-analysis.md"
  - "../sources/launch-prep.md"
  - "../entities/google-play-store.md"
  - "../entities/in-app-purchase.md"
  - "../concepts/internationalization-strategy.md"
  - "../synthesis/launch-readiness.md"
---

# 글로벌 출시 준비 상태 진단

## 핵심 요약

기술 아키텍처(DB, WebSocket, 인코딩)는 글로벌 채팅에 적합하지만, **결제 보안 구멍, 한국어 하드코딩, 콘텐츠 모더레이션 부재, 법적 문서 미비**로 실질적 글로벌 출시는 불가 상태였다(2026-03-19 기준). 이후 Phase 0~3에서 상당수 해결됨.

## 등급별 진단 결과

| 등급 | 항목 수 | 설명 |
|------|---------|------|
| CRITICAL | 3 | IAP mock 검증, 푸시 알림 한국어 하드코딩, 콘텐츠 모더레이션 부재 |
| HIGH | 2 | UI 번역 60% 미완성, 법적 문서 미비 |
| MEDIUM | 1 | 시간대 표시 오류 |
| OK | 5 | 유니코드, DB 스키마, WebSocket, 네트워크 복원력, 사용자 탐색 |

## CRITICAL 이슈 요약

1. **IAP 검증 mock 상태**: `verify_google_purchase()`가 항상 성공 반환 → 무한 클로버 획득 가능
2. **푸시 알림 한국어 하드코딩**: 비한국어 사용자(~88%)가 알림을 읽을 수 없음
3. **콘텐츠 모더레이션 부재**: 스팸/욕설/혐오 필터 없음, 신고 처리 워크플로우 미구현

## HIGH 이슈 요약

1. **UI 번역 미완성**: 141개 키 추출 완료, 700+ 하드코딩 한국어 잔존
2. **법적 문서 미비**: ToS, Privacy Policy, GDPR, COPPA 미충족

## OK 영역 (글로벌 대응 완료)

- UTF-8 유니코드/이모지 완전 지원
- DB 스키마 국제화 (다중 언어, 국가 코드, UTC 타임스탬프)
- WebSocket 지수 백오프 재연결, 오프라인 큐잉
- 국가/언어/성별/나이 필터 사용자 탐색

## 작업 로드맵 (문서 작성 시점)

- Phase 1 (2~3주): IAP 실제 검증, 푸시 알림 다국어화, 기본 모더레이션
- Phase 2 (1~2주): 법적 문서, GDPR, COPPA
- Phase 3 (2~3주): UI 번역 완성
- Phase 4 (1~2일): 시간대 수정, 전체 QA
- 예상 총 소요: 6~10주
