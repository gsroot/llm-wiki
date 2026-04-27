---
title: "Backend — Python"
type: skill
category: backend
slug: backend-python
years_of_experience: 9
proficiency: expert
related_stack:
  - FastAPI
  - Django
  - Flask
  - SQLAlchemy
  - Alembic
  - Pytest
  - Celery
  - Pandas
  - Discord.py
  - Locust
tags: [python, backend, async, api, fastapi, flask]
---

# Backend — Python

## 개요

Python 기반 백엔드 서비스를 9년간 설계·개발해온 주력 스택. 게임 데이터 분석(BI) 공통 API, 광고 MMP 데이터 결합 파이프라인, 가상자산 트래블룰(규제) API, 블록체인 Discord 인증 봇, 대용량 비동기 다운로드 워커, 통합 인증 모듈, AI 챗봇/에이전트(개인 프로젝트)까지 **FastAPI / Flask / SQLAlchemy / Pytest / Celery** 계열을 프로덕션 규모로 운영해왔다.

- 단독 유지보수 경험: `c2spf/analytics-common-api` 저장소 본인 커밋 **231 / 251 ≈ 92%** (2024-09 ~ 2026-04 진행 중)
- `ABOUT ME` 중 "Python 기반 백엔드 서비스와 데이터 파이프라인을 설계·개발" (`old-portfolio.md` L7)

## 프로젝트 증거

### 컴투스플랫폼 (재직 2017-05 ~ 현재)

