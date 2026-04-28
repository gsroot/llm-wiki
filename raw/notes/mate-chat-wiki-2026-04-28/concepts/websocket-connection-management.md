---
title: "WebSocket Connection Management"
type: concept
source_count: 1
tags: [websocket, connection, heartbeat, reconnection]
related:
  - ../entities/websocket-manager.md
  - ../entities/redis-pubsub.md
  - ../concepts/real-time-messaging.md
  - ../sources/16-realtime-websocket.md
---

# WebSocket Connection Management

## Definition

WebSocket 연결의 수립, 유지, 복구, 종료를 관리하는 일련의 메커니즘. HTTP와 달리 WebSocket은 양방향 상시 연결을 유지하므로, 연결 상태 추적, 하트비트, 재연결 전략이 필수적이다.

## How It Works in Mate Chat

### 연결 수립
1. 클라이언트가 `wss://api.matechat.com/ws?token={access_token}`으로 연결 요청
2. 서버에서 JWT 토큰 검증 (실패 시 4001 코드로 연결 거부)
3. `ConnectionManager.connect()`로 연결 등록
4. 온라인 상태 브로드캐스트

### 연결 유지 (Heartbeat)
- **간격**: 30초마다 클라이언트가 `ping` 전송
- **응답**: 서버가 `pong` 응답
- **목적**: NAT/프록시 타임아웃 방지, 연결 상태 확인

### 재연결 (Exponential Backoff)
- 연결 해제 감지 시 자동 재연결 시도
- **백오프 전략**: 1초 -> 2초 -> 4초 -> 8초 -> ... -> 최대 30초
- 재연결 시 최신 Access Token으로 인증
- Flutter에서 `_reconnect()` 메서드로 구현

### 연결 종료
- 정상 종료: 클라이언트가 `sink.close()` 호출
- 비정상 종료: `WebSocketDisconnect` 예외 캐치
- 종료 시 `ConnectionManager.disconnect()`로 연결 제거 + 오프라인 상태 브로드캐스트

### 상태 관리
서버 측 (`ConnectionManager`):
- `active_connections`: 사용자별 활성 WebSocket 연결
- `room_members`: 채팅방별 멤버 목록

클라이언트 측 (Flutter `WsClient`):
- 연결 상태 스트리밍: connecting, connected, reconnecting, disconnected
- 오프라인 메시지 큐잉

### 에러 코드
| 코드 | 의미 | 클라이언트 동작 |
|------|------|----------------|
| 4001 | 인증 실패 | 토큰 갱신 후 재연결 |
| 4002 | 세션 만료 | 재로그인 |
| 4003 | 서버 과부하 | 백오프 후 재연결 |

## Trade-offs

| 장점 | 단점 |
|------|------|
| 실시간 양방향 통신 가능 | 서버 리소스 점유 (연결당 메모리 + DB 풀) |
| 낮은 지연시간 (HTTP 오버헤드 없음) | 연결 관리 복잡성 증가 |
| 지수 백오프로 서버 부하 제어 | 오프라인 시 메시지 유실 가능성 |
| 하트비트로 좀비 연결 방지 | NAT/방화벽 환경에서 연결 불안정 가능 |

## Related

- [WebSocket Manager](../entities/websocket-manager.md) - 서버 측 연결 관리자
- [Redis Pub/Sub](../entities/redis-pubsub.md) - 분산 환경 연결 관리
- [Real-time Messaging](../concepts/real-time-messaging.md) - 연결 위에서 동작하는 메시징
