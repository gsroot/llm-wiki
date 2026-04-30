---
title: "Prometheus"
aliases: [Prometheus, 프로메테우스]
type: entity
entity_type: tool
tags: [prometheus, cncf, monitoring, observability, time-series, promql, agents-md]
related:
  - "[[grafana]]"
  - "[[docker]]"
  - "[[observability-and-cicd-stack]]"
  - "[[agent-skills]]"
  - "[[devops-cicd]]"
  - "[[prometheus-prometheus]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 7
inbound_count: 34
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 15
---

# Prometheus

## 개요

Prometheus는 SoundCloud(2012)에서 시작해 2016년 CNCF에 합류, 2018년 두 번째 졸업 프로젝트(Kubernetes 다음)가 된 시계열 메트릭 모니터링 시스템. **단일 서버 노드 자율 + HTTP pull 모델 + PromQL** 3대 특징으로 클라우드 네이티브 모니터링의 사실상 표준이 됐다. 발견된 7번째 AGENTS.md 채택 OSS이며, 그 형식이 **PR 리뷰 패턴 가이드**라는 점에서 다른 OSS와 차별화된다.

## 주요 특징

| 축 | Prometheus |
| --- | --- |
| 거버넌스 | **CNCF graduated** (2018) — 9번째 OSS 거버넌스 모델 |
| Stars (2026-04) | 63.8K |
| 라이선스 | Apache-2.0 |
| 데이터 모델 | 다차원 시계열 (metric name + key/value labels) |
| 쿼리 언어 | **PromQL** (그래프/알림/대시보드 통합) |
| 수집 모델 | HTTP pull (Push gateway는 배치 잡용) |
| 분산 스토리지 | ❌ 의존 없음 (단일 노드 자율, HA는 Cortex/Thanos/Mimir) |
| AGENTS.md | ✅ 148줄, **PR 리뷰 패턴 가이드 형식** |
| Commit 서명 | DCO 강제 (`git commit -s`) |

## 관련 개념

- [[grafana]]: Prometheus의 1차 시각화 클라이언트. "기본 페어" 관계로 거의 항상 함께 배포.
- [[docker]]: prometheus 이미지(Quay.io/Docker Hub)로 1라인 실행 가능.
- [[observability-and-cicd-stack]]: 종합의 메트릭 레이어.
- [[agent-skills]]: AGENTS.md 진화 8단계 (PR-패턴 변종)의 핵심 사례.
- [[devops-cicd]]: SRE/Observability 표준의 일부.

## AGENTS.md PR-패턴 형식

Prometheus의 AGENTS.md는 다른 OSS(Pydantic AI 코드베이스 가이드, OpenAI Agents skill 모음)와 다른 형식 — "최근 merge된 PR로부터 maintainer 선호 패턴을 추출한 contributor 가이드".

섹션 구성:
1. PR 제목 형식 (영역 prefix 강제: `tsdb`, `promql`, `agent`, ...)
2. Commits (각 커밋이 독립 컴파일/테스트 통과, DCO 서명)
3. Release notes block (6 prefix: FEATURE/ENHANCEMENT/PERF/BUGFIX/SECURITY/CHANGE)
4. Tests (버그픽스에 reproducer 테스트 필수)
5. Performance work (`benchstat` 출력 필수)
6. Code style (golangci-lint, gocritic)
7. Linking issues / Scope discipline / Documentation / CI workflow

→ **장점**: 가장 데이터 기반, 가장 유지비 낮음. **단점**: 새 contributor 진입 비용 더 높음.

## 의사결정 컨텍스트 (raw 인용)

> "Prometheus는 CNCF 두 번째 졸업 프로젝트(Kubernetes 다음)이자 시계열 메트릭 모니터링의 사실상 표준이며, 발견된 7번째 AGENTS.md 채택 OSS — 다만 그 형식이 'PR 리뷰 패턴 가이드'로 다른 OSS와 차별화됨."
> — [[prometheus-prometheus]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] DevOps 5단(Docker → GHA → Prometheus → Grafana → Sentry) 3단. **메트릭 수집 표준** — [[c2spf-analytics|c2spf 게임 데이터 BI]] 회사 시스템·[[matechat|MateChat 사이드 프로젝트]] 사이드 양쪽에서 동일 채택. PR 리뷰 패턴 AGENTS.md(148줄)는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 운영 표준 학습 자료.

## 출처

- [[prometheus-prometheus]] — README (229줄) + AGENTS.md (148줄, PR 패턴) — 7번째 AGENTS.md OSS.

## 메모

- 컴투스플랫폼 BI 영역에서 직접 사용: 게임 백엔드 메트릭(QPS, 에러율, p99 latency) 수집. 비즈니스 메트릭(DAU, 매출)은 별도 데이터 웨어하우스로 분리.
- AGENTS.md PR-패턴 형식을 c2spf-analytics에 응용 가능 — "최근 merge된 PR 분석 → AGENTS.md 자동 업데이트" 워크플로우.
- 9번째 거버넌스 모델 (CNCF graduated) — vendor-neutrality + Linux Foundation 우산.
- ASF PMC와 CNCF는 모두 vendor-neutral 재단이지만 영역 다름: ASF=데이터/JVM, CNCF=클라우드 네이티브 인프라/런타임.
