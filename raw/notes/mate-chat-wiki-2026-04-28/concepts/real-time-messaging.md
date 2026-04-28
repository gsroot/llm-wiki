---
title: "Real-time Messaging"
type: concept
source_count: 1
tags: [realtime, messaging, websocket, chat, notification]
related:
  - ../entities/websocket-manager.md
  - ../concepts/websocket-connection-management.md
  - ../concepts/typing-indicators.md
  - ../concepts/read-receipts.md
  - ../sources/16-realtime-websocket.md
---

# Real-time Messaging

## Definition

WebSocket을 통해 서버와 클라이언트 간 지연 없이 메시지를 주고받는 통신 방식. HTTP 폴링과 달리 서버가 능동적으로 클라이언트에게 데이터를 푸시할 수 있어, 채팅, 알림, 상태 동기화 등에 적합하다.

## How It Works in Mate Chat

### 메시지 전송 흐름

1. **클라이언트**: `chat.send` 타입 메시지를 WebSocket으로 전송
   ```json
   { "type": "chat.send", "data": { "room_id": "uuid", "content": "Hello!" } }
   ```
2. **서버**: 권한 확인 (채팅방 멤버인지 검증)
3. **서버**: PostgreSQL에 메시지 저장
4. **서버**: `broadcast_to_room()`으로 채팅방 온라인 멤버에게 브로드캐스트
5. **서버**: 오프라인 멤버에게 FCM 푸시 알림 전송

### 알림 전송

- **온라인 사용자**: WebSocket `notification` 타입으로 즉시 전달
- **오프라인 사용자**: FCM 푸시 알림으로 대체 전달
- 알림은 항상 DB에 저장 후 전송

### 사용자 상태 동기화

- 연결 시: `user.status` = `"online"` 브로드캐스트
- 해제 시: `user.status` = `"offline"` 브로드캐스트
- 관련 사용자들(같은 채팅방 멤버 등)에게 상태 변경 알림

### Flutter 클라이언트 구현

- `WebSocketService`: 연결, 전송, 수신, 재연결 관리
- `StreamController.broadcast()`: 수신된 메시지를 여러 리스너에 분배
- Riverpod Provider:
  - `webSocketServiceProvider`: WebSocket 서비스 인스턴스
  - `chatMessagesProvider`: 채팅방별 메시지 스트림 필터링
  - `typingUsersProvider`: 채팅방별 타이핑 사용자 관리

### 메시지 프로토콜 요약

모든 메시지는 `{ type, data, timestamp }` 구조를 따른다.

| 기능 | 클라이언트 -> 서버 | 서버 -> 클라이언트 |
|------|-------------------|-------------------|
| 채팅 | `chat.send` | `chat.message` |
| 타이핑 | `chat.typing` | `chat.typing` |
| 읽음 | `chat.read` | `chat.read` |
| 하트비트 | `ping` | `pong` |
| 알림 | - | `notification` |
| 상태 | - | `user.status` |
| 에러 | - | `error` |

## Trade-offs

| 장점 | 단점 |
|------|------|
| 즉각적인 메시지 전달 (밀리초 단위) | 서버 리소스 상시 점유 |
| 서버 푸시 가능 (알림, 상태 변경) | 모바일 배터리 소모 |
| 양방향 통신으로 타이핑/읽음 등 실시간 기능 구현 가능 | 네트워크 불안정 시 메시지 유실 가능 |
| FCM 폴백으로 오프라인 사용자 지원 | WebSocket + FCM 이중 관리 복잡성 |
| Riverpod 스트림으로 Flutter UI 반응형 업데이트 | 메시지 순서 보장을 위한 추가 로직 필요 |

## Related

- [WebSocket Manager](../entities/websocket-manager.md) - 메시지 브로드캐스트 담당 컴포넌트
- [WebSocket Connection Management](../concepts/websocket-connection-management.md) - 메시징의 기반이 되는 연결 관리
- [Typing Indicators](../concepts/typing-indicators.md) - 실시간 타이핑 표시
- [Read Receipts](../concepts/read-receipts.md) - 실시간 읽음 확인
