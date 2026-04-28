---
title: "WebSocket Manager"
type: entity
source_count: 1
tags: [websocket, realtime, connection, chat]
related:
  - ../entities/redis-pubsub.md
  - ../concepts/websocket-connection-management.md
  - ../concepts/real-time-messaging.md
  - ../sources/16-realtime-websocket.md
---

# WebSocket Manager

## Overview

Mate Chat의 WebSocket 연결을 관리하는 핵심 컴포넌트. `ConnectionManager` 클래스가 사용자별 WebSocket 연결과 채팅방별 멤버 매핑을 유지하며, 메시지 브로드캐스트와 사용자 상태 관리를 담당한다.

## Architecture

```
클라이언트들
  │
  ▼
WebSocket Endpoint (/ws?token={jwt})
  │
  ├─ JWT 검증
  │
  ▼
ConnectionManager
  ├─ active_connections: Dict[str, Set[WebSocket]]  (user_id -> WebSocket 집합, 다중 기기 지원)
  ├─ room_members: Dict[str, Set[str]]              (room_id -> user_ids)
  │
  ├─ connect()              → 연결 수락 + 온라인 상태 브로드캐스트
  ├─ disconnect()           → 연결 제거 + 오프라인 상태 브로드캐스트
  ├─ send_personal()        → 특정 사용자에게 메시지 전송
  ├─ broadcast_to_room()    → 채팅방 멤버 전체에게 브로드캐스트
  └─ broadcast_user_status() → 사용자 온/오프라인 상태 알림
```

### 메시지 핸들링 구조
- `handle_chat_send()`: 권한 확인 -> DB 저장 -> 브로드캐스트 -> 오프라인 푸시
- `handle_typing()`: 채팅방 멤버에게 타이핑 상태 브로드캐스트 (DB 저장 없음)
- `handle_read()`: DB 업데이트 -> 채팅방 멤버에게 읽음 상태 브로드캐스트

## Key Details

- **연결 URL**: `wss://api.matechat.com/ws?token={access_token}`
- **인증**: JWT 토큰을 쿼리 파라미터로 전달, 서버에서 검증
- **하트비트**: 30초 간격 ping/pong
- **상태 관리**: 연결/해제 시 자동으로 온라인/오프라인 상태 브로드캐스트
- **에러 코드**: 4001(인증 실패), 4002(세션 만료), 4003(서버 과부하)
- **싱글턴**: `manager = ConnectionManager()`로 애플리케이션 전역 인스턴스

### 메시지 프로토콜
공통 포맷: `{ "type": "...", "data": { ... }, "timestamp": "ISO8601" }`

| 방향 | 타입 | 설명 |
|------|------|------|
| C->S | `chat.send` | 메시지 전송 |
| C->S | `chat.typing` | 타이핑 상태 |
| C->S | `chat.read` | 읽음 표시 |
| C->S | `room.join` | 채팅방 참여 |
| C->S | `room.leave` | 채팅방 나가기 |
| C->S | `ping` | 하트비트 |
| S->C | `chat.message` | 새 메시지 |
| S->C | `notification` | 알림 |
| S->C | `user.status` | 온라인 상태 |
| S->C | `error` | 에러 |

## Dependencies

- **FastAPI WebSocket**: WebSocket 엔드포인트
- **python-jose**: WebSocket 연결 시 JWT 검증
- **PostgreSQL**: 메시지 저장, 읽음 상태 업데이트
- **Redis Pub/Sub**: 분산 환경 브로드캐스트 (DistributedConnectionManager)
- **FCM**: 오프라인 사용자 푸시 알림

## Known Issues

- **DB 풀 점유**: WebSocket 연결이 DB 풀 슬롯을 연결 수명 동안 점유하여 pool_size 관리 필요
- **단일 서버 한정**: 기본 ConnectionManager는 단일 프로세스에서만 동작. 분산 배포 시 DistributedConnectionManager(Redis Pub/Sub) 필요
- **다중 기기 지원**: `active_connections`가 `Dict[str, Set[WebSocket]]` 구조로 user_id당 여러 WebSocket 연결을 지원하여 다중 기기 동시 접속 가능

## Related

- [Redis Pub/Sub](../entities/redis-pubsub.md) - 분산 환경 메시지 브로드캐스트
- [WebSocket Connection Management](../concepts/websocket-connection-management.md) - 연결 관리 개념
- [Real-time Messaging](../concepts/real-time-messaging.md) - 실시간 메시징 개념
