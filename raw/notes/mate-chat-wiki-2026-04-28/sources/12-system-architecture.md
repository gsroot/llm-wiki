---
title: "시스템 아키텍처"
type: source
source_path: docs/12-system-architecture.md
date_ingested: 2026-04-07
tags: [architecture, system-design, websocket, security, deployment]
related:
  - "../sources/10-remaster-overview.md"
  - "../sources/11-tech-stack-new.md"
  - "../entities/fastapi-app.md"
  - "../entities/docker-infrastructure.md"
  - "../entities/redis.md"
  - "../concepts/layered-architecture.md"
---

# 시스템 아키텍처

## 핵심 요약

Mate Chat의 전체 시스템 아키텍처를 4개 계층(Client, Application, Data, External Services)으로 정의한 문서이다. 데이터 흐름, 보안 설계, 확장성 전략, 배포 아키텍처를 포함한다.

## 4개 계층 구조

1. **Client Layer**: Flutter 앱 (iOS/Android/Web) -> Nginx API Gateway
2. **Application Layer**: REST API Server + WebSocket Server (FastAPI) -> Service Layer
3. **Data Layer**: PostgreSQL + Redis + MinIO
4. **External Services**: OpenAI API, Google OAuth, Apple OAuth

## API Gateway (Nginx)

- SSL/TLS 종단, 리버스 프록시, 로드 밸런싱
- REST `/api/` 와 WebSocket `/ws/` 경로 분리
- Rate Limiting, 정적 파일 서빙

## 데이터 흐름

### REST API 요청
Client -> Nginx (SSL, Rate Limit) -> FastAPI Router (JWT 검증) -> Deps (DI) -> Service (비즈니스 로직) -> Repository (CRUD) -> PostgreSQL

### WebSocket 메시지
- WebSocket Manager가 방별 활성 연결과 사용자-연결 매핑 관리
- 메시지 수신 -> Handler (검증, DB 저장, 브로드캐스트) -> 같은 방 사용자에게 전달

### OAuth 인증
Flutter -> OAuth Provider -> FastAPI (토큰 검증, 사용자 조회/생성) -> JWT 발급 -> 클라이언트 API 호출

## Redis 캐시 전략

| 용도 | 키 패턴 | TTL |
|------|---------|-----|
| 세션/토큰 | `session:{user_id}` | 7일 |
| 사용자 캐시 | `user:{user_id}` | 5분 |
| 채팅방 캐시 | `room:{room_id}` | 10분 |
| Rate Limit | `rate:{ip}:{endpoint}` | 1분 |
| WebSocket 세션 | `ws:{user_id}` | 연결 중 |

## 보안 설계

- **네트워크**: TLS 1.3, Rate Limiting, CORS
- **인증/인가**: JWT 서명/만료 확인 -> 사용자 조회 -> 권한 확인 -> 요청 처리
- **데이터**: bcrypt (비밀번호), AES-256 (민감 정보), RSA-256 (JWT), TLS (통신)

## 확장성

- 수평 확장: Load Balancer -> 다수 API Pod -> Redis Cluster + PostgreSQL Primary/Replicas + MinIO Cluster
- WebSocket 분산: Redis Pub/Sub 채널 (`room:{id}`)로 Pod 간 메시지 전달
- Kubernetes HPA: 2-10 replicas 자동 스케일링

## 모니터링

- 로깅: structlog -> Fluentd/Filebeat -> Elasticsearch -> Kibana
- 메트릭: Prometheus + Grafana, Sentry (에러 추적)
- 헬스 체크: `/health`, `/health/ready`, `/health/live`
