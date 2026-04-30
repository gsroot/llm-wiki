---
title: fastapi/fastapi — 표준 기반 모던 Python 웹 프레임워크 (라이브러리 번들 SKILL.md)
type: source
source_type: article
source_url: https://github.com/fastapi/fastapi
raw_path: raw/articles/fastapi-fastapi/
author: Sebastián Ramírez (tiangolo) — fastapi.tiangolo.com
date_published: 2018-12-05
date_ingested: 2026-04-27
tags:
- fastapi
- tiangolo
- python
- pydantic
- starlette
- openapi
- async
- dependency-injection
- agent-skills
- SKILL.md
related:
- '[[backend-python-fastapi]]'
- '[[seokgeun-kim]]'
- '[[c2spf-analytics]]'
- '[[agent-skills]]'
- '[[anthropics-skills]]'
confidence: high
inbound_count: 29
aliases:
- Fastapi
- fastapi
- fastapi/fastapi — 표준 기반 모던 Python 웹 프레임워크 (라이브러리 번들 SKILL.md)
cited_by:
  - "[[agent-skills]]"
  - "[[anthropics-skills]]"
  - "[[backend-fastapi-stack]]"
  - "[[backend-python-fastapi]]"
  - "[[c2spf-analytics]]"
  - "[[fastapi]]"
  - "[[github-spec-kit]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[openai-openai-cookbook]]"
  - "[[python]]"
  - "[[seokgeun-kim]]"
  - "[[tiangolo]]"
cited_by_count: 12
---

# fastapi/fastapi — 표준 기반 모던 Python 웹 프레임워크 (라이브러리 번들 SKILL.md)

## 한줄 요약

> **OpenAPI · JSON Schema · OAuth2 표준을 1급 시민으로 두고 Python 타입힌트를 입력으로 삼는 웹 프레임워크.** v0.136.1 기준 자체 `.agents/skills/fastapi/SKILL.md`를 번들링하여 메인스트림 OSS가 LLM 에이전트에게 자기 사용법을 가르치는 첫 사례를 남겼다.

## 메타데이터 스냅샷

| 항목 | 값 |
|------|-----|
| 버전 | 0.136.1 (2026-04 기준) |
| 라이선스 | MIT |
| Python 요구 | ≥ 3.10 (3.10 ~ 3.14 지원) |
| 핵심 의존성 | `starlette>=0.46.0`, `pydantic>=2.9.0`, `typing-extensions>=4.8.0` |
| 저자 | Sebastián Ramírez (`tiangolo@gmail.com`) |
| 후원 | FastAPI Cloud (Keystone), Render·Railway·Scalar 외 다수 |
| 기업 채택 사례 | Microsoft, Uber, Netflix, Cisco, Explosion AI(spaCy) |
| 디렉토리 구조 | `fastapi/` (라이브러리 코어 + `.agents/skills/`), `docs/`, `docs_src/`, `tests/` |

## 핵심 내용

### 1. 설계 철학 — "표준 위의 프레임워크" (history-design-future.md)

- 신규 프레임워크 작성을 **수년간 회피**했던 Tiangolo가 결국 만든 이유: 기존 프레임워크 어디에도 OpenAPI · JSON Schema · OAuth2 · Python 3.6+ 타입힌트의 조합이 없었음.
- **"사후 레이어"가 아닌 설계 기반**: 코딩 전 수개월간 OpenAPI/JSON Schema/OAuth2 명세 학습.
- **에디터 우선 검증**: Python Developer Survey 80% 점유 에디터(PyCharm, VS Code, Jedi)에서 자동완성·타입체크가 최대화되는 시그니처를 먼저 설계.
- **Pydantic·Starlette에 직접 기여**하며 부족한 부분 보강 → 현재 둘을 의존성으로 사용.

### 2. 기능 매트릭스 (features.md)

- **표준 기반**: OpenAPI 자동 생성 → Swagger UI + ReDoc 2종 인터랙티브 문서. 클라이언트 SDK 자동 생성 가능.
- **타입힌트 = 입력**: 새 DSL 없음, 표준 Python 타입 그대로.
- **검증**: JSON dict/list, str(min/max), int/float(min/max), URL/Email/UUID 등 Pydantic 위임.
- **보안**: HTTP Basic, OAuth2 + JWT, Header/Query/Cookie API 키 — 모두 OpenAPI 스키마에 자동 반영.
- **DI**: 의존성 그래프(의존성의 의존성), `yield` 클린업, 라우터 레벨 공유 dependencies.
- **품질 지표**: 100% test coverage + 100% type-annotated.

### 3. Public API 표면 (`fastapi/__init__.py`)

```python
from fastapi import (
    FastAPI, APIRouter, BackgroundTasks, UploadFile,
    HTTPException, WebSocketException,
    Body, Cookie, Depends, File, Form, Header, Path, Query, Security,
    Request, Response, WebSocket, WebSocketDisconnect,
)
from starlette import status
```

