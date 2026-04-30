---
title: FastAPI
aliases:
- FastAPI
- 패스트API
- fast-api
type: entity
entity_type: tool
tags:
- fastapi
- python
- openapi
- pydantic
- starlette
- tiangolo
- agent-skills
- SKILL.md
- dependency-injection
- type-hints
related:
- '[[tiangolo]]'
- '[[backend-python-fastapi]]'
- '[[agent-skills]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-kim]]'
- '[[pydantic]]'
- '[[sqlalchemy]]'
- '[[postgresql]]'
- '[[ruff]]'
- '[[uv]]'
- '[[fastapi-fastapi]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 22
inbound_count: 87
created: 2026-04-27
updated: 2026-04-28
cited_by_count: 38
---

# FastAPI

## 개요

**FastAPI**는 Python 3.10+ 표준 타입힌트를 입력으로 받아 OpenAPI · JSON Schema · OAuth2 명세를 자동으로 생성·강제하는 ASGI 웹 프레임워크다. 2018년 12월 [[tiangolo]] (Sebastián Ramírez)가 공개했고, **Starlette**(비동기 코어) + **Pydantic**(데이터 검증)을 의존성으로 두며 둘 다에 직접 기여한 이력이 있다. 2026-04 시점 v0.136.1, MIT, 100% test coverage, 100% type-annotated.

석근 입장에서는 c2spf 애널리틱스 공통 API의 92% 단독 유지보수 영역이자 개인 비서 / 트래블메이트 / Mate Chat 백엔드의 디폴트 스택. v0.136.1부터 **라이브러리 안에 자체 SKILL.md가 번들링**되어 LLM 에이전트가 자동으로 "FastAPI 다움"을 따르도록 가이드하는 첫 OSS 사례가 되었다.

## 주요 특징

### 설계 원칙
- **표준 우선(standards-first)**: OpenAPI, JSON Schema, OAuth2를 사후 레이어가 아닌 설계 기반으로 사용. Swagger UI + ReDoc 자동 제공.
- **타입힌트 = 입력**: 새 DSL 없이 Python 표준 타입으로 라우팅, 검증, 문서, DI를 동시에 표현.
- **에디터 우선 검증**: Tiangolo가 PyCharm/VS Code/Jedi에서 자동완성이 가장 잘 동작하는 시그니처를 사전 테스트. `Annotated[int, Path(ge=1)]` 형태가 그 결실.
- **공동 진화**: Pydantic JSON Schema 호환성, Starlette ASGI 베이스 — Tiangolo의 직접 PR이 의존성 라이브러리들을 발전시켰다.

### 핵심 기술
- **DI 시스템**: 의존성의 의존성 그래프, `yield` 클린업(scope `request`/`function`), 라우터 레벨 공유 dependencies.
- **비동기 우선**: ASGI 위에서 `async def`/`def` 혼합 가능 — `def`는 자동 threadpool 위임.
- **WebSocket / SSE**: Starlette WebSocket + `EventSourceResponse` (sse-starlette).
- **Background tasks / Lifespan events**: in-process 비동기 작업 + 스타트업/셧다운 훅.

### 공개 API 표면 (`fastapi/__init__.py`, v0.136.1)

| 그룹 | 심볼 |
|------|------|
| 앱 | `FastAPI`, `APIRouter` |
| 파라미터 함수 | `Body`, `Cookie`, `Depends`, `File`, `Form`, `Header`, `Path`, `Query`, `Security` |
| 요청/응답 | `Request`, `Response`, `UploadFile` |
| 백그라운드 | `BackgroundTasks` |
| 예외 | `HTTPException`, `WebSocketException` |
| WebSocket | `WebSocket`, `WebSocketDisconnect` |
| 외부 재노출 | `from starlette import status` |

내부 코어 3대 파일: `applications.py` (181KB), `routing.py` (197KB), `param_functions.py` (69KB).

### 번들 SKILL.md (`fastapi/.agents/skills/fastapi/`)

라이브러리 디렉토리 안에 [[anthropics-skills]] 표준에 맞춘 `SKILL.md` (10.4KB) + `references/dependencies.md` + `streaming.md` + `other-tools.md`. **메인스트림 OSS 라이브러리가 LLM 에이전트용 사용 매뉴얼을 직접 출하한 첫 사례**. SKILL.md frontmatter `name: fastapi`, `description: FastAPI best practices and conventions...`.

