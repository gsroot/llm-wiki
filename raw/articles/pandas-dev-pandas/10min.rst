.. _10min:

********************
10 minutes to pandas
********************

A short introduction to pandas, geared mainly for new users.

```python
import numpy as np
import pandas as pd
```

## Basic data structures

- :class:`Series`: 1D labeled array (any type)
- :class:`DataFrame`: 2D table (rows + columns)

## Object creation

```python
s = pd.Series([1, 3, 5, np.nan, 6, 8])

dates = pd.date_range("20130101", periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))

df2 = pd.DataFrame({
    "A": 1.0,
    "B": pd.Timestamp("20130102"),
    "C": pd.Series(1, index=list(range(4)), dtype="float32"),
    "D": np.array([3] * 4, dtype="int32"),
    "E": pd.Categorical(["test", "train", "test", "train"]),
    "F": "foo",
})
df2.dtypes  # 컬럼별 dtype
```

## Viewing data

```python
df.head()
df.tail(3)
df.index
df.columns
df.to_numpy()  # 주의: NumPy는 1 dtype/array, pandas는 1 dtype/column
df.describe()
df.T
df.sort_index(axis=1, ascending=False)
df.sort_values(by="B")
```

## Selection

권장: 프로덕션 코드에서는 `.at`, `.iat`, `.loc`, `.iloc` 사용.

### 라벨 선택 (loc, at)

```python
df.loc[dates[0]]
df.loc[:, ["A", "B"]]
df.loc["20130102":"20130104", ["A", "B"]]   # 양 끝 포함
df.at[dates[0], "A"]
```

### 위치 선택 (iloc, iat)

```python
df.iloc[3]
df.iloc[3:5, 0:2]
df.iloc[[1, 2, 4], [0, 2]]
df.iat[1, 1]
```

### Boolean indexing

```python
df[df["A"] > 0]
df[df > 0]
df2[df2["E"].isin(["two", "four"])]
```

## Missing data

```python
df1.dropna(how="any")
df1.fillna(value=5)
pd.isna(df1)
```

## Operations

```python
df.mean()
df.mean(axis=1)
df.sub(s, axis="index")

df.agg(lambda x: np.mean(x) * 5.6)
df.transform(lambda x: x * 101.2)

s.value_counts()
s.str.lower()
```

## Merge / Join

```python
pd.concat([df[:3], df[3:7], df[7:]])
pd.merge(left, right, on="key")
```

## Group by (split-apply-combine)

```python
df.groupby("A")[["C", "D"]].sum()
df.groupby(["A", "B"]).sum()
```

## Reshape

```python
stacked = df2.stack()
stacked.unstack()
stacked.unstack(1)
stacked.unstack(0)

pd.pivot_table(df, values="D", index=["A", "B"], columns=["C"])
```

## Time series (BI 직무 핵심)

```python
rng = pd.date_range("1/1/2012", periods=100, freq="s")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
ts.resample("5Min").sum()

rng = pd.date_range("3/6/2012 00:00", periods=5, freq="D")
ts_utc = ts.tz_localize("UTC")
ts_utc.tz_convert("US/Eastern")
rng + pd.offsets.BusinessDay(5)
```

## Categoricals

```python
df["grade"] = df["raw_grade"].astype("category")
df["grade"] = df["grade"].cat.rename_categories(new_categories)
df["grade"] = df["grade"].cat.set_categories(["very bad", "bad", "medium", "good", "very good"])
df.groupby("grade", observed=False).size()
```

## Plotting

```python
import matplotlib.pyplot as plt
ts.plot()
df.plot()
```

## I/O

```python
df.to_csv("foo.csv");      pd.read_csv("foo.csv")
df.to_parquet("foo.parquet"); pd.read_parquet("foo.parquet")
df.to_excel("foo.xlsx", sheet_name="Sheet1"); pd.read_excel("foo.xlsx", "Sheet1")
```

## Gotcha

```python
if pd.Series([False, True, False]):
    print("I was true")
# → ValueError: Truth value of a Series is ambiguous
```

---

원본: https://github.com/pandas-dev/pandas/blob/main/doc/source/user_guide/10min.rst
SHA: de44ec8787207a5e5032360071990c8703a5c70b (size 18,945 bytes)
수집일: 2026-04-27
