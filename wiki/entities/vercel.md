---
title: "Vercel"
type: entity
entity_type: organization
tags: [vercel, organization, frontend, edge, nextjs, turbopack, AI-SDK, 23회차, 프론트엔드]
related:
  - "[[nextjs]]"
  - "[[turbopack]]"
  - "[[react]]"
  - "[[shadcn-ui]]"
  - "[[agent-skills]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# Vercel

## 개요

**Vercel**은 미국 캘리포니아 기반 **클라우드 PaaS 회사** (구 ZEIT). [[nextjs]] 프레임워크의 모회사이자 메인테이너. 22회차 [[flutter-nextjs-fullstack-pattern]] 종합에서 React 진영 풀스택 표준 발견의 핵심 주체.

## 주요 제품·OSS

| 영역 | 제품 | 라이선스 |
|---|---|---|
| 풀스택 프레임워크 | [[nextjs]] (Next.js) | MIT |
| 빌드 도구 | [[turbopack]] (Rust 기반) | MIT |
| AI 통합 | AI SDK (Vercel AI SDK) | Apache-2.0 |
| 호스팅 | Vercel Platform (PaaS, Edge Network) | 상용 |
| 컴포넌트 | shadcn/ui 후원·연계 ([[shadcn-ui]]) | (간접) |

## 위키에서의 의미

- **22회차 핵심 발견자**: Vercel이 Next.js 저장소에 도입한 (a) `$skill` 인덱싱 syntax + (b) `<!-- NEXT_JS_LLM_PR -->` HTML 마커 = [[agent-skills]] 12단계 진화의 양대 변종을 단일 OSS에서 동시 관찰한 사례.
- **VC-backed + 프레임워크 코어 = AGENTS.md 채택**: 22회차 5개 프론트엔드 OSS 중 Next.js만 AGENTS.md 보유. 양극화 가설(운영 60% vs 프론트 20%)의 단일 채택자로서 회사 운영 모델이 표준 채택을 가속한다는 가설 보강.

## 관련 개념

- [[nextjs]] — Vercel의 주력 OSS 프레임워크
- [[turbopack]] — Vercel의 Rust 기반 빌드 도구 (자체 stub)
- [[agent-skills]] — Next.js AGENTS.md가 표준의 12단계 진화 보임
- [[shadcn-ui]] — Vercel과 별개이지만 Next.js 생태계에서 사실상 표준 UI

## 출처

- [[vercel-next.js]] — Vercel 운영 모델·도구 체계가 Next.js AGENTS.md 446줄에 응축

## 메모

- 회사 BI 사이드/내부 도구를 Next.js + Vercel Hosting으로 30분 부트스트랩하면 free tier로 시연 가능. Vercel Edge Functions로 BigQuery 프록시 패턴 검토 가치 있음.
- 23회차 stub 사유: 22회차 5개 페이지가 `[[vercel]]` 참조했으나 페이지 부재. 마무리 정합성 보강.
