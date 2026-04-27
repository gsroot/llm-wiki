.. _overview:

****************
Package overview
****************

pandas is a Python package that provides fast, flexible, and expressive data structures designed to make working with
"relational" or "labeled" data both easy and intuitive. It aims to be the fundamental high-level building block for
Python's practical, **real-world** data analysis. Additionally, it seeks to become **the most powerful and flexible
open source data analysis/manipulation tool available in any language**.

pandas is well suited for many different kinds of data:

- Tabular data with heterogeneously-typed columns, as in an SQL table or Excel spreadsheet
- Ordered and unordered (not necessarily fixed-frequency) time series data
- Arbitrary matrix data (homogeneously typed or heterogeneous) with row and column labels
- Any other form of observational / statistical data sets

The two primary data structures are :class:`Series` (1-dimensional) and :class:`DataFrame` (2-dimensional).
For R users, :class:`DataFrame` provides everything that R's ``data.frame`` provides and much more. pandas is
built on top of NumPy and is intended to integrate well within a scientific computing environment.

Key strengths:

- Easy handling of **missing data**
- **Size mutability**: columns can be inserted and deleted from DataFrame
- Automatic and explicit **data alignment**
- Powerful, flexible **group by** (split-apply-combine)
- Easy conversion of ragged/differently-indexed data into DataFrame
- Intelligent label-based **slicing**, **fancy indexing**, **subsetting**
- Intuitive **merging** and **joining**
- Flexible **reshaping** and pivoting
- **Hierarchical** axis labeling
- Robust IO tools (CSV/Excel/databases/HDF5)
- **Time series** functionality

For data scientists, working with data is typically divided into multiple stages: munging and cleaning data,
analyzing/modeling it, then organizing the results of the analysis into a form suitable for plotting or tabular display.
pandas is the ideal tool for all of these tasks.

Some other notes:

- pandas is **fast**. Many of the low-level algorithmic bits have been extensively tweaked in Cython.
- pandas is a dependency of statsmodels, making it an important part of the statistical computing ecosystem in Python.
- pandas has been used extensively in production in financial applications.

Data structures
---------------

| Dimensions | Name | Description |
| ---------- | ---- | ----------- |
| 1 | Series | 1D labeled homogeneously-typed array |
| 2 | DataFrame | 2D labeled, size-mutable tabular structure with potentially heterogeneously-typed columns |

Why more than one data structure?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DataFrame is a container for Series; Series is a container for scalars. With tabular data, it is more semantically
helpful to think of the **index** (the rows) and the **columns** rather than axis 0 and axis 1.

Mutability and copying
----------------------

All pandas data structures are **value-mutable** but not always **size-mutable**. The length of a Series cannot be
changed, but columns can be inserted into a DataFrame. However, **the vast majority of methods produce new objects
and leave the input data untouched**. In general we like to **favor immutability** where sensible.

Project governance
------------------

The governance process that pandas has used informally since its inception in 2008 is formalized in
[Project Governance documents](https://github.com/pandas-dev/pandas/blob/main/web/pandas/about/governance.md).

**Wes McKinney is the Benevolent Dictator for Life (BDFL).**

License
-------

BSD 3-Clause.

---

원본: https://github.com/pandas-dev/pandas/blob/main/doc/source/getting_started/overview.rst
SHA: 98a68080d33ef44e042bd8b7be5409442c4b5ae8 (size 8,198 bytes)
수집일: 2026-04-27
