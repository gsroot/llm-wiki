---
title: "애널리틱스 에어브릿지 데이터 가공 API 개발"
type: project
company: com2us-platform
period: "2025-01 ~ 2025-02"
role: "데이터 가공 API 설계 및 개발, Spring Boot + FastAPI 기반 파이프라인 구축, 데이터 시각화 통합"
tech_stack:
  - Java
  - Spring Boot
  - Python
  - FastAPI
  - JavaScript
  - MySQL
  - Redis
  - BigQuery
  - ag-grid
  - Docker
  - Jenkins
  - Promtail
  - Loki
  - Grafana
sources:
  jira:
    - "private/jira/GCPPDTDW-2386.md"
  confluence:
    - "https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568348"
    - "private/confluence/35568348.md"
    - "https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568344"
    - "private/confluence/35568344.md"
    - "https://com2us.atlassian.net/wiki/spaces/GCPP2DTDW/pages/35568410"
    - "private/confluence/35568410.md"
  github:
    - "https://github.com/c2spf/analytics-common-api"
  gdrive: []
  gmail: []
tags: [backend, api, data-pipeline, adtech, airbridge, bigquery, fastapi, spring-boot]
metrics:
  - "기존 애널리틱스에서 확인 불가했던 광고 성과 지표를 Airbridge 기반으로 측정 가능하도록 확장"
  - "`/common/processed-data` 엔드포인트 한 번에 BigQuery 메트릭 + Airbridge 데이터를 결합·피벗팅하여 반환 (Analytics Common API Swagger 명세 근거)"
  - "공통 API 공용화로 지표·퍼널 분석에서 동일한 데이터 처리 로직 재사용 (analytics-common-api 저장소 내 본인 커밋 ~92% 점유)"
related_projects:
  - "2024-08-analytics-common-module"
  - "2025-06-analytics-react-renewal"
star:
  situation: "기존 애널리틱스는 내부 게임 로그(BigQuery) 기반 분석만 가능해 광고 성과(에어브릿지 MMP) 데이터를 지표·퍼널 분석에서 확인할 수 없었다."
  task: "에어브릿지 데이터를 애널리틱스 지표·퍼널 분석에 주입할 수 있도록 데이터 가공 API를 설계·구현하고, 기존 Spring Boot 리포트 스택과 신규 FastAPI 공통 API를 함께 확장한다."
  action: "지표 공통 API(`/common/processed-data`)에 Airbridge 데이터 모델(AirbridgeData, event_timestamp_source/timezone 옵션)과 피벗팅 로직을 추가하고, Spring Boot 리포트 계층과 연동하여 지표·퍼널 분석에서 BigQuery·Airbridge 데이터를 결합한 표 형태로 반환하도록 했다. Promtail/Loki/Grafana 기반 로그 스택으로 상용·샌드박스 운영 가시성을 확보했다."
  result: "광고주·마케터가 애널리틱스 UI 내에서 광고 성과를 측정할 수 있게 되어 서비스 활용성과 가치가 증대되었고, 공통 API에 Airbridge 처리 경로가 편입되면서 이후 React 리뉴얼·대시보드 기능에서도 동일한 파이프라인을 재사용할 수 있게 되었다."
---

# 애널리틱스 에어브릿지 데이터 가공 API 개발

> Analytics 공통 API에 **Airbridge(MMP) 광고 성과 데이터** 처리 경로를 추가하여, 애널리틱스 지표·퍼널 분석이 내부 BigQuery 로그와 외부 광고 데이터를 함께 다룰 수 있도록 확장한 2025-01 ~ 2025-02 프로젝트.

## 1. 개요

- **기간**: 2025-01 ~ 2025-02 (2개월)
- **소속**: 컴투스플랫폼 / 애널리틱스 개발 파트
- **단일 담당자**: 본인 (설계·개발·운영)

기존 애널리틱스 서비스는 사내 게임 로그 기반 BI에 초점이 맞춰져 있어 광고 유입·전환 성과를 확인하려면 에어브릿지 콘솔을 별도로 열어야 했다. 본 프로젝트는 애널리틱스 **지표 공통 API**(`analytics-common-api`)에 Airbridge 데이터 모델을 도입하고, Spring Boot 기반 리포트 백엔드와 FastAPI 기반 공통 API가 함께 동작하는 하이브리드 파이프라인으로 확장한 작업이다.

