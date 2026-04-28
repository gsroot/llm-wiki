---
title: "Redis Pub/Sub"
type: entity
source_count: 1
tags: [redis, pubsub, distributed, websocket, scaling]
related:
  - ../entities/websocket-manager.md
  - ../concepts/websocket-connection-management.md
  - ../concepts/real-time-messaging.md
  - ../sources/16-realtime-websocket.md
---

# Redis Pub/Sub

## Overview

Mate Chat의 분산 WebSocket 환경을 지원하기 위한 Redis Pub/Sub 시스템. 여러 API Pod에 분산된 WebSocket 연결 간 메시지를 중계하여, 서로 다른 서버에 연결된 사용자들도 실시간으로 통신할 수 있게 한다. 현재 구현은 완료되었으나 분산 배포는 대기 상태이다.

## Architecture

```
User A (Pod 1)     User B (Pod 2)     User C (Pod 1)
     │                   │                   │
     ▼                   ▼                   ▼
┌─────────────┐    ┌─────────────┐
│  API Pod 1  │    │  API Pod 2  │
│ Local Mgr   │    │ Local Mgr   │
│ {A, C}      │    │ {B}         │
└──────┬──────┘    └──────┬──────┘
       │   Publish        │  Subscribe
       ▼                  ▼
┌──────────────────────────────────┐
│         Redis Pub/Sub            │
│  Channel: room:{room_id}        │
│  Channel: user:{user_id}        │
└──────────────────────────────────┘
```

### DistributedConnectionManager
`ConnectionManager`를 상속하여 Redis Pub/Sub 기능을 추가한 클래스.

## Key Details

- **채널 패턴**:
  - `room:{room_id}` - 채팅방 단위 메시지 브로드캐스트
  - `user:{user_id}` - 특정 사용자에게 개인 메시지 전달
- **구독 방식**: `psubscribe("room:*", "user:*")` 패턴 구독
- **메시지 흐름**:
  1. 발신 Pod에서 Redis로 메시지 publish
  2. 모든 Pod가 구독 중인 채널에서 메시지 수신
  3. 각 Pod가 자신의 로컬 연결에서 해당 사용자 탐색 후 전달
- **exclude 처리**: 메시지에 `_exclude` 필드를 추가하여 발신자 제외
- **백그라운드 subscriber**: `start_subscriber()` 메서드가 비동기 루프로 메시지 수신

## Dependencies

- **aioredis**: 비동기 Redis 클라이언트
- **ConnectionManager**: 기본 WebSocket 연결 관리 (상속)
- **Redis 서버**: Pub/Sub 메시지 브로커

## Known Issues

- **분산 배포 미적용**: 구현은 완료되었으나 현재 단일 서버에서 운영 중
- **메시지 유실 가능성**: Redis Pub/Sub는 at-most-once 전달 보장. 구독자가 연결 해제된 동안의 메시지는 유실됨
- **확장성**: 채팅방 수가 많아지면 패턴 구독(`psubscribe`)의 성능 영향 검토 필요

## Related

- [WebSocket Manager](../entities/websocket-manager.md) - 기본 연결 관리자
- [WebSocket Connection Management](../concepts/websocket-connection-management.md) - 연결 관리 개념
- [Real-time Messaging](../concepts/real-time-messaging.md) - 실시간 메시징 개념
