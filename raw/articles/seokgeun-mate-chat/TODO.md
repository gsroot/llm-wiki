# Mate Chat - 운영 로드맵

> v1.0.0 Google Play Store 출시 후 지속 개선 계획.
>
> **현재 버전**: v1.0.0 (Android)
> **다음 마일스톤**: v1.1 — iOS App Store 출시

**최종 업데이트**: 2026-04-02

---

## 참고 자료

- 수익 예측 리포트: [`docs/29-revenue-projection.md`](./docs/29-revenue-projection.md)
  - ⚠️ **§1 Executive Summary의 v1 숫자 ($200K Base)는 폐기됨** — codex challenge에서 산식 오류 발견. 외부 인용·예산 책정에 사용 금지.
  - ✅ **현행 권고**: §15.4 v4 PMF KPI (paying users 1K + D30 8% + K-factor 0.3). 출시 액션 timeline은 §10 (D-7 / D-3 / D+30 / D+60 / D+90) 참조.

---

## v1.1 — iOS App Store 출시

### Apple OAuth 구현
- **백엔드**: `app/services/oauth_service.py` — Apple 공개 키 검증, JWKS 캐싱
- **프론트엔드**: `sign_in_with_apple` 패키지, iOS Capabilities 설정
- **참고**: Google OAuth 패턴 재사용 가능

### iOS 프로젝트 설정
- iOS 디렉토리 생성 (`flutter create -i swift --platforms ios .`)
- Bundle Identifier, Signing, Capabilities (Push, Sign in with Apple, IAP)
- Info.plist 권한 설정, Podfile 업데이트
- iOS 앱 아이콘 및 스플래시 스크린

---

## v1.2 — 안정성 & 성능 개선

### WebSocket DB 풀 최적화
- **파일**: `app/api/v1/endpoints/websocket.py:84-86`
- **문제**: WebSocket이 연결 수명 동안 DB 풀 슬롯 점유 (pool_size=10 제한)
- **해결**: 연결별 세션 → 작업별 세션 (`AsyncSessionLocal()` 컨텍스트 매니저)

### Redis Pub/Sub 분산 배포
- 코드 구현 완료, 다중 서버 배포 시나리오 테스트 필요
- Sticky Session, 서버 간 메시지 전달 검증, 부하 테스트

### 콘텐츠 모더레이션 강화
- 키워드 필터링 (욕설/스팸)
- 신고 누적 시 자동 계정 제한
- OpenAI Moderation API 연동 검토

### Flutter 테스트 커버리지 개선
- 현재 ~30% → 목표 70%
- Widget/Integration/Unit 테스트 추가

---

## v1.3+ — 기능 확장

### Settings 페이지 완성
- 알림 설정 (타입별 on/off, 소리, 진동)
- 프라이버시 설정 (프로필 공개 범위)
- 도움말/FAQ 페이지

### 채팅 기능 확장
- 리액션/답장 기능
- WebSocket 압축 (permessage-deflate)
- 사진 공유/저장 (share_plus)

### 향후 고려
- 비밀번호 정책 강화 (복잡도, 재사용 방지)
- 프로필 배지 시스템
- 음성/영상 통화 (WebRTC)

---

## 완료된 주요 작업 (v1.0.0)

- 83개 API 엔드포인트
- Google OAuth + 이메일 인증 + COPPA
- 실시간 채팅 (WebSocket) + 하이브리드 AI
- IAP 검증 (Google Play + App Store)
- FCM 푸시 알림 (11개 언어)
- 9개 언어 국제화 (한국어 잔존 0개)
- 2차 보안 감사 완료 (CRITICAL+HIGH 전체 수정)
- 377+ 백엔드 테스트
- Android 릴리스 빌드 설정 (signing, ProGuard, minification)
- Play Store 에셋 (스크린샷, 아이콘, feature graphic)
- Privacy Policy + COPPA 13세 확인

---

**참고 문서**: [CLAUDE.md](./CLAUDE.md), [docs/19-implementation-status.md](./docs/19-implementation-status.md)
