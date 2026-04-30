---
title: Copy-on-Write (CoW)
aliases:
- Copy-on-Write
- CoW
- COW
type: concept
category: data
tags:
- copy-on-write
- pandas
- optimization
related:
- '[[pandas]]'
- '[[dataframe]]'
- '[[ml-ai]]'
- '[[pandas-dev-pandas]]'
- '[[pola-rs-polars]]'
source_count: 2
observed_source_refs: 8
inbound_count: 28
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 10
---

# Copy-on-Write (CoW)

## 정의

**Copy-on-Write(CoW)**는 객체 복사를 "쓰기가 발생하기 전까지" 미루는 기법이다. 두 객체가 동일한 데이터를 공유하다가, 한쪽이 데이터를 수정하려는 순간 비로소 실제 복사가 일어난다.

## 왜 중요한가

- **메모리 효율**: 불필요한 복사 비용을 제거. 읽기만 하는 경우 0복사로 끝남.
- **예측 가능성**: 복사 의도를 명시적으로 표현할 수 있음. "수정하려면 복사된다"가 일관되게 보장됨.
- **버그 감소**: pandas 사용자가 가장 자주 만나는 함정인 `SettingWithCopyWarning`과 view/copy 모호성을 근본 해결.

## 핵심 내용

### 작동 원리

1. 객체 A에서 객체 B를 만들 때 데이터 자체는 복사하지 않고 **참조만 공유**.
2. 둘 중 어느 한쪽이 데이터를 수정하려는 순간, 그 시점에만 **실제 복사가 일어남**.
3. 이후 두 객체는 독립적으로 작동.

### 적용 도메인

- **운영체제 메모리 관리**: `fork` 호출 후 자식 프로세스가 부모 메모리를 공유하다가, write-page에 처음 쓸 때 page fault → 실제 페이지 복사.
- **파일시스템**: ZFS, Btrfs의 스냅샷.
- **데이터 분석**: [[pandas]] 2.0+가 도입한 PDEP-7 메모리 모델.
- **VCS**: Git의 객체 모델(같은 내용은 동일 SHA로 공유).
- **언어 런타임**: Swift의 표준 라이브러리 컬렉션 등.

### pandas의 CoW (PDEP-7, 2.0~3.0)

- **2.0**: opt-in 모드로 도입 (`pd.options.mode.copy_on_write = True`).
- **3.0**: 기본 동작이 됨. `SettingWithCopyWarning` 시대 종료.
- **사용자 영향**: chained assignment(`df[df.A > 0]['B'] = 1`)는 더 이상 작동하지 않음 (조용히 실패하지 않고 명확히 작동 안 함). 대신 `df.loc[df.A > 0, 'B'] = 1`를 사용해야 함.

## 실전 적용

```python
import pandas as pd

# pandas 3.0+ — CoW가 기본
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})

# 이전: view를 통한 chained assignment (혼동의 원천)
# df[df.A > 1]['B'] = 99   # 작동 안 함, 경고

# CoW 시대: 명시적 .loc[] 사용
df.loc[df.A > 1, 'B'] = 99  # 명확하고 일관됨
```

## 관련 개념

- [[dataframe]]: pandas의 핵심 자료구조. CoW 모델의 적용 대상.
- [[pandas]]: CoW를 채택한 대표 라이브러리.
- [[polars]]: 정반대 모델 — **immutable-by-default** (Apache Arrow read-only 버퍼).
- [[apache-arrow]]: immutable 메모리 모델의 표준. PyArrow 백엔드 채택 시 pandas도 점차 이 모델로 수렴.
- [[lazy-evaluation]]: lazy 평가는 CoW 트레이드오프 자체를 우회 — 중간 결과를 materialize하지 않음.

## CoW vs Immutable-by-Default 비교

| 축 | pandas (CoW) | [[polars]] (Immutable) |
|----|--------------|-----------------------|
| 메모리 모델 | NumPy 버퍼, 쓰기 시점 복사 | Apache Arrow read-only |
| in-place 업데이트 | 가능 (`df.loc[...] = ...`) | 불가 (의도적) |
| view/copy 모호성 | CoW가 해결 | 발생 자체 안 함 |
| 메모리 효율 | 읽기는 0복사, 쓰기 시 복사 | 항상 새 객체, 하지만 zero-copy 공유 |
| API 학습 곡선 | SettingWithCopyWarning 시대 종료 | "in-place는 없다" 패러다임 학습 |
| 호환성 | NumPy 생태계 1급 | Arrow 생태계 1급 ([[duckdb]]/[[pyarrow]]) |

→ 같은 문제(view/copy 모호성, 메모리 효율)에 **다른 사상으로 답한 두 라이브러리**. CoW는 "기존 모델 유지하며 명확화", Immutable은 "모델 자체를 바꿈".

## 출처

- [[pandas-dev-pandas]] — pandas 3.0 stable 릴리스, PDEP-7 메모리 모델 변혁
- [[pola-rs-polars]] — Polars의 immutable-by-default 정반대 모델

## 열린 질문

- ~~다른 데이터프레임 라이브러리(Polars, Dask 등)는 어떤 메모리 모델을 채택했는가?~~ → **답함**: Polars는 Apache Arrow immutable, Dask는 chunked CoW (pandas 모델 분산화)
- pandas가 PyArrow 백엔드(PDEP-10)로 1급 전환 시 CoW vs Immutable의 의미는? → 둘이 **수렴**할 가능성. PyArrow는 Arrow immutable 모델을 따르므로 pandas도 자연스럽게 immutable 방향
- in-place 업데이트의 인지적 가치 vs 메모리 모델 단순성: 분석가의 멘탈 모델에 어느 쪽이 더 친화적인가?