### 핵심 권장 컨벤션 (SKILL.md 요약)
- `Annotated[T, Path/Query/Depends(...)]` 강제 (디폴트 인자 패턴 금지)
- return type annotation 우선 (response_model보다)
- `ORJSONResponse`/`UJSONResponse` deprecated (Pydantic 2 Rust 직렬화로 대체)
- 라우터 prefix/tags/dependencies는 router 레벨 선언
- 의심되면 `def` (threadpool 자동 — async 안 blocking이 가장 큰 함정)
- `def` 안에서 1 함수 = 1 HTTP operation
- Pydantic `RootModel` 회피 → `Annotated[list[int], Field(min_length=1), Body]`
- Tiangolo 추천 보조 스택: **Asyncer · SQLModel · HTTPX · Typer**, **uv · Ruff · ty**

### 채택 사례
- **Microsoft**: ML 서비스 (Kabir Khan 인용) — Windows/Office 코어 통합
- **Uber**: Ludwig REST 서버
- **Netflix**: Dispatch (위기관리 오케스트레이션)
- **Cisco**: Virtual TAC Engineer (REST API 핵심)
- **Explosion AI / spaCy**: API 표준 채택
- 기업 후원: FastAPI Cloud (Keystone), Render, Railway, Scalar 외 다수

## 관련 개념

- [[backend-python-fastapi]] — 석근의 백엔드 스택 운영 맥락(c2spf 애널리틱스 공통 API)
- [[agent-skills]] — fastapi가 self-hosted SKILL.md를 출하한 첫 라이브러리. 표준의 OSS 침투 증거.
- [[anthropics-skills]] — fastapi가 채택한 표준 정의처
- [[c2spf-analytics|c2spf 게임 데이터 BI]] — fastapi 92% 단독 유지보수 코드베이스
- [[github-spec-kit]] — Codex Skills 모드(외부 통합 사례)와 fastapi(라이브러리 self-hosted 사례)의 짝
- [[mcp]] / [[harness]] — fastapi가 ASGI 위에서 에이전트 백엔드(MCP 서버, 하네스)로 자주 사용됨

## 의사결정 컨텍스트 (raw 인용)

> "OpenAPI · JSON Schema · OAuth2 표준을 1급 시민으로 두고 Python 타입힌트를 입력으로 삼는 웹 프레임워크. v0.136.1 기준 자체 .agents/skills/fastapi/SKILL.md를 번들링하여 메인스트림 OSS가 LLM 에이전트에게 자기 사용법을 가르치는 첫 사례를 남겼다."
> — [[fastapi-fastapi]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 백엔드 5단의 진입축. [[matechat|MateChat 사이드 프로젝트]] backend + [[c2spf-analytics|c2spf 게임 데이터 BI]] 본진 양쪽 채택 ([[seokgeun-kim|석근 (이 위키 owner)]]의 표준 선호 스택). **번들된 SKILL.md** 패턴은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 vendor-neutral [[agent-skills]] 채택 첫 사례 — 라이브러리 자체가 LLM 협업을 1급으로 다루는 거버넌스 신호.

## 출처

- [[fastapi-fastapi]] — fastapi/fastapi GitHub 저장소 수집(README, docs/en/docs/{features,history-design-future,async,python-types,fastapi-cli,_llm-test}, pyproject.toml, fastapi/__init__.py, fastapi/.agents/skills/fastapi/) — 본 엔티티의 정의 기반.

## 메모

- ingest의 결정적 발견은 **`.agents/skills/fastapi/SKILL.md`** — agent-stack-evolution 분석의 "표준-구현 분리(Anthropic축)" 명제를 강화하는 정량적 증거.
- 석근의 c2spf `analytics-common-api`가 SKILL.md 권장과 어디서 일치/충돌하는지 점검하는 후속 작업이 가치 있음 — 특히 `Annotated`, `response_model`, `def` vs `async def` 사용 분포.
- "Tiangolo Default Stack"(fastapi + fastapi-cli + Asyncer + SQLModel + Typer + HTTPX + Pydantic + Starlette + uv + Ruff + ty)을 별도 종합 페이지로 정리할 가치.
- **(2026-04-28)**: 백엔드 코어 6개 신규 수집으로 FastAPI 의존성 라이브러리들이 위키에 박힘 — [[pydantic]] (검증, 디폴트 의존성), [[sqlalchemy]]/[[alembic]] (DB ORM/마이그레이션, SQLModel 통합), [[postgresql]] (1순위 dialect), [[ruff]]/[[uv]] (Astral 도구 스택). 종합 페이지 [[backend-fastapi-stack]]에서 전체 흐름 분석.
