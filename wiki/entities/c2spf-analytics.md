---
title: c2spf 애널리틱스 (게임 데이터 BI)
type: entity
entity_type: service
aliases:
- c2spf-analytics
- c2spf 게임 데이터 BI
- 컴투스플랫폼 BI
- c2spf BI
- analytics
tags:
- analytics
- c2spf
- BI
- 게임데이터
- fastapi
- react
- bigquery
- ag-grid
related:
- '[[com2us-platform]]'
- '[[seokgeun-kim]]'
- '[[portfolio]]'
- '[[backend-python-fastapi]]'
- '[[frontend-react]]'
- '[[data-pipeline-bigquery]]'
- '[[devops-cicd]]'
- '[[seokgeun-stack-guide]]'
- '[[matechat]]'
- '[[llm-infra-meta-cluster]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[mcp]]'
- '[[claude-code]]'
- '[[portfolio-seed]]'
- '[[portfolio-ko]]'
- '[[c2spf-analytics-common]]'
- '[[c2spf-analytics-renewal]]'
source_count: 4
observed_source_refs: 45
inbound_count: 190
created: 2026-04-24
updated: 2026-04-29
verification_required: true
last_verified: 2026-04-29
verification_notes: 회사 BI 시스템 운영 상태 (스택·리뉴얼 진행도) — 회사 인프라 재확인
verification_procedure: 사내 GitHub c2spf 조직의 analytics-* 레포 최신 커밋 확인 (operating 상태 / 1,111 커밋 누계 변동). 분기별 c2spf-analytics-common API ownership 비율 재산출 (231/251 → 갱신). 변동 시 본문 정량 단언과 last_verified 갱신.
cited_by_count: 76
---

# c2spf 애널리틱스 (게임 데이터 BI)

> [!info] 2축 hub — 회사 본진
> [[com2us-platform|컴투스플랫폼 c2spf]]의 게임 데이터 BI 본진 시스템. FastAPI + React + BigQuery + pandas + Airbridge MMP. [[c2spf-analytics-common]](2024-08 공통 모듈)과 [[c2spf-analytics-renewal]](2025 React 리뉴얼)이 핵심 자산. [[matechat|MateChat 사이드 프로젝트]] 사이드에서 검증된 패턴이 회사로 역수입되는 단방향 펌프 형성. 운영 상태는 `verification_required: true`.
> 
> 한국어 표기: **c2spf 게임 데이터 BI** 또는 **컴투스플랫폼 BI**(c2spf-analytics).

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

## 9년차 운영 시스템의 누적 자산

c2spf 애널리틱스는 코드 자체가 아니라 **코드 + 데이터 모델 + API 계약 + 운영 가이드 + 도메인 지식이 함께 누적된 복합 자산**이다. 신규 개발자가 코드만 받아 운영하기 어려운 이유는 이 5계층 자산이 분리되어 보존되지 않기 때문이다. 본 위키의 [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]]가 권장하는 38개 SOP SKILL.md 패턴([[matechat|MateChat 사이드 프로젝트]] 본진 채택)은 이 5계층 자산을 동기화하는 후보 메커니즘이다.

### 자기 커밋 분포 (포트폴리오 기준)

- `c2spf` 조직 본인 커밋 누계: **1,111건** [재현: `git log --author='석근' --oneline | wc -l` (c2spf 조직 전체 리포지토리 합)]
- `analytics-common-api` 단독 유지보수: 231/251 커밋 (~92%) [재현: `git shortlog -sn` in `analytics-common-api`]
- `analytics-frontend` React 리뉴얼: 476커밋 (~24%, 팀 최초 React 도입) [재현: `git shortlog -sn --since=2025-06-01` in `analytics-frontend`]
- ML 유저 예측: AutoML 기반 평균 정확도 85%+ [재현: GCP AutoML `evaluation_dashboard` 또는 `model_evaluation.json`]

> 본 정량 주장의 마지막 측정 시점은 frontmatter `last_verified` 필드로 추적된다. 이후 변동은 `verification_required: true`에 따라 분기별 재산출 권장 — `verification_notes` 참조.

### 횡단 계약 4종 (2024-08 공통 모듈 리뉴얼 산출)

| 계약 | 역할 | 적용 모듈 |
|---|---|---|
| `APIResponse` | 표준 응답 envelope | analytics-common-api 모든 endpoint |
| `APICode` | 에러/상태 코드 카탈로그 | 프론트/백 공통 |
| `ProcessedData` | 시각화·다운로드 공통 데이터 모델 | 차트/퍼널/리텐션/대시보드 |
| HIVE OAuth 8 endpoint | 사내 인증 통합 | 모든 c2spf 서비스 |

