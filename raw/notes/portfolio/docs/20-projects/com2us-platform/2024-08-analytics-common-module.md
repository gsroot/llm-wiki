---
title: "애널리틱스 공통 모듈 개발 및 배포 프로세스 개선"
type: project
company: com2us-platform
period: "2024-08 ~ 2024-12 (이후 지속 유지보수 중)"
role: "데이터 시각화 공통 API · 공통 JavaScript 모듈 설계·개발, Docker + Jenkins 멀티 브랜치 파이프라인 기반 배포 프로세스 설계·도입, 로깅 스택(Promtail/Loki/Grafana) 구축"
tech_stack:
  - "Java (Spring Boot)"
  - "JavaScript"
  - "Python (FastAPI)"
  - "MySQL"
  - "Redis"
  - "GCP BigQuery"
  - "AG-grid"
  - "Docker / Docker Compose"
  - "Jenkins (Multi-branch Pipeline)"
  - "Promtail / Loki / Grafana"
sources:
  jira:
    - "GCPPDTDW-2386 — 공통 API - 2025 (상위 Story, Done, 2026-04-15)"
    - "GCPSRE-16239 — [애널리틱스] 애널리틱스 공통 api 서버 nginx 설정 변경 요청 (Done, 2025-07-08)"
    - "GCPSRE-15853 — [애널리틱스] v2 서버 패키지 설치 요청 (Done, 2025-05-09)"
    - "GCPHDBA-2820 — [GCP_HIVE_DBA] 애널리틱스 권한 관리 시스템 DB 서버신청 (Done, 2024-11-15)"
  confluence:
    - "35568348 — 지표 공통 API 명세 문서 (2025-11-18, 본문 수집)"
    - "35568344 — 로깅 스택 구축 가이드 (2025-02-06, 본문 수집)"
    - "35568328 — 지표 공통 JavaScript 파일 사용 가이드 (2024-10-29)"
    - "35568336 — Docker와 Docker Compose를 이용한 배포 가이드 (2024-10-29)"
    - "35568340 — 지표 공통 API/JS 서비스 배포 가이드 (2024-10-28)"
    - "35568332 — Jenkins 멀티 브랜치 파이프라인을 이용한 배포 가이드 (2024-10-28)"
    - "35568748 — ag-grid Enterprise 기능 가이드 (2025-06-09)"
    - "35568724 — ag-grid 테이블 전치(Transpose) 구현 가이드 (2025-06-02)"
    - "35568800 — 애널리틱스 '사용자 권한 게임 목록 조회' API 통합 - 오류 트러블슈팅 (2025-07-08, 본문 수집)"
  github:
    - "https://github.com/c2spf/analytics-common-api  # 내 커밋 231 / 전체 251 (~92%, 거의 단독 유지보수)"
  gmail: []
tags: [backend, platform, api, devops, jenkins, docker, logging, ag-grid, fastapi]
metrics:
  - "공통 API 저장소 내 커밋 점유율 약 92% (231/251) — 거의 단독 유지보수 (출처: github-c2spf/repos/analytics-common-api.md)"
  - "공통 API 명세 문서화: APIResponse 표준화 + 결과 코드 13종(APICode) + BigQuery 처리 결과 코드 4종 정의 (출처: Confluence 35568348)"
  - "공통 API 엔드포인트 그룹 4개(/common, /permissions, /hive, HIVE Auth 하위 8종) 공개 운영 (출처: Confluence 35568348)"
  - "로깅 스택 Loki 인스턴스 4개 환경 분리 운영: 상용 Primary/Standby + 샌드박스 + 테스트 (출처: Confluence 35568344)"
  - "배포/운영 가이드 4종 동시 발행 (공통 API 명세, 공통 JS, Jenkins 멀티브랜치, Docker Compose) — 2024-10~11 집중 정비"
related_projects:
  - "2025-01-airbridge-api"
  - "2025-06-analytics-react-renewal"
