---
title: "React"
type: entity
entity_type: tool
tags: [react, javascript, ui-library, meta, frontend, hooks, jsx, 23회차, 프론트엔드]
related:
  - "[[nextjs]]"
  - "[[zustand]]"
  - "[[tanstack-query]]"
  - "[[shadcn-ui]]"
  - "[[radix-ui]]"
source_count: 5
observed_source_refs: 13
inbound_count: 35
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 15
---

# React

## 개요

**React**는 Meta(Facebook)가 만든 **UI 라이브러리**. 컴포넌트 + 단방향 데이터 흐름 + Hooks(2019) 기반. 본 위키에서는 22회차 5개 프론트엔드 OSS의 **공통 호스트 진영**으로 인용됨.

본 페이지는 **stub** — React 저장소(facebook/react)가 raw 수집 대상이 아니지만, 22회차 페이지들이 `[[react]]`를 참조하는 빈도를 고려해 정합성 stub으로 등록.

## React 진영 표준 스택 (22회차 정리)

| 영역 | 도구 | 책임 |
|---|---|---|
| 풀스택 프레임워크 | [[nextjs]] | SSR/SSG/RSC + 라우팅 + API Routes |
| 클라이언트 상태 | [[zustand]] | UI 로컬 상태, 사용자 입력 |
| 서버 상태 | [[tanstack-query]] | API fetch, 캐시, refetch, mutation |
| UI 컴포넌트 | [[shadcn-ui]] (코드) + [[radix-ui]] (primitives) + [[tailwindcss]] (스타일) | 분배·접근성·스타일링 |

→ Redux+RTK Query 단일 솔루션을 대체한 **3-축 분리 패턴**. [[flutter-nextjs-fullstack-pattern]] 종합의 핵심 결론.

## Flutter와의 대비

| 진영 | 패턴 | 표현 |
|---|---|---|
| **React** | 4-축 분리 | LEGO — 책임별 라이브러리 조합 |
| **Flutter** | 단일 통합 | [[riverpod]] 하나가 클라이언트+서버+DI 모두 |

## 관련 개념

- [[nextjs]] — React 위에 빌드된 풀스택 프레임워크 표준
- [[zustand]], [[tanstack-query]], [[shadcn-ui]] — React 진영 표준 3축
- [[flutter]] — 대안 진영 (단일 통합 모델)

## 출처

- [[vercel-next.js]] — React 풀스택 프레임워크 축
- [[tanstack-tanstack-query]] — React 서버 상태 축
- [[pmndrs-zustand]] — React 클라이언트 상태 축
- [[shadcn-ui-ui]] — React UI 컴포넌트/Open Code 축
- [[rrousselGit-riverpod]] — Flutter/Riverpod과 React 진영 대비 맥락

## 메모

- 23회차 stub 사유: 22회차 신규 5개 엔티티 페이지가 모두 `[[react]]` 참조. 29회차에 22회차 프론트엔드 source 5개 기반으로 1차 보강.
- 후속 수집 트리거: React 19 (서버 컴포넌트 안정화) 또는 React 자체 AGENTS.md 도입 시 raw 수집으로 1차 소스 등록.
