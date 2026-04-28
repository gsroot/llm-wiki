---
title: "vercel/next.js (The React Framework, AGENTS.md 12단계 진화 사례)"
type: source
source_type: article
source_url: "https://github.com/vercel/next.js"
raw_path: "raw/articles/vercel-next.js/"
author: "Vercel"
date_published: 2016-10-25
date_ingested: 2026-04-28
related:
  - "[[nextjs]]"
  - "[[vercel]]"
  - "[[agent-skills]]"
  - "[[react]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
tags: [nextjs, react, vercel, ssr, app-router, turbopack, agents-md, skill-indexing, llm-pr-marker, 22회차]
confidence: high
---

# vercel/next.js 소스

## 한줄 요약

Vercel이 만든 React 프레임워크. 22회차에서 22KB짜리 AGENTS.md(=CLAUDE.md symlink)에서 `$skill` 인덱싱 + `<!-- NEXT_JS_LLM_PR -->` HTML 마커 등 **AGENTS.md 12단계 진화의 핵심 변종 2개**를 발견.

## 핵심 내용

- **저장소**: 139K stars (라이선스 MIT, default branch `canary` — main이 아닌 canary가 활성 브랜치).
- **모노레포 구조**:
  - `packages/next/` — 핵심 프레임워크 (npm `next`)
  - `packages/create-next-app/` — CLI 도구
  - `packages/next-swc/` — Native Rust SWC 바인딩
  - `turbopack/` — Rust 번들러 (git subtree)
  - `crates/` — Next.js SWC용 Rust crates
  - `test/` — 모든 테스트 스위트 (e2e/development/production/unit)
- **AGENTS.md = CLAUDE.md symlink**: 3번째 사례 (이전: PydanticAI, FastMCP). 22KB / 446줄로 수집한 OSS 중 가장 큼.
- **Turbopack 기본 채택**: `next dev`/`next build` 모두 Turbopack이 default. webpack는 `--webpack` 플래그로만.
- **테스트 모드 4종**: `test-dev-turbo`, `test-dev-webpack`, `test-start-turbo`, `test-start-webpack` — 번들러×모드 매트릭스.

## 주요 인사이트

1. **AGENTS.md 12단계 진화 — `$skill` 인덱싱**: Next.js AGENTS.md는 `$pr-status-triage`, `$flags`, `$dce-edge`, `$react-vendoring`, `$runtime-debug`, `$authoring-skills` 6개 스킬을 `$<name>` syntax로 참조. AGENTS.md가 거대 hub로 진화하고 세부 SOP는 `.agents/skills/<name>/SKILL.md`로 분리. 21회차 Sentry/Grafana의 계층화·anti-fragmentation에 이은 새 변종.
2. **AGENTS.md 12단계 진화 — LLM PR HTML 마커**: PR 본문에 `<!-- NEXT_JS_LLM_PR -->` HTML comment 의무화. LLM 생성 PR을 자동 식별·집계하기 위한 거버넌스 신호 — AGENTS.md가 PR 봇과 연결되는 첫 사례.
3. **Anti-pattern 명시 + Secret redaction**: "Never re-run the same test", "Never print secret values", "treat env values as sensitive unless test-mode flags". 21회차 Sentry의 anti-fragmentation에 이은 운영 보안 거버넌스 명문화.
4. **Default branch = canary**: main이 아닌 canary 채택 — 빠른 진화 OSS의 트레이드마크 패턴 (LangChain v1과 동일).

## 관련 엔티티/개념

- [[nextjs]] — 본 도구
- [[vercel]] — 운영 조직 (Vercel Inc.)
- [[react]] — 호스트 라이브러리
- [[agent-skills]] — AGENTS.md 12단계 진화 (`$skill` 인덱싱 + LLM PR 마커)
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 fullstack 표준

## 인용할 만한 구절

> `CLAUDE.md` is a symlink to `AGENTS.md`. They are the same file.

> Use skills for conditional, deep workflows. Keep baseline iteration/build/test policy in this file.
> - `$pr-status-triage` - CI failure and PR review triage with `scripts/pr-status.js`
> - `$flags` - feature-flag wiring across config/schema/define-env/runtime env
> - `$dce-edge` - DCE-safe `require()` patterns and edge/runtime constraints
> - `$react-vendoring` - `entry-base.ts` boundaries and vendored React type/runtime rules

> When writing PR descriptions, you MUST include the following HTML comment at the bottom of the description:
> ```
> <!-- NEXT_JS_LLM_PR -->
> ```

## 메모

22회차 (Plan 20회차 / Frontend) raw 수집. AGENTS.md 12단계 진화의 양대 변종 (`$skill` 인덱싱 + HTML PR 마커)을 단일 OSS에서 발견. 프론트엔드 진영의 유일한 AGENTS.md 채택자(5/1)로서 양극화 가설(운영 60% vs 프론트 20%) 추가 보강.
