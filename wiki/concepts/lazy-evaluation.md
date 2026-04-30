---
title: Lazy Evaluation (지연 평가)
aliases:
- Lazy Evaluation
- 지연 평가
- lazy-eval
type: concept
category: data
tags:
- lazy-evaluation
- query-optimization
- predicate-pushdown
- dataframe
- sql
- polars
- duckdb
related:
- '[[polars]]'
- '[[duckdb]]'
- '[[pandas]]'
- '[[apache-arrow]]'
- '[[copy-on-write]]'
- '[[dataframe]]'
- '[[pola-rs-polars]]'
- '[[duckdb-duckdb]]'
source_count: 2
observed_source_refs: 5
inbound_count: 15
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 9
---

# Lazy Evaluation (지연 평가)

## 정의

**Lazy Evaluation**(지연 평가)은 표현식의 실제 계산을 **그 결과가 정말 필요해지는 시점까지 미루는** 평가 전략이다. 데이터 분석 도구의 맥락에서는 "사용자가 작성한 모든 변환을 즉시 실행하지 않고, **계획(plan)으로 누적**한 후 한꺼번에 옵티마이저가 재배열·통합·푸시다운을 적용해 실행"하는 패턴을 의미한다.

**Eager Evaluation**(즉시 평가)의 정반대 — eager는 작성 즉시 실행, lazy는 `collect` / `compute` 같은 명시적 호출 시까지 미룸.

## 왜 중요한가

### 1. 성능 차이가 결정적

같은 코드를 lazy로 표현하면:
- **Predicate Pushdown**: WHERE 조건을 IO 단계로 내림 → 디스크에서 필요 행만 읽음
- **Projection Pushdown**: SELECT 컬럼을 IO 단계로 내림 → 필요 컬럼만 파싱
- **Common Subexpression Elimination (CSE)**: 같은 계산 한 번만
- **Slice Pushdown**: head/limit를 IO 단계로

→ 실측: 100GB CSV 중 5%만 필요한 쿼리에서 lazy가 eager 대비 **20-50배 빠름**.

### 2. 메모리 절약

중간 결과를 materialize하지 않음. eager에서 5단계 변환은 5개 중간 DataFrame을 메모리에 만들지만, lazy는 단일 plan을 한 번에 실행 → 피크 메모리 1/N.

### 3. Query Plan 시각화

`explain` / `EXPLAIN`으로 옵티마이저의 결정을 사람이 직접 볼 수 있음 → 디버깅·튜닝 가능. SQL DBA의 어휘를 DataFrame 사용자가 사용 가능.

## 핵심 내용

### 작동 원리 (4단계)

1. **Plan 누적**: 사용자 호출이 즉시 실행되지 않고 **AST/Logical Plan**으로 쌓임
2. **Logical Optimization**: 규칙 기반 변환 (predicate pushdown, projection pushdown, CSE, constant folding)
3. **Physical Plan**: 실행 가능한 연산 트리로 변환 (vectorized executor / streaming / parallel)
4. **Execution**: `collect` 호출 시 실제 IO + 계산 실행

### Polars의 Lazy API

```python
import polars as pl

# Lazy mode — 즉시 실행 안 됨
q = (
    pl.scan_csv("huge.csv")
    .filter(pl.col("date") >= "2024-01-01")
    .select(["user_id", "revenue"])
    .group_by("user_id")
    .agg(pl.col("revenue").sum)
)

# Plan 확인
print(q.explain)

# 이 시점에 비로소 IO + 계산
df = q.collect
```

### DuckDB의 Lazy via SQL

SQL 자체가 본질적으로 선언적·lazy. 옵티마이저가 자동으로:
- Filter pushdown
- Projection pushdown
- Join reordering
- Subquery unnesting

```sql
EXPLAIN SELECT user_id, SUM(revenue) 
FROM 'huge.parquet' 
WHERE date >= '2024-01-01' 
GROUP BY user_id;
```

### Pandas의 위치 — Eager 기본 + 일부 lazy

