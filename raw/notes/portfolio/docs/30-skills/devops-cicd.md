---
title: "DevOps / CI-CD"
type: skill
category: devops
slug: devops-cicd
years_of_experience: 8
proficiency: proficient
related_stack:
  - Docker
  - Docker Compose
  - Jenkins
  - GitHub Actions
  - Nginx
  - CentOS
  - Ubuntu
  - Promtail
  - Loki
  - Grafana
  - Fluentd
  - ElasticSearch
  - Kibana
tags: [devops, ci-cd, docker, jenkins, observability]
---

# DevOps / CI-CD

## 개요

Docker 기반 컨테이너 배포와 Jenkins 멀티 브랜치 파이프라인 설계·도입을 주도하며, 관측(Observability) 스택(Promtail/Loki/Grafana, Fluentd/ES/Kibana)까지 포함해 팀 내 배포·운영 표준을 수립해 온 DevOps 경력. 특히 2024-08 **애널리틱스 공통 모듈 & 배포 개선** 프로젝트에서 Docker Compose + Jenkins 멀티브랜치 배포 프로세스를 팀 표준으로 만들고 **배포/운영 가이드 4종을 2024-10~11에 집중 발행**해 사내 재사용 기반을 구축한 것이 대표 성과. 이후 Airbridge API(2025-01), 모바일 리포트(2025-03), React 리뉴얼(2025-06) 등 후속 프로젝트에서 동일 파이프라인을 재활용.

## 경력 타임라인 (근거 기반)

| 시점 | 프로젝트 | 역할 | 근거 |
|------|---------|------|------|
| 2020-08 ~ 2021-09 | 애널리틱스 ML 유저 예측 | Docker 배포, GCP AI Platform Pipeline 기반 MLOps | `old-portfolio.md` "애널리틱스 ML 유저 예측", `analytics-prediction.md` |
| 2021-10 ~ 2022-04 | CODE 트래블룰 API | Docker + AWS 기반 배포 | `old-portfolio.md` "CODE 트래블룰", `travelrule-api.md` |
| 2022-05 ~ 2024-03 | NFT 마켓 | **컨테이너 기반 배포 프로세스 개선** (Docker 컨테이너 빌드·이미지·릴리스 절차 표준화), Fluentd → ES → Kibana 로그 파이프라인 | `2022-05-nft-market.md` §3.2, old-portfolio.md 성과 |
| 2024-04 ~ 2024-07 | XPLA 플랫폼 | Docker 기반 배포로 블록체인 노드 의존 등 환경 편차 격리 | `2024-04-xpla-platform.md` §5, 기술 포인트 표 |
| 2024-08 ~ 2024-12 | 애널리틱스 공통 모듈 & 배포 개선 | **Docker Compose + Jenkins 멀티 브랜치 파이프라인 도입 주도**, 배포/운영 가이드 4종 집중 발행, Promtail/Loki/Grafana 로깅 스택 4환경 구축 | `2024-08-analytics-common-module.md` (대표 프로젝트) |
| 2025-01 ~ 2025-02 | Airbridge 데이터 가공 API | Jenkins 멀티브랜치 파이프라인 + Dockerized 배포, 3환경 로그 집중화 | `2025-01-airbridge-api.md` §5.5 |
| 2025-06 ~ 현재 | 애널리틱스 React 리뉴얼 | Docker + Jenkins 배포 파이프라인 유지·개선 (Docker 리소스 정리·네트워크 존재 검사 등) | `2025-06-analytics-react-renewal.md`, `analytics-common-api.md` 커밋 이력 |
| 개인 프로젝트 | Mate Chat / 트래블메이트 | Docker Compose, GitHub 기반 배포 | `old-portfolio.md` L257, L264 |

## 프로젝트 증거 (이 스킬을 사용한 프로젝트)

