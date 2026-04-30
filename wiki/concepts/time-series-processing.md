---
title: 시계열 처리 (Time Series Processing) — 저장 · 알고리즘 · 관측성
aliases:
- Time Series
- 시계열
- time-series-processing
- 시계열 처리
- TS Processing
type: concept
category: 데이터분석
tags:
- time-series
- 시계열
- timescaledb
- prometheus
- arima
- lightgbm
- pandas
- bigquery
- 데이터분석
related:
- '[[data-pipeline-bigquery]]'
- '[[dataframe]]'
- '[[observability]]'
- '[[postgresql]]'
- '[[prometheus]]'
- '[[grafana]]'
- '[[lightgbm]]'
- '[[scikit-learn]]'
- '[[pandas]]'
- '[[microsoft-lightgbm]]'
- '[[microsoft-ml-for-beginners]]'
- '[[pandas-dev-pandas]]'
- '[[postgres-postgres]]'
- '[[prometheus-prometheus]]'
- '[[c2spf-analytics]]'
- '[[matechat]]'
source_count: 5
created: 2026-04-30
updated: 2026-04-30
cited_by_count: 2
---

# 시계열 처리 (Time Series Processing) — 저장 · 알고리즘 · 관측성

## 정의

**시간을 1차 인덱스로 가진 데이터의 저장·조회·분석·모니터링** 패턴. 게임 BI(DAU/매출/세션), MateChat KPI(D+1/D+7/D+30 retention), 인프라 모니터링(CPU/latency/errors), AI/ML(forecasting/anomaly detection) 등 owner의 일상 작업 대부분이 시계열 위에서 작동.

핵심: 시계열 데이터는 **append-heavy + sequential read + time-window aggregation**의 명확한 access pattern을 가져 일반 OLTP/OLAP과 다른 인프라 + 알고리즘 + 시각화 layer가 진화함.

## 왜 중요한가

### owner 일상에서

- **[[c2spf-analytics]]**: 게임 데이터 BI는 본질적으로 시계열. DAU·MAU·매출·LTV·이탈률 모두 time series.
- **[[matechat]]**: 출시 후 KPI 회수 (D+1/D+7/D+30 retention, 주간 cohort, AI 사용량 시계열).
- **인프라 운영**: Prometheus + Grafana 메트릭 모니터링, Sentry 에러 시계열.
- **이상 탐지·forecasting**: 게임 출시 전후 코호트 분석, 매출 forecasting, 사용자 이탈 예측.

시계열 처리는 owner 직무의 거의 모든 영역에 등장 — 한 페이지로 통합 정리할 가치가 가장 큼.

## 핵심 내용

### 1. 시계열 저장 4가지 옵션

| 저장 | 사례 | 강점 | 약점 |
|---|---|---|---|
| **TimescaleDB** ([[postgresql]] 확장) | 게임 OLTP + 시계열 통합 | SQL 호환 + hypertable 자동 partition | 단일 노드, 대규모 분산 부담 |
| **[[prometheus]] TSDB** | 인프라 메트릭 (CPU, latency, error rate) | scrape pull 모델, 17K stars OSS, vendor-neutral 표준 | scalar metric만, label cardinality 제한 |
| **[[duckdb]]** + Parquet | 분석 워크로드, BI ad-hoc | columnar OLAP, 단일 파일 portable | 영속 OLTP 부적합 |
| **BigQuery + 시계열 partition** | c2spf-analytics 표준 | 무한 스케일, SQL, 매니지드 | 비용·latency, 시계열 전용 최적화 부재 |

owner의 실전 분기:
- **인프라 메트릭**: Prometheus (1차) + Grafana (시각화)
- **게임 비즈니스 데이터**: BigQuery (대용량) + DuckDB (로컬 ad-hoc)
- **OLTP에 시계열 결합**: 향후 검토 시 TimescaleDB 후보 (PostgreSQL 마이그레이션 부담 적음)

### 2. 시계열 알고리즘 3계층

