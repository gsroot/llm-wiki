---
title: "애널리틱스 서비스 React 기반 리뉴얼"
type: project
company: com2us-platform
period: "2025-06 ~ 현재"
status: in-progress
role: "프론트엔드 리드 (React 구조 설계·구축), 풀스택 개발"
tech_stack:
  - Vite
  - React
  - TypeScript
  - JavaScript (ES6+)
  - TanStack Query
  - TanStack Router
  - Zustand
  - ag-grid
  - Highcharts
  - React Hook Form
  - Playwright
  - FastAPI
  - MySQL
  - Redis
  - BigQuery
  - Docker
  - Jenkins
  - nginx
sources:
  jira:
    - private/jira/GCPPDTDW-2365.md   # 애널리틱스 프런트 엔드 개선 (Story, 상위 트래커)
    - private/jira/GCPPDT-741.md      # 차트 시각화 및 측정값 편집 UX 개선 (Story, 본인 담당)
    - private/jira/GCPPDT-742.md      # 차트 테이블 가독성 개선 (Story, 본인 담당)
    - private/jira/GCPPDT-638.md      # 지표 템플릿 기능 적용 (Story, 본인 담당, QA)
    - private/jira/GCPPDT-639.md      # 대시보드 기능 개선 (Story, 본인 담당, QA)
    - private/jira/GCPPDTDW-2386.md   # 공통 API - 2025 (Story, 본인 담당)
    - private/jira/GCPPDTDW-2114.md   # 유저 활동 추적 - 2025 (Story, 본인 담당)
    - private/jira/GCPSRE-16239.md    # 공통 API nginx 설정 변경 요청 (reporter=본인)
    - private/jira/GCPSRE-15853.md    # 애널리틱스 v2 서버 패키지 설치 요청 (reporter=본인)
  confluence:
    - private/confluence/35568626.md  # 2025 프론트엔드 개발 가이드라인 (본인 작성)
    - private/confluence/170034641.md # AI 기반 개발 생산성 향상 가이드 (본인 작성)
    - private/confluence/35568348.md  # 지표 공통 API 명세 문서 (본인 작성)
    - private/confluence/35568410.md  # 애널리틱스 리포트 아키텍처 분석 (본인 작성)
    - private/confluence/35568800.md  # 사용자 권한 게임 목록 조회 API 통합 트러블슈팅 (본인 작성)
  github:
    - "https://github.com/c2spf/analytics-frontend"   # 476 커밋 기여, 리드
    - "https://github.com/c2spf/analytics-common-api" # 231 커밋 (92%), 거의 단독 유지보수
  gdrive: []
  gmail: []
tags: [frontend, react, typescript, vite, architecture, refactoring, ag-grid, tanstack, zustand, analytics, ux]
metrics:
  - "내 분석 프론트엔드 GitHub 기여: analytics-frontend 476 커밋 (~24%), analytics-common-api 231 커밋 (92%, 거의 단독 유지보수) — GitHub 레포 인덱스 확인"
  - "팀 전체 개발 생산성 30~40% 향상 기반 구축 (old-portfolio.md L126, Confluence 170034641 L155 AI 가이드 결론 일치)"
  - "React + ag-grid 공통 컴포넌트 초안 설계 시간: 2~3일 → 하루 미만, 반복 개발 시간 50% 이상 절감 (Confluence 170034641 L83~84, AI 활용 사례 기록)"
  - "GCPPDT-742 차트 테이블 가독성 개선: MR#23/MR#24 머지 완료, 22/22 테스트 통과"
  - "GCPPDT-741 차트·측정값 UX 개선: MR#20/#22 머지 완료, 회귀 테스트 32/32 통과, 5개 로케일 i18n 지원 validateExpression 유틸 도입"
related_projects:
  - "2024-08-analytics-common-module"  # 이전 공통 모듈·배포 프로세스 확립 (본 리뉴얼의 전제)
  - "2025-01-airbridge-api"             # Airbridge 데이터 가공 API (공통 API 확장 맥락)
