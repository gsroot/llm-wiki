---
title: 'Claude Code: Slash Commands vs Agent Skills'
type: source
source_type: note
source_url: https://code.claude.com/docs/en/skills
raw_path: raw/notes/slash-commands-vs-agent-skills.md
author: 석근 (Claude Code 세션 조사·분석)
date_published: 2026-04-16
date_ingested: 2026-04-16
tags:
- claude-code
- skills
- slash-command
- agent-skills
- 운영가이드
- agent
related:
- '[[claude-code]]'
- '[[using-llm-wiki-as-rag]]'
- '[[harness]]'
- '[[context-engineering]]'
confidence: high
inbound_count: 30
cited_by:
- '[[agent-skills]]'
- '[[anthropic]]'
- '[[anthropics-skills]]'
- '[[autonomous-research-loop]]'
- '[[claude-code]]'
- '[[harness]]'
- '[[karpathy-autoresearch]]'
- '[[llm-infra-meta-cluster]]'
- '[[seokgeun-kim]]'
- '[[using-llm-wiki-as-rag]]'
cited_by_count: 10
aliases:
- 'Claude Code: Slash Commands vs Agent Skills'
- Slash Commands Vs Agent Skills
- slash commands vs agent skills
---

# Claude Code: Slash Commands vs Agent Skills

## 한줄 요약

> Anthropic이 Custom Commands를 Skills에 공식 통합했고 Skills를 권장. 자동 호출·supporting files·`context: fork`·`paths`는 Skill 전용 기능이며, 지식 조회처럼 "언제 필요할지 모르는" 도구에는 Skill이 압도적으로 유리.

## 핵심 내용

### 결정적 발견

공식 문서 원문(2026-04-16 접근):
> "Custom commands have been merged into skills. Skills are recommended since they support additional features like supporting files."