| 계층 | 도구 | 적합 시나리오 |
|---|---|---|
| **통계적 모델** | ARIMA, SARIMA, Prophet (sktime / statsmodels) | 단변량, 명확한 seasonality, 저용량 |
| **트리 기반 ML** | [[lightgbm]] / XGBoost (multi-feature regression) | 다변량, 비선형, 외부 변수 (마케팅·이벤트) 통합 |
| **딥러닝** | Temporal Fusion Transformer / N-BEATS / LSTM | 매우 큰 데이터, 복잡 패턴, 계산 비용 큼 |

owner 적용:
- **게임 매출 forecasting**: LightGBM (이벤트·마케팅·계절성을 feature로 통합) — c2spf-analytics에 직접 적용 가능
- **사용자 이탈 예측 (churn)**: LightGBM + 행동 시계열 features
- **단순 trend**: ARIMA로 충분 (단변량, 며칠 forecast)
- **딥러닝**: 현재 owner의 ROI 부족 (BI에 도입 검토 시점이 아직 아님)

### 3. 시계열 라이브러리 (Python)

| 라이브러리 | 강점 | 사용처 |
|---|---|---|
| **[[pandas]]** | DatetimeIndex, resample, rolling, shift | 첫 진입점, 모든 시계열 EDA |
| **[[polars]]** | LazyFrame + 시계열 expression, 5~10× 빠름 | 대용량 시계열 처리 |
| **[[duckdb]]** | SQL `time_bucket()`, window function | ad-hoc 분석, BI dashboard 백엔드 |
| **scikit-learn** + [[lightgbm]] | regression / forecasting | ML 파이프라인 |
| **statsmodels / sktime / Prophet** | ARIMA / 시계열 분해 | 통계적 forecasting |

owner의 stack: **pandas (EDA) → DuckDB/Polars (대용량) → LightGBM (ML)** 가 검증된 4단 파이프라인.

### 4. 관측성 시계열 (Observability TSDB)

[[observability]] 영역의 시계열은 비즈니스 시계열과 다른 특성:

| 차원 | 비즈니스 시계열 | 관측성 시계열 |
|---|---|---|
| **수집 주기** | 일·시간 (배치) | 초·밀리초 (실시간) |
| **저장 기간** | 영구 (BigQuery + GCS archive) | 최근 (15일 hot, 연간 archive) |
| **쿼리 패턴** | ad-hoc OLAP, drilldown | 실시간 대시보드, alerting |
| **도구** | BigQuery + Polars + LightGBM | Prometheus + Grafana + Loki |

owner의 c2spf-analytics는 둘 다 운영 — **비즈니스 데이터(BigQuery)** + **인프라 메트릭(Prometheus + Grafana)** 분리.

### 5. 시계열 분석 표준 패턴 5종

| 패턴 | 설명 | owner 사례 |
|---|---|---|
| **Resampling** | 분 → 시간 → 일 → 주 down/up sample | DAU 일별 → 주별 평균 |
| **Rolling Window** | N일 이동평균 / 표준편차 | 7일 이동평균 매출 (요일 노이즈 제거) |
| **Lag Features** | t-1, t-7, t-28 시점 값 features | LightGBM 학습 입력 |
| **Cohort Analysis** | 가입 주차별 retention 추적 | matechat D+1/D+7/D+30 |
| **Anomaly Detection** | 이상값 탐지 (z-score, IQR, isolation forest) | 매출 급락 알림, 인프라 outlier |

### 6. 시간대 (Timezone) 함정

owner의 글로벌 게임 BI는 시간대가 핵심 변수:
- **UTC 저장 + 로컬 표시**: 표준 (BigQuery + dbt 시간대 함수)
- **로컬 시간대 저장 (KST/JST/PT 등)**: 절대 금지 (DST 처리 지옥)
- **요일 분석은 어느 timezone?**: 한국 게이머·일본 게이머 요일 패턴이 다름 — 게임별 메인 timezone 분석 필수
- **이벤트 ingestion 시각 = client time vs server time**: client time은 조작 가능, server time은 절대 truth

## 안티패턴

