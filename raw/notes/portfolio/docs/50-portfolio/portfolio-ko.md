# 김석근 · 백엔드/풀스택 엔지니어

> 로그를 결정으로 바꾸는 시스템을 만듭니다.

Python 백엔드, 게임 데이터 분석(BI), ML/AI 서비스, 블록체인 플랫폼을 9년간 설계·구축·운영해 왔습니다. 컴투스플랫폼 애널리틱스(BI) 서비스의 공통 API·프론트엔드·배포 파이프라인을 주도하며 팀 최초 React 구조 표준화를 완수했습니다.

- 📧 [gsr2732@gmail.com](mailto:gsr2732@gmail.com)
- 🐙 GitHub — [@gsroot](https://github.com/gsroot)
- 📝 Blog — [gsroot.tistory.com](https://gsroot.tistory.com)
- 🔗 LinkedIn — [Seokgeun Kim](https://www.linkedin.com/in/seokgeun-kim-839473285/)

| 재직 | 컴투스플랫폼(Com2usPlatform) · 2017.05 ~ 현재 |
|------|------------------------------------------------|
| 전문 영역 | Python 백엔드 · 게임 데이터 분석(BI) · ML/AI 서비스 · 블록체인 플랫폼 |
| 관심 방향 | 설계 의도를 기록으로 남기는 시스템 · AI 도구 기반 개발 생산성 · 데이터 파이프라인 정합성 |

---

## Impact — 정량 지표

> 주요 수치의 출처는 모두 상대 경로 링크로 연결됩니다. 숫자는 코드·문서·티켓 증거에 기반합니다.

| 지표 | 값 | 맥락 |
|------|-----|------|
| **개발 경력** | **9년** | 컴투스플랫폼 2017.05 ~ 현재 + 줌인터넷 2016 |
| **c2spf GitHub 기여** | **1,111 커밋** | 본인 기여 커밋 총합 — [c2spf INDEX ↗](../10-sources/com2us-platform/github-c2spf/INDEX.md) |
| **공통 API 단독 유지보수** | **92% ownership** | `analytics-common-api` 231/251 커밋 — [프로젝트 ↗](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| **프론트엔드 생산성** | **30~40% 향상 기반** | 팀 최초 React 구조 표준화 — [프로젝트 ↗](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| **블록체인 플랫폼** | **5개 프로젝트** | CODE 트래블룰 · NFT 마켓 · XPLA 등 · 가스비 **~90% 절감** — [스토리 ↗](../40-stories/problem-solving-gas-fee-optimization.md) |

집계 출처: [GitHub c2spf INDEX](../10-sources/com2us-platform/github-c2spf/INDEX.md) · [Jira INDEX](../10-sources/com2us-platform/jira/INDEX.md) · [Confluence INDEX](../10-sources/com2us-platform/confluence/INDEX.md)

---

## Selected Work — 주요 프로젝트

> 최근 5개 프로젝트. 각 프로젝트의 상세 증거(Jira/Confluence/GitHub/운영 기록)는 링크에서 확인할 수 있습니다.

### 1. 애널리틱스 서비스 React 기반 리뉴얼 · 2025.06 – 현재

| 항목 | 내용 |
|------|------|
| 역할 | 프론트엔드 리드 · 아키텍처 설계 · 풀스택 개발 |
| 스택 | Vite · React · TypeScript · TanStack Query/Router · Zustand · ag-grid · Highcharts · FastAPI · MySQL · BigQuery · Docker · Jenkins |

**성과**
- 팀 최초 **React 기반 프론트엔드 아키텍처** 설계·표준화. Vite + TS + TanStack + Zustand + ag-grid 스택을 팀 표준으로 확정하고 [2025 프론트엔드 개발 가이드라인](../10-sources/com2us-platform/confluence/pages-by-space.md) 문서화.
- `c2spf/analytics-frontend` **476 커밋**(기여율 ~24%), `c2spf/analytics-common-api` **231 커밋**(92%, 거의 단독 유지보수).
- **팀 프론트엔드 생산성 30~40% 향상 기반 구축**. ag-grid 공통 컴포넌트 설계 리드타임 2~3일 → 하루 미만, 반복 개발 시간 50% 이상 절감.
- 차트·퍼널·리텐션·대시보드 4대 분석 기능을 "생성·조회·수정" 구조로 리뉴얼. GCPPDT-741/742 Story MR 머지, 회귀 테스트 **32/32 · 22/22 통과**, 측정값 연산식 에러 **8종 × 5개 로케일 i18n**.
- AI 기반 개발 생산성 향상 가이드 작성(Claude Code / Codex CLI / ChatGPT 실무 시나리오 4종 + 프롬프트 템플릿 4종).

→ [프로젝트 상세](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) · [리더십 스토리](../40-stories/leadership-react-adoption.md)

---

### 2. 애널리틱스 Airbridge 데이터 가공 API 개발 · 2025.01 – 2025.02

| 항목 | 내용 |
|------|------|
| 역할 | 단일 담당자 · 데이터 가공 API 설계·개발·운영 |
| 스택 | Java · Spring Boot · Python · FastAPI · MySQL · Redis · BigQuery · ag-grid · Docker · Jenkins · Promtail · Loki · Grafana |

**성과**
- 기존 애널리틱스에서 확인 불가했던 **광고 성과 지표**(Airbridge MMP)를 지표·퍼널 분석에 주입. 광고주·마케터가 애널리틱스 UI에서 광고 유입·전환·캠페인 성과 측정 가능해짐.
- `/common/processed-data` 단일 엔드포인트에 **BigQuery + Airbridge 결합·피벗팅** 로직 추가. `DataCollection → ProcessedData` 계약이 이후 React 리뉴얼·대시보드 기능까지 재사용됨.
- Spring Boot 리포트 계층(MyBatis + JPA 다중 소스)과 FastAPI 공통 API를 **하이브리드 파이프라인**으로 확장. 에러 코드 이원화(APICode 1001~2007 / ProcessedData result_code)로 프런트 리트라이 정책 분기 가능.
- Promtail → Loki → Grafana로 **3환경 운영 가시성** 확보(상용 Primary/Standby · 샌드박스 · 테스트).

→ [프로젝트 상세](../20-projects/com2us-platform/2025-01-airbridge-api.md)

---

### 3. 애널리틱스 공통 모듈 & 배포 프로세스 개선 · 2024.08 – 현재 (유지보수)

| 항목 | 내용 |
|------|------|
| 역할 | 단일 담당자 · 공통 API/JS 설계·개발, Docker + Jenkins 멀티브랜치 도입, Loki 로깅 스택 구축 |
| 스택 | Python(FastAPI) · Java(Spring Boot) · JavaScript · ag-grid · MySQL · Redis · BigQuery · Docker Compose · Jenkins Multi-branch · Promtail · Loki · Grafana |

**성과**
- `c2spf/analytics-common-api` **231/251 커밋 (92%)** — 거의 단독 유지보수. APIResponse `{result_code, message, data}` 표준화, APICode 13종 + BigQuery 결과 코드 4종 정립.
- **HIVE OAuth 통합**: 토큰·사용자·메뉴 권한·게임 권한 등 **8개 엔드포인트**를 공통 API에 통합. `/hive/auth/games`는 Redis 캐시 기반 최적화, 패턴 매칭 무효화 지원.
- Docker Compose + Jenkins 멀티브랜치 파이프라인으로 브랜치별(상용/스테이징/샌드박스/테스트) 자동 빌드·배포 표준화. **배포/공통 모듈 가이드 4종**을 2024-10~11 집중 발행.
- Promtail/Loki/Grafana로 **4개 환경 로그 중앙 집중화**(상용 Primary/Standby + 샌드박스 + 테스트). SSH 수동 검색 → Grafana 레이블 필터링으로 트러블슈팅 난이도 하락.
- 운영 중 지속 개선: BigQuery Decimal 타입 변환, 피벗 축 NULL 플레이스홀더, OS별 TCP Keepalive, 슬레이브 DB 동기화 이슈 대응.

→ [프로젝트 상세](../20-projects/com2us-platform/2024-08-analytics-common-module.md) · [임팩트 스토리](../40-stories/impact-analytics-common-module.md)

---

### 4. XPLA 플랫폼 개발 · 2024.04 – 2024.07

| 항목 | 내용 |
|------|------|
| 역할 | 시스템 설계 · API 정의 · 풀스택(백엔드 + 웹뷰) · 테스트·리팩토링 주도 |
| 스택 | Node.js · NestJS · TypeORM · TypeScript · React · Docker · MySQL 8 (MASTER-SLAVE) |

**성과**
- 여러 게임이 **SDK를 통해 블록체인 기능**(지갑 연동·NFT 민팅·트랜잭션 서명/전송)을 사용할 수 있는 공통 서비스 플랫폼 구축. 게임 개발팀이 블록체인 구현 복잡도 없이 통합 가능해짐.
- **NFT Mint E2E 플로우** 구현(CPBLOC-821): Action 조회 → 수수료 노출 → tx 생성 → 서명 → 전송 → 결과 페이지까지 단일 UX. 엣지 케이스(중복 token ID · XPLA 잔액 부족) 선제적 처리.
- 클린 코드 리팩토링(CPBLOC-861) + 웹뷰 다국어 기반 구조(URL 언어 코드 en/ko, CPBLOC-862). **CPBLOC 클러스터 19건 전수 Done**.
- 선행 인프라 `GCPHDBA-1245`(2022-07 블록체인 웹 지갑 상용 DB 신청) 위에 SDK 연동 레이어 확장.

→ [프로젝트 상세](../20-projects/com2us-platform/2024-04-xpla-platform.md)

---

### 5. NFT 마켓 (지갑 · Discord 홀더 인증 · 투표 컨트랙트) · 2022.05 – 2024.03

| 항목 | 내용 |
|------|------|
| 역할 | 지갑 백엔드 · Discord 봇 · 스마트 컨트랙트 · 배포 개선 |
| 스택 | Node.js · NestJS · TypeORM · Python(Discord.py · FastAPI · Pytest) · Rust · TypeScript · MySQL · Redis · Docker · Fluentd · ElasticSearch · Kibana |

**성과**
- **투표 스마트 컨트랙트 가스비 ~90% 절감** — 저장 구조·이벤트 설계 최적화로 사용자 비용 대폭 감소.
- NFT **홀더 인증 단기 상용화**: Discord 봇(Python Discord.py + FastAPI, Pytest 회귀) 기반 역할(Role) 자동 부여.
- NestJS/TypeORM 지갑 도메인 모델링 + Redis 캐시 + Fluentd → ES → Kibana 관측 파이프라인 구축.
- Epic 3건(**GCPNFT-1401** 디스코드 유지보수 · **GCPNFT-1248** C2XNFT 회계 데이터 · **GCPNFT-1971** 통합 로그인) 소유 운영. **GCPNFT 231건 중 229건 Done**.
- 컨테이너 배포 프로세스 표준화 — 이후 XPLA 플랫폼(2024-04)으로 지갑·민팅 경험 계승.

→ [프로젝트 상세](../20-projects/com2us-platform/2022-05-nft-market.md) · [문제 해결 스토리](../40-stories/problem-solving-gas-fee-optimization.md)

---

## Experience — 경력 타임라인

### 컴투스플랫폼 · 2017.05 ~ 현재 (9년)

**주요 도메인**: 게임 데이터 분석(BI) · ML/AI · 블록체인 플랫폼 · 인증·공통 인프라

| 기간 | 프로젝트 | 링크 |
|------|----------|------|
| 2025.06 ~ 현재 | 애널리틱스 React 기반 리뉴얼 | [↗](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| 2025.01 ~ 2025.02 | Airbridge 데이터 가공 API | [↗](../20-projects/com2us-platform/2025-01-airbridge-api.md) |
| 2024.08 ~ 현재 | 애널리틱스 공통 모듈 & 배포 개선 (유지보수 지속) | [↗](../20-projects/com2us-platform/2024-08-analytics-common-module.md) |
| 2024.04 ~ 2024.07 | XPLA 플랫폼 | [↗](../20-projects/com2us-platform/2024-04-xpla-platform.md) |
| 2022.05 ~ 2024.03 | NFT 마켓 (GCPNFT Epic 3건 소유) | [↗](../20-projects/com2us-platform/2022-05-nft-market.md) |
| 2021.10 ~ 2022.04 | CODE 트래블룰 API (가상자산 규제 대응) | [↗](../20-projects/com2us-platform/README.md) |
| 2021.06 ~ 2021.07 | 통합 인증 & 비동기 통신 공통 모듈 | [↗](../20-projects/com2us-platform/README.md) |
| 2020.08 ~ 2021.09 | 애널리틱스 ML 유저 예측 (AutoML + MLOps) | [↗](../40-stories/learning-automl-mlops.md) |
| 2019.03 ~ 2019.06 | 대용량 데이터 다운로드 REST API · 비동기 워커 | [↗](../20-projects/com2us-platform/README.md) |
| 2018.07 ~ 2018.08 | 게임 정보 동기화 스케줄러 | [↗](../20-projects/com2us-platform/README.md) |
| 2017.05 ~ 현재 | 애널리틱스 본체 (장기 진행 · 게임 데이터 BI) | [↗](../20-projects/com2us-platform/README.md) |

### 줌인터넷 · 2016.01 ~ 2016.07

- **줌닷컴 사용자 데이터 분석**(2016.02~06): HiveQL 기반 유입/리텐션 분석. 메인 페이지 이탈 패턴을 발견해 리텐션 전략 수립에 기여.
- **스윙 브라우저 이어보기 플러그인**(2016.01~07): Java + Spring Boot 백엔드 REST API 설계·개발·문서화.

---

## Skills — 기술 스택

> 카테고리별 대표 스킬과 문서 링크. 각 스킬 문서는 이를 증명하는 프로젝트로 역매핑됩니다.

### Backend
- **Python** (9년) — FastAPI, Django, Flask, Pytest, Celery, SQLAlchemy, Pandas → [스킬 문서](../30-skills/backend-python.md)
- **Java / Spring Boot** (10년) — Spring MVC, JPA, MyBatis, JUnit, Gradle → [스킬 문서](../30-skills/backend-java-spring.md)
- **Node.js / NestJS / TypeORM** — XPLA 플랫폼·NFT 마켓 기반
- **공통 API 설계** — APIResponse envelope 표준화, 에러 코드 이원화, OAuth 토큰 흐름 통합

### Frontend
- **React / TypeScript / Vite / TanStack** — 팀 최초 React 아키텍처 도입 리드 → [스킬 문서](../30-skills/frontend-react.md)
- **ag-grid / Highcharts / Plotly** — 대용량 BI 테이블·차트 공통 컴포넌트 설계
- **상태 관리**: Zustand, React Hook Form, TanStack Query

### Data & ML
- **데이터 파이프라인**: BigQuery, Airbridge(MMP), Digdag, Airflow, Celery → [스킬 문서](../30-skills/data-pipeline.md)
- **ML/AI**: GCP AutoML Tables, AI Platform Pipeline, BigQuery ML, Jupyter → [스킬 문서](../30-skills/ml-ai.md) · [스토리](../40-stories/learning-automl-mlops.md)
- **LLM/Agent**: LangGraph, LangChain, OpenAI API, MCP, Claude Code / Codex CLI 실무 프로세스 정착

### DevOps
- **컨테이너/CI·CD**: Docker, Docker Compose, Jenkins Multi-branch Pipeline, GitHub Actions → [스킬 문서](../30-skills/devops-cicd.md)
- **관측/로깅**: Promtail · Loki · Grafana (4환경 분리 구축), ElasticSearch · Kibana
- **인프라**: nginx, AWS EC2, GCP (BigQuery / AI Platform / Storage / AutoML), CentOS / Ubuntu
- **메시지 브로커**: Kafka, Redis, RabbitMQ, NATS

### Database
- **RDBMS**: MySQL 8 (MASTER-SLAVE), PostgreSQL, MariaDB → [스킬 문서](../30-skills/database.md)
- **Cache/NoSQL**: Redis (패턴 매칭 무효화, OAuth 세션 캐시)
- **Data Warehouse**: GCP BigQuery (피벗팅·Decimal 타입 변환·MINUTE 단위 검증)

### Blockchain / Web3
- XPLA 체인(SDK 연동 플랫폼), NFT 민팅/지갑, Rust 기반 스마트 컨트랙트, Discord 커뮤니티 인증 → [스킬 문서](../30-skills/blockchain.md)

---

## About

오늘보다 더 나은 내일을 꿈꾸며 꾸준히 성장하는 개발자입니다. Python 기반 백엔드 서비스와 데이터 파이프라인 설계·개발을 축으로, ML 서비스의 설계부터 프로덕션 배포까지 직접 경험했고, 데이터 분석 서비스(BI)를 기획·설계·운영 전반에서 주도해 왔습니다.

현상의 원인을 파악하고 분석하는 것을 즐깁니다. 공통 API 응답 계약(`{result_code, message, data}`)과 에러 코드 이원화, 프론트-백 간 `DataCollection → ProcessedData` 규약처럼 **설계 의도를 문서로 남기는 작업**을 선호합니다. 동시에 테스트 코드의 중요성을 이해하고 실무에서 활용(Pytest 회귀, 32/32·22/22 MR 테스트 통과 등)하려고 노력합니다.

개발하는 서비스의 비즈니스 목표와 가치를 명확히 이해하는 것을 중요하게 여깁니다. Airbridge 데이터 가공 API는 단순한 ETL이 아니라 "광고주·마케터가 애널리틱스 UI 내에서 광고 성과를 측정할 수 있게 만드는 것"이 목적이었고, React 리뉴얼은 "팀 전체 프론트엔드 생산성 30~40% 향상 기반 구축"을 결과로 설정했습니다. 최근에는 Claude Code / Codex CLI / ChatGPT 같은 AI 도구를 설계 초안·리팩토링·리뷰에 체계적으로 활용하는 워크플로우를 팀에 전파하고 있습니다.

사이드 프로젝트를 통해 새로운 기술을 접하고 활용하는 것을 즐기며, 간결하면서 읽기 쉬운 코드와 일관된 아키텍처를 지향합니다.

### 학력 · 자격

- **인하대학교 컴퓨터공학과** · 2007.03 ~ 2014.02 (교내 프로그래밍 공모전 3위)
- **ADSP** (데이터 분석 준전문가) · 한국데이터산업진흥원 · 2019.01.09
- **정보처리기사** · 한국산업인력공단 · 2018.11.20
- **컴퓨터활용능력 1급** · 대한상공회의소 · 2011.01.28
- **패스트캠퍼스 파이썬 데이터 분석 교육 과정** · 2016.03~05
- **Microsoft Student Partners(MSP)** · 2012.07 ~ 2013.06 — Windows 8 APPSTAR Awards 은상, Imagine Cup 데어즈대표상 수상

### 개인 프로젝트

- **Travel Mate** — AI 여행 계획 Android 앱 · Flutter + FastAPI + LangGraph + OpenAI API · 2025.10 – 2025.11. 토큰 기반 과금 시스템(1 Clover = 1,000 tokens), Google Play 인앱 결제 + 서버 측 영수증 검증. [Google Play 출시 ↗](https://play.google.com/store/apps/details?id=com.mate.travel_mate_flutter)
- **Mate Chat** — AI 기반 글로벌 소셜 메시징 플랫폼 · Python(FastAPI, SQLAlchemy) + PostgreSQL + Redis + OpenAI GPT + Flutter(Riverpod) · 2025.08 ~ 현재. WebSocket 실시간 메시징, OAuth 2.0 + JWT 인증, 가상 화폐 "클로버" 기반 AI 사용량 트래킹.
- **카카오톡 대화 분석 앱** — Flutter + Firebase + FastAPI + Pandas + Plotly · 2023.01 – 2023.08. **약 4,000명 설치** 달성(Google Play).

---

## Key Stories

> 4개의 재사용 가능한 서사 단위. 각각 Situation/Task/Action/Result 구조로 정리되어 있습니다.

1. **리더십 — 팀 최초 React 구조 설계·도입** · Spring MVC + jQuery 레거시를 Vite + React + TypeScript + TanStack + Zustand + ag-grid 스택으로 전환. analytics-frontend 476 커밋, 팀 생산성 30~40% 향상 기반. → [상세](../40-stories/leadership-react-adoption.md)
2. **임팩트 — 공통 모듈화 + 배포 표준화** · analytics-common-api 92% 단독 유지보수, Docker Compose + Jenkins 멀티브랜치 + Loki 4환경 로깅 스택 구축. 배포 가이드 4종 집중 발행. → [상세](../40-stories/impact-analytics-common-module.md)
3. **문제 해결 — NFT 투표 컨트랙트 가스비 ~90% 절감** · Rust 스마트 컨트랙트 저장 구조·이벤트 설계 최적화로 사용자 비용 대폭 감소. → [상세](../40-stories/problem-solving-gas-fee-optimization.md)
4. **학습 — AutoML 기반 MLOps 시스템을 처음부터 구축** · GCP AutoML Tables + AI Platform Pipeline + BigQuery 기반 유저 이탈/구매 예측. 평균 예측 정확도 85%+, 예측 유저 추세와 리텐션의 반비례 관계 입증. → [상세](../40-stories/learning-automl-mlops.md)

---

## Contact

> Let's build something meaningful.

- 📧 [gsr2732@gmail.com](mailto:gsr2732@gmail.com)
- 🐙 GitHub — [@gsroot](https://github.com/gsroot)
- 📝 Blog — [gsroot.tistory.com](https://gsroot.tistory.com)
- 🔗 LinkedIn — [Seokgeun Kim](https://www.linkedin.com/in/seokgeun-kim-839473285/)

---

*Last updated: 2026-04-24 · 이 문서는 웹 포트폴리오와 동일한 정보 구조(IA)를 따릅니다. 영문 버전은 [`portfolio-en.md`](./portfolio-en.md).*
