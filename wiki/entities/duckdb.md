---
title: "DuckDB"
aliases: [DuckDB, 덕디비, duck-db]
type: entity
entity_type: tool
tags: [duckdb, embedded, sql, analytical, columnar, vectorized, in-process, MIT-license, c++17, olap, sqlite-for-olap, motherduck]
related:
  - "[[postgresql]]"
  - "[[pandas]]"
  - "[[polars]]"
  - "[[pyarrow]]"
  - "[[apache-arrow]]"
  - "[[parquet]]"
  - "[[c2spf-analytics]]"
  - "[[duckdb-duckdb]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 14
inbound_count: 79
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 29
---

# DuckDB

## 개요

DuckDB는 **인프로세스 임베디드 OLAP 데이터베이스** — "분석용 [[sqlite|SQLite]]"로 자주 표현된다. 2018년 Hannes Mühleisen + Mark Raasveldt(네덜란드 CWI)가 시작, 2024년 v1.0, 2026년 v1.x stable. **단일 바이너리, 서버 없음, SQL OLAP**이라는 미발견 슬롯을 차지한 도구.

라이센스: **MIT**. 거버넌스: DuckDB Foundation + DuckDB Labs(상용 지원/MotherDuck SaaS) 이중. C++17 + CMake.

## 주요 특징

### 위치: OLAP × Embedded 사분면

| 축 | OLTP | OLAP |
|----|------|------|
| 임베디드 | [[sqlite|SQLite]] | **DuckDB** |
| 서버 | [[postgresql]] | ClickHouse / BigQuery / Snowflake |

이 사분면이 비어있던 이유: OLAP은 보통 분산/원격이라는 가정. DuckDB가 노트북에서 1억 행 분석을 1초 안에 해내자 가정이 깨짐.

### 풍부한 SQL 방언

기본 SQL을 훨씬 넘어서:
- 임의 + 중첩 correlated subqueries
- Window functions (ROWS/RANGE/GROUPS)
- Complex types: arrays, structs, maps
- "Friendly SQL": `SELECT * EXCLUDE (...)`, `GROUP BY ALL`, `SELECT * RENAME (...)`, list comprehension `[x*2 for x in arr]`

→ pandas/Polars 사용자가 SQL로 돌아올 결정적 인센티브.

### 파일 = 테이블

```sql
-- 즉시 작동, COPY/CREATE EXTERNAL TABLE 불필요
SELECT * FROM 'data.csv';
SELECT * FROM 'data.parquet';
SELECT * FROM 's3://bucket/*.parquet';
SELECT * FROM 'data.json';
```

→ **Lakehouse Lite** 패턴. Spark/Trino 없이 단일 노트북에서 데이터 레이크 직접 쿼리.

### 다언어 클라이언트 (인프로세스)

| 언어 | 호출 | 특징 |
|------|------|------|
| Python | `import duckdb; duckdb.sql(...)` | pandas/Polars/Arrow zero-copy 자동 인식 |
| R | `duckplyr` | dplyr API, lazy/eager |
| Java | JDBC | JVM 통합 |
| Wasm | 브라우저 내부 | Observable/Hex 채택 |
| CLI | `duckdb mydb.db` | 단일 바이너리 |

### 통합 깊이 — "데이터 사이언스 허브"

- **pandas**: `duckdb.sql("SELECT * FROM df")` — Python local 변수 자동 인식. 마법
- **Polars**: Arrow zero-copy. `duckdb.sql("...").pl()` ↔ `polars_df.to_pandas()` 무비용
- **Apache Arrow**: 1급 시민. ADBC 드라이버 자체 지원
- **Parquet**: 직접 SELECT, Predicate Pushdown, 스트리밍 읽기

### Vectorized Executor

DuckDB의 핵심 성능 기둥. 한 번에 1024개 행씩 처리(vector size) → CPU SIMD + 캐시 효율 극대화. [[polars]]가 같은 모델 채택.

### 빌드 시스템

- **C++17** 컴파일러 + **CMake** + **Python 3** (빌드용)
- `make` (release) / `make debug` / `make unit`
- `BUILD_BENCHMARK=1 BUILD_TPCH=1 make` — TPC-H 통합
- CONTRIBUTING.md (132줄) > README.md (51줄) — 컨트리뷰션 게이트키핑 진지함
- sanitizer 설정 (`.sanitizer-leak-suppressions.txt`) — 임베디드 DB 신뢰성 시그널

### 운영: DuckDB Foundation + Labs + MotherDuck

| 주체 | 역할 |
|------|------|
| **DuckDB Foundation** | 비영리 거버넌스, OSS 본체 |
| **DuckDB Labs** | 상용 지원, LTS 정책 |
| **MotherDuck** | DuckDB Labs의 클라우드 SaaS — 협업/지속성/공유 |

→ [[postgresql]] EnterpriseDB, [[redis]] Inc, [[polars]] Polars Cloud와 동일 패턴 (OSS + 상용 회사).

