---
title: "Backend — Java / Spring Boot"
type: skill
category: backend
slug: backend-java-spring
years_of_experience: 10
proficiency: proficient
related_stack:
  - Java
  - Spring Boot
  - Spring MVC
  - JPA
  - MyBatis
  - JUnit
  - Gradle
  - AG-grid
  - Thymeleaf
tags: [java, spring-boot, backend, api, bi]
---

# Backend — Java / Spring Boot

## 개요

2016년 줌인터넷 스윙 브라우저 백엔드 REST API를 Java/Spring Boot로 시작해, 2017년부터 컴투스플랫폼 애널리틱스(게임 데이터 분석 BI) **본체 리포트 백엔드**를 장기간 개발·유지보수 중. 2024-08 공통 모듈 & 배포 프로세스 개선, 2025-01 Airbridge 데이터 가공 API, 2025-03 애널리틱스 모바일 리포트까지 Spring MVC + MyBatis + JPA 다중 데이터소스 기반의 리포트 서비스 운영에 누적 **10년 경력**. Python/FastAPI 공통 API와 **하이브리드 스택**으로 공존시키며 레거시 Spring 서비스를 안정적으로 확장해 온 것이 특징.

## 경력 타임라인 (근거 기반)

| 시점 | 프로젝트 | 역할 | 근거 |
|------|---------|------|------|
| 2016-01 ~ 2016-07 | 줌인터넷 스윙 브라우저 이어보기 플러그인 백엔드 REST API | 설계·개발·문서화 (Java, Spring Boot, MySQL) | `old-portfolio.md` L247 |
| 2017-05 ~ 현재 | 컴투스플랫폼 애널리틱스 본체 (리포트/대시보드 BI) | 풀스택 개발, Spring MVC + jQuery + Highcharts 기반 | `old-portfolio.md` L164, Confluence 35568410 |
| 2024-08 ~ 2024-12 | 애널리틱스 공통 모듈 & 배포 개선 | Java(Spring Boot) 리포트 계층 + Python(FastAPI) 공통 API 동시 운영 | `2024-08-analytics-common-module.md` |
| 2025-01 ~ 2025-02 | Airbridge 데이터 가공 API | Spring MVC 컨트롤러-서비스-리포지토리 계층 + MyBatis/JPA 다중 데이터소스 확장 | `2025-01-airbridge-api.md` |
| 2025-03 ~ 2025-04 | 애널리틱스 모바일 리포트 | Java(Spring Boot) + JavaScript 기반 모바일 친화 리포트 뷰 (101/318 커밋 ~32%) | `github-c2spf/repos/analytics-mobile-report.md` |
| 2025-06 ~ 현재 | 애널리틱스 React 리뉴얼 | 기존 Spring 리포트 백엔드와 공존하는 프런트 전환 | `2025-06-analytics-react-renewal.md` |

## 프로젝트 증거 (이 스킬을 사용한 프로젝트)

