# 30-skills — 스킬 택소노미 & 역매핑

**Synthesis Layer**: 스킬 → 이를 증명하는 프로젝트로의 **역링크 뱅크**입니다. 이력서의 "보유 기술" 줄 하나가 실제 프로젝트로 즉시 검증 가능해집니다.

## 스킬 카테고리

| 카테고리 | 스킬 예시 | 파일 |
|---------|---------|------|
| **Backend** | Python (FastAPI, Django, Flask), Java (Spring Boot), Node.js (NestJS) | `backend-python.md`, `backend-java-spring.md`, `backend-nodejs.md` |
| **Frontend** | React, TypeScript, ag-grid, jQuery | `frontend-react.md`, `frontend-vanilla-js.md` |
| **ML/AI** | AutoML, LangGraph, OpenAI API, Pandas, BigQuery ML | `ml-ai.md` |
| **Data Pipeline** | Airflow, Digdag, Celery, BigQuery | `data-pipeline.md` |
| **DevOps** | Docker, Jenkins, GitHub Actions | `devops-container.md`, `devops-cicd.md` |
| **Database** | MySQL, PostgreSQL, MariaDB, Redis | `database.md` |
| **Blockchain** | NFT, Smart Contract, Web3, Rust | `blockchain.md` |
| **Mobile** | Flutter, Dart, Firebase | `mobile-flutter.md` |

## 스킬 문서 스키마

각 스킬 문서는 [`docs/00-meta/document-conventions.md`](../00-meta/document-conventions.md)의 `type: skill` 스키마를 따름:

```yaml
---
title: "Backend — Python"
type: skill
category: backend
slug: backend-python
years_of_experience: 9
proficiency: expert
related_stack: [FastAPI, Django, Flask]
tags: [python, backend]
---
```

본문에는:
1. 해당 스킬을 사용한 프로젝트 **테이블** (링크 포함)
2. 관련 **STAR 스토리** 링크 (`40-stories/`)
3. 관련 정량 지표 (해당 스킬로 달성한 metrics)

## 작성 순서

1. [`20-projects/`](../20-projects/) 완성 후 스킬 문서 작성
2. 해당 스킬이 등장하는 프로젝트 모두 스캔 → 테이블에 기입
3. `40-stories/` 스토리가 있으면 연결
4. 정량 지표 집계

## 우선순위

이력서·포트폴리오 빈도가 높은 순:
1. `backend-python.md` (주력 언어)
2. `ml-ai.md` (차별화 포인트)
3. `data-pipeline.md` (Analytics 도메인 전문성)
4. `frontend-react.md` (최근 리드 경험)
5. `blockchain.md` (비중 있는 경험)
6. 나머지