pandas는 본질적으로 eager. 하지만 일부 자료구조가 lazy:
- `pd.read_csv(chunksize=10000)` — iterator (streaming)
- PyArrow Datasets API (`ds.dataset(...)`) — predicate pushdown 가능

**한계**: 표현식 단위 lazy 부재. `df[df.A > 0]['B'].sum`이 두 번 materialize됨.

### Spark의 RDD/DataFrame Lazy

Apache Spark은 lazy의 산업 표준 사례:
- 모든 transformation(`.filter`, `.map`, `.groupBy`)이 lazy
- Action(`.show`, `.count`, `.collect`) 호출 시까지 실행 X
- Catalyst Optimizer가 SQL/DataFrame plan 통합 최적화

→ Polars/DuckDB는 Spark의 **노트북 사이즈 후예**.

### Lazy의 트레이드오프

| 장점 | 단점 |
|------|------|
| 옵티마이저 자동 적용 | 디버깅 어려움 (실행이 멀리 있음) |
| 메모리 효율 | API 학습 비용 (`scan_*` vs `read_*`) |
| Plan 시각화 | 일부 연산은 plan 안에서 표현 어려움 |
| Streaming 가능 | 사이드 이펙트(I/O, 로그) 시점이 불명확 |

## 실전 적용

### 시나리오 1: 100GB CSV에서 일부 분석

```python
# Eager (pandas) — 100GB 전체 메모리 필요
df = pd.read_csv("huge.csv")
filtered = df[(df.date >= "2024-01-01") & (df.region == "US")][["user_id", "revenue"]]
result = filtered.groupby("user_id").sum  # OOM 위험

# Lazy (polars) — predicate/projection이 IO 전에 적용
result = (
    pl.scan_csv("huge.csv")
    .filter((pl.col("date") >= "2024-01-01") & (pl.col("region") == "US"))
    .select(["user_id", "revenue"])
    .group_by("user_id")
    .agg(pl.col("revenue").sum)
    .collect  # 필요 행/컬럼만 디스크에서 읽음
)
```

### 시나리오 2: Plan 디버깅

```python
print(q.explain)
# WITH_COLUMNS:
#   AGGREGATE
#     SELECTION: ((col("date") >= "2024-01-01"))
#     PROJECT 2/15 columns  ← projection pushdown 적용됨
#       Csv SCAN huge.csv
```

### 시나리오 3: 회사 BI 적용 ([[c2spf-analytics|c2spf 게임 데이터 BI]])

BigQuery의 `EXPLAIN PLAN` + Polars `LazyFrame.explain` 결합 → 분석가가 SQL/DataFrame 양면에서 옵티마이저 결정 검증 가능. 비용 추정 → 쿼리 튜닝.

## 관련 개념

- [[copy-on-write]]: pandas의 eager 모델 보완. lazy는 그 자체로 CoW 문제를 회피
- [[dataframe]]: lazy/eager 듀얼 모델은 DataFrame 추상의 진화 방향
- [[predicate-pushdown]]: lazy의 가장 큰 이득 메커니즘
- [[query-optimization]]: SQL 옵티마이저 사상이 DataFrame 도구로 이식됨
- [[streaming]]: lazy + chunked execution = streaming 가능

## 출처

- [[pola-rs-polars]] — Polars의 Lazy API + Expression DSL + 4 컨텍스트 + `explain` 직접 학습
- [[duckdb-duckdb]] — SQL 기본 lazy + `EXPLAIN` 통합

## 열린 질문

- **Lazy를 학습한 분석가 vs eager 학습자의 멘탈 모델 차이**: 어느 쪽이 SQL DBA/데이터 엔지니어로 진화하기 쉬운가?
- **Pandas의 lazy 채택 가능성**: PDEP-10 이후 PyArrow Datasets 통합으로 부분 lazy. 완전 lazy DataFrame API는 PDEP 후보로 등장 가능?
- **Streaming engine 한계**: Polars streaming이 group_by/window 일부 미지원 — 표현식 단위 streaming 가능한 일반 모델은?
- **MotherDuck/Polars Cloud의 분산 lazy**: 단일 노드 lazy → 분산 lazy(Spark처럼)로 자연스럽게 확장? Polars Cloud 추적 가치
