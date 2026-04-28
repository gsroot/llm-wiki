---
title: "ML/AI (GCP AutoML · AI Platform Pipeline · LangGraph · OpenAI API)"
type: concept
category: ai
tags: [ml, ai, automl, gcp, ai-platform-pipeline, langgraph, langchain, openai, llm, mlops, prediction, pandas, scikit-learn, sklearn, dataframe, slep, fit-predict, openai-cookbook, openai-agents-python, embeddings, agents-sdk, prompt-caching, gpt-5, gpt-oss, multi-agent-framework, guardrails, human-in-the-loop]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[data-pipeline-bigquery]]"
  - "[[mcp]]"
  - "[[pandas]]"
  - "[[scikit-learn]]"
  - "[[openai]]"
  - "[[openai-cookbook]]"
  - "[[openai-agents-python]]"
source_count: 7
created: 2026-04-24
updated: 2026-04-28
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
  - **OpenAI Cookbook 사례 검색** ([[openai-cookbook]]) — 4년차 ★73K 저장소(289 콘텐츠 / 115명 저자)가 회사 BI에서 OpenAI API 도입 의사결정의 1차 자료. registry.yaml 태그 분포가 정확한 진화 화석 (embeddings 99 / completions 94 / responses 32 / agents-sdk 16 / mcp 8 / gpt-oss 13). 후보 기능 도입 시 같은 태그 ipynb cherry-pick → 회사 데이터 재현 → AGENTS.md "Recent Learnings"의 함정 사전 확인이 표준 워크플로우. `articles/Prompt_Caching101.ipynb` + `Prompt_Caching_201.ipynb`은 [[prompt-cache]] 정량 데이터 보강 1차 자료, `examples/agents_sdk/session_memory.ipynb`은 [[context-engineering]] OpenAI Sessions API 사례.
  - **gpt-oss + 한국어 fine-tuning** — `articles/gpt-oss/fine-tune-korean.ipynb` (45.9KB)이 한국어 task fine-tune 1차 자료. 한국어 BI 응용 ROI 평가 후속 후보.
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
- [[openai-openai-cookbook]] — OpenAI 공식 4년차 cookbook (★73K, 289 콘텐츠 / 115명 저자, MIT). LLM API 도입 의사결정 시 검색 가능한 사례 데이터베이스. embeddings(99건)·agents-sdk(16건)·responses(32건)·gpt-oss(13건)·mcp(8건) 태그가 4년 진화 화석. AGENTS.md "Recent Learnings" 살아있는 운영 노트 + PLANS.md ExecPlans 7시간+ 단일 작업 패턴 거버넌스 사례
- [[openai-openai-agents-python]] — OpenAI 공식 1년차 멀티 에이전트 Python SDK(★25K, v0.14.6, MIT). cookbook이 사례 데이터베이스라면 본 SDK는 **다중 에이전트 시스템 구축의 reference 라이브러리**. 회사 BI에 LLM 에이전트 적용 시 (예: BigQuery NL2SQL / 게임 데이터 분석 자동 보고 / 자율 모니터링 알림 트리아주) 본 SDK가 1차 후보. 핵심 가치: (1) **`examples/agent_patterns/` 16개 .py — 11종 패턴 reference 구현** (Anthropic 5 + OpenAI 6확장: Guardrails 3종 + Human-in-the-loop 3종 + Forced tool use), (2) **`docs/tools.md` 37.9KB** — 도구 시스템 전체 가이드 (BI 함수 호출 패턴 차용 가능), (3) **`mcp>=1.19.0` 디폴트 의존성** — MCP 서버를 BI 도메인 도구로 wrap 가능, (4) **RunState `CURRENT_SCHEMA_VERSION`** — BI 세션·캐시 직렬화 패턴 차용. 9개 운영 SOP 스킬 중 4개(`code-change-verification`/`docs-sync`/`runtime-behavior-probe`/`pr-draft-summary`)가 c2spf-analytics SOP에 직접 매핑

## 열린 질문

- AutoML 시대의 모델은 현재 운영 중인가? 재학습 주기와 정확도 추이는?
- LangGraph 에이전트의 토큰 사용량 추적과 비용 최적화는 어떤 패턴을 따르는가?
