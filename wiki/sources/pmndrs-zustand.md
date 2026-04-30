---
title: "pmndrs/zustand (React 클라이언트 상태 관리 미니멀 챔피언)"
type: source
source_type: article
source_url: "https://github.com/pmndrs/zustand"
raw_path: "raw/articles/pmndrs-zustand/"
author: "Daishi Kato + Poimandres"
date_published: 2019-04-15
date_ingested: 2026-04-28
related:
  - "[[zustand]]"
  - "[[poimandres]]"
  - "[[react]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
tags: [zustand, react, state-management, hooks, flux, minimal, 22회차]
confidence: high
inbound_count: 10
cited_by:
  - "[[flutter-nextjs-fullstack-pattern]]"
  - "[[poimandres]]"
  - "[[react]]"
  - "[[zustand]]"
cited_by_count: 4
---

# pmndrs/zustand 소스

## 한줄 요약

"Bear necessities" 컨셉의 React 클라이언트 상태관리 라이브러리. 57.8K stars · MIT · provider 없는 hook 단일 API로 zombie child / context loss / concurrent mode 문제를 한 번에 해결.

## 핵심 내용

- **저장소**: 57.8K stars (라이선스 MIT, Poimandres collective 산하).
- **단일 API**: `create((set) => ({ ... }))` 한 줄로 store 정의 → store 자체가 hook이 됨.
- **공식 차별화 (vs Redux)**:
  - Simple, un-opinionated
  - Hooks 기반
  - **No context provider 래핑 필요**
  - Transient updates (렌더 없이 컴포넌트 갱신 가능)
- **공식 차별화 (vs Context)**:
  - 보일러플레이트 적음
  - 변경된 부분만 리렌더
  - 중앙집중 + action 기반
- **해결한 문제 3종**:
  - Zombie child (react-redux 알려진 이슈)
  - React concurrency (`useMutableSource` RFC)
  - Mixed renderer 간 context loss
- **AGENTS.md/CLAUDE.md 미채택**: 22회차 프론트 5개 중 미채택.

## 주요 인사이트

1. **"Provider 없음"이 USP**: Redux/Recoil/Jotai는 모두 Provider 래핑 필요. Zustand는 모듈 import만으로 동작 → DX 우위.
2. **Bear 컨셉 = 작은 번들 + 큰 발톱**: README 헤드라인 "Don't disregard it because it's cute"는 미니멀리즘 + 깊은 React 내부 이해의 자기과시. Zombie child는 Redux 메인테이너도 fix 못한 이슈를 Zustand가 해결.
3. **TanStack Query와의 보완관계**: 클라이언트 상태(Zustand) + 서버 상태(TanStack Query) 듀얼 채택이 React 진영 사실상 표준. → 22회차 종합 페이지의 핵심 매트릭스.
4. **Poimandres collective**: react-three-fiber, drei 등 React 3D 진영 핵심 collective. Zustand는 collective의 일반 React 진영 진출작.

## 관련 엔티티/개념

- [[zustand]] — 본 도구
- [[poimandres]] — 운영 collective
- [[react]] — 호스트 라이브러리
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 클라이언트 상태 표준
- [[tanstack-query]] — 서버 상태 보완 도구

## 인용할 만한 구절

> A small, fast and scalable bearbones state-management solution using simplified flux principles. Has a comfy API based on hooks, isn't boilerplatey or opinionated.
>
> Don't disregard it because it's cute. It has quite the claws, lots of time was spent dealing with common pitfalls, like the dreaded zombie child problem, react concurrency, and context loss between mixed renderers.

## 메모

22회차 (Plan 20회차 / Frontend) raw 수집. Redux 후속 진영 중 "providerless" 미니멀 노선 대표. Zustand + TanStack Query + shadcn-ui 트리오는 사실상 모던 React 진영의 사이드 프로젝트 1순위 스택.
