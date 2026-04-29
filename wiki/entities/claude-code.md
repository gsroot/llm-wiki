---
title: "Claude Code"
type: entity
entity_type: tool
aliases: [Claude Code, claude-code, 클로드 코드, Anthropic CLI, cc]
tags: [claude-code, AI, 에이전트, agent, 코딩도구, coding-tool, anthropic, CLI, agent-skills, plugin-marketplace, claude-agent-SDK, bare-metal-harness, spec-kit]
related:
  - "[[anthropic]]"
  - "[[claude-agent-sdk]]"
  - "[[mcp]]"
  - "[[agent-skills]]"
  - "[[agent-patterns]]"
  - "[[llm-wiki-pattern]]"
  - "[[obsidian-web-clipper]]"
  - "[[cowork]]"
  - "[[harness]]"
  - "[[token-economy]]"
  - "[[context-engineering]]"
  - "[[spec-kit]]"
  - "[[spec-driven-development]]"
  - "[[seokgeun-kim]]"
  - "[[portfolio]]"
  - "[[c2spf-analytics]]"
  - "[[seokgeun-stack-guide]]"
  - "[[matechat]]"
  - "[[llm-infra-meta-cluster]]"
source_count: 8
observed_source_refs: 39
inbound_count: 119
created: 2026-04-09
updated: 2026-04-29
cited_by_count: 40
---

# Claude Code

> 한국어 표기: **클로드 코드**(Anthropic의 공식 CLI).

## 개요

[[anthropic]]이 개발한 에이전트 코딩 도구. 전체 코드베이스를 이해하고, 파일 편집, 명령 실행, 외부 도구 통합을 수행한다. Terminal CLI, VS Code, JetBrains, Desktop 앱, Web, iOS 등 다양한 환경에서 동일한 엔진으로 작동한다.

Anthropic 자기 정의 (`claude_agent_sdk/README.md`):

> "Claude Code the closest thing to a 'bare metal' harness for Claude's raw agentic power: a minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead."

= **Claude의 raw agentic power를 위한 bare-metal [[harness]]**. 같은 운영 기법을 코드로 노출하는 자매 도구가 [[claude-agent-sdk]]. 이 위키 자체가 Claude Code를 에이전트로 사용하여 운영되고 있다.

위키 그래프에서는 [[agent-skills]], [[harness]], [[mcp]]와 함께 LLM 인프라 메타 클러스터의 핵심 노드다. 이 네 노드가 어떻게 맞물리는지는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]에서 종합한다.

## 주요 특징

### 핵심 기능
- **에이전트 코딩**: 자연어 지시로 코드 작성, 디버깅, 리팩토링
- **코드베이스 이해**: 여러 파일과 도구에 걸쳐 작업 가능
- **Git 통합**: 스테이징, 커밋, 브랜치, PR을 직접 수행
- **Unix 철학**: 파이프 가능한 CLI. 다른 도구와 조합 가능