star:
  situation: "애널리틱스 서비스의 UI는 Spring MVC + Thymeleaf + Bootstrap + jQuery + Highcharts 기반 레거시 구조로 운영되고 있었고(Confluence 35568410 '애널리틱스 리포트 아키텍처 분석'), 각 서비스에 동일 로직(사용자 권한 게임 목록 조회 등)이 분산·중복 구현되어 있어 UX 개선·기능 추가의 리드타임이 길었다. 정보 구조(IA), 인터랙션, 컴포넌트 재사용성 측면에서 전면 개편 필요가 제기되었다."
  task: "팀 최초로 React 기반 프론트엔드 아키텍처를 설계·구축하고, ag-grid 중심의 공통 컴포넌트 모듈을 만들어 차트·퍼널·리텐션·대시보드 4대 분석 기능을 단계적으로 리뉴얼한다. 동시에 기존 공통 API와의 경계를 정비하고, 팀이 새 스택에 온보딩할 수 있는 가이드라인을 수립한다."
  action: "① Vite + React + TypeScript + TanStack Router + TanStack Query + Zustand + ag-grid 스택을 팀 표준으로 채택하고 '2025 프론트엔드 개발 가이드라인'(Confluence 35568626)을 문서화. ② 라우팅은 파일 기반(`src/routes/*.jsx` → `createFileRoute`), 서버 상태는 TanStack Query, 전역 상태는 Zustand 슬라이스(예: `chartStore.pieVisibility`)로 분리. ③ ag-grid 공통 모듈을 만들어 차트 테이블 컬럼 pinning·타입별 minWidth·fitCellContents 전략 도입(GCPPDT-742). ④ 차트/퍼널/리텐션/대시보드 지표를 '생성·조회·수정' 구조로 재설계, 지표 템플릿 기능(GCPPDT-638)·대시보드 CSV/이미지 내보내기(GCPPDT-639) 추가, 파이 차트 다중 측정값 시각화·validateExpression 8개 에러코드·5개 로케일 i18n(GCPPDT-741) 구현. ⑤ 공통 API(FastAPI) 측은 `result_code/message/data` 응답 envelope과 APICode(1001~2007 표준 오류 코드) 정의(Confluence 35568348). ⑥ 인프라 사전 작업으로 v2 WAS/Front/BI 서버군 도커·nginx 구성 표준화(GCPSRE-15853, 16239). ⑦ Claude Code / Codex CLI / ChatGPT를 설계 초안·리팩토링·리뷰에 도입한 AI 가이드를 별도 문서화(Confluence 170034641)."
  result: "analytics-frontend 레포에 476커밋을 기여하며 팀 최초 React 구조 표준화를 완료, GCPPDT-741/742 Story의 MR이 머지되고 회귀 테스트 통과(32/32, 22/22). ag-grid 공통 컴포넌트 설계 리드타임을 2~3일 → 하루 미만으로 단축, 반복 개발 시간 50% 이상 절감(Confluence 170034641). 팀 전체 생산성 30~40% 향상 기반을 확보(old-portfolio.md L126 원문과 Confluence 170034641 L155 결론 일치). 공통 API 측은 analytics-common-api의 92%를 본인이 기여하며 응답 envelope/오류 코드 표준화를 문서로 확립."
---

# 애널리틱스 서비스 React 기반 리뉴얼

## 개요

컴투스플랫폼의 애널리틱스(게임 데이터 분석 BI 서비스)는 2017년 최초 구축 이래 Spring MVC + Thymeleaf + jQuery + Highcharts + Bootstrap 기반의 서버 렌더링 구조로 운영되어 왔다(Confluence `애널리틱스 리포트 아키텍처 분석`, 35568410). 서비스 범위가 확장되면서 UI 노후화, 사용성 저하, 컴포넌트 재사용성 부족으로 신규 분석 기능의 리드타임이 길어졌고, "사용자 권한 게임 목록 조회" 같은 동일 기능이 서비스마다 중복 구현되는 문제도 누적되었다(Confluence 35568800 트러블슈팅 사례).

