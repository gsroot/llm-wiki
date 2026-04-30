---
title: astral-sh/ruff — Rust로 작성된 초고속 Python 린터·포매터 (Astral 회사 차원 표준화)
type: source
source_type: article
source_url: https://github.com/astral-sh/ruff
raw_path: raw/articles/astral-sh-ruff/
author: Astral (Charlie Marsh 외)
date_published: 2022-08-09
date_ingested: 2026-04-28
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
- agent-skills
- claude-md-import
- monorepo
- 800-rules
- fastapi
- pandas
- airflow
related:
- '[[astral]]'
- '[[uv]]'
- '[[fastapi]]'
- '[[pandas]]'
- '[[scikit-learn]]'
- '[[python-packaging]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[agent-stack-evolution]]'
confidence: high
inbound_count: 12
aliases:
- Astral Sh Ruff
- astral sh ruff
- astral-sh/ruff — Rust로 작성된 초고속 Python 린터·포매터
- astral-sh/ruff — Rust로 작성된 초고속 Python 린터·포매터 (Astral 회사 차원 표준화)
cited_by:
  - "[[agent-skills]]"
  - "[[backend-fastapi-stack]]"
  - "[[harness]]"
  - "[[python]]"
  - "[[ruff]]"
cited_by_count: 5
---

# astral-sh/ruff — Rust로 작성된 초고속 Python 린터·포매터

> [!tldr] 한 화면 요약 (모바일·RAG 첫 청크용)
> [[ruff|Ruff]] = Astral 첫 제품, Rust 단일 바이너리 Python 린터·포매터 (★47K). Flake8/Black/isort/pydocstyle/pyupgrade/autoflake 7+ 도구를 10~100배 빠르게 통합. **위키적 핵심**: 같은 회사 [[uv]]와 동일한 `CLAUDE.md = @AGENTS.md` 1줄 import = "회사 차원 표준화" 9번째 변형 + 동일 저장소에 차세대 타입 체커 ty 동시 개발. 본문 314줄.

## 한줄 요약

> Astral의 Python 도구 3제품(uv·ruff·ty) 중 첫 번째이자 ★47K Rust 단일 바이너리로 **Flake8/Black/isort/pydocstyle/pyupgrade/autoflake 등 7개 이상 도구를 10~100배 빠르게 통합**하고, 같은 회사의 [[uv]]와 동일한 `CLAUDE.md = @AGENTS.md` 1줄 import 패턴을 채택하여 **agent-skills 외부 채택 8단계 진화에서 "회사 차원 표준화"라는 9번째 변형 사례**를 박은 라이브러리 + 동일 저장소에 차세대 타입 체커 ty를 함께 개발 중.

## 메타

