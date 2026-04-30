---
title: "Prometheus — CNCF 졸업 모니터링 시스템 + PR-패턴 AGENTS.md"
type: source
source_type: article
source_url: "https://github.com/prometheus/prometheus"
raw_path: "raw/articles/prometheus-prometheus/"
author: "Prometheus Authors (CNCF)"
date_published: 2026-04-28
date_ingested: 2026-04-28
tags: [prometheus, cncf, monitoring, observability, time-series, promql, agents-md, 19회차]
related:
  - "[[prometheus]]"
  - "[[grafana]]"
  - "[[observability-and-cicd-stack]]"
  - "[[agent-skills]]"
confidence: high
inbound_count: 11
cited_by:
  - "[[agent-skills]]"
  - "[[devops-cicd]]"
  - "[[observability]]"
  - "[[observability-and-cicd-stack]]"
  - "[[prometheus]]"
cited_by_count: 5
---

# Prometheus — CNCF 졸업 모니터링 시스템 + PR-패턴 AGENTS.md

## 한줄 요약

> Prometheus는 CNCF 두 번째 졸업 프로젝트(Kubernetes 다음)이자 시계열 메트릭 모니터링의 사실상 표준이며, 19회차에서 발견된 7번째 AGENTS.md 채택 OSS — 다만 그 형식이 "PR 리뷰 패턴 가이드"로 다른 OSS와 차별화됨.

## 핵심 내용

- **8가지 핵심 차별점 (README)**: ① 다차원 데이터 모델(metric name + key/value labels), ② PromQL 쿼리 언어, ③ 분산 스토리지 의존 없음(단일 노드 자율), ④ HTTP pull 모델, ⑤ Push gateway(배치 잡용), ⑥ Service discovery 또는 정적 설정, ⑦ 다중 그래프/대시보드, ⑧ 계층/수평 federation.
- **CNCF 거버넌스 (9번째 OSS 거버넌스 모델)**: Cloud Native Computing Foundation의 graduated 프로젝트. Apache Software Foundation(ASF, 16회차에서 발견)과 다른 클라우드 네이티브 전용 재단.
- **AGENTS.md = PR 리뷰 패턴 가이드 (148줄)**: Pydantic AI/FastMCP 등의 "코드베이스 가이드" 형식과 다름. "merge된 PR에서 maintainer review 패턴을 추출해 contributor 가이드로 압축". 섹션: PR 제목 형식 / Commits / Release notes block / Tests / Performance work / Code style / Linking issues / Scope discipline / Documentation / CI workflow.
- **PR 제목 컨벤션 (영역 prefix 강제)**: `tsdb`, `tsdb/wlog`, `promql`, `discovery/<name>`, `agent`, `alerting`, `textparse`, `ui`, `build`, `ci`, `docs`, `chore`. 성능 작업은 `[PERF]` 또는 `perf(area):` 컨벤션.
- **Release notes block 강제**: 모든 PR에 ` ```release-notes ... ``` ` 펜스 코드 블록 필수. `[FEATURE]/[ENHANCEMENT]/[PERF]/[BUGFIX]/[SECURITY]/[CHANGE]` 6가지 prefix 또는 `NONE`.
- **DCO 서명 강제**: 모든 commit에 `git commit -s` (Developer Certificate of Origin) — CNCF 프로젝트 공통 요구사항.
- **성능 PR 정량 증빙**: `go test -count=6 -benchmem -bench` + `benchstat` 출력 본문 첨부. 회귀 발생 시 설명 또는 해결 의무.

## 주요 인사이트

- **8단계 AGENTS.md 진화 — PR 패턴 변종**: 1~7단계는 "코드베이스 사용설명서"(Pydantic AI 11 strengths) 또는 "skill 모음"(OpenAI Agents) 형식. Prometheus는 **"merge된 PR로부터 메인테이너 선호 패턴을 추출"** — 가장 데이터 기반적, 가장 유지비 낮은 형식. 다만 새 contributor 진입 비용은 더 높음.
- **CNCF 9번째 거버넌스 모델 추가**: 1~8번째: Anthropic / OpenAI / Pydantic Foundation / Astral / Pola.rs (커뮤니티) / Pandas (NumFOCUS) / Apache (ASF) / LangChain Inc.. 9번째 = **CNCF graduated**. Linux Foundation 산하 공익 재단으로 vendor-neutrality 유지.
- **"단일 서버 노드가 자율"라는 의도된 단순성**: 분산 스토리지 미사용 = SPOF 인정 + 운영 단순성 우선. 장기 보관/HA는 Cortex/Thanos/Mimir가 위에 얹는 모델 = "core는 simple하게, 확장은 outside로".
- **컴투스플랫폼 BI 적용**: 게임 백엔드 메트릭(QPS, 에러율, p99 latency) 수집 → Grafana 대시보드로 시각화. 비즈니스 메트릭(DAU, 매출)은 보통 별도 데이터 웨어하우스. **Prometheus는 인프라/애플리케이션 메트릭 전용**.

## 관련 엔티티/개념

- [[prometheus]]: 본 소스 1차 대상.
- [[grafana]]: Prometheus의 1차 시각화 클라이언트, "기본 페어" 관계.
- [[observability-and-cicd-stack]]: 19회차 종합의 메트릭 레이어.
- [[agent-skills]]: AGENTS.md 진화 8단계의 PR-패턴 변종 사례.

## 인용할 만한 구절

> "This document captures patterns and preferences observed from maintainer reviews of recently merged pull requests. Use it to align your contributions with what maintainers expect."
> — prometheus/prometheus AGENTS.md (서두)

> "single server nodes are autonomous"
> — README, 8가지 차별점 중 3번 (분산 스토리지 의존 없음)

## 메모

- PR-패턴 형식의 AGENTS.md는 c2spf-analytics에 직접 적용 가능 — "최근 merge된 PR로부터 패턴 추출 → AGENTS.md 자동 생성" 워크플로우. SOP 스킬(13회차 수집)의 후속 진화 단서.
- 16회차 ASF PMC와 19회차 CNCF가 "모두 vendor-neutral 재단"이지만 영역 다름: ASF = 데이터/JVM/메타데이터, CNCF = 클라우드 네이티브 인프라/런타임. Prometheus가 Linux Foundation 우산 아래라는 점이 LangChain Inc.(상업 회사)와 큰 대조.
- AGENTS.md 길이 짧음(148줄) — Pydantic AI(10K bytes), DeepAgents(21K bytes) 대비. PR 패턴 가이드는 "본질만 추출" 형식이라 장기 유지비가 가장 낮을 가능성.
