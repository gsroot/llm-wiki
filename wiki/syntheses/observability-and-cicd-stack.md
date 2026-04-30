---
title: "Observability + CI/CD Stack — Docker → GHA → Prometheus → Grafana → Sentry 5단 흐름"
type: synthesis
category: dev-tools
tags: [observability, cicd, docker, github-actions, prometheus, grafana, sentry, agents-md, anti-fragmentation, hierarchical-agents-md, cncf]
sources:
  - "[[moby-moby]]"
  - "[[github-actions-docs]]"
  - "[[prometheus-prometheus]]"
  - "[[grafana-grafana]]"
  - "[[getsentry-sentry]]"
  - "[[backend-fastapi-stack]]"
  - "[[agent-skills]]"
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 18
inbound_count: 39
---

# Observability + CI/CD Stack — Docker → GHA → Prometheus → Grafana → Sentry 5단 흐름

## 본문

수집한 운영/Observability 진영 5개 OSS — [[docker]] / [[github-actions]] / [[prometheus]] / [[grafana]] / [[sentry]] — 를 단일 흐름으로 묶는다. 빌드/패키징(Docker)부터 자동화(GHA), 메트릭(Prometheus), 시각화(Grafana), 에러 추적(Sentry)까지 5단을 통합하면 사이드 프로젝트와 컴투스플랫폼 BI 양쪽에 직접 응용 가능한 OSS-only 운영 스택이 된다.

개념 레벨의 관측성 정의와 metrics/logs/traces/errors/RUM 5축은 [[observability]]에 정리하고, 본 페이지는 그 개념을 Docker/GitHub Actions/Prometheus/Grafana/Sentry 운영 스택으로 구체화한다.

또한 핵심 메타 발견은 **AGENTS.md 진화 11단계** — 운영 진영 3개 OSS(Prometheus/Grafana/Sentry)가 동시에 AGENTS.md를 채택하면서 **4가지 새 변종**(PR-패턴 가이드 / `@AGENTS.md` redirect / 계층화 / anti-fragmentation 명문화)을 등장시켰다. [[agent-skills]] 11단계로 정리된 이 발견은 [[backend-fastapi-stack]]·[[dataframe-ecosystem-evolution]]·[[agent-frameworks-matrix]]에 이은 5번째 종합 축이다.

## 5단 흐름 (Pipeline)

```
[1] Docker / Moby — 빌드/패키징
        ↓ (Dockerfile, image)
[2] GitHub Actions — CI/CD 자동화
        ↓ (PR push → test → build → deploy)
[3] Prometheus — 메트릭 수집
        ↓ (HTTP pull, time series + labels)
[4] Grafana — 통합 시각화
        ↓ (multi-source: Prometheus + Loki + PostgreSQL)
[5] Sentry — 에러/RUM 추적
   (frontend + backend errors, breadcrumbs, replays)
```

각 단계의 1차 인터페이스:

| 단계 | OSS | 1차 입력 | 1차 출력 |
| --- | --- | --- | --- |
| 1. 빌드 | Docker/Moby | `Dockerfile` | OCI 이미지 |
| 2. CI/CD | GitHub Actions | `.github/workflows/*.yml` | 배포된 컨테이너 |
| 3. 메트릭 | Prometheus | `/metrics` 엔드포인트 (pull) | PromQL 쿼리 |
| 4. 시각화 | Grafana | 데이터소스 (Prometheus/Loki/PG) | 대시보드 + 알림 |
| 5. 에러 | Sentry | SDK 이벤트 (push) | 이슈 + replay |

## AGENTS.md 양극화 분석

5개 OSS의 AGENTS.md 채택 패턴:

| OSS | AGENTS.md | 형식 | 주요 특징 |
| --- | --- | --- | --- |
| Docker/Moby | ❌ | — | CONTRIBUTING.md 중심, 상업 컨텍스트 |
| GitHub Actions | ❌ | — | 분산 OSS, docs.github.com SSOT |
| Prometheus | ✅ | **PR-패턴 가이드** (148줄) | "merge된 PR로부터 패턴 추출" |
| Grafana | ✅ | **계층화 + redirect** (161줄) | docs/+alerting/ 분산, `<!-- version: 2.0.0 -->` |
| Sentry | ✅ | **Anti-fragmentation SSOT** (256줄) | "Do not add to CLAUDE.md" 명문화 |

