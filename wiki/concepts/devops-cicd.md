---
title: "DevOps & CI/CD (Docker · Jenkins 멀티브랜치 · Loki/Grafana)"
type: concept
category: dev-tools
tags: [devops, cicd, docker, docker-compose, jenkins, multi-branch, github-actions, nginx, loki, promtail, grafana, observability, prometheus, sentry, 19회차]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[backend-python-fastapi]]"
  - "[[frontend-react]]"
  - "[[docker]]"
  - "[[github-actions]]"
  - "[[prometheus]]"
  - "[[grafana]]"
  - "[[sentry]]"
  - "[[observability]]"
  - "[[observability-and-cicd-stack]]"
source_count: 8
observed_source_refs: 17
inbound_count: 43
created: 2026-04-24
updated: 2026-04-28
cited_by_count: 23
---

# DevOps & CI/CD (Docker · Jenkins 멀티브랜치 · Loki/Grafana)

## 정의

c2spf 애널리틱스 팀의 표준 배포·운영 스택. Docker Compose로 빌드 단위를 표준화하고, Jenkins 멀티 브랜치 파이프라인으로 환경별(상용/스테이징/샌드박스/테스트) 자동 빌드·배포를 실행한다. Promtail에서 Loki를 거쳐 Grafana로 4환경 로그를 중앙 집중하여 관측성을 확보.

## 왜 중요한가

- **2024-10~11 집중 발행 가이드 4종**으로 팀 표준 정립 — Docker Compose 가이드, Jenkins 멀티브랜치 가이드, 공통 API 명세, 공통 JS 가이드.
- **SSH 수동 검색에서 Grafana 레이블 필터링으로** 전환하여 트러블슈팅 난이도 하락. 환경별 로그 분리 운영(상용 Primary/Standby + 샌드박스 + 테스트)으로 4종 환경 전부 가시화.
- 공통 API 단독 유지보수 92% 환경에서, **자동화가 없으면 운영 부담이 단일 담당자에게 집중**된다는 위험을 가이드와 자동화로 분산.

## 핵심 내용

- **컨테이너**: Docker, Docker Compose. 환경별 compose 파일 분리.
- **CI**: Jenkins (멀티 브랜치 파이프라인) — 브랜치별 자동 빌드·테스트·배포. GitHub Actions는 개인 프로젝트에서 사용.
- **배포**: nginx 리버스 프록시, AWS EC2.
- **관측성**
  - Promtail에서 Loki로: 컨테이너 로그 수집·중앙화.
  - Grafana: 4환경 분리 대시보드 (상용 Primary/Standby + 샌드박스 + 테스트).
  - ElasticSearch + Kibana (구 NFT 마켓), Fluentd 구성도 경험.
- **운영 트러블슈팅**: BigQuery Decimal 변환, OS별 TCP Keepalive, 슬레이브 DB 동기화 이슈.

## 실전 적용

- 2024-10~11 가이드 4종 동시 발행으로 팀 배포 표준 단일 집중 정비.
- Jenkins 멀티브랜치 파이프라인이 `main`/`staging`/`sandbox`/`test` 브랜치별로 자동 빌드.
- React 리뉴얼(2025-06) 시 Vite 빌드를 기존 Docker 파이프라인에 통합.
- 개인 프로젝트(트래블메이트)에서는 GitHub Actions + Google Play 영수증 검증.

## 관련 개념

- [[backend-python-fastapi]] — 컨테이너에 패키징되는 백엔드
- [[frontend-react]] — Vite 빌드에서 Docker 컨테이너로, Jenkins 배포
- [[data-pipeline-bigquery]] — Promtail/Loki로 데이터 파이프라인 로그 관측

## 출처

- [[portfolio-seed]] — Docker/Jenkins/GitHub Actions 진화 타임라인
- [[portfolio-ko]] — Selected Work 5선의 인프라 측면
- [[c2spf-analytics-common]] — 가이드 4종 발행, 4환경 로깅 스택 구축
- [[moby-moby]] — Docker/Moby OSS 업스트림 (19회차 신규)
- [[github-actions-docs]] — GHA runner + toolkit (19회차 신규)
- [[prometheus-prometheus]] — CNCF graduated 메트릭 OSS (19회차 신규)
- [[grafana-grafana]] — 통합 시각화 (19회차 신규)
- [[getsentry-sentry]] — 에러/RUM 추적 (19회차 신규)

## 19회차 종합 (Observability + CI/CD 5단)

자세한 흐름은 [[observability-and-cicd-stack]] 참조: Docker → GHA → Prometheus → Grafana → Sentry 5단 OSS 통합. 19회차에서 발견된 [[agent-skills]] 11단계 진화 — 운영 진영 3 OSS(Prometheus/Grafana/Sentry) AGENTS.md 동시 채택 + 4가지 새 변종(PR-패턴/redirect/계층화/anti-fragmentation)이 본 회차의 핵심 메타 결론.

## 열린 질문

- Jenkins에서 GitHub Actions 마이그레이션의 비용/이득은? 사내 정책 의존도가 어느 정도인가?
- Loki 4환경 분리의 비용 vs 단일 인스턴스 다중 라벨 전략 비교는?
