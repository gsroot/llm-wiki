---
title: "팀 최초 React 기반 프론트엔드 구조 설계·도입"
type: story
category: leadership
period: "2025-06 ~ 현재"
primary_project: "2025-06-analytics-react-renewal"
tags: [frontend, architecture, tech-leadership, react]
skills_demonstrated:
  - frontend-react
  - devops-cicd
---

# 팀 최초 React 기반 프론트엔드 구조 설계·도입

> 애널리틱스(게임 데이터 분석 BI) 서비스의 레거시 프론트엔드를 React 기반으로 전면 전환하면서, 팀에 최초로 React 스택을 도입하고 공통 컴포넌트·가이드라인·AI 활용 체계를 표준화한 경험.

## Situation

애널리틱스 서비스의 UI는 2017년 최초 구축 이래 Spring MVC + Thymeleaf + jQuery + Highcharts + Bootstrap 기반의 서버 렌더링 구조로 운영되어 왔다 (Confluence 35568410 "애널리틱스 리포트 아키텍처 분석"). 서비스 범위 확장에 따라 UI 노후화·사용성 저하가 누적되고, "사용자 권한 게임 목록 조회" 같은 동일 기능이 서비스마다 중복 구현되어 (Confluence 35568800) 신규 분석 기능의 리드타임이 구조적으로 길어져 있었다. 팀 내에는 아직 React 기반 운영 경험이 없는 상태였다.

## Task

**팀 최초로 React 기반 프론트엔드 아키텍처를 설계·구축**하고, ag-grid 중심의 공통 컴포넌트 모듈을 만들어 차트·퍼널·리텐션·대시보드 4대 분석 기능을 단계적으로 리뉴얼하는 것. 동시에 팀원이 새 스택에 안전하게 온보딩할 수 있는 가이드라인과 AI 활용 체계를 수립해, 개인이 아닌 "팀의 표준"이 정착하도록 한다.

## Action

- **스택 선정·표준화**: Vite + React + TypeScript + TanStack Router/Query + Zustand + ag-grid 조합을 팀 표준으로 채택하고, 선정 근거(JS 우선 채택으로 온보딩 곡선 완화, Vite HMR, 파일 기반 라우팅, 경량 전역 상태)를 **"2025 프론트엔드 개발 가이드라인"**(Confluence 35568626)으로 문서화.
- **아키텍처 레이어 분리**: 라우팅은 파일 기반(`src/routes/*.jsx` → `createFileRoute`), 서버 상태는 TanStack Query, 전역 상태는 Zustand 슬라이스(예: `chartStore.pieVisibility`), 공통 토스트(`CommonToastContext`)·세션 스토어·에러 경계(`react-error-boundary`) 패턴을 표준으로 확립.
- **ag-grid 공통 컴포넌트 모듈화**: 차트 테이블 컬럼 pinning(`PINNED_DIMENSION_LIMIT=3`), 타입별 minWidth(date:110 / dim:180 / measure:130), fitCellContents 전략 도입 (Jira GCPPDT-742). 개별 화면 중복 구현을 제거하고 타입(date/dimension/measure) 기반 추상화로 UX 편차 최소화.
- **4대 분석 기능 리뉴얼 구조화**: 차트·퍼널·리텐션·대시보드를 "생성·조회·수정" 3단계 구조로 재설계하고 Story 단위로 순차 추진 — 지표 템플릿(GCPPDT-638), 대시보드 CSV/이미지 내보내기(GCPPDT-639), 파이 차트 다중 측정값·validateExpression 8개 에러코드·5개 로케일 i18n(GCPPDT-741).
- **기획·디자인·백엔드 협업 리드**: 사용성 테스트, 내부 QA, MR 코드 리뷰(경계 테스트·WHY 주석 보강 등)를 주도하고, 공통 API(FastAPI) 응답 envelope과 APICode 표(Confluence 35568348)로 프론트-백 계약을 문서로 고정.
- **AI 기반 개발 생산성 가이드 수립**: Claude Code / Codex CLI / ChatGPT 특성 비교, React + ag-grid / 공통 API / 기획서 리뷰 / 코드 리뷰 4개 실무 시나리오, 프롬프트 템플릿을 **"AI 기반 개발 생산성 향상 가이드"**(Confluence 170034641)로 정리해 팀 전파.

## Result

### 정량

- **GitHub 기여**: `c2spf/analytics-frontend` **476커밋** (2025-10-13 ~ 2026-04-23 기준 전체의 ~24%)로 리드 포지션을 가시화.
- **팀 전체 프론트엔드 생산성 30~40% 향상 기반 구축** (old-portfolio.md L126 원문 및 Confluence 170034641 §7 결론 일치).
- **ag-grid 공통 컴포넌트 설계 리드타임: 2~3일 → 하루 미만**, 반복 개발 시간 50% 이상 절감 (Confluence 170034641 §4.1).
- **회귀 테스트**: GCPPDT-741 MR#20/#22 머지 + **32/32 통과**, GCPPDT-742 MR#23/#24 머지 + **22/22 통과**.

### 정성

- 팀의 프론트엔드 표준(스택·디렉터리·상태관리·공통 컴포넌트)이 문서로 확립되어, 향후 신규 화면 작성 시 부가 코드가 최소화되고 팀 전체 코드 일관성·유지보수성이 향상.
- 공통 토스트·세션·에러 경계 패턴으로 **서비스 진입 장벽을 낮추는 아키텍처**를 확보.
- AI 도구 체계적 활용이 개인 역량에서 **조직 차원의 워크플로우**로 정착, 설계 초안·리팩토링·코드 리뷰·문서 자동화에 일관되게 사용됨.

## 관련 증거

- **Confluence 35568626** — "2025 프론트엔드 개발 가이드라인" (본인 작성)
- **Confluence 170034641** — "AI 기반 개발 생산성 향상 가이드" (본인 작성)
- **Confluence 35568348** — "지표 공통 API 명세 문서" (본인 작성)
- **Confluence 35568410** — "애널리틱스 리포트 아키텍처 분석" (레거시 구조 배경)
- **GitHub** `c2spf/analytics-frontend` — 476 커밋 기여, 리드
- **Jira** GCPPDTDW-2365 (상위 Story), GCPPDT-741/742/638/639
- **프로젝트 문서**: [`../20-projects/com2us-platform/2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
- **원 시드**: `old-portfolio.md` "애널리틱스 서비스 개편" 섹션 L111~138
