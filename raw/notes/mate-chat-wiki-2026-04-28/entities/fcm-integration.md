---
title: "FCM Integration"
type: entity
source_count: 3
tags: [fcm, firebase, push-notification, cloud-messaging]
related:
  - ./push-notification-system.md
  - ../concepts/push-notification-flow.md
  - ../sources/21-push-session-operations-guide.md
  - ../sources/28-deployment-guide.md
---

## Overview

Firebase Cloud Messaging (FCM)은 Mate Chat에서 Android 기기에 푸시 알림을 전달하는 핵심 인프라이다. 백엔드에서 Firebase Admin SDK를 사용하여 메시지를 발송하고, Flutter 클라이언트에서 `firebase_messaging` 패키지로 수신한다.

## Architecture/Structure

```
백엔드 (PushService)
    |
    v
Firebase Admin SDK (ADC 또는 서비스 계정 키)
    |
    v
FCM 서버
    |
    v
Android 기기 (firebase_messaging)
    ├── Foreground → onMessage → 로컬 알림
    ├── Background → onBackgroundMessage → 시스템 알림
    └── Terminated → getInitialMessage → cold-start 딥링크
```

## Key Details

### 백엔드 설정
- **ADC 모드 (권장)**: `FIREBASE_CREDENTIALS_PATH`를 비워두고 Application Default Credentials 사용
- **키 파일 모드**: `FIREBASE_CREDENTIALS_PATH`에 서비스 계정 JSON 경로 지정
- `FIREBASE_PROJECT_ID`: Firebase 프로젝트 식별자 (예: `mate-chat-f8889`)

### Flutter 설정
- `google-services.json`이 Firebase 프로젝트와 일치해야 함
- 알림 채널: `mate_chat_default`
- Android `POST_NOTIFICATIONS` 권한 런타임 요청

### 잘못된 토큰 처리
- Firebase 발송 시 `The registration token is not a valid FCM registration token` 에러 수신
- 해당 토큰을 `device_tokens` 테이블에서 자동 삭제
- 로그 기록: `Cleaned up invalid device tokens count=N`

### 환경별 동작
| 환경 | Firebase 초기화 | 비고 |
|------|----------------|------|
| development | 선택 | `FIREBASE_CREDENTIALS_PATH` 미설정 시 푸시 미발송 |
| staging | 필수 | ADC 또는 키 파일 |
| production | 필수 | ADC 권장 |

## Dependencies

- Firebase Admin SDK (`firebase-admin` Python 패키지)
- `firebase_messaging` Flutter 패키지
- `flutter_local_notifications` Flutter 패키지
- Google Cloud 서비스 계정 또는 ADC 인증

## Known Issues

- iOS APNs 연동은 Apple OAuth 구현 및 iOS 빌드와 함께 대기 중
- GCP 환경 외에서는 ADC 사용을 위해 `gcloud auth application-default login` 필요
- 에뮬레이터 환경에서는 Google Play Services 필요

## Related

- [Push Notification System](./push-notification-system.md)
- [Push Notification Flow](../concepts/push-notification-flow.md)
- [배포 가이드 (source)](../sources/28-deployment-guide.md)
