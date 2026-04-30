---
title: "Python 패키징 (Python Packaging)"
aliases: [Python Packaging, 파이썬 패키징]
type: concept
category: dev-tools
tags: [python-packaging, pip, poetry, uv, pyproject-toml, lockfile, pep-517, pep-518, pep-621, pep-723, pep-735, virtualenv, pyenv, pipx, pypa, dependency-resolution, supply-chain]
related:
  - "[[uv]]"
  - "[[astral]]"
  - "[[backend-python-fastapi]]"
source_count: 1
observed_source_refs: 9
inbound_count: 32
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 19
---

# Python 패키징 (Python Packaging)

## 정의

**Python 패키징**은 Python 코드를 배포 가능한 형태(sdist/wheel)로 빌드하고, 의존성을 해결·잠그고, 환경에 설치하는 일련의 표준·도구·관행을 가리킨다. 이 영역은 **PEP(Python Enhancement Proposal) 표준**과 **PyPA(Python Packaging Authority) 도구**, 그리고 두 진영을 추적·확장하는 **서드파티 도구들**(Poetry, PDM, [[uv]] 등)이 함께 형성한다.

핵심 산출물 4가지:
1. **소스 배포(sdist)**: `*.tar.gz` — 빌드 전 소스 + 메타데이터
2. **휠(wheel)**: `*.whl` — 빌드된 zip, 플랫폼 태그 포함
3. **lockfile**: 의존성 트리 잠금 (`requirements.txt` / `poetry.lock` / `Pipfile.lock` / **`uv.lock`**)
4. **가상환경(venv)**: 격리된 Python 런타임 + 패키지 트리

## 왜 중요한가

### 1) Python의 fragmentation 비용

