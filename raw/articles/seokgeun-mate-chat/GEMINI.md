# Mate Chat 프로젝트 컨텍스트

## 프로젝트 개요

**Mate Chat(메이트챗)**은 실시간 채팅과 AI 기반 상호작용 기능을 통합한 글로벌 소셜 메시징 플랫폼입니다. 이 시스템은 사용자가 전 세계 사람들과 연결(번역 지원 포함)될 수 있게 하며, GPT-4 기반의 커스텀 AI 챗봇("AI Mates")을 생성하고 상호작용할 수 있도록 합니다.

**현재 상태:**

- **백엔드:** 활성화됨, 대부분 구현 완료 (FastAPI).
- **프론트엔드:** 계획 단계/비어 있음 (`mate-chat-flutter` 디렉토리는 현재 비어 있음).
- **문서화:** `docs/` 디렉토리에 포괄적인 문서가 제공됨.

## 주요 기술

### 백엔드 (`mate_chat_backend`)

- **언어:** Python 3.11+
- **프레임워크:** FastAPI (비동기)
- **데이터베이스:** PostgreSQL 15 (비동기 SQLAlchemy 2.0 + Alembic)
- **캐싱/실시간:** Redis 7 (세션 관리, WebSocket Pub/Sub)
- **스토리지:** MinIO (S3 호환)
- **AI 통합:** OpenAI API (GPT-4)
- **패키지 관리:** `uv` (권장) / `pip`

### 프론트엔드 (`mate-chat-flutter`)

- **프레임워크:** Flutter (계획됨)
- **상태 관리:** Riverpod (계획됨)
- **네트워킹:** Dio (계획됨)

## 디렉토리 구조

- `mate_chat_backend/`: 메인 백엔드 소스 코드.
  - `app/`: 애플리케이션 코어.
    - `api/`: REST API 엔드포인트 (v1).
    - `core/`: 설정, 보안, 데이터베이스 설정.
    - `models/`: SQLAlchemy ORM 모델.
    - `schemas/`: Pydantic 데이터 모델.
    - `services/`: 비즈니스 로직 계층.
    - `websocket/`: 실시간 통신 처리.
  - `tests/`: Pytest 테스트 스위트.
  - `migrations/`: Alembic 데이터베이스 마이그레이션.
- `mate-chat-flutter/`: 향후 Flutter 모바일 애플리케이션을 위한 플레이스홀더.
- `docs/`: 방대한 프로젝트 문서 (아키텍처, API, 스키마 등).

## 개발 및 사용

### 필수 요구사항

- Docker & Docker Compose
- Python 3.11+
- `uv` (Python 패키지 관리자)

### 백엔드 실행

**Docker 사용 (권장):**

```bash
cd mate_chat_backend
./docker-setup.sh
# 또는
docker-compose up -d
```

**로컬 개발:**

1.  **의존성 설치:**
    ```bash
    cd mate_chat_backend
    uv pip install -r pyproject.toml
    ```
2.  **환경 설정:**
    `.env.example`을 `.env`로 복사하고 키(OpenAI, Google/Apple OAuth 등)를 설정합니다.
3.  **마이그레이션 실행:**
    ```bash
    alembic upgrade head
    ```
4.  **서버 시작:**
    ```bash
    uvicorn app.main:app --reload
    ```

### 테스트 및 품질

- **테스트 실행:** `pytest tests/ -v`
- **Linting:** `ruff check .`
- **포맷팅:** `black .`
- **타입 체크:** `mypy .`

## 아키텍처 하이라이트

- **WebSocket:** 실시간 채팅 및 타이핑 표시기에 사용됨.
- **인증:** OAuth 2.0 (Google, Apple) + JWT (Access/Refresh 토큰).
- **데이터베이스:** 사용자, 소셜 그래프(팔로우/메이트), 채팅(방/메시지), AI 챗봇을 다루는 16개 이상의 테이블.
- **경제 시스템:** AI 상호작용을 위한 "클로버(Clover)" 가상 화폐 시스템.

## 주요 파일

- `mate_chat_backend/app/main.py`: 애플리케이션 진입점.
- `mate_chat_backend/docker-compose.yml`: 인프라 오케스트레이션.
- `docs/13-database-schema.md`: 상세 데이터베이스 스키마 참조.
- `docs/14-api-design.md`: API 엔드포인트 명세.
