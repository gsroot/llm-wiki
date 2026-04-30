---
title: "qmd"
type: entity
entity_type: tool
tags: [검색, search, 마크다운, markdown, CLI, mcp, tool-stub, 53회차]
related:
  - "[[llm-wiki-pattern]]"
  - "[[mcp]]"
source_count: 1
observed_source_refs: 7
inbound_count: 17
page_intent: tool-stub
page_intent_note: "미래 도입 후보 도구. 현 위키 197페이지 규모는 index 기반 탐색으로 충분하나 50페이지 추가 시 검색 인프라로 도입 검토 (메모 §1)."
created: 2026-04-09
updated: 2026-04-29
cited_by_count: 7
---

# qmd

## 개요

마크다운 파일을 위한 로컬 검색 엔진. 하이브리드 BM25/벡터 검색과 LLM 리랭킹을 디바이스에서 수행한다. LLM 위키가 커졌을 때(~50페이지 이상) 인덱스 파일만으로는 탐색이 어려워지는 시점에 도입을 검토할 도구이다.

- GitHub: https://github.com/tobi/qmd

## 주요 특징

- **하이브리드 검색**: BM25(키워드) + 벡터(시맨틱) 검색을 결합
- **LLM 리랭킹**: 검색 결과를 LLM으로 재정렬하여 정확도 향상
- **로컬 실행**: 외부 서비스 의존 없이 디바이스에서 모든 처리
- **이중 인터페이스**:
  - **CLI**: LLM이 셸 명령으로 호출 가능
  - **MCP 서버**: LLM이 [[mcp]]를 통해 네이티브 도구로 직접 검색 가능

## 관련 개념

- [[llm-wiki-pattern]]: qmd는 위키가 일정 규모를 넘어설 때 검색 인프라로 도입
- [[mcp]]: qmd의 MCP 서버 모드를 통해 LLM 에이전트와 네이티브 통합

## 출처

- [[llm-wiki-idea-doc]] — 위키 규모가 커졌을 때의 검색 솔루션으로 추천

## 메모

- 현재 이 위키는 아직 소규모이므로 `index.md` 기반 탐색으로 충분하다. 50페이지를 넘기면 도입 시점.
- 한국어 형태소 분석 지원 여부를 사전 확인할 필요가 있다. 미지원 시 영어 키워드 병기로 우회 가능.
