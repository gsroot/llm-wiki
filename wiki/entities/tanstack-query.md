---
title: "TanStack Query"
type: entity
entity_type: tool
related:
  - "[[react]]"
  - "[[tanstack]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
  - "[[zustand]]"
  - "[[nextjs]]"
  - "[[riverpod]]"
  - "[[tanstack-tanstack-query]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 4
inbound_count: 35
created: 2026-04-28
updated: 2026-04-29
tags: [tanstack-query, react-query, server-state, async-state, multi-framework, 22회차]
---

# TanStack Query

## 개요

서버/비동기 상태 관리 라이브러리. React Query의 후속작으로 React/Solid/Svelte/Vue/Angular 5종 어댑터 제공. 22회차에서 Zustand(클라이언트 상태) + TanStack Query(서버 상태) **듀얼 채택 패턴**의 한쪽 축으로 자리매김.

## 주요 특징

| 측면 | 내용 |
|---|---|
| **저자** | Tanner Linsley + TanStack Team |
| **라이선스** | MIT |
| **Stars** | 49.2K |
| **에코시스템** | TanStack 12 패키지 (Config/DB/DevTools/Form/Pacer/Query/Ranger/Router/Start/Store/Table/Virtual) |
| **어댑터** | `@tanstack/react-query`, `solid-query`, `svelte-query`, `vue-query`, `angular-query-experimental` |
| **핵심 기능** | Protocol-agnostic fetch, 캐싱, refetch, pagination, infinite scroll, mutation, prefetch, cancellation, Suspense |
| **AGENTS.md** | ❌ 미채택 |

## 관련 개념

- [[react]] — 주요 호스트
- [[tanstack]] — 운영 조직
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 표준 (22회차 신규)
- [[zustand]] — 클라이언트 상태 (보완 관계)
- [[nextjs]] — TanStack Query를 SSR과 결합 (Hydration 패턴)
- [[riverpod]] — Flutter 진영 동등 위치 (비동기 caching)

## 의사결정 컨텍스트 (raw 인용)

> "비동기/서버 상태 관리를 위한 React Query 후속작. 49.2K stars · MIT · 멀티 프레임워크(React/Solid/Svelte/Vue/Angular) 지원하며 TanStack 에코시스템 12개 패키지 중 핵심."
> — [[tanstack-tanstack-query]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] React 진영 서버 상태 축. [[zustand]](클라이언트 상태)와 듀얼 채택. SSR/Hydration 시 [[nextjs]]와 결합. [[c2spf-analytics|c2spf 게임 데이터 BI]] React 리뉴얼(2025) BI 대시보드의 BigQuery 비동기 쿼리·캐싱 적용 후보. [[matechat|MateChat 사이드 프로젝트]] 사이드는 Flutter 진영이라 동등 위치 [[riverpod]] 채택. [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 클라이언트 캐싱 패턴 사례 — durable execution(LangGraph)과 다른 stateless caching 모델.

## 출처

- [[tanstack-tanstack-query]] — 본 OSS 저장소 (22회차 신규)

## 메모

22회차 (Plan 20회차 / Frontend) 신규 등록. "서버 상태 vs 클라이언트 상태" 분리 사상의 대표 라이브러리. TanStack 에코시스템 12개 중 query만 49K stars로 단일 메인테이너 → 에코 진화의 모범 사례.
