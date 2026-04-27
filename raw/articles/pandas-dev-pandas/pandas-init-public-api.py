# 발췌: pandas/__init__.py — 공개 API 표면(public API surface) 단일 진실 공급원
# 원본 SHA: a005593811cc22efd343b4d7fc940022bce46803 (size 7,975 bytes)
# 수집일: 2026-04-27
# 의미: __all__ 리스트가 곧 pandas의 "공식 명함"

# 하드 의존성 (없으면 ImportError)
_hard_dependencies = ("numpy", "dateutil")

# 핵심 공개 객체 (요약 — 전체는 아래 __all__ 참조)
from pandas.core.api import (
    # dtype
    ArrowDtype, Int8/16/32/64Dtype, UInt8/16/32/64Dtype, Float32/64Dtype,
    CategoricalDtype, PeriodDtype, IntervalDtype, DatetimeTZDtype, StringDtype, BooleanDtype,
    # missing
    NA, isna, isnull, notna, notnull,
    # indexes
    Index, CategoricalIndex, RangeIndex, MultiIndex, IntervalIndex,
    TimedeltaIndex, DatetimeIndex, PeriodIndex, IndexSlice,
    # tseries
    NaT, Period, period_range, Timedelta, timedelta_range, Timestamp,
    date_range, bdate_range, Interval, interval_range, DateOffset,
    # conversion
    to_numeric, to_datetime, to_timedelta,
    # misc
    Flags, Grouper, factorize, unique, NamedAgg, array, Categorical,
    set_eng_float_format, Series, DataFrame,
)

# Reshape
from pandas.core.reshape.api import (
    concat, lreshape, melt, wide_to_long, merge, merge_asof, merge_ordered,
    crosstab, pivot, pivot_table, get_dummies, from_dummies, cut, qcut,
)

# IO API (BI 직무 핵심)
from pandas.io.api import (
    # excel
    ExcelFile, ExcelWriter, read_excel,
    # parsers
    read_csv, read_fwf, read_table,
    # pickle
    read_pickle, to_pickle,
    # pytables
    HDFStore, read_hdf,
    # sql
    read_sql, read_sql_query, read_sql_table,
    # misc
    read_clipboard, read_parquet, read_orc, read_feather,
    read_html, read_xml, read_json, read_stata, read_sas, read_spss,
    read_iceberg,
)

from pandas.io.json._normalize import json_normalize

# 핵심 도큐먼트
__doc__ = """pandas - a powerful data analysis and manipulation library for Python"""

# __all__ (101개 항목): 공개 API 단일 진실 공급원
# 카테고리별 분류:
#
# === Core 데이터 구조 ===
# DataFrame, Series, Index, Categorical, NamedAgg, NA, NaT, Flags, Grouper, IndexSlice
#
# === dtype ===
# ArrowDtype, BooleanDtype, CategoricalDtype, DatetimeTZDtype, IntervalDtype,
# PeriodDtype, SparseDtype, StringDtype,
# Int8/16/32/64Dtype, UInt8/16/32/64Dtype, Float32/64Dtype
#
# === Index 종류 ===
# CategoricalIndex, DatetimeIndex, IntervalIndex, MultiIndex, PeriodIndex,
# RangeIndex, TimedeltaIndex
#
# === 시계열 ===
# Period, Timedelta, Timestamp, Interval, DateOffset,
# bdate_range, date_range, period_range, timedelta_range, interval_range,
# infer_freq, offsets, tseries
#
# === 변환 / 결측 ===
# to_datetime, to_numeric, to_pickle, to_timedelta,
# isna, isnull, notna, notnull,
# array, factorize, unique
#
# === Reshape ===
# concat, crosstab, cut, qcut, get_dummies, from_dummies, lreshape, melt,
# merge, merge_asof, merge_ordered, pivot, pivot_table, wide_to_long
#
# === IO Read ===
# read_clipboard, read_csv, read_excel, read_feather, read_fwf, read_hdf,
# read_html, read_iceberg, read_json, read_orc, read_parquet, read_pickle,
# read_sas, read_spss, read_sql, read_sql_query, read_sql_table,
# read_stata, read_table, read_xml
#
# === IO Write ===
# ExcelFile, ExcelWriter, HDFStore
#
# === JSON ===
# json_normalize
#
# === 옵션 ===
# describe_option, get_option, option_context, options, reset_option,
# set_eng_float_format, set_option
#
# === 모듈 ===
# api, arrays, errors, eval, io, plotting, testing, test, show_versions
#
# === 메타 ===
# __git_version__, __version__