| 프로젝트 | 기간 | Spring/Java 관련 역할 | 문서 |
|---------|------|-----------------------|------|
| 스윙 브라우저 이어보기 플러그인 | 2016-01 ~ 2016-07 | 백엔드 REST API 설계·개발·문서화 (Spring Boot + MySQL) | `old-portfolio.md` "스윙 브라우저 이어보기 플러그인 개발" |
| 애널리틱스 본체 (장기) | 2017-05 ~ 현재 | 세그먼트 결합, CSV 다운로드, 퍼널/코호트 분석, 커스텀 리포트 기능 (Spring Boot) | `old-portfolio.md` "애널리틱스(게임 데이터 분석 웹 서비스) 개발", Confluence 35568410 |
| 애널리틱스 공통 모듈 & 배포 개선 | 2024-08 ~ 2024-12 | Spring Boot 본체 유지 + FastAPI 공통 API 연계, Jenkinsfile 배포 표준화 | [`2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| Airbridge 데이터 가공 API | 2025-01 ~ 2025-02 | Spring MVC(컨트롤러-서비스-리포지토리) + MyBatis + JPA 다중 데이터소스, Hive OAuth 필터(`HiveConsoleSecurityAuthFilter`), 리포트 계층(ReportInfo → TabInfo → PageInfo → DataSourceInfo) 확장 | [`2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md) |
| 애널리틱스 모바일 리포트 | 2025-03 ~ 2025-04 | Spring Boot 백엔드 + JavaScript 프런트 (101 커밋 / 32% 점유), GA 통합·i18n·보안 설정 개선 | [`analytics-mobile-report.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-mobile-report.md) |
| 애널리틱스 React 리뉴얼 | 2025-06 ~ 현재 | 기존 Spring MVC + Thymeleaf + Bootstrap 레거시 리포트 백엔드와 React 프런트 공존 설계 | [`2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| 트래블룰 샘플 VASP | 2021-11 ~ 2022-06 | 거래소 연동용 Sample VASP API의 Java Spring WebSocket 샘플 SDK 제공 | [`travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) |

## 주요 기술 포인트

### 1. 애널리틱스 리포트 아키텍처 (장기 소유)

- Spring MVC 컨트롤러-서비스-리포지토리 3계층 구조에서 리포트 도메인을 **ReportInfo → TabInfo → PageInfo → DataSourceInfo → (DimensionItemInfo · MeasureItemInfo)** 계층으로 모델링 (Confluence 35568410)
- 회사별 구현(Admin / Com2us / Other)에 **전략 패턴**을 적용해 공통 분석 기능을 다중 테넌시로 제공
- **MyBatis + JPA 다중 데이터소스** 병용 — 복잡한 집계 쿼리는 MyBatis, CRUD·엔티티 관리는 JPA로 분리

### 2. 인증·권한 (Hive OAuth)

- `HiveConsoleSecurityAuthFilter` 기반 OAuth 액세스/리프레시 토큰 흐름 + JDBC 세션 관리
- 회사/메뉴 권한 정책을 Spring Security 필터 체인과 연동

### 3. 하이브리드 스택 운영 (Spring Boot + FastAPI)

- 전면 재작성 리스크를 피하기 위해 **기존 Spring Boot 리포트 백엔드는 유지**, 신규 데이터 가공 로직만 Python/FastAPI 공통 API로 분리
- Spring 측 `DataSourceInfo`를 확장해 외부 공통 API(FastAPI `/common/processed-data`)를 데이터 소스로 주입하는 **어댑터 설계**
- 결과: 10년된 레거시를 깨지 않고 Airbridge(MMP), BigQuery 등 신규 데이터 경로를 점진 확장

### 4. AG-grid 기반 BI 데이터 전달 계약

- Spring 리포트 API 응답 포맷을 AG-grid가 즉시 렌더링 가능한 `index / columns / data / summary_stats / date_type` 구조로 고정 (공통 API 명세 Confluence 35568348)
- 컬럼 pinning 전략, 타입별 minWidth(date:110 / dim:180 / measure:130) 규약을 백엔드-프런트 공통 계약으로 수립

### 5. 빌드·배포

- **Gradle** 기반 멀티 모듈 빌드
- 2024-08 이후 **Jenkins 멀티 브랜치 파이프라인 + Docker Compose** 배포 표준화(공통 모듈 프로젝트에서 Jenkinsfile을 공통 API와 Java 리포트 배포에 모두 재사용)

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| Spring Boot | proficient | 2016년부터 사용, 애널리틱스 본체 장기 소유, 모바일 리포트·Airbridge API에서 2025년까지 신규 개발 |
| Spring MVC (Controller/Service/Repository) | proficient | 애널리틱스 본체 표준 아키텍처, Confluence 35568410 상세 분석 문서 작성 |
| Spring Security / OAuth Filter | competent | Hive OAuth 인증 필터(`HiveConsoleSecurityAuthFilter`) 운영, 회사/메뉴 권한 정책 연동 |
| MyBatis | proficient | 애널리틱스 리포트 집계 쿼리 다수, 다중 데이터소스 관리 |
| JPA / Hibernate | competent | 엔티티·CRUD 영역, MyBatis와 병용 |
| Thymeleaf | competent | 애널리틱스 본체 서버 렌더링 레이어(레거시) |
| Gradle | proficient | `old-portfolio.md` 명시, 다년간 빌드 툴로 사용 |
| JUnit | competent | `old-portfolio.md` "Unit test tool" 명시 |
| AG-grid (프런트 연계 계약) | proficient | 공통 API 응답 포맷·컬럼 전략을 백엔드와 함께 설계 |
| WebSocket (Java Spring) | novice | 트래블룰 Sample VASP API의 거래소 연동 샘플 수준 |

## 관련 스킬 문서

- [`backend-python.md`](./backend-python.md) — FastAPI/Flask 스택. Java Spring과 하이브리드로 병용한 파트너 스킬
- [`devops-cicd.md`](./devops-cicd.md) — Jenkins 멀티브랜치 파이프라인·Docker Compose 기반으로 Java 서비스를 배포
- [`database.md`](./database.md) — MySQL 8.4, JPA/MyBatis 다중 데이터소스의 영속 계층

## 관련 정량 지표

- **analytics-mobile-report**: 101 / 318 커밋 (~32%, 2025-03 집중 기여) — Java + JavaScript 스택 (`analytics-mobile-report.md`)
- **애널리틱스 본체 장기 소유**: 2017-05 ~ 현재, Spring Boot 리포트 백엔드 지속 유지보수 (`old-portfolio.md`)
- **리포트 아키텍처 문서화**: Confluence 35568410 "애널리틱스 리포트 아키텍처 분석" 본인 작성 (2025-02-27)
- **공통 API 명세 (Java-Python 계약)**: Confluence 35568348 본인 작성, APICode 13종 표준화 (2025-11-18)

## 관련 프로젝트 전체 목록

- [`../20-projects/com2us-platform/2024-08-analytics-common-module.md`](../20-projects/com2us-platform/2024-08-analytics-common-module.md)
- [`../20-projects/com2us-platform/2025-01-airbridge-api.md`](../20-projects/com2us-platform/2025-01-airbridge-api.md)
- [`../20-projects/com2us-platform/2025-06-analytics-react-renewal.md`](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/analytics-mobile-report.md`](../10-sources/com2us-platform/github-c2spf/repos/analytics-mobile-report.md)
- [`../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) (Java Spring WebSocket 샘플)
