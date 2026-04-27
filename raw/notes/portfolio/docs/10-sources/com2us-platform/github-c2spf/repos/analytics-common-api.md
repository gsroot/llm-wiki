---
title: "c2spf/analytics-common-api"
type: source-index
company: com2us-platform
source: github
repo: c2spf/analytics-common-api
visibility: private
primary_language: Python
collected_at: "2026-04-24"
---

# c2spf/analytics-common-api

Analytics 공통 API + 공통 JavaScript — ✅ 운영 중 (지속 유지보수)

## 기본 정보

| 항목 | 값 |
|------|----|
| URL | <https://github.com/c2spf/analytics-common-api> (private) |
| Visibility | private |
| Default Branch | `main` |
| 주 언어 | Python (~97KB), JavaScript (~40KB), Dockerfile, Shell |
| 크기 | 575 KB |

## 내 기여

- **내 커밋**: **231** / 전체 251 (~92% — 거의 단독 유지보수)
- **기여 기간**: 2024-09-02 ~ 2026-04-16 (진행 중)
- **역할**: 공통 API·공통 JavaScript 설계·개발·유지보수 주 담당

## 기술 스택 (README + 커밋 메시지 기반)

- **언어**: Python (FastAPI 추정), JavaScript
- **DB**: MySQL 8.4 (2025-11 업그레이드 이력)
- **컨테이너**: Docker
- **CI/CD**: Jenkins (Jenkinsfile 포함)
- **외부 시스템**: BigQuery, Hive API

## 특이 사항 (커밋 메시지에서 확인)

- `BigQuery Decimal 타입 컬럼을 적절한 숫자 타입(int64/float64)으로 변환` (2026-04)
- `피벗 테이블 생성 시 축(axis) 컬럼의 NULL 값을 플레이스홀더로 대체` (2026-04)
- `date_type이 MINUTE일 때 minute_interval 유효성 검사 로직 추가 및 API ...` (2025-12)
- `API Reference 문서 추가` (2025-11)
- `Jenkinsfile에서 Docker 리소스 정리 방식 개선` / `Docker 네트워크 존재 여부 검사` (2025-11)
- `인프라 부서로부터 전달받은 슬레이브 DB 동기화 이슈 때문에 애널리틱스는 읽기전용도 마스터 DB를 보도록...` (2025-11)
- `Hive API 및 서비스 메서드에서 IP와 언어 코드 매개변수를 선택 사항으로 변경` (2025-10)
- `OS별 TCP Keepalive 설정 로직 개선` (2025-10)

→ 공통 API 설계·운영, BigQuery 데이터 타입 안정화, 인프라 이슈 대응, Jenkins CI/CD 개선, MySQL 버전업 전후 호환.

## 관련 프로젝트 문서

- [`docs/20-projects/com2us-platform/2024-08-analytics-common-module.md`](../../../../20-projects/com2us-platform/) (작성 예정)

## 관련 스킬

- `backend-python` (FastAPI 추정, API 설계)
- `database` (MySQL, BigQuery)
- `devops-cicd` (Jenkins, Docker)
- `frontend-vanilla-js` (공통 JavaScript)
