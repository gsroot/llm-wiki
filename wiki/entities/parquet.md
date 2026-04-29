---
title: "Apache Parquet"
type: entity
entity_type: tool
tags: [parquet, columnar, on-disk, file-format, dremel, thrift, compression, encoding, hadoop, asf, big-data]
related:
  - "[[apache-arrow]]"
  - "[[pyarrow]]"
  - "[[duckdb]]"
  - "[[polars]]"
  - "[[pandas]]"
  - "[[apache-foundation]]"
  - "[[c2spf-analytics]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# Apache Parquet

## 개요

Apache Parquet은 **컬럼 지향 온디스크 데이터 파일 포맷 표준**. 2013년 Twitter + Cloudera가 시작, Hadoop 생태계 표준화 → 2015년 ASF Top-Level Project 승격. 2023년 Apache Arrow PMC와 통합 거버넌스. **Google Dremel 논문(2010)의 record shredding 알고리즘을 OSS로 추출**.

라이센스: **Apache 2.0**. 핵심 저장소: [apache/parquet-format](https://github.com/apache/parquet-format) (Thrift 명세) + [apache/parquet-java](https://github.com/apache/parquet-java) (참조 구현). 자매: [[apache-arrow]] (인메모리 표준).

## 주요 특징

### 4계층 구조

```
File
└── Row Group (수평 파티션, 보통 128MB~1GB)
    └── Column Chunk (컬럼별 연속 청크)
        └── Page (압축/인코딩 단위, 보통 1MB)
```

이 4계층이 Parquet의 모든 것.

### 병렬화 단위 (작업별 다름)

| 작업 | 단위 |
|------|------|
| MapReduce / Spark task | File / Row Group |
| Disk IO | Column Chunk |
| Encoding / Compression | Page |

→ 분산/단일 노드 모두에서 효율 극대화. 파일 = 컴퓨팅 단위, Row Group = 메모리 단위.

### File magic + Footer 패턴

```
[PAR1] ... [data] ... [Footer Metadata] [PAR1]
```

- 4바이트 매직 넘버 `PAR1` 시작 + 끝
- **Footer**가 파일 끝에 — `seek(size-N)` 후 읽기 표준
- 메타데이터만 빠르게 읽어 **컬럼 스킵 + 파티션 프루닝** 가능
- 큰 Parquet 파일도 결정 비용 낮음

### Encoding 시스템 (8개+)

| 인코딩 | 적합 |
|--------|------|
| **PLAIN** | 그냥 raw |
| **RLE / Bit-Packing** | 반복 / 작은 정수 |
| **Dictionary** | 저카디널리티 문자열 (URL, 사용자 ID) |
| **Delta-Binary-Packed** | 정렬된 정수 (timestamp) |
| **Delta-Length-Byte-Array** | 공통 prefix 문자열 |
| **Delta-Byte-Array** | 정렬된 문자열 |
| **Byte-Stream-Split** | 부동소수점 (IEEE 754 분할) |

**압축은 직교**: GZIP / Snappy / LZ4 / Zstd / Brotli 등. **인코딩 + 압축 = 4-10배 사이즈 절감 일반적**.

### Dremel 영향 — 중첩 데이터 1급 표현

[Google Dremel 논문(2010)](https://research.google/pubs/pub36632/)의 **record shredding and assembly**:
- struct/list/map 같은 중첩을 **컬럼 단위로 분해**
- Definition Level + Repetition Level 메타데이터로 재조립
- → JSON/XML 같은 중첩이 분석용 컬럼 스토어에 1급 표현

이것이 BigQuery의 백엔드 알고리즘과 동일.

### Thrift 명세

[parquet.thrift](https://github.com/apache/parquet-format/blob/master/src/main/thrift/parquet.thrift) 단일 파일에 모든 메타데이터 구조 정의:
- `FileMetaData`, `RowGroup`, `ColumnChunk`, `PageHeader`
- `Encoding`, `CompressionCodec` enum
- `Statistics`, `BloomFilter`, `ColumnIndex` (성능)

→ 명세가 Thrift 코드 = "코드가 곧 명세".

### 모듈 구조

| 저장소 | 역할 |
|--------|------|
| [parquet-format](https://github.com/apache/parquet-format) | Thrift 명세 + 표준 |
| [parquet-java](https://github.com/apache/parquet-java) | Java 참조 구현 (Hadoop, Spark) |
| [parquet-testing](https://github.com/apache/parquet-testing) | 언어 간 호환성 테스트 |
| [arrow-rs/parquet](https://github.com/apache/arrow-rs) | Rust 구현 (DataFusion, Polars) |
| pyarrow.parquet | Python 표준 reader/writer |

### 통계 및 인덱스

- **Statistics**: 컬럼별 min/max/null_count → predicate pushdown
- **Bloom Filter**: 멤버십 테스트 빠르게
- **Column Index**: row range별 통계 → 더 정밀한 pushdown
- **Page Index**: page 단위 row 시작 → row-level seek

→ "Parquet은 단순 파일이 아니라 인덱스가 내장된 분석 DB의 디스크 포맷".

## 라이센스 / 의존성

- **Apache 2.0**
- 명세 자체는 라이브러리 없음 — Thrift IDL만
- 구현: parquet-java (Hadoop/Spark 의존), arrow-rs (zero-deps Rust), pyarrow (C++ Arrow 의존)

## 관련 개념

- [[apache-arrow]]: 자매 표준. Arrow=인메모리, Parquet=온디스크. 단일 자료형 모델 공유
- [[lakehouse]]: Parquet + Iceberg/Delta/Hudi 메타데이터 = Lakehouse 아키텍처
- [[predicate-pushdown]]: Statistics + Bloom Filter + Column Index가 가능케 함
- [[dataframe]]: pandas/Polars의 표준 영속 포맷
- [[ml-ai]]: Feature store 표준 (Tecton/Feast)
- [[c2spf-analytics|c2spf 게임 데이터 BI]]: BigQuery 외부 export, Parquet 데이터 레이크 패턴

## 관련 엔티티

- [[apache-arrow]]: 같은 PMC 산하 (2023~). 인메모리/온디스크 짝
- [[pyarrow]]: Python 표준 Parquet reader/writer
- [[duckdb]]: `SELECT * FROM 'file.parquet'` 직접 쿼리. predicate pushdown 자동
- [[polars]]: `pl.scan_parquet()` lazy 읽기, predicate pushdown 자동
- [[pandas]]: `pd.read_parquet()` (PyArrow 백엔드)
- [[apache-foundation]]: 거버넌스 주체

## 의사결정 컨텍스트 (raw 인용)

> "Parquet은 온디스크 컬럼 포맷 표준. Apache Arrow(인메모리)와 합쳐 '디스크 → 메모리 → 네트워크'의 모든 데이터 이동에서 zero-copy 보장 — 2010년대 데이터 인프라의 가장 성공적인 표준화 프로젝트."
> — [[apache-arrow]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 온디스크 컬럼 포맷 표준. [[c2spf-analytics]] BigQuery 데이터 export 표준 + [[matechat|MateChat 사이드 프로젝트]] 분석 모듈 데이터 lake 후보. **Dremel 알고리즘 영감 + thrift 메타데이터**가 빅데이터 시대 사실상 표준. [[duckdb]] CSV/Parquet 직접 SELECT + [[polars]]·[[pyarrow]] 백엔드. [[pyarrow]]와 함께 인메모리/온디스크 컬럼 표준 짝.

## 출처

- [[apache-arrow]] — apache/parquet-format README + Encodings 명세 통합 수집

## 논쟁/모순

- **Compression vs Encoding 우선순위**: 인코딩이 먼저, 압축은 나중. Dictionary + Snappy 조합이 대부분에 최적이지만 데이터 분포 따라 다름
- **Footer 위치 = 스트리밍 어려움**: 파일 끝에 footer라 streaming write 시 buffering 필요. Iceberg가 metadata 별도로 분리하는 이유
- **Row Group 크기 선택**: 너무 작으면 메타데이터 오버헤드, 너무 크면 메모리 압박. 기본 128MB~1GB 권장
- **Apache vs proprietary 변종**: Snowflake/BigQuery 내부 포맷은 Parquet 변종이지만 호환 X. Iceberg/Delta가 표준 Parquet 위에 메타데이터를 더해 "vendor-neutral lakehouse" 시도

## 메모

- **회사 BI 적용**: [[c2spf-analytics]] BigQuery → GCS Parquet export 패턴 — 외부 도구(DuckDB/Polars) 분석 가능
- **인코딩 자동 선택**: parquet-java/pyarrow 모두 컬럼 자료형 분석 후 자동 선택. 수동 튜닝은 거의 불필요
- **Page-level seek = 강력**: row-level random access 가능. NoSQL 같은 워크로드도 부분 가능
- **Iceberg/Delta/Hudi 위 Parquet**: Parquet은 파일, 그 위 메타데이터 레이어가 "lakehouse 테이블 포맷". 별도 추적 가치
- **Bloom Filter 활용**: Equality predicate에 효과적. range/IN에는 Column Index가 더 적합
- **이름 표기**: "Apache Parquet" (공식), "Parquet" (일상). 본 위키는 둘 다 사용
- **Wes McKinney**: Arrow + Parquet의 Voltron Data 통합 거버넌스 발기인. 데이터 인프라 표준화의 인물
- **후속 후보**: `concepts/columnar-storage.md`, `concepts/predicate-pushdown.md`, Iceberg/Delta/Hudi 별도 엔티티
