---
title: "Pandas vs Polars vs DuckDB — 정량 비교 매트릭스"
type: synthesis
category: data
tags: [comparison, pandas, polars, duckdb, dataframe, decision-matrix, 16회차]
sources:
  - "[[pandas-dev-pandas]]"
  - "[[pola-rs-polars]]"
  - "[[duckdb-duckdb]]"
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 10
---

# Pandas vs Polars vs DuckDB

> 같은 데이터 분석 작업을 풀 수 있는 세 도구의 **정량 비교**. 결론: **셋 다 사용**이 정답이며, 워크로드 단계별로 다른 도구가 우위.

## 1. 한눈 비교 매트릭스

| 항목 | [[pandas]] | [[polars]] | [[duckdb]] |
|------|------------|------------|------------|
| **첫 릴리스** | 2008 | 2020 | 2018 |
| **언어 본체** | Python (Cython 핫패스) | Rust | C++17 |
| **라이센스** | BSD-3-Clause | MIT | MIT |
| **Stars (★)** | 50k+ | 30k+ | 25k+ |
| **본질** | 라이브러리 | 쿼리 엔진 | 임베디드 OLAP DB |
| **API 스타일** | 메소드 + indexing | Expression DSL | SQL |
| **평가 모델** | Eager | Lazy + Eager + Streaming | SQL 본질적 lazy |
| **메모리 모델** | NumPy + CoW (PyArrow 점진) | Apache Arrow immutable | Vectorized columnar |
| **Import 시간** | 520ms | **70ms** | (인프로세스) |
| **병렬화** | 단일 스레드 (옵션 numba) | **Multi-threaded 기본** | Multi-threaded |
| **SIMD** | numexpr 경유 (옵션) | **AVX2 기본, AVX-512 nightly** | Vectorized |
| **Streaming** | chunksize iterator (제한적) | `engine='streaming'` | EXTERNAL TABLE |
| **Pushdown** | 없음 | **자동 (predicate/projection)** | **자동 (SQL 옵티마이저)** |
| **Query Plan** | 없음 | `explain()` | `EXPLAIN` |
| **Parquet 직접 SELECT** | `pd.read_parquet()` | `pl.scan_parquet()` | **`SELECT * FROM 'f.parquet'`** |
| **S3 통합** | s3fs 추가 | fsspec 통합 | `httpfs` extension |
| **Apache Arrow** | PyArrow 백엔드 (옵션) | **1급 (모든 컬럼이 Arrow)** | **1급 (zero-copy)** |
| **Window 함수** | `.rolling()`, `.expanding()` | `.rolling()`, `.over()` | **풍부한 SQL window** |
| **Group By** | `.groupby()` | `.group_by()` | `GROUP BY` |
| **Pivot** | `.pivot_table()` | `.pivot()` | `PIVOT` 절 |
| **Time Series** | **풍부 (resample, BusinessDay, tz)** | 기본 (asof, group_by_dynamic) | 기본 (date_trunc, INTERVAL) |
| **ML 통합** | **scikit-learn 1급** | `to_pandas()/to_numpy()` 변환 | SQL 피처 엔지니어링 |
| **시각화** | **Plotly/Matplotlib 1급** | Plotly 호환 (제한적) | DataFrame 변환 후 |
| **단일 노드 한계** | ~10M 행 | ~4.2B 행 (`bigidx`) | ~메모리 한계 |
| **분산 확장** | Modin/Dask/Ray | Polars Cloud (SaaS) | MotherDuck (SaaS) |
| **회사 지원** | NumFOCUS (비영리) | Polars Cloud Inc | DuckDB Foundation + Labs |
| **거버넌스** | BDFL + Core Team + PDEP | pola-rs 조직 | Foundation + Labs |

## 2. 성능 정량 비교 (PDS-H benchmark 기준)

PDS-H는 100GB TPC-H 데이터셋 기반 표준 분석 벤치마크. (출처: pola.rs/benchmarks.html)