## 2. 역할

- **데이터 가공 API 설계**
  - `DataCollection` 요청 본문에 `MetricData` + `AirbridgeData`를 함께 받아 BigQuery 쿼리와 Airbridge 쿼리를 동시에 실행·결합
  - `PivotItem` / `PivotValue` 모델로 x/y축, 행/열 위치, 소수점 처리까지 표준화
  - `ProcessedData` 응답(`index`, `columns`, `data`, `summary_stats`, `date_type`)으로 AG-grid가 바로 렌더링 가능한 포맷 확정
- **Java(Spring Boot) 리포트 계층 연동**
  - 기존 Spring MVC(컨트롤러-서비스-리포지토리 계층, MyBatis+JPA 다중 데이터 소스) 위에 Airbridge 지표를 호출하는 경로 추가
  - OAuth 기반 Hive Console 인증(`HiveConsoleSecurityAuthFilter`)과 세션 관리, 회사/메뉴 권한 정책 유지
- **Python(FastAPI) 공통 API 확장**
  - `analytics-common-api` 저장소에 Airbridge 처리 로직·모델 추가 (본인 커밋 비중이 저장소 전체의 약 92% / 231 of 251, 단독 유지보수 범위)
  - Swagger(`analytics-metricscreatorapi.withhive.com/docs`)로 API 명세 공개
- **시각화 통합**
  - AG-grid 기반 차트 테이블이 Airbridge 결합 데이터를 차원·측정값으로 구분해 표시하도록 포맷 매핑
- **운영 가시성**
  - Promtail → Loki → Grafana 스택으로 상용/샌드박스/테스트 3환경의 공통 API 로그 중앙 수집
  - 상용은 상용·스테이징 WAS 로그를 함께 수집하는 Primary/Standby 이중 구성

## 3. 기술 스택

| 계층 | 스택 |
|------|------|
| 백엔드(리포트) | Java, Spring Boot, Spring MVC, MyBatis, JPA, MySQL |
| 백엔드(공통 API) | Python, FastAPI, MySQL, Redis, BigQuery |
| 외부 데이터 | Airbridge (MMP, 광고 성과) |
| 프런트엔드 | JavaScript, AG-grid, Highcharts |
| 인프라/CI·CD | Docker, Jenkins (멀티브랜치 파이프라인) |
| 관측(Observability) | Promtail, Loki, Grafana |
| 인증 | Hive OAuth (access/refresh token), JDBC 세션 |

## 4. 주요 기술 결정

1. **하이브리드 스택 유지 (Spring Boot + FastAPI)**
   - 전면 재작성 대신 기존 Spring Boot 리포트 백엔드는 유지하고, 데이터 가공 파트만 FastAPI 공통 API로 분리. 리팩토링 리스크를 줄이면서도 신규 처리 로직은 Python 생태계(Pandas 등 피벗·집계 라이브러리)의 이점을 활용.
2. **단일 엔드포인트로 결합 처리 (`/common/processed-data`)**
   - 프런트엔드가 "BigQuery만", "Airbridge만", "둘 결합" 케이스를 분기하지 않도록 요청 본문(`DataCollection.data`)에 `MetricData`와 `AirbridgeData`를 리스트로 혼합해 전송. 서버가 두 소스에서 각각 쿼리 후 공통 축 기준으로 피벗팅·결합하여 `ProcessedData`를 반환.
3. **Airbridge 전용 옵션 모델화**
   - `AirbridgeData.option`에 `timezone`, `event_timestamp_source`를 두어 광고 이벤트의 타임존/시점 소스를 API 인자로 외부화. 타 MMP로 확장 시에도 동일 모델 확장이 가능하도록 설계.
4. **에러 코드 이원화 (APICode / ProcessedData.result_code)**
   - 인증·요청 검증 오류(APICode 1001~2007)와 데이터 처리 오류(ProcessedData.result_code: `404 BIGQUERY_TABLE_NOT_FOUND`, `422 BIGQUERY_SYNTAX_ERROR`, `400 BIGQUERY_ERROR`)를 분리해 프런트에서 리트라이 정책을 분기 가능하게 함.
5. **로그 집중화(Loki)**
   - 외부 MMP 연동 특성상 타임존·인증 이슈가 빈번할 수 있어 도입 시점부터 Promtail 기반 로그 집중 수집을 구성. `{service_name="analytics-common-api-backend-1"}` 쿼리로 환경별 즉시 추적.