Python 패키징은 역사적으로 **도구 분산**으로 악명 높았다 (XKCD #1987 "Python Environment" 만화 참고). 한 프로젝트에서 마주칠 수 있는 도구:

| 영역 | 분산된 도구 |
|------|------------|
| 가상환경 | `venv`, `virtualenv`, `conda env` |
| Python 버전 | `pyenv`, `asdf`, `conda`, OS 패키지 매니저 |
| 의존성 설치 | `pip`, `pip-tools`, `poetry`, `pdm`, `pipenv`, `conda` |
| 도구 설치 | `pipx`, `pip install --user` |
| 빌드/배포 | `setuptools`, `flit`, `hatchling`, `pdm-backend`, `poetry-core`, `twine` |
| 의존성 잠금 | `pip freeze`, `pip-compile`, `poetry lock`, `pipenv lock` |

이 분산은 학습 비용, 호환성 비용, 결정 피로(decision fatigue)를 만든다. **uv는 이 fragmentation이 우연이었음을 사후 검증**한다 — 단일 바이너리로 7개 도구를 대체함으로써.

### 2) 데이터 분석/BI 워크플로우의 재현성 문제

[[seokgeun-kim|석근 (이 위키 owner)]]의 게임 데이터 BI 환경에서 마주치는 전형적 문제:
- "내 macOS에서는 되는데 Linux Docker에서 깨진다" → lockfile platform-specific
- "CI 시간의 60%가 의존성 설치" → cold cache pip의 대표 증상
- "Python 3.10/3.11/3.12 어느 버전에서 돌리지?" → pyenv + pip 조합의 마찰
- "ML 의존성과 BI 의존성이 충돌한다" → 단일 venv에 모든 걸 박는 안티패턴

[[uv]] 같은 통합 도구체인은 이 문제들을 **데이터 모델 단일화**로 해결한다.

### 3) 공급망 보안

Python 패키지의 공급망 공격은 실제로 발생한다:
- typosquatting (예: `urlib3` vs `urllib3`)
- malicious post-install scripts
- compromised maintainer accounts

uv의 `tool.uv.sources` + universal lockfile + `--exclude-newer` (시간 잠금) 같은 기능들은 supply chain 위협 모델에 직접 대응한다.

## 핵심 내용

### A. 표준 — PEP 진화 타임라인

| PEP | 이름 | 핵심 내용 |
|-----|------|----------|
| **PEP 440** | Version Identification | 버전 식별자 표준 (1.0.0, 1.0.0a1, 1.0.0+local) |
| **PEP 508** | Dependency specification | `requests>=2,<3; python_version >= '3.8' and sys_platform == 'linux'` 같은 markers |
| **PEP 517** | Build-system independence | `setup.py` 의존성 제거, `[build-system]` 표준화 |
| **PEP 518** | `pyproject.toml` | 빌드 설정 통합 파일 표준 |
| **PEP 621** | Project metadata | `[project]` 테이블에 메타데이터 (name, version, dependencies, ...) |
| **PEP 660** | Editable installs | wheel 기반 editable install (pip install -e의 표준화) |
| **PEP 723** | Inline script metadata | 단일 파일 스크립트의 인라인 의존성 (`# /// script ... # ///`) |
| **PEP 735** | Dependency Groups | `[dependency-groups]` 테이블 — dev/test/lint 의존성 분리 표준 |

### B. 의존성 해석(Resolution) — 핵심 알고리즘

의존성 해석은 SAT 문제(NP-complete)의 한 형태:
- 입력: 직접 의존성 + 각 패키지의 metadata
- 출력: 모든 제약을 만족하는 버전 조합 (또는 "no solution")

주요 알고리즘:
- **Backtracking** (pip ≥ 20.3) — 시행착오, 충돌 시 되돌아감
- **PubGrub** ([[uv]], poetry, Cargo) — 학습 기반 가지치기, 충돌 설명 친화적
- **Dependabot 스타일** (greedy + heuristics) — 빠르지만 최적해 보장 안 함

### C. Lockfile 전략 비교

| 도구 | Lockfile | Platform-independent? | Multi-version per package? |
|------|---------|----------------------|---------------------------|
| pip-tools | `requirements.txt` | ❌ (생성 플랫폼 의존) | ❌ |
| Pipenv | `Pipfile.lock` | 부분적 | ❌ |
| Poetry | `poetry.lock` | ✅ | 제한적 |
| PDM | `pdm.lock` | ✅ | 제한적 |
| **[[uv]]** | **`uv.lock`** | **✅ universal** | **✅ markers별 multiple version** |

**Universal lockfile**의 의미: macOS 개발 / Linux CI / Windows 콘솔 / Docker x86_64 / aarch64 모두에서 **동일 lockfile**이 작동. 마커별로 패키지를 여러 버전으로 잠근다.

### D. Wheel 메타데이터 보안

Wheel은 zip이고, 내부에 `RECORD` 파일이 모든 파일 경로 + 해시를 담는다. 잘못된 RECORD는 보안 문제로 직결된다:
- **GHSA-pjjw-68hj-v9mw** (uv 0.11.6, 2026-04): "wheels with malformed RECORD entries could delete arbitrary files on uninstall"
- 대응: uv는 install 시 RECORD healing 로직 추가 + uninstall 시 venv 외부 파일 삭제 방지

### E. 도구별 포지셔닝 매트릭스

| 측면 | pip | poetry | pdm | rye | **uv** |
|------|-----|--------|-----|-----|--------|
| 작성 언어 | Python | Python | Python | Rust | **Rust** |
| 가상환경 관리 | ❌ (venv 별도) | ✅ | ✅ | ✅ | **✅** |
| Python 버전 관리 | ❌ (pyenv 별도) | ❌ | ❌ | ✅ | **✅** |
| 도구 설치 (uvx) | ❌ (pipx 별도) | ❌ | ❌ | ❌ | **✅** |
| Universal lockfile | ❌ | 부분 | 부분 | ❌ | **✅** |
| 단일 바이너리 | ❌ | ❌ | ❌ | ✅ | **✅** |
| 빌드 시스템 통합 | ❌ | ✅ | ✅ | ❌ | **✅** |
| 워크스페이스 | ❌ | ❌ | ❌ | ✅ | **✅** |

uv는 본질적으로 **rye + poetry + pip-tools + pyenv + pipx의 통합**이다.

## 실전 적용

### 시나리오 1: FastAPI 백엔드 ([[c2spf-analytics|c2spf 게임 데이터 BI]] 같은 BI)

**기존**: `requirements.txt` + `requirements-dev.txt` + Dockerfile + venv 수동 관리
**uv 전환**:
```toml
# pyproject.toml
[project]
name = "c2spf-analytics"
requires-python = ">=3.12"
dependencies = ["fastapi", "sqlalchemy", "google-cloud-bigquery"]

[dependency-groups]
dev = ["pytest", "pytest-asyncio", "ruff"]
ml = ["scikit-learn", "pandas"]

[tool.uv.sources]
c2spf-internal = { url = "https://pypi.internal.com2us-platform.com/simple" }
```
- `uv sync --group dev` → 개발환경
- `uv sync --no-group dev --group ml` → CI ML 빌드
- `uv lock` → universal `uv.lock` 생성
- Docker: `FROM python:3.12 → COPY uv.lock pyproject.toml → uv sync --frozen`

### 시나리오 2: 단일 파일 데이터 분석 스크립트 (PEP 723)

```python
# /// script
# requires-python = ">=3.12"
# dependencies = ["pandas", "matplotlib", "seaborn"]
# ///
import pandas as pd
df = pd.read_csv("metrics.csv")
df.plot()
```
실행: `uv run analyze.py` — venv 자동 생성, 의존성 자동 설치, 격리 실행. 옷에는 venv가 남지 않는다 (캐시만).

### 시나리오 3: 일회성 도구 실행 (uvx)

```bash
uvx ruff check .          # ruff 설치 없이 임시 실행
uvx --from "ipython[all]" ipython
uvx pycowsay 'hello'
```

### 시나리오 4: 모노레포 워크스페이스

```toml
# 루트 pyproject.toml
[tool.uv.workspace]
members = ["packages/*"]
```
각 멤버 디렉토리도 자체 `pyproject.toml`을 갖고, 멤버 간 의존성은 path 또는 git source로.

## 관련 개념

- [[uv]]: 본 개념의 가장 통합된 현대 구현
- [[astral]]: uv 운영 주체. ruff(Python lint/format) + uv(packaging) + ty(type) 3제품 모두 본 개념과 인접
- [[backend-python-fastapi]]: FastAPI 백엔드의 의존성 관리 영역
- [[harness]]: PEP 723 + uv run = 단일 파일 minimal harness 인프라
- [[autonomous-research-loop]]: PEP 723으로 자급자족 실험 스크립트 가능 — [[karpathy]]식 단일 파일 실험 루프의 Python 인프라
- [[token-economy]]: 의존성 설치 시간 자체가 LLM 에이전트 cycle time의 한 축 — 빠른 패키지 매니저는 에이전트 워크플로우 효율을 직접 개선

## 출처

- [[astral-sh-uv]] — uv 저장소를 통한 Python 패키징 표준 통합 사례. PEP 517/518/621/723/735 모두 구현. README "A single tool to replace pip, pip-tools, pipx, poetry, pyenv, twine, virtualenv"

## 열린 질문

1. **PEP 표준이 통합 도구를 따라잡는가?** uv가 빠르게 채택한 PEP 723, dependency-groups, `tool.uv.sources` 같은 패턴 중 — 어디까지가 표준화되고, 어디부터가 fork인가? 표준 진화 속도 vs 도구 진화 속도의 거리.
2. **"Python의 미래는 Rust인가?"** Astral 3제품 (ruff/uv/ty) + Pydantic v2의 Rust 코어 + numpy/pandas의 C 구현이 모두 동일한 문제 해법으로 수렴 중. Python core 자체가 Rust로 이주하는 시나리오는 어디까지 현실적인가? CPython의 GIL 제거 + nogil 빌드 + `freethreaded` 변종 흐름과 어떻게 상호작용하는가?
3. **`conda`와의 관계**: uv는 PyPI 중심. conda 생태계 (특히 ML/과학 계산)는 별개로 남아있다. 이 분리가 합리적인가, 아니면 향후 통합 가능한가?
4. **Lockfile 표준화**: 각 도구의 lockfile 포맷이 모두 다르다. PEP 751 같은 표준 lockfile 시도가 있지만 채택은 미미. universal lockfile 표준이 가능한가, 아니면 도구별 fork가 영구적인가?
5. **회사 BI 적용 ROI**: pip → uv 전환 시 [[c2spf-analytics|c2spf 게임 데이터 BI]] CI 시간/lockfile 일관성/dev 만족도의 실제 측정. 이 위키의 후속 실험 후보.
6. **위키 자기 적용**: 향후 위키 자동화 스크립트는 PEP 723 + uv run으로 작성하는 것이 답인가? `/wiki-ingest`, `/wiki-lint` 슬래시 커맨드의 Python 구현은 PEP 723 헤더만 박으면 의존성 명시도 함께 끝난다.
