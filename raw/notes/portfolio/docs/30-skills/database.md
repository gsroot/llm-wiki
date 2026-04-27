---
title: "Database (MySQL, PostgreSQL, MariaDB, Redis, BigQuery)"
type: skill
category: database
slug: database
years_of_experience: 10
proficiency: expert
related_stack:
  - MySQL
  - MariaDB
  - PostgreSQL
  - Redis
  - BigQuery
  - SQLAlchemy
  - Alembic
  - TypeORM
  - MyBatis
  - JPA
  - HiveQL
tags: [database, sql, nosql, redis, bigquery, rdbms]
---

# Database (MySQL, PostgreSQL, MariaDB, Redis, BigQuery)

## 개요

2016년 줌인터넷 데이터 분석(HiveQL) 시점부터 시작해 컴투스플랫폼 애널리틱스·블록체인·규제 대응·ML 예측까지 거의 모든 프로젝트에서 DB 설계·운영을 담당한 **누적 10년 경력**의 핵심 스킬. 운영 단계에서는 **MySQL 8.4 업그레이드 대응**, **슬레이브 DB 동기화 이슈로 읽기전용 트래픽 마스터 전환** 같은 장애 시나리오를 커밋 단위로 해결했고, 설계 단계에서는 **BigQuery + MySQL + Redis** 하이브리드 분석 파이프라인과 **MariaDB + Redis + NATS** 규제 API 스택을 구축. 개인 프로젝트에서는 PostgreSQL + SQLAlchemy + Alembic 스택으로 FastAPI 백엔드를 출시까지 운영.

## 경력 타임라인 (근거 기반)

| 시점 | 프로젝트 | DB 역할 | 근거 |
|------|---------|--------|------|
| 2016-02 ~ 2016-06 | 줌닷컴 사용자 데이터 분석 | **HiveQL** 분산 쿼리로 사용자 행동 분석 | `old-portfolio.md` L237 |
| 2016-01 ~ 2016-07 | 스윙 브라우저 플러그인 | MySQL + Spring Boot | `old-portfolio.md` L247 |
| 2017-05 ~ 현재 | 애널리틱스 본체 | **MySQL + Redis + GCP BigQuery** (장기 운영) | `old-portfolio.md` L164 |
| 2018-07 ~ 2018-08 | 게임 정보 동기화 스케줄러 | MySQL, GCP BigQuery, Redis 동기화 | `old-portfolio.md` L227 |
| 2019-03 ~ 2019-06 | 대용량 데이터 다운로드 REST API | MySQL, Redis, GCP BigQuery, GCP Storage | `old-portfolio.md` L218, `analytics-download.md` |
| 2020-08 ~ 2021-09 | 애널리틱스 ML 유저 예측 | MySQL 5.5(`CLASSIFICATION` DB), Redis, GCP AutoML, BigQuery ML | `old-portfolio.md` L209, `analytics-prediction.md` |
| 2021-06 ~ 2021-07 | 통합 인증 & 비동기 공통 모듈 | MySQL, Redis, SQLAlchemy | `old-portfolio.md` L200 |
| 2021-10 ~ 2022-04 | CODE 트래블룰 API | **MariaDB**, Redis, NATS, SQLAlchemy, Alembic | `old-portfolio.md` L191, `travelrule-api.md` |
| 2022-05 ~ 2024-03 | NFT 마켓 | MySQL (8, MASTER-SLAVE 웹 지갑 DB), Redis, TypeORM | `2022-05-nft-market.md`, GCPHDBA-1245 |
| 2024-04 ~ 2024-07 | XPLA 플랫폼 | MySQL 8 MASTER-SLAVE (`wallet-db-live-*` 재사용), TypeORM | `2024-04-xpla-platform.md` §기술 포인트 |
| 2024-08 ~ 2024-12 | 애널리틱스 공통 모듈 | MySQL, Redis, GCP BigQuery 통합 처리 | `2024-08-analytics-common-module.md` |
| 2025-01 ~ 2025-02 | Airbridge 데이터 가공 API | MySQL, Redis, BigQuery + Airbridge 외부 소스 결합 | `2025-01-airbridge-api.md` |
| 2025-06 ~ 현재 | 애널리틱스 React 리뉴얼 | **MySQL 8.4 업그레이드 대응** (`analytics-common-api` 커밋), BigQuery Decimal→숫자 변환, 슬레이브 동기화 이슈 대응 | `2025-06-analytics-react-renewal.md`, `analytics-common-api.md` |
| 2025-08 ~ 현재 | 개인: Mate Chat | **PostgreSQL** + SQLAlchemy + Alembic + Redis | `old-portfolio.md` L257 |
| 2025-10 ~ 2025-11 | 개인: 트래블메이트 | PostgreSQL + SQLAlchemy + Alembic | `old-portfolio.md` L264 |

## 프로젝트 증거 (이 스킬을 사용한 프로젝트)