| 프로젝트 | DevOps 기여 | 문서 |
|---------|------------|------|
| 애널리틱스 공통 모듈 & 배포 개선 (2024-08 ~ 2024-12) | **Docker Compose 배포 가이드 / Jenkins 멀티브랜치 파이프라인 가이드 / 공통 API·JS 서비스 배포 가이드 / 로깅 스택 구축 가이드 4종** 단기간 집중 발행. 4개 Loki 인스턴스(상용 Primary/Standby/샌드박스/테스트) Docker 운영. Jenkinsfile을 공통 API와 Loki 배포에 재사용 | [`2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md) §수행 내역 3·4 |
| Airbridge 데이터 가공 API (2025-01 ~ 2025-02) | Jenkins 멀티브랜치 파이프라인 + Dockerized 배포. Promtail 컨테이너 사이드카 → Loki → Grafana 3환경 구성 | [`2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md) §5.4, §5.5 |
| 애널리틱스 React 리뉴얼 (2025-06 ~ 현재) | `analytics-common-api` Jenkinsfile 운영 개선: Docker 리소스 정리 방식 개선(2025-11), Docker 네트워크 존재 여부 검사, v2 서버군 도커·nginx 표준 구성(GCPSRE-15853), 공통 API nginx 정합성 개선(GCPSRE-16239, `proxy_intercept_errors off`) | [`2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) §주요 작업 4 |
| NFT 마켓 (2022-05 ~ 2024-03) | 컨테이너 기반 배포 프로세스 개선(Docker 빌드·이미지·릴리스 표준화), Fluentd → ElasticSearch → Kibana 로그 수집 파이프라인 구축 | [`2022-05-nft-market.md`](../20-projects/com2us-platform/2022-05-nft-market.md) §3.2 |
| XPLA 플랫폼 (2024-04 ~ 2024-07) | Docker 기반 배포로 환경 일관화, 블록체인 노드 의존 컨테이너화 | [`2024-04-xpla-platform.md`](../20-projects/com2us-platform/2024-04-xpla-platform.md) §5, 기술 포인트 |
| 트래블룰 API (2021-10 ~ 2022-04) | Docker + AWS 배포, Sphinx 기반 API 문서 배포 파이프라인 | [`travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) |
| 애널리틱스 본체 (지속) | 읽기전용 트래픽 마스터 전환·TCP Keepalive 개선 등 운영 이슈 Jenkinsfile 반영 | [`analytics-common-api.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md) 특이 사항 |

## 주요 기술 포인트

### 1. Docker Compose + Jenkins 멀티 브랜치 파이프라인 (팀 표준 도입)

2024-08 공통 모듈 프로젝트에서 **팀 내 배포 표준**을 정립:

- **브랜치별 자동 빌드·배포** — 상용/스테이징/샌드박스/테스트 4개 브랜치가 각 환경으로 자동 배포
- **Jenkinsfile 재사용** — 공통 API 배포 Jenkinsfile을 로그 수집(Loki) 배포에도 재사용
- **운영 개선 지속** — Jenkinsfile Docker 리소스 정리 방식 개선, Docker 네트워크 존재 여부 검사(2025-11) 등 운영 중 발견 이슈를 파이프라인에 반영
- **2024-10~11 집중 가이드 발행 (4종)**:
  - Confluence 35568336 — Docker와 Docker Compose를 이용한 배포 가이드 (2024-10-29)
  - Confluence 35568332 — Jenkins 멀티 브랜치 파이프라인을 이용한 배포 가이드 (2024-10-28)
  - Confluence 35568340 — 지표 공통 API/JS 서비스 배포 가이드 (2024-10-28)
  - Confluence 35568344 — 로깅 스택 구축 가이드 (2025-02-06)

### 2. 관측 스택 (Observability)

- **Promtail / Loki / Grafana** (애널리틱스, 2024-08~):
  - WAS 사이드카로 Promtail 배치 → 환경별 Loki 서버로 전송 → 중앙 Grafana Explore에서 `{service_name="analytics-common-api-backend-1"}` 등 레이블 쿼리
  - 상용 Primary/Standby + 샌드박스 + 테스트 **4개 Loki 인스턴스 분리 운영**
  - Loki 배포용 Jenkinsfile까지 작성해 관측 인프라 자체를 자동화
- **Fluentd / ElasticSearch / Kibana** (NFT 마켓, 2022-05~):
  - NestJS 지갑 백엔드 로그를 Fluentd로 수집 → ES → Kibana 대시보드

### 3. Nginx 운영

- GCPSRE-16239 공통 API 서버 nginx 설정 변경 요청(2025-07-08 Done) 주도 — JSON API 응답을 위한 **`proxy_intercept_errors off` 전환**
- v2 서버군(WAS/Front/BI, live/staging/sandbox/test) nginx 표준 구성(GCPSRE-15853)

### 4. 인프라 요청·조정 (SRE/DBA 협업)

- 프로젝트 단독 DevOps 리더로서 SRE/DBA 티켓을 본인이 reporter로 올려 선제적 인프라 준비:
  - `GCPSRE-16239` 공통 API nginx 설정 변경 (2025-07-08 Done)
  - `GCPSRE-15853` v2 서버 패키지 설치 요청 (2025-05-09 Done)
  - `GCPHDBA-2820` 권한 관리 시스템 DB 서버 신청 (2024-11-15 Done)
  - `GCPHDBA-1245` 블록체인 웹 지갑 상용 DB 서버 신청 (2022-07, XPLA 웹 지갑 선행 인프라)

### 5. MLOps / 비동기 워크플로우

- **GCP AI Platform Pipeline + Digdag** 기반 MLOps 구축(2020-08 ML 예측) — 이후 ML 요구사항에 대한 빠른 대응 가능 (`old-portfolio.md` 성과)
- Digdag 워크플로우로 게임 정보 동기화 스케줄러 운영(2018-07)

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| Docker | expert | 2020년 이후 모든 프로젝트(ML 예측, 트래블룰, NFT, XPLA, 공통 모듈, Airbridge, React 리뉴얼, 개인 프로젝트)에서 사용. NFT 마켓에서는 컨테이너 배포 프로세스 개선 자체가 프로젝트 성과 |
| Docker Compose | proficient | 애널리틱스 공통 모듈에서 팀 표준 도입, 가이드 문서(Confluence 35568336) 작성 |
| Jenkins (멀티 브랜치 파이프라인) | proficient | 공통 모듈 프로젝트에서 팀 표준 설계·도입, 가이드 문서(Confluence 35568332) 작성, Jenkinsfile을 앱·Loki 배포에 재사용 |
| GitHub Actions | competent | 개인 프로젝트(Mate Chat, 트래블메이트) 범위 |
| Nginx | proficient | v2 서버군 표준 구성 및 nginx 설정 변경 요청 주도(GCPSRE-16239, GCPSRE-15853) |
| Promtail / Loki / Grafana | proficient | 4환경 분리 Loki 인스턴스 운영, Grafana 중앙 쿼리 도입 (Confluence 35568344) |
| Fluentd / ElasticSearch / Kibana | competent | NFT 마켓 로그 파이프라인 구축·운영 |
| CentOS / Ubuntu | competent | `old-portfolio.md` 명시, 운영 서버 OS |
| GCP AI Platform Pipeline | competent | 2020 ML 예측 MLOps 구축 |
| Digdag | competent | 게임 정보 동기화 스케줄러 운영 |

## 관련 스킬 문서

- [`backend-python.md`](./backend-python.md) — FastAPI/Flask 서비스의 CI/CD 대상
- [`backend-java-spring.md`](./backend-java-spring.md) — Spring Boot 서비스의 CI/CD 대상
- [`database.md`](./database.md) — SRE/DBA 협업으로 DB 인프라 요청·운영

## 관련 정량 지표

- **배포/운영 가이드 4종 집중 발행** — 2024-10-28 ~ 2024-11 단기간에 Docker Compose · Jenkins 멀티브랜치 · 공통 API/JS 배포 · 로깅 스택 가이드 동시 정비 (`2024-08-analytics-common-module.md` metrics)
- **Loki 인스턴스 4개 환경 분리 운영** — 상용 Primary/Standby + 샌드박스 + 테스트 (Confluence 35568344)
- **Jenkinsfile 재사용성** — 공통 API와 로그 수집(Loki) 배포에 동일 Jenkinsfile 템플릿 적용
- **인프라 티켓 reporter 주도** — GCPSRE-16239 / 15853, GCPHDBA-2820 / 1245 등 다수 인프라 사전 요청 주도
- **NFT 마켓 성과** — "컨테이너 관리 방식을 개선해 배포 효율성과 생산성을 향상" (`old-portfolio.md` 성과)

## 관련 프로젝트 전체 목록

- [`../20-projects/com2us-platform/2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md) (대표)
- [`../20-projects/com2us-platform/2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md)
- [`../20-projects/com2us-platform/2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
- [`../20-projects/com2us-platform/2024-04-xpla-platform.md`](../20-projects/com2us-platform/2024-04-xpla-platform.md)
- [`../20-projects/com2us-platform/2022-05-nft-market.md`](../20-projects/com2us-platform/2022-05-nft-market.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md)
