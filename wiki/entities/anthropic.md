---
title: "Anthropic"
type: entity
entity_type: organization
tags: [anthropic, AI, AI연구소, claude, claude-code, agent-skills, mcp, building-effective-agents]
related:
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[agent-skills]]"
  - "[[mcp]]"
  - "[[harness]]"
  - "[[karpathy]]"
  - "[[microsoft]]"
source_count: 4
observed_source_refs: 10
inbound_count: 54
created: 2026-04-27
updated: 2026-04-27
---

# Anthropic

## 개요

Claude 모델군과 그 주변 생태계(Claude Code, Claude Agent SDK, [[claude-managed-agents|Claude Managed Agents]], Skills, MCP 표준 등)를 만드는 AI 연구·제품 회사. 위키에서 만나는 거의 모든 핵심 도구·표준이 이쪽에서 출발한다.

## 핵심 제품·표준

| 분류 | 항목 | 위키 페이지 |
|------|------|-----------|
| 모델 | Claude Sonnet 4.6 / Haiku 4.5 / Opus 4.6 (정책: dated ID 금지, alias만) | (모델 자체 페이지 없음) |
| CLI/에이전트 | Claude Code (CLI/IDE/Web/iOS) | [[claude-code]] |
| SDK | Claude Agent SDK | [[claude-agent-sdk]] |
| Hosted runtime | [[claude-managed-agents|Claude Managed Agents]] (CMA) | hosted stateful agent runtime |
| 패키지 표준 | Agent Skills (`SKILL.md`) | [[agent-skills]] |
| 도구 표준 | Model Context Protocol (MCP) | [[mcp]] |
| 에이전트 분류 | "Building Effective Agents" 5 패턴 | [[agent-patterns]] |

## 주요 특징

### 1. "표준 vs 구현" 분리

표준은 외부 사이트(`agentskills.io`)나 블로그·논문 형태로 빼고, **구현/사례는 GitHub 리포에 분산**:

| 리포 | 역할 |
|------|------|
| [[anthropics-skills]] | Skills **배포 채널** (마켓플레이스, 17 스킬) |
| [[anthropics-claude-cookbooks]] | API/SDK **실습 채널** (~100 노트북) |
| `anthropic-cookbook` (구) | 위 리포의 옛 이름 (`anthropic-cookbook` → `claude-cookbooks` 리브랜딩) |

표준의 중립성과 자기 구현의 분리. [[microsoft]]와의 차이: Microsoft는 "교육 시리즈 단일 운영체계"가 강하고, Anthropic은 "표준-구현 분리"가 강하다.

### 2. 슬래시 커맨드 = CI = 로컬

`anthropics/claude-cookbooks` CLAUDE.md에서 관측: `/notebook-review`, `/model-check`, `/link-review`가 `.claude/commands/`에 정의되고 **Claude Code(로컬)와 GitHub Actions(CI)가 같은 정의를 호출**한다. "lint를 코드로 체크인하는" 패턴이 회사 전체 문화.

### 3. 모델 정책 (CLAUDE.md "Key Rules")

- **항상** non-dated alias 사용 (`claude-sonnet-4-6`)
- **절대** dated ID 금지 (`claude-sonnet-4-6-20250514`)
- Bedrock은 별도 형식 (`anthropic.claude-opus-4-6-v1`, global endpoint는 `global.` prefix)

이 정책 자체가 cookbooks의 `/model-check` 슬래시 커맨드로 자동 검증된다.

### 4. 노트북 출력 보존 정책

> "Notebook outputs are intentionally kept in this repository as they demonstrate expected results for users."
> — `claude-cookbooks/CONTRIBUTING.md`

기대 결과를 노트북 자체가 들고 다니게 함. **RAG 학습 데이터로서의 가치를 의식한 결정** — 사용자가 노트북을 LLM에 붙여 넣어도 "원본의 정답"을 같이 본다는 뜻.

## "Claude의 raw agentic power" 자기 정의

`claude_agent_sdk/README.md`에 박힌 자기 인식 (위키에서 가장 인용 가치 높은 문장):

> "What makes Claude Code special isn't just code understanding; it's the ability to (...) Claude Code the closest thing to a 'bare metal' harness for Claude's raw agentic power: a minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead."

요점: **Claude Code = "Claude의 raw agentic power를 위한 bare-metal harness"**. [[harness]] 개념의 anthropic-side 정통 정의이자, Claude Agent SDK가 그 power를 SW 외 도메인으로 푸는 통로라는 자리매김.

## 사람·팀 (위키에서 관측된 인물)

- **Erik Schluntz · Barry Zhang** — "Building Effective Agents" 블로그 저자 ([[agent-patterns]] 5 패턴)
- **Charmaine Lee, Pauly, Mark N., Gagan B., David Hershey 등** — Cookbooks 노트북 기여자 (registry.yaml + authors.yaml 매핑)

## 비교 — Microsoft와의 운영 차이

| 측면 | Anthropic | [[microsoft]] |
|------|-----------|--------------|
| 표준-구현 관계 | 분리 (agentskills.io ↔ anthropics/skills) | 통합 (microsoft-for-beginners 단일 운영체계) |
| 메인 포맷 | `SKILL.md` 패키지 + Jupyter notebook | `.md` lesson + 50+ 언어 자동 번역 |
| 카탈로그 | `registry.yaml` (단일 진실원) | README.md (시리즈마다 분산) |
| CI-로컬 통합 | 슬래시 커맨드 단일 채널 | GitHub Action(co-op-translator) 단일 채널 |
| 페다고지 | 노트북 → reference 구현 | quiz → lesson → assignment 6단 |

두 조직이 **같은 LLM 시대의 운영 표준을 다른 추상화 레이어로 결정화**하고 있다는 게 위키 관점의 핵심 발견.

## 관련 개념

- [[claude-code]]: 회사의 가장 성공한 제품
- [[claude-agent-sdk]]: 그 제품의 raw power를 외부에 푸는 SDK
- [[agent-skills]]: 패키지 표준
- [[mcp]]: 도구 표준
- [[harness]]: Anthropic이 자기 제품을 부르는 자기 정의
- [[agent-patterns]]: Building Effective Agents 5 패턴
- [[microsoft]]: 같은 시대에 다른 운영 방식의 대조

## 출처

- [[claude-code-overview]] — Claude Code 공식 소개
- [[anthropics-skills]] — Skills 마켓플레이스
- [[anthropics-claude-cookbooks]] — API/SDK 노트북 카탈로그
- [[slash-commands-vs-agent-skills]] — Custom Commands → Skills 통합 경위

## 메모

- Anthropic의 자체 운영 노하우(CLAUDE.md, 슬래시 커맨드, registry.yaml, authors.yaml)가 **세 번째 단계의 발견** — 첫째는 모델, 둘째는 제품(Claude Code/Skills), 셋째는 운영 표준 자체. 이 세 번째 단계가 위키에 가장 천천히 들어왔지만 가장 적용 가치가 높음.
- 후속 탐구: Anthropic 자체 페이지가 더 무거워지면 `entities/anthropic-cloud-advocates`(가칭) 같은 식으로 팀 단위로 분리할 가치가 생길 수 있음.
