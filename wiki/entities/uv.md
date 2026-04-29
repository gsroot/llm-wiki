---
title: "uv (astral-sh/uv)"
type: entity
entity_type: tool
tags: [uv, astral, python, package-manager, rust, pubgrub, universal-lockfile, pep-723, virtualenv, pyenv, poetry, pipx, pip-tools, twine, agents-md]
related:
  - "[[astral]]"
  - "[[python-packaging]]"
  - "[[github]]"
  - "[[anthropic]]"
  - "[[ruff]]"
  - "[[fastapi]]"
  - "[[pydantic]]"
  - "[[astral-sh-uv]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-28
---

# uv (astral-sh/uv)

## 개요

uv는 [[astral]]이 Rust로 작성한 Python 패키지·프로젝트 매니저다. README 첫 줄: *"An extremely fast Python package and project manager, written in Rust."*

단일 정적 바이너리로 **`pip` · `pip-tools` · `pipx` · `poetry` · `pyenv` · `twine` · `virtualenv` 7개 도구를 대체**하고, pip 대비 10–100x 빠르며, **universal lockfile**(플랫폼 독립 `uv.lock`)을 표준화한다. 2024-02 첫 릴리스 후 약 2년 만에 ★84,003개 (2026-04-27 기준)로 Python 생태계의 사실상 표준 패키지 매니저로 부상.

이름 표기: 항상 소문자 `uv` (README FAQ: *"Just 'uv', please."*). 발음: "you-vee" (`/juː viː/`).

## 주요 특징

### 6개 기능군 (독립 사용 가능)

| 기능군 | 명령 | 대체 대상 |
|--------|------|----------|
| **Python versions** | `uv python install/list/find/pin/uninstall` | pyenv |
| **Scripts** | `uv run script.py` (PEP 723 인라인 metadata) | pipx run + venv |
| **Projects** | `uv init/add/remove/sync/lock/run/tree/build/publish` | poetry / PDM / rye |
| **Tools** | `uvx`, `uv tool install/run/list` | pipx |
| **The pip interface** | `uv pip install/sync/compile/freeze/check`, `uv venv` | pip / pip-tools / virtualenv |
| **Utility** | `uv cache clean/prune/dir`, `uv self update` | (신규) |

### Universal Lockfile (`uv.lock`)

uv의 시그니처 차별점. PEP 508 markers를 활용해 macOS/Linux/Windows × CPython/PyPy × x86_64/aarch64 조합 모두에 단일 lockfile이 작동하도록 멀티버전을 잠근다. pip-tools가 플랫폼 의존적인 것과 정반대.

기본 `uv lock`은 universal. pip 인터페이스에서는 `uv pip compile --universal` 플래그로 동일 동작.

### 핵심 아키텍처 결정

1. **Rust 단일 바이너리** — Python 인터프리터 시동 비용 0
2. **PubGrub resolver** — Cargo가 사용하는 SAT-style 알고리즘. 충돌 시 인간 친화적 설명
3. **글로벌 캐시 + hardlink/reflink** — macOS=reflink, Linux=hardlink. 동일 wheel을 프로젝트별로 중복 설치하지 않음
4. **Tokio async I/O** — 병렬 다운로드
5. **Cargo-style workspaces** — `[tool.uv.workspace]`, 멤버 간 path/git/registry source

### 듀얼 지침서 패턴 — `AGENTS.md` + `CLAUDE.md`

uv 저장소는 LLM 에이전트 협업을 위해 **단일 진실원** 패턴을 채택했다:
- **`CLAUDE.md`** (1줄): `@AGENTS.md`만 import
- **`AGENTS.md`** (20줄): Rust 개발 규칙 — [[anthropic]] AGENTS.md 표준의 외부 산업 채택 사례

이는 [[github-spec-kit]]의 4축 통합과 정반대 극단으로, "표준 위에 도구별 어댑터" 미니멀 패턴.

