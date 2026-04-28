---
title: "Google Play Store"
type: entity
source_count: 4
tags: [play-store, distribution, android, store-listing]
related:
  - "../entities/in-app-purchase.md"
  - "../entities/i18n-system.md"
  - "../sources/23-google-play-store-listing.md"
  - "../sources/launch-prep.md"
  - "../concepts/app-store-optimization.md"
  - "../synthesis/launch-readiness.md"
---

# Google Play Store

## Overview

Mate Chat의 주요 배포 채널이다. 전체 국가 오픈 배포 전략을 채택하며, 9개 언어 네이티브 지원 + 영어 fallback으로 전 세계 사용자에게 앱을 제공한다. 현재 v1.0.0 AAB 빌드가 완료된 상태이다.

## Architecture/Structure

### 스토어 등록정보

- **앱 이름**: Mate Chat (en) / 메이트챗 (ko)
- **패키지명**: `com.mate.mate_chat_flutter`
- **기본 언어**: English (en-US)
- **카테고리**: Communication 또는 Social
- **가격**: 무료 + IAP (클로버)

### 빌드 정보

- AAB 파일: `app-release.aab` (72.3MB)
- 버전: 1.0.0+1
- Signing: `upload-keystore.jks`, alias `matechat_upload`
- 빌드 옵션: `--obfuscate --split-debug-info`, ProGuard + shrinkResources

### 배포 전략

- Staged Rollout: 5% -> 20% -> 50% -> 100%
- 크래시율/ANR 지표 확인 후 단계 진행
- 심각한 이슈 발견 시 롤백

## Key Details

### Play Console 앱 콘텐츠 설정

- Privacy Policy URL: `https://chat.gmateweb.com/privacy`
- Account Deletion URL: `https://chat.gmateweb.com/withdraw`
- 광고 없음
- 타겟 연령층: 13세 이상 (COPPA)
- 콘텐츠 등급: IARC 기반, 예상 12~16세 이상 (UGC)
- Data Safety: 10개 데이터 유형 수집/공유 매핑 완료

### 스토어 현지화 대상 언어

en, ko, ja, zh-Hans, zh-Hant, es, id, vi, pt-BR (앱 내 지원 언어와 동일)

## Dependencies

- Google Play Developer API: IAP 영수증 검증
- Firebase Analytics: 리텐션 지표 추적
- Play Console Vitals: 크래시율/ANR 모니터링
- Google Play 앱 서명: 업로드 키와 앱 서명 키 분리

## Known Issues

- 스토어 리스팅 다국어화 미완료 (영어/한국어만 준비, 나머지 7개 언어 미착수)
- 스크린샷 다국어 버전 미준비
- HTML 템플릿(비밀번호 재설정, 회원 탈퇴)에 한국어 잔존
- Apple App Store는 미대응 (iOS 빌드 미시작)

## Related

- [인앱 결제](../entities/in-app-purchase.md)
- [i18n 시스템](../entities/i18n-system.md)
- [앱 스토어 최적화](../concepts/app-store-optimization.md)
- [출시 준비 종합](../synthesis/launch-readiness.md)
