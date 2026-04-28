---
title: "Release Process"
type: concept
source_count: 2
tags: [release, mobile, flutter, android, google-play, checklist]
related:
  - ../entities/ci-cd-pipeline.md
  - ../concepts/deployment-pipeline.md
  - ../sources/22-mobile-release-checklist.md
  - ../sources/28-deployment-guide.md
---

## Definition

Release Process는 앱의 새 버전을 사용자에게 전달하기 위한 전체 과정이다. 빌드 준비, 환경 검증, 스모크 테스트, 빌드 생성, 스토어 업로드, 배포 후 검증을 포함한다. Mate Chat에서는 백엔드와 Flutter 앱의 릴리스가 독립적으로 진행된다.

## How It Works in Mate Chat

### 백엔드 릴리스
1. `dev` 브랜치에서 개발 완료
2. `staging` 브랜치에 머지 → 스테이징 자동 배포 → QA 검증
3. `main` 브랜치에 머지 → 프로덕션 자동 배포
4. 배포 후 검증: 헬스 체크, Sentry 릴리스 감지, 로그 확인, SSL 인증서

### Flutter 앱 릴리스
1. **입력값 확정**: 버전, 백엔드 URL, Firebase 프로젝트, Sentry DSN
2. **전제조건 검증**: 백엔드 환경 설정, Firebase 일치, keystore 준비
3. **빌드**: `git tag vX.Y.Z+N` → CI 자동 빌드 또는 로컬 `build_appbundle.sh`
4. **스모크 테스트**: 13개 릴리스 게이트 항목 검증
5. **스토어 업로드**: Google Play Console에 AAB 수동 업로드
6. **검증 증거 기록**: 빌드 경로, 커밋 SHA, 스모크 결과

### 릴리스 게이트 (필수 스모크 항목)
- 토큰 등록/해제 (로그인, 로그아웃, 전체 알림 ON/OFF)
- Foreground 알림 표시 및 억제
- Background/Terminated 푸시 수신 및 딥링크
- 온라인/오프라인 중복 방지
- 잘못된 FCM 토큰 자동 정리
- Android `POST_NOTIFICATIONS` 거부 안정성
- 오프라인 재시작 세션 유지

### 출시 금지 조건
- development 환경에서 Sentry 기본 활성화
- 명시적 백엔드 URL 없이 빌드
- Firebase 프로젝트 불일치
- 푸시 딥링크 오작동 (홈으로 이동)
- 네트워크 장애 시 강제 로그아웃

## Trade-offs

| 결정 | 장점 | 단점 |
|------|------|------|
| 태그 기반 CI 빌드 | 버전 추적 명확, 자동화 | 태그 실수 시 재작업 필요 |
| AAB 수동 업로드 | 스토어 정책 유연 대응 | 추가 수동 작업 |
| 13개 스모크 게이트 | 릴리스 품질 보장 | 검증 시간 소요 |
| 백엔드/앱 독립 릴리스 | 각자 속도로 배포 가능 | 호환성 관리 필요 |

## Related

- [CI/CD Pipeline](../entities/ci-cd-pipeline.md)
- [Deployment Pipeline](./deployment-pipeline.md)
- [Mobile Release Checklist (source)](../sources/22-mobile-release-checklist.md)
- [배포 가이드 (source)](../sources/28-deployment-guide.md)
