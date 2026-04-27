.. _install:

============
Installation
============

The pandas development team officially distributes pandas via:

- **conda-forge** for installation with conda
- **PyPI** for installation with pip
- **GitHub** for installation from source

## Installing with Conda

```sh
conda install -c conda-forge pandas
```

Recommended distribution: Miniforge. Recommended to install pandas from a virtual environment.

## Installing with pip

```sh
pip install pandas
```

With optional extras:

```sh
pip install "pandas[excel]"        # for Excel files
pip install "pandas[performance]"  # numexpr + bottleneck + numba
pip install "pandas[all]"          # all optional dependencies
```

## Installing from source

```sh
pip install cython
python -m pip install -ve . --no-build-isolation --config-settings editable-verbose=true
```

## Installing the development (nightly) version

```sh
pip install --pre --extra-index-url https://pypi.anaconda.org/scientific-python-nightly-wheels/simple pandas
```

## Required dependencies (3.0 stable, 2026-04-27)

| Package | Minimum Version |
| ------- | --------------- |
| NumPy | 1.26.0 |
| python-dateutil | 2.8.2 |
| tzdata\* | / (Windows + Pyodide only) |

## Optional extras (groupings via `pandas[<extra>]`)

| Group | 핵심 패키지 (최소 버전) |
| ----- | ---------------------- |
| **performance** | numexpr 2.10.2 / bottleneck 1.4.2 / numba 0.60.0 |
| **plot** | matplotlib 3.9.3 |
| **output-formatting** | Jinja2 3.1.5 / tabulate 0.9.0 |
| **computation** | SciPy 1.14.1 / xarray 2024.10.0 |
| **excel** | xlrd 2.0.1 / xlsxwriter 3.2.0 / openpyxl 3.1.5 / pyxlsb 1.0.10 / python-calamine 0.3.0 / odfpy 1.4.1 |
| **html** | BeautifulSoup4 4.12.3 / html5lib 1.1 / lxml 5.3.0 |
| **xml** | lxml 5.3.0 |
| **postgresql / mysql / sql-other** | SQLAlchemy 2.0.36 / psycopg2 2.9.10 / pymysql 1.1.1 / adbc-driver-postgresql 1.2.0 / adbc-driver-sqlite 1.2.0 |
| **hdf5** | PyTables 3.10.1 |
| **parquet / feather** | pyarrow 13.0.0 (또는 fastparquet 2024.11.0) |
| **iceberg** | PyIceberg 0.8.1 |
| **spss** | pyreadstat 1.2.8 |
| **fss / aws / gcp** | fsspec 2024.10.0 / s3fs 2024.10.0 / gcsfs 2024.10.0 |
| **clipboard** | PyQt5 5.15.9 / qtpy 2.4.2 |
| **compression** | Zstandard 0.23.0 |
| **timezone** | pytz 2020.1 |

## 정책 (요약)

- Required deps: 보통 ~2년 이상 된 버전이 최소 지원.
- Optional deps: 보통 ~1년 이상 된 버전이 최소 지원.

---

원본: https://github.com/pandas-dev/pandas/blob/main/doc/source/getting_started/install.rst
SHA: e3b2a01adc115e02d701030bea801f295e6a6b96 (size 21,206 bytes)
수집일: 2026-04-27
