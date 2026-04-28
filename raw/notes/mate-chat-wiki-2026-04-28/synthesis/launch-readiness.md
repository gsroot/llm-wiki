---
title: "글로벌 출시 준비 종합"
type: synthesis
source_count: 7
tags: [launch, readiness, global, strategy, blockers, competitive]
related:
  - "../sources/23-google-play-store-listing.md"
  - "../sources/24-flutter-i18n-preparation.md"
  - "../sources/25-localization-glossary.md"
  - "../sources/26-global-launch-readiness.md"
  - "../sources/27-competitive-analysis.md"
  - "../sources/launch-prep.md"
  - "../entities/google-play-store.md"
  - "../entities/in-app-purchase.md"
  - "../entities/i18n-system.md"
  - "../concepts/internationalization-strategy.md"
  - "../concepts/competitive-landscape.md"
  - "../concepts/app-store-optimization.md"
---

# 글로벌 출시 준비 종합

## 전체 현황 요약

Mate Chat v1.0.0은 Google Play Store에 출시 완료된 상태이다. 기술 인프라(DB, WebSocket, 인코딩)는 글로벌 대응이 완료되었고, 보안 검증(10/10 PASS), 테스트(447 passed), AAB 빌드(72.3MB)가 성공적으로 완료되었다. 출시 전 CRITICAL/HIGH 이슈는 해결되었으며, 일부 개선 과제가 남아 있다.

---

## 완료된 항목

| 영역 | 상태 | 상세 |
|------|------|------|
| 프로덕션 보안 | 완료 | 10/10 PASS (IAP bypass 비활성화, JWT, Argon2, Rate Limiting 등) |
| 테스트 | 완료 | 447 passed, 1 skipped, 0 failed (COPPA 테스트 포함) |
| AAB 빌드 | 완료 | v1.0.0+1, 72.3MB, obfuscate + ProGuard |
| 푸시 알림 i18n | 완료 | 11개 언어, 7개 알림 타입 |
| Flutter i18n 인프라 | 완료 | 9개 locale, 141개 번역 키, gen-l10n 파이프라인 |
| IAP 실제 검증 | 완료 | Google Play Developer API 연동 |
| 프로젝트 재구조화 | 완료 | 개발 -> 운영 모드 전환, TODO.md 축소 |
| Play Console 체크리스트 | 작성 완료 | Data Safety, 콘텐츠 등급, 타겟 연령층 매핑 |

---

## 남은 블로커

### CRITICAL

| 이슈 | 상세 | 예상 소요 |
|------|------|-----------|
| 백엔드 에러 메시지 영어 전환 | ~33건 한국어 하드코딩 에러 메시지 (5개 파일) | 1~2일 |
| 백엔드 fallback 문자열 영어 전환 | `"채팅방"` 등 4건 한국어 fallback | 1일 |

### HIGH

| 이슈 | 상세 | 예상 소요 |
|------|------|-----------|
| 콘텐츠 모더레이션 | 키워드 필터, 스팸 감지, 신고 자동 처리 없음 | 5~7일 |
| UI 번역 미완성 | ~1,031개 하드코딩 한국어 문자열 잔존 | 2~3주 |

### MEDIUM

| 이슈 | 상세 |
|------|------|
| 스토어 리스팅 다국어화 | 영어/한국어만 준비, 나머지 7개 언어 미착수 |
| 법적 문서 | ToS, Privacy Policy URL 존재하나 내용 미확인 |
| 시간대 표시 오류 | 일부 페이지에서 `.toLocal()` 누락 |

---

## 출시 전략

### 배포 방식

- **전체 국가 오픈** + 영어 fallback + 9개 언어 네이티브 지원
- Staged Rollout: 5% -> 20% -> 50% -> 100%
- AI 챗봇으로 cold start 문제 완화 (혼자서도 대화 상대 존재)

### 언어 확장 로드맵

| Phase | 시기 | 언어 수 | 국가 수 | 추가 |
|-------|------|---------|---------|------|
| 1 | 출시일 | 9 | ~70 | ko, en, ja, zh, es, pt_BR, id, vi |
| 1.5 | +1~2개월 | 11 | ~100 | +fr, de |
| 2 | +3~4개월 | 14 | ~120 | +ar(RTL), th, tr |
| 3 | +6개월 | 17 | ~128 | +hi, it, ru |

### 모니터링 기준

- 크래시율 < 1%, ANR율 < 0.5%
- D1 리텐션 > 30%, D7 리텐션 > 15%
- 스토어 평점 > 4.0

---

## 경쟁 포지셔닝

Mate Chat은 **"사람과 AI가 함께 대화하는 유일한 글로벌 채팅 앱"**으로 포지셔닝한다.

### 시장 공백

현재 시장에서 텍스트 기반 글로벌 소셜 + AI 통합을 결합한 앱은 없다. 사람 간 텍스트 채팅(HelloTalk, Tandem)에는 AI가 없고, AI 대화(Character.AI, Replika)에는 사람 간 소셜이 없으며, 글로벌 소셜(Azar, Maum)은 영상/음성 중심이다.

### 가장 유사한 경쟁자: Maum

- 한국 개발사, 6~7백만 DL, 연매출 32억원
- Mate Chat 강점: 하이브리드 AI, 그룹 채팅, 소셜 그래프, 대화 지속성, 9개 언어
- Maum 강점: 실시간 번역, 음성 통화, 피드/모먼트, 매너 평가

### 수익 모델

클로버 시스템(소모성 가상화폐)은 아시아/중동에서 검증된 모델. 5개 번들 상품(400~8,000 클로버), 8개 언어 상품 정보 준비 완료.

---

## 미포함 범위

- **Apple App Store**: iOS 빌드 미시작, Apple OAuth 미구현
- **RTL 언어**: Phase 2에서 아랍어 추가 시 Flutter UI 수정 필요
- **지역별 서버 배포**: 단일 리전, 사용자 증가 시 CDN/멀티 리전 검토
- **현지 결제 수단**: Google Play/App Store IAP로 대부분 국가 커버

---

## 핵심 판단

v1.0.0은 Google Play Store에 출시 완료되었다. 향후 과제로는 iOS App Store 배포(Apple OAuth 구현 필요), 콘텐츠 모더레이션 강화, UI 번역 완성도 개선 등이 남아 있다.
