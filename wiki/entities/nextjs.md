---
title: "Next.js"
aliases: [Next.js, 넥스트JS, next-js]
type: entity
entity_type: tool
related:
  - "[[react]]"
  - "[[vercel]]"
  - "[[turbopack]]"
  - "[[agent-skills]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
  - "[[shadcn-ui]]"
  - "[[zustand]]"
  - "[[tanstack-query]]"
  - "[[vercel-next.js]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 3
inbound_count: 45
created: 2026-04-28
updated: 2026-04-28
tags: [nextjs, react, vercel, ssr, app-router, turbopack, agents-md, skill-indexing]
cited_by_count: 16
---

# Next.js

## 개요

Vercel이 만든 React 프레임워크. `$skill` 인덱싱 + `<!-- NEXT_JS_LLM_PR -->` HTML 마커 등 **AGENTS.md 12단계 진화의 양대 변종**을 단독 OSS에서 발견. 프론트 5개 중 유일한 AGENTS.md 채택자.

## 주요 특징

| 측면 | 내용 |
|---|---|
| **운영 조직** | [[vercel]] (Vercel Inc.) |
| **라이선스** | MIT |
| **Stars** | 139.2K |
| **Default branch** | `canary` (main 아님 — 빠른 진화 OSS 패턴) |
| **번들러** | Turbopack (Rust, 기본) → webpack 폴백 |
| **모노레포** | pnpm workspace + crates (Rust) + turbopack subtree |
| **AGENTS.md** | ✅ 22KB 채택 (= CLAUDE.md symlink, 3번째 사례) |
| **`$skill` 인덱싱** | 6개 SKILL.md 참조 (`$pr-status-triage`, `$flags`, `$dce-edge`, `$react-vendoring`, `$runtime-debug`, `$authoring-skills`) |
| **LLM PR 마커** | PR 본문 `<!-- NEXT_JS_LLM_PR -->` HTML 의무화 |

## AGENTS.md 12단계 진화 표

| 단계 | 변종 | 발견 OSS | |
|---|---|---|---|
| 11-① | PR-패턴 가이드 | Prometheus | |
| 11-② | `@AGENTS.md` redirect CLAUDE.md | Grafana, Sentry | |
| 11-③ | 계층화 AGENTS.md | Grafana 2-tier, Sentry 4-tier | |
| 11-④ | Anti-fragmentation 명문화 | Sentry | |
| **12-①** | **`$skill` 인덱싱 (skills hub)** | **Next.js** | **** |
| **12-②** | **HTML PR 마커** | **Next.js** | **** |

## 관련 개념

- [[react]] — 호스트 라이브러리
- [[vercel]] — 운영 조직
- [[turbopack]] — Rust 기반 번들러 (Next.js 기본)
- [[agent-skills]] — 12단계 진화 사례
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 fullstack 표준
- [[shadcn-ui]], [[zustand]], [[tanstack-query]] — Next.js 상의 표준 React 스택

## 의사결정 컨텍스트 (raw 인용)

> "Vercel이 만든 React 프레임워크. 22KB짜리 AGENTS.md(=CLAUDE.md symlink)에서 `$skill` 인덱싱 + `<!-- NEXT_JS_LLM_PR -->` HTML 마커 등 **AGENTS.md 12단계 진화의 핵심 변종 2개**를 발견."
> — [[vercel-next.js]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] React 진영 풀스택 표준. App Router + Turbopack + SSR/RSC가 [[matechat|MateChat 사이드 프로젝트]]·[[c2spf-analytics|c2spf 게임 데이터 BI]]·[[portfolio]] 양쪽 채택 후보. **AGENTS.md 운영 패턴 학습 자료**로서 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축에도 기여 — `$skill` 인덱싱은 [[agent-skills]] 자동 라우팅의 표준화 사례.

## 출처

- [[vercel-next.js]] — 본 OSS 저장소

## 메모

신규 등록. Next.js는 React 진영의 사실상 표준 SSR/SSG 프레임워크. 정의된 양극화 가설("운영 진영 60% AGENTS.md 채택 vs 프론트 진영 20%")의 유일한 프론트 채택자로서 양극화 보강 데이터.
