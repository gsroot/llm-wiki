---
title: "이 LLM 위키를 Claude Code에서 RAG처럼 쓰는 법"
type: source
source_type: note
source_url: ""
source_scope: local
raw_path: "raw/notes/using-llm-wiki-as-rag.md"
author: "석근 (Claude Code Opus 4.6 세션 대화 정리)"
date_published: 2026-04-15
date_ingested: 2026-04-15
tags: [llm-wiki, RAG, claude-code, mcp, agent-skills, 운영가이드, 자기참조, 53회차]
related:
  - "[[llm-wiki-pattern]]"
  - "[[claude-code]]"
  - "[[mcp]]"
  - "[[qmd]]"
  - "[[slash-commands-vs-agent-skills]]"
confidence: high
cited_by:
  - "[[claude-code]]"
  - "[[claude-code-master-guide]]"
  - "[[harness]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[llm-wiki-pattern]]"
  - "[[mcp]]"
  - "[[microsoft-generative-ai-for-beginners]]"
  - "[[rag]]"
  - "[[seokgeun-kim]]"
  - "[[slash-commands-vs-agent-skills]]"
---

# 이 LLM 위키를 Claude Code에서 RAG처럼 쓰는 법

## 한줄 요약

> 이 위키는 이미 "수작업 컴파일된 RAG"다. Claude Code에서 `cd ~/llm-wiki && claude`만 해도 `index.md`가 라우터 역할을 하며 필요한 페이지를 Read로 가져오는 retrieval 루프가 자동 작동. 상황별로 5가지 통합 방법이 존재하며 현재는 방법 1로 충분.

## 핵심 내용

### 본질: 이 위키 = 컴파일된 RAG

| 항목 | 일반 RAG | 이 위키 |
|------|---------|--------|
| 지식 획득 | 벡터 검색으로 청크 회수 | 사전 컴파일된 요약·링크 |
| 라우팅 | 유사도 점수 | `index.md` (수동 큐레이션) |
| 축적 | 매 질의마다 재발견 | 복리 성장 |

Claude Code의 **Read/Grep/Glob가 retrieval 엔진**. `index.md`가 라우터, 각 위키 페이지가 컴파일된 청크.

### 5가지 통합 방법

1. **위키 디렉토리에서 직접 실행**: `cd ~/llm-wiki && claude`. CLAUDE.md 자동 로드로 index 기반 탐색 루프가 바로 작동.
2. **다른 프로젝트에서 참조**: 그 프로젝트 `CLAUDE.md`에 `/Users/sgkim/llm-wiki/wiki/` 경로와 "읽기 전용" 지침 추가.
3. **세션 시작 시 명시적 로드**: 첫 메시지로 "먼저 `.../wiki/index.md` 읽고 ..." 지시. 일회성.
4. **Agent Skill로 패키징 (✅ 구현 완료)**: `~/.claude/skills/wiki/SKILL.md` (Personal scope). 자동 호출+수동 `/wiki` 모두 지원. Slash Command에서 **승격**한 이유: Anthropic이 commands를 skills에 통합, 자동 호출·`context: fork`·supporting files 등 Skill 전용 기능이 위키 조회에 유리. 상세 비교 → [[slash-commands-vs-agent-skills]]
5. **MCP 서버로 노출**: [[qmd]] + `.mcp.json` 등록. 50+ 페이지 되면 도입.

### 방법 선택 매트릭스

| 상황 | 추천 방법 |
|------|----------|
| 위키 자체 관리 | 방법 1 |
| 회사 프로젝트에서 참조 | 방법 2 |
| 가끔 한 번씩 | 방법 3 |
| 반복 조회 + 자동 호출 | 방법 4 (Agent Skill — 자동·수동 모두) |
| 50+ 페이지 이후 | 방법 5 |

### 사용 팁

1. **위키를 자주 키워라** — 수집할 때마다 기존 페이지가 업데이트·연결되어 복리로 강해짐
2. **"위키에 물어본다" 감각** — 일반 지식 질문보다 **위키 페이지 기반 합성** 질문이 가장 강력
   - ❌ "하네스가 뭐야?"
   - ✅ "`wiki/concepts/harness.md` 기준으로 내 BI 업무 하네스를 설계한다면?"

## 주요 인사이트

- **"RAG처럼"이라는 표현의 재정의**: 사용자가 "RAG처럼 쓰고 싶다"고 말할 때 실제로 원하는 것은 벡터 검색이 아니라 **"질문하면 관련 지식이 자동으로 따라오는 경험"**. 이 위키는 그 경험을 index+링크로 이미 구현.
- **단계적 도입 원칙**: 18페이지 규모에서는 Read/Grep가 벡터 검색보다 오히려 빠르고 정확. MCP/qmd는 "필요해지면" 도입하는 3단계 확장 경로.
- **Agent Skill의 전략적 위치**: 방법 4는 Slash Command에서 Agent Skill로 승격됨 ([[slash-commands-vs-agent-skills]]). [[claude-code-master-guide]]의 "Skill로 반복 작업 절차 고정" 원칙의 개인 단위 적용. Skill = [[harness]]의 패키지 레이어 구현체.
- **위키와 프로젝트 분리 원칙**: 방법 2/3은 위키를 **읽기 전용 참조**로만 쓰고 회사 프로젝트와 쓰기 권한을 분리한다는 거버넌스 감각. [[claude-code]]의 allow/ask/deny와 같은 결.

## 관련 엔티티/개념

- [[llm-wiki-pattern]]: 이 활용 가이드의 이론적 배경. RAG와의 차이·보완관계
- [[claude-code]]: 이 위키의 주 에이전트. `CLAUDE.md`, Agent Skills, `.mcp.json` 기능 활용
- [[slash-commands-vs-agent-skills]]: 방법 4에서 Skill 선택을 뒷받침한 조사·비교 문서
- [[mcp]]: 방법 5의 핵심 프로토콜
- [[qmd]]: 방법 5의 구체적 검색 엔진 구현체

## 인용할 만한 구절

> "'RAG처럼 쓴다'는 'Claude Code가 `index.md`를 라우터로 삼아 필요한 페이지만 Read하게 한다'가 본질."

## 메모

- 이 문서는 석근님이 Claude Code 세션에서 질문해서 받은 답변을 본인이 다시 수집 대상으로 지정한 **자기 참조적 수집** — 위키 운영 메타 문서에 해당.
- 후속 과제:
  - ✅ **방법 4 완료 (2026-04-16)**: slash command 대신 Agent Skill로 승격하여 `~/.claude/skills/wiki/SKILL.md` 생성. 사유: 공식 문서상 commands가 skills로 통합됐고 자동 호출·`context: fork` 등 Skill 전용 기능이 위키 조회에 유리
  - 회사 프로젝트 CLAUDE.md 템플릿에 "참조 지식 베이스" 섹션 추가 (방법 2) — Skill 자동 호출이 있으면 우선순위 낮아짐
  - qmd 도입 시점 판정을 위한 트리거 기준: 페이지 50개 또는 "index.md 읽는 데 5초 이상 걸리기 시작할 때"
