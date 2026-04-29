---
title: "rrousselGit/riverpod (Flutter Favorite)"
type: source
source_type: article
source_url: "https://github.com/rrousselGit/riverpod"
raw_path: "raw/articles/rrousselGit-riverpod/"
author: "Remi Rousselet"
date_published: 2019-12-01
date_ingested: 2026-04-28
related:
  - "[[riverpod]]"
  - "[[flutter]]"
  - "[[matechat]]"
  - "[[flutter-nextjs-fullstack-pattern|Flutter 진영 종합]]"
tags: [riverpod, flutter, dart, state-management, reactive, dependency-injection, 22회차]
confidence: high
cited_by:
  - "[[flutter-nextjs-fullstack-pattern]]"
  - "[[react]]"
  - "[[riverpod]]"
---

# rrousselGit/riverpod 소스

## 한줄 요약

Flutter 공식 Favorite 패키지로 인정받은 reactive caching + dependency injection 프레임워크. `Provider`의 후속작이며 `@riverpod` 코드 생성 어노테이션과 `AsyncValue` 패턴으로 비동기 로딩/에러 상태를 패턴매칭으로 처리한다.

## 핵심 내용

- **저장소**: 7.2K stars (라이선스 MIT, Dart/Flutter 단일 생태계 한정).
- **3가지 패키지**: `riverpod` (순수 Dart), `flutter_riverpod` (위젯 통합), `hooks_riverpod` (flutter_hooks 통합).
- **Flutter Favorite 인정**: pub.dev/flutter.dev에서 Favorite 배지를 부여한 패키지로, 사실상 Flutter 진영의 표준 상태관리 후보.
- **저자**: Remi Rousselet — Provider의 원작자이기도 함. Riverpod는 Provider의 한계(BuildContext 의존성, late binding 오류)를 해결하기 위한 재설계.
- **`@riverpod` 코드 생성**: `riverpod_generator` 패키지가 어노테이션을 컴파일타임에 풀어 provider 보일러플레이트를 제거.
- **AsyncValue 패턴**: switch-case 패턴매칭으로 `AsyncData(:final value)` / `AsyncError(:final error)` / `AsyncLoading` 3상태를 한 번에 처리.

## 주요 인사이트

1. **Provider의 후속작이라는 정통성**: 같은 저자가 Flutter 진영에서 Provider를 만든 후 한계를 인식하고 재설계. → 진영 내 표준 후보 중 가장 신뢰받는 라인.
2. **Flutter Favorite 배지의 의미**: pub.dev에서 단순 인기와 별개로 "Flutter 팀 권장" 신호. RxDart 등은 Favorite 미보유.
3. **AGENTS.md/CLAUDE.md 미채택**: 22회차 5개 프론트엔드 OSS 중 Next.js만 AGENTS.md 채택. Riverpod/TanStack/Zustand/shadcn-ui 모두 미채택 — 프론트엔드 진영 채택률 1/5 (20%, 운영 진영 3/5의 절반 이하).

## 관련 엔티티/개념

- [[riverpod]] — 본 도구
- [[flutter]] — 호스트 프레임워크
- [[matechat|MateChat 사이드 프로젝트]] — Riverpod 기반 사이드 프로젝트
- [[agent-skills]] — AGENTS.md 미채택 사례 12단계 진화
- [[flutter-nextjs-fullstack-pattern|Flutter 진영 종합]] — Flutter 진영 표준 상태관리

## 인용할 만한 구절

> Riverpod makes working with asynchronous code a breeze by:
> - Handling errors/loading states by default. No need to manually catch errors
> - Natively supporting advanced scenarios, such as pull-to-refresh
> - Separating the logic from your UI
> - Ensuring your code is testable, scalable and reusable

## 메모

22회차 (Plan 20회차 / Frontend) raw 수집. Provider 진영 표준 후보이지만 GetX, Bloc, Cubit 등 경쟁자 다수 존재. Mate Chat 프로젝트가 Riverpod를 채택했기 때문에 석근님의 Flutter 사이드 프로젝트 의사결정에서 핵심.
