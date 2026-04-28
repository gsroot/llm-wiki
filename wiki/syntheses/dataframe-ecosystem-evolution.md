---
title: "DataFrame 생태계 진화사 — Pandas → PyArrow → Polars → DuckDB"
type: synthesis
category: data
tags: [dataframe, pandas, polars, duckdb, pyarrow, parquet, apache-arrow, kafka, lazy-evaluation, columnar, ecosystem-evolution, 16회차]
sources:
  - "[[pandas-dev-pandas]]"
  - "[[pola-rs-polars]]"
  - "[[duckdb-duckdb]]"
  - "[[apache-arrow]]"
  - "[[apache-kafka]]"
created: 2026-04-28
updated: 2026-04-28
---

# DataFrame 생태계 진화사

> 2008년 pandas의 단일 표준 시대 → 2016년 Apache Arrow의 메모리 표준화 → 2018년 DuckDB의 임베디드 OLAP → 2020년 Polars의 쿼리 엔진 패러다임. **단일 라이브러리 → 표준 위에 다 도구**로의 18년 진화.

## 1. 4단계 진화 타임라인

| 연도 | 사건 | 계층 | 의미 |
|------|------|------|------|
| **2008** | [[pandas]] 시작 (Wes McKinney @ AQR) | 라이브러리 | DataFrame 추상이 Python에 도입 |
| **2010** | Google Dremel 논문 | 학술 | 컬럼 + Record Shredding 알고리즘 발표 |
| **2013** | [[parquet]] 시작 (Twitter + Cloudera) | 온디스크 표준 | Dremel을 OSS로 — Hadoop 표준 |
| **2016** | [[apache-arrow]] 1.0 (Wes McKinney 발기) | 인메모리 표준 | 언어 횡단 컬럼 포맷 |
| **2018** | [[duckdb]] 시작 (Mühleisen + Raasveldt @ CWI) | 임베디드 OLAP | "분석용 SQLite" |
| **2020** | [[polars]] 시작 (Ritchie Vink) | 쿼리 엔진 | DataFrame DSL + 옵티마이저 |
| **2023** | pandas 2.0 + PyArrow 백엔드 | 이행기 | NumPy → Arrow 점진 전환 |
| **2024-2026** | Lakehouse 표준화 (Iceberg/Delta on Parquet) | 데이터 레이크 | 파일 = 테이블 = DB |

→ 진화의 본질: **개별 라이브러리 → 공통 표준 + 그 위 다양한 도구**.

## 2. 핵심 변곡점 — "메모리 표준 = 디스크 표준" 통합

### 2010년 이전 (개별 모델 시대)

각 라이브러리가 독자 메모리 모델:
- pandas: NumPy ndarray
- R data.frame: 자체 구조
- HDF5/Avro/ORC: 디스크별 자체 포맷
- DB 결과: 행 단위, 변환 비용

**문제**: pandas → DB 송신 시 변환 비용. R ↔ Python 호환 어려움. 디스크 ↔ 메모리 변환 4-10배 시간.

### 2016년 이후 (Arrow 통합 시대)

Apache Arrow가 **단일 자료형 모델**을 메모리·디스크 양면에 적용:
- 인메모리: Arrow Columnar Format
- 온디스크: Parquet (Arrow 자료형 직접 매핑)
- 네트워크: Arrow IPC (zero-copy 직렬화)
- DB: ADBC (JDBC/ODBC의 Arrow 후속)

→ **변환 비용이 0**으로 수렴. pandas/Polars/DuckDB가 GB/s IO 처리량을 내는 근본 이유.

## 3. 진화의 5축 — 패러다임 비교

| 축 | pandas (2008) | PyArrow (2016) | DuckDB (2018) | Polars (2020) |
|----|---------------|----------------|---------------|---------------|
| **정체성** | 라이브러리 | 메모리 표준 + Python 바인딩 | 임베디드 OLAP DB | 쿼리 엔진 |
| **API** | 메소드 + indexing | Table/Array/Compute | SQL | Expression DSL |
| **메모리 모델** | NumPy + [[copy-on-write|CoW]] | Arrow immutable | Vectorized columnar | Arrow immutable |
| **평가 모델** | Eager | Lazy Datasets | SQL 본질 lazy | [[lazy-evaluation\|Lazy]] + Eager + Streaming |
| **언어** | Python | C++ + 11+ 바인딩 | C++17 + 5+ 바인딩 | Rust + 5 바인딩 |

### 진화의 방향성

1. **메소드 → 표현식 → SQL**: API의 추상도 상승
2. **NumPy → Arrow**: 메모리 모델의 표준화
3. **Eager → Lazy**: 옵티마이저 가능성 확보
4. **단일 언어 → 다언어**: 같은 코어가 여러 언어에서 작동

## 4. CoW vs Immutable — 같은 문제의 다른 답