## 5. 주요 작업

### 5.1 `/common/processed-data` 엔드포인트 확장

지표 공통 API 명세(`private/confluence/35568348.md`)에 따라 본 엔드포인트는:

- 전달받은 **메트릭 쿼리 및 에어브릿지 쿼리**를 실행해 결합·피벗팅한 테이블 반환
- 요청: `DataCollection` = `{ data: (MetricData | AirbridgeData)[], sorts? }`
- 응답: `ProcessedData` = `{ result_code, error_message, index, columns, data, index_names, column_names, summary_stats, date_type }`
- `SummaryStats`는 행/열 각각에 대해 `sum / mean / max / min` 반환

### 5.2 Spring Boot 리포트 계층과의 연동

`private/confluence/35568410.md` (애널리틱스 리포트 아키텍처) 기반 기존 구조:

- `ReportInfo → TabInfo → PageInfo → DataSourceInfo`
- `DataSourceInfo → DimensionItemInfo, MeasureItemInfo`
- 회사별 구현(Admin/Com2us/Other) 전략 패턴 유지
- 본 프로젝트는 `DataSourceInfo` 레벨에서 Airbridge 소스를 선택 가능하게 확장하고, 리포트 요청이 공통 API를 호출하도록 연동

### 5.3 인증·권한

- Hive OAuth 토큰 흐름(`/hive/auth/token`, `/hive/auth/check-token`)과 사용자 정보(`/hive/users/me`) 재사용
- 회사/메뉴 조합 권한(`/hive/auth/menu-permissions`, `/hive/auth/combined-info`) 그대로 공통 API에 연결
- 사용자 접근 가능 게임 목록은 Redis 캐시로 조회(`/hive/auth/games`), 캐시 무효화는 `DELETE /hive/auth/games/cache`로 패턴 매칭 삭제

### 5.4 로깅/운영

`private/confluence/35568344.md` (로깅 스택 구축 가이드) 기반:

- 각 WAS에 Promtail 컨테이너 배치 → 환경별 Loki로 전송
- 상용 로그 수집 서버: `hvanmetricscreator-collectlog-live-01` (Primary) / `-02` (Standby)
- 샌드박스/테스트 전용 수집 서버 분리
- Grafana Explore에서 `{service_name=...}` 레이블 필터로 즉시 조회

### 5.5 CI/CD

- Jenkins 멀티브랜치 파이프라인 + Dockerized 배포
- `analytics-common-api` 저장소의 `Jenkinsfile`로 브랜치별 이미지 빌드/배포 자동화
- 본 프로젝트 이후에도 Docker 리소스 정리 방식 개선 등 Jenkinsfile 개선이 지속됨(저장소 커밋 이력 근거)

## 6. 성과

- **광고 성과 분석 가능화**: 기존 애널리틱스에서 확인할 수 없던 광고 유입·전환·캠페인 성과 지표를 Airbridge 기반으로 애널리틱스 UI 내에서 측정 가능하게 되어, 광고주/마케터의 데이터 접근성 향상
- **지표·퍼널 분석 확장**: 차트·퍼널 분석이 BigQuery 단일 소스가 아닌 BigQuery + MMP 결합 데이터까지 다룰 수 있게 확장
- **공통 API 재사용성**: 본 프로젝트에서 정립한 `DataCollection` → `ProcessedData` 계약은 이후 2025-06 React 리뉴얼, 대시보드 기능 개선(QA 단계, GCPPDT-639)에서도 동일 경로로 재사용됨
- **단독 유지보수 가능 규모**: `analytics-common-api` 저장소의 내 커밋 비중 ~92% (231/251 커밋, 2024-09~2026-04). 본 프로젝트 완료 후에도 BigQuery Decimal 타입 변환, 피벗 NULL 플레이스홀더, `date_type=MINUTE` 검증 등 후속 개선을 지속 수행

## 7. 증거 (Evidence)

### 7.1 Jira
- **GCPPDTDW-2386** "공통 API - 2025" (Story, Done, updated 2026-04-15) — 2025년 공통 API 전체를 묶는 상위 Story. 하위 작업에 분산된 실제 구현의 집계 지점. assignee=본인. ([`private/jira/GCPPDTDW-2386.md`](../../../private/jira/GCPPDTDW-2386.md))