| 프로젝트 | 주요 DB 작업 | 문서 |
|---------|-------------|------|
| 애널리틱스 본체 (2017~) | MySQL + Redis + BigQuery 하이브리드. BigQuery Decimal 컬럼 int64/float64 변환, `date_type=MINUTE` 검증, 피벗 축 NULL 플레이스홀더 대체 등 데이터 타입 안정화 지속 | [`analytics-common-api.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md) 특이 사항 |
| 애널리틱스 공통 모듈 (2024-08~) | MySQL 8.4 업그레이드 대응, **슬레이브 DB 동기화 이슈로 읽기전용 트래픽도 마스터 DB 전환** (2025-11 커밋), OS별 TCP Keepalive 개선, Redis 기반 `/hive/auth/games` 캐시 + 패턴 매칭 무효화 | [`2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| Airbridge 데이터 가공 API (2025-01) | BigQuery + Airbridge 쿼리 결합·피벗팅, Redis 캐시 기반 사용자/메뉴/게임 권한 제공 | [`2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md) §5.3 |
| ML 유저 예측 (2020-08) | MySQL 5.5 `CLASSIFICATION` DB, Redis, **GCP AutoML + BigQuery ML** 기반 예측 모델 운영 | [`analytics-prediction.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md) |
| 대용량 데이터 다운로드 REST API (2019-03) | MySQL, Redis, **BigQuery + Celery 비동기 워커** 기반 대용량 다운로드 JobQueue 설계 | [`analytics-download.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-download.md) |
| NFT 마켓 (2022-05) | MySQL 8 MASTER-SLAVE(`wallet-db-live-11/12`) DB 서버 신청(GCPHDBA-1245, 2022-07), Redis 캐시, TypeORM으로 지갑/NFT 메타데이터 모델링 | [`2022-05-nft-market.md`](../20-projects/com2us-platform/2022-05-nft-market.md) §3.1, §3.2 |
| XPLA 플랫폼 (2024-04) | 2022년 구축된 `wallet-db-live-*` 인프라 재사용, TypeORM 기반 백엔드 | [`2024-04-xpla-platform.md`](../20-projects/com2us-platform/2024-04-xpla-platform.md) |
| CODE 트래블룰 API (2021-10) | **MariaDB** + Redis + NATS, SQLAlchemy + Alembic, Locust 부하 테스트 | [`travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) |
| 줌닷컴 사용자 데이터 분석 (2016-02) | **HiveQL** 분산 시스템 기반 쿼리 경험 | `old-portfolio.md` |
| 권한 관리 시스템 DB (2024-11) | GCPHDBA-2820 요청자로 본인이 서비스 런칭 전 인프라 사전 준비 | [`2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md) §5 |
| 개인: Mate Chat (2025-08~) | **PostgreSQL** + SQLAlchemy + Alembic + Redis, WebSocket 채팅·AI 대화 영속화 | `old-portfolio.md` L257 |
| 개인: 트래블메이트 (2025-10) | PostgreSQL + SQLAlchemy + Alembic, 여행→1차 계획→장소 계층 데이터 모델 | `old-portfolio.md` L264 |

## 주요 기술 포인트

### 1. MySQL 장기 운영과 장애 대응

- **MySQL 8.4 업그레이드 대응** — `analytics-common-api` 2025-11 커밋에서 업그레이드 전후 호환 확인 (`analytics-common-api.md` 특이 사항)
- **슬레이브 동기화 장애 대응** — "인프라 부서로부터 전달받은 슬레이브 DB 동기화 이슈 때문에 애널리틱스는 읽기전용도 마스터 DB를 보도록…" (2025-11 커밋) — **읽기전용 트래픽을 마스터로 강제 라우팅하는 임시 조치**
- **OS별 TCP Keepalive 설정 개선** (2025-10 커밋) — 커넥션 풀 안정성 확보
- **MASTER-SLAVE 구성** — 블록체인 웹 지갑 상용 DB(GCPHDBA-1245, 2022-07)를 본인이 요청자로 신청해 `wallet-db-live-11/12` MASTER-SLAVE 인프라 도입

### 2. Redis 고가용성·캐시 전략

- **`/hive/auth/games` Redis 캐시 + 패턴 매칭 무효화** — `DELETE /hive/auth/games/cache`에서 패턴 매칭으로 일괄 무효화 (`2024-08-analytics-common-module.md` §1)
- **다수 프로젝트에서 메시지 큐·세션·캐시 3역할로 Redis 활용** — ML 예측, 인증 공통 모듈, 트래블룰, NFT, XPLA, 공통 모듈, Airbridge, React 리뉴얼, 개인 프로젝트 전반
- 트래블룰 API에서는 **Redis + NATS** 메시지 버스 조합으로 비동기 이벤트 전달

### 3. BigQuery 대용량 분석

- **애널리틱스 본체의 주 분석 엔진** — 2017년 이후 모든 리포트·퍼널·리텐션·대시보드 집계의 근간
- **Decimal 타입 이슈 해소** — 2026-04 커밋 "BigQuery Decimal 타입 컬럼을 적절한 숫자 타입(int64/float64)으로 변환"
- **피벗팅 엣지 케이스** — 피벗 축 컬럼 NULL을 플레이스홀더로 대체, `date_type=MINUTE` 시 `minute_interval` 유효성 검사
- **BigQuery ML / AutoML** — 2020 ML 예측 프로젝트에서 유저 이탈·구매 예측(평균 정확도 85%+)

### 4. SQLAlchemy + Alembic (Python ORM 표준)

- **통합 인증 공통 모듈(2021-06)부터 트래블룰(2021-10), 게임 정보 동기화(2018-07), ML 예측, 대용량 다운로드까지** 다수 Python 프로젝트에서 SQLAlchemy를 표준으로 채택
- 개인 프로젝트(Mate Chat, 트래블메이트)에서도 **Alembic 마이그레이션**을 운영에 사용하여 Google Play Store 출시까지 진행

### 5. 다중 ORM 경험

- **TypeORM** (NestJS 기반 NFT 마켓, XPLA 플랫폼)
- **MyBatis + JPA** (애널리틱스 본체 Spring Boot, 다중 데이터소스)
- **SQLAlchemy** (Python 생태계 전반)

### 6. DB 인프라 요청·신청 (DBA 협업)

- **GCPHDBA-2820** 권한 관리 시스템 DB 서버 신청 (2024-11-15 Done, 본인 reporter)
- **GCPHDBA-1245** 블록체인 웹 지갑 상용 DB 서버 신청 (2022-07, 본인 reporter)

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| MySQL | expert | 2016~현재 장기 운영, MySQL 8.4 업그레이드 대응, 마스터/슬레이브 동기화 이슈 대응, MASTER-SLAVE 인프라 설계 경험 |
| MariaDB | proficient | CODE 트래블룰 API 주 DB로 Alembic 마이그레이션과 Locust 부하 테스트 운영 |
| Redis | expert | 거의 모든 프로젝트에서 캐시·세션·메시지 큐 3역할로 사용. 패턴 매칭 무효화, NATS 조합 등 고급 패턴 경험 |
| PostgreSQL | proficient | 개인 프로젝트(Mate Chat, 트래블메이트)에서 SQLAlchemy + Alembic 기반 출시 수준 운영 |
| GCP BigQuery | expert | 애널리틱스 본체 다년간 주 분석 엔진, Decimal 타입·피벗 NULL·MINUTE 검증 등 실전 엣지 케이스 해소 |
| BigQuery ML / AutoML | competent | 2020 ML 예측 프로젝트로 평균 85% 정확도 예측 모델 운영 |
| SQLAlchemy | expert | 2018년 게임 정보 동기화부터 2025년 개인 프로젝트까지 일관 사용 |
| Alembic | proficient | 트래블룰·개인 프로젝트 마이그레이션 운영 |
| TypeORM | proficient | NFT 마켓·XPLA 플랫폼 NestJS 스택 |
| MyBatis / JPA | proficient | 애널리틱스 본체 Spring Boot 다중 데이터소스 병용 |
| HiveQL | novice | 줌닷컴 분석 시절(2016) 분산 쿼리 경험 |
| NATS | novice | 트래블룰 API에서 Redis와 병용한 메시지 버스 수준 |

## 관련 스킬 문서

- [`backend-python.md`](./backend-python.md) — SQLAlchemy·Alembic의 주 사용 맥락
- [`backend-java-spring.md`](./backend-java-spring.md) — MyBatis·JPA·다중 데이터소스의 주 사용 맥락
- [`devops-cicd.md`](./devops-cicd.md) — DBA 티켓 reporter 주도, nginx/서버 패키지 설치 요청 연계

## 관련 정량 지표

- **`wallet-db-live-11/12` MASTER-SLAVE 인프라 신청·운영** — GCPHDBA-1245(2022-07) reporter (`2024-04-xpla-platform.md`, `2022-05-nft-market.md`)
- **MySQL 8.4 업그레이드 대응 + 슬레이브 동기화 장애 읽기전용 마스터 전환 임시 조치** — `analytics-common-api` 2025-11 커밋
- **BigQuery Decimal 타입 안정화 / 피벗 NULL 플레이스홀더 / date_type=MINUTE 검증** — `analytics-common-api` 2026-04·2025-12 커밋
- **ML 예측 정확도 85%+** — BigQuery ML + GCP AutoML 기반 (`old-portfolio.md` 성과)
- **개인 프로젝트 PostgreSQL 출시 운영** — 트래블메이트 Google Play Store 출시 (`old-portfolio.md` L264)

## 관련 프로젝트 전체 목록

- [`../20-projects/com2us-platform/2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md)
- [`../20-projects/com2us-platform/2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md)
- [`../20-projects/com2us-platform/2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
- [`../20-projects/com2us-platform/2024-04-xpla-platform.md`](../20-projects/com2us-platform/2024-04-xpla-platform.md)
- [`../20-projects/com2us-platform/2022-05-nft-market.md`](../20-projects/com2us-platform/2022-05-nft-market.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-common-api.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-download.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-download.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-prediction.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md)