핵심 25개 심볼 + Starlette `status`. 코어는 `applications.py` (181KB) + `routing.py` (197KB) + `param_functions.py` (69KB) 3대 파일에 집중.

### 4. **결정적 발견 — 라이브러리 번들 SKILL.md (`fastapi/.agents/skills/fastapi/`)**

```
fastapi/
└── .agents/
    └── skills/
        └── fastapi/
            ├── SKILL.md          # 10.4 KB, frontmatter: name, description
            └── references/
                ├── dependencies.md
                ├── streaming.md
                └── other-tools.md
```

`SKILL.md` frontmatter:

```markdown
---
name: fastapi
description: FastAPI best practices and conventions. Use when working with FastAPI APIs and Pydantic models for them. Keeps FastAPI code clean and up to date with the latest features and patterns, updated with new versions.
---
```

**구조는 [[anthropics-skills]] 표준 그대로** — Progressive Disclosure(짧은 SKILL.md + references/ 보조). 이로써 [[agent-skills]] 표준의 첫 OSS 라이브러리 self-hosted 사례가 되었다([[github-spec-kit]]의 Codex Skills 모드는 외부 통합 도구 사례).

### 5. SKILL.md가 강제하는 코딩 컨벤션 (10.4 KB)

| 권장 | 금지/지양 |
|------|----------|
| `fastapi dev` / `fastapi run` CLI | 다른 ASGI 서버 직접 실행 |
| `pyproject.toml [tool.fastapi] entrypoint` | 매번 path 인자 |
| **`Annotated[T, Path/Query/Depends(...)]`** | `T = Path/Query/Depends(...)` 디폴트 인자 패턴 |
| 함수 return type / `response_model=` | `ORJSONResponse`/`UJSONResponse` (deprecated, Pydantic Rust 직렬화로 통합) |
| router 레벨 `prefix`, `tags`, `dependencies=` | `include_router`에 동일 인자 전달 |
| `def`(threadpool 자동) — 의심되면 default | blocking 코드를 `async def` 안에서 직접 호출 |
| `Annotated[list[int], Field(min_length=1), Body]` | Pydantic `RootModel` |
| 함수 1개 = HTTP operation 1개 | `@app.api_route(methods=[...])` 다중 |
| 의존성 클래스 → 함수가 인스턴스 반환 | `Annotated[Class, Depends]` 직접 |
| **Asyncer** > AnyIO/asyncio | |
| **SQLModel** > SQLAlchemy | |
| **HTTPX** > Requests | |
| **uv / Ruff / ty** | |
| `...` (Ellipsis) 사용 안 함 | `Field(..., gt=0)` 등 |

→ **Tiangolo 생태계가 자체 권장 스택을 SKILL.md로 명시**하면서 LLM 에이전트가 자동으로 "FastAPI 다움"을 따르도록 유도.

### 6. 번역 자동화의 LLM 활용 (`docs/en/docs/_llm-test.md`)

- fastapi 문서 i18n은 LLM 번역 파이프라인(`scripts/translate.py` 일반 프롬프트 + `docs/{lang}/llm-prompt.md` 언어별 프롬프트)으로 운영.
- `_llm-test.md`는 **회귀 테스트 페이지** — 번역 후 결정적이지 않은 변경을 검출하기 위한 골든 셋(코드 스니펫, 따옴표, 코드 안 따옴표, code blocks 등 케이스).
- 위키 운영 측면에서: LLM 결과의 품질을 명세화된 스냅샷으로 측정하는 패턴.

## 주요 인사이트

1. **에이전트 시대 OSS 컨벤션의 굳어짐**
 - README는 사람용, **SKILL.md는 에이전트용**이라는 분업이 메인스트림 라이브러리에서 처음 명시됨.
 - 이는 [[agent-skills]] 표준이 단순한 Anthropic 사양을 넘어 **상호운용 가능한 OSS 패턴**으로 확산되는 전환점.
 - 정리하면 외부 채택 3단계 진화: ① anthropics/skills(표준 정의) → ② github/spec-kit(외부 도구의 Codex Skills 모드, 도구 통합) → ③ **fastapi/fastapi(라이브러리 self-hosted, 자기 코드 사용법을 자기가 출하)**.

2. **표준 위에 짓되 표준에 기여한다**
 - Pydantic JSON Schema 호환성, Starlette 비동기 베이스 — 둘 다 Tiangolo가 직접 PR한 결과.
 - 차용이 아니라 **공동 진화**(co-evolution)가 핵심. fastapi의 발전은 항상 의존성 라이브러리의 발전과 묶여 있음.