### 확장 시스템
- **CLAUDE.md**: 프로젝트 루트의 마크다운 파일로 세션마다 자동 로드. 코딩 표준, 아키텍처, 워크플로우 규칙 정의. 이 위키의 스키마가 바로 이 기능을 활용
- **자동 메모리**: 빌드 명령, 디버깅 인사이트 등을 자동 축적
- **[[mcp]]**: 외부 서비스(Google Drive, Jira, Slack 등)를 네이티브 도구로 연결. 프로젝트 루트 `.mcp.json`에 등록
- **Skills (Agent Skills)**: `/review-pr`, `/deploy-staging` 같은 반복 워크플로우를 패키징. 기존 Custom Commands가 Skills에 **공식 통합**됨. [agentskills.io](https://agentskills.io) 오픈 표준 준수. 핵심 차별점은 **자동 호출**(description 기반으로 Claude가 판단), **supporting files**, **`context: fork`**(서브에이전트 격리), **`paths`**(경로 조건 활성화). 3-level progressive disclosure (Metadata 100단어 상시 / SKILL.md body <500lines / scripts·references·assets는 필요 시만) → [[agent-skills]] 개념 페이지 참조. 상세 비교 → [[slash-commands-vs-agent-skills]]
- **Plugin Marketplace**: `/plugin marketplace add <owner>/<repo>` 명령으로 외부 GitHub 리포를 플러그인 카탈로그로 등록. 등록 후 `/plugin install <plugin>@<marketplace>`로 일괄 설치. 공식 사례는 [[anthropics-skills]] (`/plugin marketplace add anthropics/skills`) — document-skills(xlsx/docx/pptx/pdf, 4개)·example-skills(skill-creator, mcp-builder 등 12개)·claude-api 3개 플러그인 제공. Partner 스킬(Notion 등)도 같은 메커니즘으로 배포
- **Hooks**: 도구 실행 전후에 셸 명령 자동 실행

### 멀티 에이전트
- **서브 에이전트**: 여러 에이전트를 병렬 생성. 리드 에이전트가 조정하고 결과 병합. 서브에이전트 조율 패턴은 [[agent-patterns]]의 Orchestrator-Workers 분류
- **[[claude-agent-sdk]]**: Claude Code의 모든 운영 기법(hooks·plan mode·output styles·subagent·MCP)을 Python SDK 옵션으로 노출. SW 외 도메인(연구 에이전트·개인 비서·SRE 등)에 raw agentic power를 푸는 통로. 6단계 튜토리얼은 [[anthropics-claude-cookbooks]] `claude_agent_sdk/` 디렉토리

### 자동화 & 크로스 디바이스
- **예약 작업**: 클라우드(서버) / 데스크톱(로컬) / `/loop`(CLI 폴링)
- **CI/CD**: GitHub Actions, GitLab CI/CD 연동
- **원격 제어**: 로컬 세션을 휴대폰/브라우저에서 계속
- **Slack 연동**: `@Claude` 멘션으로 버그 → PR 자동화

### 설치

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

설치 후 프로젝트 디렉토리에서 `claude` 명령으로 시작. 네이티브 설치는 백그라운드 자동 업데이트.

### 필수 CLI 명령

| 명령 | 기능 |
|------|------|
| `claude` | 대화형 모드 |
| `claude "task"` | 일회성 작업 |
| `claude -p "query"` | 일회성 쿼리 후 종료 (파이프라인용) |
| `claude -c` | 현재 디렉토리 최근 대화 계속 |
| `claude -r` | 이전 대화 재개 |
| `claude commit` | Git 커밋 생성 |
| `/clear` | 대화 기록 지우기 |
| `/login` | 계정 전환 |
| `/help` | 명령 목록 |

단축키: `?` 전체 단축키, `Tab` 자동완성, `↑` 명령 기록, `/` skills 탐색.

### 프롬프팅 원칙

- **구체적으로**: "버그 수정" 대신 증상·맥락을 포함하여 지시
- **단계 분해**: 복잡한 작업은 1~3단계로 쪼개서 요청
- **이해 먼저**: 변경 전 "스키마 분석"처럼 탐색 요청으로 컨텍스트 확보
- **동료 메타포**: 달성 목표 설명이 명령보다 효과적
- **권한 모델**: 파일 수정 전 항상 승인 요청, 세션 단위 "모두 수락" 모드 지원

## 관련 개념

- [[harness]]: Claude Code가 구현한 작업장 구조 전체 — 이 도구의 중심 추상
- [[context-engineering]]: CLAUDE.md 설계의 이론적 배경
- [[token-economy]]: `/compact`, `--resume`, 세션 분리 같은 기능의 설계 원리
- [[cowork]]: 비개발 지식 업무용 자매 작업 경로. 같은 하네스를 공유
- [[llm-wiki-pattern]]: 이 위키의 운영 패턴. Claude Code가 에이전트 역할 수행
- [[mcp]]: Claude Code의 외부 도구 통합 프로토콜
- [[obsidian-web-clipper]]: 소스 수집 후 Claude Code가 위키에 통합하는 워크플로우
- [[agent-skills]]: SKILL.md 기반 작업 패키지의 표준·구조·운영 원칙. Claude Code의 Skills 기능이 구현하는 개념
- [[spec-kit]] / [[spec-driven-development]]: GitHub의 SDD 메소드론 도구. `specify init . --integration claude --here` 한 줄로 9개 슬래시 명령(`/speckit.constitution` 외 8종)을 `.claude/commands/`에 자동 설치 — Claude Code가 SDD 4단계 워크플로우(헌법→사양→계획→태스크)를 그대로 수행하는 방식의 표준 설치 채널

## 운영 관점 보강 (마스터 가이드 기반)

### 허용/질문/차단 (allow/ask/deny)
모든 요청은 세 갈래로 흐른다. 고위험 작업은 프롬프트 경고가 아니라 **설정 차단**으로 앞단에서 멈춘다.

### 설정 scope 우선순위
`managed` > `user` > `project` > `local`. `managed`는 조직이 강제하는 층이며 다른 층에서 덮어쓸 수 없다 (`strictKnownMarketplaces`, `allowManagedPermissionRulesOnly`, `allowManagedMcpServersOnly`).

### 세션 재개 플래그
`claude --continue` / `claude --resume`. 이어받을 때는 `handoff.md` 같은 바깥 상태 파일과 함께 쓰는 게 안정적.

### Worktree 패턴
같은 저장소를 역할별로 분리해 병렬 작업 (plan / implement / review 세션 격리).

## 출처

- [[claude-code-overview]] — Anthropic 공식 문서 개요 페이지
- [[claude-code-quickstart]] — 설치부터 첫 세션·Git 작업까지의 실전 온보딩 가이드
- [[claude-code-master-guide]] — CHOI의 848페이지 실전 마스터 가이드. 하네스·거버넌스·직무별 플레이북 포함
- [[using-llm-wiki-as-rag]] — 이 위키를 Claude Code에서 retrieval 소스로 통합하는 5가지 방법 (Agent Skill, `.mcp.json` 등)
- [[slash-commands-vs-agent-skills]] — Slash Commands와 Agent Skills 통합 경위·비교·판단 (Anthropic 공식 문서 기반)
- [[anthropics-skills]] — Anthropic 공식 Agent Skills 레퍼런스 리포(17개 스킬·3개 플러그인 마켓플레이스·skill-creator)
- [[anthropics-claude-cookbooks]] — Claude API/SDK 실습 노트북 카탈로그 (~100 노트북, 14 디렉토리). claude_agent_sdk 6단계·managed_agents 8개·patterns/agents 5패턴·skills 3종
- [[github-spec-kit]] — GitHub의 Spec-Driven Development 툴킷. `--integration claude` 옵션이 Claude Code를 1급 시민으로 지원, `MarkdownIntegration` base class 사례

## 메모

- 석근님의 주요 개발 도구 중 하나. 회사 맥북에서 사용.
- LLM 위키에서의 역할: Obsidian이 IDE, Claude Code가 프로그래머, 위키가 코드베이스.
- Cowork도 위키 에이전트로 병행 사용 가능 (외출 시).

## 인용한 페이지 (cited_by — 51회차 자동 갱신)

- [[agent-patterns]]
- [[agent-skills]]
- [[agent-stack-evolution]]
- [[anthropic]]
- [[anthropics-claude-cookbooks]]
- [[anthropics-skills]]
- [[autonomous-research-loop]]
- [[autoresearch]]
- [[backend-fastapi-stack]]
- [[claude-agent-sdk]]
- [[claude-code-master-guide]]
- [[claude-code-overview]]
- [[claude-code-quickstart]]
- [[claude-managed-agents]]
- [[context-engineering]]
- [[cowork]]
- [[deepagents]]
- [[flutter]]
- [[flutter-flutter]]
- [[github]]
- [[github-spec-kit]]
- [[harness]]
- [[karpathy-autoresearch]]
- [[llm-infra-meta-cluster]]
- [[matechat]]
- [[mcp]]
- [[microsoft]]
- [[obsidian]]
- [[openai]]
- [[openai-openai-cookbook]]
- [[portfolio]]
- [[prompt-cache]]
- [[scikit-learn]]
- [[scikit-learn-scikit-learn]]
- [[seokgeun-kim]]
- [[slash-commands-vs-agent-skills]]
- [[spec-driven-development]]
- [[spec-kit]]
- [[token-economy]]
- [[using-llm-wiki-as-rag]]

