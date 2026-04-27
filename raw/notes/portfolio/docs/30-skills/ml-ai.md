---
title: "ML/AI"
type: skill
category: ml-ai
slug: ml-ai
years_of_experience: 6
proficiency: proficient
related_stack:
  - GCP AutoML
  - GCP AutoML Tables
  - GCP AI Platform Pipeline
  - BigQuery ML
  - Pandas
  - NumPy
  - Scikit-learn
  - Jupyter Notebook
  - LangGraph
  - LangChain
  - OpenAI API
  - MCP
tags: [ml, ai, mlops, automl, llm, agent, langgraph]
---

# ML/AI

## 개요

AutoML 기반 유저 행동 예측 서비스(2020-08 ~ 2021-09)부터 최근 LLM/Agent 기반 개인 프로젝트(2025~)까지, ML 서비스의 **설계 → 데이터 전처리 → 모델링 → 프로덕션 배포 → UI 통합**을 단독으로 수행한 경험을 보유. `old-portfolio.md` ABOUT ME에 "ML 서비스의 설계부터 프로덕션 배포까지 경험한 ML 엔지니어입니다"라고 명시(L8).

최근에는 LangGraph 기반 AI 에이전트를 구글 플레이 스토어에 출시(트래블메이트)하고, OpenAI GPT 기반 소셜 메시징 플랫폼(Mate Chat)을 개발하며 LLM/Agent 실전 적용을 확장 중.

## 프로젝트 증거

### 컴투스플랫폼

| 프로젝트 | 기간 | ML/AI 역할 | 주요 스택 | 링크 |
|---------|------|------------|----------|------|
| 애널리틱스 ML 유저 예측 기능 | 2020-08 ~ 2021-09 | 풀스택 개발, 서비스 기획 및 AutoML 모델링 참여. 데이터 전처리부터 모델링까지 전 과정 수행 | GCP AutoML, BigQuery, GCP AI Platform Pipeline, Flask, Pandas, Jupyter Notebook | old-portfolio.md 참조 |
| 애널리틱스 React 리뉴얼 (AI 개발 생산성) | 2025-06 ~ 현재 | "AI 기반 개발 생산성 향상 가이드" Confluence 문서 작성 (170034641) — AI 활용 사례 기록 | Confluence, AI 도구 | [→](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |

### 개인 프로젝트

| 프로젝트 | 기간 | ML/AI 역할 | 주요 스택 |
|---------|------|------------|----------|
| 트래블메이트 (AI 여행 계획 Android 앱) | 2025-10 ~ 2025-11 | LangGraph 기반 AI 에이전트 통합 — 여행 일정 생성부터 데이터 저장까지 전 과정 자동화, 실시간 AI 응답 스트리밍, 토큰 기반 과금(1 Clover = 1,000 tokens). **구글 플레이 스토어 출시** | LangGraph, OpenAI API, FastAPI, PostgreSQL |
| Mate Chat (AI 소셜 메시징 플랫폼) | 2025-08 ~ 현재 | OpenAI GPT 기반 커스텀 AI 챗봇("AI Mates") — 성격 커스터마이징·대화, AI 사용량 추적(가상 화폐 "클로버") | OpenAI GPT API, FastAPI, WebSocket, PostgreSQL, Redis |

### 이전 프로젝트 (참조)

- **2016-02 ~ 2016-06 줌닷컴 사용자 데이터 분석**: HiveQL 기반 분산 시스템 쿼리·분석으로 유입·리텐션 전략 수립에 기여 (ML 이전 단계의 데이터 분석 경험, `old-portfolio.md` L234~239)
- **2016-03 ~ 2016-05 패스트캠퍼스 파이썬 데이터 분석 교육**: Pandas 기반 데이터 분석·시각화 과정 수료 (`old-portfolio.md` L70~75)
- **2019-01 ADSP(데이터분석 준전문가) 취득** — 한국데이터산업진흥원 (`old-portfolio.md` L92~95)

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| GCP AutoML (Tables) | proficient | 2020~2021 유저 예측 기능 프로덕션 모델링 — 평균 정확도 85%+ (old-portfolio.md L210) |
| GCP AI Platform Pipeline | proficient | 같은 프로젝트에서 MLOps 파이프라인 구축 (old-portfolio.md L209) |
| BigQuery ML | competent | `old-portfolio.md` SKILLS 섹션 ML Pipeline 목록 (L27) |
| Pandas / NumPy / Scikit-learn | proficient | ML 전처리, 애널리틱스 데이터 가공, 카카오톡 분석 앱 등 반복 활용 |
| Jupyter Notebook | proficient | ML 유저 예측 모델링, 탐색적 데이터 분석에 활용 (old-portfolio.md L209) |
| LangGraph | proficient | 트래블메이트 에이전트 프로덕션 출시 — 일정 생성부터 저장까지 자동화 |
| LangChain | competent | `old-portfolio.md` SKILLS 섹션 LLM/Agent 목록 (L26) |
| OpenAI API | proficient | 트래블메이트(LangGraph 연동), Mate Chat(AI 챗봇 코어) |
| MCP | learning | 2025년 이후 학습/도입 초기 — `old-portfolio.md` SKILLS 섹션 명시 (L26) |

## 대표 성과

- **유저 행동 예측 정확도 85%+ 평균 달성** — 이탈 방지 전략 수립에 직접 기여 (출처: `old-portfolio.md` L210 "예측 정확도를 평균 85% 이상 달성하여 사용자 이탈 방지 전략 수립에 기여").
- **예측 유저 추세와 리텐션의 반비례 관계 입증** — 데이터 기반 마케팅 전략 수립에 활용 (출처: `old-portfolio.md` L210).
- **MLOps 기반 시스템 구축** — AI Platform Pipeline 기반으로 이후 ML 요구사항에 대한 빠른 대응 체계 확보 (출처: `old-portfolio.md` L210).
- **LangGraph 에이전트 구글 플레이 스토어 출시** — AI 여행 계획 앱 트래블메이트를 실서비스로 론칭, 토큰 기반 과금 시스템과 서버 측 영수증 검증까지 구축 (출처: `old-portfolio.md` L263~266).
- **AI 기반 개발 생산성 향상 가이드 사내 공유** — Confluence 170034641 (React 리뉴얼 프로젝트 중 본인 작성, 출처: 2025-06 프로젝트 문서 sources).

## 관련 스킬 문서

- [`backend-python.md`](./backend-python.md) — Python 백엔드 기반 위에 ML/AI 적재
- [`data-pipeline.md`](./data-pipeline.md) — 학습 데이터 수집·적재 파이프라인

## 출처

- `old-portfolio.md` L8 (ABOUT ME), L22~29 (SKILLS — ML/AI), L203~210 (ML 유저 예측), L252~266 (Mate Chat, 트래블메이트)
- `docs/20-projects/com2us-platform/2025-06-analytics-react-renewal.md` — Confluence 170034641 AI 가이드 참조
