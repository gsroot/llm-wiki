---
title: "Dart"
type: entity
entity_type: tool
tags: [dart, programming-language, google, flutter, aot, jit, javascript-compile, wasm, sound-null-safety, isolates]
related:
  - "[[flutter]]"
  - "[[google]]"
  - "[[github]]"
source_count: 1
observed_source_refs: 3
inbound_count: 13
created: 2026-04-27
updated: 2026-04-27
---

# Dart

## 개요

**Dart**는 Google이 2011년 발표한 **객체지향·클래스 기반·null-safe 프로그래밍 언어**다. C 계열 문법과 garbage collection, async/await, 강한 정적 타입 시스템을 갖췄다. 초기에는 JavaScript 대체를 노렸으나, 2017년 [[flutter]] 출시 이후 **Flutter의 유일한 framework 언어**로 정체성이 재정의됐다.

Dart의 가장 독특한 특징은 **4-target compile**: 같은 소스가 (1) AOT — ARM/x64 네이티브 머신코드(iOS/Android/Desktop 릴리스 빌드), (2) JIT — VM 위 실행(개발 시 hot reload), (3) JavaScript 또는 WebAssembly(Web), (4) Snapshot(빠른 시작)으로 컴파일된다. 이 다중 타깃이 Flutter의 멀티플랫폼 약속의 기술 기반.

## 주요 특징

### 4-Target Compile

| 타깃 | 사용 | 특징 |
|------|------|------|
| **AOT (Ahead-Of-Time)** | 릴리스 빌드 (iOS·Android·Desktop) | ARM·x64 머신코드, 빠른 시작·예측 가능한 성능 |
| **JIT (Just-In-Time)** | 개발 빌드 | hot reload (코드 변경 즉시 반영, 상태 보존) |
| **JS / WASM** | Web 빌드 | dart2js 또는 dart2wasm |
| **Snapshot** | CLI 도구·서버 | 즉시 시작 (VM 부팅 우회) |

### Sound Null Safety

Dart 2.12 이후 **sound null safety** 도입:
- 타입에 `?` 명시 없으면 non-nullable
- 컴파일러가 null 흐름을 추적 — 런타임 null check 일부 생략 가능
- Null assertion (`!`)은 명시적 위험 신호. Flutter rules는 "no `!`" 강제

### 동시성 모델: Isolates

- **Isolates** = OS 스레드 위에서 메모리 공유 없는 격리 단위
- 메시지 전달(message passing)로만 통신 — Erlang/Elixir와 유사
- `compute()` 함수로 무거운 작업을 별 isolate에 위임 (Flutter rules 권장)

### 비동기 모델

- `async`/`await` (JavaScript와 유사)
- `Future<T>` (단일 비동기 값) + `Stream<T>` (비동기 시퀀스)
- `try`/`catch`로 예외 전파

### 도구 생태계

- **`dart` CLI**: `dart run`, `dart format`, `dart analyze`, `dart test`, `dart pub`
- **`dart_format`**: 표준 포매터 (논쟁 종료)
- **`dart_analyze --fatal-infos`**: 정적 분석 ([[flutter]]는 always-on rule로 강제)
- **pub.dev**: 패키지 레지스트리 (~수만 패키지, [[flutter]]이 주 소비자)

### 라이선스·거버넌스

- **라이선스**: BSD 3-Clause
- **저장소**: [dart-lang/sdk](https://github.com/dart-lang/sdk) on [[github]]
- **개발 주도**: [[google]] (Dart Team), 외부 컨트리뷰터 다수
- **3개 채널**: `stable`, `beta`, `dev` — Flutter의 release tracking과 동기화

## 관련 개념

- [[flutter]]: Dart의 사실상 단독 대형 사용자. Dart의 거의 모든 진화 방향(sound null safety, hot reload 최적화, isolate 강화)이 Flutter 요구에 맞춰져 있음
- [[google]]: 모기관. Dart Team과 Flutter Team이 동일 조직 내 협력
- [[github]]: dart-lang/sdk와 flutter/flutter 모두 GitHub에 호스팅

## 출처

- [[flutter-flutter]] — Flutter README의 "Dart programming language" 섹션 + `pubspec.yaml` 의존성 + `.agents/rules/dart-editing.md` (always_on 룰: `dart analyze --fatal-infos` + `dart format`) + `docs/rules/rules_1k.md` 압축 룰의 14개 영역(SOLID·async·isolate·null safety 등)에서 Dart 사용 패턴 도출

## 메모

- 석근의 [[backend-python-fastapi]] FastAPI 스택과 결합 시 — 백엔드 Python, 프론트 Dart/Flutter 조합. 두 언어 모두 sound 타입 시스템(Python 3.12+ type hints + Dart sound null safety)이라 LLM 코드 생성 정확도가 높음
- 후속 탐구: (a) Dart의 isolate 모델 vs Python asyncio 비교 — 멀티프로세싱이 필요한 BI 작업에서 Dart 서버사이드(`dart_frog`, `serverpod`) 사용 가능성, (b) WebAssembly 컴파일(dart2wasm) 성숙도 — 현재 Dart 주력 외 WASM 진영(Rust, Go)과 비교 시점
- Dart는 2011년 출시 후 JS 대체 실패 → Flutter에 종속되며 살아남은 케이스. 언어 자체로는 우수하지만, Flutter 외 사용처가 적은 게 함정 (pub.dev 패키지 대부분이 Flutter 의존)
