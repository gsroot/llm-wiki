---
title: flutter/flutter — 단일 코드베이스 멀티플랫폼 UI SDK + vendor-neutral .agents/ 스킬 표준
type: source
source_type: article
source_url: https://github.com/flutter/flutter
raw_path: raw/articles/flutter-flutter/
author: Google (Flutter Team)
date_published: 2015-03-06
date_ingested: 2026-04-27
tags:
- flutter
- dart
- google
- multiplatform
- ui-toolkit
- mobile
- web
- desktop
- skia
- impeller
- hot-reload
- agent-skills
- agentskills.io
- vendor-neutral
- progressive-disclosure
- claude-code
- gemini
- copilot
related:
- '[[flutter]]'
- '[[dart]]'
- '[[google]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[anthropics-skills]]'
- '[[github-spec-kit]]'
- '[[claude-code]]'
- '[[token-economy]]'
- '[[context-engineering]]'
- '[[github]]'
confidence: high
inbound_count: 32
cited_by:
- '[[agent-skills]]'
- '[[agent-stack-evolution]]'
- '[[anthropics-skills]]'
- '[[c2spf-analytics]]'
- '[[claude-code]]'
- '[[dart]]'
- '[[flutter]]'
- '[[flutter-nextjs-fullstack-pattern]]'
- '[[github-spec-kit]]'
- '[[google]]'
- '[[harness]]'
- '[[llm-infra-meta-cluster]]'
- '[[openai-openai-cookbook]]'
cited_by_count: 13
aliases:
- Flutter
- flutter
- flutter/flutter — 단일 코드베이스 멀티플랫폼 UI SDK + vendor-neutral .agents/ 스킬 표준
---

# flutter/flutter — 단일 코드베이스 멀티플랫폼 UI SDK + vendor-neutral .agents/ 스킬 표준

> [!tldr] 한 화면 요약 (모바일·RAG 첫 청크용)
> Google [[flutter|Flutter]] 멀티플랫폼 UI SDK (★176K / 2015~). 단일 Dart 코드베이스 + Skia/Impeller 엔진. **위키적 핵심**: `.agents/skills/` 3개 SKILL.md 패키지로 [[agent-skills]] 표준 vendor-neutral 채택 (4단계 진화) + `docs/rules/` 4계층 토큰 예산 룰(1K/4K/10K/30K)로 progressive disclosure 토큰 세분화. 본문 423줄 — 빠른 참조는 ## 메타·## 핵심 내용부터.

## 한줄 요약

> Google의 멀티플랫폼 UI SDK(★176,117 / fork 30,289, 2015-03-06 창설). iOS·Android·Web·Windows·macOS·Linux·Fuchsia·임베디드를 **하나의 Dart 코드베이스 + Skia/Impeller 그래픽 엔진**으로 처리하는 framework + engine 통합 저장소. 위키적 측면에서 가장 중요한 발견은 **저장소 자체가 [[agent-skills]] 표준의 vendor-neutral 채택 사례**라는 점 — `.agents/skills/` (agentskills.io 표준 준수)에 3개 SKILL.md 패키지(`find-release`·`rebuilding-flutter-tool`·`upgrade-browser`)를 두고 `.claude/skills` → `../.agents/skills` 심볼릭 링크로 모든 에이전트가 같은 스킬을 공유하게 만듦. 또한 `docs/rules/` 4계층 토큰 예산 룰(rules_1k → rules_4k → rules_10k → rules.md 30K)이 도구별 한계(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K)를 매트릭스로 명시 — **Anthropic의 progressive disclosure를 토큰 단위로 더 세분화한 패턴**.

## 메타

