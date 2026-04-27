.. _scale:

*************************
Scaling to large datasets
*************************

pandas provides data structures for in-memory analytics, which makes using pandas to analyze datasets that are
larger than memory somewhat tricky. Even datasets that are a sizable fraction of memory become unwieldy, as some
pandas operations need to make intermediate copies.

## Load less data

```python
columns = ["id_0", "name_0", "x_0", "y_0"]

# Option 1 (낭비): 전체 로드 후 필터
pd.read_parquet("timeseries_wide.parquet")[columns]

# Option 2 (권장): 컬럼만 읽기 — ~1/10 메모리
pd.read_parquet("timeseries_wide.parquet", columns=columns)
```

`pandas.read_csv`는 `usecols=`로 동일하게 컬럼 제한 가능.

## Use efficient datatypes

low-cardinality 텍스트 컬럼은 Categorical로 변환:

```python
ts2["name"] = ts2["name"].astype("category")
ts2["id"] = pd.to_numeric(ts2["id"], downcast="unsigned")
ts2[["x", "y"]] = ts2[["x", "y"]].apply(pd.to_numeric, downcast="float")
ts2.memory_usage(deep=True)
# → 원본 대비 ~1/5 메모리
```

## Use chunking

대용량 디렉터리 (예: 연도별 parquet)에서 out-of-core value_counts:

```python
files = glob.iglob(f"{tmpdir}/ts*.parquet")
counts = pd.Series(dtype=int)
for path in files:
    df = pd.read_parquet(path)
    counts = counts.add(df["name"].value_counts(), fill_value=0)
counts.astype(int)
```

`pandas.read_csv`는 `chunksize=`로 단일 파일 청킹 가능.

## Use Other Libraries

청크 협력이 어려운 워크로드(특히 `groupby`)는 다음으로:

> "There are other libraries which provide similar APIs to pandas and work nicely with pandas DataFrame, and can give
> you the ability to scale your large dataset processing and analytics by parallel runtime, distributed memory,
> clustering, etc."

→ ecosystem.md의 "Scaling pandas" 섹션 참조 (Bodo, BigQuery DataFrames, Dask, Ibis, Koalas, Modin)

---

원본: https://github.com/pandas-dev/pandas/blob/main/doc/source/user_guide/scale.rst
SHA: ab0f27734197d5eb56a18b8dbcc07777b855654f (size 7,311 bytes)
수집일: 2026-04-27