→ **양극화 가설**: 애플리케이션 코드에 가까운 운영 OSS는 AI agent 가이드를 적극 채택, 인프라 코어 OSS(Docker, GHA)는 상업/정치적 이유로 신중. CI/CD 진영 전체(Jenkins/CircleCI/GitLab CI)가 AGENTS.md 미채택과 일치.

### 4가지 새 변종 (11단계 진화 핵심)

1. **PR-패턴 가이드** (Prometheus): "최근 merge된 PR로부터 maintainer 선호 패턴을 추출한 contributor 가이드". 가장 데이터 기반, 가장 유지비 낮음. 새 contributor 진입 비용은 더 높음.

2. **`@AGENTS.md` redirect CLAUDE.md** (Grafana/Sentry): CLAUDE.md = 1줄 `@AGENTS.md`. AGENTS.md SSOT, 두 파일 sync 운영 부담 제거.

3. **계층화 AGENTS.md** (Grafana 2-tier, Sentry 4-tier): 모노레포 영역별 다른 컨벤션 → 디렉토리별 분산.
 - Grafana: `/AGENTS.md` + `docs/AGENTS.md` + `public/app/features/alerting/unified/AGENTS.md`
 - Sentry: `/AGENTS.md` + `src/` + `tests/` + `static/` (각각 다른 CODEOWNERS 팀)

4. **Anti-fragmentation 명문화** (Sentry): "AGENTS.md is the source of truth, **do not add to CLAUDE.md or Cursor rules**" — AI agent별 룰 파일 drift 방지.

추가: **AGENTS.md 자체 버저닝** (Grafana `<!-- version: 2.0.0 -->`) — 향후 다른 OSS도 따라할 가능성.

## 거버넌스 모델 9번째 추가 — CNCF graduated

| # | 모델 | 사례 | |
| --- | --- | --- | --- |
| 1 | Anthropic | Claude Code, anthropics-skills | |
| 2 | OpenAI | OpenAI Agents Python, Cookbook | |
| 3 | Pydantic Foundation | Pydantic v2 | |
| 4 | Astral | UV, Ruff | |
| 5 | 커뮤니티 (Pola.rs) | Polars | |
| 6 | NumFOCUS | Pandas | |
| 7 | Apache Software Foundation (ASF PMC) | Arrow, Kafka | |
| 8 | LangChain Inc. | LangChain, LangGraph, DeepAgents | |
| 9 | **CNCF graduated** | **Prometheus** | **** |

→ ASF(데이터/JVM)와 CNCF(클라우드 네이티브 인프라/런타임)는 vendor-neutral 재단의 양대 산맥. Linux Foundation 우산.

## 사이드 프로젝트 적용 (30분 부트스트랩)

FastAPI + Postgres 스택에 5단 OSS 통합:

```
[Step 1] Dockerfile + docker-compose.yml
   - app(FastAPI), db(Postgres), prometheus, grafana

[Step 2] .github/workflows/deploy.yml
   - on: push to main → pytest → docker build → push → deploy
   - secrets: AWS OIDC (정적 credential 없음)

[Step 3] prometheus-fastapi-instrumentator
   - pip install → app.add_middleware(...) 1줄
   - /metrics 엔드포인트 자동 노출

[Step 4] Grafana Cloud 무료 티어
   - data source: Prometheus URL 입력
   - import dashboard 1860 (FastAPI default)

[Step 5] sentry-sdk[fastapi]
   - sentry_sdk.init(dsn=..., traces_sample_rate=0.1) 1줄
   - 백엔드 에러 + 프론트엔드 에러 (sentry-react) 통합
```

→ 5축 중 3축(metrics/errors/logs) 30분 만에 확보. 추가로 trace는 OTel 도입 시점에 보강.

## 컴투스플랫폼 BI 적용 매핑