pandas의 [[copy-on-write]]가 풀려고 한 문제:
- view/copy 모호성 (`SettingWithCopyWarning`)
- 메모리 효율 (불필요 복사 비용)
- 예측 가능성

**pandas의 답 (CoW)**: 모델은 유지하되, 쓰기 시점에 명확히 복사.
**Polars의 답 (Immutable-by-Default)**: 모델 자체를 바꿈 — 모든 버퍼가 read-only.

| 트레이드오프 | CoW (pandas) | Immutable (Polars/Arrow) |
|--------------|--------------|--------------------------|
| in-place 업데이트 | 가능 | 불가 (의도적) |
| 모호성 | 해결됨 | 발생 자체 안 함 |
| API 학습 | 기존 + `.loc[]` 패턴 | "in-place 없음" 패러다임 |
| 호환성 | NumPy 1급 | Arrow 1급 |
| zero-copy 공유 | 제한적 | 자연스러움 |

→ **둘은 수렴**: pandas 3.0 + PyArrow 백엔드 → 점차 Arrow immutable 모델 흡수. PDEP-10이 통과되면 거의 같은 모델.

## 5. 도구별 사용 시나리오 — 경쟁 아닌 보완

### 시나리오 A: 데이터 사이언스 노트북

```
[데이터 소스] → [DuckDB SELECT] → [Polars Lazy 변환] → [pandas로 변환] → [scikit-learn / Plotly]
       ↑                ↑                  ↑                    ↑
   파일/S3/PG    SQL 옵티마이저     Expression DSL       ML/시각화 호환
```

### 시나리오 B: 분석 BI API ([[c2spf-analytics]])

```
[BigQuery storage API]
       ↓ (Arrow IPC zero-copy)
   PyArrow Table
       ↓
   Polars LazyFrame (predicate/projection pushdown)
       ↓
   FastAPI 응답 (dict / Arrow IPC)
```

→ Polars가 BigQuery 데이터를 가공, FastAPI가 노출. pandas는 ML 출력에만 사용.

### 시나리오 C: 데이터 레이크 분석

```
S3 → Parquet 파일들 → DuckDB `SELECT * FROM 's3://...'` → 결과 분석
                          ↓
                   Polars `pl.scan_parquet(...)` (대안)
```

→ **둘 다 단일 노트북에서 수행 가능**. Spark/Trino 불필요.

### 시나리오 D: 이벤트 스트리밍 → 분석

```
[게임 서버] → [Kafka] → [Kafka Connect → BigQuery]
                   ↓
              [Kafka Streams] → 실시간 집계 → Redis/Cassandra
                   ↓
              [Parquet S3 sink] → DuckDB/Polars 배치 분석
```

→ [[apache-kafka]]가 streaming 인프라, Parquet/Polars/DuckDB가 분석 인프라.

## 6. Apache Foundation의 8번째 거버넌스 모델

15회차 [[backend-fastapi-stack]]에서 7개 OSS 거버넌스 모델 발견. 16회차에서 **Apache Software Foundation PMC**가 8번째:

| 거버넌스 모델 | 사례 | 특징 |
|--------------|------|------|
| BDFL | [[python]], [[pandas]] (초기) | 단일 결정자 |
| BDFL + Core Team | [[pandas]] (현재) | 위임 구조 |
| Core Team + PEP | [[python]] | 절차적 의사결정 |
| 회사 + OSS | [[fastapi]], [[pydantic]] (Pydantic Inc) | 창립자 회사 + OSS 본체 |
| VC-backed 회사 | [[astral]] (uv/ruff/ty) | 기업 통합 |
| 메일링 리스트 | [[postgresql]] | PR 받지 않음, 30년 정체성 |
| 라이센스 변경 | [[redis]] (2024 SSPL) | OSS → 유사 OSS 전환 |
| **ASF PMC** | [[apache-arrow]], [[apache-kafka]], [[parquet]] | **재단 + PMC + Apache Way** |

ASF PMC의 특징:
- **재단 = 비영리, 다중 프로젝트**
- **PMC = Project Management Committee**, 프로젝트별 거버넌스
- **Apache Way**: sustainability + diversity + code of conduct + Apache 2.0
- **JIRA + 메일링 리스트 + Confluence** 4축
- **Incubation 절차**: 새 프로젝트 → Incubator → Top-Level Project

→ Apache 산하 도구는 **단일 회사가 거버넌스를 흡수할 수 없는 구조**. [[redis]] 2024 라이센스 변경이 ASF에서는 불가.

## 7. "디스크는 친구" — Kafka 사상의 일반화

[[apache-kafka]] design.md는 분산 시스템의 핵심 명제를 단순화: **filesystem + sequential I/O + pagecache + sendfile = 충분**.

이 사상이 다른 도구에 미친 영향:

