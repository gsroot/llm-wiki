---
title: "Read Receipts"
type: concept
source_count: 1
tags: [read, receipts, realtime, websocket, chat]
related:
  - ../concepts/real-time-messaging.md
  - ../entities/websocket-manager.md
  - ../sources/16-realtime-websocket.md
---

# Read Receipts

## Definition

채팅 메시지가 상대방에 의해 읽혔는지 추적하고 표시하는 기능. 타이핑 인디케이터와 달리 읽음 상태는 DB에 영구 저장되며, WebSocket으로 실시간 동기화된다.

## How It Works in Mate Chat

### 흐름

1. **사용자 B**가 채팅방에서 메시지를 읽음:
   ```json
   { "type": "chat.read", "data": { "room_id": "uuid", "message_id": "uuid" } }
   ```
2. **서버**: `handle_read()`에서 처리
   - DB 업데이트: `update_last_read(user_id, room_id, message_id)` - `chat_room_members.last_read_at` 갱신
   - 채팅방 멤버에게 브로드캐스트 (발신자 제외)
3. **다른 멤버들의 클라이언트**: 해당 메시지의 읽음 상태 UI 업데이트

### 브로드캐스트 메시지

```json
{
  "type": "chat.read",
  "data": {
    "room_id": "uuid",
    "user_id": "읽은 사용자 ID",
    "message_id": "읽은 메시지 ID"
  }
}
```

### 관련 DB 구조

- `chat_room_members.last_read_at`: 사용자가 마지막으로 읽은 시점
- `chat_messages.read_count`: 메시지별 읽음 수

### 특징

- **DB 저장**: 타이핑과 달리 영구 저장 (앱 재시작 후에도 상태 유지)
- **발신자 제외**: `exclude=user_id`로 자신에게 브로드캐스트하지 않음
- **last_read_at 기반**: 특정 메시지 ID가 아닌 시점 기반으로 이전 메시지 모두 읽음 처리

## Trade-offs

| 장점 | 단점 |
|------|------|
| 메시지 전달 확인으로 사용자 신뢰감 향상 | DB 쓰기 부하 (읽을 때마다 업데이트) |
| 읽지 않은 메시지 수 계산 가능 | 프라이버시 우려 (상대방이 읽었는지 노출) |
| 영구 저장으로 오프라인 후에도 상태 유지 | 대규모 채팅방에서 브로드캐스트 트래픽 증가 |
| `last_read_at` 방식으로 개별 메시지 추적 없이 효율적 | 정확한 메시지별 읽음 카운트는 별도 로직 필요 |

## Related

- [Real-time Messaging](../concepts/real-time-messaging.md) - 읽음 확인이 속한 실시간 메시징 시스템
- [WebSocket Manager](../entities/websocket-manager.md) - 읽음 상태 브로드캐스트를 처리하는 컴포넌트
