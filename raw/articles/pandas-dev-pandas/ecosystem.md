# Ecosystem

This is a community-maintained list of projects that build on pandas to provide tools in the PyData space.
The pandas core development team does not necessarily endorse any particular project on this list.

## Extensions

pandas allows third-party packages to enhance its functionality through:
- Extension Accessors (custom .ak / .vgplot / .pint / .gppd / .sc namespaces on Series/DataFrame)
- Extension Types (custom dtypes for awkward arrays, db-dtypes, genomics, units, text, etc.)
- Plotting backends (Altair, Bokeh, hvplot, Plotly via `pd.set_option("plotting.backend", "<backend>")`)

### Accessor 디렉터리 (예시)

| Library | Accessor | Classes |
| ------- | -------- | ------- |
| akimbo | `ak` | Series |
| **bigframes** | `bigquery` | DataFrame |
| pdvega | `vgplot` | Series, DataFrame |
| pandas-genomics | `genomics` | Series, DataFrame |
| pint-pandas | `pint` | Series, DataFrame |
| physipandas | `physipy` | Series, DataFrame |
| composeml | `slice` | DataFrame |
| gurobipy-pandas | `gppd` | Series, DataFrame |
| staircase | `sc` | Series, DataFrame |
| woodwork | `slice` | Series, DataFrame |

### 데이터 타입 확장

- akimbo (Awkward Arrays in Series/DataFrame)
- **db-dtypes** (DATE, TIME, JSON from BigQuery — pandas-gbq 의존성)
- pandas-genomics
- physipandas (물리량 + 단위)
- pint-pandas (numeric + unit)
- Text Extensions for Pandas (NLP)

### 플로팅 백엔드

Altair · Bokeh · hvplot · Plotly

## 도메인 특화 확장

- **Geopandas** — 지리정보 + 지오메트리 연산
- gurobipy-pandas — 수리 최적화 (Gurobi)
- Hail Query — 유전체 시퀀싱 데이터 (out-of-core, distributed)
- staircase — 수학적 계단함수 모델링 (실수/datetime/timedelta)
- xarray — N차원 라벨드 배열 (pandas의 N차원 형제)

## 데이터 IO 확장 (BI 직무 핵심)

- ArcticDB — 객체 스토리지 기반 DataFrame DB
- BCPandas — MS SQL Server 고성능 쓰기 (df.to_sql 대체)
- Deltalake — Delta Lake 네이티브 접근 (Spark/JVM 불필요)
- fredapi — FRED 경제 데이터 API
- **Hugging Face** — `pd.read_parquet("hf://datasets/...")` / `df.to_parquet("hf://datasets/me/foo/train.parquet")`
- NTV-pandas — JSON 변환기 (Table Schema, NTV 포맷)
- pandas-datareader — 원격 데이터 (Google Finance, Tiingo, Quandl, FRED, World Bank, OECD, MOEX 등)
- **pandas-gbq** — BigQuery 고성능 읽기/쓰기 (2.2+ 분리, `pandas_gbq.read_gbq` / `pandas_gbq.to_gbq`)
- pandaSDMX — SDMX 통계 데이터 (statistics offices, central banks)

## 스케일 (out-of-core / 분산)

- **Bodo** — JIT 컴파일러로 pandas 워크로드를 클러스터로 자동 병렬화 (MPI 기반 HPC)
- **BigQuery DataFrames (bigframes)** — pandas API를 BigQuery 엔진으로 컴파일. `bpd.read_pandas(pd_df)` / `df.bigquery.ai.forecast(...)`. Polars hybrid engine.
- **Dask** — 분산 DataFrame, out-of-core
- Ibis — pandas 환경과 원격 시스템(Hadoop/Spark/Postgres) 사이 다리
- Koalas — Spark 위의 pandas API
- **Modin** — `import modin.pandas as pd` — 멀티코어/클러스터 자동 활용

## 데이터 정제·검증

- **Pandera** — 런타임 데이터 프레임 검증
- pyjanitor — 메서드 체이닝 데이터 정제

## 개발 도구

- **Hamilton** (Stitch Fix) — 선언형 데이터플로우 프레임워크 (feature engineering for ML)
- IPython / Jupyter / JupyterLab
- **marimo** — 반응형 Python+SQL 노트북 (DataFrame 인터랙티브 표·필터·SQL on DataFrame)
- pandas-stubs — 타입 스텁
- Spyder — Variable Explorer + Numpydoc 통합

## 기타 관련 라이브러리

- Compose — 라벨링 + 예측 엔지니어링
- **D-Tale** — 웹 기반 DataFrame 시각화 (Jupyter/Colab/Kaggle 통합)
- Featuretools — 자동 피처 엔지니어링 (시계열·관계형)
- IPython Vega
- plotnine — ggplot2 포팅 ("Grammar of Graphics")
- pygwalker — 인터랙티브 EDA + Vega-Lite 차트 저장
- **seaborn** — matplotlib 기반 통계 시각화 (pandas 객체 이해)
- skrub — pandas → scikit-learn 다리 (피처 빌딩)
- **Statsmodels** — 통계/계량경제, pandas와 오랜 특별 관계
- STUMPY — 시계열 매트릭스 프로파일

---

원본: https://github.com/pandas-dev/pandas/blob/main/web/pandas/community/ecosystem.md
SHA: 97c886ec8360487c76e3131a650171e5492c36c4 (size 28,020 bytes)
수집일: 2026-04-27 (석근님 BI 직무 직결: pandas-gbq, bigframes, Modin, Dask, Pandera, Hugging Face, Hamilton 핵심)
