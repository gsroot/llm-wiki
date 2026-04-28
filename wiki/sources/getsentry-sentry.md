---
title: "Sentry — 에러 트래킹 + 반-fragmentation AGENTS.md SSOT"
type: source
source_type: article
source_url: "https://github.com/getsentry/sentry"
raw_path: "raw/articles/getsentry-sentry/"
author: "Sentry (Functional Software, Inc.)"
date_published: 2026-04-28
date_ingested: 2026-04-28
tags: [sentry, error-tracking, observability, agents-md, anti-fragmentation, viewer-context, 19회차]
related: [[sentry]], [[observability-and-cicd-stack]], [[agent-skills]]
confidence: high
---

# Sentry — 에러 트래킹 + 반-fragmentation AGENTS.md SSOT

## 한줄 요약

> Sentry는 developer-first 에러 트래킹/성능 모니터링 플랫폼이며, AGENTS.md를 "AI agent instruction의 single source of truth"로 강제 선언한 첫 OSS — "CLAUDE.md/Cursor rules에 추가하지 말라"는 **반-fragmentation 룰**이 핵심.

## 핵심 내용

- **AGENTS.md SSOT 강제 선언 (서두)**: "**IMPORTANT**: AGENTS.md files are the source of truth for AI agent instructions. Always update the relevant AGENTS.md file when adding or modifying agent guidance. **Do not add to CLAUDE.md or Cursor rules.**" — 명시적 anti-fragmentation 룰.
- **계층화 AGENTS.md (4-tier)**: 루트 `/AGENTS.md` (overview + 명령) + `src/AGENTS.md` (백엔드 패턴) + `tests/AGENTS.md` (테스트 패턴) + `static/AGENTS.md` (프론트엔드 패턴). 각각 다른 CODEOWNERS 팀이 owner (`@getsentry/dev-infra`, `@getsentry/design-engineering`).
- **`@AGENTS.md` redirect CLAUDE.md**: Grafana와 동일 패턴. CLAUDE.md = 1줄 `@AGENTS.md`. SSOT 일관성 확보.
- **Python 가상환경 강제 (CRITICAL)**: AI agent용 명령 가이드 — `cd /path/to/sentry && .venv/bin/pytest tests/...`. `required_permissions: ['all']` 사용 권고. 직접 `pytest` 호출 금지.
- **Skill 시스템 (`.agents/skills/`)**: 워크플로우 스티어링(commit, pre-commit, hybrid cloud)은 skill로 분리. AGENTS.md = 정적 가이드, skills = 동적 워크플로우. 14회차 OpenAI Agents의 9개 SOP 스킬과 유사 구조.
- **Feature flag 5단계 워크플로우**: ① `temporary.py`에 등록 → ② Python 체크 (`features.has(...)`) → ③ Frontend 체크 (`organization.features.includes(...)`) → ④ Test (`with self.feature(...)`) → ⑤ Rollout (별도 `sentry-options-automator` 레포).
- **PR 분리 룰 강제 (CI 체크)**: "Frontend(`static/`)와 backend(`src/`, `tests/`)는 **atomically deployed되지 않음. CI check enforces this**". Grafana와 동일하지만 CI가 강제.
- **Customer 정보 보호 명시**: AGENTS.md에 "PR/commit/code에 customer 정보 절대 포함 금지" 섹션 — `org-slug`, `user@example.com` 같은 anonymized 예시만 사용. 컴플라이언스 자동화의 단서.
- **Viewer Context contextvar**: `sentry.viewer_context.get_viewer_context()` — org/user identity를 명시적으로 threading하지 말고 contextvar에서 읽으라는 패턴.

## 주요 인사이트

- **반-fragmentation = SSOT 명문화**: "여러 AI agent별 룰 파일(.cursor/, .github/copilot-instructions.md, CLAUDE.md, AGENTS.md)이 동시 존재하면 drift 발생" → **AGENTS.md만 SSOT로 두고 나머지는 redirect**. Sentry가 가장 강력하게 명문화한 첫 사례.
- **9단계 진화 + 10단계 진화 결합**: Sentry = 9단계(`@AGENTS.md` redirect) + 10단계(계층화 4-tier)를 동시 채택. Grafana(9+10단계)와 함께 운영 진영의 새 표준 형성.
- **SOP 스킬 + AGENTS.md 분리**: 14회차 발견 "AGENTS.md = static guide, skills = workflow"가 Sentry에서도 명시적으로 채택 (`.agents/skills/`). 정적/동적 분리는 AGENTS.md 표준의 사실상 두 번째 축.
- **컴투스플랫폼 BI 적용**: 게임 백엔드 에러 추적은 Sentry의 직접 사용 사례. 또한 BI 대시보드 자체의 에러(쿼리 실패, panel 렌더 오류) 추적 가능. Feature flag 5단계 워크플로우 = c2spf-analytics에 적용하면 안전한 점진적 롤아웃 가능.
- **Customer 정보 보호 자동화 단서**: AGENTS.md가 "PR/commit/code 모두 anonymize" 명시 → Pre-commit hook/CI lint로 자동 검증 가능. PHI/PII 컴플라이언스 영역에 직접 응용.

## 관련 엔티티/개념

- [[sentry]]: 본 소스 1차 대상.
- [[grafana]]: 같은 9+10단계 AGENTS.md 진화 패턴 채택.
- [[agent-skills]]: 반-fragmentation 룰을 명문화한 첫 사례.
- [[observability-and-cicd-stack]]: 19회차 에러 추적 레이어.

## 인용할 만한 구절

> "**IMPORTANT**: AGENTS.md files are the source of truth for AI agent instructions. Always update the relevant AGENTS.md file when adding or modifying agent guidance. **Do not add to CLAUDE.md or Cursor rules.**"
> — getsentry/sentry AGENTS.md 서두

> "If your changes touch both frontend and backend, split them into **separate PRs**. Land the backend PR first when the frontend depends on new API changes."
> — AGENTS.md, "Pull Requests" 섹션

> "**Never include customer information in pull requests, commits, or code.** This covers organization slugs, user emails, account names, internal IDs tied to specific customers, support ticket details."
> — AGENTS.md, "Customer Information" 섹션

## 메모

- 256줄(8927 bytes) — 19회차 OSS 중 가장 긴 AGENTS.md. Sentry가 가장 강한 SSOT 의지.
- "viewer_context" 패턴은 c2spf-analytics에 직접 응용 가능 — 사용자/org 식별을 명시적으로 인자로 전달하지 말고 FastAPI dependency injection + contextvar로 처리.
- `prek run -q` (pre-commit 도구) — `pre-commit` 대신 Sentry 자체 fork. 단일 CLI로 lint/format/typecheck 통합. c2spf-analytics에서도 같은 패턴 채택 가치.
- 21회차 점검 시 "AGENTS.md 채택자별 fragmentation 룰 비교 매트릭스" 작성 필요 — Sentry(strict SSOT) / Grafana(silent SSOT) / Pydantic AI(byte-for-byte sync) / Prometheus(PR-pattern only) 4가지 모드.
