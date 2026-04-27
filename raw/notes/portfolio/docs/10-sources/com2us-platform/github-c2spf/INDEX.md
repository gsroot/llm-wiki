---
title: "컴투스플랫폼 GitHub c2spf 조직 레포 인덱스"
type: source-index
company: com2us-platform
source: github
collected_at: "2026-04-24"
---

# GitHub c2spf — 레포 인덱스

컴투스플랫폼의 GitHub 조직 <https://github.com/c2spf>에서 내가 기여한 레포지토리의 **공개 인덱스**입니다.

> 🔒 모든 레포는 **private**이므로 외부에서 직접 열람할 수 없습니다. 레포 이름·커밋 수·기술 스택을 증빙으로 사용합니다.

## 수집 상태

- 📅 **수집일**: 2026-04-24
- 🔑 **조회 계정**: `gsroot` (<https://github.com/gsroot>) + 사내 이메일 `sgkim@com2us.com`
- 📊 **총 커밋 (내 기여분)**: **1,111 커밋** across 6개 레포 (2019~2026)
- 🔍 **수집 방법**: [`docs/00-meta/collection-strategy.md`](../../../00-meta/collection-strategy.md)의 GitHub 섹션 참조

## 전체 레포 테이블

| 레포 | 주 언어 | 내 커밋 수 / 전체 | 기여 기간 | 관련 프로젝트 | 상세 |
|------|---------|------------------|----------|-------------|------|
| [analytics-frontend](./repos/analytics-frontend.md) | JavaScript / TypeScript | **476** / 2,000+ | 2025-10 ~ 현재 | [React 리뉴얼](../../../20-projects/com2us-platform/) | ✅ |
| [analytics-common-api](./repos/analytics-common-api.md) | Python | **231** / 251 | 2024-09 ~ 현재 | [공통 모듈](../../../20-projects/com2us-platform/) | ✅ |
| [travelrule-api](./repos/travelrule-api.md) | Python | **135** / 507 | 2021-11 ~ 2022-06 | [CODE 트래블룰](../../../20-projects/com2us-platform/) | ✅ |
| [analytics-prediction](./repos/analytics-prediction.md) | Python | **116** / 925 | 2020-08 ~ 2021-03 | [ML 유저 예측](../../../20-projects/com2us-platform/) | ✅ |
| [analytics-mobile-report](./repos/analytics-mobile-report.md) | JavaScript | **101** / 318 | 2025-03 ~ 2025-04 | 🆕 신규 프로젝트 (포트폴리오 보강 필요) | ✅ |
| [analytics-download](./repos/analytics-download.md) | Python | **52** / 319 | 2019-03 ~ 2019-05 | [대용량 다운로드](../../../20-projects/com2us-platform/) | ✅ |

## 내 기여 하이라이트

- 📦 **전체 레포**: 6개 (c2spf 조직 전체가 6개, 모두 내가 기여한 프로젝트)
- ✍️ **내 커밋**: **1,111개** (전체 4,320 커밋의 ~26%)
- 📆 **기여 기간**: 2019-03 ~ 2026-04 (약 7년)
- 🥇 **가장 많이 기여한 레포**: `analytics-frontend` (476 커밋, 리드 역할)
- 🧰 **사용 언어**: Python (주), JavaScript/TypeScript, Java 일부

### 기간별 기여 (연도별)
| 연도 | 주 작업 레포 | 비고 |
|------|------------|------|
| 2019 | analytics-download | Python/Celery 비동기 워커 |
| 2020~2021 | analytics-prediction | AutoML, Flask+React |
| 2021~2022 | travelrule-api | FastAPI/블록체인 규제 대응 |
| 2024~ | analytics-common-api | 공통 API 모듈화 |
| 2025~ | analytics-frontend, analytics-mobile-report | React 리뉴얼, 모바일 리포트 |

## 프로젝트 문서와의 매핑

각 레포는 [`docs/20-projects/com2us-platform/`](../../../20-projects/com2us-platform/)의 해당 프로젝트 문서에서 `sources.github` 필드로 참조됩니다:

| 레포 | 매핑 프로젝트 파일 (예정) |
|------|-------------------------|
| analytics-frontend | `2025-06-analytics-react-renewal.md` |
| analytics-common-api | `2024-08-analytics-common-module.md` |
| analytics-mobile-report | `2025-03-analytics-mobile-report.md` (신규) |
| travelrule-api | `2021-10-code-travel-rule-api.md` |
| analytics-prediction | `2020-08-analytics-ml-prediction.md` |
| analytics-download | `2019-03-analytics-download-api.md` |

## 특이 사항

- **커밋 이메일 2종 사용**: 개인 계정 `gsr2732@gmail.com` + 사내 `sgkim@com2us.com`. 집계 시 둘 다 포함
- **analytics-mobile-report 신규 발견**: `old-portfolio.md`에 없지만 2025-03~04에 101 커밋. 별도 프로젝트 문서로 정리 필요
- **analytics-frontend 기술 스택 업데이트**: old-portfolio.md의 "React, ag-grid"만 기술되었으나 실제로는 **Vite + React + TanStack Query + TanStack Router + Zustand** 스택. 20-projects 문서 작성 시 정확히 반영 필요
