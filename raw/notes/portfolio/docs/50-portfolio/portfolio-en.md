# Seokgeun Kim · Backend / Full-stack Engineer

> I build systems that turn logs into decisions.

- 📧 gsr2732@gmail.com · [GitHub](https://github.com/gsroot) · [Blog](https://gsroot.tistory.com) · [LinkedIn](https://www.linkedin.com/in/seokgeun-kim-839473285/)
- **Focus**: Python backend · Game data analytics (BI) · ML/AI services · Blockchain platforms
- **Current**: Com2usPlatform · May 2017 — Present
- **Based in**: Seoul, Korea

---

## Impact — Quantitative Metrics

> A snapshot of measurable outcomes from nine years of engineering.

| Metric | Value | Context |
|--------|-------|---------|
| **9 years** | Engineering career | Com2usPlatform (2017.05–present) + Zum Internet (2016) |
| **1,111 commits** | Across 6 c2spf repositories | My contributions in the `c2spf` GitHub organization |
| **92% ownership** | `analytics-common-api` | 231/251 commits — effectively sole maintainer |
| **~90% gas-fee reduction** | On-chain voting smart contract | Rust / XPLA (Cosmos SDK) storage and event redesign |

> Additional evidence: 476 commits in `c2spf/analytics-frontend` (team's first React migration) · 85%+ accuracy in ML churn/purchase prediction · 30–40% frontend productivity uplift foundation.

---

## Selected Work — Projects

> Latest five projects. Each title shows period · role · key stack. Detailed evidence (Jira / Confluence / GitHub) lives in the linked project docs.

### Analytics Service React Renewal · Jun 2025 – Present

**Role** Frontend lead · architecture design · full-stack
**Stack** Vite · React · TypeScript · TanStack Query/Router · Zustand · ag-grid · Highcharts · React Hook Form · Playwright · FastAPI · Docker · Jenkins

**Context** Ended 8+ years of Spring MVC + Thymeleaf + jQuery legacy UI on the company's internal game BI platform.

**Outcomes**
- Led the **team's first React-based frontend architecture** and stack standardization
- Rebuilt four core analytics features (Chart / Funnel / Retention / Dashboard) into a "create · read · update" structure
- Built ag-grid common components with type-based pinning and minWidth strategies
- Authored **two team-wide standards** on Confluence: *2025 Frontend Development Guidelines* and *AI-Assisted Productivity Guide* (Claude Code / Codex CLI / ChatGPT scenarios)
- Foundation for **30–40% frontend productivity uplift**; ag-grid common-component design lead time **2–3 days → <1 day**; 50%+ repetitive-dev-time reduction
- **476 commits** to `c2spf/analytics-frontend` (~24% of repo); regression tests 32/32 and 22/22 passing for the two Story-level merges

→ [Detailed doc](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md)

---

### Airbridge Data Processing API · Jan 2025 – Feb 2025

**Role** Sole owner · design + implementation
**Stack** Python (FastAPI) · Java (Spring Boot) · MySQL · Redis · GCP BigQuery · ag-grid · Docker · Jenkins · Promtail / Loki / Grafana

**Context** Added an external-ad-performance data path (Airbridge MMP) to Analytics so advertisers and marketers could measure campaigns inside the existing BI UI for the first time.

**Outcomes**
- Designed the single `/common/processed-data` endpoint — accepts `MetricData | AirbridgeData`, returns a pivoted `ProcessedData` payload (index, columns, data, summary_stats, date_type) directly consumable by ag-grid
- Kept the hybrid stack deliberately: Spring Boot report layer preserved; new data-shaping logic added in the FastAPI common API to avoid rewrite risk
- Built observability (Promtail → Loki → Grafana) across **prod / staging / sandbox / test** environments
- The `DataCollection → ProcessedData` contract became the **reusable baseline** for the 2025-06 React renewal and dashboard improvements

→ [Detailed doc](../20-projects/com2us-platform/2025-01-airbridge-api.md)

---

### Analytics Common Module & Deployment Improvement · Aug 2024 – Present (maintenance)

**Role** Sole owner · platform work
**Stack** Python (FastAPI) · Java (Spring Boot) · JavaScript · MySQL · Redis · GCP BigQuery · ag-grid · Jenkins · Docker · Promtail / Loki / Grafana

**Context** Duplicated visualization / auth / BigQuery-query logic across multiple reports made changes expensive and inconsistent.

**Outcomes**
- Extracted common logic into the `analytics-common-api` FastAPI server and a shared JavaScript module
- Defined the `APIResponse` envelope and a **13-code `APICode`** taxonomy for consistent error contracts
- Standardized deployment: Docker Compose + Jenkins multi-branch pipeline automating build/release across prod / staging / sandbox / test
- Central logging: **4 Loki instances per environment** (prod primary/standby + sandbox + test), replacing SSH-driven log hunting
- Published **4 deployment/operations guides** in a 2024-10 to 2024-11 sprint (Common API spec, shared JS usage, Docker Compose, Jenkins multi-branch)
- **92% ownership** (231/251 commits) — effectively sole maintainer; ongoing work includes BigQuery Decimal conversion, pivot-axis NULL placeholders, `date_type=MINUTE` validation, TCP keepalive tuning, slave-sync mitigations

→ [Detailed doc](../20-projects/com2us-platform/2024-08-analytics-common-module.md)

---

### XPLA Platform · Apr 2024 – Jul 2024

**Role** System designer · full-stack · sole developer
**Stack** Node.js · NestJS · TypeORM · React (embedded web-view) · Docker · MySQL (master–slave)

**Context** Multiple games needed a shared blockchain-feature platform (wallet, NFT minting, tx signing/broadcast) so they could integrate XPLA without re-implementing chain details.

**Outcomes**
- Designed and built an SDK-based blockchain-feature platform covering the full NFT Mint E2E flow: action lookup → fee display → tx creation → signing → broadcast → result page
- Edge-case guards: duplicate-mint prevention, insufficient-balance gating
- i18n groundwork set (URL language code, en/ko-ready)
- **Completed on schedule**; 19/19 tickets closed across the CPBLOC cluster

→ [Detailed doc](../20-projects/com2us-platform/2024-04-xpla-platform.md)

---

### NFT Marketplace · May 2022 – Mar 2024

**Role** Backend · smart contract · DevOps · Epic owner (3 Epics)
**Stack** Node.js (NestJS, TypeORM) · Python (Discord.py, FastAPI, Pytest) · Rust · TypeScript · MySQL · Redis · Docker · Fluentd / ElasticSearch / Kibana

**Context** NFT-wallet management for the C2X/XPLA ecosystem: wallet backend, Discord holder-verification bot, on-chain voting smart contract.

**Outcomes**
- **~90% gas-fee reduction** on the on-chain voting smart contract (Rust, XPLA / Cosmos SDK) via storage-layout and event-emission redesign
- Discord holder-verification bot productionized in a short window — demonstrated a reusable pattern for multi-method verification
- Container-based deployment standardization (Docker); logging via Fluentd → ElasticSearch → Kibana
- Owner of 3 Epics (C2XNFT accounting, Discord maintenance, integrated SSO); **229/231 tickets Done** on the GCPNFT project as of 2025-08

→ [Detailed doc](../20-projects/com2us-platform/2022-05-nft-market.md)

---

### Earlier highlights (summarized)

- **CODE Travel Rule API** (Oct 2021 – Apr 2022): FATF travel-rule common API for virtual-asset exchanges · Python (FastAPI, SQLAlchemy, Pytest, Locust) · MariaDB · NATS. Delivered the web + blockchain API versions and integrated with VerifyVasp despite scope changes and a tight schedule.
- **Unified Auth & Async Messaging Common Module** (Jun – Jul 2021): consolidated per-project auth and refactored async messaging into a pub/sub REST module (Flask + SQLAlchemy + Pytest), enabling MSA reuse.
- **Analytics ML User Prediction** (Aug 2020 – Sep 2021): AutoML-based churn/purchase prediction, **85%+ average accuracy**; built the team's MLOps foundation on GCP AutoML Tables + BigQuery ML + AI Platform Pipeline.
- **Large-volume Data Download REST API & Async Worker** (Mar – Jun 2019): Flask + Celery + Pandas, BigQuery + GCS; replaced a manual request process with user-initiated async downloads.
- **Game Info Sync Scheduler** (Jul – Aug 2018): Digdag + Python ETL to sync AppCenter game metadata into MySQL and BigQuery.
- **Analytics core development** (May 2017 – Present, long-running): segment joins, CSV export, funnel analysis, cohort analysis, and custom reports as a full-stack engineer (Spring Boot + jQuery/React/Redux + BigQuery + GCS).

---

## Experience — Timeline

> Two companies. Breadth of domains: BI, ML, blockchain, frontend architecture.

### Com2usPlatform · May 2017 — Present

**Role** Backend / Full-stack Engineer — Analytics / Blockchain / ML

The Analytics product is the company's internal BI platform for game-log data — used by live-ops, marketing, and game teams across the Com2us group. I've been the core full-stack engineer since its inception in 2017.

- 9 years of continuous ownership across one platform — from Spring MVC monolith to FastAPI + React modern stack
- Scope has grown from BI features to ML services (AutoML-based prediction), blockchain platforms (NFT marketplace, XPLA SDK, CODE Travel Rule), and architectural leadership (2025 React migration)
- 1,111 commits across 6 c2spf repositories; owner / lead on multiple Epics

### Zum Internet · Jan 2016 — Jul 2016

**Role** Data / Backend Engineer (intern-to-junior)

- User-behavior analysis of the zum.com portal via **HiveQL** — identified the main-page bounce pattern and informed retention strategy
- Swing Browser "Watch Later" plugin — designed and documented Spring Boot REST APIs powering the feature

---

## Skills — Five Categories

> Grouped by primary domain. Each bullet links to its full skill doc.

### Backend
- **Python** (~9y): FastAPI · Django · Flask · SQLAlchemy · Pytest · Celery · uv → [skill doc](../30-skills/backend-python.md)
- **Java / Spring Boot** (~10y, including Com2usPlatform legacy ownership): Spring Boot · MyBatis / JPA · JUnit → [skill doc](../30-skills/backend-java-spring.md)
- **Node.js / NestJS**: TypeORM · NestJS (XPLA, NFT marketplace)

### Frontend
- **React + TypeScript**: Vite · TanStack Query/Router · Zustand · ag-grid · Highcharts · React Hook Form · Playwright → [skill doc](../30-skills/frontend-react.md)
- **Mobile**: Flutter · Riverpod · GoRouter · Dio (Travel Mate, Mate Chat)

### Data & ML
- **Data Pipeline**: BigQuery · Airflow · Digdag · Celery · Pandas · NumPy → [skill doc](../30-skills/data-pipeline.md)
- **ML / AI**: GCP AutoML Tables · BigQuery ML · AI Platform Pipeline · LangGraph · LangChain · OpenAI API · MCP · scikit-learn · Jupyter → [skill doc](../30-skills/ml-ai.md)

### DevOps
- Docker · Docker Compose · Jenkins (multi-branch pipelines) · GitHub Actions · Nginx
- Observability: Promtail / Loki / Grafana · Fluentd / ElasticSearch / Kibana
- Cloud: GCP (BigQuery, AI Platform, Storage, AutoML) · AWS EC2 → [skill doc](../30-skills/devops-cicd.md)

### Database & Blockchain
- **Database**: MySQL (master–slave) · PostgreSQL · MariaDB · Redis (Sentinel HA) → [skill doc](../30-skills/database.md)
- **Blockchain**: Rust (XPLA / Cosmos SDK smart contracts) · TypeScript wallet/NFT services · FATF Travel Rule → [skill doc](../30-skills/blockchain.md)

---

## About

I'm a Python-first backend engineer who has spent the last nine years turning raw game logs into decisions that product, live-ops, and marketing teams can act on. The work started as the core full-stack engineer on Com2usPlatform's Analytics BI — and grew from there, domain by domain, into ML prediction services, on-chain smart contracts, and a team-wide frontend modernization.

My style is pragmatic ownership: take an area nobody else owns, reduce it to a clean contract, and make it boring to operate. That's how a scattered set of Spring reports became the `analytics-common-api` (~92% of its commits are mine), and how eight years of jQuery UI became the team's first React architecture in 2025 — with documented standards and measurable productivity gains instead of a one-off rewrite.

Outside of work, I ship. Travel Mate (an AI travel-planning Android app built with Flutter + FastAPI + LangGraph) launched on Google Play in November 2025; Mate Chat (global AI-based social messaging) is in active development. I treat side projects as a forcing function for learning — LLM agents, OAuth 2.0, in-app purchase, WebSocket real-time — so that the next work project benefits from skills I've already debugged on my own time.

I care about small files, clear contracts, and honest metrics. I write tests because I like being able to sleep. I believe interfaces should hide complexity rather than redistribute it.

### Education & Certifications
- **Inha University** — B.S. in Computer Engineering (Mar 2007 – Feb 2014)
- **ADSP** (Advanced Data Analytics Semi-Professional) — Korea Data Industry Agency, 2019
- **Engineer Information Processing** — HRD Korea, 2018
- **Microsoft Student Partners (MSP)** 2012–2013 — Windows 8 APPSTAR Silver; Imagine Cup (Dare-the-Future) Award

### Personal Projects
- **Travel Mate** — AI travel-planning Android app · Flutter + FastAPI + LangGraph + OpenAI API · [Launched on Google Play (Nov 2025)](https://play.google.com/store/apps/details?id=com.mate.travel_mate_flutter) · in-app purchase with 1 Clover = 1,000 tokens metering
- **Mate Chat** — AI-based global social messaging (Aug 2025 – Present) · FastAPI + WebSocket + PostgreSQL + Redis + OAuth 2.0 + OpenAI GPT · customizable "AI Mates", follow/friend graph, virtual currency
- **KakaoTalk Conversation Analyzer** (Jan – Aug 2023) — Flutter + Firebase + FastAPI + Pandas + Plotly · ~4,000 Google Play installs over ~1 year of operation

---

## Contact

> Let's build something meaningful.

- 📧 [gsr2732@gmail.com](mailto:gsr2732@gmail.com)
- 🐙 GitHub — [@gsroot](https://github.com/gsroot)
- 📝 Blog — [gsroot.tistory.com](https://gsroot.tistory.com)
- 🔗 LinkedIn — [Seokgeun Kim](https://www.linkedin.com/in/seokgeun-kim-839473285/)

---

## Key Stories

Four signature moments with full STAR write-ups.

- **Impact — Analytics Common Module**: consolidated duplicated reports into `analytics-common-api` (92% commits), standardizing response contracts and 4-env deployment. → [story](../40-stories/impact-analytics-common-module.md)
- **Leadership — React adoption**: led the team's first React architecture migration, authored two Confluence-wide standards, built the foundation for 30–40% productivity uplift. → [story](../40-stories/leadership-react-adoption.md)
- **Problem Solving — Gas-fee optimization**: redesigned a voting smart contract's storage and event emission for ~90% gas savings (Rust / XPLA / Cosmos SDK). → [story](../40-stories/problem-solving-gas-fee-optimization.md)
- **Learning — AutoML & MLOps**: self-taught GCP AutoML + AI Platform Pipeline end-to-end, reached 85%+ prediction accuracy, and established the team's MLOps foundation. → [story](../40-stories/learning-automl-mlops.md)

---

*Last updated: 2026-04-24 · This document mirrors the information architecture of the [web portfolio](../../web/).*
