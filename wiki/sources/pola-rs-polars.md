---
title: pola-rs/polars (Polars 저장소)
type: source
source_type: article
source_url: https://github.com/pola-rs/polars
raw_path: raw/articles/pola-rs-polars/
author: pola-rs (Ritchie Vink + 컨트리뷰터)
date_published: 2020-08-01
date_ingested: 2026-04-28
tags:
- polars
- dataframe
- rust
- lazy-evaluation
- query-optimization
- apache-arrow
- streaming
- simd
- multi-threaded
- pyo3
related:
- '[[polars]]'
- '[[pandas]]'
- '[[duckdb]]'
- '[[pyarrow]]'
- '[[copy-on-write]]'
- '[[dataframe]]'
- '[[lazy-evaluation]]'
confidence: high
inbound_count: 27
aliases:
- Pola Rs Polars
- pola rs polars
- pola-rs/polars (Polars 저장소)
cited_by:
  - "[[apache-arrow]]"
  - "[[c2spf-analytics]]"
  - "[[copy-on-write]]"
  - "[[dataframe-ecosystem-evolution]]"
  - "[[lakehouse]]"
  - "[[lazy-evaluation]]"
  - "[[oss-saas-dual]]"
  - "[[pandas-vs-polars-vs-duckdb]]"
  - "[[polars]]"
  - "[[predicate-pushdown]]"
  - "[[query-optimization]]"
  - "[[streaming]]"
  - "[[zero-copy]]"
cited_by_count: 13
---

# pola-rs/polars (Polars 저장소)

## 한줄 요약

> Rust로 작성된 분석 쿼리 엔진. **Lazy + Eager + Streaming 3중 실행 모델**과 **Apache Arrow 컬럼 포맷 in-memory**로 pandas 대비 임포트 7배·연산 10~100배 가속 — DataFrame 추상을 "표현식 + 컨텍스트" DSL로 재정의했다.

## 핵심 내용

### 정체성 (README 첫 줄)

*"Polars: Extremely fast Query Engine for DataFrames, written in Rust"*. README는 처음부터 "라이브러리"가 아닌 **쿼리 엔진**으로 자기를 정의 — pandas와의 결정적 차이.

### 7대 핵심 특징

1. **Lazy | Eager 듀얼 모드** — 같은 API, 실행 시점만 다름 (Eager는 lazy를 즉시 collect하는 wrapper)
2. **Streaming** — `collect(engine='streaming')` 하나로 RAM 초과 데이터셋 처리. 250GB on a laptop을 README가 직접 약속
3. **Query optimization** — predicate pushdown, projection pushdown, common subexpression elimination
4. **Multi-threaded** — 모든 작업 기본 병렬 (Rayon)
5. **SIMD** — AVX2 기본, AVX-512는 nightly. 구형 CPU용 `LTS_CPU=1` 빌드 플래그 + `polars[rtcompat]` PyPI 패키지
6. **Powerful expression API** — Polars만의 DSL: `pl.col("weight") / pl.col("height").pow(2)`
7. **다언어 프론트엔드** — Python, Rust, Node.js, R, SQL (단일 코어 + 5개 바인딩)

### 4가지 컨텍스트 (Expression이 평가되는 환경)

`select`, `with_columns`, `filter`, `group_by` — 동일 표현식이 컨텍스트에 따라 다른 결과 산출. 이는 SQL의 SELECT/WHERE/GROUP BY 의미론을 DataFrame DSL로 옮긴 것.

### Lazy API의 핵심 약속

`scan_csv` → `LazyFrame` → `collect`만 호출하면, 옵티마이저가:
- **Predicate pushdown**: filter를 CSV 읽기 단계로 내림 (필요 행만 디스크에서 읽음)
- **Projection pushdown**: select를 CSV 읽기 단계로 내림 (필요 컬럼만 파싱)

`explain`으로 query plan을 시각화 가능 — 일반 사용자가 cost-based optimizer를 직접 볼 수 있는 드문 인터페이스.

### 성능 메트릭 (README 자체 인용)

- **임포트 시간**: polars 70ms vs numpy 104ms vs pandas 520ms → CLI/스크립트 cold start 결정적 차이
- **PDS-H 벤치마크**: pola.rs/benchmarks.html 공개, 정직성 시그널
- **Zero required dependencies**: 단일 wheel `pip install polars`만으로 동작

### 기술 스택

- 본체: **Rust** (Cargo crate `polars`)
- Python 바인딩: **PyO3** (`py-polars` crate → `polars` Python 패키지로 빌드)
- In-memory: **[[apache-arrow]] Columnar Format** — README가 명시적 인용 (62줄)
- 빌드: `maturin` (Rust → Python wheel 컴파일러, [[uv]]와 같은 PyO3 생태계)

### 관리형 / 분산 Polars (cloud.pola.rs)

README가 직접 언급 — **Polars Cloud**. 오픈소스 + 매니지드/분산 클러스터 상용 모델. [[astral]]의 OSS+VC 패턴 동일 (Polars 사가 별도 법인).

