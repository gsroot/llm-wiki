---
title: 데이터 파이프라인 (BigQuery 중심 BI)
aliases:
- Data Pipeline BigQuery
- 데이터 파이프라인
- 빅쿼리 파이프라인
type: concept
category: data
tags:
- bigquery
- mysql
- redis
- airflow
- BI
- mmp
- pandas
- bigframes
- modin
- dask
- pyarrow
related:
- '[[seokgeun-kim]]'
- '[[c2spf-analytics]]'
- '[[backend-python-fastapi]]'
- '[[ml-ai]]'
- '[[pandas]]'
- '[[pandas-dev]]'
- '[[portfolio-seed]]'
- '[[portfolio-ko]]'
- '[[c2spf-analytics-common]]'
- '[[c2spf-analytics-renewal]]'
- '[[pandas-dev-pandas]]'
source_count: 5
observed_source_refs: 24
inbound_count: 50
created: 2026-04-24
updated: 2026-04-27
cited_by_count: 22
---

# 데이터 파이프라인 (BigQuery 중심 BI)

## 정의

GCP BigQuery를 핵심 데이터 웨어하우스로 두고, 게임 로그 수집·가공·시각화 전 과정을 통합하는 데이터 레이어. 운영 DB(MySQL/MariaDB)·캐시(Redis) 계층과 분석 DB(BigQuery)가 워크플로 도구(Digdag · Celery · Airflow)와 결합해 **실시간 운영 + 배치 분석**을 함께 지원한다.

## 왜 중요한가

- **9년 이상 누적 운영** — 2017년부터 c2spf 애널리틱스의 핵심 데이터 백본으로 BigQuery를 사용. 게임 BI의 원천.
- BI 시각화·예측·다운로드·MMP 결합 등 **모든 분석 기능의 단일 진실 공급원(single source of truth)**.
- 8년 이상 BigQuery 위에서 운영을 지속하며 누적된 운영 노하우 — Decimal 변환, 슬레이브 동기화, 피벗 NULL 처리 등.

## 핵심 내용

- **저장소 계층**
  - Operational: MySQL · MariaDB · PostgreSQL · Redis (캐시/큐)
  - Analytical: GCP BigQuery (메인), GCP Storage (다운로드 결과 파일).
- **수집/가공**
  - 게임 클라이언트 로그 → 로그 수집 파이프라인 → BigQuery 저장.
  - Airbridge MMP 데이터 결합으로 광고 성과 분석 (2025-01).
  - HiveQL 기반 분산 쿼리 경험(줌인터넷).
- **워크플로 오케스트레이션**
  - Digdag (게임 정보 동기화 스케줄러, 2018-07~08).
  - Celery (대용량 다운로드 비동기 워커, 2019).
  - GCP AI Platform Pipeline (ML 예측 MLOps, 2020~2021).
- **운영 트릭**
  - BigQuery `Decimal` 타입 변환 규칙 정립.
  - 피벗 축 NULL 플레이스홀더 처리.
  - 슬레이브 DB 동기화 지연 대응(쿼리 라우팅, 재시도).
  - OS별 TCP Keepalive 설정 차이.

## 실전 적용

- **`/common/processed-data` 단일 엔드포인트** — BigQuery + Airbridge 결합·피벗팅 로직.
- **APIResponse + ProcessedData result_code** — 데이터 처리 결과를 4종 코드로 정형화.
- **BigQuery ML / AutoML Tables** — 게임 유저 이탈/구매 예측 (정확도 평균 85%+).
- **BigQuery + GCP Storage** — 대용량 데이터 다운로드 파이프라인 (Celery 비동기 워커).

## pandas 통합 — 도구 레이어 표준 (2026-04-27 추가)

[[pandas]]는 BigQuery 데이터 파이프라인의 **클라이언트 측 도구 레이어 표준**이다. BigQuery → pandas → 시각화/통계/ML로 이어지는 흐름이 9년 운영 전반의 기본 패턴.

### 진입 포인트 (BigQuery → pandas)

| 도구 | 호출 방식 | 사용 시기 |
|------|---------|----------|
| **pandas-gbq** | `pandas_gbq.read_gbq("SELECT ...")` / `pandas_gbq.to_gbq(df, ...)` | 표준 BigQuery ↔ DataFrame, 2.2+ 별도 패키지 분리됨 |
| **bigframes** | `bpd.read_pandas(pd_df)` / `df.bigquery.ai.forecast(...)` | pandas API를 BigQuery 엔진으로 컴파일 — 데이터를 BQ 밖으로 옮기지 않고 처리 |
| `read_sql` (옵션) | sqlalchemy + bigquery-sqlalchemy | 간단 쿼리 |