→ 2024-08 이후 모든 리포트·대시보드 기능이 이 4 계약 위에 구축. 회사 내 개발 표준의 사실상 SSOT.

## 위키 안에서의 위상

c2spf-analytics는 본 위키에서 인바운드 상위권 hub다. **시점 스냅샷**으로는 4위(43)였고, agent-skills(58) / harness(49) / ml-ai(44) 다음 위치였다. 이후 5축 LLM 인프라 메타 개념들의 인바운드는 더 자랐지만, c2spf-analytics 자신도 함께 자라 인바운드 상위 hub 위치를 유지한다. 즉 **회사 BI 운영 시스템이 위키의 핵심 hub 중 하나**이며, 이는 본 위키가 직장인의 위키임을 그래프 측면에서 자연스럽게 입증한다.

> 본문의 인바운드 수치는 시점 스냅샷이다. 현재 측정은 `python3 scripts/wiki-lint.py --report`로 재산출 가능 — 자동 필드(`inbound_count`, `cited_by`)가 source-of-truth.

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]]의 "회사 BI 적용 매핑" 표는 수집된 32개 OSS를 c2spf 운영에 적용하는 시나리오를 다룬다. 본 페이지는 그 매핑의 적용 대상 시스템.

## MateChat 자작 SKILL → c2spf 역수입 후보

[[matechat]] 본진 raw 수집에서 발견된 `.agents/skills/` 39 SKILL.md 중 **자작 11개 (외부 설치 28개 제외)** → 그중 **c2spf 운영에 직접 차용 가능한 9개** (build-app-bundle은 Android Flutter 전용 / flutter-qa-audit는 Flutter QA 전용이라 c2spf 부적합):

| MateChat SKILL | c2spf 적용 시나리오 |
|---|---|
| `fastapi-testing` | analytics-common-api 113 테스트 패턴 표준화 |
| `api-consistency` | APIResponse/APICode 계약 검증 자동화 |
| `migration-safety` | analytics 데이터베이스 alembic 변경 검증 (현 Jenkins 의존 → 자동화) |
| `pre-deployment` | 4환경(dev/qa/staging/prod) 배포 전 체크리스트 표준화 |
| `feature-workflow` | 차트/퍼널/리텐션 신규 분석 기능 추가 SOP |
| `doc-management` | 9년차 운영 SOP 누적 문서 관리 |
| `security-review` | HIVE OAuth + BigQuery 권한 점검 |
| `code-change-verification` | PR 단위 변경 영향 분석 자동화 |
| `runtime-behavior-probe` | 운영 환경 이슈 재현 SOP |

→ 후속 후보: 39 SKILL 중 자작 11개 본문 1회독 후 [[seokgeun-stack-guide]]에 "회사 BI 차용 SOP 후보" 섹션 추가.

## 관련 개념

- [[com2us-platform]] — 운영 회사
- [[seokgeun-kim|석근 (이 위키 owner)]] — 주축 개발자, 1,111커밋 누계
- [[backend-python-fastapi]] — 공통 API 스택, [[matechat]] 백엔드와 동일 6단
- [[frontend-react]] — 2025-06 리뉴얼 표준, [[tanstack-query]] + [[zustand]] 발견과 일치
- [[data-pipeline-bigquery]] — BI 데이터 파이프라인
- [[devops-cicd]] — Jenkins + Docker 표준화, [[github-actions]] 마이그레이션 후보
- [[ml-ai]] — analytics-prediction 모듈, [[scikit-learn]] / [[lightgbm]] 수집과 일치
- [[matechat]] — 38 SKILL 역수입 원천 + 동일 6단 백엔드 스택의 사이드 프로젝트 검증

## 출처

- [[portfolio-seed]] — 애널리틱스 본체(2017~) + 다운로드 API + ML 예측 + 공통 모듈 + 리뉴얼 등 다년 역사
- [[portfolio-ko]] — Selected Work 5선 중 3개가 애널리틱스 관련
- [[c2spf-analytics-common]] — 공통 모듈 & 배포 프로세스 (2024-08~)
- [[c2spf-analytics-renewal]] — Airbridge API + React 리뉴얼 (2025)
- [[seokgeun-stack-guide]] — 수집한 32개 OSS의 c2spf 적용 매핑

## 논쟁/모순

(없음)

## 메모

