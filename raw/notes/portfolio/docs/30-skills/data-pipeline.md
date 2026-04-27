---
title: "Data Pipeline"
type: skill
category: data-pipeline
slug: data-pipeline
years_of_experience: 8
proficiency: expert
related_stack:
  - GCP BigQuery
  - GCP Storage
  - Celery
  - Airflow
  - Digdag
  - Pandas
  - SQLAlchemy
  - Promtail
  - Loki
  - Grafana
  - Fluentd
  - ElasticSearch
  - Kibana
  - Redis
tags: [data-pipeline, etl, bigquery, airflow, celery, digdag, logging, observability]
---

# Data Pipeline

## 개요

게임 로그 기반 애널리틱스(BI) 서비스의 **데이터 수집 → 가공 → 적재 → 시각화** 전 단계를 8년간 설계·운영해왔다. BigQuery를 중심으로 Celery·Digdag 등의 워크플로 도구와 Pandas 기반 가공, Promtail/Loki/Grafana 기반 로그 관측까지 엔드-투-엔드 책임 범위.

- `ABOUT ME`: "데이터 분석 서비스(BI)를 설계부터 운영까지 경험한 BI 엔지니어" (`old-portfolio.md` L9)
- 애널리틱스 본체 개발 2017-05 ~ 현재 (장기, `old-portfolio.md` L158~165)

## 프로젝트 증거

### 컴투스플랫폼

