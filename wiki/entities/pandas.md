---
title: "pandas (데이터 분석 라이브러리)"
type: entity
entity_type: tool
tags: [pandas, python, dataframe, data-analysis, time-series, BI, scikit-learn, numpy, pyarrow, bigquery, copy-on-write, 데이터분석]
related:
  - "[[pandas-dev]]"
  - "[[microsoft-data-science-for-beginners]]"
  - "[[microsoft-ml-for-beginners]]"
  - "[[data-pipeline-bigquery]]"
  - "[[ml-ai]]"
  - "[[c2spf-analytics]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# pandas (데이터 분석 라이브러리)

## 개요

**pandas**는 Python의 사실상 표준 데이터 분석 라이브러리다. 2008년 Wes McKinney가 AQR Capital Management(헤지펀드)에서 사내 도구로 개발 시작, 2009년 오픈소스, 2015년 [[numfocus]] 후원 프로젝트, 2026-04-27 v3.0 stable.

**Mission**: "the fundamental high-level building block for doing practical, real world data analysis in Python"

**Vision**: 데이터 분석/조작 소프트웨어가 (1) 누구나 접근 가능 (2) 무료로 사용/수정 가능 (3) 유연 (4) 강력 (5) 사용 쉬움 (6) 빠름.

석근님 [[c2spf-analytics]] BI 직무에서 [[data-pipeline-bigquery]] → DataFrame → 대시보드/통계의 핵심 도구 레이어.

## 주요 특징

### 두 가지 핵심 데이터 구조

| Dimensions | Name | Description |
|-----------|------|-------------|
| 1 | Series | 1D labeled homogeneously-typed array |
| 2 | DataFrame | 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns |

R 사용자에게는 `data.frame`의 풍부한 확장으로 이해 가능. NumPy 위에 구축됨.

### 101개 공개 API (pandas/__init__.py의 __all__)

20개 IO 읽기 함수가 가장 풍부 — `read_csv`, `read_parquet`, `read_sql`, `read_excel`, `read_hdf`, `read_orc`, `read_feather`, `read_json`, `read_xml`, `read_iceberg`, `read_html`, `read_clipboard`, `read_sas`, `read_spss`, `read_stata`, `read_table`, `read_fwf`, `read_pickle`, `read_sql_query`, `read_sql_table`. 이는 pandas가 본질적으로 "**모든 데이터 소스를 DataFrame으로 끌어오는** 게이트웨이"임을 시사.

핵심 능력:
- **Missing data 처리** — `NaN`, `NA`, `NaT` 통합
- **Data alignment** — 자동 라벨 기반 정렬
- **Group by** — split-apply-combine
- **Hierarchical indexing** (MultiIndex) — N차원 데이터를 2차원 구조에 표현
- **Time series** — date_range, frequency conversion, rolling/resample, tz handling, BusinessDay offset
- **Categoricals** — low-cardinality 텍스트의 메모리 효율 표현
- **PyArrow integration** — `dtype_backend="pyarrow"`, `read_csv(engine="pyarrow")`

### 성능 모델

- 핫패스는 **Cython** 또는 C로 작성
- **[[copy-on-write|Copy-on-Write]]** ([[pdep|PDEP]]-7, v2.0 Implemented) — 메모리 모델 변혁
- 옵션 의존성 `pandas[performance]` (numexpr, bottleneck, numba)으로 가속

### 시계열 (BI 핵심)

`Timestamp`, `Period`, `Timedelta`, `DateOffset`, `BusinessDay`, `tz_localize`/`tz_convert`, `resample("5Min").sum()`, `pd.offsets.BusinessDay(5)` — 게임 BI의 DAU/MAU/리텐션 코호트 분석은 사실상 pandas resample + groupby + Categorical의 합주.

## 학술 인용 정보

- **DOI**: 10.5281/zenodo.3509134 (Zenodo, 버전별 별도 DOI)
- **저자**: "The pandas development team" (집단 저자)
- **인용 논문**: McKinney, "Data structures for statistical computing in python", *Proceedings of the 9th Python in Science Conference*, 2010, pp 56–61, DOI 10.25080/Majora-92bf1922-00a.
- **CITATION.cff** 표준 사용 — GitHub의 자동 인용 메타데이터.

