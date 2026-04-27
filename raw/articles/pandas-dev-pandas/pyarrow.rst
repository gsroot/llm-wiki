.. _pyarrow:

*********************
PyArrow Functionality
*********************

pandas can utilize PyArrow to extend functionality and improve the performance of various APIs. This includes:

- 더 광범위한 데이터 타입 (NumPy 대비)
- 모든 데이터 타입에 대한 결측(NA) 지원
- 고성능 IO 리더 통합
- Apache Arrow 사양 기반 다른 데이터프레임 라이브러리(polars, cuDF)와의 상호운용성

## Data Structure Integration

```python
ser = pd.Series([-1.5, 0.2, None], dtype="float32[pyarrow]")
idx = pd.Index([True, None], dtype="bool[pyarrow]")
df = pd.DataFrame([[1, 2], [3, 4]], dtype="uint64[pyarrow]")
```

주의: `"string[pyarrow]"` ≠ `pd.ArrowDtype(pa.string())`.
- `pd.StringDtype("pyarrow")`는 NumPy-backed nullable types 반환 가능
- `pd.ArrowDtype(pa.string())`는 ArrowDtype 반환

매개변수가 있는 PyArrow 타입:

```python
import pyarrow as pa
list_str_type = pa.list_(pa.string())
ser = pd.Series([["hello"], ["there"]], dtype=pd.ArrowDtype(list_str_type))

decimal_type = pd.ArrowDtype(pa.decimal128(3, scale=2))
df = pd.DataFrame([[Decimal("3.19"), None], [None, Decimal("-1.23")]], dtype=decimal_type)
```

PyArrow Table → DataFrame:

```python
df = table.to_pandas(types_mapper=pd.ArrowDtype)
```

## Operations (PyArrow compute로 가속)

- Numeric aggregations / arithmetic / rounding
- Logical and comparison functions
- String functionality (`str.startswith`, etc.)
- Datetime functionality (`dt.strftime`)

## I/O Reading

엔진을 PyArrow로 디스패치할 수 있는 함수:

- `read_csv` (`engine="pyarrow"`)
- `read_feather`
- `read_json`
- `read_orc`
- `read_parquet`
- `read_table` (experimental)

PyArrow-backed 데이터 반환은 `dtype_backend="pyarrow"` 매개변수로:

```python
df_pyarrow = pd.read_csv(data, dtype_backend="pyarrow")
df_pyarrow.dtypes
```

`dtype_backend`를 지원하는 비-IO 함수: `to_numeric`, `DataFrame.convert_dtypes`, `Series.convert_dtypes`.

---

원본: https://github.com/pandas-dev/pandas/blob/main/doc/source/user_guide/pyarrow.rst
SHA: 1807341530e698c8cbfb19a6ced347bdaaa1998b (size 6,425 bytes)
수집일: 2026-04-27 (PDEP-10 "Required pyarrow dependency"와 직결)
