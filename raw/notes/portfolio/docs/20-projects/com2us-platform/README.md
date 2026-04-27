# 컴투스플랫폼 — 프로젝트 통합 문서

**Synthesis Layer**: 원천 자료(`docs/10-sources/com2us-platform/`)를 **프로젝트 단위**로 통합한 문서 모음. 각 프로젝트 문서는 frontmatter `sources:`에 원천 링크, 본문에 STAR 스토리와 정량 지표를 담음.

## 재직 정보

- **회사**: 컴투스플랫폼
- **재직 기간**: 2017-05 ~ 현재
- **주요 도메인**: 게임 데이터 분석(BI), ML/AI, 블록체인 플랫폼, 인증/공통 인프라

## 프로젝트 타임라인

```
gantt
    title 컴투스플랫폼 프로젝트 타임라인 (2022~현재)
    dateFormat  YYYY-MM
    section Analytics
    공통모듈·배포 개선     :2024-08, 5M
    Airbridge 데이터 API   :2025-01, 2M
    React 리뉴얼          :2025-06, 11M
    section Blockchain
    NFT 마켓              :2022-05, 22M
    XPLA 플랫폼           :2024-04, 4M
```

## 프로젝트 목록 (최근 3년 우선, 최신순)

| 시작 | 프로젝트 | 기간 | 상태 | 문서 |
|------|---------|------|------|------|
| 2025-06 | 애널리틱스 React 리뉴얼 | 2025-06 ~ 현재 | 🚧 진행 중 | `2025-06-analytics-react-renewal.md` |
| 2025-01 | Airbridge 데이터 가공 API | 2025-01 ~ 2025-02 | ✅ 완료 | `2025-01-airbridge-api.md` |
| 2024-08 | 애널리틱스 공통 모듈 & 배포 개선 | 2024-08 ~ 2024-12 | ✅ 완료 | `2024-08-analytics-common-module.md` |
| 2024-04 | XPLA 플랫폼 | 2024-04 ~ 2024-07 | ✅ 완료 | `2024-04-xpla-platform.md` |
| 2022-05 | NFT 마켓 | 2022-05 ~ 2024-03 | ✅ 완료 | `2022-05-nft-market.md` |

### 이전 프로젝트 (2022년 이전)

`old-portfolio.md`에 요약되어 있음. 필요시 `docs/20-projects/com2us-platform/` 아래에 `YYYY-MM-*.md` 형식으로 상세 문서화.

| 시작 | 프로젝트 | 기간 |
|------|---------|------|
| 2021-10 | CODE 트래블룰 API | 2021-10 ~ 2022-04 |
| 2021-06 | 통합 인증 & 비동기 통신 공통 모듈 | 2021-06 ~ 2021-07 |
| 2020-08 | 애널리틱스 ML 유저 예측 | 2020-08 ~ 2021-09 |
| 2019-03 | 대용량 데이터 다운로드 REST API | 2019-03 ~ 2019-06 |
| 2018-07 | 게임 정보 동기화 스케줄러 | 2018-07 ~ 2018-08 |
| 2017-05 | 애널리틱스(게임 데이터 분석 웹서비스) | 2017-05 ~ 현재 (장기) |

## 프로젝트 클러스터

### 🎯 Analytics 시리즈
핵심 도메인. 게임 로그 기반 BI 서비스의 설계·개발·운영.
- 2017-05 애널리틱스 본체 (장기 진행)
- 2024-08 공통 모듈 & 배포 개선
- 2025-01 Airbridge API
- 2025-06 React 리뉴얼

### ⛓️ Blockchain 시리즈
블록체인 플랫폼·규제·NFT.
- 2021-10 CODE 트래블룰 API
- 2022-05 NFT 마켓
- 2024-04 XPLA 플랫폼

### 🧠 ML/AI 시리즈
AutoML 기반 유저 예측, MLOps.
- 2020-08 유저 예측 (AutoML)

### 🔧 Infrastructure
공통 모듈, 인증, 데이터 파이프라인.
- 2018-07 게임 정보 동기화
- 2019-03 대용량 데이터 다운로드
- 2021-06 통합 인증 & 비동기 통신

## 작성 가이드

- 새 프로젝트 파일명: `YYYY-MM-<slug>.md` (예: `2025-06-analytics-react-renewal.md`)
- frontmatter 스키마: [`docs/00-meta/document-conventions.md`](../../00-meta/document-conventions.md)
- 증거 링크: `sources:` 필드에 Jira/Confluence/GitHub/GDrive/Gmail 경로
- STAR 섹션, `metrics:` 정량 지표, `related_projects:` 크로스 링크
