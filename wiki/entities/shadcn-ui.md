---
title: "shadcn/ui"
type: entity
entity_type: tool
related:
  - "[[react]]"
  - "[[radix-ui]]"
  - "[[tailwindcss]]"
  - "[[vercel]]"
  - "[[frontend-react-stack]]"
  - "[[nextjs]]"
  - "[[agent-skills]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
tags: [shadcn-ui, react, components, tailwind, radix, open-code, code-distribution, 22회차]
---

# shadcn/ui

## 개요

React 컴포넌트 "코드 분배 플랫폼". `npm install` 패키지가 아니라 `npx shadcn add <component>` CLI로 컴포넌트 코드를 직접 사용자 프로젝트에 복사하는 새로운 거버넌스 모델 — "Open Code" 자체 슬로건.

## 주요 특징

| 측면 | 내용 |
|---|---|
| **저자** | shadcn (단일 메인테이너, Vercel 후원 후 채용) |
| **라이선스** | MIT |
| **Stars** | 113.1K (22회차 5개 중 1위) |
| **분배 방식** | CLI를 통한 소스 코드 직접 복사 (의존성 미설치) |
| **기반 스택** | Radix UI (headless) + Tailwind CSS + class-variance-authority |
| **README 길이** | 17줄 (수집 OSS 중 최단 — "코드를 보라" 메시지) |
| **AGENTS.md** | ❌ 미채택 |

## 10번째 OSS 거버넌스 모델 — "Open Code (Code Distribution Platform)"

| 모델 # | 모델 | 대표 OSS | 회차 |
|---|---|---|---|
| 1~7 | Vendor PaaS, ASF PMC, BDFL 등 | (위키 누적) | 1~16회차 |
| 8 | ASF PMC | Apache Kafka, Airflow | 16회차 |
| 9 | CNCF graduated | Prometheus, Kubernetes | 21회차 |
| **10** | **Open Code (코드 분배)** | **shadcn-ui/ui** | **22회차** |

→ npm 의존성이 아닌 사용자 코드 fork → 의존성 업데이트 부재 → 사용자 코드베이스가 SSOT.

## 관련 개념

- [[react]] — 호스트 라이브러리
- [[radix-ui]] — 컴포넌트 동작 layer (headless)
- [[tailwindcss]] — 스타일 layer
- [[vercel]] — 후원사 (shadcn 본인 채용)
- [[frontend-react-stack]] — React 진영 UI 표준 (22회차 신규)
- [[nextjs]] — Next.js 표준 UI 라이브러리로 사실상 등극
- [[agent-skills]] — 10번째 거버넌스 모델 추가 사례

## 출처

- [[shadcn-ui-ui]] — 본 OSS 저장소 (22회차 신규)

## 메모

22회차 (Plan 20회차 / Frontend) 신규 등록. MUI/Chakra/Mantine과 다른 "라이브러리 미설치" 노선. 113K stars로 22회차 1위지만 단일 메인테이너 + Vercel 후원 패턴은 9번째 거버넌스 모델(CNCF 다수 메인테이너) 정반대 끝. Anti-fragmentation의 정반대 = "의도적 fragmentation".
