---
title: "컴투스플랫폼 애널리틱스 React 리뉴얼 + Airbridge API (2025)"
type: source
source_type: note
source_url: ""
source_scope: local
raw_path: "raw/notes/portfolio/docs/20-projects/com2us-platform/"
author: "석근"
date_published: 2026-04-24
date_ingested: 2026-04-24
tags: [com2us-platform, c2spf, analytics, react, typescript, vite, tanstack, zustand, ag-grid, airbridge, fastapi, mmp]
related:
  - "[[com2us-platform]]"
  - "[[c2spf-analytics]]"
  - "[[seokgeun-kim]]"
  - "[[frontend-react]]"
  - "[[backend-python-fastapi]]"
  - "[[data-pipeline-bigquery]]"
confidence: high
cited_by:
  - "[[backend-python-fastapi]]"
  - "[[c2spf-ai-agent-adoption-candidates]]"
  - "[[c2spf-analytics]]"
  - "[[career-timeline-seokgeun]]"
  - "[[com2us-platform]]"
  - "[[data-pipeline-bigquery]]"
  - "[[frontend-react]]"
  - "[[microsoft-data-science-for-beginners]]"
  - "[[microsoft-web-dev-for-beginners]]"
  - "[[pandas-dev-pandas]]"
  - "[[portfolio]]"
---

# 컴투스플랫폼 애널리틱스 React 리뉴얼 + Airbridge API (2025)

## 한줄 요약

> 2025-01 Airbridge MMP 데이터 가공 API에서 2025-06 팀 최초 React 기반 프론트엔드 아키텍처 리뉴얼로 이어지는 연속 프로젝트. APIResponse + ProcessedData 계약을 React 리뉴얼까지 재사용하며, 차트·퍼널·리텐션·대시보드 4대 분석 기능을 "생성·조회·수정" 구조로 재설계했다.

## 핵심 내용

### Airbridge 데이터 가공 API (2025-01 ~ 2025-02)

- **역할**: 단일 담당자. 데이터 가공 API 설계·개발·운영.
- **스택**: Java(Spring Boot, MyBatis, JPA 다중 소스), Python(FastAPI), MySQL, Redis, GCP BigQuery, AG-grid, Docker, Jenkins, Promtail/Loki/Grafana.
- **성과**
  - `/common/processed-data` 단일 엔드포인트에 **BigQuery + Airbridge 결합·피벗팅** 로직 추가.
  - `DataCollection → ProcessedData` 계약 정립 — 이후 React 리뉴얼·대시보드 기능까지 재사용.
  - Spring Boot 리포트 계층 + FastAPI 공통 API의 **하이브리드 파이프라인** 구축.
  - 에러 코드 이원화(APICode 1001~2007 / ProcessedData result_code)로 프론트 리트라이 정책 분기 가능.
  - 광고주·마케터가 애널리틱스 UI에서 광고 유입·전환·캠페인 성과 측정 가능.

### 애널리틱스 React 리뉴얼 (2025-06 ~ 현재)

- **역할**: 프론트엔드 리드 · 아키텍처 설계 · 풀스택 개발.
- **스택**: Vite + React + TypeScript + TanStack Query/Router + Zustand + ag-grid + Highcharts + FastAPI + MySQL + BigQuery + Docker + Jenkins.
- **성과**
  - 팀 최초 **React 기반 프론트엔드 아키텍처** 설계·표준화. "2025 프론트엔드 개발 가이드라인" 문서화.
  - `c2spf/analytics-frontend` **476커밋 (~24%)**, `c2spf/analytics-common-api` **231커밋 (92%)**.
  - **팀 프론트엔드 생산성 30~40% 향상 기반 구축**. ag-grid 공통 컴포넌트 설계 리드타임 2~3일에서 하루 미만으로, 반복 개발 시간 50%+ 절감.
  - 차트·퍼널·리텐션·대시보드 4대 분석 기능을 "생성·조회·수정" 구조로 단계적 리뉴얼.
  - GCPPDT-741/742 Story MR 머지, 회귀 테스트 **32/32 · 22/22 통과**, 측정값 연산식 에러 **8종 × 5개 로케일 i18n**.
  - AI 기반 개발 생산성 향상 가이드 작성 (Claude Code / Codex CLI / ChatGPT 시나리오 4종 + 프롬프트 템플릿 4종).

### 증거 (portfolio 저장소)

- `docs/20-projects/com2us-platform/2025-01-airbridge-api.md`
- `docs/20-projects/com2us-platform/2025-06-analytics-react-renewal.md`
- `docs/40-stories/leadership-react-adoption.md` — 리더십 STAR 스토리
- GitHub: `c2spf/analytics-frontend`, `c2spf/analytics-common-api`
- Jira: GCPPDT-741, GCPPDT-742, GCPPDT-638, GCPPDT-639, GCPPDT-167
- Confluence: 35568348 (공통 API 명세), 170034641 (FE 가이드라인)

## 주요 인사이트

- **계약(Contract) 재사용의 위력** — 2024-08 공통 모듈에서 정립한 APIResponse·APICode 표준이 2025-01 Airbridge에서 ProcessedData로 확장되고, 2025-06 React 리뉴얼에서 그대로 재사용됨. **표준화의 복리 효과**.
- 두 프로젝트는 6개월 간격이지만 같은 인프라(`analytics-common-api`)와 같은 데이터 모델 위에서 동작 — 단일 시스템의 점진적 진화로 봐야 함.
- "팀 최초"라는 키워드가 두 번 등장(React 도입, FE 가이드라인 문서화). **표준 정립자(standard-setter)** 포지션이 명확히 드러나는 프로젝트.

## 관련 엔티티/개념

- [[c2spf-analytics|c2spf 게임 데이터 BI]] — 서비스 본체
- [[com2us-platform|컴투스플랫폼 c2spf]] · [[seokgeun-kim|석근 (이 위키 owner)]]
- [[frontend-react]] — Vite + TS + TanStack + Zustand + ag-grid 표준화
- [[backend-python-fastapi]] — 공통 API 확장
- [[data-pipeline-bigquery]] — Airbridge MMP × BigQuery 결합

## 메모

- 원본 경로: `raw/notes/portfolio/docs/20-projects/com2us-platform/2025-01-airbridge-api.md`, `.../2025-06-analytics-react-renewal.md`.
- Airbridge와 React 리뉴얼을 한 source 페이지로 합쳐 수집한 이유: 공통 API 인프라 위에서 동작하는 연속 프로젝트이며, 시간순으로 같은 시스템의 진화 단계로 이해하는 것이 자연스러움.