### 빌드 변형 (`make build-*`)

`build` (debug 빠른 컴파일) → `build-release` → `build-nodebug-release` → `build-debug-release` → `build-dist-release` (5단계 점진). 사용자 전용 컴파일 시 트레이드오프 명시화.

### Big idx / Legacy 빌드

- `bigidx` 플래그: 2^32 (~4.2B) 행 초과 데이터용. PyPI는 `polars[rt64]`
- `polars[rtcompat]`: AVX 없는 CPU용 (2011년 이전 또는 Rosetta x86-64). 호환성에 진심

## 주요 인사이트

### 1. Polars는 라이브러리가 아니라 "쿼리 엔진"

이 정체성 차이가 모든 결과에 영향: query plan, optimizer, lazy evaluation은 데이터베이스의 어휘. pandas는 "메모리 위 DataFrame 조작 함수 모음", Polars는 "DataFrame 위 SQL 같은 옵티마이저". → [[duckdb]]와 같은 군에 가까움.

### 2. CoW가 아니라 immutable-by-default

[[copy-on-write]]가 [[pandas]] 메모리 모델인 반면, Polars는 [[apache-arrow]] read-only 버퍼 위에서 작동 → **모든 연산이 새 컬럼/DataFrame 생성**. CoW의 "변경 시점 복사" 트레이드오프가 아예 발생하지 않는다. 단점은 in-place 업데이트 부재 (의도된 디자인).

### 3. 다언어 단일 코어 패턴

Polars의 5개 프론트엔드(Py/Rust/Node/R/SQL)는 모두 동일 Rust crate를 호출 — [[uv]]가 Python tools 7개를 단일 Rust crate로 통합한 패턴과 동일. **언어 횡단 통합 = Rust 재작성 패턴**의 또 다른 사례.

### 4. PDS-H 벤치마크 공개 = ruff/uv의 BENCHMARKS.md와 같은 정직성 시그널

벤치마크 결과를 외부 호스팅 + 재현 가능한 형태로 공개 → [[astral]]의 패턴과 일치. "측정되지 않는 것은 신뢰되지 않는다" 문화.

### 5. README가 임포트 시간을 명시 (70ms vs 520ms)

Cold start = 1개 명령 = 70ms로 7.4배. CLI 도구 / Lambda / 컨테이너 부팅에서 결정적 영향. pandas는 NumPy 임포트만으로 100ms+. Polars는 numpy도 의존 안 함.

## 관련 엔티티/개념

- [[polars]]: 본 소스의 메인 엔티티
- [[pandas]]: 가장 직접적인 비교 대상 — 임포트 7배 · 연산 10-100배 · 메모리 모델 (CoW vs immutable)
- [[duckdb]]: "쿼리 엔진" 정체성 공유. Polars=DataFrame DSL, DuckDB=SQL. 상호 보완 관계
- [[pyarrow]]: Polars의 in-memory 표현 (Apache Arrow Columnar Format)
- [[copy-on-write]]: pandas의 메모리 모델 vs Polars의 immutable-by-default 대조
- [[lazy-evaluation]]: Polars의 핵심 패턴 — predicate/projection pushdown
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 회사 BI에서 pandas 워크로드 후보로 평가 가능

## 인용할 만한 구절

> "Polars is an analytical query engine written for DataFrames."
> — README.md (49줄)

> "If you have data that does not fit into memory, Polars' query engine is able to process your query (or parts of your query) in a streaming fashion. This drastically reduces memory requirements, so you might be able to process your 250GB dataset on your laptop."
> — README.md (84-87줄)

> "polars: 70ms / numpy: 104ms / pandas: 520ms"
> — README.md (78-80줄, import time)

## 메모

- **회사 BI 마이그레이션 가설**: [[c2spf-analytics|c2spf 게임 데이터 BI]]의 BigQuery → DataFrame 패턴에서 pandas → polars 전환은 (1) cold start 7배 빨라짐 (2) 200GB+ 일일 로그 streaming 처리 가능 (3) Arrow 통합으로 [[pyarrow]] 직접 호환. **Risk**: API 학습곡선 (pandas와 다른 DSL), pandas-only 통합 라이브러리(plotly, geopandas 일부) 호환성 검증 필요.
- **Lazy API 학습 우선순위**: 종합 페이지에서 lazy_api.md를 직접 인용 — predicate/projection pushdown은 Pandas 사용자가 가장 먼저 만나는 인지 부조화 지점
- **Polars Cloud 추적 가치**: 오픈소스 → SaaS 전환 패턴. 5년 후 라이센스 유지 여부 추적
- **bigidx 플래그**: 4.2B 행 초과 시점 = pandas의 64비트 한계와 동일. 두 라이브러리가 같은 물리적 메모리 한계를 만남 → "단일 노드 한계" 문제는 분산 시스템(Spark/Dask)으로만 해결됨
- **Streaming engine = experimental**: README는 stable로 보이지만 v1.x 시점 streaming은 일부 연산 미지원. 운영 도입 시 query별 검증 필수
