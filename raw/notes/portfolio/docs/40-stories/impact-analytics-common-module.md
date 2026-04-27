---
title: "애널리틱스 공통 모듈화 + 배포 표준화로 팀 개발 효율 향상"
type: story
category: impact
period: "2024-08 ~ 현재"
primary_project: "2024-08-analytics-common-module"
tags: [platform, common-module, devops, jenkins, docker]
skills_demonstrated:
  - backend-python
  - devops-cicd
  - data-pipeline
---

# 애널리틱스 공통 모듈화 + 배포 표준화로 팀 개발 효율 향상

## Situation

애널리틱스(게임 데이터 분석 BI) 서비스가 다년간 확장되면서 리포트·대시보드별로 **데이터 가공·시각화 로직이 중복·분산**되고, 배포는 서버별 수동 작업 비중이 커 속도·안정성 측면에서 한계가 컸다. 환경별 로그도 개별 서버에 산재해 장애 트러블슈팅 시 SSH로 직접 접속해 검색해야 했다 (출처: `2024-08-analytics-common-module.md` 배경 섹션).

## Task

- 공통 API·공통 JavaScript 모듈을 신규 설계·개발해 데이터 가공/권한/HIVE 인증 로직을 **단일 소스로 수렴**
- Docker Compose + Jenkins 멀티 브랜치 파이프라인을 팀 표준으로 도입하고 **가이드 문서화**
- Promtail/Loki/Grafana 로깅 스택을 환경별로 분리 구축해 **운영 가시성** 확보

## Action

- **공통 API 서버 설계·구현** (`c2spf/analytics-common-api`, Python/FastAPI): `APIResponse { result_code, message, data }` 표준 포맷 + `APICode` 13종 + BigQuery `ProcessedData` 결과 코드 4종을 정립. `/common/processed-data`, `/permissions`, HIVE OAuth 8개 엔드포인트 통합 (Confluence 35568348).
- **공통 JavaScript + AG-grid 도입**: 프런트용 '지표 공통 JavaScript' 모듈 분리 제공, AG-grid Enterprise·테이블 전치(Transpose) 구현 가이드 작성 (Confluence 35568328 / 35568724 / 35568748). 후속 React 리뉴얼의 차트·테이블 기반이 됨.
- **배포 가이드 4종 이틀 집중 발행 (2024-10-28 ~ 10-29)**: Jenkins 멀티 브랜치 파이프라인 가이드(35568332), Docker Compose 배포 가이드(35568336), 공통 API/JS 서비스 배포 가이드(35568340), 공통 JavaScript 사용 가이드(35568328)를 단기간 집중 정비해 팀 표준으로 고정.
- **로깅 스택 표준화**: Promtail(WAS 사이드카) → Loki(환경별 4종: 상용 Primary/Standby + 샌드박스 + 테스트) → 중앙 Grafana 구조를 Docker로 운영하고, Loki 배포용 Jenkinsfile도 재작성해 배포 파이프라인을 재사용 (Confluence 35568344).
- **단독 유지보수 체계 지속**: 2024-09부터 현재까지 공통 API 저장소를 단독 유지하며 BigQuery Decimal 타입 변환, 피벗 축 NULL 플레이스홀더 대체, OS별 TCP Keepalive 개선, 슬레이브 DB 동기화 이슈 대응 등 운영 이슈를 지속 해소.

## Result

- **정량**:
  - `analytics-common-api` 저장소 내 **커밋 231 / 251 ≈ 92%** 점유 — 단독 유지보수 가능한 수준으로 경계 설계가 정리됨 (출처: `github-c2spf/repos/analytics-common-api.md`).
  - 배포·운영 가이드 **4종 이틀 집중 발행** (2024-10-28 ~ 10-29)으로 팀 표준 확립.
  - **Loki 인스턴스 4개 환경** 분리 운영 (상용 Primary/Standby + 샌드박스 + 테스트, Confluence 35568344).
  - 공통 API 엔드포인트 그룹 **4개**(/common, /permissions, /hive, HIVE Auth 하위 8종) 공개 운영 (Confluence 35568348).
- **정성**:
  - 공통 API + 공통 JS로 수렴되며 리포트 간 **코드 일관성·유지보수성 향상** (old-portfolio 인용).
  - Docker + 멀티 브랜치 파이프라인으로 **배포 속도·안정성 모두 개선** (old-portfolio 인용).
  - 4개 환경 로그가 Grafana 단일 인터페이스에서 조회·필터링 가능해져 **장애 트러블슈팅 난이도 하락**.
- **지속 운영**: 2024-08 시작분이 상위 Story **"공통 API - 2025"(GCPPDTDW-2386, 2026-04-15 Done)** 로 이어지며 장기 진화 중.

## 관련 증거

- GitHub: <https://github.com/c2spf/analytics-common-api> (private, 커밋 231/251 ≈ 92%)
- Confluence (본문 수집): 35568348 (지표 공통 API 명세), 35568344 (로깅 스택 구축 가이드)
- Confluence (메타): 35568332 (Jenkins 멀티 브랜치), 35568336 (Docker Compose), 35568340 (공통 API/JS 서비스 배포), 35568328 (공통 JS 사용), 35568724 · 35568748 (AG-grid)
- Jira: **GCPPDTDW-2386** (공통 API - 2025 상위 Story), GCPSRE-16239, GCPSRE-15853, GCPHDBA-2820
- 관련 프로젝트: [`2024-08-analytics-common-module`](../20-projects/com2us-platform/2024-08-analytics-common-module.md), [`2025-06-analytics-react-renewal`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
