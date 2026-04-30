---
title: TanStack
type: entity
entity_type: organization
aliases:
- TanStack
- tanstack
- 탄스택
- Tanner Linsley
- TanStack 진영
tags:
- tanstack
- react
related:
- '[[tanstack-query]]'
- '[[react]]'
- '[[tanstack-tanstack-query]]'
source_count: 1
observed_source_refs: 3
inbound_count: 12
created: 2026-04-28
updated: 2026-04-29
cited_by_count: 4
---

# TanStack

## 개요

**TanStack**은 Tanner Linsley가 운영하는 **헤드리스 OSS 패키지 모음**. [[tanstack-query]] 외에 12개 이상의 멀티 프레임워크 헤드리스 라이브러리(Table / Router / Form / Virtual / Ranger 등)를 동일 메인테이너 + 어댑터 전략으로 통합.

본 페이지는 **stub** — TanStack 조직 페이지가 raw 수집 대상이 아닌 상태에서 [[tanstack-query]] / [[tanstack-query]] source 페이지가 참조하므로 정합성 stub으로 등록.

## 12+ 패키지 생태계

| 패키지 | 책임 |
|---|---|
| [[tanstack-query]] | 서버 상태·async state |
| TanStack Table | 헤드리스 테이블 (정렬·필터·페이지네이션) |
| TanStack Router | 타입 안전 라우팅 (TS-first) |
| TanStack Form | 폼 상태·검증 |
| TanStack Virtual | 가상 스크롤 |
| TanStack Ranger | 다중 슬라이더 |
| TanStack Store | 미니멀 상태관리 (Zustand 대안) |
| TanStack DB / Pacer / Match-sorter / Config / Devtools / Start | 보조 도구 |

## 거버넌스

- 단일 메인테이너 (Tanner Linsley) + 어댑터 전략 — React/Solid/Svelte/Vue 4 프레임워크 동시 지원
- 후원 모델: GitHub Sponsors + Open Collective + Vercel 부분 협력
- 누적 10 거버넌스 모델 중 **단독 메인테이너 모델의 대표** (Daishi의 [[zustand]]와 비슷, [[shadcn-ui]] (단독)과 다른 점은 12+ 패키지 폭)

## 관련 개념

- [[tanstack-query]] — 본 조직 대표 OSS
- [[react]] — 주된 호스트 (멀티 프레임워크 어댑터로 진영 횡단)

## 출처

- [[tanstack-tanstack-query]] — TanStack Query와 TanStack 12+ 패키지 생태계

## 메모

- stub 사유: 점검에서 `[[tanstack]]` 깨진 링크 발견. TanStack Query source 기반으로 1차 보강.
- 후속: TanStack Router (타입 안전 라우팅) 또는 TanStack Form은 [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] React 진영 부트스트랩에 추가 검토 가치.
