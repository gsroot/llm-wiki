---
title: "TanStack/query (서버 상태 관리의 사실상 표준)"
type: source
source_type: article
source_url: "https://github.com/TanStack/query"
raw_path: "raw/articles/tanstack-query/"
author: "Tanner Linsley + TanStack Team"
date_published: 2019-09-01
date_ingested: 2026-04-28
related:
  - "[[tanstack-query]]"
  - "[[tanstack]]"
  - "[[react]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
tags: [tanstack-query, react-query, server-state, async-state, multi-framework, 22회차]
confidence: high
---

# TanStack/query 소스

## 한줄 요약

비동기/서버 상태 관리를 위한 React Query 후속작. 49.2K stars · MIT · 멀티 프레임워크(React/Solid/Svelte/Vue/Angular) 지원하며 TanStack 에코시스템 12개 패키지 중 핵심.

## 핵심 내용

- **저장소**: 49.2K stars (라이선스 MIT).
- **다중 어댑터**: `@tanstack/react-query`, `@tanstack/solid-query`, `@tanstack/svelte-query`, `@tanstack/vue-query`, `@tanstack/angular-query-experimental` — 코어 + 어댑터 분리 구조.
- **TanStack 에코시스템 12개 패키지**: Config, DB, DevTools, Form, Pacer, Query, Ranger, Router, Start, Store, Table, Virtual.
- **핵심 기능**:
  - Protocol-agnostic fetching (REST/GraphQL/promises)
  - Caching, refetching, pagination & infinite scroll
  - Mutations, dependent queries, background updates
  - Prefetching, cancellation, React Suspense 지원
- **AGENTS.md/CLAUDE.md 미채택**: 22회차 프론트 5개 중 미채택 (Next.js만 채택).

## 주요 인사이트

1. **"서버 상태 vs 클라이언트 상태" 분리 사상**: Zustand/Redux는 클라이언트 로컬 상태 전용이지만 TanStack Query는 "fetch 결과 + 캐시 + 동기화"라는 별도 영역을 담당. → React Query + Zustand 조합이 표준화된 이유.
2. **멀티 프레임워크 어댑터 전략**: Vercel의 Next.js가 React 단일이라면 TanStack은 코어 + 어댑터로 모든 프론트엔드 프레임워크 동시 지원. → 라이브러리 OSS 거버넌스 모델 차별화.
3. **TanStack 12개 패키지 모노레포**: Tanner Linsley 한 명이 시작했지만 query만 49K stars, 전체 합산하면 100K+ stars. 단일 메인테이너 → 에코시스템 진화 사례.

## 관련 엔티티/개념

- [[tanstack-query]] — 본 도구
- [[tanstack]] — 운영 조직
- [[react]] — 주요 호스트
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 표준 fetcher

## 인용할 만한 구절

> An async state management library built to simplify fetching, caching, synchronizing, and updating server state.
>
> - Protocol‑agnostic fetching (REST, GraphQL, promises, etc.)
> - Caching, refetching, pagination & infinite scroll
> - Mutations, dependent queries & background updates

## 메모

22회차 (Plan 20회차 / Frontend) raw 수집. TanStack Query는 React Query → 멀티 프레임워크 확장 → TanStack 에코 12개 진화의 흐름. shadcn-ui와 함께 "프레임워크 비종속" 거버넌스 사례 (shadcn은 코드 복사, TanStack은 어댑터 분리).