Claude Code Skills는 [agentskills.io](https://agentskills.io) 오픈 표준을 따르며, Claude Code는 이를 호출 제어·서브에이전트 실행·동적 context injection으로 확장.

### 두 방식의 실제 차이

| 기능 | `.claude/commands/*.md` | `.claude/skills/*/SKILL.md` |
|------|------------------------|----------------------------|
| `/name` 호출 | ✅ | ✅ |
| `$ARGUMENTS`, `$0` 치환 | ✅ | ✅ |
| Frontmatter | ✅ | ✅ |
| **자동 호출 (모델 판단)** | ❌ | ✅ |
| **supporting files** | ❌ | ✅ |
| **progressive disclosure** | 부분 | ✅ |
| **`context: fork`** (서브에이전트) | ❌ | ✅ |
| **`paths`** (경로 조건 활성) | ❌ | ✅ |
| 동적 injection (`` !`cmd` ``) | ✅ | ✅ |
| `allowed-tools` | ✅ | ✅ |

### Skill 저장 위치와 우선순위

`Enterprise` > `Personal (~/.claude/skills/)` > `Project (.claude/skills/)` > `Plugin`

- **Personal**: 모든 프로젝트에서 작동. 개인 도구의 기본 선택
- **Project**: 해당 프로젝트만. 팀 공유 시 Git 커밋
- **Plugin**: `plugin-name:skill-name` 네임스페이스

### Skill이 위키 조회에 유리한 4가지 이유

1. **자동 호출**: description 기반으로 Claude가 "위키에 관련 지식이 있을 수 있겠다" 판단하면 자동 발동. `/wiki`로 수동 호출도 여전히 가능. 이게 진짜 "RAG처럼"의 본질
2. **Supporting files로 노하우 패키징**: SKILL.md를 짧게 유지, `query-patterns.md`·스크립트는 필요할 때만 로드 → [[token-economy]] 원칙
3. **`context: fork`로 격리**: 여러 위키 페이지 Read 후 결과만 돌려줌. 메인 세션 컨텍스트 오염 방지. [[harness]]의 세션 분리 원칙 적용
4. **`paths`로 자동 호출 조건 제한**: 코드 작성 중에는 방해 안 하고, 문서 작업 중에만 활성화 같은 조건부 발동

### 호출 제어 매트릭스

| 설정 | 사용자 호출 | Claude 자동 호출 | 컨텍스트 로드 |
|-----|-----------|----------------|-------------|
| 기본값 | ✅ | ✅ | description만 상시, 본문은 호출 시 |
| `disable-model-invocation: true` | ✅ | ❌ | 호출 시에만 전부 |
| `user-invocable: false` | ❌ | ✅ | description 상시, 본문은 호출 시 |

### Frontmatter 핵심 필드

전체 14개 필드 중 위키 조회에 핵심적인 것:

| 필드 | 위키 조회에서의 역할 |
|------|-------------------|
| `description` | Claude가 자동 호출 판단 기준. 1,536자 cap. 키워드 front-load 중요 |
| `context: fork` | 조회를 서브에이전트로 격리. 메인 컨텍스트 보호 |
| `agent: Explore` | read-only 도구에 최적화된 서브에이전트 |
| `argument-hint` | `/wiki [주제]` 자동완성 힌트 |

### Skill content lifecycle

- 호출 시 본문이 conversation에 한 메시지로 삽입, 세션 끝까지 남음
- auto-compaction 시 최근 호출 skill들이 25,000 tokens 예산 내에서 복원 (최근 것 우선)
- 큰 skill이거나 여러 개 호출 후에는 오래된 것이 탈락 가능 → re-invoke로 복원

### 동적 context injection

SKILL.md에서 `` !`command` `` 구문으로 셸 명령 출력을 프롬프트에 주입 가능. 위키 조회에 응용하면 `index.md` 파싱, 최근 수집 로그 요약 등을 전처리로 넣을 수 있음.

## 주요 인사이트

- **"단순함" 논거는 약하다**: `.claude/commands/wiki.md` 와 `.claude/skills/wiki/SKILL.md`의 차이는 디렉토리 하나. 이 한 단계 비용 < Skill 전용 기능의 이득
- **Skill = [[harness]]의 패키지 레이어 구현체**: 마스터 가이드의 4층 레이어 중 "패키지 레이어(Skills, Plugins)"가 여기에 해당. 지식(SKILL.md) + 도구(allowed-tools) + 통제(disable-model-invocation, paths)를 하나로 묶는 단위
- **Slash Command → Skill 이관 비용은 0**: 기존 commands 파일을 `skills/name/SKILL.md`로 옮기기만 하면 됨. frontmatter 호환
- **판단 기준**: 어떤 도구든 Skills로 시작한다. 예외는 기존 commands 자산이 많아 이관 비용이 큰 경우뿐

## 관련 엔티티/개념

- [[claude-code]]: Skills 기능을 제공하는 주 제품
- [[harness]]: Skills가 "패키지 레이어"로서 하네스 아키텍처에 위치
- [[context-engineering]]: Skill의 progressive disclosure는 컨텍스트 엔지니어링의 "필요 범위만 로드" 원칙 구현
- [[token-economy]]: description만 상시 로드, 본문은 호출 시만 로드하는 lazy loading
- [[using-llm-wiki-as-rag]]: 이 조사의 원래 동기 (방법 4 구현)

## 인용할 만한 구절

> "Custom commands have been merged into skills. Skills are recommended since they support additional features like supporting files."
> — Anthropic, Claude Code Skills 공식 문서 (2026)

## 메모

- 이 조사의 실제 적용: `~/.claude/skills/wiki/SKILL.md` 생성 (2026-04-16). Personal scope, 자동 호출 허용, `context: fork` + `agent: Explore`, 광범위 description + "빈 조회 즉시 종료" 로직
- `disableSkillShellExecution` 설정으로 `` !`...` `` 실행을 managed settings에서 비활성화 가능 — 거버넌스 관점
- 공식 문서 URL은 `slash-commands`에서 `skills`로 리다이렉트됨 — 통합이 공식화된 증거
