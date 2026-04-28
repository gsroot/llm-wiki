---
title: "새로운 기술 스택"
type: source
source_path: docs/11-tech-stack-new.md
date_ingested: 2026-04-07
tags: [tech-stack, fastapi, postgresql, redis, flutter, minio]
related:
  - "../sources/10-remaster-overview.md"
  - "../sources/12-system-architecture.md"
  - "../entities/fastapi-app.md"
  - "../entities/postgresql.md"
  - "../entities/redis.md"
  - "../entities/minio.md"
---

# 새로운 기술 스택

## 핵심 요약

리마스터 후 Mate Chat의 기술 스택 전체 구성을 정의한 문서이다. 백엔드(FastAPI + PostgreSQL + Redis), 프론트엔드(Flutter + Riverpod), 인프라(Docker/Kubernetes), 모니터링(Sentry + structlog) 등 모든 계층의 기술 선택과 근거를 포함한다.

## 백엔드 핵심 스택

- **FastAPI**: Python 기반, 비동기, 자동 API 문서화, Pydantic 통합, WebSocket 네이티브 지원
- **SQLAlchemy 2.0**: 비동기 ORM, asyncpg 드라이버, Alembic 마이그레이션
- **Pydantic v2**: Rust 기반 고성능 검증, pydantic-settings로 설정 관리
- **패키지 관리**: uv (Rust 기반, pip 대비 10-100배 빠름)

## 데이터 계층

- **PostgreSQL 17**: JSONB, Array, Full-text Search, UUID 기본 키 활용
- **Redis 7+**: 세션, 캐시, Rate Limiting, WebSocket 세션 관리, Pub/Sub

## 인증

- JWT (Access 15분 + Refresh 7일, Redis 저장) -- 실제 운영에서는 Access 7일 + Refresh 6개월로 조정됨
- OAuth 2.0: Google, Apple (선택적 Facebook)
- 패키지: python-jose, passlib[bcrypt], httpx

## 프론트엔드 (Flutter)

- 상태 관리: Riverpod 2.5.0 + riverpod_generator
- HTTP: Dio 5.4.0 (인터셉터 기반 JWT 자동 갱신)
- WebSocket: web_socket_channel 2.4.0
- 로컬 저장소: flutter_secure_storage, shared_preferences, Hive
- 인증: google_sign_in, sign_in_with_apple

## 파일 저장소

- MinIO (S3 호환), boto3 클라이언트
- 구조: `/profile-images/`, `/chatroom-images/`, `/chat-attachments/`

## 배포 옵션

1. VPS 단일 서버 (Nginx + Let's Encrypt)
2. 클라우드 매니지드 (AWS/GCP/Azure)
3. Kubernetes (자동 스케일링)

## 코드 품질 도구

- 백엔드: ruff (Linter + Formatter), mypy (타입 체크), pre-commit
- 프론트엔드: flutter_lints
- 테스트: pytest + pytest-asyncio, mockito
