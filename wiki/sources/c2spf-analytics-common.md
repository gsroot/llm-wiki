---
title: 컴투스플랫폼 애널리틱스 공통 모듈 & 배포 프로세스 (2024-08)
type: source
source_type: note
source_url: ''
source_scope: local
raw_path: raw/notes/portfolio/docs/20-projects/com2us-platform/2024-08-analytics-common-module.md
author: 석근
date_published: 2026-04-24
date_ingested: 2026-04-24
tags:
- com2us-platform
- c2spf
- analytics
- fastapi
- spring-boot
- ag-grid
- jenkins
- docker
- loki
- grafana
related:
- '[[com2us-platform]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-kim]]'
- '[[backend-python-fastapi]]'
- '[[devops-cicd]]'
- '[[data-pipeline-bigquery]]'
confidence: high
inbound_count: 28
aliases:
- C2Spf Analytics Common
- c2spf analytics common
- 컴투스플랫폼 애널리틱스 공통 모듈 & 배포 프로세스 (2024-08)
cited_by:
  - "[[api-response-envelope]]"
  - "[[backend-python-fastapi]]"
  - "[[c2spf-ai-agent-adoption-candidates]]"
  - "[[c2spf-analytics]]"
  - "[[career-timeline-seokgeun]]"
  - "[[com2us-platform]]"
  - "[[data-pipeline-bigquery]]"
  - "[[devops-cicd]]"
  - "[[portfolio]]"
  - "[[seokgeun-kim]]"
cited_by_count: 10
---

# 컴투스플랫폼 애널리틱스 공통 모듈 & 배포 프로세스 (2024-08)

## 한줄 요약

> 2024-08 ~ 2024-12(+ 이후 지속 유지보수), 데이터 시각화 공통 API(FastAPI)와 공통 JavaScript 모듈을 신규 설계·개발해 중복 제거하고, Docker Compose + Jenkins 멀티브랜치 파이프라인 + Promtail/Loki/Grafana 4환경 로깅 스택을 팀 표준으로 정립한 프로젝트.

## 핵심 내용

- **기간/역할**: 2024-08 ~ 2024-12(+ 유지보수). 시각화 공통 API + 공통 JS 모듈 설계·개발, Docker + Jenkins 멀티브랜치 배포 표준화, 로깅 스택 구축 — 단일 담당자.
- **기술 스택**: Java(Spring Boot), JavaScript, Python(FastAPI), MySQL, Redis, GCP BigQuery, AG-grid, Docker Compose, Jenkins Multi-branch, Promtail/Loki/Grafana.
- **핵심 성과**
 - `c2spf/analytics-common-api` **커밋 231/251 ≈ 92%** — 거의 단독 유지보수.
 - APIResponse `{result_code, message, data}` 표준 포맷 + **APICode 13종** + BigQuery ProcessedData 결과 코드 4종 정립.
 - **HIVE OAuth 8개 엔드포인트**를 공통 API에 통합 — 토큰·사용자·메뉴 권한·게임 권한. `/hive/auth/games`는 Redis 캐시 기반 최적화, 패턴 매칭 무효화 지원.
 - **배포/운영 가이드 4종 2024-10~11 집중 발행** — 공통 API 명세, 공통 JS, Jenkins 멀티브랜치, Docker Compose.
 - Promtail → Loki → Grafana 4환경(상용 Primary/Standby·샌드박스·테스트) 로그 중앙 집중화 → SSH 수동 검색에서 Grafana 레이블 필터링으로 전환.
 - 운영 개선: BigQuery Decimal 타입 변환, 피벗 축 NULL 플레이스홀더, OS별 TCP Keepalive, 슬레이브 DB 동기화 이슈 대응.
- **증거**
 - `docs/20-projects/com2us-platform/2024-08-analytics-common-module.md` — 통합 문서
 - `docs/40-stories/impact-analytics-common-module.md` — 임팩트 STAR 스토리
 - GitHub c2spf: analytics-common-api, analytics-frontend, analytics-prediction 등
 - Confluence 페이지 35568348 · 35568344 · 35568328 · 35568336 · 35568340 · 35568332 (본문 일부 수집)
 - Jira: GCPPDTDW-2386(상위 Story), GCPSRE-16239, GCPSRE-15853, GCPHDBA-2820 등

## 주요 인사이트

- "92% 커밋 점유율"은 단독 오너십을 뚜렷이 보여주는 지표. 공통 API가 사실상 개인 주도 프로젝트였음을 정량화.
- **표준화 가이드 4종을 한 달 안에 집중 발행(2024-10~11)** — 개발과 문서화를 병행한 비선형 워크플로. 이후 팀의 배포 표준이 이 가이드를 근거로 운영됨.
- HIVE OAuth 통합은 "공통 API 범위 확장"의 대표 예시. 단순 시각화 API에서 권한·인증까지 포괄하는 플랫폼 API로 진화.

## 관련 엔티티/개념

- [[c2spf-analytics|c2spf 게임 데이터 BI]] — 서비스 주체
- [[com2us-platform|컴투스플랫폼 c2spf]] — 소속
- [[seokgeun-kim|석근 (이 위키 owner)]] — 담당자
- [[backend-python-fastapi]] — 주력 스택
- [[devops-cicd]] — Docker + Jenkins 표준화
- [[data-pipeline-bigquery]] — BI 데이터 파이프라인

## 메모

- 원본 경로: `raw/notes/portfolio/docs/20-projects/com2us-platform/2024-08-analytics-common-module.md`.
- 이후 프로젝트(Airbridge API, React 리뉴얼)의 기반이 됨 — APIResponse envelope와 FastAPI 공통 API가 이후 재사용됨.