2025년 6월부터 **팀 최초 React 기반 프론트엔드 아키텍처** 전환을 주도하여, Vite + React + TypeScript + TanStack Router/Query + Zustand + ag-grid 스택을 표준화하고, 차트·퍼널·리텐션·대시보드 4대 분석 기능을 "생성·조회·수정" 구조로 단계적으로 리뉴얼하고 있다. 동시에 FastAPI 기반 공통 API와 공통 JavaScript 모듈을 지속 유지보수하여 신·구 서비스의 데이터 처리 경로를 통일했다.

## 역할·책임

- **팀 최초 React 구조 설계·구축 주도** — Vite + React + TypeScript 스택 확정, 라우팅·상태관리·서버 상태 레이어 분리
- **2025 프론트엔드 개발 가이드라인 문서화** — 팀원 온보딩 절차(`.nvmrc`, Vite dev 서버, 파일 기반 라우팅 규칙), React Hook 가이드, 공통 토스트/세션 사용법 정리 (Confluence 35568626)
- **ag-grid 공통 컴포넌트 모듈 개발** — 차트 테이블 컬럼 pinning 전략(`PINNED_DIMENSION_LIMIT=3`), 타입별 minWidth(date:110 / dim:180 / measure:130), fitCellContents 전환 (Jira GCPPDT-742)
- **차트·퍼널·리텐션·대시보드 기능 개발** — 지표 템플릿 적용(GCPPDT-638), 대시보드 CSV/이미지 내보내기(GCPPDT-639), 파이 차트 다중 측정값 시각화·측정값 연산식 검증(GCPPDT-741)
- **공통 API 유지보수·확장** — analytics-common-api 231커밋(전체의 92%), FastAPI + MySQL 8.4 + BigQuery + Redis 스택, Jenkins CI/CD 파이프라인 개선
- **인프라 정합성 확보** — 애널리틱스 v2 서버군(WAS/Front/BI, live/staging/sandbox/test) 도커·nginx 구성(GCPSRE-15853), 운영 중 nginx 설정 개선(GCPSRE-16239)
- **기획·디자인·백엔드 협업 및 QA** — 사용성 테스트, 내부 QA, 코드 리뷰, MR 피드백 반영(경계 테스트/WHY 주석 보강 등)
- **AI 기반 개발 생산성 향상 가이드 작성** — 팀원들이 Claude Code / Codex CLI / ChatGPT를 실무에 활용할 수 있도록 시나리오·프롬프트 템플릿 정리 (Confluence 170034641)

## 기술적 의사결정

### 왜 React + Vite인가

- JavaScript(ES6+)를 우선 채택하여 팀 온보딩 학습 곡선을 낮추고, 빠른 프로토타이핑과 점진적 TypeScript 도입을 병행할 수 있는 기반을 만듦(Confluence 35568626 §개발 언어)
- Vite + `@vitejs/plugin-react-swc` 조합으로 HMR 속도와 빌드 파이프라인 단순화를 확보

### 왜 TanStack Router / Query인가

- 파일 기반(`src/routes/page-name.jsx` → `createFileRoute`) 라우팅으로 라우트 구조가 폴더 구조와 일치, `beforeLoad`·`_layout`에서 토큰 검증·메뉴 초기화를 선언형으로 배치(Confluence 35568626 §페이지 로딩 순서)
- TanStack Query로 서버 상태 캐싱/동기화/리페칭을 일원화 → 각 컴포넌트가 세부 요청 관리에서 해방

### 왜 Zustand인가

- 경량 전역 상태 관리. 차트 가시성(`chartStore.pieVisibility` 슬라이스 등) 같은 UI 전용 상태를 로컬/스토어 양방향 persist로 관리(Jira GCPPDT-726 서술)
- Redux·MobX 대비 보일러플레이트 감소, React Hook 기반이라 Query와 구성 일관성 유지

