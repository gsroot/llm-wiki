---
title: "Frontend — React"
type: skill
category: frontend
slug: frontend-react
years_of_experience: 6
proficiency: expert
related_stack: [React, TypeScript, Vite, TanStack Query, TanStack Router, Zustand, Mobx, ag-grid, Redux]
tags: [react, typescript, frontend, spa, tanstack]
---

# Frontend — React

## 개요

2019년부터 React 사용. 최근 2025년 애널리틱스 팀 최초의 React 기반 리뉴얼을 주도하며 Vite + TanStack Router/Query + Zustand + ag-grid 현대 스택을 팀 표준으로 정립했다. NFT 마켓·XPLA 플랫폼·CODE 트래블룰 관리 대시보드 등 블록체인/Web3 서비스의 프론트엔드에도 폭넓게 적용한 경험이 있다.

## 프로젝트 증거

| 프로젝트 | 기간 | 역할 | 링크 |
|---------|------|------|------|
| 애널리틱스 React 기반 리뉴얼 | 2025-06 ~ 현재 | FE 리드, React 구조 설계·구축 주도 (476커밋) | [→](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| XPLA 플랫폼 (웹뷰) | 2024-04 ~ 2024-07 | 풀스택, React 웹뷰 페이지 상태 전이 설계·구현 | [→](../20-projects/com2us-platform/2024-04-xpla-platform.md) |
| NFT 마켓 (관리 대시보드 계열 포함) | 2022-05 ~ 2024-03 | NFT 지갑/Discord 연동 프론트 기여 | [→](../20-projects/com2us-platform/2022-05-nft-market.md) |
| CODE 트래블룰 API — 거래소 관리 대시보드 | 2021-10 ~ 2022-06 | Python backend + React frontend 대시보드 | [→](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) |
| ML 유저 예측 프론트엔드 | 2020-08 ~ 2021-09 | React + Mobx 기반 구현 | (old-portfolio.md 참조) |
| 애널리틱스 본체 (초기 화면) | 2017 ~ 2025 | jQuery + Thymeleaf → React 전환 주도 | (old-portfolio.md; Confluence 35568410) |

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| React | expert | 2019년부터 6년, 2025 리뉴얼 팀 표준 주도 |
| TypeScript | proficient | 애널리틱스 리뉴얼·XPLA 플랫폼 등에서 실무 적용 |
| Vite | proficient | 2025 리뉴얼에서 `@vitejs/plugin-react-swc` + `@tanstack/router-vite-plugin` 표준화 |
| TanStack Query / Router | proficient | 2025 리뉴얼 최초 도입, 파일 기반 라우팅·서버 상태 캐싱 일원화 |
| Zustand | proficient | `chartStore.pieVisibility` 등 UI 상태 슬라이스 설계 |
| Mobx | proficient | ML 유저 예측 프로젝트에서 전역 상태 관리 |
| Redux | competent | 이전 프로젝트에서 사용 경험 |
| ag-grid | expert | 차트 테이블 공통 모듈 주도 — 타입별 minWidth / pinning 전략 / fitCellContents (GCPPDT-742) |
| React Hook Form | proficient | 2025 리뉴얼 폼 성능·검증 레이어 |
| Playwright | competent | E2E 회귀(32/32, 22/22) 체계 도입 |

## 대표 성과

- **팀 최초 React 기반 아키텍처 표준화** — Vite + React + TypeScript + TanStack + Zustand + ag-grid 스택 확정, `2025 프론트엔드 개발 가이드라인`(Confluence 35568626) 문서화
- **analytics-frontend 476커밋**(전체 ~24%) — GitHub 레포 인덱스 확인 (`docs/10-sources/com2us-platform/github-c2spf/repos/analytics-frontend.md`)
- **ag-grid 공통 컴포넌트 설계 리드타임**: 2~3일 → **하루 미만**, 반복 개발 시간 50% 이상 절감 (Confluence 170034641 §4.1)
- **팀 전체 프론트엔드 생산성 30~40% 향상 기반 구축** (old-portfolio.md L126 및 Confluence 170034641 §7 일치)
- **GCPPDT-741 차트·측정값 UX 개선**: MR#20/#22 머지, 회귀 테스트 **32/32 통과**, 8종 에러 코드 × **5개 로케일 i18n** (validateExpression 유틸)
- **GCPPDT-742 차트 테이블 가독성**: MR#23/#24 머지, **22/22 테스트 통과**

## 관련 인용 출처

- [old-portfolio.md](../../old-portfolio.md) — React 6년 경험·ML 예측 Mobx·팀 생산성 30~40% 서술 원문
- Confluence 35568626 (2025 프론트엔드 개발 가이드라인)
- Confluence 170034641 (AI 기반 개발 생산성 향상 가이드)
- Confluence 35568410 (애널리틱스 리포트 아키텍처 분석 — 레거시 → React 전환 근거)
- GitHub: [`c2spf/analytics-frontend`](../10-sources/com2us-platform/github-c2spf/repos/analytics-frontend.md)