| 쿼리 | pandas | polars (eager) | polars (lazy) | duckdb |
|------|--------|----------------|---------------|--------|
| Q1 (filter + agg) | ~120s | ~10s | **~3s** | ~4s |
| Q5 (5-table join) | OOM 위험 | ~25s | **~8s** | ~6s |
| Q19 (복잡 조건) | ~80s | ~12s | **~4s** | ~5s |

→ **lazy mode의 polars/duckdb는 pandas 대비 20-40배**, eager polars는 ~10배.

(주의: 실측은 데이터/하드웨어/쿼리에 따라 다름. 위는 일반 경향)

## 3. API 비교 — 같은 작업, 다른 표현

### 작업: "2024년 데이터에서 user_id별 revenue 합계, 상위 10명"

#### pandas

```python
import pandas as pd

df = pd.read_parquet("sales.parquet")
result = (
    df[df.date >= "2024-01-01"]
    .groupby("user_id")["revenue"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)
```

#### Polars (Lazy)

```python
import polars as pl

result = (
    pl.scan_parquet("sales.parquet")
    .filter(pl.col("date") >= "2024-01-01")
    .group_by("user_id")
    .agg(pl.col("revenue").sum())
    .sort("revenue", descending=True)
    .head(10)
    .collect()
)
```

#### DuckDB (SQL)

```python
import duckdb

result = duckdb.sql("""
    SELECT user_id, SUM(revenue) AS total
    FROM 'sales.parquet'
    WHERE date >= '2024-01-01'
    GROUP BY user_id
    ORDER BY total DESC
    LIMIT 10
""").df()
```

→ **셋 다 가독성 OK**. 차이는 (1) 옵티마이저 (2) 메모리 사용 (3) 학습 비용.

## 4. 의사결정 트리

```
Q1: SQL이 익숙하고 ad-hoc 분석이 주 목적인가?
  YES → DuckDB
  NO ↓
  
Q2: 데이터가 100MB 이하이고 ML/시각화 통합이 핵심인가?
  YES → pandas (단순함 우위)
  NO ↓
  
Q3: 데이터가 1GB+ 또는 latency 민감 (cold start)인가?
  YES → Polars (lazy + streaming)
  NO ↓
  
Q4: 운영 워크로드인가?
  YES → Polars (lazy 옵티마이저)
  NO → 기존 도구 유지 (pandas 컴팩트)
```

### 핵심 결정 요인

| 요인 | pandas | polars | duckdb |
|------|--------|--------|--------|
| **scikit-learn 의존** | ★★★ | ★★ (변환) | ★ (변환) |
| **Plotly/Matplotlib 1급** | ★★★ | ★★ | ★ |
| **메모리 200MB 이하** | ★★★ | ★★★ | ★★ |
| **데이터 200GB+** | ★ (OOM) | ★★★ | ★★★ |
| **SQL 친화 팀** | ★ | ★★ | ★★★ |
| **Query Plan 디버깅** | ★ (없음) | ★★★ | ★★★ |
| **Lambda/컨테이너 cold start** | ★ (520ms) | ★★★ (70ms) | ★★ |
| **Parquet 직접 쿼리** | ★★ | ★★ | ★★★ |
| **다언어 클러스터 (Wasm)** | ★ | ★★ | ★★★ |
| **분산 확장** | ★★ (Modin/Dask) | ★★ (Cloud) | ★★ (MotherDuck) |

## 5. "셋 다 사용" 시나리오 (권장)

### 데이터 사이언스 노트북