## 라이센스 / 의존성

- **MIT** (관대한 OSS)
- 의존성: 사실상 zero (자체 포함 라이브러리). 단일 바이너리 ~30MB
- 확장: 별도 모듈 시스템 (`INSTALL httpfs`, `INSTALL parquet`, `INSTALL postgres_scanner`)

## 관련 개념

- [[apache-arrow]]: zero-copy 통합 표준. ADBC 드라이버
- [[parquet]]: 직접 SELECT 가능한 1급 입력 포맷
- [[lazy-evaluation]]: SQL 옵티마이저 자체가 lazy
- [[dataframe]]: pandas/Polars DataFrame을 SQL 테이블로 자동 인식
- [[ml-ai]]: ML 피처 엔지니어링을 SQL로 표현 → 재현성 + 옵티마이저 자동 적용
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: BigQuery 비용 절감 워크로드 후보

## 관련 엔티티

- [[postgresql]]: SQL 진영 자매. 정반대 워크로드(OLTP vs OLAP). PG_scanner extension으로 직접 연결
- [[polars]]: 같은 정체성("쿼리 엔진"). DuckDB=SQL, Polars=DataFrame DSL. Arrow zero-copy로 상호 보완
- [[pandas]]: 직접 통합 — `duckdb.sql("SELECT * FROM df")`. 마이그레이션 0
- [[pyarrow]]: 메모리 표현 다리. ADBC 드라이버
- [[parquet]]: 입력/출력 1급 포맷
- [[fastapi]]: BI API 백엔드로 PG 대신 DuckDB가 적합한 read-heavy 분석 워크로드
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: 잠재 채택자

## 의사결정 컨텍스트 (raw 인용)

> "DuckDB는 '분석용 SQLite' — 단일 바이너리·임베디드·인프로세스 OLAP 데이터베이스. 풍부한 SQL 방언과 CSV/Parquet 직접 SELECT 두 가지 결정으로 데이터 분석 워크플로우를 데이터베이스 경험으로 끌어왔다."
> — [[duckdb-duckdb]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 임베디드 OLAP 영역. [[matechat|MateChat 사이드 프로젝트]] 사이드 프로젝트의 SQLite 분석 본진 + [[c2spf-analytics]] BigQuery 보완 (오프라인/임베디드 분석 시). [[pandas]]·[[polars]]와 [[pandas-vs-polars-vs-duckdb]] 결정 매트릭스에서 함께 평가. **CSV/Parquet 직접 SELECT** 패턴은 파일 = 테이블 패러다임의 대표 사례 — [[apache-arrow]]·[[parquet]]과 함께 컬럼 표준 진영의 한 축.

## 출처

- [[duckdb-duckdb]] — duckdb/duckdb GitHub 저장소 (README + CONTRIBUTING + SECURITY 통합 수집)

## 논쟁/모순

> [!warning] 논쟁/모순
> - **단일 작성자 동시성**: 동시 쓰기 1개만 허용. 멀티프로세스 쓰기는 lock 충돌 → OLAP 임베디드의 트레이드오프, 의도된 디자인
> - **메모리 한계**: in-process이므로 Python heap에 종속. 100GB+ 데이터셋은 streaming/외부 디스크 사용 필수
> - **MotherDuck = SaaS 의존성**: OSS 본체 vs MotherDuck 기능 차이 추적 필요. 라이센스는 본체 MIT 유지
> - **PostgreSQL과의 경쟁/보완**: BI 도구가 PG에서 DuckDB로 옮겨가는 사례 vs PG의 분석 확장(citus, timescaledb)으로 대응. 사분면이 흐려지는 중


## 메모

- **회사 BI 적용 가설**: [[c2spf-analytics]] BigQuery 비용 절감:
  - "탐색은 DuckDB on local Parquet, 운영은 BQ" 분리
  - DuckDB → BigQuery FDW (`postgres_scanner`처럼 `bq_scanner` 가능성)
  - 단점: 데이터 지속성 단일 노드, 협업은 MotherDuck 필요 (SaaS 비용)
- **CHANGELOG 부재**: GitHub Releases + duckdb.org/news로 분산. 추적 시 RSS 또는 Watch
- **C++17 + CMake**: [[redis]]/[[postgresql]] C에 비하면 모던. 컨트리뷰션 진입장벽 비교적 낮음
- **Wasm 클라이언트**: Observable/Hex/Quarto가 채택. 데이터 프라이버시 + 즉각 인터랙티비티
- **이름 표기**: "DuckDB" (CamelCase, 회사 + 제품), "duckdb" (소문자, CLI/Python 패키지/Cargo crate)
- **Hannes Mühleisen + Mark Raasveldt**: CWI(네덜란드 컴퓨팅 연구소) 출신. 학술 → 산업 OSS 전환 사례
- **후속 후보**: `concepts/embedded-database.md`, `concepts/lazy-evaluation.md`, MotherDuck 별도 추적