star:
  situation: "애널리틱스(게임 데이터 분석 BI) 서비스가 다년간 확장되며 리포트·대시보드별로 데이터 가공·시각화 로직이 중복·분산되어 코드 일관성과 유지보수성이 떨어지고, 배포도 서버별 수동 작업 비중이 커 속도·안정성 측면에서 한계가 있었음. 공통 API 서버·로그 수집 인프라도 환경별로 정리되어 있지 않아 장애 트러블슈팅 난이도가 높았음."
  task: "① 데이터 시각화에 공통으로 쓰이는 서버 API(피벗/집계/권한/HIVE Auth)와 프론트의 공통 JavaScript 모듈을 신규 설계·개발해 중복을 제거, ② Docker Compose + Jenkins 멀티 브랜치 파이프라인 기반 배포 프로세스를 표준화, ③ Promtail/Loki/Grafana 기반 로깅 스택을 환경별로 분리 구축해 운영 가시성을 확보."
  action: |
    - 공통 API 서버(c2spf/analytics-common-api, Python/FastAPI 추정)를 신규 설계·구현. APIResponse { result_code, message, data } 표준 포맷과 결과 코드 체계(APICode 13종 + BigQuery ProcessedData 코드 4종)를 정립하고, /common/processed-data에서 BigQuery·Airbridge 쿼리를 결합·피벗팅해 테이블로 반환하도록 설계 (Confluence 35568348).
    - HIVE OAuth 인증 플로우 전반(/hive/auth/token·check-token·menu-permissions·menu-others·combined-info·games·games/cache)을 공통 API에 통합해 사용자/메뉴/게임 권한 조회를 Redis 캐시와 함께 단일 엔드포인트 세트로 제공.
    - 권한 관리(/permissions) CRUD 엔드포인트와 중복 조합 400·미존재 404 등 표준화된 오류 처리 규약을 적용 (Confluence 35568348).
    - 프론트용 '지표 공통 JavaScript' 모듈을 분리 제공하고 AG-grid를 도입해 대용량 사용자 데이터 처리·테이블 전치(Transpose)·Enterprise 기능 활용 가이드를 작성 (Confluence 35568328, 35568724, 35568748).
    - Docker + Docker Compose 기반 컨테이너 배포 구조와 Jenkins 멀티 브랜치 파이프라인을 도입해 브랜치별(상용/스테이징/샌드박스/테스트) 자동 빌드·배포를 구성하고, 팀 내 재사용 가능한 배포 가이드 4종을 2024-10~11 집중 발행 (Confluence 35568336, 35568332, 35568340).
    - 로깅 스택을 Promtail(WAS 사이드카) → Loki(환경별 수집 서버) → Grafana(중앙 조회) 구조로 표준화. 상용 Primary/Standby, 샌드박스, 테스트 4개 Loki 인스턴스를 Docker로 운영하고 Loki 배포용 Jenkinsfile까지 작성 (Confluence 35568344).
    - 단독 유지보수 체계를 유지하며(커밋 231/251 ≈ 92%) BigQuery Decimal→숫자 타입 변환, 피벗 축 NULL 플레이스홀더 대체, OS별 TCP Keepalive 개선, 슬레이브 동기화 이슈 대응 등 운영 중 이슈를 지속 해소 (github-c2spf/repos/analytics-common-api.md).
  result: |
    - 데이터 가공·시각화 로직을 '공통 API + 공통 JavaScript' 한 세트로 수렴시켜 리포트 간 코드 일관성과 유지보수성을 크게 향상 (정성).
    - AG-grid 도입으로 대용량 사용자 데이터의 처리·가독성이 강화되어 후속 프로젝트(2025-06 React 리뉴얼)의 차트/테이블 기반이 됨.
    - Docker Compose + Jenkins 멀티 브랜치 파이프라인으로 배포 속도·반복성·안정성이 개선되어 브랜치별 환경 배포가 팀 표준이 됨 (배포 가이드 4종 집중 발행).
    - Promtail/Loki/Grafana 로깅 스택이 환경별로 분리 구축되어 SSH 수동 검색 대비 중앙 집중·실시간 필터링·협업 용이성을 확보 (Confluence 35568344).
    - 2024-08에 시작된 공통 모듈이 이후에도 상위 Story '공통 API - 2025'(GCPPDTDW-2386, 2026-04-15 Done)로 이어지며 장기 운영/진화 중.
---

# 애널리틱스 공통 모듈 개발 및 배포 프로세스 개선

## 개요