| 프로젝트 | 기간 | 파이썬 역할 | 주요 스택 | 링크 |
|---------|------|------------|----------|------|
| 애널리틱스 React 리뉴얼 (공통 API 구간) | 2025-06 ~ 현재 | FastAPI 공통 API 단독 유지보수, React 프런트와의 API 계약 확립 | FastAPI, SQLAlchemy, BigQuery, Redis | [→](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| 애널리틱스 Airbridge 데이터 가공 API | 2025-01 ~ 2025-02 | FastAPI `/common/processed-data`에 `AirbridgeData` 모델 + 피벗팅 로직 추가, BigQuery·Airbridge 결합 | FastAPI, Pandas(피벗), BigQuery | [→](../20-projects/com2us-platform/2025-01-airbridge-api.md) |
| 애널리틱스 공통 모듈 & 배포 개선 | 2024-08 ~ 2024-12 | FastAPI 공통 API 신규 설계·구현 (APIResponse 표준, 결과 코드 체계, HIVE OAuth 통합, 권한 CRUD) | FastAPI, SQLAlchemy, Redis, BigQuery | [→](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| NFT 마켓 Discord 홀더 인증 봇 | 2022-05 ~ 2024-03 | Discord.py + FastAPI 인증 엔드포인트 분리, Pytest 회귀 보장 | Discord.py, FastAPI, Pytest, MySQL, Redis | [→](../20-projects/com2us-platform/2022-05-nft-market.md) |

### 이전 컴투스플랫폼 프로젝트 (old-portfolio.md 기준)

| 프로젝트 | 기간 | 파이썬 역할 | 주요 스택 |
|---------|------|------------|----------|
| CODE 트래블룰 API | 2021-10 ~ 2022-04 | 가상자산 거래소 간 트래블룰 공통 API — 웹/블록체인 버전, Sample VASP API | FastAPI, SQLAlchemy, Pytest, Locust |
| 통합 인증 & 비동기 통신 공통 모듈 | 2021-06 ~ 2021-07 | 기획·설계·풀스택. Pub/Sub → REST API 모듈화 | Flask, SQLAlchemy, Pytest |
| ML 유저 예측 기능 | 2020-08 ~ 2021-09 | Flask 풀스택 + AutoML 모델링 | Flask, Pandas, Jupyter, SQLAlchemy, Pytest |
| 대용량 데이터 다운로드 REST API / 비동기 워커 | 2019-03 ~ 2019-06 | REST API + Celery 워커 설계·개발 | Flask, Celery, Pandas, Pytest |
| 게임 정보 동기화 스케줄러 | 2018-07 ~ 2018-08 | Digdag + Python 스크립트로 BigQuery/DB 동기화 | Pandas, SQLAlchemy, Pytest |

### 개인 프로젝트

| 프로젝트 | 기간 | 파이썬 역할 | 주요 스택 |
|---------|------|------------|----------|
| Mate Chat (AI 기반 소셜 메시징 플랫폼) | 2025-08 ~ 현재 | FastAPI 백엔드, Repository/Service 계층, JWT + OAuth 2.0, WebSocket 실시간 메시징, Alembic 마이그레이션 | FastAPI, SQLAlchemy, Alembic, Pytest, PostgreSQL, Redis, uv |
| 트래블메이트 (AI 여행 계획 앱) | 2025-10 ~ 2025-11 | FastAPI + LangGraph 에이전트, 스트리밍 응답, 가상화폐 과금 시스템, Google Play 영수증 검증 | FastAPI, SQLAlchemy, Alembic, Pytest, LangGraph, PostgreSQL, uv |
| 카카오톡 대화 분석 앱 | 2023-01 ~ 2023-08 | FastAPI + Pandas 기반 대화 통계 분석 API | FastAPI, Pandas, Pytest |

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| FastAPI | expert | 공통 API 단독 유지보수(92%), Airbridge API, NFT Discord 봇, Mate Chat, 트래블메이트 등 주력 프레임워크 |
| Flask | proficient | ML 유저 예측, 대용량 다운로드, 통합 인증 등 2019~2021년 주력 프레임워크 |
| SQLAlchemy / Alembic | expert | 상용 서비스부터 개인 프로젝트까지 일관 사용. Alembic으로 스키마 마이그레이션 운영 |
| Pytest | proficient | 전 프로젝트에서 회귀 테스트 스위트 유지 (old-portfolio.md 기재) |
| Celery | proficient | 대용량 다운로드 비동기 워커(2019), 애널리틱스 워크플로 (SKILLS 섹션 Workflow) |
| Pandas | proficient | BigQuery·Airbridge 결과 피벗팅, ML 전처리, 카카오톡 분석 등 데이터 가공 범용 활용 |
| Discord.py | competent | NFT 마켓 Discord 홀더 인증 봇 상용화 |
| Locust | competent | CODE 트래블룰 API 부하 테스트 |
| Django | competent | `old-portfolio.md` SKILLS 섹션 Framework 목록 (개인·학습 경험 중심) |
| uv (패키지 매니저) | proficient | 2025년 개인 프로젝트 2종에서 표준 도입 |

## 대표 성과

- **공통 API 단독 유지보수 체계**: `c2spf/analytics-common-api` 본인 커밋 **231/251 ≈ 92%** — 저장소 단독 유지보수 수준으로 경계 설계·응답 포맷·OAuth 통합을 단독 주도 (출처: 2024-08 / 2025-01 프로젝트 문서, `github-c2spf/repos/analytics-common-api.md`).
- **API 응답 규약 표준화**: `APIResponse { result_code, message, data }` + `APICode` 13종 + `ProcessedData.result_code` 4종(BigQuery 오류 분리) 정립 (출처: Confluence 35568348).
- **하이브리드 스택 전략**: Airbridge 프로젝트에서 기존 Spring Boot 리포트 백엔드를 유지하면서 데이터 가공 파트만 FastAPI 공통 API로 분리하여 리팩토링 리스크를 줄이고 Pandas 기반 피벗·집계 이점을 확보 (출처: 2025-01 프로젝트 문서).
- **Google Play 출시**: LangGraph + FastAPI 기반 트래블메이트 앱을 스토어에 출시, 서버 측 영수증 검증 결제 시스템 구축 (출처: `old-portfolio.md` L263~266).

## 관련 스킬 문서

- [`ml-ai.md`](./ml-ai.md) — Python 기반 ML/AI 서비스 (AutoML, LangGraph)
- [`data-pipeline.md`](./data-pipeline.md) — Celery / Pandas 기반 데이터 파이프라인

## 출처

- `old-portfolio.md` — 경력/스킬 요약 (L7 "Python 기반 백엔드", L35 언어/프레임워크, 프로젝트별 기술 스택)
- `docs/20-projects/com2us-platform/*.md` — 프로젝트별 YAML `tech_stack` 및 STAR 본문
- `docs/10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md` — 커밋 비중 근거