### 7.2 Confluence
- **지표 공통 API 명세 문서** (Page 35568348, author 김석근, lastmodified 2025-11-18): `/common/processed-data` 엔드포인트, `AirbridgeData.option`(timezone, event_timestamp_source), `APICode` / `ProcessedData.result_code` 정의, Swagger URL `https://analytics-metricscreatorapi.withhive.com/docs` ([`private/confluence/35568348.md`](../../../private/confluence/35568348.md))
- **로깅 스택 구축 가이드** (Page 35568344, author 김석근, lastmodified 2025-02-06 — **본 프로젝트 기간과 일치**): Promtail/Loki/Grafana 구성, 환경별 수집 서버, `analytics-common-api-backend-1` 서비스 레이블 ([`private/confluence/35568344.md`](../../../private/confluence/35568344.md))
- **애널리틱스 리포트 아키텍처 분석** (Page 35568410, author 김석근, lastmodified 2025-02-27 — **본 프로젝트 기간과 일치**): Spring Boot 리포트 계층/모델(ReportInfo, PageInfo, DataSourceInfo), OAuth 인증 흐름 ([`private/confluence/35568410.md`](../../../private/confluence/35568410.md))

### 7.3 GitHub
- **c2spf/analytics-common-api** (private, Python/JavaScript, 575 KB): 본인 커밋 231/251 (~92%), 기여 기간 2024-09-02 ~ 2026-04-16. 커밋 메시지 중 본 프로젝트 영역 증거:
  - `BigQuery Decimal 타입 컬럼을 적절한 숫자 타입(int64/float64)으로 변환` (2026-04)
  - `피벗 테이블 생성 시 축(axis) 컬럼의 NULL 값을 플레이스홀더로 대체` (2026-04)
  - `date_type이 MINUTE일 때 minute_interval 유효성 검사 로직 추가 및 API ...` (2025-12)
  - `Jenkinsfile에서 Docker 리소스 정리 방식 개선` (2025-11)
  - 참고: [`docs/10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md`](../../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md)

### 7.4 Swagger / 운영
- Analytics Common API Swagger UI: <https://analytics-metricscreatorapi.withhive.com/docs>

## 8. STAR 요약

- **S (Situation)**: 기존 애널리틱스는 내부 게임 로그(BigQuery) 기반 분석만 가능해 광고 성과(에어브릿지 MMP) 데이터를 지표·퍼널 분석에서 확인할 수 없었다.
- **T (Task)**: 에어브릿지 데이터를 애널리틱스 지표·퍼널 분석에 주입할 수 있도록 데이터 가공 API를 설계·구현하고, 기존 Spring Boot 리포트 스택과 신규 FastAPI 공통 API를 함께 확장한다.
- **A (Action)**: 지표 공통 API `/common/processed-data`에 `AirbridgeData` 모델과 옵션(timezone, event_timestamp_source)을 추가하고, BigQuery·Airbridge 쿼리를 동시에 실행·피벗팅하여 단일 응답(`ProcessedData`)으로 반환하도록 구현. Spring Boot 리포트 계층은 `DataSourceInfo` 확장으로 공통 API에 연결. Hive OAuth 인증과 회사/메뉴 권한 정책을 그대로 재사용하고, Promtail/Loki/Grafana 로그 스택으로 3환경 운영 가시성을 확보.
- **R (Result)**: 광고주·마케터가 애널리틱스 UI 내에서 광고 성과를 측정할 수 있게 되어 서비스 활용성과 가치가 증대. 본 프로젝트에서 정립된 `DataCollection → ProcessedData` 계약은 이후 React 리뉴얼과 대시보드 기능에서도 동일 경로로 재사용되었고, `analytics-common-api` 저장소는 본인이 2024-09부터 단독에 가까운 비중(~92%)으로 유지보수하는 주력 공통 모듈로 자리잡음.

## 9. 관련 프로젝트

- **[2024-08 애널리틱스 공통 모듈 & 배포 개선](./2024-08-analytics-common-module.md)** — 본 프로젝트의 선행. 공통 API 기반 및 Docker/멀티브랜치 파이프라인 도입
- **[2025-06 애널리틱스 React 리뉴얼](./2025-06-analytics-react-renewal.md)** — 본 프로젝트에서 확립한 공통 API 계약을 프런트엔드가 소비