컴투스플랫폼 애널리틱스(게임 데이터 분석 BI) 서비스에서 데이터 시각화를 위한 **공통 API 서버**와 **공통 JavaScript 모듈**을 신규 설계·개발하고, **Docker Compose + Jenkins 멀티 브랜치 파이프라인** 기반 배포 프로세스, **Promtail/Loki/Grafana** 로깅 스택을 함께 도입한 플랫폼 정비 프로젝트. 2024-08 착수, 2024-12까지 1차 개발·배포 가이드 정비를 완료했으며 이후에도 `analytics-common-api` 저장소 단독 유지보수 담당으로 지속 운영 중.

## 배경 (Situation)

- 애널리틱스가 장기 확장되며 리포트·대시보드별로 **데이터 가공·시각화 로직이 중복**되고, 공통 변경이 여러 레포로 파급되어 유지보수 비용이 증가.
- 배포가 서버별 수동 작업 비중이 커서 속도·안정성 문제 상존. 상용/스테이징/샌드박스/테스트 환경별 표준 배포 절차 부재.
- 환경별 로그가 개별 서버에 산재해 장애 트러블슈팅 시 SSH로 직접 접속해 검색해야 하는 비효율.

## 목표 (Task)

1. **공통 모듈화**: 데이터 시각화/권한/HIVE 인증에 공통으로 쓰이는 API와 프론트 JS를 분리해 단일 소스로 수렴.
2. **배포 표준화**: Docker Compose + Jenkins 멀티 브랜치 파이프라인을 팀 표준으로 도입, 가이드 문서화.
3. **운영 가시성**: Promtail/Loki/Grafana를 도입해 환경별 로그를 중앙에서 조회·필터링 가능하게 구축.

## 수행 내역 (Action)

### 1. 공통 API 서버 설계·구현 (`c2spf/analytics-common-api`)

- 저장소 단독 유지보수 담당 (내 커밋 **231 / 251 ≈ 92%**, 2024-09-02 ~ 2026-04-16 진행 중).
- **응답 포맷 표준화**: `APIResponse { result_code, message, data }` + `APICode` 13종(성공 0, 검증 1001, 인증 1002~2007), `ProcessedData.result_code` 4종(BigQuery 오류 분리).
- **Common Data 엔드포인트**: `POST /common/processed-data` — BigQuery·Airbridge 쿼리를 결합·피벗팅하여 `index`, `columns`, `data`, `index_names`, `column_names`, `summary_stats`, `date_type`까지 반환.
- **HIVE OAuth 통합**: 토큰 발급/검증, 사용자 정보, 메뉴 권한, 게임 권한 등 **8개 엔드포인트**를 공통 API에 통합. `/hive/auth/games`는 Redis 캐시 기반 최적화, `/hive/auth/games/cache DELETE`는 패턴 매칭 무효화 지원.
- **권한 관리(Permissions)**: `POST/GET/DELETE /permissions/` 및 `/permissions/{id}` — 중복 조합 400, 미존재 404 등 오류 규약 일관 적용.
- **지속 유지보수 중 해소한 이슈(커밋 메시지 근거)**: BigQuery Decimal 타입 변환, 피벗 축 NULL 플레이스홀더 대체, `date_type=MINUTE`일 때 `minute_interval` 검증, OS별 TCP Keepalive, 슬레이브 DB 동기화 이슈로 인한 마스터 읽기 전환, Hive API IP/언어 파라미터 선택화.

### 2. 공통 JavaScript · AG-grid 도입

- "지표 공통 JavaScript 파일" 모듈과 사용 가이드(Confluence 35568328, 2024-10-29) 정비.
- AG-grid 도입: Enterprise 기능 가이드(35568748, 2025-06-09)와 테이블 전치(Transpose) 구현 가이드(35568724, 2025-06-02) 작성. 대용량 사용자 데이터 처리·렌더링 강화를 위한 공통 기반 확보.

### 3. Docker + Jenkins 멀티 브랜치 파이프라인 배포

- **Docker Compose 배포 가이드**(35568336, 2024-10-29), **Jenkins 멀티 브랜치 파이프라인 가이드**(35568332, 2024-10-28), **공통 API/JS 서비스 배포 가이드**(35568340, 2024-10-28) 3종을 단기간 집중 발행.
- 브랜치별 자동 빌드·배포로 **상용/스테이징/샌드박스/테스트** 환경 분리. Jenkinsfile은 공통 API뿐 아니라 로그 수집(Loki) 배포에도 재사용.
- 운영 개선 지속: Jenkinsfile Docker 리소스 정리 방식 개선, Docker 네트워크 존재 여부 검사 등(2025-11 커밋).

