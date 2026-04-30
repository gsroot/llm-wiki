---
title: apache/arrow + apache/parquet-format (Arrow + Parquet 명세)
type: source
source_type: article
source_url: https://github.com/apache/arrow
raw_path: raw/articles/apache-arrow/
author: Apache Software Foundation (Wes McKinney 발기, Arrow PMC)
date_published: 2016-02-17
date_ingested: 2026-04-28
tags:
- apache-arrow
- pyarrow
- parquet
- columnar
- in-memory
- ipc
- zero-copy
- asf
- dremel
related:
- '[[pyarrow]]'
- '[[parquet]]'
- '[[pandas]]'
- '[[polars]]'
- '[[duckdb]]'
- '[[apache-foundation]]'
confidence: high
inbound_count: 50
cited_by:
- '[[apache-foundation]]'
- '[[append-only-log]]'
- '[[c2spf-analytics]]'
- '[[copy-on-write]]'
- '[[dataframe-ecosystem-evolution]]'
- '[[duckdb]]'
- '[[duckdb-duckdb]]'
- '[[kafka]]'
- '[[lakehouse]]'
- '[[lazy-evaluation]]'
- '[[lightgbm]]'
- '[[microsoft-lightgbm]]'
- '[[pandas-vs-polars-vs-duckdb]]'
- '[[parquet]]'
- '[[pola-rs-polars]]'
- '[[polars]]'
- '[[predicate-pushdown]]'
- '[[pyarrow]]'
- '[[zero-copy]]'
cited_by_count: 19
aliases:
- Apache Arrow
- apache arrow
- apache/arrow + apache/parquet-format
- apache/arrow + apache/parquet-format (Arrow + Parquet 명세)
---

# apache/arrow + apache/parquet-format

## 한줄 요약

> Apache Arrow는 **언어 횡단 인메모리 컬럼 포맷 표준**, Parquet은 **온디스크 컬럼 포맷 표준**. 둘이 합쳐 "디스크 → 메모리 → 네트워크"의 모든 데이터 이동에서 zero-copy 보장 — 2010년대 데이터 인프라의 가장 성공적인 표준화 프로젝트.

## 핵심 내용

### 두 저장소의 관계

| 항목 | apache/arrow | apache/parquet-format |
|------|-------------|----------------------|
| 위치 | 인메모리 표현 | 온디스크 표현 |
| 본체 | C++/Python/Java/Go/...11+ 구현 | Thrift 명세 + 참조 구현 (parquet-java) |
| 자매 저장소 | arrow-rs, arrow-go, arrow-java 별도 | parquet-java, parquet-testing 별도 |
| 라이센스 | Apache 2.0 | Apache 2.0 |
| 거버넌스 | Apache Software Foundation PMC | 동일 PMC (Arrow 산하로 통합됨, 2023~) |

→ **단일 컬럼 포맷이 메모리·디스크 양면에서 표준이 됨**. 데이터 인프라 역사상 드문 통합.

### Arrow의 5대 컴포넌트

1. **Columnar Format**: 표준 인메모리 표현 (자료형, 중첩, null bitmap, offset 모두 명세)
2. **IPC Format**: Arrow 데이터 + 메타데이터의 직렬화 (프로세스 간/이기종 환경 통신)
3. **ADBC** (Arrow Database Connectivity): JDBC/ODBC의 Arrow 버전 — DB 결과를 Arrow로 직접 받음
4. **Flight RPC**: Arrow IPC + gRPC = 분산 데이터 서비스 빌딩 블록
5. **Gandiva**: LLVM 기반 표현식 컴파일러 — Arrow 위에서 SQL/표현식을 JIT 컴파일

### 11+ 언어 구현 매트릭스

C++, GLib, .NET (별도), Go (별도), Java (별도), JavaScript (별도), Julia (별도), Python, R, Ruby, Rust (별도), Swift (별도). `↗` 마커는 별도 저장소로 분리됨 — Arrow 사이즈가 너무 커서 monorepo에서 split됨.

### Format/ 디렉토리 = 명세 그 자체

- `Schema.fbs` (571줄): Arrow의 핵심 자료형 정의 — FlatBuffers IDL
- `Message.fbs`, `File.fbs`, `Tensor.fbs`, `SparseTensor.fbs`: 각각 메시지/파일/텐서 IDL
- `Flight.proto`, `FlightSql.proto`: gRPC 프로토콜
- 명세를 **FlatBuffers + Protocol Buffers IDL로 직접 표현** — "코드가 곧 명세".

### Parquet 명세 (parquet-format)

#### 핵심 계층 구조

```
File
└── Row Group (수평 파티션)
    └── Column Chunk (컬럼별 연속 청크)
        └── Page (압축/인코딩 단위)
```

이 4계층이 Parquet의 모든 것.

#### 병렬화 단위

| 작업 | 단위 |
|------|------|
| MapReduce | File / Row Group |
| IO | Column Chunk |
| Encoding/Compression | Page |

→ 작업 종류별로 다른 병렬화 단위. 분산/단일 노드 모두에서 효율 극대화.

#### Dremel 영향

