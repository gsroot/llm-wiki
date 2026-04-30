---
title: Flutter
aliases:
- Flutter
- 플러터
type: entity
entity_type: tool
tags:
- flutter
- dart
- google
- ui-toolkit
- multiplatform
- mobile
- web
- desktop
- skia
- impeller
- hot-reload
- agent-skills
- agentskills.io
- vendor-neutral
- riverpod
- mate-chat
related:
- '[[dart]]'
- '[[google]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[github]]'
- '[[token-economy]]'
- '[[anthropics-skills]]'
- '[[github-spec-kit]]'
- '[[claude-code]]'
- '[[riverpod]]'
- '[[matechat]]'
- '[[flutter-nextjs-fullstack-pattern]]'
- '[[flutter-flutter]]'
- '[[seokgeun-stack-guide]]'
source_count: 1
observed_source_refs: 17
inbound_count: 61
created: 2026-04-27
updated: 2026-04-28
cited_by_count: 21
---

# Flutter

## 개요

**Flutter**는 Google이 개발·유지하는 **멀티플랫폼 UI SDK**다. iOS·Android·Web·Windows·macOS·Linux·Fuchsia·임베디드를 **하나의 [[dart]] 코드베이스 + Skia/Impeller 그래픽 엔진**으로 처리한다. 2015년 출시 이후 11년간 활성 개발 중이며 ★176K(2026-04-27 기준)의 대규모 OSS.

대부분의 cross-platform 프레임워크가 OEM 위젯에 다리(bridge)를 놓는 반면, Flutter는 **자체 그래픽 엔진(Skia → Impeller)으로 직접 픽셀을 그림** — "control over every pixel"이 슬로건. 이 설계 결정이 (1) 플랫폼 간 픽셀 동등성, (2) 새 위젯 즉시 추가 가능, (3) iOS/Android 디자인 가이드(Cupertino/Material) 양쪽 동시 제공을 가능하게 함.

## 주요 특징

### 기술 스택

- **언어**: [[dart]] (AOT/JIT/JS/WASM 4-target compile)
- **그래픽 엔진**: Skia (Chrome·Android와 같은 엔진) + Impeller (iOS Metal 우선)
- **위젯 시스템**: Material 3 (다중 플랫폼 룩) + Cupertino (iOS 룩) + 사용자 정의
- **개발 도구**: stateful **hot reload**, VS Code/IntelliJ 플러그인, `flutter` CLI
- **외부 통합**: FFI (Android·iOS·macOS·Windows), platform channels (네이티브 API), pub.dev (수만 패키지)

### 라이선스·거버넌스