### 왜 ag-grid 공통 모듈인가

- 차트 테이블이 BI 서비스의 핵심이고 차원/측정값 조합에 따라 컬럼 폭·pinning 요구가 복잡. 개별 화면에서 각자 구현하면 UX 편차와 중복 수정이 커지므로, 타입 기반(date/dimension/measure) 공통 전략으로 추상화(Jira GCPPDT-720 → GCPPDT-742)
- React + ag-grid 공통 컴포넌트 AI 활용 시나리오에서 초안 설계 시간을 2~3일 → 하루 미만으로 단축한 경험(Confluence 170034641 §4.1)

### 왜 FastAPI (공통 API)인가

- 기존 공통 API가 Python/FastAPI 기반으로 운영 중이었고(레포 `analytics-common-api`), BigQuery/Hive API 연동 로직을 유지하면서 점진적 개선이 가능
- 응답 envelope `{ result_code, message, data }` 표준화, APICode 표(1001~2007)·BigQuery 처리 결과 코드로 프론트-백 계약을 문서로 고정(Confluence 35568348)

## 주요 작업

### 1. 프론트엔드 아키텍처 수립

- `src/routes/`(라우트), `src/client/`(API), `src/components/Workspace/`(화면 컴포넌트), `src/stores/`(상태), `src/hooks/`, `src/constants/` 디렉터리 표준 정의
- `.nvmrc` 기반 Node 24.8.0 고정, `.env.local` 표준 키(Oauth·Common API·메뉴 CD 등) 공유 (Confluence 35568626 §로컬 세팅)
- `@tanstack/router-vite-plugin` 도입, ESLint + Prettier + Playwright 체계 표준화

### 2. 공통 컴포넌트·인프라 구축

- ag-grid 차트 테이블: `PINNED_DIMENSION_LIMIT=3` 기반 "날짜만 pinned" 전략, 타입별 minWidth + fitCellContents (Jira GCPPDT-742 서술)
- 공통 토스트(`CommonToastContext`)·세션 스토어(`useSessionStore`) 일관화 (Confluence 35568626)
- 에러 경계(`react-error-boundary`), 폼 성능(`react-hook-form`) 도입

### 3. 4대 분석 기능 리뉴얼 (차트·퍼널·리텐션·대시보드)

- **차트** (GCPPDT-741): 파이 차트 다중 측정값 Small Multiples, `chartStore.pieVisibility`, 가시성 저장/복원 및 대시보드 위젯 간 상태 격리, Line/Bar/Area/Spline 공통 X축 날짜 피벗
- **측정값 편집기** (GCPPDT-741): `validateExpression` 유틸, 8개 에러 코드, 5개 로케일 i18n, `ExpressionEditor`/`ExpressionModal` 통합
- **지표 템플릿** (GCPPDT-638): `templateIdx` 파라미터 기반 자동 적용, 대시보드 위젯 프로젝트 선택, 템플릿 null 프로젝트 자동 생성 로직
- **대시보드** (GCPPDT-639): AG-Grid CSV 내보내기, Highcharts 이미지 내보내기, 링크 공유 제거(운영 정책)
- **유저 활동 추적** (GCPPDTDW-2114): playerId 기반 유저 검색·타임라인·세그먼트 자동 생성

### 4. 공통 API·인프라 운영

- analytics-common-api(FastAPI) 2025년 Story(GCPPDTDW-2386) 담당: BigQuery Decimal→int64/float64 변환, 피벗 NULL 플레이스홀더, `date_type=MINUTE` 유효성 검사, MySQL 8.4 업그레이드 대응
- API Reference 문서 추가(2025-11), Jenkinsfile Docker 리소스 정리·네트워크 존재 여부 검사 등 CI/CD 안정화
- 인프라 부서 슬레이브 DB 동기화 이슈에 대응해 읽기전용 트래픽도 마스터 DB로 전환하는 임시 조치
- v2 서버군 패키지·도커 표준 구성 요청(GCPSRE-15853), 공통 API nginx 설정 정합성 개선 — JSON API 응답을 위한 `proxy_intercept_errors off` 전환(GCPSRE-16239)