```python
import pandas as pd
import polars as pl
import duckdb

# 1) DuckDB: 빠른 SQL 탐색 + 큰 데이터셋 필터링
arrow_table = duckdb.sql("""
    SELECT user_id, date, revenue 
    FROM 's3://bucket/sales-2024.parquet' 
    WHERE date >= '2024-01-01'
""").arrow()

# 2) Polars: lazy 변환 + group_by/window/streaming
pl_df = pl.from_arrow(arrow_table)
features = (
    pl_df.lazy()
    .with_columns(pl.col("revenue").rolling_mean(7).over("user_id").alias("ma7"))
    .group_by("user_id")
    .agg([pl.col("revenue").sum(), pl.col("ma7").last()])
    .collect()
)

# 3) pandas: scikit-learn 입력 + Plotly 시각화
pd_df = features.to_pandas()
from sklearn.cluster import KMeans
clusters = KMeans(n_clusters=5).fit_predict(pd_df[["revenue", "ma7"]])
pd_df["cluster"] = clusters
pd_df.plot(...)  # Plotly/Matplotlib 호환
```

→ **각 도구의 강점만 사용**. PyArrow가 사이의 zero-copy 다리.

## 6. 마이그레이션 비용 추정 ([[c2spf-analytics|c2spf 게임 데이터 BI]])

기존 pandas 코드 → Polars/DuckDB 도입:

| 작업 | 추정 시간 |
|------|----------|
| Polars Expression DSL 학습 (분석가 1인) | 2-3일 |
| 기존 핵심 함수 5개 Polars 변환 | 1주 |
| pytest로 결과 동등성 검증 | 3일 |
| 운영 배포 + 모니터링 | 1주 |
| **합계** | **~3-4주** (1인 풀타임) |

ROI:
- Cold start 단축: API latency p50 -100ms (pandas import 제거)
- 메모리: 200GB+ 일일 로그 처리 가능
- BQ 비용: ad-hoc DuckDB로 옮기면 슬롯 -30% 추정

## 7. 주의사항 / 함정

### Polars
- API가 pandas와 다름 → "직관적이지만 다름"의 학습 비용
- Streaming engine이 일부 연산(특정 group_by, window) 미지원 — query별 검증
- Plotly/Geopandas 일부 함수 pandas-only → 변환 레이어 필요

### DuckDB
- 동시 쓰기 1개만 — 멀티프로세스 쓰기 시 lock 충돌
- in-process이므로 Python heap 종속 — 100GB+ 데이터셋은 streaming/외부 디스크
- CHANGELOG.md 부재 — GitHub Releases + duckdb.org/news로 분산

### Pandas
- 단일 스레드 — 큰 데이터셋에서 느림. Modin/Dask로 우회
- import 520ms — Lambda/컨테이너 cold start에 결정적
- SettingWithCopyWarning은 CoW로 해결됐지만 chained assignment 패턴 변경 필요

## 8. 결론

**경쟁이 아닌 보완**. 셋 다 [[apache-arrow]] 위에 빌드되어 zero-copy 교환 → **워크플로우 단계별로 최적 도구**:

- **DuckDB**: 데이터 진입점 (SQL, 파일 직접 SELECT)
- **Polars**: 메인 변환 (lazy DSL, streaming)
- **Pandas**: ML 출력 + 시각화 (생태계 호환)

석근님의 [[c2spf-analytics|c2spf 게임 데이터 BI]] BI 워크로드 권장: **세 도구 모두 학습 + 단계별 사용**. 학습 우선순위:

1. DuckDB SQL — 즉시 도입 가능, 학습 곡선 낮음
2. Polars Expression DSL — 2-3일 투자로 productivity 큰 향상
3. pandas — 이미 사용, 점차 ML 출력에만 한정

## 출처

- [[pandas-dev-pandas]] — pandas 16회차 직전 (11회차) 수집
- [[pola-rs-polars]] — 16회차 수집
- [[duckdb-duckdb]] — 16회차 수집
- [[dataframe-ecosystem-evolution]] — 16회차 종합 분석

## 후속 작업

- 실제 PDS-H 벤치마크 재현 (회사 BI 워크로드 대표 쿼리 5-10개) — 정량 검증
- Modin/Dask/Ray 비교 매트릭스 추가 (분산 확장 관점)
- Iceberg/Delta + DuckDB/Polars 통합 패턴 정리
