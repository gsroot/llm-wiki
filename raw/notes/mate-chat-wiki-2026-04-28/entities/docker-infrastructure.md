---
title: "Docker Infrastructure"
type: entity
source_count: 2
tags: [docker, deployment, kubernetes, nginx, infrastructure]
related:
  - "../entities/fastapi-app.md"
  - "../entities/postgresql.md"
  - "../entities/redis.md"
  - "../entities/minio.md"
---

# Docker Infrastructure

## Overview

Mate Chat의 개발/배포 인프라를 Docker 컨테이너로 구성한다. 로컬 개발 환경은 Docker Compose(4개 서비스), 프로덕션은 Kubernetes 배포를 목표로 한다.

## Architecture/Structure

### 로컬 개발 (Docker Compose)

4개 서비스:
1. **api**: FastAPI 애플리케이션 (포트 8000)
2. **postgres**: PostgreSQL 17 (포트 5432)
3. **redis**: Redis 7 (포트 6379)
4. **minio**: MinIO 객체 스토리지 (포트 9000/9001)

### 프로덕션 (Kubernetes)

- Ingress Controller (nginx-ingress)
- API Deployment: HPA 2-10 replicas 자동 스케일링
- Redis StatefulSet
- PostgreSQL StatefulSet
- Load Balancer -> 다수 API Pod

### API Gateway (Nginx)

- SSL/TLS 종단 (Let's Encrypt)
- REST (`/api/`) 및 WebSocket (`/ws/`) 경로 분리
- 리버스 프록시, 로드 밸런싱

## Key Details

- **로컬 실행**: `./docker-setup.sh` 또는 `docker-compose up -d`
- **배포 옵션 3가지**: VPS 단일 서버, 클라우드 매니지드, Kubernetes
- **CI/CD**: GitHub Actions 워크플로우 (스테이징 + Flutter 릴리스)

## Dependencies

- Docker & Docker Compose
- Kubernetes (프로덕션)
- Nginx (API Gateway)

## Known Issues

- CI/CD 파이프라인 정비 완료 (2026-04-03)
- Kubernetes 프로덕션 배포는 아직 VPS 기반으로 운영 중

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 컨테이너화된 앱
- [PostgreSQL](../entities/postgresql.md), [Redis](../entities/redis.md), [MinIO](../entities/minio.md) -- 인프라 서비스
