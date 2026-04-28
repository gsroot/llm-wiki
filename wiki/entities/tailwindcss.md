---
title: "Tailwind CSS"
type: entity
entity_type: tool
tags: [tailwindcss, css, utility-first, atomic-css, shadcn-ui-foundation, 25회차]
related:
  - "[[shadcn-ui]]"
  - "[[react]]"
  - "[[radix-ui]]"
  - "[[nextjs]]"
source_count: 0
created: 2026-04-28
updated: 2026-04-28
---

# Tailwind CSS

## 개요

**Tailwind CSS**는 Adam Wathan이 만든 **utility-first CSS 프레임워크**. `bg-blue-500 px-4 py-2 rounded` 같은 atomic 클래스 조합으로 디자인. 2017 출시 후 React 진영의 사실상 표준 스타일링 전략으로 안착.

본 페이지는 **stub** — Tailwind 저장소가 raw 수집 대상이 아닌 상태에서 22회차 [[shadcn-ui]] / [[nextjs]] 페이지 + 24회차 [[matechat]]에서 참조하므로 정합성 stub으로 등록.

## 핵심 특성

| 항목 | 값 |
|---|---|
| 라이선스 | MIT |
| 회사 | Tailwind Labs |
| 메인 제품 | Tailwind CSS (OSS) + Tailwind UI (상용) + Headless UI (헤드리스 컴포넌트) |
| 빌드 | PostCSS 플러그인 / JIT 모드 (사용된 클래스만 생성) |
| 빌드 도구 | tailwindcss CLI / Vite / Next.js 통합 |

## 본 위키 인용 맥락

- 22회차 [[shadcn-ui]]: `npx shadcn add` 시 Radix Primitive + **Tailwind 클래스** 조합 분배
- 22회차 [[nextjs]] 부트스트랩: `pnpm create next-app --tailwind` 표준 옵션
- 23회차 [[seokgeun-stack-guide]]: 사이드 프로젝트 30분 부트스트랩의 default 스타일 도구

## 관련 개념

- [[shadcn-ui]] / [[radix-ui]] — Tailwind를 활용하는 컴포넌트 layer
- [[react]] — 주된 호스트 진영
- [[nextjs]] — 통합 표준

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[tailwindcss]]` 깨진 링크 발견.
- v4 (2025+) 변화: Rust 기반 Lightning CSS 통합, `@import "tailwindcss"` 단일 줄 설정. [[ruff]] / [[uv]] / [[turbopack]]과 함께 "Rust 가속" 흐름의 일부.
