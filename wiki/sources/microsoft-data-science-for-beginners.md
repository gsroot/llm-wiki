---
title: "microsoft/Data-Science-For-Beginners — 10 weeks, 20 Lessons 데이터과학 입문"
type: source
source_type: article
source_url: "https://github.com/microsoft/Data-Science-For-Beginners"
raw_path: "raw/articles/microsoft-data-science-for-beginners/"
author: "Microsoft Cloud Advocates"
date_published: 2021-03-03
date_ingested: 2026-04-27
tags: [data-science, microsoft, microsoft-for-beginners, pandas, sql, nosql, matplotlib, data-visualization, data-ethics, data-lifecycle, azure-ml, BI]
related:
  - "[[microsoft]]"
  - "[[microsoft-for-beginners]]"
  - "[[data-pipeline-bigquery]]"
  - "[[ml-ai]]"
  - "[[c2spf-analytics]]"
  - "[[pandas]]"
  - "[[pandas-dev-pandas]]"
confidence: high
---

# microsoft/Data-Science-For-Beginners — 10 weeks, 20 Lessons 데이터과학 입문

## 한줄 요약

> Microsoft Cloud Advocates의 데이터과학 입문 — 10주 20 lesson을 "정의 → **윤리** → 관계형/NoSQL → Python(pandas) → 데이터 준비 → Matplotlib 시각화 4종 → **라이프사이클(획득→분석→커뮤니케이션)** → 클라우드(Azure ML) → 실제 응용"으로 단계화한 BI 직결 코스. 첫 본문이 **Data Science Ethics**라는 점이 다른 시리즈와 차별화.

## 메타

- 라이선스: MIT
- 별 35,119 (2026-04-27 기준, 5개 시리즈 중 가장 적지만 가장 직무 직결)
- 첫 커밋 2021-03-03 — ML-For-Beginners와 같은 날 출시 (자매 코스)
- 기본 언어: Jupyter Notebook + pandas
- 페다고지: 40 quizzes (3문제씩) + sketchnote + assignment
- 별도 `examples/` 디렉토리 — 절대 초보자용 hello-world 5종 (Hello World, Loading Data, Simple Analysis, Basic Visualization, Real-World Project)

## 20 Lesson 그루핑

| 단원 | Lessons | 핵심 |
|------|---------|------|
| 1-Introduction | 01–04 | 정의 / **윤리** / 데이터 분류 / 통계와 확률 |
| 2-Working-With-Data | 05–08 | 관계형(SQL) / NoSQL / Python(pandas) / 데이터 준비 |
| 3-Data-Visualization | 09–13 | Matplotlib — 수량/분포/비율/관계/**의미있는 시각화** |
| **4-Data-Science-Lifecycle** | **14–16** | **Introduction → Analyzing → Communication (raw 보관)** |
| 5-Data-Science-In-Cloud | 17–19 | Azure ML — Introduction / Low-Code / 배포 |
| 6-Data-Science-In-Wild | 20 | 실제 데이터과학 사례 |

## 핵심 시사점

### 1. 02 = Data Science Ethics가 본문 두 번째

대부분의 입문 코스가 윤리를 부록으로 빼는 데 비해 이 코스는 **02번**에 윤리를 두어 "데이터 다루기 = 윤리 책임"을 첫 인상으로 박는다. 게임 데이터 BI 같은 프라이버시 민감 도메인에는 첫 단원으로 가르칠 만한 위치.

### 2. 13 = "Meaningful Visualizations"

시각화 단원의 마지막을 "예쁜 차트 만드는 법"이 아닌 "**Visualization for Decision Making**"으로 마무리. BI 개발자에게 직결 — 회사 대시보드의 차트 1개당 의사결정 1개를 매핑하는 발상.

### 3. 4-Lifecycle = "Introduction → Analyzing → Communication"

데이터과학을 **3단계 라이프사이클**로 압축:
1. **Introduction (14)**: 획득·추출 (capturing requirement, data sources)
2. **Analyzing (15)**: 분석 (EDA → 모델링)
3. **Communication (16)**: **결과 전달** (의사결정자 친화적 표현)

3단계 모델은 회사 BI 운영(요구사항 수집 → 쿼리/모델 → 대시보드/리포팅)과 1:1 매핑된다.

### 4. examples/ 디렉토리 = "절대 초보 트랙"

본 코스에 들어가기 전 5개 hello-world 예제로 사전 워밍업. 이는 본 코스 진입장벽을 낮추는 운영 패턴 — 위키에도 "처음 보는 사람용 1페이지" 별도 운영 가능.

### 5. 5-Data-Science-In-Cloud — Azure ML Studio 일색

3 lesson 중 2개가 **Low-Code(Designer)** + **Azure ML Studio 배포**. 클라우드 단원에서 "코드 거의 안 짜고 ML 모델 학습·배포"를 강조 — 이는 회사 BI에서 데이터 분석가가 직접 모델 운영할 때의 실무 패턴과 일치.

## 석근에게 가장 가치있는 lesson

- **4-Data-Science-Lifecycle (14–16)** — BI 라이프사이클 직결, 14번 raw 보관
- **02 (Data Ethics)** — 게임 사용자 데이터(개인정보) 다루는 BI에 직결
- **05–08 (SQL/NoSQL/pandas/preparation)** — pandas + BigQuery 조합 실무 기초
- **13 (Meaningful Visualizations)** — 회사 대시보드 설계 원칙
- **17–19 (Azure ML)** — Azure를 안 쓰더라도 Low-Code ML 운영 발상은 GCP/AWS에 이식 가능

## 관련 엔티티/개념

- [[microsoft]] / [[microsoft-for-beginners]]
- [[microsoft-ml-for-beginners]] — 같은 날 출시된 자매 코스. ML 알고리즘 ↔ 데이터과학 라이프사이클로 상호 보완
- [[data-pipeline-bigquery]] — BigQuery + pandas 조합으로 회사 BI 직접 응용
- [[c2spf-analytics|c2spf 게임 데이터 BI]] — 컴투스플랫폼 BI 서비스의 라이프사이클과 매핑 가능
- [[ml-ai]] — Azure ML Studio가 회사의 AutoML/LangGraph와 비교 대상

## 인용

> "By the end of this series, students will have learned basic principles of data science, including ethical concepts, data preparation, different ways of working with data, data visualization, data analysis, real-world use cases of data science, and more."
> — README

## 메모

- 5개 시리즈 중 석근의 직무(컴투스플랫폼 게임 데이터 BI 서비스 개발자)에 가장 직결되는 코스. ML-For-Beginners가 "알고리즘", 이것이 "운영 라이프사이클".
- 후속 탐구: 02 (Data Ethics) lesson도 raw 보관 검토 — 회사 BI에 적용할 윤리 체크리스트로 활용 가능.
- 16 (Communication) lesson은 [[c2spf-analytics-renewal]]의 Airbridge 통합 보고처럼 "결과를 누구에게 어떻게"의 실무 가이드로 응용 가능.
