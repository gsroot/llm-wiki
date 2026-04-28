---
title: "Typing Indicators"
type: concept
source_count: 1
tags: [typing, realtime, websocket, ux]
related:
  - ../concepts/real-time-messaging.md
  - ../entities/websocket-manager.md
  - ../sources/16-realtime-websocket.md
---

# Typing Indicators

## Definition

채팅 상대방이 현재 메시지를 입력 중인지 실시간으로 표시하는 기능. WebSocket을 통해 타이핑 시작/종료 이벤트를 전달하며, 사용자 경험을 향상시키는 비저장형(ephemeral) 이벤트이다.

## How It Works in Mate Chat

### 흐름

1. **사용자 A**가 텍스트 입력 시작:
   ```json
   { "type": "chat.typing", "data": { "room_id": "uuid", "is_typing": true } }
   ```
2. **서버**: `handle_typing()`에서 발신자를 제외한 채팅방 멤버에게 브로드캐스트
   ```json
   { "type": "chat.typing", "data": { "room_id": "uuid", "user_id": "A의 ID", "is_typing": true } }
   ```
3. **다른 멤버들의 클라이언트**: 타이핑 인디케이터 UI 표시
4. **사용자 A**가 입력 중단/전송 시:
   ```json
   { "type": "chat.typing", "data": { "room_id": "uuid", "is_typing": false } }
   ```

### 특징

- **DB 저장 없음**: 순수 브로드캐스트만 수행 (영구 저장 불필요)
- **발신자 제외**: `exclude=user_id`로 자신에게는 전달하지 않음
- **Flutter 클라이언트**: `sendTyping(roomId, isTyping)` 메서드로 전송
- **Riverpod**: `typingUsersProvider`가 채팅방별 타이핑 사용자 Set 관리

### Flutter 구현

```dart
// 전송
wsService.sendTyping(roomId, true);   // 입력 시작
wsService.sendTyping(roomId, false);  // 입력 종료

// 수신: typingUsersProvider (StateNotifierProvider.family)
```

## Trade-offs

| 장점 | 단점 |
|------|------|
| 대화가 활발하다는 시각적 피드백 제공 | 네트워크 트래픽 증가 (빈번한 이벤트) |
| DB 저장 없어 서버 부하 최소 | 디바운싱 없을 경우 과도한 이벤트 발생 가능 |
| 구현이 단순 (브로드캐스트만) | 지연이 있으면 UX 불일치 발생 |

## Related

- [Real-time Messaging](../concepts/real-time-messaging.md) - 타이핑 인디케이터가 속한 실시간 메시징 시스템
- [WebSocket Manager](../entities/websocket-manager.md) - 브로드캐스트를 처리하는 컴포넌트