| 단계 | BI 적용 | 기존 도구 |
| --- | --- | --- |
| 1. Docker | c2spf-analytics 분석 잡 컨테이너화 | Docker (이미 사용) |
| 2. GHA | 회사 정책상 Jenkins → GHA 마이그레이션 후보 | Jenkins 멀티브랜치 |
| 3. Prometheus | 데이터 파이프라인 메트릭(처리량, 실패율) | (현재 미정) |
| 4. Grafana | 4환경(상용/스테이징/샌드박스/테스트) 분리 대시보드 | **이미 사용** |
| 5. Sentry | 데이터 파이프라인 에러 추적 + BI 대시보드 자체 에러 | (현재 미정) |

→ Grafana는 이미 운영 중, Prometheus/Sentry 도입이 가장 큰 가시성 향상 후보.

## Sentry Feature Flag 5단계 워크플로우 — c2spf-analytics 응용

[[sentry]] AGENTS.md에서 발견된 패턴을 BI 시스템에 적용:

1. `temporary.py` 등록 (예: `analytics:new-aggregation`)
2. Python 체크 (`features.has(...)`)
3. Dashboard 체크 (`organization.features.includes(...)`)
4. Test (`with self.feature(...)` 컨텍스트)
5. Rollout (별도 자동화 레포)

→ 안전한 점진적 롤아웃 가능. BI는 데이터 정합성이 핵심이라 atomic switch보다 단계적 노출이 안전.

## 위험 요소 / 라이선스 주의

| OSS | 라이선스 | SaaS화 영향 |
| --- | --- | --- |
| Docker/Moby | Apache-2.0 | 자유 |
| GitHub Actions | 분산 (대부분 MIT) | 자유 |
| Prometheus | Apache-2.0 | 자유 |
| **Grafana** | **AGPL-3.0** | **SaaS 시 소스 공개 의무** |
| **Sentry** | **BSL → Apache-2.0 (3년 후)** | **SaaS 재판매 차단, 3년 후 자동 전환** |

→ Grafana/Sentry self-hosted는 자유, SaaS 형태로 외부에 제공 시 라이선스 검토 필수. Grafana Cloud / Sentry SaaS는 별도 트랙.

## 다음 진화 단서

발견된 다음 진화 후보:

1. **AGENTS.md 자동 생성 도구** (현재는 사람이 직접 작성). Prometheus PR-패턴 가이드처럼 "최근 merge된 PR 분석 → AGENTS.md 자동 업데이트" 워크플로우.
2. **AGENTS.md 버저닝 표준화** (Grafana `<!-- version: 2.0.0 -->` 첫 도입). 향후 SemVer 또는 날짜 기반 표준.
3. **Workflow YAML / Dockerfile 가이드 표준** — 코드 외 자산에 대한 LLM 가이드. 현재 없음, 점검 시 정리 필요.
4. **OpenTelemetry 통합 layer** — Prometheus/Grafana/Sentry 모두 OTLP 입력 지원, 단일 instrument 패키지로 5축 동시 emit 가능성.

## 출처

- [[moby-moby]] — Docker Engine OSS 업스트림, AGENTS.md 미채택
- [[github-actions-docs]] — actions/runner + actions/toolkit, 분산 OSS
- [[prometheus-prometheus]] — CNCF graduated, PR-패턴 AGENTS.md
- [[grafana-grafana]] — 9+10단계 진화, AGENTS.md 버저닝 첫 도입
- [[getsentry-sentry]] — Anti-fragmentation SSOT 명문화
- [[backend-fastapi-stack]] — 종합, 자매 종합 (FastAPI 메트릭 instrumentation 연계)
- [[agent-skills]] — 11단계 진화 = 메타 결론

## 열린 질문

- AGENTS.md 양극화(애플리케이션 vs 인프라)는 시간이 지나며 좁혀질까, 유지될까? 점검 시 Docker/GHA 재확인.
- Grafana AGPL-3.0 self-hosted vs Grafana Cloud 무료 티어의 BI 사용 시 trade-off는?
- OpenTelemetry가 Prometheus/Grafana/Sentry 3가지 OSS를 단일 instrument로 통합하면 본 5단 흐름이 4단으로 압축될까? (Step 3+5 합쳐지는 시나리오)
- Sentry의 viewer_context contextvar 패턴을 c2spf-analytics에 도입하면 인증 코드의 readability/typing 측면에서 얼마나 개선되는지 정량 측정 가능한가?
