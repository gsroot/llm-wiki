---
title: "LightGBM"
aliases: [LightGBM, 라이트지비엠, light-gbm]
type: entity
entity_type: tool
tags: [lightgbm, ml, gbdt, gradient-boosting, decision-tree, machine-learning, microsoft, lightgbm-org, neurips, effver]
related:
  - "[[scikit-learn]]"
  - "[[ml-ai]]"
  - "[[pandas]]"
  - "[[parquet]]"
  - "[[microsoft-lightgbm]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 4
inbound_count: 22
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 10
---

# LightGBM

## 개요

**Light Gradient Boosting Machine** — Microsoft Research에서 출범한 GBDT(Gradient Boosting Decision Tree) 프레임워크. 2017년 NIPS 논문이 표준이 되어 **Kaggle/실무 ML의 사실 표준 GBDT 라이브러리**로 자리잡았다. 2026년 3월 `Microsoft/LightGBM` → `lightgbm-org/LightGBM`로 조직 졸업했으나 같은 메인테이너가 운영.

## 주요 특징

### 알고리즘 혁신 (vs XGBoost)
- **Histogram-based split finding** — 연속값을 bin으로 양자화 → 메모리·속도 개선
- **Leaf-wise tree growth** — depth-wise 대신 가장 손실 감소 큰 leaf 우선 (정확도↑, 과적합 위험)
- **GOSS (Gradient-based One-Side Sampling)** — 큰 gradient 샘플 우선 (선택적 샘플링)
- **EFB (Exclusive Feature Bundling)** — 상호배타 피처 묶기 → 차원 축소
- **Parallel/Distributed/GPU** 학습 1급 지원

### 기술 스택
- **언어**: C++ 코어 + Python/R/JVM/C#/Rust/Ruby/Julia 바인딩
- **모델 포맷**: 자체 텍스트 형식 + ONNX/PMML/Treelite로 export
- **데이터 입력**: NumPy / pandas DataFrame / pyarrow Tables / Dataset API (sparse/CSR 지원)
- **GPU**: OpenCL / CUDA (별도 빌드)

### 거버넌스
- **2026년 3월 Microsoft → lightgbm-org 졸업** (새로운 OSS 거버넌스 사례)
- License: MIT
- **EffVer 버전 체계** (SemVer가 아닌 effective version) — 사용자 영향 중심

### 통합 생태계 (외부 25+개)
- **AutoML**: FLAML / Optuna LightGBM Tuner / MLJAR
- **분산**: SynapseML (Spark) / lightgbm_ray / Mars / Kubeflow
- **추론 가속**: cuML FIL (GPU) / daal4py (Intel CPU) / Treelite / lleaves (LLVM)
- **시각화/설명**: SHAP / Shapash / dtreeviz / supertree
- **시계열**: mlforecast / skforecast
- **Postgres**: postgresml (SQL로 LightGBM 학습)

## 관련 개념

- [[scikit-learn]]: sklearn-compatible API (`lgb.LGBMClassifier`) — Pipeline에 직접 삽입 가능
- [[pandas]] / [[polars]]: 전처리 → DataFrame 형태로 LightGBM에 입력 (zero-copy 변환은 [[apache-arrow]] 경유)
- [[parquet]]: 학습 데이터 형식 (Parquet → DataFrame → LightGBM Dataset)
- [[ml-ai]]: 클래식 ML의 "tabular data 1순위 베이스라인"
- [[duckdb]]: DuckDB로 피처 엔지니어링 SQL 작성 → LightGBM 학습

## 의사결정 컨텍스트 (raw 인용)

> "2017년 NeurIPS 논문이 표준이 된 GBDT 프레임워크. C++로 구현된 코어 + 다국어 바인딩 + 2026년 3월 Microsoft에서 lightgbm-org로 조직 졸업한 거버넌스 사례."
> — [[microsoft-lightgbm]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] ML 영역의 GBDT 표준. [[c2spf-analytics|c2spf 게임 데이터 BI]] BI 시스템에서 유저 예측 모델 후보(현재는 GCP AutoML 사용, 자체 제어 필요 시 LightGBM 차용 후보). [[matechat|MateChat 사이드 프로젝트]] 사이드의 채팅 분석 모듈 ML 후보 ([[scikit-learn]]·[[pandas]]와 함께 데이터 분석 본진). **EffVer 버전 체계 + Microsoft 졸업**은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 OSS 거버넌스 카탈로그 9번째 모델 — [[bdfl]]·[[pdep]] 등과 함께 거버넌스 다양성 사례.

## 출처

- [[microsoft-lightgbm]] — 수집, README + MAINTAINING.md + CONTRIBUTING.md (총 280줄)

## 메모

- **석근님 BI 적용**: 게임 데이터 BI에서 churn / LTV / 매출 예측에 가장 흔한 모델. [[c2spf-analytics|c2spf 게임 데이터 BI]] 스택의 ML 1순위.
- **vs XGBoost**: 정확도는 비슷, LightGBM이 학습 속도·메모리 면에서 우위 (큰 데이터셋). XGBoost는 R 생태계에서 여전히 강함.
- **vs CatBoost**: CatBoost는 categorical 자동 처리·overfitting 안정성 우위, LightGBM은 다양한 통합 우위.
- **EffVer**: 향후 위키에서 [[uv]]/[[ruff]]/[[pandas]]/[[polars]]의 버전 정책과 비교 매트릭스 작성 가치.
