---
title: "DataFrame"
type: concept
category: data
tags: [dataframe, pandas, polars, dask, 데이터분석, 자료구조, tabular-data, data-analysis]
related:
  - "[[pandas]]"
  - "[[copy-on-write]]"
  - "[[ml-ai]]"
  - "[[data-pipeline-bigquery]]"
  - "[[pandas-dev-pandas]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# DataFrame

## 정의

**DataFrame**은 행(row)과 열(column)을 가진 2차원 레이블된 데이터 구조다. SQL 테이블이나 스프레드시트와 비슷하지만, 프로그램 안에서 인메모리로 조작·변환·집계할 수 있게 추상화된 객체다. 각 열은 서로 다른 데이터 타입을 가질 수 있고, 행/열 모두에 인덱스(레이블)가 붙는다.

## 왜 중요한가

- **데이터 분석의 보편적 추상**: 거의 모든 데이터 분석 도구가 "표(table) 모양의 데이터를 다루는 객체"를 중심으로 설계됨. R의 `data.frame`이 원형이고, [[pandas]]가 Python에 이식하면서 사실상 표준이 됨.
- **SQL과 코드 사이의 다리**: 데이터베이스의 행/열 의미론을 그대로 가져오면서, 프로그램 흐름 안에서 메서드 체이닝으로 변환을 표현 가능.
- **ML/AI 입력 형식의 사실상 표준**: scikit-learn, TensorFlow, PyTorch DataLoader가 모두 DataFrame 또는 NumPy 배열을 1급 입력으로 받음.

## 핵심 내용

### R에서 시작된 계보

- **1996**: R의 `data.frame` — 통계 분석을 위한 이질적 컬럼 테이블.
- **2008**: Wes McKinney가 [[pandas]] 시작. R의 추상을 Python 생태계에 이식.
- **2011~**: scikit-learn, statsmodels 등 ML/통계 라이브러리가 DataFrame을 입력으로 채택.
- **2020+**: Polars(Rust), Dask(분산), Ibis(SQL 백엔드) 등 차세대 구현체 등장.

### 핵심 연산

| 연산 종류 | 예시 (pandas 기준) |
|---|---|
| 선택 | `df['col']`, `df.loc[...]`, `df.iloc[...]` |
| 필터 | `df[df.col > 0]` |
| 집계 | `df.groupby('key').agg(...)` |
| 결합 | `df1.merge(df2, on=...)`, `pd.concat(...)` |
| 변형 | `df.pivot()`, `df.melt()`, `df.stack()` |
| 시계열 | `df.resample('D').mean()` |

### 구현체별 특징

- **pandas**: 사실상 표준. 단일 머신 인메모리. [[copy-on-write]] 도입으로 메모리 모델 현대화.
- **Polars**: Rust 기반, lazy evaluation, multi-threaded. pandas 대비 5~30배 빠름.
- **Dask**: 큰 데이터를 청크로 나눠 분산 처리. pandas API와 호환.
- **Ibis**: SQL 백엔드(BigQuery, DuckDB 등) 위에 DataFrame API를 얹음. [[data-pipeline-bigquery]]와 통합 가능.

## 실전 적용

```python
import pandas as pd

# 기본 사용
df = pd.DataFrame({
    "user_id": [1, 2, 3],
    "score": [85, 92, 78],
})

# 분석 파이프라인 (메서드 체이닝)
result = (
    df
    .query("score > 80")
    .assign(grade=lambda d: d['score'].apply(lambda s: 'A' if s >= 90 else 'B'))
    .groupby('grade')['score']
    .mean()
)
```

## 관련 개념

- [[pandas]]: DataFrame을 Python에 가져온 대표 라이브러리.
- [[copy-on-write]]: pandas 3.0의 DataFrame 메모리 모델.
- [[ml-ai]]: scikit-learn 등 ML 도구의 입력 형식이 DataFrame.
- [[data-pipeline-bigquery]]: BigQuery → DataFrame 변환이 BI 워크플로우의 핵심 연결고리.

## 출처

- [[pandas-dev-pandas]] — pandas 라이브러리 자체와 DataFrame 추상의 발전사

## 열린 질문

- DataFrame 추상은 결국 SQL의 재현인가, 아니면 SQL을 넘어서는가? lazy evaluation·columnar 백엔드 시대에 DataFrame과 SQL의 경계는 어디서 무너지는가?
- 분산 환경([[devops-cicd]]/대규모 데이터 처리)에서 DataFrame API가 어디까지 성립하는가? Spark DataFrame과 pandas DataFrame의 의미론 차이.