### 메모리 폭발 대응 결정 트리 (`scale.rst` 기반)

게임 BI 데이터의 메모리 폭발(수억 row, 시계열 누적) 대응:

1. **Load less data**: `pd.read_parquet(path, columns=[...])` 또는 `usecols=` — 필요한 컬럼만 읽기 (~1/10 메모리)
2. **Efficient datatypes**: low-cardinality 텍스트 → `Categorical`, numeric → `pd.to_numeric(downcast="...")` (~1/5 메모리)
3. **Chunking**: 연도별 parquet 디렉터리에서 `glob.iglob` + 청크별 `value_counts.add(fill_value=0)` — out-of-core 가능
4. **다른 라이브러리로 전환**:
   - `import modin.pandas as pd` (한 줄 변경, 멀티코어/클러스터)
   - **bigframes**: 데이터를 BigQuery에 두고 pandas 코드만 컴파일 (석근님 BI 환경에 가장 fit)
   - Dask/Bodo: 분산/HPC

### PyArrow 통합 ([[pdep|PDEP]]-10 진행 중)

BigQuery는 Arrow 기반 응답을 우선시. pandas의 `dtype_backend="pyarrow"` + `read_csv(engine="pyarrow")` + `pd.ArrowDtype(pa.string())`로 (1) 결측 지원 (2) polars/cuDF/DuckDB와의 상호운용 (3) 더 빠른 IO. 

[[c2spf-analytics-renewal]]의 React 리뉴얼 백엔드에서 pandas → JSON 직렬화 시 Arrow-backed 데이터로 통일하면 큰 응답 페이로드 최적화 가능.

### 검증 도구 — Pandera

[[microsoft-data-science-for-beginners]]가 강조하는 "데이터 윤리·해석성"을 코드로 구현하는 라이브러리. DataFrame의 스키마(컬럼·타입·범위·NULL 정책)를 런타임 검증. BI 파이프라인의 입력/출력 경계에 두면 "잘못된 데이터가 대시보드에 흘러가는" 사고를 막음.

```python
import pandera as pa
schema = pa.DataFrameSchema({
    "user_id": pa.Column(int, nullable=False),
    "dau_date": pa.Column(pa.DateTime),
    "revenue": pa.Column(float, pa.Check.ge(0)),
})
schema.validate(df)
```

## 관련 개념

- [[backend-python-fastapi]] — 백엔드가 BigQuery·MySQL·Redis 호출 (DataFrame 직렬화 시 pandas 사용)
- [[ml-ai]] — BigQuery → AutoML → AI Platform Pipeline 파이프라인의 데이터 소스 (pandas DataFrame이 입력 표준)
- [[devops-cicd]] — Promtail/Loki/Grafana로 데이터 파이프라인 로그 관측
- [[pandas]] — 클라이언트 측 도구 레이어 표준
- [[pandas-dev]] — [[bdfl|BDFL]] + Core Team + [[numfocus|NumFOCUS]] 거버넌스로 운영되는 조직

## 출처

- [[portfolio-seed]] — 9년차 BigQuery 운영 타임라인
- [[portfolio-ko]] — Selected Work 5선의 데이터 측면
- [[c2spf-analytics-common]] — 공통 모듈에서의 BigQuery 운영 디테일
- [[c2spf-analytics-renewal]] — Airbridge × BigQuery 결합 파이프라인
- [[pandas-dev-pandas]] — pandas 도구 레이어, scale.rst 결정 트리, ecosystem.md의 BI 직결 라이브러리(pandas-gbq, bigframes, Modin, Dask, Pandera)

## 열린 질문

- BigQuery의 비용 최적화 패턴(파티셔닝·클러스터링)은 어떤 기준으로 적용되었는가?
- HiveQL 시대 → BigQuery 전환 시 마이그레이션 비용/이득은?
- bigframes를 [[c2spf-analytics-renewal]]의 React 리뉴얼 백엔드에 도입하면 BigQuery 응답을 DataFrame으로 받는 비용을 어디까지 줄일 수 있는가?
- PyArrow-backed DataFrame이 게임 BI의 시계열·카테고리 데이터에 미치는 메모리/속도 효과는 NumPy-backed 대비 얼마나 큰가?