- 9년차 운영 중인 장기 시스템 — 단순 코드 외에 데이터 모델, API 계약, 운영 가이드가 함께 누적된 복합 자산.
- 2024-08 공통 모듈 리뉴얼이 이후 모든 리포트·대시보드 기능의 기반이 됨. APIResponse·APICode·ProcessedData 계약이 횡단.
- 본 페이지는 인바운드 4위 hub로서의 위상을 본문에 명시하고 [[matechat]] / [[seokgeun-stack-guide]] 양방향 백링크 추가, MateChat 38 SKILL 역수입 9개 후보 표 박힘. 식별된 "빈약 페이지" 결함 해소.
- 향후 보강 후보: 분석 도메인별 KPI 카탈로그(차트/퍼널/리텐션/대시보드 별 표준 지표), HIVE OAuth 8 endpoint 카탈로그, ML 예측 모델 영속성 의사결정 트리(skops/ONNX/joblib).

## 인용한 페이지 (cited_by)

- [[agent-skills]]
- [[alembic]]
- [[apache-arrow]]
- [[apache-kafka]]
- [[astral]]
- [[astral-sh-uv]]
- [[backend-fastapi-stack]]
- [[backend-python-fastapi]]
- [[c2spf-ai-agent-adoption-candidates]]
- [[c2spf-analytics-common]]
- [[c2spf-analytics-renewal]]
- [[career-timeline-seokgeun]]
- [[claude-code]]
- [[com2us-platform]]
- [[data-pipeline-bigquery]]
- [[dataframe-ecosystem-evolution]]
- [[devops-cicd]]
- [[docker]]
- [[duckdb]]
- [[duckdb-duckdb]]
- [[fastapi]]
- [[fastapi-fastapi]]
- [[flutter]]
- [[flutter-flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[frontend-react]]
- [[google]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[lazy-evaluation]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[matechat]]
- [[matechat-chat-analysis-module]]
- [[mcp]]
- [[microsoft-data-science-for-beginners]]
- [[microsoft-lightgbm]]
- [[ml-ai]]
- [[nextjs]]
- [[pandas]]
- [[pandas-ai]]
- [[pandas-dev-pandas]]
- [[pandas-vs-polars-vs-duckdb]]
- [[parquet]]
- [[pola-rs-polars]]
- [[polars]]
- [[portfolio]]
- [[portfolio-ko]]
- [[portfolio-resume-ko]]
- [[portfolio-seed]]
- [[postgresql]]
- [[prometheus]]
- [[pyarrow]]
- [[pydantic]]
- [[python-packaging]]
- [[redis]]
- [[ruff]]
- [[scikit-learn]]
- [[scikit-learn-scikit-learn]]
- [[seokgeun-kim]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[tanstack-query]]
- [[uv]]
- [[zustand]]

## 인용한 페이지

- [[agent-sdk-comparison]]
- [[agent-skills]]
- [[alembic]]
- [[apache-arrow]]
- [[apache-kafka]]
- [[astral]]
- [[astral-sh-uv]]
- [[backend-fastapi-stack]]
- [[backend-python-fastapi]]
- [[c2spf-ai-agent-adoption-candidates]]
- [[c2spf-analytics-common]]
- [[c2spf-analytics-renewal]]
- [[career-timeline-seokgeun]]
- [[chain-of-thought-prompting]]
- [[claude-code]]
- [[codex]]
- [[com2us-platform]]
- [[data-pipeline-bigquery]]
- [[dataframe-ecosystem-evolution]]
- [[devops-cicd]]
- [[docker]]
- [[duckdb]]
- [[duckdb-duckdb]]
- [[fastapi]]
- [[fastapi-fastapi]]
- [[flutter]]
- [[flutter-flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[frontend-react]]
- [[google]]
- [[governance-axis-comparison]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[lazy-evaluation]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[matechat]]
- [[matechat-chat-analysis-module]]
- [[mcp]]
- [[microsoft-data-science-for-beginners]]
- [[microsoft-lightgbm]]
- [[ml-ai]]
- [[nextjs]]
- [[openai-chatgpt-codex-guide]]
- [[pandas]]
- [[pandas-ai]]
- [[pandas-dev-pandas]]
- [[pandas-vs-polars-vs-duckdb]]
- [[parquet]]
- [[pola-rs-polars]]
- [[polars]]
- [[portfolio]]
- [[portfolio-ko]]
- [[portfolio-resume-ko]]
- [[portfolio-seed]]
- [[postgresql]]
- [[progressive-disclosure]]
- [[prometheus]]
- [[pyarrow]]
- [[pydantic]]
- [[python-packaging]]
- [[rcif-prompt-pattern]]
- [[redis]]
- [[ruff]]
- [[scikit-learn]]
- [[scikit-learn-scikit-learn]]
- [[seokgeun-kim]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[tanstack-query]]
- [[uv]]
- [[vendor-neutral]]
- [[zustand]]
