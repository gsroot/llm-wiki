---
title: "Flutter + Next.js 듀얼 클라이언트 풀스택 패턴 (22회차 종합)"
type: synthesis
category: frontend-architecture
sources:
  - "[[rrousselGit-riverpod]]"
  - "[[vercel-next.js]]"
  - "[[tanstack-tanstack-query]]"
  - "[[pmndrs-zustand]]"
  - "[[shadcn-ui-ui]]"
  - "[[flutter-flutter]]"
  - "[[matechat]]"
sources_count: 7
related:
  - "[[riverpod]]"
  - "[[nextjs]]"
  - "[[tanstack-query]]"
  - "[[zustand]]"
  - "[[shadcn-ui]]"
  - "[[flutter]]"
  - "[[agent-skills]]"
  - "[[backend-fastapi-stack]]"
  - "[[matechat]]"
created: 2026-04-28
updated: 2026-04-28
tags: [frontend, fullstack, flutter, nextjs, react, state-management, riverpod, zustand, tanstack-query, shadcn-ui, 22회차, 프론트엔드]
---

# Flutter + Next.js 듀얼 클라이언트 풀스택 패턴

## 한줄 요약

22회차에서 수집한 5개 프론트엔드 OSS(Riverpod / Next.js / TanStack Query / Zustand / shadcn-ui)를 통해 **모바일=Flutter+Riverpod / 웹=Next.js+(Zustand+TanStack Query+shadcn-ui)** 듀얼 클라이언트 표준이 형성되었음을 정리. 백엔드는 [[backend-fastapi-stack]]가 양 클라이언트를 동시에 서빙.

## 5개 OSS 메타데이터 비교 매트릭스

| OSS | Stars | License | 영역 | 진영 | AGENTS.md | 거버넌스 모델 |
|---|---|---|---|---|---|---|
| **Next.js** | 139.2K | MIT | SSR/풀스택 프레임워크 | React | ✅ 22KB | Vendor (Vercel) |
| **shadcn-ui/ui** | 113.1K | MIT | UI 컴포넌트 분배 | React | ❌ | **Open Code (10번째 모델)** |
| **Zustand** | 57.9K | MIT | 클라이언트 상태 | React | ❌ | Collective (Poimandres) |
| **TanStack Query** | 49.2K | MIT | 서버 상태 | 멀티 | ❌ | 단일 메인테이너 + 어댑터 |
| **Riverpod** | 7.2K | MIT | 클라이언트+비동기 상태 | Flutter | ❌ | BDFL (Remi Rousselet) |

## 핵심 발견

### 1. AGENTS.md 12단계 진화 — Next.js 단일 OSS에서 양대 변종 동시 발견

22회차 핵심 메타 결론. 21회차 4가지 변종에 이어 12단계 진화의 양대 변종이 Next.js AGENTS.md (22KB / 446줄, = CLAUDE.md symlink) 안에서 동시 등장:

| 단계 | 변종 | 정의 | 발견 OSS | 회차 |
|---|---|---|---|---|
| 11-① | PR-패턴 가이드 | "Recent Learnings" 누적 형식 | Prometheus | 21 |
| 11-② | `@AGENTS.md` redirect CLAUDE.md | CLAUDE.md를 1줄 redirect로 | Grafana, Sentry | 21 |
| 11-③ | 계층화 AGENTS.md | 디렉토리별 AGENTS.md 다층 | Grafana 2-tier, Sentry 4-tier | 21 |
| 11-④ | Anti-fragmentation 명문화 | "여기만이 SSOT" 선언 | Sentry | 21 |
| **12-①** | **`$skill` 인덱싱 (skills hub)** | `$<name>` syntax로 SKILL.md 참조 | **Next.js** | **22** |
| **12-②** | **HTML PR 마커** | LLM 생성 PR 자동 식별 마커 | **Next.js** | **22** |

→ AGENTS.md가 단순 가이드를 넘어 **(a) skills 디렉토리의 인덱스/허브** 그리고 **(b) PR 봇과 연결된 거버넌스 신호 발신기**로 진화.

### 2. AGENTS.md 양극화 가설 보강 — 프론트 진영 채택률 20%

| 진영 | 회차 | 채택 OSS | 미채택 OSS | 채택률 |
|---|---|---|---|---|
| 운영/Observability | 21회차 | Prometheus, Grafana, Sentry | Docker(Moby), GHA | **3/5 = 60%** |
| **프론트엔드** | **22회차** | **Next.js** | **Riverpod, TanStack Query, Zustand, shadcn-ui** | **1/5 = 20%** |

→ 21회차에서 발견한 양극화 가설(운영 OSS는 채택 빠름, 인프라/클라이언트는 늦음)을 추가 데이터로 보강. **프론트엔드 진영의 AGENTS.md 도입은 운영 진영의 1/3 수준**.

### 3. 10번째 OSS 거버넌스 모델 — "Open Code (코드 분배 플랫폼)"

shadcn-ui/ui가 21회차까지 누적된 9개 거버넌스 모델에 추가:

| 모델 # | 모델 | 핵심 패턴 | 대표 OSS |
|---|---|---|---|
| 8 | ASF PMC | 위원회 합의 | Apache Kafka |
| 9 | CNCF graduated | 졸업 후 자율 | Prometheus |
| **10** | **Open Code** | **코드 직접 복사, 의존성 미설치** | **shadcn-ui/ui** |

