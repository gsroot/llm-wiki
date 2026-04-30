---
title: "GitHub Actions"
aliases: [GitHub Actions, 깃허브 액션, GHA]
type: entity
entity_type: service
tags: [github-actions, ci-cd, runner, toolkit, devops, oidc, 19회차]
related:
  - "[[docker]]"
  - "[[devops-cicd]]"
  - "[[observability-and-cicd-stack]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 3
inbound_count: 15
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 7
---

# GitHub Actions

## 개요

GitHub Actions(GHA)는 GitHub(2018 출시, 2019 GA)이 운영하는 CI/CD 서비스이자 분산 OSS 생태계. `actions/runner` (.NET Core executor) + `actions/toolkit` (TypeScript SDK) + `actions/checkout` 등 수만 개 third-party action으로 구성된다. 단일 megamonolith 저장소가 없는 19회차의 유일한 항목으로, 실제 가이드는 docs.github.com이 SSOT.

## 주요 특징

| 축 | GitHub Actions |
| --- | --- |
| 운영 주체 | GitHub (Microsoft) |
| 출시 | 2018 (베타) → 2019 (GA) |
| 핵심 OSS | `actions/runner` (.NET Core), `actions/toolkit` (TypeScript) |
| 작성 방식 | ① JS action(toolkit), ② Composite action(YAML), ③ Docker action |
| Runner 종류 | GitHub-hosted (Ubuntu/Windows/macOS) + Self-hosted |
| Workflow 정의 | `.github/workflows/*.yml` (JSON Schema 검증) |
| Marketplace | `marketplace.github.com/actions` (수만 개 action) |
| AGENTS.md | ❌ 미채택 (GitHub Copilot이 자체 표준) |

## 관련 개념

- [[docker]]: Docker action / Container job / `setup-buildx-action` 등 컨테이너 통합 핵심.
- [[devops-cicd]]: GHA = OSS 진영 CI/CD의 사실상 표준.
- [[observability-and-cicd-stack]]: 19회차 종합의 CI/CD 자동화 레이어.

## actions/toolkit 핵심 패키지 (TypeScript SDK)

| 패키지 | 용도 |
| --- | --- |
| `@actions/core` | Input/output/logging |
| `@actions/exec` | 외부 명령 실행 |
| `@actions/glob` | 파일 매칭 |
| `@actions/io` | 파일 시스템 |
| `@actions/tool-cache` | 도구 캐시 |
| `@actions/github` | Octokit wrapper |
| `@actions/artifact` | Artifact 업/다운로드 |
| `@actions/cache` | 의존성 캐시 |

## OIDC 기반 클라우드 인증 (BI 적용 핵심)

정적 credential 없이 AWS STS / GCP Workload Identity / Azure AD 토큰 발급 가능. 컴투스 플랫폼 BI에서 IAM 토큰 관리 단순화 가능 — `aws-actions/configure-aws-credentials@v4`.

## 19회차 운영 진영 CI/CD 비교

| 도구 | 위치 | OSS | AGENTS.md |
| --- | --- | --- | --- |
| GitHub Actions | GitHub 통합 | 분산형 | ❌ |
| Jenkins | Self-hosted | 단일 OSS | ❌ |
| CircleCI | SaaS | 부분 OSS | ❌ |
| GitLab CI | GitLab 통합 | 단일 OSS | ❌ |

→ **CI/CD 진영 전체에 AGENTS.md 표준 미확산**. 운영 진영 안에서도 모니터링(Prometheus/Grafana/Sentry, 100% 채택)과 CI/CD(0% 채택)의 양극화.

## 출처

- [[github-actions-docs]] — actions/runner README (39줄) + actions/toolkit README (250줄) — confidence: medium (단일 저장소 부재).

## 메모

- BI 적용 핵심: c2spf-analytics 배포 자동화 (PR push → pytest → Docker build → S3/ECR push → 운영 환경 deploy).
- Self-hosted runner를 회사 VPC 내에 두면 보안 경계 안에서 BI 파이프라인 자동화 가능.
- `@actions/cache`로 pip 의존성 캐시(빌드 5배 빠름), `@actions/artifact`로 분석 결과 워크플로우 간 공유 가능.
- 21회차 점검 시 "GHA workflow YAML LLM 자동 생성 패턴" 정리 필요 — AGENTS.md가 없으므로 별도 가이드.
