---
source_url: https://wikidocs.net/340836
book: ChatGPT & Codex 실무 활용 가이드
author: 송영옥
license: CC-BY (wikidocs by.png 아이콘 표시)
fetched_at: 2026-04-30
ingestion_mode: path-b-summary
---

# Chapter 24. Assistants API — 대화형 AI 에이전트 구축

## 페이지 구조 (헤딩 outline)
- Assistants API란?
- 핵심 개념 4가지 (Assistant / Thread / Message / Run)
- 기본 코드 예시
  - 대화 이어가기
- 내장 도구 활용
  - File Search — 문서 기반 답변 (RAG)
  - Code Interpreter — 코드 실행과 데이터 분석
- Function Calling — 외부 시스템 연동
  - 날씨 API 연동 예시
- 실습: 제품 매뉴얼 기반 고객 상담 봇 구축
  - 전체 구현 코드
  - 대화형 CLI 인터페이스 추가

## 핵심 요약 (자가 작문)

Assistants API는 단발성 질문-답변에 특화된 Chat Completions와 달리, 대화 상태(state)를 자동 관리하는 고수준 API로 소개된다. Assistant·Thread·Message·Run 네 가지 객체를 중심으로 다중 턴 대화 흐름을 손쉽게 구성할 수 있고, File Search(문서 기반 RAG), Code Interpreter(코드 실행·데이터 분석), Function Calling(외부 시스템 연동) 같은 내장 도구를 그대로 활용할 수 있다. 챕터는 기본 코드 예시 → 대화 이어가기 → File Search·Code Interpreter 사용 → 날씨 API를 호출하는 Function Calling 예제로 단계적으로 깊어진다. Thread를 DB에 저장해 사용자별 대화 세션을 유지하면 재방문 사용자에게도 이전 대화 컨텍스트를 그대로 이어 줄 수 있다는 패턴이 제시된다. 실습은 제품 매뉴얼 기반 고객 상담 봇을 CLI까지 포함해 만들어 본다.

## 인용 (key quotes, 짧게)

> "Chat Completions API가 단발성 질문-답변에 특화되어 있다면, Assistants API는 상태(state)를 유지하는 AI 어시스턴트를 구축하기 위한 고수준 API입니다."

> "Thread를 데이터베이스에 저장하여 사용자별 대화 세션을 유지하면, 재방문 사용자에게 이전 대화 이어가기 기능을 제공할 수 있습니다."

## 메타 정보
- 표: 1개 / 코드블록: 7개 / 이미지: 1개
- 마지막 편집: 2026-04-12

원본: https://wikidocs.net/340836
