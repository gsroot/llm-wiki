---
title: "Zustand"
type: entity
entity_type: tool
related:
  - "[[react]]"
  - "[[poimandres]]"
  - "[[flutter-nextjs-fullstack-pattern|React 진영 종합]]"
  - "[[tanstack-query]]"
  - "[[nextjs]]"
  - "[[riverpod]]"
  - "[[pmndrs-zustand]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
tags: [zustand, react, state-management, hooks, flux, minimal, providerless, 22회차]
---

# Zustand

## 개요

React 클라이언트 상태관리 미니멀 챔피언. "Bear necessities" 컨셉으로 provider 래핑 없이 hook 단일 API로 동작. zombie child / context loss / concurrent mode 3대 React 내부 이슈를 정공법으로 해결.

## 주요 특징

| 측면 | 내용 |
|---|---|
| **저자** | Daishi Kato 외 (Poimandres collective) |
| **라이선스** | MIT |
| **Stars** | 57.9K |
| **API** | `create((set) => ({ ... }))` 단일 |
| **No Provider** | 모듈 import만으로 동작 (Redux/Recoil/Jotai 차별점) |
| **번들 크기** | 매우 작음 (cute bear ≠ 실력 부족) |
| **해결 이슈** | zombie child, react concurrency (`useMutableSource`), mixed renderer context loss |
| **AGENTS.md** | ❌ 미채택 |

## React 진영 듀얼 채택 패턴

| 영역 | 라이브러리 | 책임 |
|---|---|---|
| 클라이언트 상태 | **Zustand** | UI 로컬 상태, 사용자 입력, 전역 토글 |
| 서버 상태 | **TanStack Query** | API fetch 캐시, refetch, 동기화 |

→ React 진영 사실상 표준 (Redux + RTK Query 대체).

## 관련 개념

- [[react]] — 호스트 라이브러리
- [[poimandres]] — 운영 collective (react-three-fiber 원조)
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 클라이언트 상태 표준 (22회차 신규)
- [[tanstack-query]] — 서버 상태 보완 도구
- [[nextjs]] — Zustand는 SSR Hydration 안전성 검증 완료
- [[riverpod]] — Flutter 진영 동등 위치 라이브러리

## 의사결정 컨텍스트 (raw 인용)

> "'Bear necessities' 컨셉의 React 클라이언트 상태관리 라이브러리. 57.8K stars · MIT · provider 없는 hook 단일 API로 zombie child / context loss / concurrent mode 문제를 한 번에 해결."
> — [[pmndrs-zustand]] 한줄 요약

[[seokgeun-stack-guide]] React 클라이언트 상태 표준. [[tanstack-query]](서버 상태)와 듀얼 채택이 22회차 결론. [[c2spf-analytics]] React 리뉴얼(2025) 클라이언트 UI 상태 후보. [[matechat]] Flutter 진영 동등 위치는 [[riverpod]]. **providerless 미니멀 API**로 boilerplate 최소화 — [[llm-infra-meta-cluster]] 5축의 minimalist 디자인 철학 사례 ([[redis]] MANIFESTO와 비슷한 opinionated 모델). [[poimandres]] collective 산하.

## 출처

- [[pmndrs-zustand]] — 본 OSS 저장소 (22회차 신규)

## 메모

22회차 (Plan 20회차 / Frontend) 신규 등록. Redux 후속군 중 "providerless" 미니멀 노선 대표. 동등 위치 경쟁자: Jotai (atom 기반), Valtio (proxy 기반), Recoil (Facebook 제외 진영). Zustand가 압도적 1위.
