---
title: Ruff (astral-sh/ruff)
aliases:
- Ruff
- 러프
type: entity
entity_type: tool
tags:
- ruff
- astral
- python
- linter
- formatter
- rust
- pep8
- ty
- agents-md
- claude-md-import
- 800-rules
related:
- '[[astral]]'
- '[[uv]]'
- '[[fastapi]]'
- '[[python-packaging]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[astral-sh-ruff]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 6
inbound_count: 41
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 24
---

# Ruff (astral-sh/ruff)

## 개요

[[astral]] 회사의 Python 도구 3제품 (uv·ruff·ty) 중 첫 번째. **Rust 단일 바이너리로 Black + Flake8 + isort + pydocstyle + pyupgrade + autoflake 등 7개+ 도구를 10~100배 빠르게 통합**한 린터·포매터. ★47K, 800+ 룰, Apache Airflow / FastAPI / Pandas / SciPy / Hugging Face 등 700+ OSS 채택. 같은 저장소에서 차세대 타입 체커 ty를 동거 개발 — Astral의 Python 도구 일체화 비전.

## 메타

- **저장소**: https://github.com/astral-sh/ruff
- **공식 문서**: [docs.astral.sh/ruff](https://docs.astral.sh/ruff/) + [Playground](https://play.ruff.rs/)
- **PyPI**: `ruff`
- **라이선스**: MIT
- **언어**: Rust (Python wrapper 포함)
- **창설**: 2022-08-09 (3년 8개월차)
- **별점/포크**: ★47,274 / fork 2,030
- **저장소 크기**: 134 MB

## 주요 특징

### 1. 통합된 도구

- **린트**: Flake8 + 수십 개 플러그인 (flake8-bugbear 등)
- **포맷**: Black 호환
- **import 정렬**: isort 호환
- **docstring**: pydocstyle
- **업그레이드**: pyupgrade
- **자동 수정**: `ruff check --fix`
- **모노레포 cascading**: pyproject.toml `[tool.ruff]` 통합

### 2. ty 차세대 타입 체커 (동거)

- 같은 저장소 안에 Rust 크레이트로 동거 (`ty_*` 명명 컨벤션)
- ruff_python_parser / ruff_python_ast 재사용
- **mdtest 패턴** — Markdown 파일에 시나리오 + 코드 + 기대 진단의 3구조 테스트
- **Salsa Incrementality** — `.node()` 접근은 `#[salsa::tracked]`로 감싸 변경 영향만 재계산

### 3. CLAUDE.md = @AGENTS.md 패턴 ([[uv]]와 동일)

루트 `CLAUDE.md`가 12바이트 — `@AGENTS.md`. 같은 회사 [[uv]] (10회차)와 동일 패턴 → **agent-skills 외부 채택 8단계 진화의 9번째 변형 사례 = "회사 차원 표준화"**.

### 4. AGENTS.md 14항목 개발 가이드라인

- 모든 변경 테스트 강제
- 새 코드 작성 자제 ("기존 메커니즘 우선")
- panic!/unreachable!/unwrap() 회피 → 타입 시스템에 인코딩
- `uvx prek run -a` task 종료 시 자동 강제
- ty Salsa incrementality
- `cargo dev generate-all` 자동 재생성

각 항목에 **이유 명시** ("왜 이렇게 해야 하는가").

### 5. 800+ 룰 + Preview Mode

새 룰을 `--preview` 플래그로 점진적 노출 → 안정 룰 영향 없이 사용자 시도 가능. [[scikit-learn]] SLEP / [[openai-agents-python]] Public API Positional Compatibility와 같은 **"안정성 vs 진화" 양립** 패턴.

### 6. 대규모 채택

Apache Airflow, Apache Superset, FastAPI, Hugging Face, Pandas, SciPy, Zulip, dagster ... 700+. 결정적 요인 — 속도 (10~100x) / 단일 도구 / 호환성 / 자동 수정.

### 7. 자동 재생성 (`cargo dev generate-all`)

룰 정의 변경 시 schemas / docs / CLI reference 모두 자동 재생성. **"진실 단일 소스 + 자동 동기화"** 패턴.

## 관련 개념

- [[agent-skills]]: 9번째 외부 채택 사례 (회사 차원 표준화)
- [[harness]]: 14항목 AGENTS.md = AI 에이전트 작업용 명시 규칙
- [[python-packaging]]: pyproject.toml `[tool.ruff]` 통합

## 관련 엔티티

- [[astral]]: 운영 회사 (uv·ruff·ty 3제품)
- [[uv]]: 자매 도구 (10회차 수집), 같은 `CLAUDE.md = @AGENTS.md` 패턴
- [[fastapi]]: SKILL.md 디폴트 스택에 포함 (9회차)

## 의사결정 컨텍스트 (raw 인용)

> "Astral의 Python 도구 3제품(uv·ruff·ty) 중 첫 번째이자 ★47K Rust 단일 바이너리로 Flake8/Black/isort/pydocstyle/pyupgrade/autoflake 등 7개 이상 도구를 10~100배 빠르게 통합하고, 같은 회사의 uv(10회차 수집)와 동일한 CLAUDE.md = @AGENTS.md 1줄 import 패턴을 채택."
> — [[astral-sh-ruff]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 개발 도구 영역. [[uv]](Astral 1번 도구)와 함께 [[matechat|MateChat 사이드 프로젝트]]·[[c2spf-analytics|c2spf 게임 데이터 BI]] 양쪽 표준화 후보. **회사 차원 표준화**(Astral) 거버넌스 모델은 [[bdfl]]·[[pdep]] 등과 함께 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 OSS 거버넌스 카탈로그 9번째 모델로 등록. 차세대 ty 타입 체커 동일 저장소.

## 출처

- [[astral-sh-ruff]] — 본 저장소 1차 수집 (15회차, 2026-04-28)

## 메모

- ruff = 본 위키에서 [[uv]]와 한 묶음 — Astral 회사 차원 표준화 검증
- ty 본체 단독 수집은 별도 회차 후보 (Rust 본체 + mdtest 본체)
- prek 도구의 정체 추가 분석 필요 (uvx로 호출되는 pre-commit 도구)
- 회사 BI c2spf-analytics 적용 시 pylint/black 분리 → ruff 통합으로 CI 53s → 3s (15~20x 단축) 추정
- AGENTS.md 14항목 패턴을 c2spf 자체 운영 가이드에 차용 가능
