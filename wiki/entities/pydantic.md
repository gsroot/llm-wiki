---
title: "Pydantic (pydantic/pydantic)"
type: entity
entity_type: tool
tags: [pydantic, python, validation, type-hints, json-schema, fastapi, openai-agents-python, mypy, pyright, pydantic-core, rust-extension, v1-to-v2-migration, version-policy, samuel-colvin, llms-txt, hyperlint, vale, logfire, pydantic-ai, annotated, pep-593, 18회차]
related: [[[fastapi]], [[openai-agents-python]], [[python-packaging]], [[uv]], [[sqlalchemy]], [[pydantic-ai]]]
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# Pydantic (pydantic/pydantic)

## 개요

9년차 ★27.6K Python 데이터 검증 라이브러리. **타입 힌트만으로 스키마 정의 + 자동 검증 + JSON Schema 생성** 패턴을 정착시킨 사실상 표준 — [[fastapi]] / [[openai-agents-python]] 모두 디폴트 의존성. V2(2023) ground-up rewrite로 `pydantic-core` Rust 확장 분리 + 5~50배 성능 개선 + V1 빌트인 `from pydantic import v1`로 점진적 마이그레이션 보장. 자매 제품 — Pydantic Logfire (관측성) / **[[pydantic-ai]] (LLM 에이전트, 18회차 수집 완료)**.

## Pydantic AI 연계 (18회차)

[[pydantic-ai]]는 README에서 본인을 "validation layer 원천"으로 명시:

> "Pydantic Validation is the validation layer of the OpenAI SDK, the Google ADK, the Anthropic SDK, LangChain, LlamaIndex, AutoGPT, Transformers, CrewAI, Instructor and many more."

→ Pydantic의 영향력 범위가 **LLM 프레임워크 전체로 확산**. Pydantic AI는 이 layer를 만든 팀이 직접 agent SDK로 위로 올라온 결과.

## 메타

- **저장소**: https://github.com/pydantic/pydantic
- **공식 문서**: [docs.pydantic.dev](https://docs.pydantic.dev)
- **PyPI**: `pydantic`
- **라이선스**: MIT
- **언어**: Python (`pydantic-core`만 Rust)
- **창설**: 2017-05-03 (9년차)
- **별점/포크**: ★27,613 / fork 2,570
- **저장소 크기**: 397 MB
- **Python 요구**: >=3.10
- **자매 제품**: Pydantic Logfire / Pydantic AI

## 주요 특징

### 1. 타입 힌트 = 스키마 정의

```python
from pydantic import BaseModel
class User(BaseModel):
    id: int
    name: str = 'John Doe'
    friends: list[int] = []
```

dict → 자동 검증 + 강제 변환. `external_data = {'id': '123'}`이면 `id=123` (int).

### 2. Annotated + 메타데이터 (V2)

PEP 593 표준 패턴 — `Annotated[float, Gt(0)]` / `Annotated[str, Field(max_length=50)]`. [[fastapi]] DI / [[sqlalchemy]] Mapped[...] 모두 같은 표현 → **단일 타입 체인**.

### 3. V2 = ground-up rewrite + Rust 확장

- **`pydantic-core`** Rust 검증 코어 (별도 PyPI 패키지)
- **5~50배 성능 향상**
- **명시 버전 정책** — "V1→V2 같은 magnitude 변경은 다시 없다"
- V1 빌트인: `from pydantic import v1 as pydantic_v1` → 점진적 마이그레이션

### 4. 명시 버전 정책

V2 minor에서 "breaking 아님" 정의 명시 — 미문서화 의존, JSON Schema $ref 형식 변경, ValidationError 키 추가 등. **명시 부분만 호환성 계약**으로 보호. [[openai-agents-python]] dataclass positional compatibility와 동일 철학.

### 5. llms.txt 표준 채택

README 첫 줄 배지에 `llms.txt-green`. [[openai-agents-python]] (14회차)에 이은 **두 번째 메이저 라이브러리 채택 사례**.

### 6. .hyperlint/ Vale 스타일 가이드

루트의 `.hyperlint/` 디렉토리 = 자연어 린터 Vale 룰셋. **문서 작성 자체를 자동 검증**. AGENTS.md/SLEP/Constitution이 코드 거버넌스라면 hyperlint는 문서 거버넌스.

### 7. mypy + Pyright + IDE 통합

타입 힌트 = 정적 타입 검사기 + IDE 호환. [[openai-agents-python]] pyright 채택 이유와 직결.

### 8. 자매 제품 일체화

- **Pydantic** = 검증
- **Pydantic Logfire** = 관측성 (19회차 수집 예정)
- **Pydantic AI** = LLM 에이전트 (18회차 수집 예정)

[[astral]] uv·ruff·ty 3제품과 같은 회사 차원 도구 일체화 패턴.

## 관련 개념

- [[python-packaging]]: PyPI 표준 패키지
- [[agent-stack-evolution]]: llms.txt 채택 패턴

## 관련 엔티티

- [[fastapi]]: Pydantic 없이 동작 불가
- [[openai-agents-python]]: `pydantic>=2.12` 디폴트 의존성
- [[sqlalchemy]]: 같은 Annotated 패턴 (SQLModel로 통합)
- [[uv]]: Pydantic 사용자가 사실상 모두 uv 사용

## 출처

- [[pydantic-pydantic]] — 본 저장소 1차 수집 (15회차, 2026-04-28)

## 메모

- Pydantic은 위키에 1차 자료가 없는 **사실상 가장 영향력 큰 Python 라이브러리** — FastAPI(9회차) / openai-agents-python(14회차) 모두 의존
- Pydantic 진영 3제품 (검증/Logfire/AI) 완성 후 Astral 3제품과 비교 가능
- 회사 BI 적용 — c2spf-analytics API 응답 모델 V2화 + Logfire 도입 시 자동 인스트루멘테이션
- `.hyperlint/` Vale 룰셋을 본 위키 자체 운영에 차용 가능
