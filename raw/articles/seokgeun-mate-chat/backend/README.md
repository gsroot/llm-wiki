# Mate Chat 백엔드

Mate Chat 글로벌 메시징 플랫폼을 위한 FastAPI 기반 백엔드입니다.

## 빠른 시작

```bash
uv venv
source .venv/bin/activate
uv pip install -e ".[dev]"
alembic upgrade head
uvicorn app.main:app --reload
```

## API 엔드포인트

- **문서:** http://localhost:8000/docs
- **인증:** `/v1/auth/` (3개 엔드포인트)
- **사용자:** `/v1/users/` (5개 엔드포인트)
- **소셜:** `/v1/` (7개 엔드포인트)
- **채팅:** `/v1/chat-rooms/` (7개 엔드포인트)
- **WebSocket:** `ws://localhost:8000/v1/ws/chat/{room_id}`
- **AI 챗봇:** `/v1/chatbots/` (5개 엔드포인트)

## 언어 계약

- 사용자-facing API/템플릿의 기본 언어는 영어(`en`)입니다.
- 한국어(`ko`)는 우선 지원 언어로 유지되며, 로컬라이즈된 화면/템플릿에서는 `Accept-Language` 선호를 통해 선택됩니다.
- 지원하지 않는 언어 요청은 영어로 폴백합니다.

## 기술 스택

- Python 3.13 + FastAPI
- PostgreSQL 15 + SQLAlchemy 2.0
- Redis 7
- OpenAI GPT-4

## 테스트

```bash
pytest tests/ -v              # 30개 테스트
pytest tests/ --cov=app       # 61% 커버리지
```

## 정리 작업

소프트 삭제된 채팅방/메시지를 보존 기간 후 정리:

```bash
cd mate_chat_backend
uv run python -m app.utils.cleanup_soft_deleted_rooms --days 30
```

`--days` 기본값은 30일입니다.

번역 레거시 데이터 백필 및 번역 캐시 프리워밍:

```bash
cd mate_chat_backend
uv run python -m app.utils.backfill_translations --batch-size 100
uv run python -m app.utils.backfill_translations --entity-type chat_message --target-locale en --target-locale ja
uv run python -m app.utils.backfill_translations --help
```

## 모니터링

- **Prometheus:** `/metrics` 엔드포인트 제공
- **번역 운영 요약:** `GET /v1/translations/admin/metrics` (관리자 인증 필요)
- **Sentry:** `SENTRY_DSN`이 설정되고 `ENVIRONMENT`가 `staging` 또는 `production`일 때만 초기화됨

## 문서

[메인 README](../README.md)와 [docs/](../docs/) 폴더를 참조하세요.