[Google Dremel 논문(2010)](https://github.com/julienledem/redelm/wiki/The-striping-and-assembly-algorithms-from-the-Dremel-paper)의 **record shredding and assembly** 알고리즘을 직접 채택. 중첩 데이터(struct, list, map)를 컬럼 단위로 분해/재조립 → JSON/XML 같은 중첩을 분석용 컬럼 스토어에 1급 표현.

#### File magic + Footer

`PAR1` (4바이트 매직 넘버) + 파일 끝 메타데이터 footer → "파일 끝부터 읽기" 패턴이 표준. 큰 Parquet 파일도 메타데이터만 빠르게 읽어 **컬럼 스킵 + 파티션 프루닝** 가능.

#### Encoding 시스템 (Encodings.md, 393줄)

PLAIN, RLE/Bit-Packing, Dictionary, Delta-Binary-Packed, Delta-Length-Byte-Array, Delta-Byte-Array, Byte-Stream-Split — 컬럼 자료형/분포에 따라 인코딩 자동 선택. 압축(GZIP/Snappy/LZ4/Zstd)과 직교.

### IPC Format = "프로세스 간 zero-copy"

Arrow 메모리 표현을 그대로 직렬화 → 수신측이 zero-copy로 매핑. shared memory, mmap, gRPC 모두 지원. → Polars/DuckDB/pandas 사이의 데이터 교환이 메모리 복사 없이 가능.

## 주요 인사이트

### 1. "메모리 표준 = 디스크 표준" 통합의 의미

이전 세대(HDF5, Avro, ORC, CSV)는 디스크 포맷이고, 메모리는 각 언어마다 자유. Arrow + Parquet은 **단일 자료형 모델**을 메모리·디스크에 모두 적용 → IO에서 변환 비용 사라짐. 이것이 [[polars]]/[[duckdb]]가 **GB/s 수준 IO 처리량**을 내는 근본 이유.

### 2. PMC 거버넌스 = 8번째 OSS 거버넌스 모델

[[backend-fastapi-stack]]에서 7개 거버넌스 모델 발견 → Apache Software Foundation의 **PMC (Project Management Committee)** 모델은 8번째. 메일링 리스트 + JIRA + Confluence + Apache Way (sustainability + diversity + code of conduct) 4축. [[postgresql]] 메일링 리스트와 다른 점은 ASF의 공식 인큐베이션 절차.

### 3. Dremel 논문의 산업 표준화 사례

Google Dremel(2010)은 BigQuery의 백엔드 — 폐쇄형. 그 알고리즘을 OSS로 추출 → Parquet → BigQuery 외부에서도 Dremel 병렬화 가능. 학술 → 산업 → OSS 패턴의 정공법 사례.

### 4. ADBC = JDBC의 Arrow 시대 후속

JDBC/ODBC는 행 단위 결과 → 분석 워크로드에서 컬럼 변환 비용. ADBC는 결과를 처음부터 Arrow로 → DB ↔ Polars/DuckDB/pandas 사이 변환 비용 0. PostgreSQL/SQLite 등이 ADBC 드라이버 채택 진행 중.

### 5. 11+ 언어 = 단일 표준의 가치

Arrow를 채택한 도구는 자동으로 모든 다른 Arrow 도구와 호환. → 데이터 인프라 lock-in 감소. 같은 패턴으로 [[redis]] RESP, HTTP, JSON이 표준화 효과를 만듦.

## 관련 엔티티/개념

- [[pyarrow]]: Arrow의 Python 바인딩 — pandas/Polars/DuckDB의 다리
- [[parquet]]: 자매 표준 (디스크 컬럼 포맷)
- [[pandas]]: PyArrow 백엔드(`dtype_backend="pyarrow"`)로 점진적 통합. PDEP-10 통과 시 1급 모델
- [[polars]]: Arrow를 in-memory 표현으로 직접 사용. zero-copy 제로
- [[duckdb]]: Arrow zero-copy 통합 + Parquet 직접 SELECT
- [[apache-foundation]]: 거버넌스 주체 (별도 엔티티 후보)
- [[copy-on-write]]: Arrow의 immutable 모델은 CoW와 정반대 — 한 번 만든 버퍼 read-only

## 인용할 만한 구절

> "Apache Arrow is a universal columnar format and multi-language toolbox for fast data interchange and in-memory analytics."
> — apache/arrow README.md (28-30줄)

> "Apache Parquet is an open source, column-oriented data file format designed for efficient data storage and retrieval."
> — apache/parquet-format README.md (25-27줄)

> "We created Parquet to make the advantages of compressed, efficient columnar data representation available to any project in the Hadoop ecosystem."
> — apache/parquet-format README.md (35-36줄)

## 메모

- **PyArrow는 별도 엔티티 페이지**: Arrow는 표준/조직, PyArrow는 도구 — 분리해서 관리
- **arrow-rs / arrow-go 별도 저장소**: 단일 ASF 우산 아래지만 monorepo split — 본 저장소만 수집, 향후 별도 수집 후보
- **Flight SQL = ADBC 백본**: Snowflake/BigQuery가 Flight SQL 채택 검토 진행 중. 채택 시 데이터 웨어하우스 ↔ 분석 도구 lock-in 추가 감소
- **Gandiva**: LLVM JIT 컴파일러 — DuckDB의 vectorized executor와 다른 접근. Arrow 위에서 표현식을 JIT.
- **회사 BI**: [[c2spf-analytics|c2spf 게임 데이터 BI]] BigQuery 결과를 Arrow IPC로 받아 Polars/DuckDB로 추가 분석하는 워크플로우 가능. ADBC 드라이버 채택 시 자동 활성화
- **Wes McKinney**: pandas → Apache Arrow → Voltron Data로 이어진 커리어. DataFrame 추상의 "재발명자"
