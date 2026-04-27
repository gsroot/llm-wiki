---
title: "ML/AI (GCP AutoML · AI Platform Pipeline · LangGraph · OpenAI API)"
type: concept
category: ai
tags: [ml, ai, automl, gcp, ai-platform-pipeline, langgraph, langchain, openai, llm, mlops, prediction, pandas, scikit-learn, sklearn, dataframe, slep, fit-predict]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[data-pipeline-bigquery]]"
  - "[[mcp]]"
  - "[[pandas]]"
  - "[[scikit-learn]]"
source_count: 5
created: 2026-04-24
updated: 2026-04-27
---

# ML/AI (GCP AutoML · AI Platform Pipeline · LangGraph · OpenAI API)

## 정의

석근의 ML/AI 영역은 두 시대로 나뉜다. **2020~2021 AutoML 시대** — GCP AutoML Tables + AI Platform Pipeline 기반의 게임 유저 예측 MLOps. **2025~ LLM/Agent 시대** — LangGraph + LangChain + OpenAI API + MCP 기반의 에이전트 프로젝트(트래블메이트, Mate Chat).

## 왜 중요한가

- **ML 유저 예측 정확도 평균 85% 이상 달성** — 게임 이탈/구매 예측 모델로 마케팅·리텐션 전략에 직접 기여.
- **MLOps 체계 구축** — 단발성 모델이 아니라 AI Platform Pipeline 기반 자동 재학습/배포 시스템.
- **LangGraph 에이전트 프로덕션 배포** — 트래블메이트 Android 앱 Google Play 출시(2025-11), 실시간 AI 응답 스트리밍 + 토큰 기반 과금(클로버) 시스템.

## 핵심 내용

- **AutoML 기반 예측 (2020-08 ~ 2021-09)**
  - GCP AutoML Tables: 이탈/구매 예측 모델 학습.
  - GCP AI Platform Pipeline: 자동 재학습, 배포, 모니터링.
  - Digdag로 데이터 적재 워크플로 구성.
  - 예측 결과 시각화: React + Mobx UI.
  - 정확도 평균 85%+ — 예측된 유저의 추세와 리텐션 추세가 반비례한다는 인사이트 도출.
- **LLM/Agent 시대 (2025~)**
  - **트래블메이트** (Google Play 출시, 2025-10~11) — LangGraph 에이전트로 여행 일정 자동 생성, 1 Clover = 1,000 tokens 과금, 서버 측 영수증 검증.
  - **Mate Chat** (2025-08~) — OpenAI GPT 기반 커스텀 AI 챗봇("AI Mates"), WebSocket 실시간 메시징.
  - **MCP** ([[mcp]]) — Claude Code/Cowork 통합 활용.
- **데이터 분석 도구**: [[pandas]], NumPy, [[scikit-learn]], Jupyter Notebook (지속적). pandas DataFrame이 scikit-learn의 first-class citizen이므로 학습 입력/예측 출력이 모두 DataFrame 표준. AutoML Tables는 BigQuery 직접 학습이지만 결과 검증·후처리는 [[pandas-dev-pandas]] 도구 레이어에서 수행.
- **scikit-learn 직접 사용 가능성** (대안 검토): 현 AutoML Tables 의존도를 sklearn `RandomForestClassifier` + `Pipeline(StandardScaler, ...)` 직접 구성으로 전환 시 — (a) 학습 비용(GCP AutoML Tables 시간당 과금) 절감, (b) 모델 디버깅 가능 (트리 구조·feature importance 노출), (c) `sample_weight` 라우팅(Metadata Routing API, 1.3+)으로 신규/이탈 유저 가중치 차별화, (d) `model_persistence.rst` 5단 의사결정으로 ONNX/joblib/skops 옵션 평가. 트레이드오프는 AutoML이 자동 Feature Engineering·HPO를 다 해주는 부분을 직접 짜야 한다는 점.

## 실전 적용

- **유저 예측에서 마케팅 전략으로**: 이탈 예측을 마케팅 캠페인 타겟팅에 적용.
- **AI 에이전트에서 모바일 앱 수익화로**: LangGraph 워크플로 + 토큰 과금 + 인앱결제 결합.
- **Pandas 데이터 처리**: 카카오톡 대화 분석 앱 등 개인 프로젝트에서 Plotly 시각화와 결합.

## 관련 개념

- [[data-pipeline-bigquery]] — ML 학습 데이터 소스
- [[backend-python-fastapi]] — ML 서비스 백엔드 (Flask에서 FastAPI로)
- [[mcp]] — LLM 도구 호출 프로토콜
- [[scikit-learn]] — Python ML 사실상 표준 라이브러리, 5가지 API 컨트랙트(`fit`/`predict`/`transform`/`Pipeline`/Meta-estimator)

## 출처

- [[portfolio-seed]] — AutoML/AI Platform Pipeline 시대 + LLM/Agent 시대 양쪽
- [[portfolio-resume-ko]] · [[portfolio-ko]] — 정량 지표(85%+ 정확도, Google Play 출시)
- [[pandas-dev-pandas]] — ML 입력/출력의 도구 레이어 표준 (DataFrame), Pandera로 학습 데이터 검증, ecosystem.md의 skrub/Hamilton/Featuretools가 pandas → ML 다리
- [[scikit-learn-scikit-learn]] — sklearn 자체 소스 페이지, 거버넌스(SLEP)·5단 영속성 의사결정·생태계 30개+ 호환 라이브러리·AGENTS.md 정책

## 열린 질문

- AutoML 시대의 모델은 현재 운영 중인가? 재학습 주기와 정확도 추이는?
- LangGraph 에이전트의 토큰 사용량 추적과 비용 최적화는 어떤 패턴을 따르는가?