- **라이선스**: BSD 3-Clause
- **저장소**: [flutter/flutter](https://github.com/flutter/flutter) on [[github]]
- **컨트리뷰터 모델**: "majority of people with commit access are not part of Google's Flutter team" — 외부 컨트리뷰터 다수
- **품질 배지**: SLSA Level 1, OpenSSF Best Practices, codecov, LFX Health Score

### 운영 원칙 (`docs/about/Values.md`)

| 가치 | 핵심 명제 |
|------|----------|
| Build the best way to develop UIs | 생산적·아름답게·빠르게·확장 가능하게 |
| Focus on the user | end user 1순위, developer 2순위 |
| Openness | 외부 컨트리뷰터 commit 접근 다수 |
| **Maintaining quality** | **feature-driven, not date-driven** |
| Have fun doing it | "bias towards action" |

### 차등 지원 모델 4단계

| 레벨 | 약속 |
|-----|------|
| 1 | well-written code 작동 보장 (Android·iOS 64bit ARM) |
| 2 | best-effort, 적극 보장 X (32bit iOS 등) |
| 3 | 작동 무관, 쉬운 패치만 수용 (esoteric SoC) |
| 4 | 패치 거부 (로드맵 외 시도) |

### `.agents/`: agent-skills 표준의 vendor-neutral 채택 (위키 핵심 발견)

flutter/flutter 저장소가 채택한 **AI 에이전트 통합 모델**:

```
.agents/
├── rules/dart-editing.md         (always_on trigger)
└── skills/
    ├── README.md                  (agentskills.io 표준 명시 인용)
    ├── find-release/SKILL.md
    ├── rebuilding-flutter-tool/SKILL.md (+ scripts/)
    └── upgrade-browser/SKILL.md (+ scripts/)

.claude/skills -> ../.agents/skills  (심볼릭 링크)
.gemini/styleguide.md (6.9KB)
agent-artifacts/.gitignore (AI 산출물 격리)
```

특징:
- **vendor-neutral 위치**(`.agents/`)를 단일 원천으로 두고 각 벤더(Claude·Gemini·Codex 등)는 자기 위치에서 forwarding
- **agentskills.io 오픈 표준** 명시 인용 — Anthropic 폐쇄 표준이 아님을 공인
- **`dart_skills_lint`** 자체 검증 도구 (--check-trailing-whitespace, --check-absolute-paths, --check-relative-paths, --fix)
- 5개 채택 요건 + Dart 스크립트 도메인 일관성 강제

이는 [[agent-skills]] 표준의 **두 번째 외부 채택 사례** ([[github-spec-kit]]의 Codex Skills 모드가 첫 번째). 그러나 채택 모델이 다름: spec-kit는 "메소드론을 다중 에이전트에 동일 설치", Flutter는 "자산을 vendor-neutral화하고 다중 에이전트가 forwarding".

### `docs/rules/`: 토큰 예산 4계층 룰

도구별 룰 한계에 맞춰 동일 룰을 4단계로 보유:

| 파일 | 크기 | 대상 |
|------|------|------|
| `rules.md` | 30,711B | Claude Code, Cursor, Aider (제한 없음) |
| `rules_10k.md` | 9,392B | Antigravity 12K |
| `rules_4k.md` | 3,513B | GitHub Copilot 4K |
| `rules_1k.md` | 799B | OpenAI 1.5K, CodeRabbit 1K |

[[anthropics-skills]]의 progressive disclosure를 토큰 단위로 더 세분화한 패턴. [[token-economy]] 페이지의 첫 실증.

## 관련 개념

- [[dart]]: Flutter의 유일한 framework 언어. 4-target compile (AOT/JIT/JS/WASM)이 멀티플랫폼의 기술 기반
- [[agent-skills]]: Flutter가 `.agents/skills/`로 채택한 표준. SKILL.md 패키지 + agentskills.io 오픈 표준
- [[harness]]: Flutter `.agents/` + `docs/rules/`가 "vendor-neutral 자산 + 토큰 예산 4계층"의 거대 OSS 거버넌스 사례
- [[token-economy]]: rules_1k → 4k → 10k → full 4계층은 토큰 예산 차별화의 첫 대규모 OSS 사례
- [[github-spec-kit]]: agent-skills 표준의 다른 외부 채택 사례 — 두 모델 비교 가능 (메소드론 vs 자산)
- [[anthropics-skills]]: 표준의 정의자. Flutter는 그 표준을 채택하면서도 위치 컨벤션은 자체 결정

## 의사결정 컨텍스트 (raw 인용)

> "Google의 멀티플랫폼 UI SDK(★176K). iOS·Android·Web·Windows·macOS·Linux를 단일 Dart 코드베이스로 처리. 위키적으로 가장 중요한 발견은 저장소 자체가 agent-skills 표준의 vendor-neutral 채택 사례 — `.agents/skills/` (agentskills.io 표준)에 3개 SKILL.md + `.claude/skills` 심볼릭 링크. `docs/rules/` 4계층 토큰 예산 룰(rules_1k → rules_4k → rules_10k → rules.md 30K)이 도구별 한계를 매트릭스로 명시 — Anthropic의 progressive disclosure를 토큰 단위로 더 세분화."
> — [[flutter-flutter]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 모바일·멀티플랫폼 UI 표준. [[matechat|MateChat 사이드 프로젝트]] Google Play 출시(v1.0.0) 본진 채택 — 39 SKILL 운영의 클라이언트 진영. **vendor-neutral agentskills.io 표준 + 4계층 토큰 예산**은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 [[agent-skills]] 8단계 진화 핵심 사례. [[riverpod]] 상태관리 + [[dart]] 언어 + Skia/Impeller 그래픽.

## 출처

- [[flutter-flutter]] — 본 엔티티의 1차 소스. README, Values, .agents/skills 정책, docs/rules 4계층, agent-artifacts 패턴, 5 가치 + 4단계 지원 모델 모두 포함

## 메모

- 석근의 **개인 비서 AI 모바일 앱** 후보 1순위 — iOS+Android+Web 3 플랫폼 단일 코드베이스. 백엔드 [[backend-python-fastapi]] FastAPI + 프론트 Flutter 조합으로 회사 BI([[c2spf-analytics|c2spf 게임 데이터 BI]]) React 스택과 별개의 개인 프로젝트 스택 형성 가능
- Flutter의 `.agents/` 패턴을 llm-wiki 자체에 차용 검토 가치 있음 — 회사 맥북·집 윈도우 양쪽에서 git pull만으로 SKILL 자산 sync
- "feature-driven, not date-driven" 사상은 BI 운영에도 차용 가능 — 분기 OKR 기반 관행과 충돌하지만, 품질 우선 원칙으로 일부 핵심 지표에는 적용 가능
- 후속 탐구: (a) Flutter `examples/` 단순 앱 1개로 위키 페이지 시각화 PoC, (b) `dart_skills_lint` 소스 1회독, (c) Cupertino vs Material 선택 기준 정리
