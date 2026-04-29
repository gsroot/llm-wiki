---
title: "MCP (Model Context Protocol)"
type: concept
category: ai
aliases: [Model Context Protocol, mcp, 모델 컨텍스트 프로토콜, MCP, mcp-server]
tags: [mcp, model-context-protocol, LLM, 도구, tool-use, 프로토콜, a2a, nlweb, agentic-protocols, claude-cookbooks, claude-agent-SDK, json-rpc-subprocess]
related:
  - "[[llm-wiki-pattern]]"
  - "[[qmd]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[anthropic]]"
  - "[[microsoft-for-beginners]]"
  - "[[context-engineering]]"
  - "[[agent-patterns]]"
  - "[[agent-skills]]"
  - "[[harness]]"
  - "[[seokgeun-kim]]"
  - "[[portfolio]]"
  - "[[c2spf-analytics]]"
  - "[[seokgeun-stack-guide]]"
  - "[[matechat]]"
  - "[[llm-infra-meta-cluster]]"
source_count: 6
observed_source_refs: 53
inbound_count: 131
created: 2026-04-09
updated: 2026-04-29
cited_by_count: 41
---

# MCP (Model Context Protocol)

> 한국어 표기: **모델 컨텍스트 프로토콜**(Model Context Protocol).

## 정의

LLM 에이전트가 외부 도구와 리소스를 **함수처럼 호출**할 수 있게 해주는 개방형 프로토콜. Anthropic이 주도하여 개발했으며, LLM이 셸 명령을 실행하는 것보다 더 구조화되고 안전한 방식으로 외부 시스템과 상호작용할 수 있게 한다.

## 왜 중요한가

LLM 위키 맥락에서 MCP는 위키 검색을 LLM의 **네이티브 도구**로 노출하는 핵심 기술이다. 셸 명령어로 검색 스크립트를 실행하는 것과 비교하면:
- 응답 속도가 빠르다
- 에러 처리가 구조화되어 있다
- LLM이 도구의 입출력 스키마를 이해하고 적절히 활용한다

본 위키에서는 MCP가 [[agent-skills]] / [[harness]] / [[claude-code]]와 함께 LLM 인프라 메타 클러스터를 이룬다. 프로토콜·스킬·하네스·실행 도구의 관계를 한 번에 볼 때는 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]를 참조한다.

## 핵심 내용

### 동작 방식

**클라이언트-서버 아키텍처** ([[microsoft-ai-agents-for-beginners]] lesson 11 정의):
- **Hosts** — LLM 애플리케이션 (예: VSCode, Claude Code). MCP 서버에 연결을 시작하는 주체
- **Clients** — Host 안에서 서버와 1:1 연결을 유지하는 컴포넌트
- **Servers** — 특정 능력을 노출하는 경량 프로그램

**3 Primitives (서버가 노출하는 기능 단위)**:
- **Tools** — 에이전트가 호출할 수 있는 액션/함수 (예: `get_weather`, `purchase_product`). 이름·설명·입출력 스키마를 capabilities listing에 광고
- **Resources** — 클라이언트가 요청 시 제공받는 읽기 전용 데이터/문서 (파일 내용, DB 레코드, 로그 — text 또는 binary)
- **Prompts** — 복잡한 워크플로우를 위한 사전 정의 템플릿

**호출 흐름**:
1. Host의 Client가 Server에 연결
2. Client가 "어떤 tools/resources/prompts가 있는가?" 조회 (**Dynamic Tool Discovery**)
3. LLM이 사용자 의도에 맞는 tool 선택, 파라미터와 함께 Server에 호출
4. Server가 실제 백엔드(API/DB)를 wrapping해 결과 반환
5. LLM이 결과를 응답에 활용

### MCP의 3가지 이점 (vs 전통 API)

[[microsoft-ai-agents-for-beginners]] lesson 11이 명문화한 비교:

| 면 | 전통 API | MCP |
|----|---------|-----|
| 통합 | API 변화 시 코드 수정 필요 | "**integrate once**" — 동적 발견 |
| LLM 호환성 | 모델별 함수 호출 형식 차이 | 다른 LLM에 동일한 MCP 서버 사용 |
| 보안 | 키/인증을 API마다 다르게 관리 | 표준 인증 — 서버 추가 시 확장성 ↑ |

### 자매 프로토콜: A2A · NLWeb (Agentic Protocols)

MCP는 단독이 아니라 더 큰 "**Agentic Protocols**" 카테고리의 한 축. lesson 11은 3종을 병행 가르침:

- **MCP (Model Context Protocol)** — LLM ↔ **외부 도구/데이터**. Anthropic 발의.
- **A2A (Agent-to-Agent)** — 에이전트 ↔ **다른 에이전트**. 서로 다른 조직·환경·기술 스택의 에이전트가 공유 작업을 협력해 처리. Google이 주도하여 표준화.
- **NLWeb (Natural Language Web)** — **자연어 인터페이스를 모든 웹사이트로**. 에이전트가 사이트 콘텐츠를 발견·상호작용 가능.

세 프로토콜은 같은 추상화 레벨에서 다른 관계를 표준화한다 — MCP=수직(LLM↔도구), A2A=수평(에이전트↔에이전트), NLWeb=수직(에이전트↔웹).

