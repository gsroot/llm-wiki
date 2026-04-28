# Repository Guidelines

## 프로젝트 구조 및 현황

- `docs/` — 설계/스펙 문서(01~18); 변경 전 `12-system-architecture.md`, `13-database-schema.md`, `14-api-design.md`, `15-auth-system.md`, `16-realtime-websocket.md` 우선 확인.
- `mate_chat_backend/` — FastAPI 백엔드(기능 구현 70% 수준). `app/`(api/models/schemas/services/repositories/websocket), `migrations/`(Alembic), `tests/`(pytest), `.env.example` 포함.
- `mate-chat-flutter/` — Flutter는 아직 스캐폴드되지 않음; 생성 시 이 경로 내부에 모듈/에셋을 배치.
- 신규 다이어그램·에셋은 관련 경로(`docs/` 또는 기능 폴더)와 함께 보관, 루트 난립 금지.

## 개발/빌드/테스트 명령

- 전제: Python 3.11+, `uv` 사용. 백엔드 작업 시 `cd mate_chat_backend`.
- 로컬 셋업: `uv venv && source .venv/bin/activate && uv pip install -e ".[dev]"` (또는 `uv pip install -r pyproject.toml`); `.env.example`을 `.env`로 복사 후 값 설정.
- 마이그레이션: `alembic upgrade head`.
- 서버 실행: `uvicorn app.main:app --reload`.
- 테스트: `uv run pytest -v` 또는 `uv run pytest --cov=app`.
- 새 명령/스크립트는 `README.md`와 스크립트 도움말에 설명 추가.

## 코드 스타일 및 네이밍

- Python: Black/Isort/Ruff/Mypy 설정(pyproject, line length 100). async 우선, 타입 힌트 필수, repository+service 패턴 유지.
- Dart/Flutter: `flutter_lints` 기준(프로젝트 생성 후); 기능별로 `lib/` 하위 폴더 구성, PascalCase 위젯/ lowerCamelCase 멤버.
- 비자명한 결정에는 짧은 주석/도크스트링을 남기고, 함수는 작고 순수하게 유지.

## 테스트 가이드

- 위치·네이밍: `mate_chat_backend/tests/` 내 `test_*.py`; Arrange-Act-Assert, fixture/팩토리 활용.
- 회귀 방지: 버그 수정 시 최소 1개 회귀 테스트 추가. 커버리지를 의미 있게 유지(현재 약 61%).
- Flutter 착수 후에는 `flutter test`를 기본으로, UI 플로우는 위젯 테스트, 로직은 단위 테스트로 분리.

## 커밋 및 PR 가이드

- 커밋: 명령형으로 명확히(`Add user search endpoint`, `Fix websocket auth`), 포매팅-only 변경은 분리.
- PR: 요약, 테스트 결과(`pytest? flutter test?`), UI/API 변경 시 스크린샷 또는 curl 트레이스, 관련 이슈/`docs/` 링크 포함. 범위는 좁게 유지하고 린트·포매터·테스트 통과 후 요청.

## 보안 및 설정

- 비밀값 커밋 금지; `.env` 로컬 사용, 필요한 키는 `mate_chat_backend/.env.example`에 예시 추가.
- 인증/권한 흐름은 `docs/15-auth-system.md`와 대조하고 벗어나면 명시.
- DB 마이그레이션은 전/후방 호환성 고려, 되돌릴 수 없는 변경은 `docs/`나 PR 본문에 기록.
