---
title: PyArrow
aliases:
- PyArrow
- 파이애로우
- Apache Arrow Python
type: entity
entity_type: tool
tags:
- pyarrow
- apache-arrow
- columnar
- in-memory
- zero-copy
- parquet
- ipc
- python
related:
- '[[apache-arrow]]'
- '[[parquet]]'
- '[[pandas]]'
- '[[polars]]'
- '[[duckdb]]'
- '[[copy-on-write]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 8
inbound_count: 46
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 19
---

# PyArrow

## 개요

PyArrow는 [[apache-arrow]]의 **Python 바인딩**. C++ Arrow 라이브러리를 Python에서 사용 가능하게 하며, **데이터 사이언스 스택의 메모리 표현 표준**으로 자리잡음. 2016년 Apache Arrow 1.0과 함께 시작. 2026년 현재 v18.x.

라이센스: **Apache 2.0**. PyPI: `pyarrow` (단일 패키지에 C++ 바이너리 동봉, ~80MB wheel). [[pandas]]·[[polars]]·[[duckdb]] 모두 의존하는 사실상의 데이터 사이언스 메모리 인프라.

## 주요 특징

### 5대 컴포넌트 (Arrow 본체와 동일)

1. **Columnar Format** — `pyarrow.Table`, `RecordBatch`, `Array`
2. **IPC** — 프로세스 간 zero-copy 전송 (`pyarrow.ipc.write_stream`)
3. **Parquet** — `pyarrow.parquet.read_table` / `write_table`
4. **Flight RPC** — `pyarrow.flight` (gRPC 기반 분산)
5. **Compute** — `pyarrow.compute` (벡터 연산, Gandiva 통합)

### 핵심 사용 패턴

```python
import pyarrow as pa
import pyarrow.parquet as pq

# Parquet 직접 읽기
table = pq.read_table("data.parquet")

# pandas ↔ PyArrow zero-copy
df = table.to_pandas()
table2 = pa.Table.from_pandas(df)

# Polars ↔ PyArrow zero-copy
import polars as pl
pl_df = pl.from_arrow(table)
arrow_back = pl_df.to_arrow()

# DuckDB ↔ PyArrow zero-copy
import duckdb
duckdb.sql("SELECT * FROM table").arrow()
```

→ **3개 DataFrame 라이브러리의 공통 다리**.

### PyArrow as pandas 백엔드

pandas 2.0+에서 `dtype_backend="pyarrow"` 옵션 — pandas의 인메모리 모델을 NumPy 대신 Arrow로:

```python
df = pd.read_csv("data.csv", dtype_backend="pyarrow", engine="pyarrow")
df = pd.read_parquet("data.parquet", dtype_backend="pyarrow")
```

[[pandas]] PDEP-10이 통과되면 PyArrow가 1급 모델 (NumPy 의존 깨짐).

### Compute 함수

`pyarrow.compute` 모듈은 200+ 벡터 연산 제공:
- 산술 (`add`, `multiply`, `divide`)
- 문자열 (`utf8_upper`, `match_substring`, `split_pattern`)
- 시계열 (`year`, `quarter`, `is_in`)
- 집계 (`sum`, `mean`, `mode`)

Gandiva LLVM JIT 컴파일러와 통합 — 표현식이 SIMD로 컴파일됨.

### Datasets API — 멀티파일/파티션 추상

```python
import pyarrow.dataset as ds

dataset = ds.dataset("s3://bucket/year=2024/", partitioning="hive")
filtered = dataset.scanner(filter=ds.field("region") == "US")
table = filtered.to_table()
```

→ Hive-style 파티션 자동 인식, predicate pushdown, schema evolution. **데이터 레이크의 Python 게이트웨이**.

### IPC vs Parquet

| 용도 | 포맷 | 특징 |
|------|------|------|
| 프로세스 간/네트워크 | **IPC (Feather)** | zero-copy 매핑, 직렬화 빠름, 압축 옵션 |
| 영속/장기 저장 | **Parquet** | 압축률 높음, 컬럼 프루닝, 스키마 진화 |

IPC = "임시 빠른 직렬화", Parquet = "영구 효율 저장". 둘 다 PyArrow가 표준.

### ADBC (Arrow Database Connectivity)

`adbc_driver_postgresql`, `adbc_driver_sqlite`, `adbc_driver_bigquery` 등 — DB 결과를 처음부터 Arrow로 받음 → JDBC/ODBC 변환 비용 0. PyArrow가 ADBC의 Python 측 표준.

## 라이센스 / 의존성

