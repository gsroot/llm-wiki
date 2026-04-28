---
title: "Push Notification Flow"
type: concept
source_count: 3
tags: [push-notification, fcm, delivery, real-time, mobile]
related:
  - ../entities/push-notification-system.md
  - ../entities/fcm-integration.md
  - ../sources/20-push-notification-e2e-checklist.md
  - ../sources/21-push-session-operations-guide.md
---

## Definition

Push Notification Flow는 서버에서 알림이 발생한 시점부터 사용자의 기기에 표시되기까지의 전체 흐름을 의미한다. 수신자의 앱 상태(foreground/background/terminated)와 온라인 여부에 따라 배달 경로가 달라지며, 중복 방지와 사용자 경험 최적화를 목표로 한다.

## How It Works in Mate Chat

### 알림 발생 → 배달 결정 흐름

```
이벤트 발생 (follow, mate_request, chat 등)
    |
    v
NotificationService.create_notification()
    ├── notifications 테이블에 레코드 저장
    ├── notification_enabled 확인 → false면 중단
    ├── 카테고리별 설정 확인 (chat_notification_enabled 등)
    └── Redis 공유 presence 확인
         |
         ├── 온라인 (WebSocket 활성) → 시스템 푸시 억제
         │   └── 인앱 WebSocket으로만 전달
         │
         └── 오프라인 → PushService.send_push_notification()
              |
              v
         device_tokens 조회
              |
              v
         Firebase Admin SDK → FCM 서버 → 기기
              |
              ├── Foreground → onMessage
              │   ├── 같은 채팅방 → 억제
              │   ├── 카테고리 OFF → 억제
              │   └── 그 외 → 로컬 알림 표시
              │
              ├── Background → 시스템 알림 표시
              │   └── 탭 → 딥링크 라우팅
              │
              └── Terminated → 시스템 알림 표시
                  └── 탭 → cold-start → auth bootstrap → 딥링크
```

### 온라인 판정 메커니즘
- WebSocket 연결 시 Redis에 presence 키 설정 (TTL 포함)
- WebSocket ping/heartbeat 시 presence TTL 갱신
- WebSocket 종료 시 presence 삭제
- Presence 키 만료 = 오프라인 판정 → 푸시 발송 허용

### Cold-start 딥링크 처리
1. 알림 탭 데이터를 큐에 저장
2. 앱 시작 → auth bootstrap 완료 대기
3. 인증 완료 후 큐에서 딥링크 데이터 꺼내 라우팅
4. `router.go(...)` 사용으로 결정적 라우트 해석

### 세션 복원력
- Transient 네트워크 장애 시 세션 유지 (강제 로그아웃 금지)
- Refresh token이 명시적으로 유효하지 않을 때만 강제 로그아웃
- 오프라인 재시작 시 캐시된 프로필/세션 데이터 우선 사용

## Trade-offs

| 결정 | 장점 | 단점 |
|------|------|------|
| Redis 공유 presence | 분산 환경에서 정확한 온라인 판정 | Redis 의존성 추가, TTL 만료 지연 |
| Foreground 로컬 알림 | 사용자가 다른 화면에서도 알림 인지 | 같은 화면 중복 가능성 (별도 억제 로직 필요) |
| Cold-start 큐잉 | 인증 전 네비게이션 방지 | 앱 시작 시간 미세 증가 |
| notifications 테이블 = source of truth | 푸시 실패해도 히스토리 보존 | DB 쓰기 부하 |

## Related

- [Push Notification System](../entities/push-notification-system.md)
- [FCM Integration](../entities/fcm-integration.md)
- [Push Notification E2E Checklist (source)](../sources/20-push-notification-e2e-checklist.md)
- [Push/Session Operations Guide (source)](../sources/21-push-session-operations-guide.md)
