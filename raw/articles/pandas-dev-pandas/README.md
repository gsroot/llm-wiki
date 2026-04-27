<picture align="center">
  <source media="(prefers-color-scheme: dark)" srcset="https://pandas.pydata.org/static/img/pandas_white.svg">
  <img alt="Pandas Logo" src="https://pandas.pydata.org/static/img/pandas.svg">
</picture>

-----------------

# pandas: A Powerful Python Data Analysis Toolkit

| | |
| --- | --- |
| Testing | [![CI - Test](https://github.com/pandas-dev/pandas/actions/workflows/unit-tests.yml/badge.svg)](https://github.com/pandas-dev/pandas/actions/workflows/unit-tests.yml) [![Coverage](https://codecov.io/github/pandas-dev/pandas/coverage.svg?branch=main)](https://codecov.io/gh/pandas-dev/pandas) |
| Package | [![PyPI Latest Release](https://img.shields.io/pypi/v/pandas.svg)](https://pypi.org/project/pandas/) [![PyPI Downloads](https://img.shields.io/pypi/dm/pandas.svg?label=PyPI%20downloads)](https://pypi.org/project/pandas/) [![Conda Latest Release](https://anaconda.org/conda-forge/pandas/badges/version.svg)](https://anaconda.org/conda-forge/pandas) [![Conda Downloads](https://img.shields.io/conda/dn/conda-forge/pandas.svg?label=Conda%20downloads)](https://anaconda.org/conda-forge/pandas) |
| Meta | [![Powered by NumFOCUS](https://img.shields.io/badge/powered%20by-NumFOCUS-orange.svg?style=flat&colorA=E1523D&colorB=007D8A)](https://numfocus.org) [![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3509134.svg)](https://doi.org/10.5281/zenodo.3509134) [![License - BSD 3-Clause](https://img.shields.io/pypi/l/pandas.svg)](https://github.com/pandas-dev/pandas/blob/main/LICENSE) [![Slack](https://img.shields.io/badge/join_Slack-information-brightgreen.svg?logo=slack)](https://pandas.pydata.org/docs/dev/development/community.html?highlight=slack#community-slack) [![LFX Health Score](https://insights.linuxfoundation.org/api/badge/health-score?project=pandas-dev-pandas)](https://insights.linuxfoundation.org/project/pandas-dev-pandas) |


## What is it?

**pandas** is a Python package that provides fast, flexible, and expressive data
structures designed to make working with "relational" or "labeled" data both
easy and intuitive. It aims to be the fundamental high-level building block for
doing practical, **real-world** data analysis in Python. Additionally, it has
the broader goal of becoming **the most powerful and flexible open-source data
analysis/manipulation tool available in any language**. It is already well on
its way towards this goal.

## Main Features
Here are just a few of the things that pandas does well:

  - Easy handling of **missing data** (represented as `NaN`, `NA`, or `NaT`) in floating point as well as non-floating point data
  - Size mutability: columns can be **inserted and deleted** from DataFrame and higher dimensional objects
  - Automatic and explicit **data alignment**
  - Powerful, flexible **group by** functionality (split-apply-combine)
  - Intelligent label-based **slicing**, **fancy indexing**, and **subsetting**
  - Intuitive **merging** and **joining** data sets
  - Flexible **reshaping** and **pivoting**
  - **Hierarchical** labeling of axes
  - Robust I/O tools (CSV, Excel, databases, HDF5, Parquet)
  - **Time series**-specific functionality

## Where to get it

```sh
# conda
conda install -c conda-forge pandas
# or PyPI
pip install pandas
```

## Dependencies
- NumPy 1.26.0+
- python-dateutil 2.8.2+
- tzdata (Windows/Emscripten only)

## License
BSD 3-Clause

## Background
Work on `pandas` started at AQR (a quantitative hedge fund) in 2008 and has been under active development since then.

## Discussion and Development
- GitHub issue tracker: https://github.com/pandas-dev/pandas/issues
- pandas-dev mailing list: https://mail.python.org/mailman/listinfo/pandas-dev
- Slack channel for development discussion
- Frequent community meetings + monthly new contributor meetings

## Code of Conduct
https://github.com/pandas-dev/.github/blob/master/CODE_OF_CONDUCT.md

---

원본: https://github.com/pandas-dev/pandas/blob/main/README.md
SHA: ad905ee1c0e3ad28042ff9a72b2c8ae64f693957 (size 11,363 bytes)
수집일: 2026-04-27 (8회차)
