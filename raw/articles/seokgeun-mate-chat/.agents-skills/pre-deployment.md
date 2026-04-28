---
name: pre-deployment
description: >
  Mate Chat을 프로덕션에 배포하거나 릴리스할 때 포괄적인 배포 전 체크리스트를 실행합니다.
  트리거 키워드: "배포", "deploy", "production", "릴리스", "release", "프로덕션".
  테스트, 마이그레이션, 환경 변수, 문서, 빌드를 검증합니다.
allowed-tools:
  - Bash
  - Read
  - Grep
---

# 배포 전 체크리스트

프로덕션 릴리스 전 Mate Chat의 자동화된 배포 전 검증.

## 개요

**Mate Chat 상태**: 85% 완료
- **백엔드**: 83개 API 엔드포인트, 113개 테스트
- **프론트엔드**: 132개 Dart 파일, Flutter 앱
- **인프라**: Docker, PostgreSQL, Redis, MinIO

**이 스킬은 안전한 프로덕션 배포를 보장합니다**:
- 코드 품질 (테스트, 타입, 린트)
- 데이터베이스 (마이그레이션 적용)
- 설정 (환경 변수)
- 빌드 (Docker 이미지)
- 문서 (최신 상태)

---

## 관련 시스템

**Slash Command:** `/deploy` (사용자 명시적 호출)
- 사용자가 `/deploy` 입력하여 배포 프로세스 시작
- 프로덕션 배포 및 CI/CD 설정 작업을 명시적으로 시작

**Sub-Agent:** `devops-release-engineer` (자동 호출)
- 복잡한 배포 설정 및 인프라 작업 시 자동으로 호출되는 전문가
- Docker, CI/CD, 클라우드 배포 전문가
- 트리거 조건: 프로덕션 배포, 인프라 설정, Docker 컨테이너 설정

**Agent Skill:** `pre-deployment` (이 스킬 - 자동 트리거)
- 트리거: 프로덕션 배포 명령 실행 전 자동 실행
- 역할: 테스트, 마이그레이션, 환경 변수, 빌드, 문서 자동 검증

**차이점:**
- **Slash Command (`/deploy`)**: 사용자가 명시적으로 입력하여 배포 시작
- **Sub-Agent (`devops-release-engineer`)**: 복잡한 인프라 작업 시 자동 호출
- **Agent Skill (`pre-deployment`)**: 배포 전 자동으로 체크리스트 실행

---

## 빠른 사전 점검

Mate Chat을 프로덕션에 배포하기 전:

- [ ] ✅ 모든 테스트 통과 (113개 테스트)
- [ ] ✅ 타입 체크 통과 (mypy)
- [ ] ✅ 린트 통과 (ruff)
- [ ] ✅ 마이그레이션 적용됨
- [ ] ✅ 환경 변수 유효함
- [ ] ✅ Docker 빌드 성공
- [ ] ✅ 문서 업데이트됨
- [ ] ✅ 버전 번호 증가됨
- [ ] ✅ AGENTS.md 완료율 업데이트됨

---

## 자동화된 검증 스크립트

이 스킬에는 검증을 자동화하는 bash 스크립트가 포함되어 있습니다:

**배포 전 실행:**
```bash
cd mate_chat_backend
bash ../.Codex/skills/pre-deployment/scripts/pre-deploy-check.sh
```

**검증 항목:**
1. Python 환경 (uv 설치됨)
2. 모든 테스트 통과 (pytest)
3. 타입 체킹 (mypy)
4. 코드 린팅 (ruff)
5. 마이그레이션 상태 (alembic)
6. 환경 변수 존재 여부
7. Docker 빌드 테스트
8. Git 상태 (커밋되지 않은 변경사항 없음)

구현은 [scripts/pre-deploy-check.sh](./scripts/pre-deploy-check.sh)를 참조하세요.

---

## 배포 체크리스트

전체 상세 체크리스트는 [deployment-checklist.md](./references/deployment-checklist.md)를 참조하세요.

### 6단계 프로세스