- **Apache 2.0**
- 의존성: NumPy (옵션 of optional)
- C++ Arrow 라이브러리 동봉 (vendored)
- 선택적: pandas (변환), gandiva (JIT), Flight (gRPC)

## 관련 개념

- [[apache-arrow]]: 본체 표준. PyArrow는 그 Python 바인딩
- [[parquet]]: 자매 표준. PyArrow가 Python 측 표준 reader/writer
- [[copy-on-write]]: pandas의 메모리 모델 vs PyArrow의 immutable — 정반대. PDEP-10 통과 시 pandas가 PyArrow 모델로 전환
- [[lazy-evaluation]]: PyArrow Datasets API가 lazy scan 제공
- [[dataframe]]: PyArrow Table은 DataFrame의 일반화 (컬럼 추상)
- [[ml-ai]]: ML 피처 저장소 표준 — Tecton/Feast가 Arrow 위에 빌드
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: BigQuery storage API + PyArrow zero-copy 패턴이 표준

## 관련 엔티티

- [[apache-arrow]]: 본체. Apache Software Foundation 산하
- [[pandas]]: PyArrow 백엔드 점진 통합. PDEP-10 통과 시 1급
- [[polars]]: PyArrow 위에서 실행. Polars는 Arrow의 직계 후손
- [[duckdb]]: PyArrow zero-copy 통합. ADBC 자체 지원
- [[parquet]]: PyArrow가 Python 측 표준 reader/writer
- [[fastapi]]: API 응답 시 PyArrow IPC 직렬화 → 클라이언트 zero-copy 가능 (gRPC + Arrow Flight)
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 데이터 파이프라인의 메모리 다리

## 의사결정 컨텍스트 (raw 인용)

> "Apache Arrow는 언어 횡단 인메모리 컬럼 포맷 표준. 둘이 합쳐 '디스크 → 메모리 → 네트워크'의 모든 데이터 이동에서 zero-copy 보장 — 2010년대 데이터 인프라의 가장 성공적인 표준화 프로젝트."
> — [[apache-arrow]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 컬럼 데이터 인메모리 표준. [[c2spf-analytics]] BigQuery → pandas/polars 변환 시 zero-copy 백엔드. **언어 횡단 표준**(11+ 언어)은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 ASF PMC 거버넌스 사례 — [[pandas]]·[[polars]]·[[duckdb]] 모두 디폴트 백엔드 채택. [[parquet]]과 함께 인메모리/온디스크 컬럼 표준 짝.

## 출처

- [[apache-arrow]] — apache/arrow + apache/parquet-format 통합 수집

## 논쟁/모순

> [!warning] 논쟁/모순
> - **Wheel 크기 ~80MB**: C++ 바이너리 동봉으로 Lambda/컨테이너에 무거움. `pyarrow-stubs` 같은 type-only 패키지로 분리 시도 있음
> - **NumPy 호환성 vs Arrow 모델**: pandas가 NumPy → PyArrow로 옮겨가는 과정에서 일부 NumPy-only 라이브러리 호환성 깨짐. PDEP-10 통과 시점이 분기점
> - **ADBC vs JDBC/ODBC**: ADBC는 분석 워크로드 최적이지만 transactional 워크로드에서 JDBC만큼 성숙하지 않음. 도입 시점 검토 필요
> - **Compute 함수 vs Polars**: PyArrow.compute는 200+ 함수, Polars는 더 많고 expression DSL 친화. 단순 변환은 PyArrow, 복잡 분석은 Polars


## 메모

- **회사 BI 적용**: [[c2spf-analytics]]에서 BigQuery storage API → PyArrow → pandas/Polars 파이프라인이 표준. ADBC 드라이버 채택 진행 시 변환 비용 추가 감소
- **PDEP-10 추적**: pandas의 PyArrow 1급 통합 진행도 — 통과 시 NumPy 의존 깨지고 import 빨라짐
- **Datasets API 학습**: 데이터 레이크 워크로드의 표준 Python 게이트웨이 — Hive 파티션, predicate pushdown 자동
- **IPC vs Parquet 트레이드오프**: 프로토타이핑은 IPC(Feather), 영속은 Parquet. CSV는 거의 사용 안 함 (Arrow 도입 후)
- **Gandiva JIT**: LLVM 기반 표현식 컴파일러. 운영 도입 시 컴파일 시간 vs 런타임 trade-off 검증
- **이름 표기**: "PyArrow" (CamelCase 공식), "pyarrow" (소문자, Python 패키지). 본 위키는 PyArrow 사용
- **후속 후보**: ADBC 별도 엔티티, Flight SQL 추적, Datasets API 패턴 정리
