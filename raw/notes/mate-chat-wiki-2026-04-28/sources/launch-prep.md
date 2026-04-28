---
title: "출시 준비 종합 (Launch Prep)"
type: source
source_path: docs/_launch-prep/
date_ingested: 2026-04-07
tags: [launch, strategy, iap, phase, rollout, play-store]
related:
  - "../sources/23-google-play-store-listing.md"
  - "../sources/26-global-launch-readiness.md"
  - "../entities/google-play-store.md"
  - "../entities/in-app-purchase.md"
  - "../synthesis/launch-readiness.md"
---

# 출시 준비 종합 (Launch Prep)

## 핵심 요약

`docs/_launch-prep/` 디렉토리에 포함된 글로벌 출시 전략, IAP 상품 등록 정보, Phase 0~4 실행 로그를 종합한 요약이다. 프로젝트를 개발 모드에서 운영 모드로 전환하고, 보안 검증과 AAB 빌드를 완료하여 Google Play Store v1.0.0 출시를 완료했다.

## 글로벌 출시 전략

- **출시 방식**: 전체 국가 오픈 + 영어 fallback + 9개 언어 네이티브 지원
- **Staged Rollout**: 5% -> 20% -> 50% -> 100% 단계적 배포 권장
- **출시 전 필수 작업**: 백엔드 에러 메시지 영어 전환(CRITICAL), fallback 문자열 영어 전환(CRITICAL), 콘텐츠 모더레이션(HIGH), 스토어 리스팅 다국어화(MEDIUM)
- **푸시 알림 i18n**: 11개 언어 완료 (7개 알림 타입)

### Phase별 언어 확장 로드맵

| Phase | 시기 | 언어 수 | 네이티브 지원 국가 | 추가 언어 |
|-------|------|---------|-------------------|-----------|
| 1 | 출시일 | 9개 | ~70개국 | ko, en, ja, zh, es, pt, pt_BR, id, vi |
| 1.5 | +1~2개월 | 11개 | ~100개국 | +fr, de |
| 2 | +3~4개월 | 14개 | ~120개국 | +ar, th, tr |
| 3 | +6개월 | 17개 | ~128개국 | +hi, it, ru |

### 모니터링 지표

- 크래시율 < 1%, ANR율 < 0.5%
- D1 리텐션 > 30%, D7 리텐션 > 15%
- 스토어 평점 > 4.0

## IAP 상품 등록 정보

5개 클로버 번들 상품, 8개 언어 이름/설명 준비 완료:

| 상품 ID | 총 클로버 | 보너스율 | 티어 |
|---------|----------|---------|------|
| `clover_bundle_70000` | 8,000 | +43% | Diamond |
| `clover_bundle_45000` | 4,800 | +33% | Gold |
| `clover_bundle_25000` | 2,400 | +20% | Silver |
| `clover_bundle_12000` | 1,100 | +10% | Bronze |
| `clover_bundle_5000` | 400 | - | Basic |

## Phase 실행 로그 요약

### Phase 0: 프로젝트 재구조화 (완료)

- docs/ 아카이브 분류, 개발용 스크립트 삭제
- CLAUDE.md를 운영 모드로 업데이트
- TODO.md를 617줄 -> 90줄로 축소, 버전 기반 로드맵 전환

### Phase 2: 보안 체크리스트 + 테스트 (완료)

- 프로덕션 보안 10/10 PASS
- 테스트 447 passed, 1 skipped, 0 failed
- COPPA 테스트 추가, AndroidManifest.xml 검증

### Phase 3: 프로덕션 빌드 (완료)

- AAB 빌드 성공: v1.0.0+1, 72.3MB
- Signing 설정 확인, ProGuard/shrinkResources 적용
- Flutter 3.38.3 / Dart 3.10.1

### Phase 4: Play Store 콘솔 체크리스트

- 스토어 등록정보, 앱 콘텐츠(Privacy Policy, Data Safety), 콘텐츠 등급, 타겟 연령층(13세 이상), 인앱 상품, 서명 키 확인 항목 정리
- 데이터 수집/공유 유형 10개 항목 매핑 완료

## 남은 블로커 (출시 전략 문서 기준)

1. 백엔드 에러 메시지 영어 전환 (CRITICAL)
2. 백엔드 fallback 문자열 영어 전환 (CRITICAL)
3. 콘텐츠 모더레이션 기본 구축 (HIGH)
