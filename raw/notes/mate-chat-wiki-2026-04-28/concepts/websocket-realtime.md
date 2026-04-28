---
title: "WebSocket Realtime"
type: concept
source_count: 3
tags: [websocket, realtime, chat, pubsub, distributed]
related:
  - "../entities/fastapi-app.md"
  - "../entities/redis.md"
  - "../entities/flutter-app.md"
  - "../concepts/async-first.md"
  - "../concepts/websocket-connection-management.md"
  - "../concepts/real-time-messaging.md"
  - "../concepts/typing-indicators.md"
  - "../concepts/read-receipts.md"
---

# WebSocket Realtime

## Definition

HTTP 기반 폴링이 아닌 WebSocket 프로토콜을 통해 서버-클라이언트 간 양방향 실시간 통신을 구현하는 패턴이다.

## How It Works in Mate Chat

### 연결

```
ws://[host]:8000/v1/ws/chat/{roomId}?token={jwt}
```

### 메시지 타입

- `message`: 채팅 메시지 (DB 저장 + 브로드캐스트)
- `typing`: 타이핑 인디케이터 (브로드캐스트만)
- `read`: 읽음 표시 (브로드캐스트 + DB 업데이트)
- `ping/pong`: 하트비트

### 서버 측 (FastAPI)

- **WebSocket Manager**: 방별 활성 연결 추적, 사용자-연결 매핑 (다중 기기 지원)
- **Handler**: 메시지 검증 -> DB 저장 -> 같은 방 멤버에게 브로드캐스트
- **AI 트리거**: `@botname` 멘션 감지 시 하이브리드 AI 채팅 응답 생성
- **분산 지원**: Redis Pub/Sub 채널 (`room:{id}`)로 Pod 간 메시지 전달

### 클라이언트 측 (Flutter)

- **자동 재연결**: 지수 백오프 (1s, 2s, 4s, 8s, max 30s)
- **하트비트**: 30초 간격 ping
- **오프라인 큐잉**: 연결 끊김 시 메시지를 큐에 저장, 재연결 후 전송
- **상태 스트리밍**: connecting, connected, reconnecting, disconnected

### Nginx 설정

WebSocket용 별도 location 블록:
- `proxy_http_version 1.1`
- `Upgrade` / `Connection "upgrade"` 헤더

## Trade-offs

**장점**:
- 낮은 지연 시간의 양방향 실시간 통신
- 다양한 이벤트 타입 지원 (채팅, 타이핑, 읽음 등)
- 연결 상태 완전 관리 가능

**단점**:
- Firestore 자동 동기화 대비 오프라인 지원 직접 구현 필요
- 각 WebSocket 연결이 DB 풀 슬롯 장기 점유
- 분산 환경에서 Pub/Sub 인프라 추가 필요

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- WebSocket 서버
- [Redis](../entities/redis.md) -- Pub/Sub 분산 메시징
- [Flutter Application](../entities/flutter-app.md) -- WebSocket 클라이언트
- [Async-First](../concepts/async-first.md) -- 비동기 WebSocket 처리
- [WebSocket Connection Management](../concepts/websocket-connection-management.md) -- 하트비트, 지수 백오프, 재연결 관리
- [Real-time Messaging](../concepts/real-time-messaging.md) -- 메시지 전송 흐름, 상태 동기화
- [Typing Indicators](../concepts/typing-indicators.md) -- 비저장형, 브로드캐스트 전용 타이핑
- [Read Receipts](../concepts/read-receipts.md) -- last_read_at 기반 읽음 표시
