---
title: Claude Agent SDK
type: entity
entity_type: tool
tags:
- claude-agent-SDK
- anthropic
- SDK
- agent
- claude-code
- mcp
- hooks
related:
- '[[claude-code]]'
- '[[anthropic]]'
- '[[anthropics-claude-cookbooks]]'
- '[[agent-skills]]'
- '[[mcp]]'
- '[[harness]]'
source_count: 1
observed_source_refs: 5
inbound_count: 46
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 18
---

# Claude Agent SDK

## 개요

[[anthropic]]이 공개한 **Claude Code의 raw agentic power를 일반 도메인(SW 외)에 풀어놓는 Python SDK**. 원래 Anthropic 엔지니어가 개발 워크플로우를 가속화하려 만든 내부 도구였는데, 공개 후 연구·데이터 분석·워크플로우 자동화·모니터링·콘텐츠 생성 등 비-코딩 도메인에서 광범위 채택되며 "범용 에이전트 빌더"로 자리매김.

핵심: `query` 한 줄과 `ClaudeSDKClient` / `ClaudeAgentOptions` 두 인터페이스만으로 Claude Code의 모든 운영 기법(hooks · plan mode · subagent · MCP · output styles · custom slash commands)을 그대로 사용.

## 주요 특징

### 1. 인터페이스 (Python SDK)

| API | 역할 |
|-----|------|
| `query` | 단일 자율 쿼리 (async iter로 응답 스트림) |
| `ClaudeSDKClient` | 멀티턴 세션 + 컨텍스트 영속 |
| `ClaudeAgentOptions` | 시스템 프롬프트, 도구, 권한, hooks 설정 |

### 2. 기본 도구 (Out of the box)

- `WebSearch` — 자율 정보 수집
- `Read` (멀티모달) — 텍스트/이미지/PDF
- `Bash` — Python 스크립트, shell 명령
- `Edit` / `Write` — 파일 조작
- 외부 시스템: **MCP 서버 통합** (Git MCP 13+ tools, GitHub MCP 100+ tools, 자체 JSON-RPC subprocess MCP 서버 가능)

### 3. Claude Code 운영 기법의 SDK화

Claude Code에서 검증된 모든 운영 기법이 SDK 옵션으로 노출:

| Claude Code 기법 | SDK에서의 사용처 |
|----------------|----------------|
| `CLAUDE.md` 영속 컨텍스트 | 시스템 프롬프트 + 파일 경로 마운트 |
| **Output styles** | 다른 청중에 맞춘 커뮤니케이션 톤 변경 |
| **Plan mode** | 복잡 태스크에서 실행 없이 계획만 |
| **Custom slash commands** | 자주 쓰는 작업 단축 |
| **Hooks** (`PreToolUse`, `PostToolUse`) | 컴플라이언스 audit trail, write 검증 |
| **Subagent orchestration** | 도메인 전문 서브에이전트 조율 |

### 4. 6단계 튜토리얼 시리즈

[[anthropics-claude-cookbooks]] `claude_agent_sdk/` 디렉토리에 각 단계가 다음 단계로 빌드되는 6개 노트북:

1. **00 The One-Liner Research Agent** — `query` async iter 기본
2. **01 The Chief of Staff Agent** — CEO용 비서, 모든 운영 기법 압축
3. **02 The Observability Agent** — Git/GitHub MCP, CI/CD 분석
4. **03 The Site Reliability Agent** — 자체 MCP 서버, Prometheus, read-write remediation, safety hooks
5. **04 Migrating from OpenAI Agents SDK** — 마이그레이션
6. **05 Building a Session Browser** — 세션 로그 시각화

01번이 석근의 "개인 비서 AI" 관심사에 정확히 매핑.

### 5. Claude Code와의 관계

| 관점 | Claude Code | Claude Agent SDK |
|------|-------------|------------------|
| 사용자 | 사람 (CLI/IDE/Web) | 개발자 (Python 코드) |
| 목적 | 코딩 보조 | 임의 도메인 에이전트 빌드 |
| 운영 기법 | 인터페이스로 노출 | 동일 기법을 옵션으로 노출 |
| 비유 | 운영체계의 "쉘" | 운영체계의 "syscall API" |

Claude Code = Anthropic이 자기 운영 패턴을 사람에게 노출하는 진입점. Agent SDK = 같은 패턴을 코드로 노출하는 진입점.

## "Beyond Coding: The Agent Builder's Toolkit"

`claude_agent_sdk/README.md`의 자기 정의:

> "Originally an internal tool built by Anthropic engineers to accelerate development workflows, the SDK's public release revealed unexpected potential. (...) The pattern was clear: the SDK had inadvertently become an effective agent-building framework. Its architecture, designed to handle software development complexity, proved remarkably well-suited for general-purpose agent creation."

요점: SW 개발 복잡도를 다루도록 설계한 SDK가 우연히 범용 에이전트 빌더가 됐다는 자기 진술. **"강력한 SW 개발 도구 = 강력한 일반 에이전트 도구"** 라는 가설.

## 관련 개념

- [[claude-code]]: 같은 운영 기법의 사람용 진입점. SDK는 동일 기법의 코드용 진입점.
- [[anthropic]]: Agent SDK의 제작·운영 주체
- [[harness]]: SDK의 모든 옵션은 4층 하네스(지식·도구·패키지·통제)의 코드화
- [[agent-skills]]: SDK 안에서 Skills를 옵션으로 활성화 가능 (claude_agent_sdk + skills 조합)
- [[mcp]]: SDK의 외부 시스템 통합 표준 진입로
- [[autonomous-research-loop]]: research_agent 노트북이 이 패턴의 SDK 구현

## 출처

- [[anthropics-claude-cookbooks]] — `claude_agent_sdk/` 디렉토리 + 6개 튜토리얼 노트북 + README

## 메모

- [[claude-managed-agents]]는 Agent SDK와 분리해 추적할 가치가 있음 — Agent SDK가 "에이전트의 SDK"라면 Managed Agents는 "에이전트의 PaaS". 두 추상화 레이어가 다름.
- 04번 노트북 (OpenAI Agents SDK → Claude Agent SDK 마이그레이션)이 별도로 가치 있음 — OpenAI Agents SDK 사용자 → Claude로 이동하는 표준 변환 가이드.
