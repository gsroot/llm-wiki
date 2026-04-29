---
title: "프론트엔드 (React + TypeScript + Vite + TanStack)"
type: concept
category: web-dev
tags: [frontend, react, typescript, vite, tanstack, zustand, ag-grid, highcharts, mobx, 프론트엔드]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[backend-python-fastapi]]"
source_count: 4
observed_source_refs: 9
inbound_count: 18
created: 2026-04-24
updated: 2026-04-24
---

# 프론트엔드 (React + TypeScript + Vite + TanStack)

## 정의

c2spf 애널리틱스 React 리뉴얼(2025-06~)에서 표준화된 프론트엔드 스택. 모던 React 생태계 핵심 도구를 결합한다: Vite(빌드) · React + TypeScript(코어) · TanStack Router/Query(라우팅·서버 상태) · Zustand(클라이언트 상태) · ag-grid(데이터 그리드) · Highcharts(차트) · React Hook Form · Playwright(E2E).

## 왜 중요한가

- **팀 최초 React 도입** — 기존 jQuery + Mobx 기반 UI에서 React+TS 기반으로 전환. 석근이 아키텍처를 단독 설계하고 "2025 프론트엔드 개발 가이드라인" 문서 발행.
- **팀 프론트엔드 생산성 30~40% 향상 기반** 구축. ag-grid 공통 컴포넌트 설계 리드타임 2~3일에서 하루 미만으로, 반복 개발 시간 50%+ 절감.
- 백엔드 APIResponse·APICode 계약을 직접 소비 — `analytics-common-api`와의 강한 정합.

## 핵심 내용

- **빌드/번들**: Vite (Rollup 기반, ESM 친화). 기존 webpack 환경에서 마이그레이션 시 dev 서버 시작 시간이 큰 폭으로 단축.
- **라우팅·서버 상태**: TanStack Router (타입 안전 라우터), TanStack Query (server-state cache).
- **클라이언트 상태**: Zustand (단순한 store 기반). Mobx는 레거시 ML 예측 모듈에서 유지.
- **데이터 그리드**: AG-grid (Enterprise 기능 활용). 피벗·컬럼 그룹·커스텀 페이징·테이블 전치(transpose) 등 적극 활용.
- **차트**: Highcharts (분석 차트), Plotly (개인 프로젝트).
- **i18n**: 측정값 연산식 에러 8종 × 5개 로케일 다국어 지원.
- **품질**: 회귀 테스트 32/32 · 22/22 통과(GCPPDT-741/742 Story).
- **AI 협업**: Claude Code / Codex CLI / ChatGPT 시나리오 4종 + 프롬프트 템플릿 4종 가이드 제작.

## 실전 적용

- **차트·퍼널·리텐션·대시보드** 4대 분석 기능을 "생성·조회·수정" 구조로 단계적 리뉴얼.
- **공통 컴포넌트 아키텍처** — ag-grid 래핑 컴포넌트, 필터·툴팁·가이드 통합.
- **레거시 동거** — `analytics-frontend` 내에서 신규 React 모듈과 기존 jQuery/Mobx 모듈이 공존, 점진적 이관.
- 개인 프로젝트(트래블메이트 · Mate Chat · 카카오톡 분석)에서는 **Flutter** 사용 (모바일 앱). 하지만 회사 내부에서는 React가 표준.

## 관련 개념

- [[backend-python-fastapi]] — 호출 대상 (APIResponse 계약 소비)
- [[devops-cicd]] — Vite 빌드 → Docker → Jenkins 배포

## 출처

- [[portfolio-seed]] — React/Mobx 진화 타임라인
- [[portfolio-resume-ko]] · [[portfolio-ko]] — 정량 지표(476 커밋, 30~40% 향상)
- [[c2spf-analytics-renewal]] — 리뉴얼 상세

## 열린 질문

- TanStack Router의 타입 안전성과 Zustand의 단순성을 어떻게 조합해 폼 상태를 관리하는지 정형화된 패턴이 있는가?
- ag-grid Enterprise 활용 모듈의 성능 비용은 어떻게 관리되는가?
