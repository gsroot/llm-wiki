---
title: "Docker Deployment"
type: entity
source_count: 1
tags: [docker, deployment, traefik, infrastructure, docker-compose]
related:
  - ./ci-cd-pipeline.md
  - ../concepts/deployment-pipeline.md
  - ../sources/28-deployment-guide.md
---

## Overview

Mate Chat의 백엔드는 Docker Compose 기반으로 배포된다. 인프라는 두 개의 Docker Compose 프로젝트로 분리되어 있으며, Traefik 리버스 프록시를 통해 HTTPS 트래픽을 처리한다.

## Architecture/Structure

```
클라이언트
    |
    v
Traefik 3.6 (Let's Encrypt SSL)  ← common-compose
    |
    v
FastAPI 백엔드 (4 워커)           ← mate-chat 프로젝트
    |
    ├── PostgreSQL 17              ← common-compose
    ├── Redis 7                    ← common-compose
    └── MinIO                      ← common-compose
```

### Docker Compose 프로젝트 분리

| 프로젝트 | 서비스 |
|----------|--------|
| **common-compose** | Traefik, PostgreSQL 17, Redis 7, MinIO, Grafana, Loki, Promtail, Adminer |
| **mate-chat** | FastAPI 백엔드 (prod 프로필) |

두 프로젝트는 `traefik-public` Docker 네트워크를 통해 연결된다.

## Key Details

### 컨테이너 구성
- 베이스 이미지: `python:3.13`
- 패키지 매니저: `uv`
- 앱 서버: FastAPI CLI (4 워커)
- 프로덕션/스테이징 별도 스택 (환경별 시크릿)

### 서브도메인 구성
| 서브도메인 | 서비스 |
|-----------|--------|
| `chat.${DOMAIN}` | Mate Chat 백엔드 API |
| `traefik.${DOMAIN}` | Traefik 대시보드 |
| `adminer.${DOMAIN}` | DB 관리 |
| `minio.${DOMAIN}` | MinIO API |
| `grafana.${DOMAIN}` | 모니터링 대시보드 |

### 헬스 체크 및 롤백
- 배포 전 현재 이미지를 `:rollback` 태그로 저장
- 배포 후 `/health` 엔드포인트 10회 폴링 (3초 간격)
- 실패 시 `:rollback` 이미지로 자동 복원

### 데이터베이스 마이그레이션
- 배포 시 `docker compose run --rm backend uv run alembic upgrade head` 자동 실행
- 마이그레이션 실패 시 배포 중단

## Dependencies

- Docker & Docker Compose
- `traefik-public` Docker 네트워크 (수동 생성 필요)
- common-compose 프로젝트가 먼저 실행되어 있어야 함
- Self-hosted GitHub Actions runner (production/staging 라벨)

## Known Issues

- WebSocket 연결이 DB 풀 슬롯을 연결 수명 동안 점유 (pool_size 튜닝 필요)
- 수평 확장 시 WebSocket Sticky Session 및 Redis Pub/Sub 분산 배포 필요
- MinIO 단일 인스턴스 (프로덕션 확장 시 Cloudflare R2 또는 AWS S3 전환 권장)

## Related

- [CI/CD Pipeline](./ci-cd-pipeline.md)
- [Deployment Pipeline](../concepts/deployment-pipeline.md)
- [배포 가이드 (source)](../sources/28-deployment-guide.md)
