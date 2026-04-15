---
title: "MCP (Model Context Protocol)"
type: concept
category: ai
tags: [MCP, model-context-protocol, LLM, 도구, tool-use, 프로토콜]
related: [[llm-wiki-pattern]], [[qmd]], [[claude-code]]
source_count: 3
created: 2026-04-09
updated: 2026-04-15
---

# MCP (Model Context Protocol)

## 정의

LLM 에이전트가 외부 도구와 리소스를 **함수처럼 호출**할 수 있게 해주는 개방형 프로토콜. Anthropic이 주도하여 개발했으며, LLM이 셸 명령을 실행하는 것보다 더 구조화되고 안전한 방식으로 외부 시스템과 상호작용할 수 있게 한다.

## 왜 중요한가

LLM 위키 맥락에서 MCP는 위키 검색을 LLM의 **네이티브 도구**로 노출하는 핵심 기술이다. 셸 명령어로 검색 스크립트를 실행하는 것과 비교하면:
- 응답 속도가 빠르다
- 에러 처리가 구조화되어 있다
- LLM이 도구의 입출력 스키마를 이해하고 적절히 활용한다

## 핵심 내용

### 동작 방식

1. **MCP 서버**가 도구(tool)와 리소스(resource)를 정의하여 노출
2. **MCP 클라이언트**(LLM 에이전트)가 해당 도구를 발견하고 호출
3. 결과를 LLM이 받아서 응답에 활용

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

## 열린 질문

- MCP 서버를 직접 만들어 위키 전용 도구(페이지 생성, 링크 체크 등)를 노출하면 수집 워크플로우를 더 자동화할 수 있을까?
