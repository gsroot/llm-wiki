---
title: Moby (Docker Engine 업스트림) — 컨테이너 생태계의 레고 키트
type: source
source_type: article
source_url: https://github.com/moby/moby
raw_path: raw/articles/moby-moby/
author: Moby Project (Docker Inc. + 커뮤니티)
date_published: 2026-04-28
date_ingested: 2026-04-28
tags:
- docker
- moby
- container
- devops
- runtime
related:
- '[[docker]]'
- '[[devops-cicd]]'
- '[[observability-and-cicd-stack]]'
confidence: high
inbound_count: 8
cited_by:
- '[[devops-cicd]]'
- '[[docker]]'
- '[[observability-and-cicd-stack]]'
cited_by_count: 3
aliases:
- Moby
- Moby (Docker Engine 업스트림) — 컨테이너 생태계의 레고 키트
- moby
---

# Moby (Docker Engine 업스트림) — 컨테이너 생태계의 레고 키트

## 한줄 요약

> Moby는 Docker가 만든 오픈소스 컨테이너 툴킷으로, "Docker Engine의 업스트림"이자 "컨테이너 시스템 조립용 레고 세트" 두 정체성을 동시에 가진다.

## 핵심 내용

- **이중 정체성**: README 명시 — "Docker Project를 위해 Docker와 커뮤니티가 만든 오픈소스 컴포넌트들"인 동시에 "다른 프로젝트도 Moby를 업스트림으로 사용 가능". Docker Inc.의 일방적 통제가 아닌 "외부 메인테이너/컨트리뷰터 환영" 명시.
- **5대 원칙 (Principles)**: ① Modular(잘 정의된 API의 컴포넌트들), ② Batteries included but swappable(필수 부품은 포함하되 교체 가능), ③ Usable security(사용성 해치지 않는 기본 보안), ④ Developer focused(엔드유저용 아닌 개발자용 빌딩블록), ⑤ Open project(커뮤니티가 방향 결정).
- **Go 모듈 재정렬 (Docker v29, 2025-11)**: `github.com/docker/docker` deprecated → `github.com/moby/moby/v2` (메인 binary용, Go 라이브러리로 import 금지) + `github.com/moby/moby/client` + `github.com/moby/moby/api`로 분리.
- **릴리스 태그 분리**: Docker Engine 빌드는 `docker-vXX.Y.Z` 접두사 태그(`go get` 금지), client/api 모듈은 독립 시맨틱 버저닝(`client/v1.x.x`).
- **상업 vs OSS 경계**: README가 직접 명시 — "기업 지원 원하면 Docker Desktop 또는 Mirantis Container Runtime, OSS는 best-effort 메인테이너 지원".
- **AGENTS.md 부재**: 운영/Observability 진영의 다른 OSS와 달리 Moby는 AGENTS.md/CLAUDE.md 미채택. CONTRIBUTING.md 중심의 전통적 OSS 거버넌스 유지.

## 주요 인사이트

- **"Lego set" 메타포**: README 사용 단어 그대로. FastMCP의 "MCP 서버 만드는 LEGO 블록"과 동일 메타포 — 인프라 OSS의 자기 정의 패턴.
- **Docker → Moby 분리(2017)의 결과를 2026에 정착**: v29(2025-11)가 마지막 import path 정리. 8년 만의 거버넌스 분리 완성. Docker는 제품 브랜드, Moby는 OSS 코드베이스로 이름 분리.
- **AGENTS.md 비채택의 의미**: Prometheus/Grafana/Sentry는 채택, Moby는 미채택 → 운영 진영도 한 방향 수렴 아님. Docker Inc.의 상업 모델이 OSS 메인테이너 가이드를 내부에 두는 패턴일 가능성.
- **컴투스플랫폼 BI 적용**: c2spf-analytics 같은 분석 컨테이너의 베이스 이미지로 직접 사용. Moby = 인프라 레이어로서 BI 파이프라인의 "보이지 않는 토대".

## 관련 엔티티/개념

- [[docker]]: 본 소스 1차 대상. Docker = Moby 위에 빌드된 제품.
- [[devops-cicd]]: 컨테이너는 CI/CD의 사실상 표준 패키징 단위.
- [[observability-and-cicd-stack]]: 종합 — Docker → GHA → Prometheus → Grafana → Sentry 흐름의 1단계.

## 인용할 만한 구절

> "Moby is an open-source project created by Docker to enable and accelerate software containerization. It provides a 'Lego set' of toolkit components, the framework for assembling them into custom container-based systems."
> — moby/moby README

> "External maintainers and contributors are welcomed."
> — moby/moby README, "Relationship with Docker" 섹션

## 메모

- README가 71K stars 대비 매우 짧음(102줄) — 핵심 원칙과 모듈 재정렬만 다룸. 실제 가이드는 docs/ 하위로 분산. 이는 운영 OSS의 패턴 ("저장소가 아닌 docs 사이트가 SSOT").
- 점검 시점에 Moby의 AGENTS.md 채택 여부 재확인 필요 — Grafana/Sentry처럼 후발 채택 가능.
- BI 영역에서 Docker의 직접 활용은 분석 잡 컨테이너화 + airflow/dbt 격리. moby/api Go 모듈은 BI에서 거의 쓸 일 없음.
