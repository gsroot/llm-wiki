---
title: microsoft/ML-For-Beginners — 12 weeks, 26 Lessons 클래식 ML
type: source
source_type: article
source_url: https://github.com/microsoft/ML-For-Beginners
raw_path: raw/articles/microsoft-ml-for-beginners/
author: Microsoft Cloud Advocates
date_published: 2021-03-03
date_ingested: 2026-04-27
tags:
- machine-learning
- microsoft
- microsoft-for-beginners
- scikit-learn
- python
- classic-ml
- time-series
related:
- '[[microsoft]]'
- '[[microsoft-for-beginners]]'
- '[[ml-ai]]'
- '[[data-pipeline-bigquery]]'
confidence: high
inbound_count: 25
aliases:
- Microsoft Ml For Beginners
- microsoft ml for beginners
- microsoft/ML-For-Beginners — 12 weeks, 26 Lessons 클래식 ML
cited_by:
  - "[[agent-stack-evolution]]"
  - "[[microsoft]]"
  - "[[microsoft-data-science-for-beginners]]"
  - "[[microsoft-for-beginners]]"
  - "[[pandas]]"
  - "[[pandas-dev-pandas]]"
  - "[[scikit-learn]]"
  - "[[scikit-learn-scikit-learn]]"
cited_by_count: 8
---

# microsoft/ML-For-Beginners — 12 weeks, 26 Lessons 클래식 ML

## 한줄 요약

> Microsoft Cloud Advocates의 "**고전 머신러닝**" 입문 — 의도적으로 딥러닝을 회피하고 Scikit-learn 중심으로 회귀 → 분류 → 클러스터링 → NLP → 시계열 → 강화학습까지를 12주 26 lesson으로, Python뿐 아니라 R lesson도 함께 제공. 프로젝트는 "세계 문화"라는 공통 테마 (호박 가격, 아시아·인도 요리, 나이지리아 음악, 호텔 리뷰, 세계 전력 사용량).

## 메타

- 라이선스: MIT
- 별 85,483 (2026-04-27 기준)
- 첫 커밋 2021-03-03 — 5개 시리즈 중 두 번째로 오래됨
- 기본 언어: Python (Jupyter Notebook) + R 솔루션 병행 (`solution/R/lesson_*.html`)
- 페다고지 핵심: pre-lecture quiz → 본문 → knowledge checks → challenge → assignment → post-lecture quiz (총 52 quizzes, 3문제씩, `quiz-app/` 디렉토리)
- PAT(Progress Assessment Tool) — 학습자가 Discussion에 채우는 자기평가 루브릭

## 26 Lesson 그루핑

| 단원 | Lessons | 데이터/주제 |
|------|---------|------------|
| 1-Introduction | 01–04 | 기초·역사·공정성·기법 |
| 2-Regression | 05–08 | **북미 호박 가격** — 선형/다항/로지스틱 |
| 3-Web-App | 09 | 학습 모델 웹 앱화 |
| 4-Classification | 10–13 | **아시아·인도 요리** — 분류기 비교, 추천 앱 |
| 5-Clustering | 14–15 | **나이지리아 음악** — K-Means |
| 6-NLP | 16–20 | 봇·번역·**유럽 호텔 리뷰** 감성분석 |
| **7-TimeSeries** | **21–23** | **세계 전력 사용량 — ARIMA, SVR (raw 보관)** |
| 8-Reinforcement | 24–25 | **Peter & Wolf** Q-Learning, Gym |
| 9-Real-World | 26+ | 실제 응용 + **RAI dashboard 모델 디버깅** |

## 핵심 시사점

### 1. 의도적 "딥러닝 회피"

> "you will learn about what is sometimes called **classic machine learning**, using primarily Scikit-learn as a library and avoiding deep learning, which is covered in our [AI for Beginners](https://aka.ms/ai4beginners) curriculum."

같은 사단의 다른 코스(`AI-For-Beginners`)와 **명시적 분업**. 입문자가 한 코스만 끝내도 일관된 추상화 레벨에 머물 수 있게 하는 페다고지 결정.

### 2. R lesson 병행

각 lesson에 `solution/R/lesson_NN.html`이 있어 Python·R 양쪽으로 같은 알고리즘 학습 가능. **R Markdown** 자체를 `code chunks + YAML header`로 정의하며 데이터 분석의 표준 프레임으로 권유 — pandas + Jupyter 외 다른 표준을 가르치는 의도.

### 3. "세계 문화" 데이터셋 — 페다고지 강화

호박 가격, 아시아 요리, 나이지리아 음악, 유럽 호텔 리뷰, 세계 전력 — 입문자에게 친숙한 도메인을 통해 "어디에든 ML이 적용된다"는 메시지를 시각화. 단순 iris/MNIST 데이터셋 회피.

### 4. 9-Real-World — Responsible AI dashboard

마지막 단원에 **모델 디버깅을 RAI dashboard로** 가르침. 단순 학습→평가가 아닌 "공정성·해석성"을 ML 입문 코스 본문에 포함시킨 결정. 입문자에게 "ML은 정확도만이 아니다"를 첫 코스에서 주입.

## 석근에게 가장 가치있는 lesson

- **7-TimeSeries (21–23)** — BI 직결, raw 보관 (전력 사용량 예측은 게임 데이터 BI의 사용자/매출 시계열과 같은 형태)
- **9-Real-World/2-Debugging-ML-Models** — Responsible AI dashboard로 모델 디버깅, 회사 BI 모델에 응용 가능
- **3-Web-App** — 학습된 모델을 Flask 등으로 서비스화하는 패턴, FastAPI에 응용 가능
- 10-13 (Classification) — 추천 시스템(요리 추천)이라 게임 추천 BI와 직결

## 관련 엔티티/개념

- [[microsoft]] / [[microsoft-for-beginners]]
- [[ml-ai]] — 회사 BI에서 사용하는 AutoML과 비교 가능
- [[data-pipeline-bigquery]] — BigQuery에 적재된 시계열 데이터를 ARIMA/SVR로 다루는 발상
- [[scikit-learn]] — 26 lesson 전체가 의존하는 라이브러리. ML-For-Beginners의 "한 가지 추상화로 모든 ML 알고리즘 다루기"는 sklearn의 5가지 API 컨트랙트(`fit`/`predict`/`transform`/`Pipeline`/Meta-estimator)가 19년 변하지 않았기에 가능

## 인용

> "We have chosen two pedagogical tenets while building this curriculum: ensuring that it is hands-on **project-based** and that it includes **frequent quizzes**. In addition, this curriculum has a common **theme** to give it cohesion."
> — README

## 메모

- 5개 시리즈 중 가장 "전통 데이터과학" 성격이 짙어 회사 업무(BI/ML)와 가장 가깝다.
- 후속 탐구: 7-TimeSeries lesson 21을 raw에 보관함 — ARIMA/SVR 두 개 lesson도 추가 보관 시 BI 시계열 적용에 직접 도움.
- 다음 단계: [[microsoft-data-science-for-beginners]]와 짝으로 보면 "ML 알고리즘"과 "데이터과학 라이프사이클"이 상호 보완적.
