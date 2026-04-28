---
title: "Sentry"
type: entity
entity_type: tool
tags: [sentry, error-tracking, observability, agents-md, anti-fragmentation, viewer-context, 19회차]
related:
  - "[[grafana]]"
  - "[[docker]]"
  - "[[observability-and-cicd-stack]]"
  - "[[agent-skills]]"
  - "[[devops-cicd]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# Sentry

## 개요

Sentry는 David Cramer(2008, Disqus 사내 프로젝트)가 만든 developer-first 에러 트래킹/성능 모니터링 플랫폼. Functional Software, Inc.가 운영하며 Django + React 모노레포다. 19회차에서 발견된 가장 강력한 **반-fragmentation AGENTS.md SSOT** 사례 — "AGENTS.md is the source of truth, do not add to CLAUDE.md or Cursor rules"를 명문화한 첫 OSS.

## 주요 특징

| 축 | Sentry |
| --- | --- |
| 운영 주체 | Functional Software, Inc. |
| Stars (2026-04) | 43.7K |
| 라이선스 | BSL → Apache-2.0 (3년 후 자동 전환) |
| 백엔드 | Django (Python) + Celery |
| 프론트엔드 | React (TypeScript) |
| 데이터베이스 | PostgreSQL + Clickhouse(분석) |
| AGENTS.md | ✅ 256줄(8927 bytes, 19회차 OSS 중 최장) |
| 반-fragmentation 룰 | "Do not add to CLAUDE.md or Cursor rules" 명시 |
| 계층화 AGENTS.md | 4-tier: `/AGENTS.md` + `src/` + `tests/` + `static/` |
| Skill 시스템 | `.agents/skills/` (워크플로우 동적 가이드) |
| PR 분리 강제 | CI check가 frontend/backend atomically deploy 차단 |

## 관련 개념

- [[grafana]]: 같은 9+10단계 AGENTS.md 진화 패턴 (운영 진영 표준).
- [[docker]]: getsentry/sentry 이미지 + self-hosted Sentry 가능.
- [[observability-and-cicd-stack]]: 19회차 에러 추적 레이어.
- [[agent-skills]]: 반-fragmentation 룰 명문화 첫 사례.
- [[devops-cicd]]: 배포 후 에러 추적의 사실상 표준.

## AGENTS.md SSOT 강제 선언 (19회차 핵심 발견)

Sentry AGENTS.md 서두는 다른 어떤 OSS보다 강력한 명문화:

> **IMPORTANT**: AGENTS.md files are the source of truth for AI agent instructions. Always update the relevant AGENTS.md file when adding or modifying agent guidance. **Do not add to CLAUDE.md or Cursor rules.**

→ 의미: "AI agent별 룰 파일이 분산되면 drift 발생" → AGENTS.md만 SSOT, 나머지는 redirect.

### 4-tier 계층화 AGENTS.md

| 위치 | 영역 | CODEOWNERS 팀 |
| --- | --- | --- |
| `/AGENTS.md` | 루트 (overview + 명령) | `@getsentry/dev-infra` |
| `src/AGENTS.md` | 백엔드 패턴 | (각 backend 팀) |
| `tests/AGENTS.md` | 테스트 패턴 | (각 backend 팀) |
| `static/AGENTS.md` | 프론트엔드 패턴 | `@getsentry/design-engineering` |

### Feature flag 5단계 워크플로우

① `temporary.py` 등록 → ② Python 체크 → ③ Frontend 체크 → ④ Test (`with self.feature(...)`) → ⑤ Rollout (`sentry-options-automator` 별도 레포). c2spf-analytics에 직접 응용 가능.

### Customer 정보 보호 자동화 단서

"PR/commit/code 모두 anonymize" 명시 + `org-slug`/`user@example.com` 같은 anonymized 예시만 사용. Pre-commit hook/CI lint로 자동 검증 가능 → PHI/PII 컴플라이언스에 응용.

## 출처

- [[getsentry-sentry]] — README (62줄) + AGENTS.md (256줄, 8927 bytes) + CLAUDE.md (1줄 redirect) + .github/CONTRIBUTING.md (379 bytes).

## 메모

- BI 적용: 게임 백엔드 에러 추적 1차 사용. BI 대시보드 자체의 에러(쿼리 실패, panel 렌더 오류) 추적 가능.
- `viewer_context` contextvar 패턴 = c2spf-analytics에 응용 가치 — 사용자/org 식별을 명시적 인자 대신 FastAPI dependency injection + contextvar로 처리.
- `prek run -q` (pre-commit fork) — 단일 CLI로 lint/format/typecheck 통합.
- BSL 라이선스 주의: SaaS 형태 재판매 차단. Sentry SaaS와 self-hosted 구분 명확. 3년 후 Apache-2.0 자동 전환 트랙.