### 4. Promtail / Loki / Grafana 로깅 스택

- 환경별 Loki 인스턴스 4종을 Docker 컨테이너로 운영 (Confluence 35568344):
  - 상용 Primary / 상용 Standby / 샌드박스 / 테스트.
- 각 WAS에 Promtail 사이드카로 로그 전송, 상용은 상용·스테이징 WAS 로그를 함께 수집.
- 중앙 Grafana(`dtmonitoring-workgf-live-c01`)에서 Loki 데이터소스 등록 → Explore에서 `{service_name="analytics-common-api-backend-1"}` 등 레이블 기반 쿼리/필터링/시간 범위 탐색.
- 효과: 중앙 집중, 실시간 필터링, 협업 용이성, Raw/Parsed 뷰 분석.

### 5. 연관 인프라 요청 (SRE/DBA)

- `GCPSRE-16239` — 공통 API 서버 nginx 설정 변경 요청 (2025-07-08 Done).
- `GCPSRE-15853` — v2 서버 패키지 설치 요청 (2025-05-09 Done).
- `GCPHDBA-2820` — 권한 관리 시스템 DB 서버 신청 (2024-11-15 Done). 본인이 요청자(reporter)로 서비스 런칭 전 인프라 준비.

## 성과 (Result)

- **코드 일관성·유지보수성 향상**: 데이터 가공·시각화 로직이 공통 API + 공통 JS로 수렴. 단독 유지보수(~92%)가 가능한 수준으로 경계 설계가 정리됨.
- **AG-grid 도입으로 사용자 데이터 처리 강화**: 대용량 테이블/전치/Enterprise 기능이 프런트 표준이 되어 후속 "애널리틱스 React 리뉴얼"(2025-06~)의 차트·테이블 기반으로 계승.
- **배포 속도·안정성 개선**: Docker Compose + Jenkins 멀티 브랜치 파이프라인으로 브랜치-환경 자동 배포가 표준화. 배포 가이드 4종을 2024-10~11에 집중 발행하여 팀 내 재사용 가능.
- **운영 가시성 확보**: 4개 환경의 로그가 Grafana 단일 인터페이스에서 조회·필터링 가능해져 장애 트러블슈팅 난이도 하락 (정성).
- **장기 운영 지속**: 공통 API는 2024-09 이후 상위 Story "공통 API - 2025"(GCPPDTDW-2386, 2026-04-15 Done)로 이어지며 현재도 유지보수·진화 중.

## 기술 스택

- **백엔드**: Python (FastAPI 추정, 공통 API), Java (Spring Boot, 애널리틱스 본체)
- **프런트**: 공통 JavaScript (Vanilla), AG-grid (Enterprise)
- **데이터**: MySQL, Redis, GCP BigQuery, Airbridge(외부 MMP)
- **인프라·배포**: Docker, Docker Compose, Jenkins (Multi-branch Pipeline)
- **로깅·모니터링**: Promtail, Loki, Grafana

## 관련 프로젝트

- [`2025-01-airbridge-api`](./2025-01-airbridge-api.md) — 공통 API의 `AirbridgeData` 처리 경로로 직접 연결되는 후속 프로젝트.
- [`2025-06-analytics-react-renewal`](./2025-06-analytics-react-renewal.md) — 공통 JS·AG-grid 기반을 React로 승계한 프런트엔드 리뉴얼.

## 증거 링크

- GitHub: <https://github.com/c2spf/analytics-common-api> (private, 내 커밋 231/251 ~ 92%)
- Confluence (본문 수집):
  - 35568348 — 지표 공통 API 명세 문서
  - 35568344 — 로깅 스택 구축 가이드
  - 35568800 — 공통 API 통합 트러블슈팅 (관련)
- Confluence (메타만):
  - 35568328 / 35568336 / 35568340 / 35568332 (2024-10~11 배포·공통 JS 가이드)
  - 35568748 / 35568724 (ag-grid 가이드)
- Jira: GCPPDTDW-2386, GCPSRE-16239, GCPSRE-15853, GCPHDBA-2820
