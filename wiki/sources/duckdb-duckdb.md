---
title: "duckdb/duckdb (DuckDB 저장소)"
type: source
source_type: article
source_url: "https://github.com/duckdb/duckdb"
raw_path: "raw/articles/duckdb-duckdb/"
author: "duckdb 개발팀 (Hannes Mühleisen + Mark Raasveldt + DuckDB Labs)"
date_published: 2018-06-26
date_ingested: 2026-04-28
tags: [duckdb, embedded, sql, analytical, columnar, vectorized, in-process, MIT-license, c++17, cmake]
related:
  - "[[duckdb]]"
  - "[[postgresql]]"
  - "[[pandas]]"
  - "[[polars]]"
  - "[[pyarrow]]"
  - "[[parquet]]"
  - "[[sqlite]]"
confidence: high
cited_by:
  - "[[dataframe-ecosystem-evolution]]"
  - "[[duckdb]]"
  - "[[lakehouse]]"
  - "[[lazy-evaluation]]"
  - "[[oss-saas-dual]]"
  - "[[pandas-vs-polars-vs-duckdb]]"
  - "[[predicate-pushdown]]"
  - "[[query-optimization]]"
  - "[[sqlite]]"
  - "[[streaming]]"
  - "[[zero-copy]]"
---

# duckdb/duckdb (DuckDB 저장소)

## 한줄 요약

> DuckDB는 "분석용 SQLite" — 단일 바이너리·임베디드·인프로세스 OLAP 데이터베이스. **풍부한 SQL 방언**과 **CSV/Parquet 직접 SELECT** 두 가지 결정으로 데이터 분석 워크플로우를 데이터베이스 경험으로 끌어왔다.

## 핵심 내용

### 정체성 (README)

*"DuckDB is a high-performance analytical database system. It is designed to be fast, reliable, portable, and easy to use."* — 4축 (speed, reliability, portability, ease) 명시. SQLite와 같은 "임베디드" 위치이지만 OLTP 대신 **OLAP** 특화.

### 핵심 결정 1: SQL 방언 풍부

기본 SQL을 **훨씬** 넘어서는 기능:
- 임의 + 중첩 correlated subqueries
- Window functions
- Collations
- Complex types: arrays, structs, maps
- "Friendly SQL" 확장 (`SELECT * EXCLUDE (...)`, `GROUP BY ALL`, `SELECT * RENAME (...)`, list comprehension)

→ pandas/Polars 사용자가 SQL로 돌아오게 하는 결정적 설계.

### 핵심 결정 2: 파일을 직접 FROM에 사용

```sql
SELECT * FROM 'myfile.csv';
SELECT * FROM 'myfile.parquet';
```

`COPY ... FROM`이나 `CREATE EXTERNAL TABLE` 없이 즉시 작동. **파일 = 테이블** 패러다임 — 분석가 워크플로우 친화. CSV/Parquet/JSON/Excel 자동 인식.

### 다언어 클라이언트

CLI (standalone), Python, R, Java, Wasm, etc. 각 언어에서 **인프로세스**로 실행:
- Python: `import duckdb; duckdb.sql(...)` 또는 pandas/Polars/Arrow 직접 호환
- R: `dplyr` API (`duckplyr`)
- Wasm: 브라우저에서 직접 SQL 분석 가능

### 통합 깊이

- **pandas**: `duckdb.sql("SELECT * FROM df")` — Python local 변수 자동 인식
- **dplyr**: `duckplyr` lazy/eager 양방향
- **Apache Arrow**: zero-copy 변환 — Polars↔DuckDB 무손실 교환

### 빌드 시스템

- **C++17** 컴파일러 + **CMake** + **Python 3** (빌드용)
- `make` (release), `make debug`, `make unit`, `make allunit`
- `BUILD_BENCHMARK=1 BUILD_TPCH=1 make` — TPC-H 벤치마크 통합 지원
- Build Guide + Contribution Guide가 각각 별도 페이지로 존재

### CONTRIBUTING.md (132줄, 풍부)

CONTRIBUTING.md가 README보다 길다 (132 > 51줄) — 컨트리뷰션 게이트키핑이 진지함. clang-format/clang-tidy 자동 검증, sanitizer 설정 (`.sanitizer-leak-suppressions.txt`, `.sanitizer-thread-suppressions.txt`).

### SECURITY.md 별도 존재

보안 advisory 채널 정리. 임베디드 DB로서 신뢰성 진지함의 시그널.

### 운영 모델: DuckDB Labs

