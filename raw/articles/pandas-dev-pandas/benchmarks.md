# Benchmarks

Benchmarks are tests to measure the performance of pandas. There are two different
kinds of benchmarks relevant to pandas:

* Internal pandas benchmarks to measure speed and memory usage over time
* Community benchmarks comparing the speed or memory usage of different tools at doing the same job

## pandas benchmarks

pandas benchmarks are implemented in the asv_bench directory of our repository, using the
[airspeed velocity (asv)](https://asv.readthedocs.io/en/latest/) framework.

The benchmarks can be run locally by any pandas developer with `asv run`, useful to detect if local changes
have an impact in performance.

Note: benchmarks are not deterministic. Hardware differences and varying levels of stress can produce
significant differences when running the same exact code.

## Automated benchmark runner

The [asv-runner repository](https://github.com/pandas-dev/asv-runner/) automatically runs the pandas asv benchmark
suite for every (or almost every) commit to the main branch. Run on GitHub Actions. Results at:
https://pandas-dev.github.io/asv-runner/

## Community benchmarks

The main benchmarks comparing dataframe tools that include pandas are:

- [DuckDB (former H2O.ai) benchmarks](https://duckdblabs.github.io/db-benchmark/)
- [TPCH benchmarks](https://pola.rs/posts/benchmarks/)

---

원본: https://github.com/pandas-dev/pandas/blob/main/web/pandas/community/benchmarks.md
SHA: 0844e81b0166b4941053e4321619643fd7b44dd0 (size 1,987 bytes)
수집일: 2026-04-27