### 5. 팀 생산성 프로그램

- `2025 프론트엔드 개발 가이드라인`(Confluence 35568626) — 스택, 로컬 세팅, 페이지 생성 방법, Hook 레퍼런스, 자주 하는 실수 정리
- `AI 기반 개발 생산성 향상 가이드`(Confluence 170034641) — Claude Code / Codex CLI / ChatGPT 특성 비교, React + ag-grid/공통 API/기획서 리뷰/코드 리뷰 4가지 실무 시나리오, 리팩토링·API·오류분석·문서 자동화 4개 프롬프트 템플릿 수록

## 성과

### 정량

- **GitHub 기여**: analytics-frontend **476커밋**(전체 ~24%), analytics-common-api **231커밋**(전체의 **92%**, 거의 단독 유지보수) — 레포 인덱스 문서 확인
- **팀 생산성**: 반복 개발 리드타임 **30~40% 향상 기반 구축** (old-portfolio.md L126 원문; Confluence 170034641 §7 결론에서도 동일 수치로 정리)
- **ag-grid 공통 컴포넌트 설계 시간**: 2~3일 → **하루 미만**, 반복 개발 시간 **50% 이상 절감** (Confluence 170034641 §4.1)
- **MR·테스트**: GCPPDT-742 차트 테이블 MR#23/#24 머지 완료, **22/22 테스트 통과**; GCPPDT-741 MR#20/#22 머지, **회귀 테스트 32/32 통과**
- **로컬라이제이션**: 측정값 연산식 에러 **8종 × 5개 로케일 i18n** 지원 (GCPPDT-727)

### 정성

- 팀 전체 코드 일관성·유지보수성 향상 — 스택·디렉터리·상태관리 표준이 문서로 공유
- 분석 작업 플로우 단축 및 사용성 대폭 개선 — 용어·지표·필터·툴팁 재정비(old-portfolio.md 성과)
- 서비스 진입 장벽 완화 — 공통 토스트·세션·에러 경계 패턴으로 신규 화면 작성 시 부가 코드 최소화
- 분석 기능의 신뢰도·속도·확장성 강화로 **서비스 경쟁력 및 조직 내 애널리틱스 활용도 증가**에 기여(old-portfolio.md 성과)
- AI 도구 체계적 활용 — 설계·구조화·코드 리뷰·문서화에서 조직 차원의 워크플로우로 정착

## 증거

### GitHub (2건)