- **Repository**: astral-sh/ruff
- **별점/포크**: ★47,274 / fork 2,030 (수집일 2026-04-28 기준)
- **라이선스**: MIT
- **언어**: Rust (Python wrapper 포함)
- **PyPI 패키지**: `ruff`
- **창설일**: 2022-08-09 (3년 8개월차)
- **최종 push**: 2026-04-28 (수집일 당일까지 활발)
- **저장소 크기**: 134 MB
- **Topics**: linter, pep8, python, python3, ruff, rust, rustpython, static-analysis, static-code-analysis, style-guide, styleguide
- **Astral 라인업 동거**: 본 저장소가 ruff(린터·포매터) + ty(타입 체커) 두 제품을 같이 개발. `ruff_*` (Ruff 전용) + `ty_*` (ty 전용) 크레이트 명명 컨벤션. ty는 ruff_python_parser·ruff_python_ast 등을 재사용
- **공식 문서**: [docs.astral.sh/ruff](https://docs.astral.sh/ruff/) + [Playground](https://play.ruff.rs/)
- **개발 토론**: Discord (Astral 서버)

## raw 파일 구조 (보관 12개 파일, 약 232KB)

```
raw/articles/astral-sh-ruff/
├── README.md (39KB) — 인스톨 / 800+ 룰 / 사용 사례 / 700+ Who's Using Ruff
├── AGENTS.md (4.2KB) ★ 개발 가이드라인 + ty mdtest + Salsa incrementality
├── CLAUDE.md (12B) ★ `@AGENTS.md`
├── BREAKING_CHANGES.md
├── CONTRIBUTING.md
├── pyproject.toml
├── Cargo.toml — Rust workspace
├── mkdocs.yml
├── .claude_settings.json — `.claude/settings.json` (Claude Code hook 설정)
├── docs_configuration.md ★ pyproject.toml 통합 + monorepo cascading
├── docs_linter.md ★ 룰 카테고리 + 자동 수정
├── docs_formatter.md ★ Black 호환
└── docs_preview.md ★ 새 룰 점진적 노출
```

**제외**: `crates/` Rust 본체 (수십 MB), `python/` 래퍼, `playground/`, `fuzz/`, `assets/`, `changelogs/`, `scripts/`, `tests/`, `_typos.toml`, `clippy.toml`, `rustfmt.toml`.

## 핵심 내용

### 1. 10~100배 속도 + 7개 이상 도구 통합

Black/Flake8/isort/pydocstyle/pyupgrade/autoflake 등을 **단일 Rust 바이너리**로 대체. 800+ 룰 + 자동 수정. 인용 사례:

- **Sebastián Ramírez (FastAPI 창시자)**: "Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually running and checking the code."
- **Nick Schrock (Elementl 창업자, GraphQL 공동 창시자)**: "Primarily because it is nearly 1000x faster. ... pylint takes about 2.5 minutes ... ruff takes .4 seconds. (250k LOC)"
- **Bryan Van de Ven (Bokeh 공동 창시자, Conda 원저자)**: "~150-200x faster than flake8 ... 0.2s instead of 20s."
- **Timothy Crosley (isort 창시자)**: "so fast I couldn't believe it was working till I intentionally introduced some errors."

대규모 채택: Apache Airflow, Apache Superset, FastAPI, Hugging Face, Pandas, SciPy, Zulip, dagster.

### 2. CLAUDE.md = @AGENTS.md — Astral 회사 차원 표준화

루트 `CLAUDE.md`는 단 한 줄:
```
@AGENTS.md
```

같은 회사 [[uv]]와 **완전히 동일한 패턴**. 즉 Astral은 자체 도구 3제품 (ruff·uv·ty) 모두에서 같은 컨벤션을 채택. `ty`는 같은 저장소에 동거하므로 자동 적용. 이는:

- **agent-skills 외부 채택 8단계 진화의 9번째 변형 사례**, 그러나 패턴 자체는 4번째(uv)와 동일
- 따라서 진정한 새 패턴은 **"회사 단위 표준화 (Company-level Standardization)"** — 같은 조직이 모든 제품에 같은 컨벤션을 채택
- agent-skills 외부 채택을 "조직별 채택" → "조직 내 표준화"로 한 단계 더 세분화하는 신호

| 단계 | 저장소 | 패턴 | 회사 |
|------|--------|------|------|
| 1 | anthropics/skills | SKILL.md 패키지 표준 정의 | Anthropic |
| 2 | github/spec-kit | Codex Skills 메소드론 | GitHub |
| 3 | fastapi/fastapi | self-hosted SKILL.md | tiangolo (개인) |
| 4 | astral-sh/uv | `@AGENTS.md` 1줄 import | **Astral** |
| 5 | scikit-learn/scikit-learn | SLEP + AGENTS.md AI disclosure | scikit-learn community |
| 6 | flutter/flutter | vendor-neutral `.agents/` | Google |
| 7 | openai/openai-cookbook | 살아있는 AGENTS.md | OpenAI |
| 8 | openai/openai-agents-python | AGENTS.md=CLAUDE.md 동기화 + 9개 SOP | OpenAI |
| **9** | **astral-sh/ruff** | **uv와 동일 패턴 → 회사 차원 표준화** | **Astral (재차)** |

### 3. AGENTS.md 개발 가이드라인 (4.2KB) — 14개 항목

읽어보면 단순한 일반 개발 가이드를 넘어 **AI 에이전트 작업용 명시 규칙**이 다수 포함:

| # | 가이드라인 | 비고 |
|---|--------|------|
| 1 | "All changes must be tested. If you're not testing your changes, you're not done." | 테스트 강제 |
| 2 | "Look to see if your tests could go in an existing file..." | 새 파일 자제 |
| 3 | "Get your tests to pass. If you didn't run the tests, your code does not work." | 검증 강제 |
| 4 | "Follow existing code style. Check neighboring files for patterns." | 패턴 일관성 |
| 5 | Rust imports always at top, never local in functions | 명시 스타일 |
| 6 | "Always run `uvx prek run -a` at the end of a task" | pre-commit 자동화 |
| 7 | "Avoid writing significant amounts of new code." | 기존 메커니즘 우선 |
| 8 | "Try hard to avoid `panic!`, `unreachable!`, `.unwrap`" | 타입 시스템에 인코딩 |
| 9 | "Prefer let chains (`if let && ...`) over nested `if let`" | Rust 모던 스타일 |
| 10 | "Use `#[expect]` over `#[allow]`" | Clippy 지시 |
| 11 | "Don't use comments to narrate code, but do use them for invariants" | 주석 정책 |
| 12 | ty 에러 메시지 narrow terminal 고려 | 사용자 경험 |
| 13 | "Salsa incrementality (ty): Any `.node` access must be `#[salsa::tracked]`" | 인크리멘털 컴파일 |
| 14 | "Run `cargo dev generate-all` after changing config" | 자동 재생성 |

각 가이드라인은 AI 에이전트가 **"왜 이렇게 해야 하는가"**까지 명시. 예를 들어 8번은 "panic!을 피하라"가 아니라 "타입 시스템에 인코딩하라"는 대안 제시.

### 4. ty 차세대 타입 체커 (mdtest 패턴)

같은 저장소에서 `ty` Python 타입 체커 개발. 결정적 발견 — **mdtest**:

- 테스트 파일이 **Markdown** (`crates/ty_python_semantic/resources/mdtest/<path>.md`)
- 헤더 텍스트가 테스트 케이스 이름 → `MDTEST_TEST_FILTER="<filter>"`로 단일 케이스 실행
- 스냅샷 자동 갱신: `MDTEST_UPDATE_SNAPSHOTS=1`
- AGENTS.md가 명시 — "After running the tests, always review the contents of any snapshots that have been added or updated."

이는 [[scikit-learn]] doctest와는 완전 다른 모델 — 타입 체커는 **자연어로 시나리오 설명 + 코드 + 기대 진단**의 3구조가 자연스럽기 때문. 회사 BI에 적용 시: SQL 쿼리 회귀 테스트를 mdtest 형태로 작성 가능 ("게임 출시 직후 D+1 활성 유저 = N명 → 쿼리 X 결과 동일").

### 5. ty Salsa Incrementality (Rust 인크리멘털 컴파일러)

> "Any method that accesses `.node` must be `#[salsa::tracked]`, or it will break incrementality. Prefer higher-level semantic APIs over raw AST access."

Salsa는 Rust 인크리멘털 컴파일러 프레임워크 (rust-analyzer가 사용). ty가 같은 패턴 채택. **AST 접근을 추적된 함수로 감싸 변경 영향 범위만 재계산**. AGENTS.md가 이 규칙을 깨면 인크리멘털리티가 망가진다고 명시.

### 6. uvx prek run -a — 회사 도구 스택 자동 강제

`uvx`는 [[uv]]가 제공하는 일회성 실행 명령. `prek`는 pre-commit-conformat (또는 비슷한) 도구. AGENTS.md가 "task 종료/리베이스/리뷰 코멘트 응대/푸시 전" 모두에서 자동 호출 강제. **회사 도구 스택을 AGENTS.md에 박음** 패턴 — fastapi와 openai-agents-python에서도 본 동일 패턴.

### 7. monorepo 친화적 cascading 설정

`docs/configuration.md`:

- `pyproject.toml` `[tool.ruff]` 섹션 통합 (별도 `.ruff.toml`도 가능)
- 디렉토리 계층마다 cascading 적용 — 상위 + 하위 가까운 설정 둘 다
- monorepo 시나리오에서 패키지별 다른 룰 자연스럽게 처리
- `--isolated` 플래그로 cascading 무시도 가능

이는 회사 BI c2spf-analytics가 모노레포라면 c2spf-platform (cmd backend) / c2spf-render (frontend) / c2spf-ml (Python 분석) 각자 독립 룰셋 운영 가능.

## 인사이트

### Insight 1: agent-skills 8단계 진화 → 9번째 "회사 차원 표준화" 신호

ruff의 `CLAUDE.md = @AGENTS.md`는 uv와 정확히 같은 패턴 — 즉 새 패턴이 아니라 **같은 회사의 또 다른 제품**. 이는 다음을 시사:

- agent-skills 외부 채택은 "조직 차원"을 넘어 **"조직 내 표준화"로 한 단계 진화**
- Astral 같은 회사가 향후 출시할 ty(이미 같은 저장소), 또는 새 제품도 같은 패턴 채택할 것
- 회사 단위 컨벤션을 강요하는 메커니즘이 없으나 **자연스럽게 한 회사 내 도구가 같은 컨벤션을 따라가는 패턴이 발견**됨
- 따라서 다른 회사들도 ("OpenAI는 cookbook + agents-python 둘 다 살아있는 AGENTS.md", "Google은 flutter + (대상 후보 dart)") 같은 패턴이 나타날 가능성 높음

### Insight 2: Astral 도구 일체화 — uv(패키징) + ruff(린트/포맷) + ty(타입) = "Rust 통합 디폴트 스택"

[[fastapi]] SKILL.md가 명시한 디폴트 스택 (FastAPI/SQLModel/Asyncer/HTTPX/Typer/uv/Ruff/ty) 중 **마지막 3개가 모두 Astral 제품**. Astral의 비전:

- **uv** = pip + virtualenv + pyenv + pipx + poetry 통합
- **ruff** = Black + Flake8 + isort + pydocstyle + pyupgrade + autoflake 통합 ()
- **ty** = mypy / pyright 차세대 (개발 중)

세 도구 모두 Rust + 기존 도구 N개 통합. 회사 BI 적용 시 "Python 도구 단일 진입점"으로 c2spf-analytics 마이그레이션 ROI 분석 후속 후보. fastapi 디폴트 스택 → uv 본체 → scikit-learn 거버넌스 → openai-agents-python ruff/uv/pyright → ruff 본체로 **Astral 도구 스택의 위키 내 가시성 완성**.

### Insight 3: AGENTS.md = 14항목 개발 가이드라인 = AI 명령

ruff AGENTS.md는 anthropics-skills SKILL.md 패키지나 openai-agents-python 9개 SOP와는 다른 형태:

- **단일 .md 4.2KB** (vs anthropics-skills 패키지 / openai-agents-python 9개 분리)
- **개발자 가이드 + AI 에이전트 명령의 이중 역할** — 사람도 읽고 AI도 읽는 자연어
- **각 룰에 이유 명시** ("avoid panic! → 타입 시스템에 인코딩하라")
- **자동 강제 명령 포함** ("Always run `uvx prek run -a` at the end")

이는 **단일 .md 자연어 가이드 패턴**의 첫 회사 차원 사례. 본 위키 CLAUDE.md도 같은 형태 (AGENTS.md import). 회사 BI c2spf-analytics에 적용 시 AGENTS.md 한 파일에 14~20개 운영 규칙 박는 형태 차용 가능.

### Insight 4: ty mdtest = 자연어 + 코드 + 기대 진단의 3구조

mdtest 패턴은 SLEP doctest와 다음과 같이 다름:

| 측면 | scikit-learn doctest | ruff/ty mdtest |
|------|------|------|
| 위치 | docstring 안 | 별도 .md 파일 |
| 형식 | `>>> code` | Markdown 헤더 + 코드 블록 |
| 검증 | 출력 비교 | 진단(diagnostic) 메시지 비교 |
| 인덱스 | 함수 단위 | 시나리오 헤더 단위 |
| 자연어 | 짧은 docstring | 충분한 설명 |
| 실행 | `pytest --doctest-modules` | `MDTEST_TEST_FILTER` |

타입 체커처럼 **"이 코드가 X 진단을 내야 한다"**가 자연스러운 도메인에서는 mdtest가 우수. SQL 쿼리 회귀 (BigQuery EXPLAIN 결과)나 API 계약 (스키마 진단)에 적용 가능 후보.

### Insight 5: 700+ Who's Using Ruff = Python OSS 대규모 채택 표준

README의 "Who's Using Ruff" 섹션이 매우 김 (Apache Airflow, Apache Superset, AWS APIs, Beanie, BentoML, Bokeh, Bottlerocket, Bytewax, ...). 700개 이상 명시. 이는 Python OSS의 사실상 표준이 된 증거.

대규모 채택의 결정적 요인:
- **속도** (10~100x) — CI 파이프라인 단축으로 직접 ROI
- **단일 도구** — N개 도구 + N개 설정 → 1개로
- **호환성** — Black/Flake8/isort 자동 마이그레이션
- **자동 수정** — `ruff check --fix`로 즉시 정정

c2spf-analytics 적용 시 ROI 추정: pylint/black 분리 → ruff 통합 시 CI 30~60s → 5s 이하.

### Insight 6: 자동 수정(autofix) + Preview Mode = 점진적 룰 도입

`docs/preview.md`는 **새 룰을 안정 룰셋과 분리**하여 점진적 노출:

- `--preview` 플래그로만 활성화
- 안정화 후 일반 룰로 승격
- 사용자가 "현재 통과하는 코드가 갑자기 fail" 위험 없이 새 룰 시도

이는 [[scikit-learn]] SLEP의 점진적 진화 패턴, [[openai-agents-python]]의 Public API Positional Compatibility와 **같은 "안정성 vs 진화" 양립 패턴**의 또 다른 형태.

### Insight 7: 800+ 룰 + 자동 재생성 — `cargo dev generate-all`

AGENTS.md 마지막 항목: "Run `cargo dev generate-all` after changing configuration options, CLI arguments, lint rules, or environment variable definitions, as these changes require regeneration of schemas, docs, and CLI references."

이는 **"진실 단일 소스 + 자동 동기화"** 패턴 — 코드(Rust)가 진실, 룰 정의를 변경하면 자동으로 docs / JSON Schema / CLI reference 모두 재생성. [[openai-cookbook]] `check_notebooks.py` registry.yaml 자동 검증과 같은 계열.

본 위키도 `wiki/index.md`를 frontmatter에서 자동 생성하는 PoC로 차용 가능.

## 인용 (raw에서 직접 발췌)

### AGENTS.md — 14개 가이드라인 중 핵심 5개

> All changes must be tested. If you're not testing your changes, you're not done.

> Avoid writing significant amounts of new code. This is often a sign that we're missing an existing method or mechanism that could help solve the problem. Look for existing utilities first.

> Try hard to avoid patterns that require `panic!`, `unreachable!`, or `.unwrap`. Instead, try to encode those constraints in the type system. Don't be afraid to write code that's more verbose or requires largeish refactors if it enables you to avoid these unsafe calls.

> Use comments purposefully. Don't use comments to narrate code, but do use them to explain invariants and why something unusual was done a particular way.

> Salsa incrementality (ty): Any method that accesses `.node` must be `#[salsa::tracked]`, or it will break incrementality. Prefer higher-level semantic APIs over raw AST access.

### CLAUDE.md (전문 — 12바이트)

> @AGENTS.md

### README.md — Sebastián Ramírez 인용

> Ruff is so fast that sometimes I add an intentional bug in the code just to confirm it's actually running and checking the code.
> — Sebastián Ramírez (FastAPI 창시자)

### docs/preview.md — 점진적 룰 도입 정책

> Preview mode enables a "preview" set of rules and behaviors that have been deemed safe to opt-in to but are not yet stable. Preview mode is intended to allow users to test out new behaviors before they become the default.

## 후속 탐구

1. **ty 본체 단독 수집** — `crates/ty_*` Rust 코드 + `crates/ty_python_semantic/resources/mdtest/` 본체
2. **prek 도구 분석** — uvx로 호출되는 pre-commit 도구의 정체 및 ruff/uv 통합 메커니즘
3. **BREAKING_CHANGES.md 변경 이력** — ruff의 호환성 정책 vs scikit-learn SLEP / openai-agents-python Positional Compatibility 비교
4. **`cargo dev generate-all` 실제 출력물** — schemas/docs/CLI reference 자동 재생성 메커니즘이 위키 index.md 자동 생성 PoC에 그대로 차용 가능한지
5. **800+ 룰 카테고리 매핑** — Flake8 plugin들과 1:1 대응 표
6. **Astral의 다음 제품** — uv·ruff·ty 다음 후보 (혹은 c2spf 같은 회사 차원 도구 통합 차용)
7. **Apache Airflow / Hugging Face / Pandas Ruff 채택 PR** — 대규모 코드베이스 마이그레이션 사례 분석
8. **Charlie Marsh 인터뷰/블로그 분석** — Astral 비전 1차 자료

## 회사 BI 적용 가설

### 가설 1: c2spf-analytics ruff 도입

가설로 제시한 "c2spf-analytics uv 마이그레이션"과 한 묶음으로 ruff 도입. CI 파이프라인 변화:

| 단계 | 기존 (Jenkins) | ruff 도입 후 |
|------|------|------|
| Lint | pylint 30s + flake8 15s | ruff check 1~2s |
| Format | black 5s | ruff format 0.5s |
| Imports | isort 3s | (ruff 통합) |
| 합계 | 53s | ~3s (15~20x 단축) |

c2spf-analytics 모노레포라면 cascading 설정으로 backend/frontend/ml 각자 독립 룰셋. ROI: CI 시간 절감 + 개발자 IDE에서 즉시 피드백.

### 가설 2: AGENTS.md 14항목 가이드라인을 c2spf 팀 운영에 차용

ruff AGENTS.md의 14항목 같은 형태로 c2spf-analytics 자체 AGENTS.md 작성:

- "BigQuery 쿼리는 dry-run + 비용 추정 후 배포"
- "Pandas → BigFrames 마이그레이션 시 100% 동치 테스트"
- "Grafana 대시보드 변경은 staging 24h 검증 후 프로덕션"
- "결제 데이터 쿼리는 `[financial]` 태그 필수 + 별도 review"

각 항목에 **이유 명시**(ruff 패턴) — "왜 이렇게 해야 하는가". 신규 입사자 + AI 에이전트 모두 24시간 내 운영 표준 학습 가능.

### 가설 3: ty mdtest를 BI 회귀 테스트에 차용

게임 출시 전후 핵심 메트릭 회귀 테스트를 mdtest 형태로 작성. 자연어 + SQL + 기대 결과의 3구조가 BI 도메인에 자연스럽게 맞음. 회귀 발생 시 단일 케이스 디버깅 가능.

## 메모

[[uv]]의 자매 제품 수집. 같은 [[astral]] 회사의 두 번째 제품이 같은 컨벤션을 정확히 답습 — agent-skills 외부 채택 패턴이 "조직 외부 채택" → "조직 내 표준화"로 한 단계 진화. 다음 후보로 ty 본체 단독 수집 시 **3제품 일체화**가 위키에 박힐 것. 또한 발견 "회사 차원 표준화" 패턴은 같은 회사 여러 제품 수집 시 (예: pmndrs 진영의 Zustand·Jotai·Recoil, Vercel 진영의 Next.js·SWR·AI SDK) 다시 검증할 가설.
