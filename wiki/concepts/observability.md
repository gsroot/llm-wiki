---
title: Observability — 메트릭/로그/트레이스 + 에러 + 사용자 경험
aliases:
- Observability
- 관측성
- 옵저버빌리티
type: concept
category: dev-tools
tags:
- observability
- monitoring
- error-tracking
- prometheus
- grafana
- sentry
related:
- '[[prometheus]]'
- '[[grafana]]'
- '[[sentry]]'
- '[[devops-cicd]]'
- '[[observability-and-cicd-stack]]'
- '[[github-actions]]'
- '[[docker]]'
- '[[prometheus-prometheus]]'
- '[[grafana-grafana]]'
- '[[getsentry-sentry]]'
source_count: 3
observed_source_refs: 3
inbound_count: 10
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 6
---

# Observability — 메트릭/로그/트레이스 + 에러 + 사용자 경험

## 정의

**Observability(관측 가능성)** = 시스템 외부 출력(로그, 메트릭, 트레이스)만 보고 내부 상태를 추론할 수 있는 능력. 모니터링이 "알려진 문제를 감지"라면, observability는 "알려지지 않은 문제도 추론"이다. 5축 데이터(metrics/logs/traces/errors/RUM)를 OSS 도구 5개([[prometheus]] / [[grafana]] / [[sentry]] / OpenTelemetry / Loki)로 매핑한다.

## 왜 중요한가

석근 입장에서:

1. **컴투스플랫폼 BI 운영**: 데이터 파이프라인 장애 시 SSH 수동 검색에서 [[grafana]] 라벨 필터링으로 전환하여 트러블슈팅 시간 단축. 4환경(상용/스테이징/샌드박스/테스트) 분리 운영의 핵심 도구.
2. **사이드 프로젝트 적용**: FastAPI + Postgres 스택의 운영 가시성을 [[prometheus]] + [[grafana]] + [[sentry]] 3단 OSS로 무료/저비용 확보 가능.
3. **AGENTS.md 표준 진화의 직접 증거**: Prometheus/Grafana/Sentry 3개 OSS가 동시에 AGENTS.md 채택 — 운영 진영의 새 표준 형성. [[agent-skills]] 진화 8~10단계의 핵심 실증 데이터.

## 5축 관측 데이터

| 축 | 정의 | 1차 OSS | 데이터 모델 |
| --- | --- | --- | --- |
| **Metrics** | 시간에 따른 수치 (QPS, latency, error rate) | [[prometheus]] | 시계열 (timestamp + value + labels) |
| **Logs** | 이벤트 텍스트 스트림 | Loki / ELK / Fluentd | 구조화/비구조화 텍스트 + labels |
| **Traces** | 분산 시스템 요청 흐름 | Jaeger / Tempo / OpenTelemetry | Span 트리 + correlation ID |
| **Errors** | 예외/실패 이벤트 + 컨텍스트 | [[sentry]] | Stack trace + breadcrumb + user/release |
| **RUM (Real User Monitoring)** | 클라이언트 측 사용자 경험 | Sentry RUM / Datadog RUM | Page load, interaction, session replay |

## 3 Pillars + 2 (확장 모델)

전통적 3 pillars(Metrics/Logs/Traces)에 **Errors**(Sentry 진영 강조)와 **RUM/Session**(프론트엔드 강조) 2축을 추가한 5축 모델.

```
[Backend]              [Frontend]
   │                       │
   ├── Metrics  ──→ Prom + Grafana
   ├── Logs    ──→ Loki + Grafana
   ├── Traces  ──→ Jaeger / Tempo
   ├── Errors  ──→ Sentry  ←── Errors (Frontend)
   │                          ←── RUM/Session (Frontend)
   │                          ←── Replay (Frontend)
   ↓
   추론: 무엇이 깨졌나? 누구에게 영향? 언제부터?
```

## OpenTelemetry — 통합 표준

**OpenTelemetry(OTel)** = CNCF 프로젝트로 metrics/logs/traces 수집의 vendor-neutral 표준. SDK + Collector + Protocol(OTLP)로 분리. 대부분의 backend(Prometheus/Loki/Tempo/Jaeger/Sentry)가 OTLP 입력 지원.

→ [[prometheus]]가 OTel 호환 receiver로 보강되는 추세 (Prometheus 3.0+).

## 발견 — AGENTS.md와 Observability의 동시 진화

5개 OSS 중 [[prometheus]] / [[grafana]] / [[sentry]] 3개가 AGENTS.md 채택, [[docker]] / [[github-actions]] 2개는 미채택. 이 양극화는 **"애플리케이션 코드에 가까운 운영 OSS는 AI agent 가이드를 적극 채택, 인프라 코어 OSS는 신중"** 패턴을 시사.

| OSS | AGENTS.md | 형식 |
| --- | --- | --- |
| Prometheus | ✅ | PR 패턴 가이드 (148줄) |
| Grafana | ✅ | 계층화 + redirect (161줄, v2.0.0) |
| Sentry | ✅ | Anti-fragmentation SSOT (256줄) |
| Docker/Moby | ❌ | CONTRIBUTING.md만 |
| GitHub Actions | ❌ | 분산형 OSS, docs SSOT |

→ 자세한 비교: [[observability-and-cicd-stack]] § "AGENTS.md 양극화 분석".

## 실전 적용

- **컴투스플랫폼 BI**: 데이터 파이프라인 장애 발생 시 Grafana → Prometheus → Logs 순서로 drill-down. Sentry는 BI 대시보드 자체의 프론트엔드 에러 추적 (panel render failure, query timeout).
- **사이드 프로젝트**: FastAPI에 `prometheus-fastapi-instrumentator` + `sentry-sdk` 추가, Grafana Cloud 무료 티어로 시각화. 30분 만에 5축 중 3축(metrics/errors/logs) 확보 가능.
- **4환경 분리**: 상용 Primary/Standby + 샌드박스 + 테스트 — 라벨(`env=prod-primary` 등)로 분리하면 단일 Grafana 인스턴스로 모두 관측 가능.

## 관련 개념

- [[devops-cicd]]: 운영 자동화의 자매 개념. CI/CD가 "변경 자동화"라면 observability는 "운영 자동화의 시각".
- [[agent-skills]]: 발견 — 운영 OSS의 AGENTS.md 채택 패턴.
- [[backend-python-fastapi]]: 메트릭/로그/에러를 emit하는 1차 후보.
- [[data-pipeline-bigquery]]: 파이프라인 자체의 관측 — Promtail → Loki → Grafana.

## 출처

- [[prometheus-prometheus]] — 메트릭 레이어 1차 소스
- [[grafana-grafana]] — 시각화 레이어 1차 소스
- [[getsentry-sentry]] — 에러/RUM 레이어 1차 소스

## 열린 질문

- OpenTelemetry로 통합 시 Prometheus 직접 수집(pull) vs OTel Collector 경유(push) 중 BI 시나리오는 어느 쪽이 적합한가?
- AGPL-3.0 (Grafana) 라이선스가 사이드 프로젝트 SaaS화에 미치는 영향 — Grafana Cloud 사용 vs self-hosted vs alternative(Metabase)?
- 5축 중 RUM은 프론트엔드 한정 → BI 대시보드(Grafana) 자체에 RUM을 붙이는 게 가능한가? Sentry SDK 가능성 검토.
