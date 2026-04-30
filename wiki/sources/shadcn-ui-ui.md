---
title: shadcn-ui/ui (Open Code 패러다임 — 라이브러리가 아닌 코드 분배)
type: source
source_type: article
source_url: https://github.com/shadcn-ui/ui
raw_path: raw/articles/shadcn-ui-ui/
author: shadcn
date_published: 2023-03-08
date_ingested: 2026-04-28
related:
- '[[shadcn-ui]]'
- '[[radix-ui]]'
- '[[tailwindcss]]'
- '[[react]]'
- '[[flutter-nextjs-fullstack-pattern|React 진영 종합]]'
tags:
- shadcn-ui
- react
- components
- tailwind
- radix
- open-code
- code-distribution
confidence: high
inbound_count: 14
cited_by:
- '[[agent-skills]]'
- '[[flutter-nextjs-fullstack-pattern]]'
- '[[radix-ui]]'
- '[[react]]'
- '[[shadcn-ui]]'
- '[[tailwindcss]]'
cited_by_count: 6
aliases:
- Shadcn Ui
- shadcn ui
- shadcn-ui/ui (Open Code 패러다임 — 라이브러리가 아닌 코드 분배)
- shadcn-ui/ui 소스
---

# shadcn-ui/ui 소스

## 한줄 요약

113K stars · MIT의 React 컴포넌트 "코드 분배 플랫폼". `npm install shadcn-ui` 가 아니라 CLI로 컴포넌트 코드를 직접 프로젝트에 복사하는 새로운 거버넌스 모델 — "Open Code" 라는 자체 슬로건.

## 핵심 내용

- **저장소**: 113.1K stars (라이선스 MIT, 단일 메인테이너 `shadcn`).
- **Open Code 패러다임**: README 본문 첫 줄 "A set of beautifully designed components that you can customize, extend, and build on. Start here then make it your own. Open Source. Open Code. **Use this to build your own component library**."
- **분배 메커니즘**: `npx shadcn add button` 명령으로 컴포넌트 소스를 `components/ui/` 디렉토리에 직접 복사. 라이브러리 의존성이 아닌 **코드 자체**가 사용자 프로젝트에 포함됨.
- **기반 스택**: Radix UI (headless) + Tailwind CSS (styling) + class-variance-authority — 즉 Shadcn은 이 셋의 조합 레시피.
- **README 17줄**: 수집 OSS 중 가장 짧음 (다른 OSS는 100~500줄). → "코드를 보라" 선언.
- **AGENTS.md/CLAUDE.md 미채택**: 프론트 5개 중 미채택.

## 주요 인사이트

1. **새로운 OSS 거버넌스 모델 — "코드 분배 플랫폼"**: 발견된 9개 거버넌스 모델(Vendor PaaS, ASF PMC, CNCF graduated, Functional Software/BSL 등)에 더해 **10번째 모델: 코드 분배 (Open Code)**. npm install이 아닌 CLI 복사 → 사용자 코드베이스가 fork 결과 → 의존성 업데이트 부재.
2. **README의 미니멀리즘**: 17줄짜리 README는 "라이브러리 사용법 문서가 필요 없다"의 메시지. 모든 문서는 ui.shadcn.com 사이트와 복사된 코드 자체에 위임.
3. **113K stars vs 단일 메인테이너**: 5개 중 가장 높은 stars지만 메인테이너는 `shadcn` 1명. (Vercel이 후원). → 9번째 거버넌스 모델 (CNCF) 정반대 끝의 "1인 표준 + 빅테크 후원" 패턴.
4. **Anti-fragmentation의 정반대**: Sentry는 "여러 곳에 같은 내용 쓰지 마" 지침. shadcn은 "모두에게 코드를 복사하게 해라" — 완전한 fragmentation을 의도적으로 채택.

## 관련 엔티티/개념

- [[shadcn-ui]] — 본 도구
- [[radix-ui]] — headless 컴포넌트 기반
- [[tailwindcss]] — 스타일 시스템
- [[react]] — 호스트 라이브러리
- [[flutter-nextjs-fullstack-pattern|React 진영 종합]] — React 진영 UI 표준
- [[agent-skills]] — 10번째 거버넌스 모델 (Open Code) 추가

## 인용할 만한 구절

> A set of beautifully designed components that you can customize, extend, and build on. Start here then make it your own. Open Source. Open Code. **Use this to build your own component library**.

## 메모

raw 수집. shadcn-ui는 React 진영의 컴포넌트 라이브러리 표준 (MUI, Chakra, Mantine 대안). Vercel이 shadcn 본인을 직원으로 채용. 위키 거버넌스 모델 카탈로그에 "Open Code" 추가 — Distribution platform이 새로운 모델로 등극.