| 도구 | 적용 |
|------|------|
| [[postgresql]] WAL | Append-only sequential log |
| [[kafka]] Topic | WAL을 분산 시스템으로 일반화 |
| [[redis]] AOF | append-only file (Kafka WAL 사상) |
| [[parquet]] | column chunk = sequential read 단위 |
| [[duckdb]] | mmap + zero-copy Parquet 읽기 |
| [[polars]] | streaming engine = sequential page processing |

→ "데이터 인프라는 본질적으로 sequential I/O 위에 빌드됨" — 16회차의 메타 발견.

## 8. 회사 BI 적용 — c2spf-analytics 권장 스택

### 현재 (가정)
```yaml
storage:
  - bigquery: 운영 데이터 웨어하우스
  - gcs: 백업 + 외부 export
compute:
  - pandas: 데이터 가공
api:
  - fastapi: 대시보드 API
```

### 16회차 후 권장
```yaml
storage:
  - bigquery: 운영 DW (변경 없음)
  - gcs: parquet export (포맷 표준화)
ingestion:
  - kafka: 게임 서버 이벤트 → BQ streaming insert (대안 평가)
compute:
  - polars: 메인 데이터 가공 (lazy + streaming, pandas 대체)
  - duckdb: ad-hoc 탐색, BQ 비용 절감 (parquet 직접 SELECT)
  - pandas: ML 출력만 (scikit-learn 호환)
memory:
  - pyarrow: 모든 도구 사이의 zero-copy 다리
api:
  - fastapi: 응답 시 Arrow IPC 또는 dict (변경 없음)
```

### 마이그레이션 ROI
- **Cold start**: 520ms (pandas import) → 70ms (polars import) — Lambda/컨테이너에서 결정적
- **메모리**: 200GB+ 일일 로그 streaming 처리 가능 (pandas는 OOM)
- **BQ 비용**: 탐색 워크로드를 DuckDB로 옮기면 슬롯 비용 절감
- **Risk**: API 학습 (Polars DSL ≠ pandas), Plotly/Geopandas 일부 pandas-only

## 9. 16회차의 메타 발견

### 1. "메모리 표준 = 디스크 표준" 통합의 위력

Apache Arrow + Parquet의 단일 자료형 모델은 데이터 인프라 역사상 가장 성공적인 표준화. **변환 비용 0** 보장 → 도구 lock-in 감소 + 새 도구 진입 장벽 낮춤.

### 2. "쿼리 엔진" 정체성의 부상

[[polars]]와 [[duckdb]]가 동시에 "쿼리 엔진"이라는 자기 정의 → DataFrame ↔ SQL 경계 무너짐. **둘 다 옵티마이저 + 벡터화 + Arrow** 위에 빌드.

### 3. Lazy = 미래

pandas eager의 직접 후예가 없음. Polars/DuckDB/Spark/Dask 모두 lazy. **eager는 탐색용, lazy는 운영용**으로 분화 중.

### 4. 학술 → OSS → SaaS 패턴

| 학술 | OSS | SaaS |
|------|-----|------|
| Dremel 논문 (Google, 2010) | Parquet (2013) | BigQuery |
| C-Store 논문 (2005) | DuckDB (2018) | MotherDuck |
| Lakehouse 논문 | Iceberg/Delta (2018) | Databricks |

→ "학술 논문 → 5-10년 후 OSS → SaaS" 사이클이 표준화.

### 5. 단일 노드 한계 = 4.2B 행

[[polars]] `bigidx`, [[pandas]] 64bit index, [[duckdb]] in-process — 모두 **2^32 행**에서 한계. 그 너머는 분산 시스템 (Spark/Dask). 16회차에서 본 도구 모두는 **노트북~중형 서버 사이즈** 대상.

## 출처

- [[pandas-dev-pandas]] — 11회차 수집, DataFrame 추상의 표준
- [[pola-rs-polars]] — 16회차 수집, 쿼리 엔진 패러다임
- [[duckdb-duckdb]] — 16회차 수집, 임베디드 OLAP
- [[apache-arrow]] — 16회차 수집, 메모리/디스크 표준 통합
- [[apache-kafka]] — 16회차 수집, 데이터 인프라 사상

## 후속 작업

- `concepts/predicate-pushdown.md` — Lazy/SQL/Parquet 통합 메커니즘
- `concepts/columnar-storage.md` — Arrow/Parquet/DuckDB/Polars 공통 기반
- `entities/iceberg.md`, `entities/delta-lake.md` — Parquet 위 lakehouse 표준
- `entities/spark.md` — 분산 lazy의 산업 표준 (4.2B 행 너머)
- `entities/voltron-data.md` — Wes McKinney의 통합 거버넌스 회사
- 17회차 ML 클래식 + LLM 인프라 진행 시 LangChain/LangGraph가 Polars/Pandas 통합 패턴 검토