### LLM 위키에서의 활용

- [[qmd]] 같은 검색 엔진을 MCP 서버로 노출하면, LLM이 위키 페이지를 자연스럽게 검색 가능
- Claude Code의 경우 프로젝트 루트 `.mcp.json`에 서버를 등록하면 자동 연결
- 위키 규모가 50페이지를 넘어가면 도입 권장

### 지원 에이전트

- **[[claude-code]]**: `.mcp.json` 기반 프로젝트 레벨 설정. Google Drive, Jira, Slack 등 외부 서비스를 MCP로 연결하여 네이티브 도구로 사용 가능
- **Codex**: 유사한 MCP 연동 지원
- 기타 MCP 호환 에이전트에서도 사용 가능

### Claude Code에서의 MCP 활용 범위

Claude Code 공식 문서에 따르면 MCP는 단순 검색을 넘어 다양한 외부 시스템과 통합된다:
- Google Drive에서 설계 문서 읽기
- Jira에서 티켓 업데이트
- Slack에서 데이터 가져오기
- 커스텀 도구 연결

## 실전 적용

현재 이 위키에서는 아직 MCP 검색을 사용하지 않는다. `index.md` 기반 탐색으로 충분한 규모이기 때문이다. 위키가 성장하면 qmd MCP 서버 도입이 자연스러운 다음 단계가 된다.

## 관련 개념

- [[llm-wiki-pattern]]: MCP는 위키 패턴의 확장 인프라
- [[qmd]]: MCP 서버 모드를 제공하는 구체적 도구
- [[claude-code]]: MCP의 대표적 클라이언트. Anthropic이 MCP 프로토콜과 Claude Code를 함께 개발

## 사용 순서 (마스터 가이드)

**MCP로 닿기 → Skill로 절차 얹기 → Plugin으로 배포**. MCP는 "닿는 길"이고, Skill은 그 위에 올리는 반복 작업 매뉴얼, Plugin은 Skills·commands·agents·hooks·MCP를 묶어 팀에 배포하는 상자.

거버넌스 관점에서는 `allowManagedMcpServersOnly` 같은 managed 설정으로 조직이 허용한 MCP만 실제 연결되도록 강제할 수 있다.

## 출처

- [[llm-wiki-idea-doc]] — 역자 주석 3번에서 MCP를 "게임 체인저"로 소개
- [[claude-code-overview]] — Claude Code 공식 문서에서 MCP를 외부 데이터 소스 연결의 핵심으로 설명
- [[claude-code-master-guide]] — 6장 "확장과 자동화"에서 MCP·Skill·Plugin·Connector·Hook 5종의 관계와 사용 순서 정리
- [[using-llm-wiki-as-rag]] — `.mcp.json` 등록 예시와 qmd를 위키 전용 MCP 서버로 쓰는 방법
- [[microsoft-ai-agents-for-beginners]] — lesson 11 "Agentic Protocols (MCP, A2A, NLWeb)"에서 MCP의 3 primitives(Tools/Resources/Prompts), 클라이언트-서버 아키텍처, 자매 프로토콜 카탈로그화
- [[anthropics-claude-cookbooks]] — `claude_agent_sdk/` Observability Agent(Git MCP 13+ tools, GitHub MCP 100+ tools) + SRE Agent(자체 JSON-RPC subprocess MCP 서버 12+ tools, Prometheus 통합) + `managed_agents/CMA_operate_in_production.ipynb` (vault-backed MCP credentials) — 운영 레벨 MCP 통합의 reference

## 열린 질문

- MCP 서버를 직접 만들어 위키 전용 도구(페이지 생성, 링크 체크 등)를 노출하면 수집 워크플로우를 더 자동화할 수 있을까?

## 인용한 페이지 (cited_by — 51회차 자동 갱신)

- [[agent-frameworks-matrix]]
- [[agent-patterns]]
- [[agent-skills]]
- [[agent-stack-evolution]]
- [[anthropic]]
- [[anthropics-claude-cookbooks]]
- [[anthropics-skills]]
- [[backend-fastapi-stack]]
- [[claude-agent-sdk]]
- [[claude-code]]
- [[claude-code-master-guide]]
- [[claude-code-overview]]
- [[claude-managed-agents]]
- [[context-engineering]]
- [[fastapi]]
- [[fastmcp]]
- [[harness]]
- [[jlowin-fastmcp]]
- [[langchain]]
- [[langchain-ai-langchain]]
- [[langchain-ai-langgraph]]
- [[langgraph]]
- [[llm-infra-meta-cluster]]
- [[llm-wiki-idea-doc]]
- [[llm-wiki-pattern]]
- [[matechat]]
- [[microsoft]]
- [[microsoft-ai-agents-for-beginners]]
- [[microsoft-for-beginners]]
- [[microsoft-generative-ai-for-beginners]]
- [[ml-ai]]
- [[obsidian-guide]]
- [[openai]]
- [[openai-agents-python]]
- [[openai-cookbook]]
- [[openai-openai-agents-python]]
- [[openai-openai-cookbook]]
- [[portfolio]]
- [[qmd]]
- [[seokgeun-kim]]
- [[using-llm-wiki-as-rag]]

