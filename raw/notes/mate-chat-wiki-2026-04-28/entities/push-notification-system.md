---
title: "Push Notification System"
type: entity
source_count: 3
tags: [push-notification, fcm, apns, notification, real-time]
related:
  - ./fcm-integration.md
  - ../concepts/push-notification-flow.md
  - ../sources/20-push-notification-e2e-checklist.md
  - ../sources/21-push-session-operations-guide.md
  - ../sources/22-mobile-release-checklist.md
---

## Overview

Mate Chat의 푸시 알림 시스템은 백엔드 알림 서비스, Firebase Cloud Messaging (FCM), Flutter 클라이언트의 세 계층으로 구성된다. 7가지 알림 타입(follow, mate_request, mate, invite, force_exit, manager_transfer, chat)을 지원하며, 수신자의 앱 상태에 따라 로컬 알림 또는 시스템 푸시를 선택적으로 전달한다.

## Architecture/Structure

```
알림 발생 이벤트 (소셜/채팅 서비스)
    |
    v
NotificationService (app/services/notification_service.py)
    ├── notifications 테이블에 레코드 생성
    ├── Redis 공유 presence 확인 (is_user_online)
    └── 오프라인 사용자 → PushService 호출
         |
         v
PushService (app/services/push_service.py)
    ├── device_tokens 조회
    ├── Firebase Admin SDK로 FCM 발송
    └── 잘못된 토큰 자동 정리
         |
         v
Flutter PushNotificationService (lib/core/push/push_notification_service.dart)
    ├── Foreground: 로컬 알림 표시 (같은 채팅방이면 억제)
    ├── Background: 시스템 알림 → 탭 시 딥링크
    └── Terminated: cold-start → auth bootstrap 후 딥링크
```

## Key Details

### 알림 타입 및 페이로드
| 타입 | 트리거 | 페이로드 키 |
|------|--------|------------|
| `follow` | 팔로우 | `user_id` |
| `mate_request` | 메이트 요청 | `requester_id`, `user_id` |
| `mate` | 메이트 수락 | `mate_id`, `user_id` |
| `invite` | 채팅방 초대 | `room_id`, `invite_id` |
| `force_exit` | 강제 퇴장 | `room_id` |
| `manager_transfer` | 관리자 이전 | `room_id` |
| `chat` | 채팅 메시지 | `room_id`, `sender_id`, `sender_nickname` |

### Delivery Policy
- **Foreground (다른 화면)**: 로컬 알림 표시
- **Foreground (같은 채팅방)**: 억제
- **Foreground (카테고리 OFF)**: 억제
- **Background / Terminated**: 시스템 푸시 발송
- **Online (WebSocket 활성)**: 시스템 푸시 억제 (Redis presence 기반)
- **Offline**: 시스템 푸시 발송

### Token Lifecycle
1. 로그인 시 device token 등록 (`POST /notifications/device-token`)
2. 로그아웃 시 삭제 (`DELETE /notifications/device-token/{token}`)
3. 전체 알림 OFF 시 토큰 해제 + `notification_enabled=false` 동기화
4. 전체 알림 ON 시 토큰 재등록 + `notification_enabled=true` 동기화
5. 잘못된 토큰은 FCM 거부 시 자동 삭제

## Dependencies

- Firebase Admin SDK (백엔드)
- `firebase_messaging` (Flutter)
- `flutter_local_notifications` (Flutter foreground 알림)
- Redis (공유 presence 관리)
- `device_tokens` 테이블
- `notifications` 테이블

## Known Issues

- iOS APNs 배포는 Apple OAuth 및 iOS 앱 빌드와 함께 대기 중
- 인앱 결제 검증과 유사하게 실제 프로덕션 환경에서의 대규모 테스트 미실시

## Related

- [FCM Integration](./fcm-integration.md)
- [Push Notification Flow](../concepts/push-notification-flow.md)
- [Push Notification E2E Checklist (source)](../sources/20-push-notification-e2e-checklist.md)
- [Push/Session Operations Guide (source)](../sources/21-push-session-operations-guide.md)
