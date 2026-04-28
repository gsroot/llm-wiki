---
title: "WebSocket 실시간 통신 설계"
type: source
source_path: docs/16-realtime-websocket.md
date_ingested: 2026-04-07
tags: [websocket, realtime, redis, pubsub, chat]
related:
  - ../entities/websocket-manager.md
  - ../entities/redis-pubsub.md
  - ../concepts/websocket-connection-management.md
  - ../concepts/real-time-messaging.md
  - ../concepts/typing-indicators.md
  - ../concepts/read-receipts.md
---

# WebSocket 실시간 통신 설계 - 소스 요약

## 문서 개요

Mate Chat의 WebSocket 기반 실시간 통신 시스템 전체 설계를 다루는 문서. 연결 관리, 메시지 프로토콜, 채팅/알림 기능, 분산 환경 지원(Redis Pub/Sub), Flutter 클라이언트 구현까지 포괄한다.

## 핵심 내용

### WebSocket 용도
- 실시간 채팅 메시지 송수신
- 타이핑 인디케이터
- 읽음 표시 동기화
- 사용자 온라인/오프라인 상태
- 실시간 알림

### 연결 정보
- 엔드포인트: `wss://api.matechat.com/ws`
- 인증: JWT Token (쿼리 파라미터)
- 하트비트: 30초 간격 ping/pong
- 재연결: 지수 백오프 (1s -> 2s -> 4s -> ... -> max 30s)

### ConnectionManager
- `active_connections`: user_id -> WebSocket 매핑
- `room_members`: room_id -> user_ids 매핑
- 방별 브로드캐스트, 개인 메시지, 사용자 상태 브로드캐스트 지원

### 메시지 프로토콜
- 공통 구조: `{type, data, timestamp}`
- 클라이언트 -> 서버: `chat.send`, `chat.typing`, `chat.read`, `room.join`, `room.leave`, `ping`
- 서버 -> 클라이언트: `chat.message`, `chat.typing`, `chat.read`, `notification`, `user.status`, `pong`, `error`

### 분산 환경 (Redis Pub/Sub)
- 채널 패턴: `room:{room_id}`, `user:{user_id}`
- `DistributedConnectionManager`가 `ConnectionManager` 상속
- 백그라운드 subscriber로 메시지 수신
- 구현 완료, 분산 배포 대기 상태

### Flutter 클라이언트
- `WebSocketService` 클래스: 연결, 메시지 전송, 하트비트, 재연결
- Riverpod Provider로 상태 관리
- `StreamController.broadcast()`로 메시지 스트리밍

### 에러 처리
- 연결 에러 코드: 4001(인증 실패), 4002(세션 만료), 4003(서버 과부하)
- 메시지 에러: Rate Limit 등 (retry_after 포함)

## 관련 파일
- `app/websocket/manager.py`
- `app/websocket/pubsub.py`
- `app/api/v1/endpoints/websocket.py`
- `lib/core/websocket/ws_client.dart` (Flutter)
