---
title: "microsoft/generative-ai-for-beginners — 21 Lessons GenAI 입문"
type: source
source_type: article
source_url: "https://github.com/microsoft/generative-ai-for-beginners"
raw_path: "raw/articles/microsoft-generative-ai-for-beginners/"
author: "Microsoft Cloud Advocates"
date_published: 2023-06-19
date_ingested: 2026-04-27
tags: [generative-AI, microsoft, microsoft-for-beginners, openai, prompt-engineering, rag, ai-agents, slm, mistral, meta]
related:
  - "[[microsoft]]"
  - "[[microsoft-for-beginners]]"
  - "[[mcp]]"
  - "[[context-engineering]]"
  - "[[agent-skills]]"
confidence: high
---

# microsoft/generative-ai-for-beginners — 21 Lessons GenAI 입문

## 한줄 요약

> Microsoft Cloud Advocates의 GenAI 입문 커리큘럼 v3 — 21개 Lesson을 "Learn(개념)" / "Build(코드)"로 명시 분리하고, Python·TypeScript 둘 다 지원하며 Azure OpenAI / OpenAI / GitHub Models를 백엔드로 선택할 수 있는 "다중 런타임 지원" 입문 커리큘럼.

## 메타

- 라이선스: MIT
- 별 109,895 / 포크 58,958 (2026-04-27 기준, 5개 시리즈 중 1위)
- 크기: 6.6GB (50+ 언어 자동 번역으로 비대해짐 — sparse-checkout으로 `!translations !translated_images` 제외 권장)
- 기본 언어: Jupyter Notebook
- 자매 코스 분기: `Generative-AI-for-beginners-dotnet`, `generative-ai-for-beginners-java`, `generative-ai-with-javascript` — 같은 커리큘럼을 언어별로 운영
- 공식 모임: Microsoft Foundry Discord

## 21 Lesson 구조

전반부(00–10) = 입문 + 텍스트/검색/이미지 앱, 중반부(11–17) = 통합·라이프사이클·RAG·오픈소스, 후반부(18–21) = 모델 단별 심화

| # | Lesson | 종류 | 핵심 |
|---|--------|------|------|
| 00 | Course Setup | Learn | Azure / GitHub Models / OpenAI 환경 |
| 01 | Intro to GenAI & LLMs | Learn | 기초 |
| 02 | Exploring & comparing different LLMs | Learn | 모델 선택 |
| 03 | Using GenAI Responsibly | Learn | 책임 |
| 04 | Prompt Engineering Fundamentals | Learn | 기초 |
| 05 | Advanced Prompts | Learn | 응용 |
| 06 | Text Generation Apps | Build | 첫 빌드 |
| 07 | Chat Applications | Build | 대화 |
| 08 | Search Apps + Vector DB | Build | 임베딩 검색 |
| 09 | Image Generation Apps | Build | DALL·E |
| 10 | Low Code AI Apps | Build | Power Platform |
| 11 | Function Calling | Build | 외부 도구 통합 |
| 12 | Designing UX for AI | Learn | UX |
| 13 | Securing AI Apps | Learn | 위협 모델 |
| 14 | GenAI Application Lifecycle | Learn | LLMOps |
| **15** | **RAG and Vector Databases** | **Build** | **검색 증강 (raw 보관)** |
| 16 | Open Source Models / HF | Build | Hugging Face |
| **17** | **AI Agents** | **Build** | **에이전트 프레임워크 (raw 보관)** |
| 18 | Fine-Tuning LLMs | Learn | 파인튜닝 |
| 19 | Building with SLMs | Learn | 소형 모델 |
| 20 | Building with Mistral Models | Learn | Mistral |
| 21 | Building with Meta Models | Learn | Llama 계열 |

## 핵심 시사점

### 1. "Learn / Build" 명시 분리

각 Lesson을 "**Learn:** ..." 또는 "**Build:** ..."으로 prefix 표기 — 학습자가 자기 단계에 맞춰 점프할 수 있게. 위키 페이지 운영에도 이식 가능: 개념(Learn) 페이지와 종합/실습(Build) 페이지를 명시 마킹.

### 2. 다중 백엔드(다중 런타임) 입문 코스

같은 lesson을 Azure OpenAI / OpenAI / GitHub Models 어디서든 돌릴 수 있도록 환경 변수로 분리. 각 lesson 폴더에 `aoai-assignment` / `oai-assignment` / `githubmodels` suffix가 붙은 배리언트가 존재. 입문 코스가 특정 벤더에 락인되지 않게 하는 의도적 설계.

### 3. 21번까지 "최신 모델 단원"이 별도

19=SLM, 20=Mistral, 21=Meta — 시리즈 본체가 모델 카탈로그를 강의로 흡수. 모델 라인이 늘 때마다 후행 lesson을 추가하는 운영 모델. 위키에 "엔티티별 단원" 패턴으로 응용 가능.

### 4. Azure co-op-translator로 50+ 언어 자동화

`translations/<lang>/README.md`가 GitHub Action으로 자동 갱신. 위키 자체에는 적용 어렵지만, "원본 1개 + 번역 N개" 분리 패턴이 [[llm-wiki-pattern]]의 raw/wiki 분리와 비슷한 발상.

## 석근에게 가장 가치있는 lesson

- **15 = RAG and Vector Databases** — [[llm-wiki-pattern]]의 RAG 활용([[using-llm-wiki-as-rag]])과 직결, raw에 보관함
- **17 = AI Agents** — 가벼운 에이전트 프레임워크 입문, 다음 단계로 [[microsoft-ai-agents-for-beginners]]
- 11 = Function Calling — [[mcp]]와 비교 가치 (전통 함수 호출 vs MCP)
- 14 = GenAI Application Lifecycle — BI 서비스에 LLM을 끼워넣을 때의 LLMOps 시각

## 관련 엔티티/개념

- [[microsoft]] — 운영 주체
- [[microsoft-for-beginners]] — 같은 톤·페다고지·인프라를 공유하는 시리즈 그룹
- [[microsoft-ai-agents-for-beginners]] — 17번 lesson을 12+ lesson으로 확장
- [[mcp]] — 11번(Function Calling)과 비교점
- [[context-engineering]] — RAG·function calling은 "동적 컨텍스트 조립"의 한 갈래

## 인용

> "Lessons are labeled either 'Learn' lessons explaining a Generative AI concept or 'Build' lessons that explain a concept and code examples in both Python and TypeScript when possible."
> — README

## 메모

- v3 명시 = 커리큘럼 자체가 살아있는 문서. v1·v2 흔적은 git history에서만 확인 가능 (블로그·강의 주기와 별도로 코드/설명이 갱신됨).
- "Other Courses" 섹션이 README 마지막에 일관되게 노출되어 시리즈 카탈로그 역할. 위키의 [[microsoft-for-beginners]] 엔티티 페이지가 같은 역할을 한다.
- 후속 탐구: 11(Function Calling) lesson을 추가 raw 보관해 [[mcp]]와의 추상화 차이를 정리할 수 있다.
