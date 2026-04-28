---
name: websocket-pattern
description: >
  Mate Chat에서 실시간 기능, 채팅 기능, 브로드캐스트 메시징을 추가할 때 WebSocket 구현 패턴을 제공합니다.
  트리거 키워드: "WebSocket", "실시간", "채팅", "메시지", "broadcast", "타이핑", "typing",
  "온라인 상태", "presence". 기존 WebSocket 아키텍처와의 일관성을 보장합니다.
allowed-tools:
  - Read
  - Grep
  - Glob
context:
  fork: false
model: sonnet
user-invocable: true
---

# WebSocket 구현 패턴

Mate Chat의 실시간 기능을 위한 WebSocket 구현 패턴 및 모범 사례를 제공합니다.

## 개요

**Mate Chat WebSocket**: 실시간 채팅, 타이핑 인디케이터, 읽음 표시, 온라인 상태

**기존 구현**:
- ConnectionManager (`app/websocket/manager.py`)
- Redis Pub/Sub (`app/websocket/pubsub.py`)
- 엔드포인트 (`app/api/v1/endpoints/websocket.py`)

**이 스킬은 다음을 보장합니다**:
- 일관된 메시지 타입 사용
- 적절한 에러 처리
- 다중 기기 지원
- 브로드캐스트 패턴 준수
- Redis Pub/Sub 통합

---

## WebSocket 연결 URL

```
ws://[host]:8000/v1/ws/chat/{room_id}?token={jwt}
```

**인증**: JWT 토큰 (쿼리 파라미터)
**프로토콜**: WebSocket (ws:// 또는 wss://)

---

## 메시지 타입

### 기존 메시지 타입

1. **message** - 채팅 메시지 (DB 저장 + 브로드캐스트)
2. **typing** - 타이핑 인디케이터 (브로드캐스트만)
3. **read** - 읽음 표시 (브로드캐스트 + DB 업데이트)
4. **ping/pong** - 하트비트

전체 메시지 타입 상세 및 예시는 [websocket-guide.md](./references/websocket-guide.md#메시지-타입)을 참조하세요.

### 새 메시지 타입 추가 시

**체크리스트**:
- [ ] 메시지 타입 이름 정의 (snake_case)
- [ ] 서버 핸들러 구현 (`manager.py`)
- [ ] 클라이언트 핸들러 구현 (Flutter `ws_client.dart`)
- [ ] 문서 업데이트 (`docs/16-realtime-websocket.md`)

**예시**: [websocket-guide.md](./references/websocket-guide.md#새-메시지-타입-추가)를 참조하세요.

---

## ConnectionManager 사용

### 현재 구현

```python
# app/websocket/manager.py
class ConnectionManager:
    async def connect(self, websocket, room_id, user_id)
    async def disconnect(self, room_id, user_id)
    async def broadcast(self, room_id, message)
    async def send_personal(self, user_id, message)
```

### 주요 패턴

**1. 다중 기기 지원**:
```python
# 사용자-연결 매핑 (1:N)
self.user_connections[user_id].append(connection)
```

**2. 방별 브로드캐스트**:
```python
# 방의 모든 멤버에게 전송
await manager.broadcast(room_id, {"type": "message", ...})
```

**3. 개인 메시지**:
```python
# 특정 사용자의 모든 기기에 전송
await manager.send_personal(user_id, {"type": "notification", ...})
```

상세 사용법은 [websocket-guide.md](./references/websocket-guide.md#ConnectionManager-사용법)을 참조하세요.

---

## 에러 처리

### 클라이언트 측 (Flutter)

**자동 재연결**:
```dart
// lib/core/websocket/ws_client.dart
// 지수 백오프: 1s, 2s, 4s, 8s, ... max 30s
```

**오프라인 메시지 큐**:
```dart
// 연결 끊김 시 메시지 큐에 저장
// 재연결 후 자동 전송
```

### 서버 측

**연결 실패 처리**:
```python
try:
    await websocket.accept()
    # ...
except WebSocketDisconnect:
    await manager.disconnect(room_id, user_id)
except Exception as e:
    logger.error(f"WebSocket error: {e}")
    await websocket.close(code=1011, reason="Internal error")
```

전체 에러 처리 가이드는 [websocket-guide.md](./references/websocket-guide.md#에러-처리)를 참조하세요.

---

## Redis Pub/Sub 통합

### 분산 배포 지원

**현재 상태**: 구현 완료, 분산 배포 대기

```python
# app/websocket/pubsub.py
class RedisPubSub:
    async def publish(self, channel, message)
    async def subscribe(self, channel, handler)
```

**사용 패턴**:
```python
# 메시지 브로드캐스트 (모든 서버로)
await pubsub.publish(f"room:{room_id}", message_data)

# 다른 서버에서 받은 메시지 처리
await pubsub.subscribe(f"room:{room_id}", handle_message)
```

상세 구현은 [websocket-guide.md](./references/websocket-guide.md#Redis-PubSub)를 참조하세요.

---

## 주요 주의사항

1. **메시지 타입 일관성** - 기존 타입 (message, typing, read, ping/pong) 준수
2. **에러 처리 필수** - 연결 끊김, 재연결 로직 포함
3. **다중 기기 지원** - 한 사용자가 여러 기기 사용 가능
4. **브로드캐스트 효율성** - 불필요한 메시지 전송 방지
5. **문서 동기화** - 새 메시지 타입은 반드시 문서화
6. **테스트 필수** - 연결, 재연결, 에러 시나리오 테스트

---

## 테스트

### 로컬 테스트

```bash
# wscat 설치
npm install -g wscat

# 연결 테스트
wscat -c "ws://localhost:8000/v1/ws/chat/1?token=YOUR_JWT"

# 메시지 전송
> {"type": "message", "content": "Hello"}

# 응답 확인
< {"type": "message", "content": "Hello", ...}
```

### Flutter 테스트

```dart
// 연결 상태 확인
wsClient.connectionStateStream.listen((state) {
  print('WebSocket state: $state');
});

// 메시지 수신
wsClient.messagesStream.listen((message) {
  print('Received: $message');
});

// 메시지 전송
wsClient.sendMessage('{"type": "message", ...}');
```

---

## 참조 파일

### 상세 가이드
- **[websocket-guide.md](./references/websocket-guide.md)** - 완전한 WebSocket 구현 가이드
  - 메시지 타입 상세
  - ConnectionManager 사용법
  - 에러 처리 패턴
  - Redis Pub/Sub 통합
  - 테스트 방법
  - 트러블슈팅

### 기존 구현 파일
- `app/websocket/manager.py` - ConnectionManager 클래스
- `app/websocket/pubsub.py` - Redis Pub/Sub 통합
- `app/api/v1/endpoints/websocket.py` - WebSocket 엔드포인트
- `lib/core/websocket/ws_client.dart` - Flutter WebSocket 클라이언트

---

**기억하세요**: 일관된 패턴이 안정적인 실시간 통신을 만듭니다!
