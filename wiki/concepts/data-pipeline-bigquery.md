---
title: "데이터 파이프라인 (BigQuery 중심 BI)"
type: concept
category: data
tags: [data-pipeline, bigquery, mysql, redis, mariadb, hiveql, digdag, celery, airflow, BI, mmp]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[backend-python-fastapi]]"
  - "[[ml-ai]]"
source_count: 4
created: 2026-04-24
updated: 2026-04-24
---

# 데이터 파이프라인 (BigQuery 중심 BI)

## 정의

GCP BigQuery를 핵심 데이터 웨어하우스로 두고, 게임 로그 수집·가공·시각화 전 과정을 통합하는 데이터 레이어. 운영 DB(MySQL/MariaDB)·캐시(Redis) 계층과 분석 DB(BigQuery)가 워크플로 도구(Digdag · Celery · Airflow)와 결합해 **실시간 운영 + 배치 분석**을 함께 지원한다.

## 왜 중요한가

- **9년 이상 누적 운영** — 2017년부터 c2spf 애널리틱스의 핵심 데이터 백본으로 BigQuery를 사용. 게임 BI의 원천.
- BI 시각화·예측·다운로드·MMP 결합 등 **모든 분석 기능의 단일 진실 공급원(single source of truth)**.
- 8년 이상 BigQuery 위에서 운영을 지속하며 누적된 운영 노하우 — Decimal 변환, 슬레이브 동기화, 피벗 NULL 처리 등.

## 핵심 내용

- **저장소 계층**
  - Operational: MySQL · MariaDB · PostgreSQL · Redis (캐시/큐)
  - Analytical: GCP BigQuery (메인), GCP Storage (다운로드 결과 파일).
- **수집/가공**
  - 게임 클라이언트 로그 → 로그 수집 파이프라인 → BigQuery 저장.
  - Airbridge MMP 데이터 결합으로 광고 성과 분석 (2025-01).
  - HiveQL 기반 분산 쿼리 경험(줌인터넷).
- **워크플로 오케스트레이션**
  - Digdag (게임 정보 동기화 스케줄러, 2018-07~08).
  - Celery (대용량 다운로드 비동기 워커, 2019).
  - GCP AI Platform Pipeline (ML 예측 MLOps, 2020~2021).
- **운영 트릭**
  - BigQuery `Decimal` 타입 변환 규칙 정립.
  - 피벗 축 NULL 플레이스홀더 처리.
  - 슬레이브 DB 동기화 지연 대응(쿼리 라우팅, 재시도).
  - OS별 TCP Keepalive 설정 차이.

## 실전 적용

- **`/common/processed-data` 단일 엔드포인트** — BigQuery + Airbridge 결합·피벗팅 로직.
- **APIResponse + ProcessedData result_code** — 데이터 처리 결과를 4종 코드로 정형화.
- **BigQuery ML / AutoML Tables** — 게임 유저 이탈/구매 예측 (정확도 평균 85%+).
- **BigQuery + GCP Storage** — 대용량 데이터 다운로드 파이프라인 (Celery 비동기 워커).

## 관련 개념

- [[backend-python-fastapi]] — 백엔드가 BigQuery·MySQL·Redis 호출
- [[ml-ai]] — BigQuery → AutoML → AI Platform Pipeline 파이프라인의 데이터 소스
- [[devops-cicd]] — Promtail/Loki/Grafana로 데이터 파이프라인 로그 관측

## 출처

- [[portfolio-seed]] — 9년차 BigQuery 운영 타임라인
- [[portfolio-ko]] — Selected Work 5선의 데이터 측면
- [[c2spf-analytics-common]] — 공통 모듈에서의 BigQuery 운영 디테일
- [[c2spf-analytics-renewal]] — Airbridge × BigQuery 결합 파이프라인

## 열린 질문

- BigQuery의 비용 최적화 패턴(파티셔닝·클러스터링)은 어떤 기준으로 적용되었는가?
- HiveQL 시대 → BigQuery 전환 시 마이그레이션 비용/이득은?
