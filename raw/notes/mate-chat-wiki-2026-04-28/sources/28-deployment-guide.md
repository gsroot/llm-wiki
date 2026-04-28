---
title: "배포 가이드"
type: source
source_path: docs/28-deployment-guide.md
date_ingested: 2026-04-07
tags: [deployment, docker, ci-cd, github-actions, traefik, flutter, infrastructure]
related:
  - ../entities/docker-deployment.md
  - ../entities/ci-cd-pipeline.md
  - ../concepts/deployment-pipeline.md
  - ../concepts/release-process.md
---

## 요약

Mate Chat의 전체 배포 파이프라인을 다루는 종합 가이드이다. 백엔드 (프로덕션/스테이징), Flutter 앱 (CI/수동), 인프라 서비스, 브랜치 전략, CI 파이프라인, GitHub Secrets를 모두 포함한다.

## 핵심 내용

### 배포 파이프라인 (3종)
| 파이프라인 | 트리거 | 대상 |
|-----------|--------|------|
| 백엔드 프로덕션 | `main` push | Self-hosted Docker + Traefik |
| 백엔드 스테이징 | `staging` push | Self-hosted Docker + Traefik (별도 스택) |
| Flutter 릴리스 | `vX.Y.Z+N` 태그 push | GitHub Release + Google Play Console |

### 인프라 구성
- 두 개의 Docker Compose 프로젝트: common-compose (Traefik, PostgreSQL, Redis, MinIO, Grafana 등) + mate-chat backend
- Traefik 3.6: 리버스 프록시 + Let's Encrypt 자동 HTTPS
- Self-hosted GitHub Actions runner

### 배포 프로세스
1. 코드 체크아웃
2. 현재 이미지 롤백용 저장
3. Docker 빌드
4. Alembic 마이그레이션
5. 컨테이너 배포
6. 헬스 체크 (최대 10회 x 3초)
7. 실패 시 자동 롤백

### GitHub Secrets
- 백엔드 프로덕션: 22개
- 백엔드 스테이징 추가: 7개
- Flutter 릴리스: 7개
- 백엔드 CI: 1개

### 오브젝트 스토리지 옵션
- MinIO (현재, 무료), AWS S3, Cloudflare R2 (환경변수만 변경으로 전환 가능)

### 모니터링
- PLG 스택: Promtail + Loki + Grafana
