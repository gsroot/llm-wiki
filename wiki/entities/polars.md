---
title: "Polars"
type: entity
entity_type: tool
tags: [polars, dataframe, rust, lazy-evaluation, query-optimization, apache-arrow, streaming, simd, multi-threaded, pyo3, immutable, pola-rs]
related:
  - "[[pandas]]"
  - "[[duckdb]]"
  - "[[pyarrow]]"
  - "[[apache-arrow]]"
  - "[[copy-on-write]]"
  - "[[dataframe]]"
  - "[[lazy-evaluation]]"
  - "[[c2spf-analytics]]"
  - "[[pola-rs-polars]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 14
inbound_count: 80
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 31
---

# Polars

## 개요

Polars는 Rust로 작성된 **분석 쿼리 엔진**(자칭 "Query Engine")이자 그 위의 다언어 DataFrame 라이브러리다. 2020년 Ritchie Vink이 시작했고, 2026년 현재 v1.x stable. **pandas의 직접 후계자가 아니라 SQL 옵티마이저 사상을 DataFrame DSL로 옮긴** 새 패러다임.

라이센스: MIT. 거버넌스: pola-rs 조직 + Polars Cloud 상용 (별도 회사). PyPI star: ★30k+, 빠르게 산업 채택 중.

## 주요 특징

### 듀얼 실행 모델 + Streaming = 3중 모드

| 모드 | 호출 | 사용 시점 |
|------|------|----------|
| **Eager** | `pl.read_csv()` → DataFrame 즉시 | 탐색/디버깅 |
| **Lazy** | `pl.scan_csv()` → LazyFrame → `.collect()` | 운영 (옵티마이저 적용) |
| **Streaming** | `.collect(engine='streaming')` | RAM 초과 데이터 |

→ **같은 API, 실행 시점만 다름**. Eager는 lazy를 즉시 collect하는 wrapper로 구현됨.

### Expression DSL + 4 컨텍스트

Polars만의 도메인 특화 언어:

```python
import polars as pl
df.select(pl.col("price") * pl.col("qty"))         # select context
df.with_columns(...)                                # with_columns context
df.filter(pl.col("date") >= "2024-01-01")          # filter context
df.group_by("category").agg(pl.col("price").sum()) # group_by context
```

같은 expression이 **컨텍스트에 따라 다른 결과** — SQL의 SELECT/WHERE/GROUP BY 의미론을 메소드 체이닝으로 옮김.

### Lazy 옵티마이저

`scan_csv()` → `LazyFrame` → `collect()` 호출 시:
- **Predicate pushdown**: filter를 IO 단계로 내림
- **Projection pushdown**: select를 IO 단계로 내림
- **CSE** (Common Subexpression Elimination)
- **Slice pushdown**: head/tail 같은 limit를 내림
- `explain()`으로 실제 query plan 확인 가능

### Apache Arrow 메모리 모델 = immutable-by-default

[[apache-arrow]] columnar format을 in-memory 표현으로 직접 사용 → **모든 버퍼는 read-only**. [[copy-on-write]]가 아니라 **immutable-by-default**:
- 모든 연산이 새 컬럼/DataFrame 생성
- in-place 업데이트 없음 (의도적)
- zero-copy: pandas/DuckDB/PyArrow 사이 무손실 교환

→ pandas의 SettingWithCopyWarning 같은 모호성 자체가 발생하지 않음.

### 성능 (README 자체 인용)

| 메트릭 | Polars | NumPy | Pandas |
|--------|--------|-------|--------|
| Import time | **70ms** | 104ms | 520ms |
| PDS-H bench | (공개) | N/A | (느림) |

PDS-H 벤치마크 결과를 pola.rs/benchmarks.html에 공개 — [[ruff]]/[[uv]]의 BENCHMARKS.md 패턴과 동일.

### 다언어 단일 코어

Rust crate `polars` → 5개 프론트엔드:
- Python (`pip install polars`, PyO3 바인딩)
- Rust (Cargo crate)
- Node.js (`nodejs-polars`)
- R (r-polars)
- SQL 프론트엔드 (DuckDB-style)

→ **단일 코어 + 다언어 바인딩** = [[uv]]/[[astral]]의 통합 패턴.

### 빌드 변형

5단계 빌드 모드 (`make build` ~ `build-dist-release`) + `bigidx` 플래그(4.2B 행 초과) + `polars[rtcompat]`(AVX 없는 CPU). 컴파일 타임-성능 트레이드오프 명시화.

## 라이센스 / 의존성

- **MIT**
- 본체: Rust crate `polars`
- Python: PyO3 바인딩, **zero required dependencies** (NumPy도 없음)
- 옵션 그룹: `polars[all]`, `polars[pandas]`, `polars[pyarrow]`, `polars[numpy]`, `polars[fsspec]`, `polars[deltalake]`, `polars[iceberg]`, `polars[gpu]`

## 관련 개념

