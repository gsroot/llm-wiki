---
title: "Radix UI"
type: entity
entity_type: tool
aliases: [Radix UI, Radix, radix-ui, 라딕스 UI, headless React primitives]
tags: [radix-ui, react, primitives, accessibility, headless, shadcn-ui-foundation, 25회차, 50회차]
related:
  - "[[shadcn-ui]]"
  - "[[react]]"
  - "[[tailwindcss]]"
source_count: 1
observed_source_refs: 3
inbound_count: 17
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 5
---

# Radix UI

## 개요

**Radix UI**는 WorkOS가 개발한 **headless React 컴포넌트 primitives** 라이브러리. 스타일이 없는 접근성 우선 (WAI-ARIA 준수) primitives를 제공해 [[shadcn-ui]]가 그 위에 [[tailwindcss]] 스타일링을 얹어 분배하는 패턴의 기반.

본 페이지는 **stub** — Radix UI 단독 저장소가 raw 수집 대상이 아닌 상태에서 22회차 [[shadcn-ui]] / [[react]] 페이지가 참조하므로 정합성 stub으로 등록.

## 핵심 특성

| 항목 | 값 |
|---|---|
| 라이선스 | MIT |
| 메인테이너 | WorkOS (전 ZEIT/Vercel 일부 출신) |
| 패키지 | `@radix-ui/react-*` 30+ primitives (Dialog / Dropdown / Tooltip / Tabs 등) |
| 스타일 | Headless (CSS 미포함) |
| 접근성 | WAI-ARIA 완전 구현 (포커스 트랩, 키보드 네비게이션, 스크린리더) |

## 본 위키 인용 맥락

- 22회차 [[shadcn-ui]] "Open Code" 거버넌스 모델의 기술 기반 — `npx shadcn add button` = Radix Primitive + Tailwind 클래스를 사용자 코드베이스에 복사
- React 진영 4-축 분리 패턴에서 UI 컴포넌트 책임의 1차 layer

## 관련 개념

- [[shadcn-ui]] — Radix 위에 빌드된 분배 플랫폼
- [[react]] — 호스트 라이브러리
- [[tailwindcss]] — 스타일링 보조

## 출처

- [[shadcn-ui-ui]] — shadcn/ui의 Open Code 모델과 Radix Primitive 기반 컴포넌트 분배 맥락

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[radix-ui]]` 깨진 링크 발견. 29회차에 shadcn-ui source 기반으로 1차 보강.
- shadcn-ui와의 관계: shadcn은 Radix를 강제하지 않지만 사실상 표준 의존. 다른 headless 라이브러리(Headless UI / Ariakit)도 가능.
