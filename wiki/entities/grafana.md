---
title: "Grafana"
aliases: [Grafana, 그라파나]
type: entity
entity_type: tool
tags: [grafana, observability, dashboard, agents-md, hierarchical-agents]
related:
  - "[[prometheus]]"
  - "[[postgresql]]"
  - "[[docker]]"
  - "[[sentry]]"
  - "[[observability-and-cicd-stack]]"
  - "[[agent-skills]]"
  - "[[devops-cicd]]"
  - "[[grafana-grafana]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 6
inbound_count: 32
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 13
---

# Grafana

## 개요

Grafana는 Torkel Ödegaard(2014)가 만든 멀티 데이터소스 시각화 플랫폼이며, 메트릭/로그/트레이스를 한 화면에 통합한다. Grafana Labs(상업 회사)가 운영하지만 OSS는 AGPL-3.0으로 강한 카피레프트를 유지한다. 발견된 **9단계 + 10단계 AGENTS.md 진화의 핵심 증거** — `@AGENTS.md` 한 줄 CLAUDE.md(SSOT redirect)와 디렉토리별 AGENTS.md(계층화)를 동시 채택한 첫 OSS 중 하나(Sentry와 함께).

## 주요 특징

| 축 | Grafana |
| --- | --- |
| 운영 주체 | Grafana Labs (상업 회사) |
| Stars (2026-04) | 73.5K (운영 진영 최대) |
| 라이선스 | AGPL-3.0-only (예외 Apache-2.0), Enterprise/Pro는 별도 |
| 백엔드 | Go + Wire DI + CUE 스키마 |
| 프론트엔드 | TypeScript/React + Redux Toolkit + RTK Query + Emotion CSS |
| 빌드 태그 | `oss` / `enterprise` / `pro` |
| AGENTS.md | ✅ 161줄, **9단계(redirect) + 10단계(계층화) 동시 채택** |
| CLAUDE.md | `@AGENTS.md` 한 줄 redirect |
| 디렉토리별 AGENTS.md | `docs/AGENTS.md`, `public/app/features/alerting/unified/AGENTS.md` |
| CODEOWNERS | `/AGENTS.md @grafana/docs-tooling` (문서 팀이 owner) |

## 관련 개념

- [[prometheus]]: 1차 데이터소스, 사실상 표준 페어.
- [[postgresql]]: Grafana 자체 메타데이터 저장소 + 데이터소스 양쪽으로 사용 가능.
- [[docker]]: 공식 grafana/grafana 이미지로 배포.
- [[sentry]]: 같은 9+10단계 AGENTS.md 진화 패턴 (운영 진영 표준).
- [[observability-and-cicd-stack]]: 시각화 레이어.
- [[agent-skills]]: AGENTS.md 진화 9~10단계의 핵심 증거.
- [[devops-cicd]]: 운영 가시성의 1차 진입점.

## AGENTS.md 진화 9~10단계 동시 채택

**9단계 — `@AGENTS.md` redirect**: CLAUDE.md = 1줄 `@AGENTS.md`. AGENTS.md SSOT, fragmentation 제거.

**10단계 — 계층화 AGENTS.md**: 모노레포 영역별로 다른 컨벤션 → 디렉토리별 분산.

```
Grafana 모노레포 구조:
/AGENTS.md                                              ← 루트(인덱스 + 공통)
├── docs/AGENTS.md                                      ← 문서 스타일 가이드
└── public/app/features/alerting/unified/AGENTS.md      ← Alerting squad 패턴
```

→ AGENTS.md 자체에 `<!-- version: 2.0.0 -->` 주석 — **AGENTS.md 버저닝 도입 첫 사례**.

## PR 분리 룰 (Grafana + Sentry 공통)

"Frontend(`public/`)와 Backend(`pkg/`)는 atomically deployed되지 않음 — 각각 별도 PR 필수, 다른 cadence". c2spf-analytics 같은 모노레포 BI 시스템에 직접 응용 가능.

## 의사결정 컨텍스트 (raw 인용)

> "Grafana는 메트릭/로그/트레이스를 한 화면에서 다루는 통합 시각화 플랫폼이며, 발견된 9단계 AGENTS.md 진화의 핵심 사례 — **계층화 AGENTS.md(루트 + 디렉토리별)** + **`@AGENTS.md` 한 줄짜리 CLAUDE.md(SSOT redirect)** 패턴."
> — [[grafana-grafana]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] DevOps 5단 4단. [[prometheus]](메트릭) + Loki(로그)·Tempo(트레이스, 별도 entity 미생성)을 한 dashboard로 통합. **계층화 AGENTS.md** 패턴은 [[matechat|MateChat 사이드 프로젝트]] 39 SKILL 운영의 directory-scoped scope 통제와 직접 연결 — [[agent-skills]] progressive disclosure의 동등 패턴.

## 출처

- [[grafana-grafana]] — README (51줄) + AGENTS.md (161줄, 7862 bytes) + CLAUDE.md (1줄 redirect) + CONTRIBUTING.md.

## 메모

- BI 영역에서 직접 사용: Plugin workspace(`grafana-postgresql-datasource`)로 컴투스 플랫폼 게임 분석 DB 연결. Tableau 대비 OSS + AGPL 운영 조건 클리어.
- AGPL 라이선스 주의: SaaS로 제공 시 소스 공개 의무. Grafana Cloud(상업)는 다른 라이선스 트랙.
- 점검 시 "AGENTS.md 채택자별 fragmentation 룰 비교 매트릭스" 작성 — Grafana(silent SSOT, redirect로 안내) vs Sentry(strict SSOT, "do not add to CLAUDE.md" 명문화) 차이점 정리 필요.
