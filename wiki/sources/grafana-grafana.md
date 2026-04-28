---
title: "Grafana — 멀티 데이터소스 시각화 + 계층화 AGENTS.md"
type: source
source_type: article
source_url: "https://github.com/grafana/grafana"
raw_path: "raw/articles/grafana-grafana/"
author: "Grafana Labs"
date_published: 2026-04-28
date_ingested: 2026-04-28
tags: [grafana, observability, dashboard, agents-md, hierarchical-agents, 19회차]
related: [[grafana]], [[prometheus]], [[observability-and-cicd-stack]], [[agent-skills]]
confidence: high
---

# Grafana — 멀티 데이터소스 시각화 + 계층화 AGENTS.md

## 한줄 요약

> Grafana는 메트릭/로그/트레이스를 한 화면에서 다루는 통합 시각화 플랫폼이며, 19회차에서 발견된 9단계 AGENTS.md 진화의 핵심 사례 — **계층화 AGENTS.md(루트 + 디렉토리별)** + **`@AGENTS.md` 한 줄짜리 CLAUDE.md(SSOT redirect)** 패턴.

## 핵심 내용

- **6가지 핵심 기능 (README)**: ① Visualizations(panel plugin), ② Dynamic Dashboards(template variable), ③ Explore Metrics(ad-hoc + drilldown), ④ Explore Logs(metric→log 라벨 보존), ⑤ Alerting(시각적 룰 + Slack/PagerDuty/OpsGenie 통합), ⑥ Mixed Data Sources(쿼리당 다른 데이터소스 가능).
- **AGPL-3.0-only 라이선스 (예외 Apache-2.0)**: 16회차 Apache Arrow(Apache-2.0)/Polars(MIT)와 다른 strong copyleft. Enterprise 빌드 태그(`enterprise`, `pro`)는 별도 라이선스.
- **계층화 AGENTS.md (10단계 진화 패턴)**: 루트 `AGENTS.md`가 "디렉토리별 AGENTS.md exists"를 선언 → `docs/AGENTS.md` (문서 스타일), `public/app/features/alerting/unified/AGENTS.md` (Alerting squad 패턴). LLM은 작업 디렉토리에 따라 해당 AGENTS.md 자동 로드.
- **`@AGENTS.md` 한 줄 CLAUDE.md (9단계 진화)**: `raw/articles/grafana-grafana/CLAUDE.md` = 단 1줄 `@AGENTS.md`. AGENTS.md를 SSOT로 두고 CLAUDE.md는 redirect만. CODEOWNERS에서 `/AGENTS.md @grafana/docs-tooling` — 문서 팀이 owner.
- **Backend(Go) + Frontend(TypeScript/React) 모노레포**: Yarn workspaces(프론트) + Go workspaces(백엔드). Wire DI(의존성 주입), CUE 스키마(`kinds/` → Go+TS 자동 생성), Feature toggles(`pkg/services/featuremgmt/`).
- **빌드 태그 3종**: `oss`(default) / `enterprise` / `pro`. SQLite embedded(외부 DB 불필요), `make run`은 hot-reload(air) on `localhost:3000` (admin/admin).
- **PR 분리 강제**: "Frontend(`public/`)와 Backend(`pkg/`)는 atomically deployed되지 않음 — 각각 별도 PR 필수, 다른 cadence". 이건 Sentry AGENTS.md와 동일한 강제 룰.

## 주요 인사이트

- **9단계 진화 — `@AGENTS.md` symlink-style**: 1~8단계의 byte-for-byte 동기화(Pydantic AI/FastMCP)는 "두 파일 sync 필요한 운영 부담". 9단계는 **CLAUDE.md를 1줄로 축소** → AGENTS.md SSOT, fragmentation 제거. Grafana + Sentry 동시 채택 = 운영 진영의 새 표준 가능.
- **10단계 진화 — 계층화 AGENTS.md**: 모노레포에서 영역별로 다른 컨벤션이 필요할 때 → **AGENTS.md를 디렉토리에 분산**. 루트는 "where to look"의 인덱스. CODEOWNERS와 결합하면 영역 책임팀이 자기 AGENTS.md를 직접 관리 가능.
- **프론트/백엔드 PR 분리 룰**: "다른 cadence로 배포되므로 분리". 이건 c2spf-analytics 같은 모노레포 BI 시스템에도 직접 적용 가능 — backend(FastAPI) PR과 frontend(대시보드) PR을 atomically merge하지 말 것.
- **컴투스플랫폼 BI 적용**: Prometheus 메트릭의 1차 소비자. 또한 PostgreSQL/InfluxDB/Loki/Tempo/Jaeger 데이터소스 연결로 게임 데이터 BI 대시보드의 통합 진입점.

## 관련 엔티티/개념

- [[grafana]]: 본 소스 1차 대상.
- [[prometheus]]: 1차 데이터소스, 사실상 표준 페어.
- [[postgresql]]: BI 컨텍스트에서 SQL 데이터소스로 직접 연결.
- [[agent-skills]]: 9~10단계 진화의 핵심 증거.
- [[observability-and-cicd-stack]]: 19회차 시각화 레이어.

## 인용할 만한 구절

> "This file provides guidance to AI agents when working with code in the Grafana repository.
> **Directory-scoped agent files exist for specialized areas — read them when working in those directories:**
> - `docs/AGENTS.md` — Documentation style guide
> - `public/app/features/alerting/unified/AGENTS.md` — Alerting squad patterns"
> — grafana/grafana AGENTS.md 서두 (계층화 패턴 선언)

> "Separate PRs for frontend and backend changes (deployed at different cadences)"
> — AGENTS.md, Principles 섹션

## 메모

- 73K stars(2026-04-28 기준)로 16회차 Apache Kafka(28K) 대비 큰 규모. 스타 수가 운영 진영의 압도적 도달성을 보여줌.
- AGENTS.md 7862 bytes — Prometheus(4859)보다 크고 Sentry(8927)보다 작음. 적절한 균형점.
- `<!-- version: 2.0.0 -->` 주석 — AGENTS.md 자체에 버저닝 도입한 첫 사례. 향후 다른 OSS도 따라할 가능성.
- BI 적용에서 Plugin workspace(`grafana-postgresql-datasource`)는 컴투스 플랫폼 게임 분석 DB 직접 연결에 가장 매력적 — Tableau 대비 OSS + AGPL 강제 운영 조건만 클리어.