→ npm install이 아닌 CLI 복사 → 사용자 코드베이스가 fork 결과 → 의존성 업데이트 부재. 21회차 Sentry의 anti-fragmentation 명시화와 정반대로, **의도적 fragmentation을 제도화**한 모델.

### 4. React 진영 듀얼 채택 패턴 (Zustand + TanStack Query)

22회차에서 명확히 정리된 사실상 표준:

| 영역 | 라이브러리 | 책임 |
|---|---|---|
| 클라이언트 상태 | **Zustand** (or Jotai/Valtio) | UI 로컬 상태, 사용자 입력 |
| 서버 상태 | **TanStack Query** | API fetch, 캐시, refetch, mutation |
| UI 컴포넌트 | **shadcn-ui** | Radix UI + Tailwind 조합 |
| 풀스택 프레임워크 | **Next.js** | SSR/SSG/RSC + 라우팅 + API |

→ Redux + Redux Toolkit Query 단일 솔루션 시대를 대체한 **3-축 분리 패턴**.

### 5. Flutter 진영 단일 통합 라이브러리 — Riverpod

React 진영이 4개 라이브러리로 책임 분리하는 것에 비해, Flutter 진영은 [[riverpod]] 하나가:
- 클라이언트 상태 (StateProvider)
- 서버 상태 (FutureProvider, AsyncValue)
- DI (모든 provider가 곧 service locator)

3가지를 통합. → "Flutter는 단일 표준, React는 LEGO" 구도. Mate Chat 프로젝트가 이 구도의 실증 사례.

## 듀얼 클라이언트 통합 시나리오 (석근님 사이드 프로젝트 30분 부트스트랩)

### 시나리오 A: 모바일 우선 (Mate Chat 패턴)

```
Flutter + Riverpod (모바일)
    ↓ HTTP/WS
FastAPI (백엔드, [[backend-fastapi-stack]])
    ↓
PostgreSQL + Redis
```

→ 단일 클라이언트 단순함, App Store 배포, Riverpod 단일 통합. Mate Chat 실증.

### 시나리오 B: 웹 우선 (사이드 프로젝트 권장)

```
Next.js (웹)
  - shadcn-ui (UI)
  - Zustand (클라이언트 상태)
  - TanStack Query (서버 상태)
    ↓ HTTP
FastAPI (백엔드)
    ↓
PostgreSQL + Redis
```

→ 30분 부트스트랩: `npx create-next-app@latest` + `npx shadcn add button` + `npm install zustand @tanstack/react-query` 후 즉시 개발. 스토어 등록 불필요, Vercel 배포 free tier.

### 시나리오 C: 듀얼 클라이언트 (성숙형)

```
Flutter (모바일) + Next.js (웹) + 공통 FastAPI 백엔드
```

→ 두 클라이언트가 동일한 OpenAPI 스키마 공유, 코드 생성 (`openapi-generator` for Dart, `openapi-typescript` for TS) 활용. 단일 백엔드가 양 클라이언트 동시 서빙.

## 컴투스플랫폼 BI 적용 매핑

| 영역 | 22회차 도구 | 적용 사례 |
|---|---|---|
| 사내 대시보드 (웹) | Next.js + shadcn-ui | 게임 데이터 시각화 BI 페이지 |
| 비동기 BigQuery 쿼리 표시 | TanStack Query | 30초+ 걸리는 쿼리의 캐시/refetch |
| 사용자 필터 상태 | Zustand | 기간/게임/지표 필터 클라이언트 보존 |
| 모바일 알림 클라이언트 | Flutter + Riverpod | (가설) BI 임계치 알림 앱 |

## 라이선스 주의

22회차 5개 OSS는 모두 MIT 라이선스 — **상용 통합 부담 없음**. 21회차의 Grafana(AGPL-3.0) / Sentry(BSL→Apache-2.0) 라이선스 주의가 무관. 사이드 프로젝트 / 회사 내부 도구 모두 안전.

## 사용 출처 (22회차 신규 + 기존 통합)

22회차 신규:
- [[rrousselGit-riverpod]]
- [[vercel-next.js]]
- [[tanstack-query]]
- [[pmndrs-zustand]]
- [[shadcn-ui-ui]]

기존 통합:
- [[flutter-flutter]] (20회차) — Flutter 진영 호스트
- [[matechat|MateChat 사이드 프로젝트]] (17~18회차) — Riverpod 실증 프로젝트

## 21회차 종합 (observability-and-cicd-stack)과의 연결

22회차 종합은 **클라이언트 + 백엔드** 흐름을 정리하고, 21회차 종합 [[observability-and-cicd-stack]]은 그 위에 **CI/CD + 관측성**을 덧입힘. 두 종합을 조합하면 사이드 프로젝트의 전체 라이프사이클 (개발 → 빌드 → 배포 → 운영 → 관측) 완성.

## 미래 작업

1. **Plan 21회차 마무리**: [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 작성 시 22회차 5개 도구가 React/Flutter 진영의 핵심 카탈로그로 들어감.
2. **점검 (Lint)**: 위키 깨진 링크 검증 — `[[frontend-flutter-stack]]`, `[[frontend-react-stack]]`, `[[poimandres]]`, `[[radix-ui]]`, `[[tailwindcss]]`, `[[turbopack]]`, `[[tanstack]]` 등이 stub 또는 본 종합 페이지로 redirect 필요.
3. **AGENTS.md 12단계 추적**: Vercel의 다른 OSS (turbo, swr 등)에 `$skill` 인덱싱 + LLM PR 마커 확산 여부 모니터링.
