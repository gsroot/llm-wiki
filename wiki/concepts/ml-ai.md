---
title: "ML/AI (GCP AutoML · AI Platform Pipeline · LangGraph · OpenAI API)"
type: concept
category: ai
tags: [ml, ai, automl, gcp, ai-platform-pipeline, langgraph, langchain, openai, llm, mlops, prediction]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[data-pipeline-bigquery]]"
  - "[[mcp]]"
source_count: 3
created: 2026-04-24
updated: 2026-04-24
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
- **데이터 분석 도구**: Pandas, NumPy, Scikit-learn, Jupyter Notebook (지속적).

## 실전 적용

- **유저 예측에서 마케팅 전략으로**: 이탈 예측을 마케팅 캠페인 타겟팅에 적용.
- **AI 에이전트에서 모바일 앱 수익화로**: LangGraph 워크플로 + 토큰 과금 + 인앱결제 결합.
- **Pandas 데이터 처리**: 카카오톡 대화 분석 앱 등 개인 프로젝트에서 Plotly 시각화와 결합.

## 관련 개념

- [[data-pipeline-bigquery]] — ML 학습 데이터 소스
- [[backend-python-fastapi]] — ML 서비스 백엔드 (Flask에서 FastAPI로)
- [[mcp]] — LLM 도구 호출 프로토콜

## 출처

- [[portfolio-seed]] — AutoML/AI Platform Pipeline 시대 + LLM/Agent 시대 양쪽
- [[portfolio-resume-ko]] · [[portfolio-ko]] — 정량 지표(85%+ 정확도, Google Play 출시)

## 열린 질문

- AutoML 시대의 모델은 현재 운영 중인가? 재학습 주기와 정확도 추이는?
- LangGraph 에이전트의 토큰 사용량 추적과 비용 최적화는 어떤 패턴을 따르는가?
