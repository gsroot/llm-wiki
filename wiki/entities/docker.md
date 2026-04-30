---
title: "Docker / Moby"
type: entity
entity_type: tool
tags: [docker, moby, container, runtime, devops, 19회차]
related:
  - "[[devops-cicd]]"
  - "[[github-actions]]"
  - "[[prometheus]]"
  - "[[grafana]]"
  - "[[sentry]]"
  - "[[observability-and-cicd-stack]]"
  - "[[moby-moby]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 4
inbound_count: 23
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 12
---

# Docker / Moby

## 개요

Docker는 컨테이너화 개념을 대중화한 회사이자 제품 브랜드, Moby는 그 OSS 코드베이스(`github.com/moby/moby`)다. 2017년 분리 이후 2025년 v29에서 Go 모듈 import path 정리(`github.com/docker/docker` → `github.com/moby/moby/v2`)로 거버넌스 분리가 8년 만에 완성됐다. Docker Engine은 컨테이너 빌드/실행 표준이며, BI/ML/웹/CI 파이프라인의 사실상 패키징 단위.

## 주요 특징

| 축 | Docker / Moby |
| --- | --- |
| 정체성 | OSS 컨테이너 툴킷 + 상업 제품(Docker Desktop, Mirantis Container Runtime) 듀얼 |
| 메타포 | "Lego set" — README가 직접 사용 |
| 라이선스 | Apache-2.0 (Moby), 상용은 별도 |
| 5대 원칙 | Modular / Batteries included but swappable / Usable security / Developer focused / Open project |
| Stars (2026-04) | 71.5K (moby/moby) |
| AGENTS.md | ❌ 미채택 (운영 진영 4개 중 유일) |
| 거버넌스 | Docker Inc. + 외부 메인테이너/컨트리뷰터 환영 명시 |

## 관련 개념

- [[devops-cicd]]: 컨테이너 = CI/CD 사실상 표준 패키징.
- [[github-actions]]: Docker action / Container job / setup-buildx-action 등 GHA 핵심 통합.
- [[prometheus]]: prometheus 컨테이너 이미지가 1차 배포 방식 (Quay.io, Docker Hub).
- [[grafana]]: 동일 — 컨테이너 이미지로 배포.
- [[observability-and-cicd-stack]]: 19회차 종합의 1단계(빌드/패키징).

## 19회차 운영/Observability 진영 비교

| OSS | AGENTS.md | 거버넌스 | 라이선스 |
| --- | --- | --- | --- |
| Docker/Moby | ❌ | Docker Inc. + 커뮤니티 | Apache-2.0 |
| Prometheus | ✅ (PR 패턴) | CNCF graduated | Apache-2.0 |
| Grafana | ✅ (계층화 + redirect) | Grafana Labs | AGPL-3.0 |
| Sentry | ✅ (anti-fragmentation) | Functional Software Inc. | BSL → Apache-2.0 (3년 후) |
| GitHub Actions | ❌ | GitHub (Microsoft) | 분산 OSS |

→ **AGENTS.md 채택률: 운영 진영 5개 중 3개 (60%)**.

## 의사결정 컨텍스트 (raw 인용)

> "Moby는 Docker가 만든 오픈소스 컨테이너 툴킷으로, 'Docker Engine의 업스트림'이자 '컨테이너 시스템 조립용 레고 세트' 두 정체성을 동시에 가진다."
> — [[moby-moby]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] DevOps 5단(Docker → GHA → Prometheus → Grafana → Sentry) 1단. **이중 정체성** — Docker Engine 업스트림 + 외부 컨트리뷰터 빌드 블록. Docker v29(2026)에서 Moby 분리 8년 만에 완성. [[c2spf-analytics|c2spf 게임 데이터 BI]] 회사 시스템·[[matechat|MateChat 사이드 프로젝트]] 사이드 양쪽에서 동일 패턴 채택.

## 출처

- [[moby-moby]] — README + CONTRIBUTING (102 + ~600줄), AGENTS.md 미채택 확인.

## 메모

- Docker → Moby 분리(2017~2025)의 8년 여정은 "OSS와 상업의 분리 운영" 케이스 스터디로 가치.
- BI 적용: c2spf-analytics 분석 잡을 Docker 컨테이너로 격리 → GHA로 빌드/푸시 → Kubernetes/ECS에 배포가 자연스러운 흐름.
- 21회차 점검 시 Moby AGENTS.md 채택 여부 재검증 필요 (운영 진영 trend 따라갈 가능성).