| 프로젝트 | 기간 | 파이프라인 역할 | 주요 스택 | 링크 |
|---------|------|----------------|----------|------|
| 애널리틱스 본체 (게임 데이터 분석 BI) | 2017-05 ~ 현재 | 풀스택 개발 — 세그먼트 결합, CSV 다운로드, 퍼널·코호트·커스텀 리포트. 게임 로그 수집·가공·시각화 전 구간 | BigQuery, GCP Storage, MySQL, Redis, Spring Boot (+ Python 일부) | old-portfolio.md L158~165 |
| 애널리틱스 React 리뉴얼 (공통 API) | 2025-06 ~ 현재 | 공통 API 계약(`DataCollection → ProcessedData`) 확립, 재사용 가능한 데이터 가공 엔드포인트 | FastAPI, BigQuery, Redis | [→](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| 애널리틱스 Airbridge 데이터 가공 API | 2025-01 ~ 2025-02 | BigQuery + Airbridge(MMP) 외부 광고 데이터 동시 실행·피벗팅·결합 | FastAPI, BigQuery, Airbridge, Pandas | [→](../20-projects/com2us-platform/2025-01-airbridge-api.md) |
| 애널리틱스 공통 모듈 & 배포 개선 (로깅 스택 포함) | 2024-08 ~ 2024-12 | `/common/processed-data` 엔드포인트 신설, **Promtail → Loki → Grafana** 4개 환경(상용 Primary/Standby·샌드박스·테스트) 구축 | FastAPI, BigQuery, Promtail, Loki, Grafana | [→](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| NFT 마켓 (관측 파이프라인) | 2022-05 ~ 2024-03 | Fluentd → ElasticSearch → Kibana 로그 파이프라인 구축 | Fluentd, ElasticSearch, Kibana | [→](../20-projects/com2us-platform/2022-05-nft-market.md) |

### 이전 프로젝트 (old-portfolio.md 기준)

| 프로젝트 | 기간 | 파이프라인 역할 | 주요 스택 |
|---------|------|----------------|----------|
| ML 유저 예측 (MLOps 파이프라인) | 2020-08 ~ 2021-09 | GCP AI Platform Pipeline 기반 학습·예측 파이프라인, Digdag 스케줄링 | GCP AI Platform Pipeline, BigQuery, Digdag |
| 대용량 데이터 다운로드 REST API/비동기 워커 | 2019-03 ~ 2019-06 | Celery 기반 비동기 워커 — 세그먼트 스냅샷·리포트 대용량 데이터 다운로드 자동화 | Celery, Pandas, BigQuery, GCP Storage |
| 게임 정보 동기화 스케줄러 | 2018-07 ~ 2018-08 | Digdag 워크플로 + Python 스크립트 — 앱센터 API → 애널리틱스 DB + BigQuery 동기화 | Digdag, Pandas, SQLAlchemy, BigQuery |

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| GCP BigQuery | expert | 애널리틱스 본체 장기 운영(2017~), 공통 API `/common/processed-data`에서 BigQuery 쿼리 결합·피벗팅 표준화 |
| GCP Storage | proficient | 대용량 다운로드 워커(2019), 애널리틱스 본체 기술 스택에 명시 (old-portfolio.md L164) |
| Celery | proficient | 대용량 다운로드 비동기 워커(2019), `old-portfolio.md` SKILLS — Workflow (L29) |
| Airflow | proficient | `old-portfolio.md` SKILLS — Workflow 섹션 (L29) |
| Digdag | proficient | 게임 정보 동기화 스케줄러(2018), ML 유저 예측(2020) 등 다년간 활용 |
| Pandas / SQLAlchemy | proficient | ETL 전 과정에서 가공/적재 범용 활용 |
| Promtail / Loki / Grafana | proficient | 2024-08 공통 모듈 프로젝트에서 4개 환경 Loki 인스턴스 운영 + Jenkinsfile 배포 자동화 |
| Fluentd / ElasticSearch / Kibana | competent | NFT 마켓 로그 파이프라인 구축 |
| Redis | proficient | HIVE OAuth 인증 캐시(`/hive/auth/games`), 공통 API 캐시 패턴 매칭 무효화 |

## 대표 성과

- **공통 가공 엔드포인트 설계·표준화**: `POST /common/processed-data` 하나로 BigQuery·Airbridge 쿼리를 결합·피벗팅하여 `index/columns/data/summary_stats(sum/mean/max/min)/date_type`까지 반환하는 계약을 확립 — AG-grid가 바로 렌더링 가능 (출처: Confluence 35568348, 2025-01 프로젝트 문서).
- **4개 환경 로깅 스택 단독 구축**: Promtail(WAS 사이드카) → Loki(상용 Primary/Standby·샌드박스·테스트 분리) → Grafana 중앙 조회 구조를 Docker로 운영, Loki 배포용 Jenkinsfile까지 작성 (출처: 2024-08 프로젝트 문서 Action/Result).
- **대용량 다운로드 자동화**: Celery 비동기 워커로 사용자 수동 요청 과정을 자동화, 업무 효율 향상 (출처: `old-portfolio.md` L212~219).
- **분산 게임 정보 단일화**: Digdag 스케줄러로 각기 다른 위치에서 관리되던 게임 정보를 항상 최신 동기화 상태로 유지, 사용자 혼란 방지 (출처: `old-portfolio.md` L221~228).
- **BigQuery 운영 안정화 지속 개선**: Decimal 타입 변환, 피벗 축 NULL 플레이스홀더 대체, `date_type=MINUTE`일 때 `minute_interval` 검증, 슬레이브 동기화 이슈 대응 등 (출처: `analytics-common-api` 커밋 근거, 2024-08 문서).

## 관련 스킬 문서

- [`backend-python.md`](./backend-python.md) — 파이프라인 코드의 주 구현 언어
- [`ml-ai.md`](./ml-ai.md) — 파이프라인 위에서 동작하는 AutoML/LLM 서비스

## 출처

- `old-portfolio.md` L9 (ABOUT ME — BI 엔지니어), L27~29 (SKILLS — ML Pipeline/Workflow), L158~165 (애널리틱스 본체), L203~228 (ML/다운로드/동기화), L177~183 (NFT 로그 파이프라인)
- `docs/20-projects/com2us-platform/2024-08-analytics-common-module.md` — 로깅 스택 4개 환경, BigQuery 처리 결과 코드
- `docs/20-projects/com2us-platform/2025-01-airbridge-api.md` — BigQuery + Airbridge 결합 처리
