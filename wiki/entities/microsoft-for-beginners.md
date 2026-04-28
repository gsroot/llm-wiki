---
title: "microsoft-for-beginners (시리즈)"
type: entity
entity_type: project
tags: [microsoft-for-beginners, microsoft, microsoft-cloud-advocates, curriculum, 무료교육, project-based-learning, co-op-translator, github-copilot]
related:
  - "[[microsoft]]"
  - "[[mcp]]"
  - "[[context-engineering]]"
  - "[[ml-ai]]"
  - "[[data-pipeline-bigquery]]"
  - "[[frontend-react]]"
source_count: 5
created: 2026-04-27
updated: 2026-04-27
---

# microsoft-for-beginners (시리즈)

## 개요

[[microsoft]]의 Cloud Advocates(DevRel 조직)가 GitHub 위에서 양산하는 **무료 입문 커리큘럼 시리즈**. GitHub topic `microsoft-for-beginners`로 분류되며 동일한 페다고지·인프라·라이선스(MIT)·자동 번역 체계를 공유. 위키에는 **5개 시리즈**가 수집되어 있고, 시리즈 전체는 더 큰 카탈로그(`AI-For-Beginners`, `mcp-for-beginners`, `edgeai-for-beginners`, `IoT-For-Beginners`, `XR-Development-For-Beginners`, `Security-101`, `Cybersecurity for Beginners` 등)로 이어진다.

## 주요 특징

### 1. 공통 인프라

- **MIT 라이선스** — 모든 시리즈 동일
- **Azure co-op-translator GitHub Action** — 50+ 언어 자동 번역 (`translations/<lang>/`, `translated_images/` 디렉토리). 이 때문에 리포지토리 크기가 1.5–6.5GB로 비대해짐 → sparse-checkout으로 `!translations !translated_images` 제외 권장
- **Microsoft Foundry Discord** — 단일 커뮤니티 공간
- **GitHub Codespaces** — 즉시 실행 환경
- **`quiz-app/` 디렉토리** — 모든 시리즈가 동일 퀴즈 앱(Vue.js 추정) 호스팅, 결과는 `ff-quizzes.netlify.app/<series>/`에 게시

### 2. 공통 페다고지

> "We have chosen two pedagogical tenets: ensuring that it is hands-on **project-based** and that it includes **frequent quizzes**."

각 lesson 구성:
- (선택) sketchnote
- (선택) 보조 영상
- pre-lecture warmup quiz
- 본문 (README.md)
- 프로젝트 기반 lesson은 단계별 빌드 가이드
- knowledge checks
- challenge
- supplemental reading
- assignment
- post-lecture quiz

### 3. 위키에 수집된 5개 시리즈

| 시리즈 | Lessons | 별 | 첫 커밋 | 핵심 소스 페이지 |
|--------|---------|-----|--------|------------------|
| Generative AI | 21 | 109,895 | 2023-06-19 | [[microsoft-generative-ai-for-beginners]] |
| Web Dev | 24 | 95,682 | 2020-11-10 | [[microsoft-web-dev-for-beginners]] |
| Machine Learning | 26 | 85,483 | 2021-03-03 | [[microsoft-ml-for-beginners]] |
| AI Agents | 12+ | 59,691 | 2024-11-28 | [[microsoft-ai-agents-for-beginners]] |
| Data Science | 20 | 35,119 | 2021-03-03 | [[microsoft-data-science-for-beginners]] |

총합: **107 lessons, 386,000+ 별, 8,800,000+ 단어 추정**.

### 4. 시리즈 그래프 — README "Other Courses" 섹션

각 시리즈 README 마지막에 동일한 "**Other Courses**" 표가 있어 카탈로그 역할. 5개 그룹으로 분류:
- LangChain (LangChain4j / LangChain.js / LangChain)
- Azure / Edge / MCP / Agents (AZD / Edge AI / MCP / AI Agents)
- Generative AI Series (.NET / Java / JavaScript)
- Core Learning (ML / Data Science / AI / Cybersecurity / Web Dev / IoT / XR)
- Copilot Series (Copilot AI Pair / .NET / Adventure)

### 5. 라이프사이클: 살아있는 커리큘럼

- **버전 명시** — Generative AI는 v3, lesson 19–21이 SLM/Mistral/Meta 단원으로 신규 추가
- **"Coming Soon"** — AI Agents 시리즈는 16–18번이 아직 미완성
- **GitHub Copilot Agent 챌린지** — 기존 Web Dev 코스에 사후 추가

→ 시리즈가 닫히지 않고 모델·프로토콜 변화에 따라 연장됨.

## 위키 운영 관점에서 배울 점

1. **번역 분리 패턴** — 원본 1개 + 번역 N개를 sparse-checkout으로 분리. 위키의 raw/wiki 분리 발상과 같은 결.
2. **README가 강의 본문** — 각 lesson 디렉토리의 README.md가 곧 강의. 위키 페이지가 강의 단위가 될 수 있음을 시사.
3. **Other Courses = 시리즈 카탈로그** — 위키의 [[microsoft-for-beginners]] 엔티티가 같은 역할.
4. **퀴즈/체크 구조** — 학습 자원에 자기 평가가 내장. 위키에 "체크 질문" 섹션 신설 검토 가능.
5. **공통 인프라 일관성** — 5개 시리즈가 같은 GitHub Action·Discord·퀴즈 앱·페다고지를 공유. 위키도 5종 템플릿(entity·concept·source·synthesis + 신규 lesson?)을 강제.

## 관련 개념

- [[microsoft]]: 운영 주체
- [[mcp]]: AI Agents lesson 11이 정확화·보강
- [[context-engineering]]: AI Agents lesson 12가 보강
- [[ml-ai]]: ML/Data Science 시리즈가 보강
- [[data-pipeline-bigquery]]: Data Science 시리즈가 응용 발상 보강
- [[frontend-react]]: Web Dev 시리즈가 진입 전 단계 멘탈 모델

## 출처

- [[microsoft-generative-ai-for-beginners]]
- [[microsoft-ai-agents-for-beginners]]
- [[microsoft-ml-for-beginners]]
- [[microsoft-web-dev-for-beginners]]
- [[microsoft-data-science-for-beginners]]

## 메모

- "for-beginners"라는 명칭에도 불구하고 **AI Agents 시리즈는 이미 중급 이상**의 추상화(MCP/A2A/NLWeb, Context Engineering, Multi-Agent)를 다룸. 시리즈명이 진입 장벽을 낮춰 보이지만 실제로는 Cloud Advocates 자체 학습 라이브러리 역할.
- 후속 탐구: 이 5개를 다 끝내면 다음은 `microsoft/mcp-for-beginners`, `microsoft/AI-For-Beginners`(딥러닝 보강), `microsoft/edgeai-for-beginners`(엣지 추론) 순으로 보강 가능.
- 위키 운영 패턴 응용: `templates/lesson.md` 신설 검토 — pre-lecture quiz / 본문 / knowledge checks / challenge / assignment / post-lecture quiz 6단 구조.