| 안티패턴 | 문제 | 회피 |
|---|---|---|
| 시계열 데이터를 일반 RDBMS row-major에 단순 INSERT | scan 비용 폭발, partition 없음 | TimescaleDB hypertable 또는 BigQuery 시계열 partition |
| Prometheus에 high-cardinality label (user_id, request_id) | TSDB 폭발, OOM | Loki / Sentry / BigQuery로 분리 |
| pandas로 100GB+ 시계열 메모리 적재 | OOM | Polars LazyFrame 또는 DuckDB SQL |
| ARIMA를 multi-feature 시계열에 강제 | 외부 변수 무시 | LightGBM regression with lag features |
| 클라이언트 시각으로 분석 | DST + 조작 가능 + 시간대 혼란 | 항상 server UTC로 분석, 표시만 로컬 |

## owner 활용 시나리오

### [[c2spf-analytics]] 게임 데이터 분석

```python
import polars as pl
import lightgbm as lgb

# 1. 시계열 추출 (BigQuery → Polars)
df = pl.read_database("""
    SELECT date, game_id, dau, revenue, event_count
    FROM analytics.daily_kpi
    WHERE date >= '2025-01-01'
    ORDER BY date, game_id
""", connection=bq_conn)

# 2. Lag features
df = df.with_columns([
    pl.col("dau").shift(1).over("game_id").alias("dau_lag_1"),
    pl.col("dau").shift(7).over("game_id").alias("dau_lag_7"),
    pl.col("revenue").rolling_mean(window_size=7).over("game_id").alias("revenue_7d_avg"),
])

# 3. LightGBM forecasting
model = lgb.LGBMRegressor(n_estimators=500, learning_rate=0.05)
model.fit(X_train, y_train)
```

### [[matechat]] 출시 후 KPI 회수

D+1 / D+7 / D+30 retention cohort 분석. server UTC로 가입 시각 저장 → cohort_week 계산 → 주차별 retention rate 시계열. matechat-30day-validation-loop의 핵심 입력.

### 위키 자체 시계열 — 페이지 수 진화

이 위키 자체도 시계열: 일별 page count, 주별 source 추가 수, 월별 신설 concept 수. `git log` + 간단 스크립트로 추출 가능. owner의 위키 운영 ROI 모니터링.

## 관련 개념

- [[data-pipeline-bigquery]] — 시계열 저장의 owner 1차 인프라.
- [[dataframe]] — 시계열의 in-memory 표현 (pandas DatetimeIndex, Polars datetime).
- [[observability]] — 인프라 시계열 (Prometheus + Grafana).
- [[lazy-evaluation]] — Polars + DuckDB가 시계열 처리를 lazy로 수행해 OOM 회피.
- [[predicate-pushdown]] — 시계열 partition + WHERE date 가 자동 결합.

## 출처

- [[microsoft-ml-for-beginners]] — 7-TimeSeries 시리즈 (lesson 21~) ARIMA/SVR. 시계열 ML 입문 표준.
- [[microsoft-lightgbm]] — GBDT 기반 시계열 forecasting. 게임 매출 예측 직접 적용.
- [[pandas-dev-pandas]] — DatetimeIndex / resample / rolling / shift API. owner 일상 도구.
- [[postgres-postgres]] — TimescaleDB 확장 검토. PostgreSQL OLTP + 시계열 통합.
- [[prometheus-prometheus]] — TSDB 표준. owner의 인프라 메트릭 1차 저장.

## 열린 질문

- **TimescaleDB 도입 ROI**: c2spf-analytics가 BigQuery에 의존하지만 일부 시계열은 TimescaleDB가 비용·latency 우위. 어느 시점에 분기 결정?
- **딥러닝 시계열 도입 ROI**: LightGBM이 95% 시나리오 커버. Temporal Fusion Transformer 같은 SOTA가 c2spf 도입 정당화 시점은?
- **matechat AI 사용량 시계열 분석**: 챗봇 사용 패턴 (시간대·요일·세션 길이) 분석으로 inference 비용 예측 가능?
- **시계열 데이터 거버넌스**: schema 변경 (예: 새 metric 추가) 시 [[governance-axis-comparison|6축 거버넌스]] 중 어느 것이 적합?
