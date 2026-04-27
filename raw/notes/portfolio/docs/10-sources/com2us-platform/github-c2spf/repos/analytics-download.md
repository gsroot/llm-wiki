---
title: "c2spf/analytics-download"
type: source-index
company: com2us-platform
source: github
repo: c2spf/analytics-download
visibility: private
primary_language: Python
collected_at: "2026-04-24"
---

# c2spf/analytics-download

빅쿼리 대용량 다운로드 JobQueue Worker 데몬 — ✅ 완료

## 기본 정보

| 항목 | 값 |
|------|----|
| URL | <https://github.com/c2spf/analytics-download> (private) |
| Visibility | private |
| Default Branch | `master` |
| 주 언어 | Python (~80KB), JavaScript (~21KB), HTML, CSS |
| 크기 | 5.9 MB |

## 내 기여

- **내 커밋**: **52** / 전체 319 (~16%)
- **기여 기간**: 2019-03-07 ~ 2019-05-16 (프로젝트 전담 구간)
- **역할**: 프로젝트 전담 — REST API 설계, 비동기 다운로드 워커 설계·구현

## README (원문 요약)

> # 대용량 다운로드  
> 빅쿼리 다운로드 JobQueue Worker 데몬  
> 참고: 사내 Confluence (pageId 170075783)

## 기술 스택 (old-portfolio.md + 언어 분포)

- **백엔드**: Python (Flask, Celery, Pandas, Pytest)
- **데이터베이스**: MySQL, Redis
- **클라우드**: GCP BigQuery, GCP Storage
- **용도**: 애널리틱스 세그먼트 스냅샷, 리포트 결과 등 대용량 데이터 REST API + 비동기 다운로드

## 관련 프로젝트 문서

- [`docs/20-projects/com2us-platform/2019-03-analytics-download-api.md`](../../../../20-projects/com2us-platform/) (on-demand)

## 관련 스킬

- `backend-python` (Flask, Celery)
- `data-pipeline` (Celery 비동기 워커, JobQueue 패턴)
- `database` (MySQL, Redis, BigQuery)