### PEP 723 인라인 의존성 — 단일 파일 자급자족

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["requests"]
# ///
import requests
```

`uv run example.py`만으로 격리 venv 자동 생성·실행. [[karpathy]]식 단일 파일 철학의 일반화.

### 보안 — 활발한 대응

CHANGELOG v0.11.6 (2026-04-09): wheel RECORD 파싱 취약점 advisory(GHSA-pjjw-68hj-v9mw) 5일 내 patch + healing 로직. v0.11.7~0.11.8: TLS 인증 검증 강화, pre-signed URL redact.

### 릴리스 케이던스

- **v0.5.0 → v0.11.8 (현재)** in CHANGELOG.md (742줄)
- 패치/마이너 사이클: **2~3주**
- **v0.11.8 = 2026-04-27 (본 위키 수집일 당일 릴리스)** — 매우 활발

## 관련 개념

- [[python-packaging]]: uv가 통합·구현하는 Python 패키징 표준 (PEP 517/518/621/723/735, dependency-groups 등)
- [[harness]]: uv 저장소의 `AGENTS.md` 20줄 = minimal harness의 산업판 — [[anthropic]] 패키지 두께와 대비
- [[agent-skills]]: AGENTS.md 표준 채택 사례 트래킹 — uv는 외부 산업 채택의 대표
- [[autonomous-research-loop]]: PEP 723 + `uv run` = 단일 파일 자급자족 실험 루프 인프라
- [[backend-python-fastapi]]: FastAPI 백엔드의 의존성 관리 후보 (마이그레이션 ROI 높음)

## 관련 엔티티

- [[astral]]: 운영 주체 (ruff·ty 동일사)
- [[github]]: 호스팅, advisory 채널
- [[anthropic]]: AGENTS.md 표준 발행자, uv는 채택자
- [[seokgeun-kim|석근 (이 위키 owner)]]: 잠재 채택자 — 회사 BI [[c2spf-analytics|c2spf 게임 데이터 BI]] 마이그레이션 후보
- [[karpathy]]: 단일 파일 철학 공명 (`uv run` + PEP 723)
- [[c2spf-analytics]]: FastAPI + Python 환경, uv 채택 가능성 검토 대상
- [[github-spec-kit]]: 다축 통합 vs uv 재구현 통합 — 정반대 극단

## 의사결정 컨텍스트 (raw 인용)

> "uv는 pip · pip-tools · pipx · poetry · pyenv · twine · virtualenv 7가지 도구를 단일 Rust 바이너리로 통합하고, pip 대비 10–100배 빠른 성능과 universal lockfile을 제공하는 Astral의 Python 도구체인."
> — [[astral-sh-uv]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] Python 패키지 관리 표준. [[matechat|MateChat 사이드 프로젝트]] backend + [[c2spf-analytics]] 후보. [[ruff]]와 함께 Astral 회사 표준 (CLAUDE.md = @AGENTS.md 1줄 import 패턴). **7개 도구 통합 + universal lockfile**이 Python 생태 fragmentation 해소 사례 — [[python-packaging]] 개념 페이지의 출처. **Rust-in-Python** 트렌드는 [[ruff]]·[[polars]]·[[pydantic]]과 함께 5축 LLM 인프라 메타에 등록.

## 출처

- [[astral-sh-uv]] — uv 자체 저장소 수집 (37개 파일, README/AGENTS.md/CLAUDE.md/CHANGELOG/BENCHMARKS/STYLE/CONTRIBUTING/SECURITY + docs/index/getting-started/concepts/projects/guides)

## 논쟁/모순

- **PEP 723 빠른 채택 vs 표준 안정성**: uv는 PEP 723 인라인 metadata를 빠르게 prod-ready로 채택했지만, 표준이 정착하기 전 채택은 향후 incompatibility 위험이 있다는 우려가 일부 PyPA 진영에 있음.
- **`tool.uv.sources` vs PEP 표준**: uv 고유 확장 (git/path/index alternative source). 다른 도구로의 마이그레이션 시 lockfile 호환성 깨짐. Astral은 PEP 표준화 추진 중이라 함.
- **Rust 의존도**: uv는 Python 도구이지만 본체는 Rust. Python 코어 컨트리뷰터 충원 채널은 별개. 일부 Python 커뮤니티에서 "Python의 미래가 Rust에 의존하는가" 논쟁 진행 중.

## 메모

- **회사 BI 마이그레이션 가설**: [[c2spf-analytics]] FastAPI 백엔드 + Jenkins CI 환경에서 pip → uv 전환 시 효과 추정:
  - Cold install 시간: 5분 → 10초 수준 (CI 단축 효과 직접)
  - lockfile universal로 macOS 개발 / Linux Docker 일관성 보장
  - `dependency-groups`로 `[dev]`, `[ml]`, `[bi]` 등 task별 의존성 분리
  - 적용 가능성: **High** — pyproject.toml만 정비하면 거의 drop-in
- **개인 비서 워크플로우**: PEP 723 + `uv run` 패턴이 [[karpathy-autoresearch]]식 단일 파일 실험 루프의 Python판 인프라
- **위키 자기 인용**: 향후 `/wiki-ingest` 슬래시 커맨드를 Python 스크립트로 구현한다면 PEP 723 + uv run 패턴이 답
- **버전 추적 가치**: v0.x 단계임에도 prod-ready로 광범위 채택. 1.0 이전이지만 사실상 안정. 향후 1.0 릴리스가 의미하는 변화 추적 가치
- **이름 표기 강제**: 항상 소문자 `uv`. 위키 본문에서도 일관 적용
