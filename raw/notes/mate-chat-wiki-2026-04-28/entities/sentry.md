---
title: "Sentry"
type: entity
source_count: 2
tags: [monitoring, error-tracking, sentry, observability]
related:
  - "../entities/fastapi-app.md"
  - "../concepts/layered-architecture.md"
---

# Sentry

## Overview

Mate Chat의 에러 추적 및 APM(Application Performance Monitoring) 도구이다. FastAPI 애플리케이션에 통합되어 런타임 에러를 실시간으로 수집/보고한다.

## Architecture/Structure

- `sentry-sdk[fastapi]` 패키지를 통해 FastAPI와 직접 통합
- 환경 변수 `SENTRY_DSN`으로 프로젝트 설정
- structlog과 함께 사용하여 구조화된 에러 컨텍스트 제공

## Key Details

- **패키지**: sentry-sdk >= 2.39.0
- **용도**: 에러율 추적, 성능 모니터링
- **보완 도구**: Prometheus + Grafana (메트릭), Elasticsearch + Kibana (로그)

## Dependencies

- sentry-sdk[fastapi]
- FastAPI 미들웨어 통합

## Known Issues

- 별도 문제 없음

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 통합 대상
