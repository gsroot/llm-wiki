---
title: "Deployment Pipeline"
type: concept
source_count: 1
tags: [deployment, ci-cd, docker, automation, devops]
related:
  - ../entities/docker-deployment.md
  - ../entities/ci-cd-pipeline.md
  - ./release-process.md
  - ../sources/28-deployment-guide.md
---

## Definition

Deployment Pipeline은 코드 변경이 프로덕션 환경에 도달하기까지 거치는 자동화된 단계의 연속이다. 빌드, 테스트, 마이그레이션, 배포, 헬스 체크, 롤백을 포함하며, 각 단계의 실패가 이후 단계를 차단하는 안전 장치 역할을 한다.

## How It Works in Mate Chat

Mate Chat의 배포 파이프라인은 Git 브랜치 push를 트리거로 GitHub Actions에서 실행된다.

### 백엔드 배포 흐름

```
git push origin main (또는 staging)
    |
    v
GitHub Actions (Self-hosted runner)
    |
    ├── 1. 코드 체크아웃
    ├── 2. 현재 이미지 → :rollback 태그 저장
    ├── 3. docker compose build (prod 프로필)
    ├── 4. alembic upgrade head (DB 마이그레이션)
    ├── 5. docker compose up -d (배포)
    ├── 6. /health 폴링 (10회 x 3초)
    └── 7-a. 성공 → 완료
        7-b. 실패 → :rollback 이미지 복원 → docker compose up -d --no-build
```

### Flutter 릴리스 흐름

```
git tag vX.Y.Z+N && git push origin vX.Y.Z+N
    |
    v
GitHub Actions (GitHub-hosted runner)
    |
    ├── 1. 태그 버전 파싱 및 형식 검증
    ├── 2. Java 17 + Flutter 설정
    ├── 3. Secrets에서 key.properties, keystore 생성
    ├── 4. AAB 빌드 (난독화 + split-debug-info)
    ├── 5. AAB 아티팩트 업로드 (90일 보관)
    └── 6. GitHub Release 생성 (AAB 첨부)
        |
        v
    수동: Google Play Console에 AAB 업로드
```

### 환경 분리
- **프로덕션**: `main` push, 프로덕션 시크릿 사용
- **스테이징**: `staging` push, 스테이징 전용 시크릿 (JWT, DB, Redis 등 별도)
- **개발**: 로컬 Docker Compose (common-compose)

## Trade-offs

| 결정 | 장점 | 단점 |
|------|------|------|
| Self-hosted runner 사용 | 비용 절감, 서버 직접 접근 | 러너 관리 부담, 단일 장애점 |
| 롤백 이미지 사전 저장 | 빠른 복구, 자동화 | 디스크 사용 증가 |
| 헬스 체크 후 자동 롤백 | 배포 안전성 향상 | 일부 마이그레이션은 롤백 불가 |
| Flutter AAB 수동 업로드 | Google Play 정책 유연 대응 | 수동 작업 필요 |
| 프로덕션/스테이징 인프라 공유 | 비용 절감 | 리소스 경쟁 가능성 |

## Related

- [Docker Deployment](../entities/docker-deployment.md)
- [CI/CD Pipeline](../entities/ci-cd-pipeline.md)
- [Release Process](./release-process.md)
