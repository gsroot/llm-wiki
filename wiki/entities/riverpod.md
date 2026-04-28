---
title: "Riverpod"
type: entity
entity_type: tool
related:
  - "[[flutter]]"
  - "[[mate-chat]]"
  - "[[seokgeun-kim]]"
  - "[[flutter-nextjs-fullstack-pattern|Flutter 진영 종합]]"
  - "[[zustand]]"
  - "[[tanstack-query]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
tags: [riverpod, flutter, dart, state-management, dependency-injection, reactive, 22회차]
---

# Riverpod

## 개요

Flutter/Dart 진영의 reactive caching + dependency injection 프레임워크. Provider의 후속작으로 같은 저자(Remi Rousselet)가 Provider의 한계를 해결하기 위해 재설계. `pub.dev` Flutter Favorite 인정.

## 주요 특징

| 측면 | 내용 |
|---|---|
| **저자** | Remi Rousselet (Provider 원작자 동일) |
| **라이선스** | MIT |
| **Stars** | 7.2K (낮은 별수 — Dart 단일 진영) |
| **3종 패키지** | `riverpod` (순수 Dart), `flutter_riverpod` (위젯), `hooks_riverpod` (flutter_hooks) |
| **API** | `@riverpod` 어노테이션 + `riverpod_generator` 코드 생성 |
| **3상태 패턴** | `AsyncData` / `AsyncError` / `AsyncLoading` 패턴매칭 |
| **DI 모델** | BuildContext에 의존하지 않는 글로벌 provider container |
| **AGENTS.md** | ❌ 미채택 (22회차 프론트 5개 중 4개 미채택군) |

## 관련 개념

- [[flutter]] — 호스트 프레임워크
- [[mate-chat]] — Riverpod 기반 사이드 프로젝트
- [[seokgeun-kim]] — 사용자 (석근님 Flutter 사이드 프로젝트 핵심 라이브러리)
- [[flutter-nextjs-fullstack-pattern|Flutter 진영 종합]] — Flutter 진영 표준 상태관리 (22회차 신규 종합)
- [[zustand]] — React 진영 동등 위치 라이브러리
- [[tanstack-query]] — Riverpod의 비동기 fetch+cache 기능과 유사 영역

## 출처

- [[rrousselGit-riverpod]] — 본 OSS 저장소 (22회차 신규)

## 메모

22회차 (Plan 20회차 / Frontend) 신규 등록. Flutter 진영 상태관리는 Riverpod 외에 Bloc, GetX, Provider, MobX, Cubit이 경쟁. Riverpod의 "Flutter Favorite" 배지 + 같은 저자라는 정통성이 사실상 표준 후보.
