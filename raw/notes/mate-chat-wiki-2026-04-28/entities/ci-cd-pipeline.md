---
title: "CI/CD Pipeline"
type: entity
source_count: 2
tags: [ci-cd, github-actions, deployment, testing, automation]
related:
  - ./docker-deployment.md
  - ../concepts/deployment-pipeline.md
  - ../concepts/release-process.md
  - ../sources/28-deployment-guide.md
  - ../sources/22-mobile-release-checklist.md
---

## Overview

Mate Chat은 GitHub Actions 기반의 CI/CD 파이프라인을 운영한다. 백엔드 CI (PR 테스트), 프로덕션 배포, 스테이징 배포, Flutter 릴리스의 4가지 워크플로우로 구성된다.

## Architecture/Structure

```
개발 흐름:
  feature/* → dev → staging (QA) → main (프로덕션)
  hotfix/*  → main (프로덕션) → dev 역머지

워크플로우:
  ┌─ backend-ci.yml        ← PR (mate_chat_backend/ 변경 시)
  ├─ deploy-production.yml ← main push (mate_chat_backend/ 변경 시)
  ├─ deploy-staging.yml    ← staging push (mate_chat_backend/ 변경 시)
  └─ flutter-release.yml   ← vX.Y.Z+N 태그 push
```

## Key Details

### 워크플로우별 상세

#### 1. Backend CI (`backend-ci.yml`)
- **트리거**: `mate_chat_backend/` 변경이 포함된 PR
- **단계**: DB 생성 -> Python 3.13 + uv 설정 -> 의존성 설치 -> Alembic 마이그레이션 -> pytest
- **실행 환경**: Self-hosted runner

#### 2. 프로덕션 배포 (`deploy-production.yml`)
- **트리거**: `main` 브랜치 push + `mate_chat_backend/` 변경
- **단계**: 체크아웃 -> 롤백 이미지 저장 -> Docker 빌드 -> Alembic 마이그레이션 -> 배포 -> 헬스 체크 -> (실패 시 롤백)

#### 3. 스테이징 배포 (`deploy-staging.yml`)
- **트리거**: `staging` 브랜치 push + `mate_chat_backend/` 변경
- 프로덕션과 동일 파이프라인, 별도 시크릿 사용

#### 4. Flutter 릴리스 (`flutter-release.yml`)
- **트리거**: `vX.Y.Z+N` 태그 push
- **단계**: 버전 파싱 -> Java 17 + Flutter 설정 -> keystore/sentry 설정 -> AAB 빌드 (난독화 적용) -> GitHub 아티팩트 업로드 -> GitHub Release 생성

### GitHub Secrets 총계
- 백엔드 프로덕션: 22개
- 백엔드 스테이징 추가: 7개
- Flutter 릴리스: 7개
- 백엔드 CI: 1개

### 브랜치 전략
| 브랜치 | 용도 |
|--------|------|
| `main` | 프로덕션 배포 (자동) |
| `staging` | 스테이징 배포 (자동) |
| `dev` | 일상 개발 |
| `feature/*` | 새 기능 (PR -> dev) |
| `fix/*` | 버그 수정 (PR -> dev) |
| `hotfix/*` | 긴급 프로덕션 수정 (PR -> main) |

## Dependencies

- GitHub Actions
- Self-hosted GitHub Actions runner (`self-hosted`, `production` 라벨)
- Docker & Docker Compose
- Python 3.13 + uv
- Java 17 + Flutter (stable)
- Google Play Console (AAB 수동 업로드)

## Known Issues

- Flutter AAB는 GitHub Release에 첨부되지만, Google Play Console 업로드는 수동
- iOS 빌드 파이프라인 미구현 (Apple Developer 계정 필요)

## Related

- [Docker Deployment](./docker-deployment.md)
- [Deployment Pipeline](../concepts/deployment-pipeline.md)
- [Release Process](../concepts/release-process.md)
