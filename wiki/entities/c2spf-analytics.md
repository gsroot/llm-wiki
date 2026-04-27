---
title: "c2spf 애널리틱스 (게임 데이터 BI)"
type: entity
entity_type: service
tags: [analytics, c2spf, 애널리틱스, BI, 게임데이터, fastapi, react, bigquery, ag-grid]
related:
  - "[[com2us-platform]]"
  - "[[seokgeun-kim]]"
  - "[[backend-python-fastapi]]"
  - "[[frontend-react]]"
  - "[[data-pipeline-bigquery]]"
  - "[[devops-cicd]]"
source_count: 4
created: 2026-04-24
updated: 2026-04-24
---

# c2spf 애널리틱스 (게임 데이터 BI)

## 개요

컴투스플랫폼이 운영하는 게임 데이터 분석 BI 웹 서비스. 회사 내 모든 게임에서 발생하는 로그 데이터를 수집·분석하여 대시보드·리포트·세그먼트·퍼널·코호트·ML 예측 등의 분석 기능으로 제공한다. 2017년부터 운영되어 왔으며, 김석근이 풀스택 개발 주축으로 다수 모듈을 단독 유지보수.

## 주요 특징

- **레포지토리 군** (`c2spf` GitHub 조직 내)
  - `analytics-frontend` — UI. 2025-06부터 React + TypeScript + Vite 기반으로 리뉴얼. 본인 476커밋 (~24%).
  - `analytics-common-api` — 데이터 가공·시각화·HIVE OAuth 공통 API. FastAPI 기반. 본인 231/251 커밋 (~92%).
  - `analytics-prediction` — ML 유저 예측 (이탈/구매 예측, AutoML 기반).
  - `analytics-mobile-report` — 모바일 리포트.
  - `analytics-download` — 대용량 데이터 다운로드 REST API + Celery 비동기 워커.
- **핵심 분석 기능**
  - 차트 / 퍼널 / 리텐션 / 대시보드 (4대 분석 기능, 2025-06 리뉴얼로 "생성·조회·수정" 구조 표준화).
  - 세그먼트 결합 / CSV 다운로드 / 코호트 / 커스텀 리포트.
  - ML 유저 예측 (이탈/구매, GCP AutoML + AI Platform Pipeline 기반 MLOps).
  - Airbridge MMP 결합 광고 성과 분석 (2025-01 추가).
- **기술 스택**
  - Backend: Python (FastAPI), Java (Spring Boot, MyBatis, JPA)
  - Frontend: React + TypeScript + Vite + TanStack + Zustand + ag-grid + Highcharts (구 jQuery/Mobx)
  - Data: GCP BigQuery, MySQL, Redis
  - DevOps: Docker Compose, Jenkins Multi-branch, Promtail/Loki/Grafana 4환경
  - 인증: HIVE OAuth (사내 인증 시스템) 8개 엔드포인트 통합

## 관련 개념

- [[com2us-platform]] — 운영 회사
- [[seokgeun-kim]] — 주축 개발자
- [[backend-python-fastapi]] — 공통 API 스택
- [[frontend-react]] — 2025-06 리뉴얼 표준
- [[data-pipeline-bigquery]] — BI 데이터 파이프라인
- [[devops-cicd]] — Jenkins + Docker 표준화
- [[ml-ai]] — analytics-prediction 모듈

## 출처

- [[portfolio-seed]] — 애널리틱스 본체(2017~) + 다운로드 API + ML 예측 + 공통 모듈 + 리뉴얼 등 다년 역사
- [[portfolio-ko]] — Selected Work 5선 중 3개가 애널리틱스 관련
- [[c2spf-analytics-common]] — 공통 모듈 & 배포 프로세스 (2024-08~)
- [[c2spf-analytics-renewal]] — Airbridge API + React 리뉴얼 (2025)

## 논쟁/모순

(없음)

## 메모

- 9년차 운영 중인 장기 시스템 — 단순 코드 외에 데이터 모델, API 계약, 운영 가이드가 함께 누적된 복합 자산.
- 2024-08 공통 모듈 리뉴얼이 이후 모든 리포트·대시보드 기능의 기반이 됨. APIResponse·APICode·ProcessedData 계약이 횡단.