## 라이선스 / 의존성

- **BSD 3-Clause** ("Simplified" / "New" BSD)
- 필수: NumPy 1.26.0+, python-dateutil 2.8.2+, tzdata (Windows/Pyodide 한정)
- 옵션 그룹: `performance`, `plot`, `excel`, `html`, `xml`, `postgresql`, `mysql`, `sql-other`, `hdf5`, `parquet`, `feather`, `iceberg`, `spss`, `fss/aws/gcp`, `clipboard`, `compression`, `timezone`, `computation`, `output-formatting`, `all`

## 4축 정체성

| 축 | 내용 | 비교 |
|----|------|------|
| 라이브러리 본체 | 101 공개 API, BSD-3 | NumPy/SciPy와 동급의 PyData 핵심 |
| **거버넌스** | [[bdfl|BDFL]] + Core Team + [[numfocus|NumFOCUS]] Subcommittee | spec-kit·anthropics-skills와 본질적으로 다른 3축 |
| **로드맵 시스템** | [[pdep|PDEP]] (절차적 결정) | spec-kit Constitution(사전 합의)과 대조 |
| 에코시스템 | Modin/Dask/Bodo/bigframes로 스케일, Pandera로 검증, scikit-learn 연동 | 표준 인터페이스 역할 |

## Brand & Logo

- 이름은 항상 소문자 "pandas" — 문장 시작 위치라도 소문자
- 로고 색상: Blue `#150458`, Yellow `#FFCA00`, Pink `#E70488`
- 로고 디자인 in-kind 후원: Indeed

## 관련 개념

- [[data-pipeline-bigquery]]: pandas-gbq, bigframes 액세서로 BigQuery ↔ DataFrame 양방향
- [[ml-ai]]: scikit-learn의 first-class citizen (입력/출력 모두 DataFrame), skrub이 다리
- [[pdep]]: pandas의 거버넌스 산출물 시스템 (1~14번 채택, BDFL 단계 → PDEP 단계로 거버넌스 진화)
- [[copy-on-write]]: PDEP-7 메모리 모델 변혁
- [[dataframe]]: 데이터 분석의 보편적 추상
- [[lazy-evaluation]]: pandas는 본질적 eager. Polars/DuckDB의 lazy 모델과 대조 — PDEP-10 이후 부분 lazy 진화 가능성

## 자매 도구 비교 (16회차 추가)

| 축 | pandas | [[polars]] | [[duckdb]] |
|----|--------|------------|------------|
| 정체성 | 라이브러리 | 쿼리 엔진 | 임베디드 OLAP DB |
| 메모리 모델 | NumPy + CoW (PyArrow 점진) | Apache Arrow immutable | Vectorized columnar |
| 평가 모델 | Eager | Lazy + Eager + Streaming | SQL 본질적 lazy |
| Import 시간 | 520ms | 70ms | (인프로세스, 즉시) |
| API | 메소드 + indexing | Expression DSL | SQL |
| Lock-in | NumPy, 풍부한 통합 | Apache Arrow | Apache Arrow + SQL 표준 |

→ 셋은 경쟁이 아니라 **워크플로우 단계별 도구**. 자세한 비교는 [[dataframe-ecosystem-evolution]] / [[pandas-vs-polars-vs-duckdb]] 참조.

## 출처

- [[pandas-dev-pandas]] — pandas-dev/pandas GitHub 저장소 + 공식 웹사이트(pandas.pydata.org/about/, /community/) 통합 수집

## 메모

- McKinney의 책 "Python for Data Analysis"가 pandas 학습의 표준 — 2012년 초판, 현재 3판. 일하면서 곁에 두면 좋은 레퍼런스.
- Wes McKinney = [[bdfl|BDFL]]이지만 일상 메인테이너 리스트에서는 "inactive"로 분류됨 — BDFL ≠ 일상 운영자라는 거버넌스 위계 표시.
- pandas 3.0 stable 출시 후 PyArrow가 점차 1급 데이터 모델로 전환 중. PDEP-10이 통과되면 NumPy 단일 의존이 깨짐.
- "Highly optimized for performance" — 그러나 100M+ row에서는 Modin/Dask/Bodo로 자동 병렬화 또는 bigframes로 BigQuery 위임이 표준 결정 트리.