README가 명시적으로 [duckdblabs.com/support](https://duckdblabs.com/support/)와 [endoflife.date/duckdb](https://endoflife.date/duckdb) 링크 — 공식 LTS 정책과 상용 지원이 별도 법인. **OSS 본체 + 상용 지원** 모델 ([[postgresql]] EnterpriseDB, [[redis]] Redis Inc, [[polars]] Polars Cloud와 동일 패턴).

## 주요 인사이트

### 1. "SQLite for OLAP" 포지셔닝의 의미

SQLite는 OLTP/임베디드의 사실상 표준. DuckDB는 **OLAP/임베디드라는 미발견 슬롯**을 차지함:

| 축 | OLTP | OLAP |
|----|------|------|
| 임베디드 | SQLite | **DuckDB** |
| 서버 | [[postgresql]] | ClickHouse / BigQuery / Snowflake |

이 사분면이 비어있던 이유는 OLAP은 보통 분산/원격이라는 가정 — DuckDB가 "노트북에서 1억 행 분석"을 1초 안에 해내자 가정이 깨짐.

### 2. 파일을 테이블처럼 — Lakehouse Lite

`SELECT * FROM 's3://bucket/*.parquet'` 같은 패턴이 DuckDB만으로 가능 → 별도 Spark/Trino 없이 단일 노트북에서 데이터 레이크 직접 쿼리. **MotherDuck**(DuckDB Labs의 SaaS)이 이를 클라우드로 확장.

### 3. Polars와의 관계: 경쟁 아닌 상호 보완

- Polars: DataFrame DSL + Lazy + Streaming
- DuckDB: SQL + 풍부한 OLAP 기능 + 영구 저장소
- 둘 다 [[apache-arrow]] 위에서 zero-copy 교환 가능 → "Polars로 ETL → DuckDB에 영구 저장 → SQL 분석" 워크플로우가 자연스러움

### 4. SQL을 데이터 분석으로 되돌림

pandas/Polars의 메소드 체이닝은 강력하지만, **SQL은 선언적이고 옵티마이저 친화적**. DuckDB는 SQL을 잃었던 분석가에게 다시 가져오면서 동시에 "Friendly SQL" 확장으로 반복 작성 줄임. → BI 도구 직접 연결도 자연스러움.

### 5. Wasm 클라이언트 — 브라우저 내부 분석

DuckDB-Wasm은 데이터를 서버로 보내지 않고 브라우저에서 직접 SQL 분석 → 데이터 프라이버시 + 즉각적 인터랙티비티. Observable, Hex 등 노트북 도구가 채택.

## 관련 엔티티/개념

- [[duckdb]]: 본 소스의 메인 엔티티
- [[postgresql]]: 같은 SQL 진영, 정반대 워크로드 (OLTP vs OLAP). DuckDB가 PG 대비 분석 쿼리 100x+ 빠름
- [[polars]]: Apache Arrow 위에서 zero-copy 교환 가능한 자매 도구
- [[pandas]]: `duckdb.sql("SELECT * FROM df")` 직접 통합으로 마이그레이션 비용 거의 0
- [[pyarrow]]: 메모리 표현 표준, DuckDB Python 클라이언트의 zero-copy 다리
- [[parquet]]: `SELECT * FROM 'file.parquet'`로 직접 쿼리 가능 — 가장 자주 사용되는 입력 포맷
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 회사 BI에서 BigQuery 외부 캐시/탐색 도구로 후보

## 인용할 만한 구절

> "DuckDB is a high-performance analytical database system. It is designed to be fast, reliable, portable, and easy to use."
> — README.md (18줄)

> "For CSV files and Parquet files, data import is as simple as referencing the file in the FROM clause"
> — README.md (30줄)

## 메모

- **MotherDuck**: DuckDB Labs의 클라우드 SaaS. "DuckDB + 협업/지속성/공유" 추가 — 추적 대상
- **회사 BI 적용**: [[c2spf-analytics]]에서 BigQuery 비용 절감 워크로드 후보 — "탐색은 DuckDB on local Parquet으로, 운영은 BQ로" 분리
- **C++17 + CMake**: [[redis]]/[[postgresql]]의 C에 비하면 모던. 컨트리뷰션 진입장벽이 비교적 낮음
- **Python 통합 깊이**: pandas/polars/pyarrow를 모두 zero-copy 인식 — 데이터 사이언스 스택의 "허브" 역할
- **CHANGELOG 부재**: 루트에 CHANGELOG.md 없음 → 릴리스 노트는 GitHub Releases + duckdb.org/news로 분산. 추적 채널 명시 필요
