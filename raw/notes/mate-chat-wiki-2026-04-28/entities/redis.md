---
title: "Redis"
type: entity
source_count: 3
tags: [cache, redis, rate-limiting, pubsub, session]
related:
  - "../entities/fastapi-app.md"
  - "../entities/postgresql.md"
  - "../concepts/websocket-realtime.md"
---

# Redis

## Overview

Mate Chat에서 캐싱, 세션 관리, Rate Limiting, WebSocket 분산 메시징(Pub/Sub) 등 다목적으로 사용되는 인메모리 데이터 저장소이다. Redis 7+ 버전을 사용한다.

## Architecture/Structure

### 키 패턴 및 TTL

| 용도 | 키 패턴 | TTL |
|------|---------|-----|
| 세션/토큰 | `session:{user_id}` | 7일 |
| 사용자 캐시 | `user:{user_id}` | 5분 |
| 채팅방 캐시 | `room:{room_id}` | 10분 |
| Rate Limit | `rate:{ip}:{endpoint}` | 1분 |
| WebSocket 세션 | `ws:{user_id}` | 연결 지속 |

### Pub/Sub 채널

- 채널 패턴: `room:{room_id}`
- 분산 환경에서 다수 API Pod 간 WebSocket 메시지 전달용

## Key Details

- **Rate Limiting**: 글로벌 60 req/min, 인증 10 req/min
- **세션 저장**: Refresh Token을 Redis에 저장하여 만료/무효화 관리
- **분산 WebSocket**: Pod 1에서 발행한 메시지를 Pod 2의 구독자에게 전달
- **패키지**: redis >= 5.0.0 (Python 클라이언트)

## Dependencies

- Redis 서버 7+
- Python redis 패키지
- FastAPI 미들웨어 (Rate Limiting)

## Known Issues

- Redis Pub/Sub 분산 배포 미구현 (구현은 완료, 실제 다중 서버 배포 대기)
- 프로덕션 환경에서 Redis Cluster 구성 필요

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- Rate Limiting, 세션 관리
- [PostgreSQL](../entities/postgresql.md) -- 주 저장소 (Redis는 캐시 계층)
- [WebSocket Realtime](../concepts/websocket-realtime.md) -- Pub/Sub 분산 메시징
