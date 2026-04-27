---
title: "AutoML 기반 MLOps 시스템을 처음부터 구축"
type: story
category: learning
period: "2020-08 ~ 2021-09"
primary_project: "2020-08-analytics-ml-prediction"
tags: [ml, automl, mlops, learning, gcp]
skills_demonstrated:
  - ml-ai
  - data-pipeline
  - backend-python
  - frontend-react
---

# AutoML 기반 MLOps 시스템을 처음부터 구축

## Situation

애널리틱스 서비스에 **유저 행동(이탈·구매) 예측** 니즈가 발생했으나, 조직 내 ML 서비스 운영 경험이 부재했다. 모델 학습 인프라, 주기적 추론 파이프라인, 결과 시각화 UI 모두 처음부터 설계해야 하는 상황 (출처: old-portfolio "애널리틱스 ML 유저 예측 기능 개발").

## Task

데이터 전처리 → AutoML 모델링 → 주기적 학습·추론 파이프라인 → 결과 리포트/세그먼트 분석 UI까지 **전 과정을 단독 풀스택으로 설계·구현**. 서비스 기획 및 AutoML 모델링에도 참여.

## Action

- **MLOps 시스템 설계**: **GCP AutoML Tables · BigQuery ML · AI Platform Pipeline** 조합으로 예측 모델 학습·배포 파이프라인 구축. Digdag 워크플로우로 주기적 학습·추론을 자동화.
- **풀스택 구현**: 백엔드는 Python **Flask** + Pandas + SQLAlchemy + Pytest, 프런트엔드는 **React + Mobx**. 예측 결과를 사용자가 쉽게 이해할 수 있도록 리포트·세그먼트 분석 UI/UX를 설계.
- **데이터 파이프라인**: MySQL·Redis + GCP BigQuery를 데이터 소스로 연결하고, 전처리 로직을 Jupyter Notebook에서 프로토타이핑 후 서비스 코드로 이관.
- **컨테이너 배포**: Flask 서버와 워커를 Docker 컨테이너화해 반복 배포 가능한 구조 확보.
- **리포지토리 기여**: `c2spf/analytics-prediction` 저장소에 **116+ 커밋** 투입, 2020-08-25 ~ 2021-03-05 집중 개발 기간 + 이후 유지보수 (출처: `github-c2spf/repos/analytics-prediction.md`).

## Result

- **정량**:
  - 예측 **정확도 평균 85% 이상** 달성 (old-portfolio 인용).
  - `analytics-prediction` 저장소에 **116+ 커밋** (페이지네이션 상한, 실제 더 많을 수 있음).
  - 기술 스택 학습·적용 범위: Python (Flask, Pandas, Jupyter, SQLAlchemy, Pytest) + React/Mobx + GCP AutoML·BigQuery ML·AI Platform Pipeline + Digdag + Docker.
- **정성**:
  - **예측된 유저 추세 ↔ 리텐션 추세가 반비례 관계**임을 입증해 데이터 기반 마케팅 전략 수립에 기여 (old-portfolio 인용).
  - 사용자 이탈 방지 전략 수립에 활용될 수 있는 예측 근거 제공.
- **조직 임팩트**:
  - **MLOps 기반 시스템 확보**로 이후 ML 요구사항에 빠른 대응 가능 (old-portfolio 인용).
  - 데이터 전처리부터 UI까지 전 과정을 단독 풀스택으로 경험하며, 이후 플랫폼(공통 API·React 리뉴얼 등)에서 데이터/ML 연동 설계의 기반 경험이 됨.

## 관련 증거

- GitHub: <https://github.com/c2spf/analytics-prediction> (private, 내 커밋 **116+** / 전체 925, 페이지네이션 상한)
- 사내 Confluence: pageId **193136207** (프로젝트 문서), pageId **210931595** (개발 가이드)
- old-portfolio: "애널리틱스 ML 유저 예측 기능 개발" 섹션 (2020-08 ~ 2021-09)
- 기술 스택 출처: `docs/10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md`