- **저장소**: [flutter/flutter](https://github.com/flutter/flutter)
- **라이선스**: BSD 3-Clause
- **언어**: Dart (framework) + C++/Java/Objective-C (engine)
- **별/포크**: 176,117 / 30,289 (2026-04-27 기준)
- **창설**: 2015-03-06 (Google), 11년차
- **공식 사이트**: <https://flutter.dev>, 문서: <https://docs.flutter.dev>
- **Topics**: android, app-framework, cross-platform, dart, dart-platform, desktop, flutter, fuchsia, ios, linux-desktop, macos, material-design, mobile, mobile-development, skia, web, web-framework, windows
- **저장소 크기**: 440MB (engine 포함)
- **CI/품질 배지**: SLSA Level 1, OpenSSF Best Practices, codecov, LFX Health Score

## 저장소 핵심 디렉토리

| 경로 | 역할 |
|------|------|
| `engine/` | Skia/Impeller 그래픽 엔진 (C++/Java/Objective-C) |
| `packages/` | flutter, flutter_test, flutter_driver, flutter_tools 등 Dart 프레임워크 패키지 |
| `dev/` | 내부 개발 도구·통합 테스트·devicelab 벤치마크 |
| `bin/` | `flutter` CLI 실행 진입점 |
| `examples/` | 공식 예제 앱 (`hello_world`, `flutter_gallery` 외) |
| `docs/` | 컨트리뷰터 위키 (위 GitHub Wiki를 git 추적으로 이전) |
| **`.agents/`** | **vendor-neutral AI 에이전트 룰·스킬 표준 디렉토리** (rules + skills) |
| **`.claude/`** | Claude Code 통합 — `.claude/skills` → `../.agents/skills` 심볼릭 링크 |
| **`.gemini/`** | Gemini 통합 — `config.yaml` + `styleguide.md` |
| **`agent-artifacts/`** | AI 에이전트가 생성하는 임시 산출물 (`.gitignore` 별도) |
| `third_party/` | Skia 등 외부 의존성 |

## 핵심 1 — Flutter의 정체성: "control over every pixel"

README 표제 직하 한 문장: *"Flutter is Google's SDK for crafting beautiful, fast user experiences for mobile, web, and desktop from a single codebase."*

기술 스택 4기둥:

| 기둥 | 구성 | 의미 |
|------|------|------|
| **그래픽** | Skia + Impeller | 하드웨어 가속 2D — Chrome·Android와 같은 엔진. **OEM 위젯을 호출하지 않고 직접 그림** (vs React Native) |
| **언어** | Dart | AOT(ARM·x64 머신코드)·JIT(hot reload)·JS·WASM 4가지 컴파일 타깃 |
| **위젯** | Cupertino + Material + custom | iOS 네이티브 룩(Cupertino) vs 다중 플랫폼 룩(Material), 둘 다 직접 렌더링 |
| **개발자 경험** | stateful hot reload + VS Code/IntelliJ 플러그인 + FFI + platform channels | "Productive development" 슬로건의 실체 |

위키적 의미: **단일 코드베이스 → 모든 플랫폼**의 이상이 (1) Dart의 다중 컴파일 타깃 + (2) Skia/Impeller의 자기-그리기 엔진으로 실제 작동. React Native가 "OEM 위젯 다리"라면 Flutter는 "캔버스 엔진".

## 핵심 2 — Flutter Values: "Build a thing people want"

`docs/about/Values.md` (6.7KB)가 박은 5개 핵심 가치:

| 가치 | 핵심 명제 |
|------|----------|
| 🏗️ **Build the best way to develop UIs** | 생산적·아름답게·빠르게·확장 가능하게 |
| 🔎 **Focus on the user and all else will follow** | "developer's user(=end user)"가 1순위, "developer(=Flutter 사용자)"가 2순위 |
| 📖 **Openness** | "majority of people with commit access are not part of Google's Flutter team" — 외부 컨트리뷰터가 다수 |
| 💫 **Maintaining quality** | **feature-driven, not date-driven** — 이벤트 마감에 맞추지 않음 |
| 🤣 **Have fun doing it** | "bias towards action — better to try something and be wrong, than to plan forever" |

특히 "Levels of support" 섹션이 박은 4단계 차등 지원 모델:

| 레벨 | 약속 | 사례 |
|-----|------|------|
| **0** | 코드까지 같이 도와줌 (top-tier customers) | 매우 드뭄 |
| **1** | well-written code 작동을 best-effort 보장, 테스트 있음 | Android·iOS 64bit ARM (Stable) |
| **2** | 작동하면 운, 안 막지만 적극 보장 X | 32bit iOS, 일부 Linux 배포판 |
| **3** | 작동 무관, 쉬운 패치만 수용 | esoteric SoC, 자체 임베디드 |
| **4** | 패치 거부 | "Rust port of the framework" 같은 로드맵 외 시도 |

위키적 의미: BI 서비스도 "지원 레벨"을 명시화하면 우선순위 분쟁이 사라진다 — 이 모델 차용 가치 있음.

## 핵심 3 — `.agents/`: agent-skills 표준의 vendor-neutral 채택 (위키 핵심)

### 디렉토리 레이아웃

```
.agents/
├── rules/
│   └── dart-editing.md         (309B, trigger: always_on)
└── skills/
    ├── README.md                (3.8KB, 스킬 채택 정책)
    ├── find-release/
    │   └── SKILL.md             (2.1KB)
    ├── rebuilding-flutter-tool/
    │   ├── SKILL.md             (792B)
    │   └── scripts/
    └── upgrade-browser/
        ├── SKILL.md             (4.3KB)
        └── scripts/

.claude/
└── skills -> ../.agents/skills  (17B 심볼릭 링크)

.gemini/
├── config.yaml                  (785B)
└── styleguide.md                (6.9KB)
```

### `.agents/skills/README.md`가 박은 5개 채택 요건

> "1. **Prior Usage**: The skill must have been used by the author. 2. **Target Audience**: explicitly designed for Flutter contributors. 3. **Provide Examples**: PR must include prompts and outputs. 4. **Naming Conventions**: must follow the established **Claude naming conventions** (https://platform.claude.com/...). 5. **Standard Compliance**: must follow the open standard at **https://agentskills.io/specification**."

명시적으로 (1) Anthropic의 Claude naming convention과 (2) agentskills.io 표준을 인용 — agent-skills가 Anthropic 폐쇄 표준이 아니라 **외부 채택 가능한 오픈 표준**임을 Flutter가 공인.

또한 6번째 준-필수 요건: *"Dart Scripts: Scripts should be written in Dart."* — 도메인 일관성 강제.

### 자체 검증 도구: `dart_skills_lint`

```bash
dart run dart_skills_lint:cli --skills-directory ../../.agents/skills \
  --check-trailing-whitespace \
  --check-absolute-paths \
  --check-relative-paths \
  --fix
```

체크 항목:
- 후행 공백 (line-break용 2-space는 예외)
- 절대 경로 링크 금지 → `--check-absolute-paths`
- 상대 경로 링크의 실제 파일 존재 → `--check-relative-paths`
- `--fix-apply`로 자동 수정

위키적 의미: SKILL.md를 코드 자산으로 취급해 **lint·CI·자동 수정 파이프라인**까지 갖춘 첫 사례. anthropics/skills의 "표준" + flutter/flutter의 "검증 도구" = SKILL.md 거버넌스 풀스택.

### 3개 운영 스킬 분석

#### `find-release` (2.1KB)

```yaml
---
name: find-release
description: A skill to find the lowest Dart and Flutter release containing
  a given commit. Use this skill whenever users ask about when a commit
  landed in Flutter or Dart releases, inquire about release versions for
  specific SHAs, or want to know if a commit is included in stable, beta,
  or dev channels for Flutter/Dart projects.
---
```

3단계 워크플로우: (1) commit SHA·channel 추출 → (2) `dart run engine/src/flutter/third_party/dart/tools/find_release.dart --commit=<SHA> --channel=<CHANNEL>` 실행 → (3) "Lowest release tag" 보고. **컨트리뷰터의 반복 질문(이 커밋 언제 stable에 들어갔어?)을 SKILL로 표준화한 것**.

#### `rebuilding-flutter-tool` (792B + scripts/)

flutter CLI 자체를 재빌드하는 절차. 본문은 짧고 `scripts/`로 결정론적 작업을 위임 ([[anthropics-skills]]의 "스크립트 블랙박스 패턴" 사례).

#### `upgrade-browser` (4.3KB + scripts/)

Chrome/Firefox 버전을 Flutter Web Engine + Framework 테스트에서 동시 업그레이드하는 5단계:

1. `dart scripts/fetch_versions.dart latest <chrome|firefox>` — 최신 버전 확인
2. `engine/src/flutter/lib/web_ui/dev/package_lock.yaml` + `.ci.yaml` 업데이트
3. `dev/felt generate-builder-json` — CI config sync
4. `dev/felt test --browser <chrome|firefox>` — 로컬 검증
5. `dart dev/package_roller.dart` — CIPD 업로드 (CIPD 권한 필요 → **사용자 확인** 명시)

위키적 의미: 이 스킬 한 개가 사람 컨트리뷰터의 1-2시간 작업(어떤 파일을 어떻게 고치고 어디로 업로드해야 하는지)을 LLM이 자동 처리하게 만든다. 그러나 단계 5처럼 **권한 필요 시 사용자에게 확인**을 본문에서 명시 — agent autonomy의 적정선.

### `.agents/rules/dart-editing.md` (309B, trigger: always_on)

```markdown
---
trigger: always_on
---

Before declaring a task done:
1. Address all lints, warnings, and errors introduced or present in the modified
   files. Run `dart analyze --fatal-infos <files>` or use the MCP server.
2. Run `dart format` on the modified files. Run `dart format <files>` or use the
   MCP server.
```

모든 LLM 작업이 끝나기 전 강제 실행될 2개 명령. `trigger: always_on` frontmatter는 [[agent-skills]] 페이지에 안 적힌 새 운영 키 — Flutter가 자체 정의한 **rule auto-trigger** 의미론.

## 핵심 4 — `docs/rules/`: 토큰 예산 4계층 룰

`docs/rules/README.md`가 박은 4단계 룰 파일 + 도구별 한계 매트릭스:

| 파일 | 크기 | 대상 도구 |
|------|------|----------|
| `rules.md` | 30,711B | Aider, Cursor, JetBrains AI (제한 없음) |
| `rules_10k.md` | 9,392B | Antigravity 12K limit 대응 |
| `rules_4k.md` | 3,513B | GitHub Copilot 4K hard limit |
| `rules_1k.md` | 799B | OpenAI ChatGPT 1.5K, CodeRabbit 1K hard limit |

도구별 한계 표 (2026-01-05 갱신):

| 도구 | Rules 한계 | 출처 |
|------|----------|------|
| Aider | 제한 없음 | model context window |
| **Antigravity (Google)** | **12,000자 hard** | client-side error message |
| Claude Code | 제한 없음 | `CLAUDE.md` |
| **CodeRabbit** | **1,000자 hard** | "Instructions" field |
| Cursor | 제한 없음 | 500 lines 권장 |
| Gemini CLI | 1M+ 토큰 | model context window |
| **GitHub Copilot** | **4,000자 hard (Code Review)** | Chat ~2 pages |
| Goose | 제한 없음 | summarize/truncate 전략 |
| **OpenAI ChatGPT** | **1,500자 hard** | custom instructions |

### `rules_1k.md` (799B) — 극단 압축 사례

```
**Role:** Expert Dev. Premium, beautiful code.
**Tools:** dart_format, dart_fix, analyze_files.
**Stack:** Nav: go_router, State: ValueNotifier, Data: json_serializable, UI: Material 3
**Code:** SOLID, Layers: Pres/Domain/Data, PascalTypes camelMembers snake_files
**Async:** async/await, try-catch.  **Log:** dart:developer ONLY.  **Null:** sound, no `!`
**Perf:** const everywhere, ListView.builder, compute for heavy
**Testing:** flutter test, integration_test.  **A11y:** 4.5:1 contrast, Semantics
**Design:** "Wow" factor. Glassmorphism, shadows.  **Docs:** Public API ///
```

**14개 영역, 800자 미만**. 모든 약어가 의도적 — "expert dev" 컨텍스트로 LLM이 자연 보간하리란 가정. 위키 운영에 직접 차용 가능한 패턴.

### 위키적 의미: progressive disclosure를 토큰 단위로 세분화

[[anthropics-skills]]의 progressive disclosure는 3-level (메타 → SKILL.md body → references). Flutter는 그 사이를 **rules_1k → 4k → 10k → full**로 4-tier 분할 — 메타-스킬 안에서도 도구별로 다른 깊이를 자동 매칭하는 사상. [[token-economy]] 페이지의 첫 실증.

## 핵심 5 — `agent-artifacts/`: AI 산출물 분리 격리

```
agent-artifacts/
├── .gitignore         (25B — 전부 ignore)
└── README.md          (227B — 용도 설명)
```

별도 디렉토리 + 자체 .gitignore — AI 에이전트가 생성하는 임시 산출물(스케치·계획서·중간 결과)이 **사람의 작업물(commit 대상)과 분리**되도록 강제. Anthropic의 "scratch space" 개념의 코드 표현.

위키적 의미: 위키 운영에도 동일 패턴 차용 가능 — `wiki/scratch/` 또는 `wiki/.agent-artifacts/`를 두면 LLM의 임시 분석 결과가 정식 페이지(entities·concepts·sources)와 섞이지 않음.

## 핵심 6 — `.gemini/styleguide.md`: 멀티 벤더 통합

`.gemini/`는 Google 자체 도구(Gemini Code Assist) 통합:

- `config.yaml` (785B): Gemini 설정
- `styleguide.md` (6.9KB): Flutter Dart 스타일가이드 압축본 — Gemini가 PR 리뷰에 사용

`.claude/skills`가 `../.agents/skills`로 향하는 심볼릭 링크인 이유는 명확: **vendor-neutral 위치(`.agents/`)를 단일 원천으로** 하고, 각 벤더(Claude·Gemini·Codex 등)는 자기 위치에 심볼릭/래퍼만 두면 같은 자산을 본다.

이게 Anthropic의 [[anthropics-skills]] 전략(`.claude/skills/`)과 정면으로 다른 점:

| 진영 | 위치 | 의도 |
|------|------|------|
| Anthropic | `.claude/skills/` | 자기 도구 중심, 다른 벤더는 자기 위치 사용 |
| **Flutter** | **`.agents/skills/`** + 심볼릭 링크들 | **vendor-neutral 단일 원천**, 다른 벤더가 forward |
| GitHub spec-kit (Codex) | `.codex/skills/` (specify 설치 시) | 벤더별 분산 설치 |

## 핵심 7 — Contributing 절차의 "design doc" 강제

`docs/contributing/Design-Documents.md`가 박은 가이드 + `docs/contributing/Tree-hygiene.md` (38KB)가 박은 PR 절차:

1. 사소한 변경 외엔 **design doc** 작성 의무 ([Flutter design doc template](https://flutter.dev/go/template))
2. design doc은 PR 전에 maintainer 검토
3. 4-step contributor 흐름:
 - Engine env setup
 - Framework env setup
 - Tree hygiene (PR landing, code review, breaking changes, regressions)
 - Style guide

위키적 의미: 이 흐름이 [[github-spec-kit]]의 SDD와 본질적으로 같은 사상 — **사양 우선, 코드는 사양의 표현**. spec-kit이 이걸 도구화한 것이라면, Flutter는 11년간 사람 절차로 운영해온 것.

## 주요 인사이트

### 1. agent-skills 표준의 두 번째 외부 채택 — 그러나 다른 길

[[github-spec-kit]] 페이지에서 "Codex Skills 모드 = agent-skills 표준의 첫 외부 채택"이라고 박았다. flutter/flutter는 **두 번째 사례**이지만 **다른 채택 모델**:

| 차원 | spec-kit (Codex) | flutter/flutter |
|------|-----------------|-----------------|
| 위치 | `.codex/skills/` (벤더별) | `.agents/skills/` (vendor-neutral) + 심볼릭 링크 |
| 트리거 | `specify init . --integration codex --integration-options="--skills"` 한 줄 | git에 커밋된 영구 자산 |
| 거버넌스 | spec-kit의 5 templates가 강제 | 자체 README + `dart_skills_lint` 도구 |
| 의도 | "메소드론을 다중 에이전트에 동일 설치" | "에이전트 변경에 무관한 단일 자산 풀" |

**둘 다 agentskills.io 표준을 인용**하지만, spec-kit는 "방법론 → 다중 에이전트 어댑터", Flutter는 "자산 → 다중 에이전트 forwarding". [[agent-skills]] 페이지의 외부 채택 사례 절에 둘 다 박혀야 함.

### 2. `.claude/skills` → `../.agents/skills` 심볼릭 링크의 의미론

표면적으로는 한 줄 hack이지만, 이게 박는 메시지:

> "Anthropic이 정의한 위치 컨벤션(`.claude/skills/`)을 우리는 따르긴 하지만, 우리의 자산은 Anthropic 종속이 아니다. 우리 자산은 vendor-neutral 위치(`.agents/`)에 있고, Claude는 거기로 forwarding된다."

이는 **표준의 거꾸로 읽기**: agent-skills 표준은 SKILL.md 형식만 정의하고 위치는 벤더 자유라면, Flutter는 자기 위치를 정해놓고 벤더들이 거기로 오라고 한다. **표준 채택자가 표준 정의자를 누른 사례**.

### 3. 토큰 예산 매트릭스가 만드는 신호

`docs/rules/` 4계층의 도구별 한계 표(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K)는 단순한 가이드가 아니라 **AI 도구 시장의 현재 상태 스냅샷**이다. 2026-01-05 기준이라 명시. 위키 관점:

- [[claude-code]]·Cursor·Gemini = 사실상 무제한 (모델 컨텍스트 한계)
- Copilot = 4K hard (코드 리뷰)
- ChatGPT custom instructions = 1.5K
- CodeRabbit = 1K

이는 [[token-economy]] 페이지의 새 인사이트: **"룰 파일 한계" 자체가 도구 차별화 축이 됐다**. Flutter처럼 동일 자산을 4단계로 보유하는 패턴이 다른 대규모 OSS에 퍼질 가능성 — 후속 추적 대상.

### 4. Microsoft·Anthropic·Karpathy·GitHub·**Google(Flutter)** 5축

[[agent-stack-evolution]]가 박은 3축에 spec-kit를 추가해 4축이 됐다. Flutter를 추가하면 5축:

| 진영 | 핵심 명제 | 결과물 |
|------|---------|--------|
| Microsoft for-beginners | 단일 운영체계로 학습 콘텐츠 정렬 | 5개 커리큘럼 + co-op-translator |
| Anthropic | 표준은 분리·구현은 cookbook+marketplace | anthropics/skills + claude-cookbooks |
| Karpathy | 최소 하네스로 자율 진화 | autoresearch + nanochat |
| GitHub spec-kit | 메소드론 도구화 + 30+ 에이전트 동일 설치 | spec-kit |
| **Google (Flutter)** | **자산 vendor-neutral화 + 토큰 예산 4계층** | flutter/flutter `.agents/` + `docs/rules/` |

Google의 차별점: **이미 11년 운영한 대규모 OSS가 자기 컨트리뷰터를 위해 agent-skills 표준을 후행 채택**. 새 메소드론 발명이 아니라 기존 거버넌스에 표준 통합.

### 5. Material/Cupertino 이중성과 위젯 카탈로그

Flutter의 위젯 시스템은 **Cupertino**(iOS 룩) + **Material**(다중 플랫폼 룩) + **사용자 정의** 3층. 두 룩이 동시 제공 → 같은 코드베이스에서 플랫폼별 픽셀 퍼펙트.

위키적 의미: **개인 비서 AI 모바일 앱**을 만들 때 Cupertino vs Material 선택이 첫 결정. iOS-only면 Cupertino, cross-platform면 Material. Apple은 자기 플랫폼에서 Cupertino 룩을 권장하지만, Flutter는 둘 다 지원.

### 6. Engine·Framework 분리 절차

`docs/about/The-Engine-architecture.md` (17.7KB) + `docs/about/The-Framework-architecture.md` (468B 매우 짧음) — 엔진은 깊이, 프레임워크 아키텍처는 외부 문서(docs.flutter.dev)에 양보. 컨트리뷰터 환경설정도 이중:

```
1. Setting-up-the-Engine-development-environment.md  (C++/Java/ObjC 컨트리뷰터)
2. Setting-up-the-Framework-development-environment.md  (Dart 컨트리뷰터)
```

하나의 PR이 양쪽을 동시 건드리면 양쪽 절차 모두 거치는 **이중 게이트**. 이게 거대 OSS의 분업 구조.

### 7. "Vibe coding" 안 박았다 — 그러나 실질적으로는 agent-driven

[[github-spec-kit]]는 README 첫 줄에 "vibe coding"을 안티-패턴으로 박았다. flutter/flutter는 그런 명시 발언 없음 — 그러나 (1) `.agents/skills/` 표준 채택, (2) `dart_skills_lint` 자체 검증, (3) `dart-editing.md` always-on 룰을 보면 **agent-driven 방향으로 적극 이동 중**. spec-kit가 메타 메소드론, Flutter는 거대 OSS의 점진적 통합.

## 위키 갱신 포인트

| 페이지 | 갱신 내용 |
|--------|----------|
| 신규 [[flutter]] | tool/framework 페이지 — Skia/Impeller, Dart, 위젯 시스템, .agents/ 채택 |
| 신규 [[dart]] | tool/language 페이지 — AOT/JIT/JS/WASM 4-target, sound null safety |
| 신규 [[google]] | organization 페이지 — Microsoft·Anthropic·GitHub와 균형 |
| [[agent-skills]] | flutter/flutter를 "agent-skills 표준의 두 번째 외부 채택 + vendor-neutral 모델" 사례로 추가 |
| [[harness]] | docs/rules 4계층 토큰 예산 패턴을 progressive disclosure 변종으로 추가 |
| [[agent-stack-evolution]] | 4축 → 5축으로 확장 (Google/Flutter 추가) |
| [[token-economy]] | "룰 파일 한계 = 도구 차별화 축" 시사점 추가, 도구별 한계 매트릭스 |

## 석근 직결 활용 시나리오

1. **개인 비서 AI 모바일 앱 — Flutter 채택 결정**: iOS+Android+Web 3 플랫폼을 단일 코드베이스로 처리. Material 3 + ColorScheme.fromSeed로 다크모드까지 자동. 백엔드는 [[backend-python-fastapi]] FastAPI, 프론트는 Flutter — 회사 BI([[c2spf-analytics|c2spf 게임 데이터 BI]]) React 스택과 다른 선택지를 하나 더 확보.
2. **위키 운영에 `.agents/` 패턴 차용**: 현재 `~/.claude/skills/wiki/SKILL.md`가 운영 중. llm-wiki 저장소 자체에 `.agents/skills/`를 두고 `.claude/skills` 심볼릭 링크 — 회사 맥북·집 윈도우 양쪽에서 git pull만으로 sync. 이미 [[anthropics-skills]] 표준 따르므로 호환.
3. **`docs/rules/` 4계층 토큰 예산을 위키 운영 룰에 적용**: `CLAUDE.md`(현재 ~190줄)가 무거워지면 도구별 한계에 맞춰 `CLAUDE_1k.md`·`CLAUDE_4k.md`·`CLAUDE_10k.md` 분할. CodeRabbit 같은 도구를 쓸 때 자동 매칭.
4. **`agent-artifacts/` 패턴을 위키에 차용**: 현재 LLM이 위키에 직접 쓰는데, 임시 분석은 `wiki/.agent-artifacts/`로 격리하면 정식 페이지와 섞이지 않음. .gitignore로 커밋 차단.
5. **`Values.md` 모델을 c2spf BI 거버넌스에 차용**: "Levels of support" 4단계(0-3 + 4 거부)를 BI 지표·대시보드 카탈로그에 적용 — 어떤 지표는 24/7 보장, 어떤 건 best-effort, 어떤 건 작동만 하면 OK. 우선순위 분쟁 사라짐.
6. **`dart_skills_lint` 패턴을 위키 SKILL.md에 차용**: 위키에도 `.agents/skills/` 두면 자체 lint 도구가 필요. `dart_skills_lint`를 fork해 마크다운 트레일링 공백·상대 경로 검증을 자동화. 회사 맥북·집 윈도우에서 동일하게 작동.

## 인용할 만한 구절

> "Flutter is Google's SDK for crafting beautiful, fast user experiences for mobile, web, and desktop from a single codebase."
> — `README.md` 표제 직하

> "The best way to develop user interfaces is the *productive* way of developing. (...) Caring about the developer means creating a joyful and productive development experience with quick iteration cycles, creating usable, simple, reliable, predictable APIs, giving the developer full access to the underlying platform, and so forth."
> — `docs/about/Values.md`, "Build the best way to develop user interfaces" + "Focus on the user"

> "We are feature-driven, not date-driven: we do not plan work based on deadlines. (...) This means sometimes a feature we intended to announce will slip and not be announced, but we prefer this to announcing a rushed feature."
> — `docs/about/Values.md`, "Maintaining quality"

> "We encourage a bias towards action. It's better to try something and be wrong, than to plan forever and never execute."
> — `docs/about/Values.md`, "Have fun doing it"

> "Standard Compliance: The skill must follow the open standard specification outlined at https://agentskills.io/specification."
> — `.agents/skills/README.md`, "Requirements for New Skill Adoption"

> "Provide Novel Information: Tell the agent what it *needs* to know, not what it already knows. One Skill Per CLI Tool: Create a dedicated skill for each CLI tool. (...) Structure and Rules: Be extremely strict about your style. The more structured and rule-based your instructions are (with a limited number of exceptions), the better. Agents have an exponential reward function for structure."
> — `.agents/skills/README.md`, "Recommended Practices"

> "Before declaring a task done: 1. Address all lints, warnings, and errors introduced or present in the modified files. 2. Run `dart format` on the modified files."
> — `.agents/rules/dart-editing.md` (전문, `trigger: always_on`)

## 메모

- raw 보관 28개 파일: 루트 메타 6종(README·CONTRIBUTING·CODE_OF_CONDUCT·CHANGELOG·LICENSE·pubspec.yaml) + .agents 5종(dart-editing rule + skills README + 3 SKILL.md) + docs/about 5종(Values·Repository-architecture·Glossary·Framework·Engine architectures) + docs/contributing 2종(Design-Documents·Tree-hygiene) + docs/rules 5단계(README + 4 tiers) + docs 2종(README·Self-Service-Index) + .gemini 2종(config·styleguide) + agent-artifacts 2종(README·.gitignore). engine/ C++ 소스, packages/ Dart 소스는 보관 제외 (메타·거버넌스 자료가 위키 관심사).
- README 자체는 짧음(7KB) — 진짜 콘텐츠는 `docs/about/Values.md` + `docs/contributing/Tree-hygiene.md` (38KB)에 있음. 거대 OSS의 표준 분포.
- 후속 탐구 후보: (a) `dart_skills_lint` 소스 코드 1회독 — 마크다운 lint 패턴 추출, (b) `docs/contributing/Tree-hygiene.md` 38KB의 PR 절차 풀파이프라인 vs spec-kit 9 명령 매핑 — 사람 절차의 코드화 흐름, (c) `examples/` 디렉토리에서 단순 앱 1개 골라 위키 페이지(개념·엔티티 변환) 시각화 PoC.
- 2026-04-27 활성: pushed_at 오늘, open_issues 12,587 (대규모 활성 트래픽). v3.x 안정버전 운영 중.
- Flutter는 위키 기존 [[microsoft-for-beginners]]의 `Web-Dev-For-Beginners`나 `ai-agents-for-beginners`와는 매우 다른 결 — Microsoft가 "교육 콘텐츠 정렬", Flutter는 "거대 OSS 자체의 거버넌스". 둘 다 같은 표준(agent-skills)을 채택하지만 적용 도메인이 다름. 이게 표준의 진짜 가치 — 도메인 무관성.