3. **에디터 검증 우선 설계**
 - 코드 작성 전 PyCharm/VS Code에서 시그니처 후보들을 실제로 입력해보며 자동완성이 가장 잘 동작하는 형태를 찾음.
 - 결과가 `Annotated[int, Path(ge=1)]` 같은 표면 — 시그니처 한 줄에 타입·검증·문서·DI가 동시에 표현되도록 설계.
 - 석근의 c2spf 분석 API 표준화 작업과 같은 패턴(개발자 경험 우선 → 표준 자동 생성 → 클라이언트 일원화).

4. **Pydantic 2 / Rust 직렬화 시대의 코드 컨벤션 변경**
 - `ORJSONResponse` 같은 별도 JSON 가속기는 **Pydantic 2의 Rust 코어 직렬화로 흡수** → 대신 응답 모델/타입을 정확히 선언하라.
 - 이는 [[backend-python-fastapi]]에 기록된 c2spf의 Pydantic v1/v2 마이그레이션과 직결되는 운영 시사점.

5. **`def` vs `async def` 디폴트 가이드**
 - SKILL.md는 **의심되면 `def`**을 권장(자동으로 threadpool에서 실행) — async 내부에서의 우발적 blocking이 운영 환경에서 가장 큰 성능 함정이라는 인식.

6. **Tiangolo 생태계의 묵시적 표준 스택**
 - SKILL.md에서 권장되는 비-FastAPI 라이브러리: **Asyncer · SQLModel · HTTPX · Typer**(전부 Tiangolo 작품) + **uv · Ruff · ty**(Astral).
 - "마이크로 모놀리스" 같은 패키지 큐레이션. 개인비서/BI 백엔드 신규 구축 시 **이 스택을 디폴트로 채택**할 합리적 근거가 됨.

## 인용할 만한 구절

> "FastAPI wouldn't exist if not for the previous work of others. (...) But at some point, there was no other option than creating something that provided all these features, taking the best ideas from previous tools, and combining them in the best way possible, using language features that weren't even available before (Python 3.6+ type hints)."
> — Sebastián Ramírez, history-design-future.md

> "Always prefer the `Annotated` style for parameter and dependency declarations. It keeps the function signatures working in other contexts, respects the types, allows reusability."
> — `fastapi/.agents/skills/fastapi/SKILL.md`

> "Do not use `ORJSONResponse` or `UJSONResponse`, they are deprecated. Instead, declare a return type or response model. Pydantic will handle the data serialization on the Rust side."
> — `SKILL.md` Performance 섹션

> "I'm using FastAPI a ton these days. (...) I'm actually planning to use it for all of my team's ML services at Microsoft."
> — Kabir Khan, Microsoft

## 관련 엔티티/개념

- [[fastapi]] — 새 엔티티 (도구). 본 소스가 정의 기반.
- [[tiangolo]] — 새 엔티티 (사람). Sebastián Ramírez의 OSS 생태계.
- [[agent-skills]] — 라이브러리 self-hosted SKILL.md 사례 추가.
- [[anthropics-skills]] — 표준 정의처. fastapi가 표준을 그대로 채택.
- [[github-spec-kit]] — Codex Skills 모드(도구 통합 사례)와 fastapi(라이브러리 사례)의 짝.
- [[backend-python-fastapi]] — 석근의 c2spf 애널리틱스 공통 API 운영 맥락. Pydantic v2 / `def` 기본 / `Annotated` 컨벤션 시사점이 직접 연결.
- [[c2spf-analytics|c2spf 게임 데이터 BI]] — `analytics-common-api`(FastAPI) 92% 단독 유지보수 — 이 위키의 직접적 운영 컨텍스트.

## 메모

- **ingest의 결정적 시사점**: fastapi/.agents/skills/ 발견은 [[agent-stack-evolution]] 종합 분석의 "표준-구현 분리(Anthropic축)" 명제를 강화 — 표준이 OSS 라이브러리에 침투했다는 정량적 증거.
- **후속 작업 후보**:
 1. `wiki/syntheses/agent-stack-evolution.md` 갱신 — 4번째 사례(library self-hosted skill) 반영.
 2. SKILL.md 컨벤션이 c2spf `analytics-common-api` 코드베이스의 어느 부분과 충돌/일치하는지 점검(특히 `Annotated`, `response_model`, `ORJSONResponse` 사용 여부).
 3. fastapi-cli + Asyncer + SQLModel + Typer + HTTPX 묶음을 "Tiangolo Default Stack"으로 별도 종합 페이지화 후보.
 4. `_llm-test.md` 패턴은 위키 자체 lint 워크플로우(LLM 출력 회귀 검사)에 응용 가능.
- **열린 질문**: SKILL.md의 권장이 c2spf의 기존 `result_code/message/data` envelope과 어떻게 결합될 수 있는가? envelope을 응답 모델로 만들고 generic으로 타입화하면 자동 OpenAPI 스키마와 충돌하지 않을지.
