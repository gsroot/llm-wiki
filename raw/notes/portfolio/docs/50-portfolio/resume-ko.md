# 김석근 (Seokgeun Kim) — 백엔드/풀스택 개발자

- Email: gsr2732@gmail.com · GitHub [@gsroot](https://github.com/gsroot) · [Blog](https://gsroot.tistory.com) · [LinkedIn](https://www.linkedin.com/in/seokgeun-kim-839473285/)
- **전문 영역**: Python 백엔드 · 게임 데이터 분석(BI) · ML/AI 서비스 · 블록체인 플랫폼

## Summary

- 9년차 백엔드/풀스택 개발자. **애널리틱스 공통 API(c2spf/analytics-common-api) 단독 유지보수(본인 커밋 231/251 ≈ 92%)** 및 **팀 최초 React 리뉴얼 주도**로 프론트엔드 생산성 30~40% 향상 기반을 구축.
- AutoML/LangGraph 기반 ML·AI 서비스를 프로덕션까지 배포한 풀스택 엔지니어. **AI 여행 계획 Android 앱 Google Play 출시(2025-11)**.
- CODE 트래블룰 · NFT 마켓(투표 스마트 컨트랙트 **가스비 ~90% 절감**) · XPLA 플랫폼 등 **블록체인 프로젝트 3건** 주도.
- `analytics-frontend` **476커밋(~24%)** 기여, 공통 API 응답 envelope·APICode 표준화로 프론트-백 계약 고정.

## 핵심 성과 하이라이트

- **팀 최초 React 기반 프론트엔드 아키텍처 도입·표준화** — Vite + React + TypeScript + TanStack + Zustand + ag-grid 스택 정립, "2025 프론트엔드 개발 가이드라인" 문서화. ag-grid 공통 컴포넌트 설계 리드타임 2~3일 → 하루 미만으로 단축.
- **공통 API 단독 유지보수(92% 커밋 점유)** — APIResponse 표준 포맷 + APICode 13종 + BigQuery ProcessedData 결과 코드 4종 정립. Airbridge(MMP) 결합 파이프라인으로 광고 성과 분석을 애널리틱스 UI에서 측정 가능하게 확장.
- **배포·운영 가이드 4종 집중 발행(2024-10)** — Docker Compose + Jenkins 멀티 브랜치 파이프라인 팀 표준화, Promtail/Loki/Grafana 로깅 스택 4개 환경(상용 Primary/Standby·샌드박스·테스트) 분리 운영.
- **ML 유저 예측 평균 정확도 85% 이상 달성** — GCP AutoML + AI Platform Pipeline 기반 MLOps 체계 구축, 예측 결과를 마케팅/리텐션 전략에 활용.
- **LangGraph 기반 AI 여행 계획 앱 Google Play 출시** — 토큰 기반 과금 시스템(1 Clover = 1,000 tokens) + 서버 측 영수증 검증 결제 시스템 구축.

## 경력

### 컴투스플랫폼 (Com2usPlatform) · 2017-05 ~ 현재 · 백엔드/풀스택 개발자

- **애널리틱스 React 리뉴얼** (2025-06 ~ 현재) — 팀 최초 React 기반 아키텍처 설계·구축 주도. `analytics-frontend` 476커밋 기여. 차트·퍼널·리텐션·대시보드 4대 분석 기능 "생성·조회·수정" 구조로 단계적 리뉴얼. [상세](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)
- **Airbridge 데이터 가공 API** (2025-01 ~ 2025-02) — `/common/processed-data` 엔드포인트에 AirbridgeData 모델·피벗팅 로직 추가. Spring Boot 리포트 스택 + FastAPI 공통 API 하이브리드 파이프라인 구축. [상세](../20-projects/com2us-platform/2025-01-airbridge-api.md)
- **애널리틱스 공통 모듈 & 배포 프로세스 개선** (2024-08 ~ 2024-12) — FastAPI 공통 API 신규 설계·구현, HIVE OAuth 통합(8개 엔드포인트), Docker Compose + Jenkins 멀티 브랜치 파이프라인 표준화, Promtail/Loki/Grafana 로깅 스택 구축. [상세](../20-projects/com2us-platform/2024-08-analytics-common-module.md)
- **XPLA 플랫폼** (2024-04 ~ 2024-07) — NestJS + TypeORM 백엔드, React 웹뷰. NFT 민팅 E2E 플로우(Action 조회 → 서명 → 전송 → 결과) 및 중복 민팅·수수료 부족 엣지 케이스 선제 처리. CPBLOC 19건 전수 완료. [상세](../20-projects/com2us-platform/2024-04-xpla-platform.md)
- **NFT 마켓** (2022-05 ~ 2024-03) — NFT 지갑 관리 백엔드(NestJS/TypeORM), Discord 홀더 인증 봇(Discord.py + FastAPI + Pytest), Rust 기반 투표 스마트 컨트랙트 최적화로 **가스비 ~90% 절감**, Docker 배포 개선. GCPNFT 229/231 Done. [상세](../20-projects/com2us-platform/2022-05-nft-market.md)
- **CODE 트래블룰 API** (2021-10 ~ 2022-04) — 가상자산 거래소 트래블룰 공통 API 주도(FastAPI, SQLAlchemy, Pytest, Locust). VerifyVasp 솔루션과의 연동 완료.
- **통합 인증 & 비동기 통신 공통 모듈** (2021-06 ~ 2021-07) — Pub/Sub 로직을 REST API로 모듈화 (Flask).
- **애널리틱스 ML 유저 예측** (2020-08 ~ 2021-09) — AutoML 기반 이탈/구매 예측, 평균 정확도 85% 이상. AI Platform Pipeline 기반 MLOps 체계 구축 (Flask + React/Mobx + GCP AutoML).
- **대용량 데이터 다운로드 REST API / 비동기 워커** (2019-03 ~ 2019-06) — Celery 비동기 워커 기반 자동화 (Flask, Pandas, BigQuery).
- **게임 정보 동기화 스케줄러** (2018-07 ~ 2018-08) — Digdag 워크플로 + BigQuery 동기화.
- **애널리틱스 본체(게임 데이터 분석 BI)** (2017-05 ~ 현재) — 세그먼트 결합, CSV 다운로드, 퍼널·코호트·커스텀 리포트 기능 풀스택 개발 (Spring Boot + jQuery/React).

### 줌인터넷 · 2016-01 ~ 2016-07

- 스윙 브라우저 이어보기 플러그인 백엔드 REST API 설계·개발·문서화 (Java, Spring Boot, MySQL).
- 줌닷컴 포털 사용자 유입 데이터 분석 (HiveQL).

## 기술 스택

- **Backend**: Python (FastAPI, Flask, Django, SQLAlchemy, Alembic, Celery, Pytest) · Java (Spring Boot, Spring MVC, MyBatis, JPA, Gradle) · Node.js (NestJS, TypeORM)
- **Frontend**: React + TypeScript + Vite · TanStack Router/Query · Zustand · Mobx · ag-grid · Highcharts · React Hook Form · Playwright
- **Data/ML**: GCP BigQuery · GCP AutoML (Tables) · GCP AI Platform Pipeline · Pandas · LangGraph · LangChain · OpenAI API · Airflow · Celery · Digdag
- **DevOps**: Docker / Docker Compose · Jenkins (멀티 브랜치 파이프라인) · GitHub Actions · nginx · AWS EC2 · GCP
- **Observability**: Promtail / Loki / Grafana · Fluentd / ElasticSearch / Kibana
- **Data Store**: MySQL · PostgreSQL · MariaDB · Redis · BigQuery
- **Blockchain**: Rust (smart contract) · XPLA (Cosmos SDK 계열) · Web3

## 학력 · 자격

- **인하대학교 컴퓨터공학과** (2007-03 ~ 2014-02) — 교내 프로그래밍 공모전 3위
- **패스트캠퍼스 파이썬 데이터 분석 교육 과정** (2016-03 ~ 2016-05)
- **ADSP (데이터분석 준전문가)** — 한국데이터산업진흥원, 2019-01
- **정보처리기사** — 한국산업인력공단, 2018-11
- **Microsoft Student Partners (MSP)** (2012-07 ~ 2013-06) — Windows 8 APPSTAR Awards 은상, Imagine Cup 데어즈대표상 수상

## 개인 프로젝트

- **트래블메이트 — AI 기반 여행 계획 Android 앱** (2025-10 ~ 2025-11) — LangGraph 에이전트로 여행 일정 생성 자동화, 실시간 AI 스트리밍, 토큰 기반 과금(클로버) + Google Play 인앱 결제. [Google Play](https://play.google.com/store/apps/details?id=com.mate.travel_mate_flutter) 출시. (Flutter, FastAPI, LangGraph, PostgreSQL, uv)
- **Mate Chat — AI 기반 글로벌 소셜 메시징 플랫폼** (2025-08 ~ 현재) — OpenAI GPT 기반 커스텀 AI 챗봇("AI Mates"), WebSocket 실시간 메시징, JWT + OAuth 2.0(Google) 인증. (FastAPI, SQLAlchemy, PostgreSQL, Redis, Flutter/Riverpod)
- **카카오톡 대화 분석 앱** (2023-01 ~ 2023-08) — 감정 분포·대화 빈도·주요 키워드 시각화. 약 1년간 서비스 운영, 약 4,000명 설치. (Flutter, Firebase, FastAPI, Pandas, Plotly)
