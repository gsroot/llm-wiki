---
title: "Turbopack"
type: entity
entity_type: tool
tags: [turbopack, vercel, rust, bundler, nextjs, build-tool, 25회차]
related: [[vercel]], [[nextjs]], [[react]]
source_count: 0
created: 2026-04-28
updated: 2026-04-28
---

# Turbopack

## 개요

**Turbopack**은 [[vercel]]이 개발한 **Rust 기반 차세대 번들러**. webpack의 후속작으로 Next.js 13+에서 default branch `canary` 표준 (22회차 [[vercel-next.js]] AGENTS.md 명시 — `next dev --turbo` 기본).

본 페이지는 **stub** — Turbopack 단독 저장소가 raw 수집 대상이 아닌 상태에서 [[nextjs]] 등 22회차 페이지가 참조하므로 정합성 stub으로 등록.

## 핵심 특성

| 항목 | 값 |
|---|---|
| 언어 | Rust |
| 라이선스 | MIT |
| 상위 회사 | [[vercel]] |
| 위치 | `vercel/turborepo` 모노레포 내 `crates/turbopack-*` |
| 비교 도구 | webpack (JS, 전통), [[ruff]] / [[uv]] (Rust 가속의 다른 사례) |

## 본 위키 인용 맥락

- 22회차 [[nextjs]] AGENTS.md: 빌드 명령 `pnpm build` / `pnpm test-{dev,start}-{turbo,webpack}` 4 모드 — Turbopack과 webpack 비교 테스트가 표준 워크플로우
- [[flutter-nextjs-fullstack-pattern]]: React 진영 부트스트랩에서 default 빌더로 등장
- "Rust로 JS 도구를 재작성" 패턴(Ruff/uv/Turbopack)은 22회차까지 누적된 일관 흐름

## 관련 개념

- [[vercel]] — 메인테이너
- [[nextjs]] — 주된 채택자
- [[ruff]] / [[uv]] — Rust 기반 도구 체인의 다른 사례

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[turbopack]]` 깨진 링크 발견. 정합성 보강.
- 후속 트리거: Turbopack 별도 AGENTS.md 또는 1.0 안정화 시 raw 수집 → 1차 source 등록.