- [[apache-arrow]]: in-memory 표현 표준. Polars의 모든 컬럼은 Arrow 버퍼
- [[copy-on-write]]: pandas의 메모리 모델 vs Polars의 immutable-by-default — 정반대 접근
- [[lazy-evaluation]]: Polars의 핵심 패턴. SQL 옵티마이저 사상 적용
- [[dataframe]]: Polars의 핵심 자료구조
- [[ml-ai]]: scikit-learn은 NumPy/pandas만 지원 → Polars는 `to_pandas()`/`to_numpy()` 변환 필요
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 회사 BI BigQuery → DataFrame 패턴에서 pandas 대체 후보

## 관련 엔티티

- [[pandas]]: 가장 직접적인 비교. 임포트 7배·연산 10-100배·메모리 모델 정반대
- [[duckdb]]: SQL 진영의 같은 정체성("쿼리 엔진"). DuckDB=SQL, Polars=DataFrame DSL. Arrow zero-copy로 상호 보완
- [[pyarrow]]: Polars의 메모리 표현 표준. PyArrow Table ↔ Polars DataFrame zero-copy
- [[scikit-learn]]: ML 입력으로는 `df.to_numpy()` 변환 필요. 직접 호환은 미흡
- [[fastapi]]: API 응답 DataFrame을 Polars로 처리 후 dict/JSON 직렬화 패턴 가능
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: BI 워크로드 마이그레이션 후보 (잠재 채택자)

## 의사결정 컨텍스트 (raw 인용)

> "Rust로 작성된 분석 쿼리 엔진. Lazy + Eager + Streaming 3중 실행 모델과 Apache Arrow 컬럼 포맷 in-memory로 pandas 대비 임포트 7배·연산 10~100배 가속 — DataFrame 추상을 '표현식 + 컨텍스트' DSL로 재정의."
> — [[pola-rs-polars]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] DataFrame 영역에서 [[pandas]] 대안. [[c2spf-analytics]] 대규모 분석 시 마이그레이션 후보 + [[matechat|MateChat 사이드 프로젝트]] 채팅 분석 모듈 데이터 처리 후보 ([[pandas-vs-polars-vs-duckdb]] 결정 매트릭스 참조). **Lazy + Eager + Streaming 3중 모델**·**Apache Arrow immutable**은 [[copy-on-write]] CoW와 정반대 메모리 모델 — [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 메모리 모델 진화 사례. [[apache-arrow]]·[[duckdb]]와 함께 컬럼 진영 표준.

## 출처

- [[pola-rs-polars]] — pola-rs/polars GitHub 저장소 (README + CONTRIBUTING + 3개 concept 문서 통합 수집)

## 논쟁/모순

> [!warning] 논쟁/모순
> - **Pandas 호환 API 부재**: 의도적 결정. pandas 사용자에게는 학습 비용 — DSL/index 모델 다름. Modin/cuDF가 pandas API 호환을 목표로 하는 것과 정반대 전략
> - **Streaming engine 성숙도**: README는 stable처럼 보이지만 v1.x 시점 일부 연산(특정 group_by, window) streaming 미지원. 운영 도입 시 query별 검증 필수
> - **Arrow lock-in**: [[apache-arrow]] 위에 강하게 묶임 → Arrow 명세 변경 시 영향. 반대로 다른 Arrow 도구(DuckDB/pandas-pyarrow)와 무손실 교환은 강점
> - **Cloud SaaS 전환 위험**: Polars Cloud 상용 모델. [[redis]] 2024 라이센스 변경처럼 향후 OSS 라이센스 변경 가능성 (현재 MIT 유지)


## 메모

- **회사 BI 마이그레이션 가설**: [[c2spf-analytics]] FastAPI + BigQuery 환경에서 pandas → polars 전환 효과:
  - Cold start: API 컨테이너 부팅 ~500ms 단축 (numpy 의존 제거)
  - Memory: 200GB+ 일일 로그 streaming 처리 가능
  - Arrow 통합: BigQuery storage API + Polars zero-copy
  - **Risk**: Plotly/Geopandas 일부 함수 pandas-only — 변환 레이어 필요
- **DuckDB와 함께**: Polars가 DataFrame DSL, DuckDB가 SQL — **둘 다 사용**이 현실적 선택. 같은 Arrow 위에서 zero-copy 교환
- **bigidx vs 분산**: 4.2B 행 = 단일 노드 한계. 그 너머는 Spark/Dask로 가야 함. Polars-distributed는 Polars Cloud의 SaaS 영역
- **이름 표기**: "Polars" (PascalCase, 회사/제품), "polars" (소문자, Python 패키지 + Rust crate)
- **Ritchie Vink**: 창립자, 트위터 활발. AI/ML 스택과 데이터 분석 스택의 다리 역할
- **후속 후보**: `concepts/lazy-evaluation.md` 신규 작성 (Polars + DuckDB + Spark 공통 패턴)