1. **코드 품질** ✅
   - 모든 테스트 실행 (pytest)
   - 타입 체크 (mypy)
   - 린팅 (ruff)

2. **데이터베이스** ✅
   - 마이그레이션 상태 확인
   - 데이터베이스 백업

3. **설정** ✅
   - 환경 변수 검증
   - 시크릿 보안 확인

4. **빌드 & 인프라** ✅
   - Docker 빌드 테스트
   - Docker Compose 검증

5. **문서** ✅
   - AGENTS.md 업데이트
   - docs/ 디렉토리 확인
   - API 문서 확인

6. **버전 관리** ✅
   - Git 상태 확인
   - 버전 증가
   - 변경 로그 업데이트

각 단계의 상세 가이드는 [deployment-checklist.md](./references/deployment-checklist.md)를 참조하세요.

---

## Docker 빌드 & 배포

Docker 관련 상세 절차는 [docker-checklist.md](./references/docker-checklist.md)를 참조하세요.

### 빠른 테스트

```bash
# Docker 이미지 빌드
cd mate_chat_backend
docker build -t matechat-backend:test .

# 전체 스택 테스트
docker-compose up -d
curl http://localhost:8000/health
docker-compose down
```

---

## 환경 변수 검증

필수 환경 변수 목록 및 검증 방법은 [env-validation.md](./references/env-validation.md)를 참조하세요.

### 필수 변수 (요약)

**백엔드**:
- `DATABASE_URL`, `REDIS_URL`
- `JWT_SECRET_KEY`
- `OPENAI_API_KEY`
- `GOOGLE_CLIENT_ID`
- `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD`
- `MINIO_ENDPOINT`, `MINIO_ACCESS_KEY`, `MINIO_SECRET_KEY`
- `SENTRY_DSN`

전체 목록 및 검증 스크립트는 [env-validation.md](./references/env-validation.md)를 참조하세요.

---

## 롤백 계획

배포 실패 시 롤백 절차는 [deployment-checklist.md](./references/deployment-checklist.md#롤백-절차)를 참조하세요.

### 빠른 롤백

```bash
# 데이터베이스 롤백
alembic downgrade -1

# Docker 롤백
docker-compose down
docker-compose up -d  # 이전 버전

# 확인
curl https://api.matechat.com/health
```

---

## 주요 주의사항

1. **자동화 스크립트 필수 실행** - pre-deploy-check.sh를 항상 실행
2. **데이터베이스 백업 필수** - 마이그레이션 전에 반드시 백업
3. **환경 변수 검증** - 누락된 변수로 인한 실패 방지
4. **단계별 진행** - 한 번에 하나씩, 각 단계 확인
5. **롤백 계획 준비** - 실패 시 즉시 복구 가능하도록

---

## 배포 후 모니터링

**처음 1시간** - 중요 모니터링:

```bash
# 로그 확인
docker-compose logs -f backend

# 에러율 체크 (Sentry 대시보드)

# 응답 시간 모니터링
```

**처음 24시간** - 메트릭 추적:
- 에러율 (< 1% 유지)
- 응답 시간 (p95 < 500ms)
- WebSocket 연결 (안정적)
- 데이터베이스 쿼리 성능
- 메모리/CPU 사용량

---

## 참조 파일

### 상세 가이드
- **[deployment-checklist.md](./references/deployment-checklist.md)** - 6단계 전체 상세 체크리스트, 롤백 절차, 트러블슈팅
- **[docker-checklist.md](./references/docker-checklist.md)** - Docker 빌드, 테스트, 배포 절차
- **[env-validation.md](./references/env-validation.md)** - 필수 환경 변수 목록 및 검증 방법

### 자동화 스크립트
- **[scripts/pre-deploy-check.sh](./scripts/pre-deploy-check.sh)** - 배포 전 자동 검증 스크립트

---

**기억하세요**: 철저한 배포 전 체크는 프로덕션 문제를 예방합니다!

"작은" 변경이라도 절대 체크리스트를 건너뛰지 마세요.
