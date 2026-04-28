---
title: "Mobile Release Checklist"
type: source
source_path: docs/22-mobile-release-checklist.md
date_ingested: 2026-04-07
tags: [release, mobile, flutter, android, checklist]
related:
  - ../entities/ci-cd-pipeline.md
  - ../concepts/release-process.md
  - ./21-push-session-operations-guide.md
  - ./20-push-notification-e2e-checklist.md
---

## 요약

Flutter 앱 릴리스를 위한 핸드오프 체크리스트이다. 릴리스 입력값, 백엔드/Flutter 전제조건, 빌드 명령어, 푸시/세션 스모크 체크, 검증 증거, 출시 금지 조건을 정의한다.

## 핵심 내용

### 릴리스 입력값
- 타겟 버전 (`x.y.z+build`), 백엔드 환경, Firebase 프로젝트, Sentry DSN, Google Play 패키지명

### 빌드 명령어
- Android 스모크 테스트: `./scripts/run_android.sh --mode release ...`
- Android App Bundle: `./scripts/build_appbundle.sh --version X.Y.Z+N ...`

### 푸시/세션 스모크 체크 (13개 릴리스 게이트)
- 로그인/로그아웃 토큰 등록/해제
- 전체 알림 ON/OFF 토큰 동기화
- Foreground/Background/Terminated 푸시 동작
- 온라인 중복 방지, 오프라인 복구
- 잘못된 FCM 토큰 자동 정리
- Android POST_NOTIFICATIONS 거부 시 안정성
- 오프라인 재시작 세션 유지

### 출시 금지 조건
- development 환경에서 Sentry 활성화
- 명시적 백엔드 URL 없이 릴리스 빌드
- Firebase 프로젝트 불일치
- 푸시 딥링크가 홈으로 이동하는 경우
- 네트워크 장애 시 강제 로그아웃
