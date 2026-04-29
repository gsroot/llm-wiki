---
title: "Spec Kit (Specify CLI)"
type: entity
entity_type: tool
tags: [spec-kit, specify-cli, github, spec-driven-development, sdd, slash-command, agent-skills, claude-code, copilot, gemini, codex, cursor, multi-agent]
related:
  - "[[github]]"
  - "[[spec-driven-development]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[agent-skills]]"
  - "[[harness]]"
  - "[[agent-patterns]]"
  - "[[anthropics-skills]]"
source_count: 1
observed_source_refs: 3
inbound_count: 20
created: 2026-04-27
updated: 2026-04-27
---

# Spec Kit (Specify CLI)

## 개요

[[github]]이 직접 운영하는 **Spec-Driven Development(SDD) 툴킷**. ★91k+ / fork 7.8k (2026-04-27 기준), MIT, 2025-08 시작, 2026-04-24 v0.8.1. 이름은 두 단위로 분리: **Spec Kit**은 메소드론·템플릿·슬래시 명령의 묶음, **Specify CLI(`specify`)**는 그것을 30+ AI 코딩 에이전트에 설치·관리하는 Python CLI.

## 주요 특징

### 1. 단 한 줄로 30+ 에이전트에 동일 워크플로우 설치

```bash
# 설치
uv tool install specify-cli --from git+https://github.com/github/spec-kit.git@vX.Y.Z

# 프로젝트에 적용 (Claude Code)
specify init . --integration claude --here

# 프로젝트에 적용 (Copilot)
specify init . --integration copilot --here

# Codex CLI는 Skills 모드 가능 (agent-skills 표준)
specify init . --integration codex --integration-options="--skills"
```

지원 에이전트: **Claude Code, Cursor, Copilot, Gemini CLI, Codex CLI, Qwen CLI, Qoder CLI, Tabnine CLI, Kiro CLI, opencode, Pi, Forge, Goose, Mistral Vibe, Windsurf** 외. 각 에이전트의 디렉토리 컨벤션에 맞게 명령 파일을 자동 배포 (`.claude/commands/`, `.cursor/commands/`, `.gemini/commands/`, `.codex/skills/` 등).

### 2. 9개 슬래시 명령 (워크플로우 단위)

| 명령 | 단계 | 핵심 산출 |
|------|------|----------|
| `/speckit.constitution` | 헌법 수립 | `.specify/memory/constitution.md` (9 Articles) |
| `/speckit.specify` | 사양 작성 | `specs/[NNN-branch]/spec.md` |
| `/speckit.clarify` | 마커 해소 | `[NEEDS CLARIFICATION]` 사용자 질의 |
| `/speckit.plan` | 계획 수립 | `plan.md` + `research.md` + `data-model.md` + `contracts/` |
| `/speckit.tasks` | 태스크 분해 | `tasks.md` (`[P]` 병렬 마커) |
| `/speckit.analyze` | 일관성 분석 | spec/plan/tasks 교차 검증 |
| `/speckit.checklist` | 체크리스트 생성 | 도메인별 (보안·접근성·성능…) |
| `/speckit.implement` | 실행 | TDD 코드 + 테스트 |
| `/speckit.taskstoissues` | 발행 | GitHub Issues 자동 생성 |

전체 워크플로우와 메소드론은 [[spec-driven-development]] 페이지 참조.

### 3. 5개 템플릿 (LLM 출력 제약)

`templates/` 디렉토리에 `spec-template.md`, `plan-template.md`, `tasks-template.md`, `constitution-template.md`, `checklist-template.md`. 각 템플릿이 **프롬프트 엔지니어링 정수 7가지 메커니즘**(WHAT/WHY 강제, `[NEEDS CLARIFICATION]` 의무, 자체 체크박스, Phase Gates, 계층적 디테일, 테스트 우선, 추측 차단)을 담고 있음.

### 4. 5가지 Integration Base Class

`AGENTS.md`가 박은 통합 아키텍처:

| Base Class | 출력 | 사례 |
|-----------|------|------|
| `MarkdownIntegration` | `.md` | Claude Code, Cursor, Windsurf |
| `TomlIntegration` | `.toml` | Gemini CLI |
| `YamlIntegration` | `.yaml` | Goose |
| `SkillsIntegration` | `SKILL.md` 패키지 | Codex CLI (--skills) |
| `IntegrationBase` (직접) | 커스텀 | Copilot |