- [`c2spf/analytics-frontend`](https://github.com/c2spf/analytics-frontend) — 476커밋 / 전체 2,000+ (~24%), 2025-10-13 ~ 2026-04-23 기여, 프론트엔드 리드
- [`c2spf/analytics-common-api`](https://github.com/c2spf/analytics-common-api) — 231커밋 / 전체 251 (~92%), 2024-09-02 ~ 2026-04-16 기여, 공통 API·공통 JavaScript 담당

### Jira (9건)

| 키 | 제목 | 타입 | 상태 |
|----|------|------|------|
| [GCPPDTDW-2365](https://com2us.atlassian.net/browse/GCPPDTDW-2365) | 애널리틱스 프런트 엔드 개선 (상위 Story) | Story | In Progress |
| [GCPPDT-741](https://com2us.atlassian.net/browse/GCPPDT-741) | 차트 시각화 및 측정값 편집 UX 개선 | Story | In Progress |
| [GCPPDT-742](https://com2us.atlassian.net/browse/GCPPDT-742) | 차트 테이블 가독성 개선 | Story | In Progress |
| [GCPPDT-638](https://com2us.atlassian.net/browse/GCPPDT-638) | 지표 템플릿 기능 적용 | Story | QA |
| [GCPPDT-639](https://com2us.atlassian.net/browse/GCPPDT-639) | 대시보드 기능 개선 | Story | QA |
| [GCPPDTDW-2386](https://com2us.atlassian.net/browse/GCPPDTDW-2386) | 공통 API - 2025 | Story | Done |
| [GCPPDTDW-2114](https://com2us.atlassian.net/browse/GCPPDTDW-2114) | 유저 활동 추적 - 2025 | Story | Done |
| [GCPSRE-15853](https://com2us.atlassian.net/browse/GCPSRE-15853) | v2 서버 패키지 설치 요청 | 설치 | Done |
| [GCPSRE-16239](https://com2us.atlassian.net/browse/GCPSRE-16239) | 공통 API nginx 설정 변경 요청 | 설정 | Done |

### Confluence (5건)

| 제목 | Page ID | 수정일 |
|------|---------|--------|
| [2025 프론트엔드 개발 가이드라인](https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568626) | 35568626 | 2025-11-18 |
| [AI 기반 개발 생산성 향상 가이드](https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/170034641) | 170034641 | 2025-11-27 |
| [지표 공통 API 명세 문서](https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568348) | 35568348 | 2025-11-18 |
| [애널리틱스 리포트 아키텍처 분석](https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568410) | 35568410 | 2025-02-27 |
| [사용자 권한 게임 목록 조회 API 통합 트러블슈팅](https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568800) | 35568800 | 2025-07-08 |

### GDrive / Gmail

- GDrive: 수집된 항목 없음
- Gmail: Phase 수집 blocked

## STAR 요약

### Situation

애널리틱스 서비스는 Spring MVC + Thymeleaf + jQuery + Highcharts 기반 레거시 UI로 운영되어 UX 노후화·컴포넌트 재사용성 부족·동일 로직 중복(사용자 권한 게임 목록 조회 등)이 누적되어 있었고, 기획·디자인·백엔드 간 협업 사이클이 길어 신규 분석 기능의 리드타임이 구조적으로 늘어나 있었다.

### Task

팀 최초 React 기반 프론트엔드 아키텍처를 설계·구축하고, ag-grid 공통 모듈로 차트·퍼널·리텐션·대시보드 4대 분석 기능을 "생성·조회·수정" 구조로 리뉴얼하여 UX·성능·유지보수성을 단계적으로 개선한다.

### Action

Vite + React + TypeScript + TanStack Router/Query + Zustand + ag-grid 스택을 표준으로 채택·문서화하고(Confluence 35568626), 공통 컴포넌트(차트 테이블 컬럼 전략, 에러 경계, 토스트/세션)·공통 API 응답 envelope(Confluence 35568348)를 확립. 차트 다중 측정값·측정값 연산식 검증(GCPPDT-741), 차트 테이블 가독성(GCPPDT-742), 지표 템플릿(GCPPDT-638), 대시보드 내보내기(GCPPDT-639) 등 Story를 순차적으로 완료. 인프라 측에서는 v2 서버군 구성(GCPSRE-15853)과 공통 API nginx 정합성(GCPSRE-16239)을 요청·조정. AI 기반 개발 생산성 향상 가이드(Confluence 170034641)로 팀의 AI 활용 체계를 정리.

### Result

analytics-frontend에 476커밋, analytics-common-api에 231커밋(92%)을 기여하며 팀 최초 React 구조 표준화를 완료. MR들이 순차 머지되고 회귀 테스트 통과(32/32, 22/22). ag-grid 공통 컴포넌트 설계 리드타임이 2~3일 → 하루 미만으로 단축되고 반복 개발 시간 50% 이상 절감되며, **팀 전체 프론트엔드 생산성 30~40% 향상 기반**이 확보됨(old-portfolio.md L126 및 Confluence 170034641 §7 일치). 공통 API 응답 envelope·오류 코드 표준화 문서화로 프론트-백 계약이 고정되어 신규 기능의 협업 사이클이 단축됨.
