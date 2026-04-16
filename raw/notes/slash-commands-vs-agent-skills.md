# Claude Code: Slash Commands vs Agent Skills — 비교·판단

> 2026-04-16, Claude Code(Opus 4.6) 세션에서 "개인 위키 조회용 도구를 어느 쪽으로 만들지"
> 질문에 대한 조사·분석 결과. 공식 문서(`https://code.claude.com/docs/en/skills`,
> `https://code.claude.com/docs/en/slash-commands`) 2026-04-16 접근 기준.

## 핵심 발견: 두 기능은 이미 통합됐다

공식 문서 원문:

> **Custom commands have been merged into skills.** A file at `.claude/commands/deploy.md`
> and a skill at `.claude/skills/deploy/SKILL.md` both create `/deploy` and work the same way.
> **Skills are recommended** since they support additional features like supporting files.

정리:

- 두 파일 모두 `/skill-name` 으로 호출된다
- 기존 `.claude/commands/*.md` 파일은 호환성 유지 차원에서 계속 작동
- Anthropic의 명시적 권장 방향은 **Skills**
- Claude Code Skills는 [agentskills.io](https://agentskills.io) 오픈 표준을 따름

## 두 방식의 실제 차이

| 기능 | `.claude/commands/*.md` | `.claude/skills/*/SKILL.md` |
|------|------------------------|----------------------------|
| `/command-name` 호출 | ✅ | ✅ |
| `$ARGUMENTS`, `$0`, `$1` 치환 | ✅ | ✅ |
| YAML frontmatter | ✅ | ✅ |
| 자동 호출 (모델 판단) | ❌ | ✅ (description 기반) |
| supporting files (reference.md, scripts/) | ❌ | ✅ |
| progressive disclosure (본문은 호출 시에만 로드) | 부분적 | ✅ |
| `context: fork` (서브에이전트 격리) | ❌ | ✅ |
| `paths` (특정 파일 경로에서만 활성) | ❌ | ✅ |
| `` !`command` `` 동적 context injection | ✅ | ✅ |
| `allowed-tools` 툴 권한 선언 | ✅ | ✅ |

## Skills가 특히 유리한 4가지 이유 (지식 조회 용도 관점)

### 1. 자동 호출 — "질문하면 자동으로 따라오는 지식"

Slash command는 반드시 `/command-name`으로 명시 호출해야 한다. Skill은 description에
"관련 질문일 때 사용"을 선언하면 Claude가 판단하여 자동 호출. 이게 진짜 "RAG처럼"의
핵심에 가깝다.

### 2. Supporting files로 노하우 패키징

```
wiki-lookup/
├── SKILL.md               # 핵심 지침 (짧게)
├── query-patterns.md      # 질의 유형별 접근법
└── scripts/
    └── wiki-stats.sh      # 보조 스크립트
```

SKILL.md를 짧게 유지하고 상세는 필요할 때만 로드 = 토큰 경제학 원칙. 공식 팁:
"Keep SKILL.md under 500 lines."

### 3. `context: fork`로 조회를 메인 컨텍스트와 격리

여러 페이지를 Read해도 메인 세션 컨텍스트가 오염되지 않음. 서브에이전트가 조회하고
결과만 돌려줌. 하네스의 "세션 분리" 원칙에 정합.

### 4. `paths`로 자동 호출 조건 제한

예: `paths: ["**/*.md", "**/docs/**"]` — 문서 작업 중에만 자동 후보에 오름.
코드 작성 중에는 방해 안 함.

## Skill 저장 위치 (우선순위)

```
Enterprise  >  Personal (~/.claude/skills/)  >  Project (.claude/skills/)  >  Plugin
```

- **Personal scope**: 모든 프로젝트에서 자동 사용. 개인 도구용 기본 선택
- **Project scope**: 해당 프로젝트에서만. 팀 공유 시 Git 커밋
- **Plugin**: `plugin-name:skill-name` 네임스페이스, 충돌 없음

## SKILL.md Frontmatter 전체 필드

| 필드 | 필수 | 설명 |
|------|------|------|
| `name` | No | 생략 시 디렉토리명 사용. 소문자·숫자·하이픈 (최대 64자) |
| `description` | 권장 | Claude가 자동 호출 판단 기준. 1,536자 capped |
| `when_to_use` | No | description에 덧붙일 추가 트리거 문구 |
| `argument-hint` | No | 자동완성 힌트. 예: `[issue-number]` |
| `disable-model-invocation` | No | `true`면 자동 호출 차단 (수동 `/name` 만) |
| `user-invocable` | No | `false`면 `/` 메뉴에서 숨김 (Claude만 사용) |
| `allowed-tools` | No | 권한 요청 없이 쓸 수 있는 툴 선언 |
| `model` | No | 이 skill 활성 시 사용할 모델 |
| `effort` | No | `low`/`medium`/`high`/`max` |
| `context` | No | `fork` 지정 시 서브에이전트 격리 실행 |
| `agent` | No | `context: fork` 시 사용할 서브에이전트 유형 (`Explore`, `Plan`, `general-purpose` 등) |
| `hooks` | No | skill 수명주기 hooks |
| `paths` | No | 자동 호출을 제한할 glob 패턴 |
| `shell` | No | `` !`...` `` 실행 쉘 (`bash`/`powershell`) |

## 문자열 치환 변수

| 변수 | 설명 |
|------|------|
| `$ARGUMENTS` | 전체 인자 |
| `$ARGUMENTS[N]`, `$N` | 개별 인자 (0-based) |
| `${CLAUDE_SESSION_ID}` | 현재 세션 ID (로그 파일명 등) |
| `${CLAUDE_SKILL_DIR}` | SKILL.md 있는 디렉토리 (스크립트 참조) |

## 동적 context injection

SKILL.md 안에서 shell을 미리 실행하고 그 출력을 프롬프트에 주입 가능:

```yaml
---
name: pr-summary
description: Summarize changes in a pull request
allowed-tools: Bash(gh *)
---

- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
```

멀티라인은 fenced code block:

````markdown
```!
node --version
npm --version
git status --short
```
````

## Skill content lifecycle

- 호출 시 SKILL.md 본문이 conversation에 **한 메시지로** 삽입되어 세션 끝까지 남음
- Claude Code는 후속 턴에 skill 파일을 **다시 읽지 않음** → "언젠가 지켜야 할 규칙"을
  표준 지침 스타일로 써야 함 (일회성 단계가 아니라)
- Auto-compaction 시 가장 최근 호출된 skill들만 최대 25,000 tokens 예산 내에서 복원

## 호출 제어 매트릭스

| Frontmatter 설정 | 사용자 호출 | Claude 자동 호출 | 컨텍스트 로드 시점 |
|-----------------|-----------|----------------|------------------|
| (기본값) | ✅ | ✅ | description은 항상 로드, 본문은 호출 시 |
| `disable-model-invocation: true` | ✅ | ❌ | description도 미로드, 사용자 호출 시만 본문 로드 |
| `user-invocable: false` | ❌ | ✅ | description 항상 로드, 호출 시 본문 |

## 한 반박 가능성 검토

> "Slash command가 더 단순하니까 처음엔 그게 낫지 않나?"

실제 문법 차이는 디렉토리 하나. `.claude/commands/wiki.md` ↔ `.claude/skills/wiki/SKILL.md`.
이 한 단계의 추가 비용이 Skills 전용 기능(자동 호출·fork·paths·supporting files)이 주는
이득보다 작다. 그래서 "단순함" 논거는 약함.

## 판단 기준

어떤 기능을 만들든 Skills로 시작한다. 예외는:

- 기존 `.claude/commands/` 자산이 많아 이관 비용이 큰 경우 (당분간 병행)
- 정말 1회성·실험용 (그냥 프롬프트 템플릿)

## 지식 조회용 Skill 설계 권장안

### (a) 수동 호출 전용 (사이드이펙트 있는 작업)

```yaml
---
name: deploy
description: Deploy to production
disable-model-invocation: true
allowed-tools: Bash(git *) Bash(./deploy.sh)
---
```

### (b) 자동 호출 허용 (지식 조회)

```yaml
---
name: wiki
description: >
  개인 지식 베이스 조회. 관련 지식이 축적돼 있을 가능성이 있으면 먼저 확인.
context: fork
agent: Explore
argument-hint: "[주제]"
---
```

## 참고 자료

- 공식 Skills 문서: https://code.claude.com/docs/en/skills
- 공식 Slash Commands 문서: https://code.claude.com/docs/en/slash-commands (Skills 페이지로 리다이렉트됨)
- Agent Skills 오픈 표준: https://agentskills.io
- Commands 참조 (built-in + bundled): https://code.claude.com/docs/en/commands

## 적용 기록

이 조사의 결론을 2026-04-16에 `~/.claude/skills/wiki/SKILL.md`로 실제 구현.
Personal scope, 자동 호출 허용, `context: fork` + `agent: Explore`, 광범위
description + "빈 조회 시 즉시 종료" 로직.