새 통합 추가는 `src/specify_cli/integrations/<key>/__init__.py` 한 파일이면 됨. 대부분의 에이전트는 `MarkdownIntegration`만 상속 (zero override).

### 5. 4층 Override Stack — Templates 우선순위

```
⬆ 1. Project-Local Overrides   (.specify/templates/overrides/)
  2. Presets (HOW 변경)         (.specify/presets/templates/)
  3. Extensions (새 능력)        (.specify/extensions/templates/)
⬇ 4. Spec Kit Core             (.specify/templates/)
```

런타임 첫 매치. Presets는 형식·용어·언어를 바꾸고, Extensions는 새 명령·통합을 추가.

### 6. `extensions/catalog.community.json` — 40+ 커뮤니티 확장

카테고리: `docs`, `code`, `process`, `integration`, `visibility`. Effect: `Read-only`, `Read+Write`. 사례: Jira 통합, Confluence 동기화, Azure DevOps Boards 연동, V-Model 추적성, 보안 게이트, 다국어 spec.

## 위키 맥락에서의 역할

석근에게 spec-kit가 의미 있는 면:

1. **[[harness]] 개념의 반대 극단** — [[autoresearch]] (program.md 한 장 = 최소 하네스) ↔ spec-kit (9 슬래시 + 5 템플릿 + 헌법 = 완전 표준화 하네스). [[harness]] 페이지의 스펙트럼이 양극으로 완성됨
2. **[[claude-code]] + spec-kit 통합 가능** — `specify init . --integration claude`로 Claude Code 프로젝트에 9 명령 추가
3. **[[agent-skills]] 표준의 첫 외부 채택 사례** — Codex Skills 모드가 [[anthropics-skills]] 표준을 그대로 사용
4. **위키 자체에 적용 가능** — `templates/commands/`에 `/wiki-ingest`, `/wiki-lint` 같은 LLM 지침서를 spec-kit 패턴으로 작성하면 CLAUDE.md 워크플로우의 코드화

## 관련 개념

- [[spec-driven-development]]: spec-kit가 강제하는 메소드론 자체
- [[github]]: spec-kit의 운영 조직
- [[harness]]: spec-kit = 메타-하네스 (하네스의 하네스)
- [[agent-patterns]]: spec-kit 단계가 5 패턴을 사전 합성한 결과물 (Prompt Chaining + Evaluator-Optimizer + Parallelization + Routing)
- [[claude-code]]: 30+ 통합 중 1급 시민, `MarkdownIntegration` 상속
- [[claude-agent-sdk]]: spec-kit 워크플로우는 Agent SDK로도 구현 가능
- [[agent-skills]]: Codex Skills 모드가 SKILL.md 패키지 형태로 spec-kit 9 명령 배포
- [[anthropics-skills]]: 표준의 정의자, spec-kit Codex 통합이 첫 외부 채택자

## 출처

- [[github-spec-kit]] — GitHub 공식 저장소 수집 소스 (32개 파일, README 765줄, spec-driven.md 412줄, AGENTS.md 451줄, 9 슬래시 명령 정의 마크다운, 5 템플릿)

## 메모

- spec-kit Python CLI 자체 코드(`src/specify_cli/`)는 raw 보관에서 제외. 메소드론은 마크다운에 다 있음 — Python은 그 마크다운을 어디에 복사할지 결정하는 thin wrapper.
- v0.8.1 기준 CHANGELOG.md가 1,368줄 — 활발한 진화 중. 향후 변경 추적이 의미 있는 자산.
- Specify CLI = "spec-kit 메소드론 배포자"로 정의가 정착하면 `Spec Kit` (방법론 + 템플릿) ↔ `Specify CLI` (배포자) 두 entity 분리도 검토 가능. 현재는 한 페이지로 충분.
- 후속 탐구: (a) `specify init` 대신 raw 파일 복사로 위키에 spec-kit 9 명령을 적용하는 시도, (b) 위키 자체용 `wiki-kit` 메타-도구 가능성 (spec-kit 패턴 차용), (c) Codex Skills 모드 디렉토리 구조 실측.
