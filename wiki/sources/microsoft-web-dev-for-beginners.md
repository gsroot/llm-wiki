---
title: "microsoft/Web-Dev-For-Beginners — 12 weeks, 24 Lessons 웹 개발 입문"
type: source
source_type: article
source_url: "https://github.com/microsoft/Web-Dev-For-Beginners"
raw_path: "raw/articles/microsoft-web-dev-for-beginners/"
author: "Microsoft Cloud Advocates"
date_published: 2020-11-10
date_ingested: 2026-04-27
tags: [web-dev, microsoft, microsoft-for-beginners, html, css, javascript, vanilla-js, project-based, accessibility, github-copilot]
related:
  - "[[microsoft]]"
  - "[[microsoft-for-beginners]]"
  - "[[frontend-react]]"
confidence: high
---

# microsoft/Web-Dev-For-Beginners — 12 weeks, 24 Lessons 웹 개발 입문

## 한줄 요약

> Microsoft Cloud Advocates의 웹 개발 입문 — **의도적으로 React/Vue/Angular 같은 프레임워크를 회피**하고 순수 HTML/CSS/Vanilla JS로 7개 프로젝트(Terrarium → Typing Game → Browser Extension → Space Game → **Banking App** → Code Editor → **AI Chat Assistant**)를 12주에 직접 빌드시키는 프로젝트 기반 코스. 최근 GitHub Copilot Agent 챌린지와 9-chat-project(GenAI 통합)가 추가됨.

## 메타

- 라이선스: MIT
- 별 95,682 (2026-04-27 기준, 5개 시리즈 중 2위)
- 첫 커밋 2020-11-10 — 5개 시리즈 중 **가장 오래된 모체**
- 기본 언어: JavaScript / HTML / CSS
- 페다고지: 48 quizzes (3문제씩)
- 최근 업데이트: GitHub Copilot Agent mode 챌린지가 대부분 챕터에 추가됨, 9-chat-project가 AI Assistant 빌드로 신설

## 24 Lesson 그루핑 (7개 프로젝트)

| 프로젝트 | Lessons | 학습 주제 |
|----------|---------|----------|
| 1-getting-started | 01–03 | 프로그래밍 도구 / GitHub / **접근성(Accessibility)** |
| 2-js-basics | 04–07 | 데이터 타입, 함수, 조건, 배열 |
| 3-terrarium | 08–10 | HTML / CSS / **DOM + Closures** |
| 4-typing-game | 11 | 키보드 이벤트 |
| 5-browser-extension | 12–14 | 브라우저 / API + LocalStorage / **백그라운드 + 성능** |
| 6-space-game | 15–20 | **Pub/Sub 패턴**, Canvas, 충돌, 점수, 종료 |
| 7-bank-project | 21–24 | **HTML 템플릿 라우팅**, 폼, 데이터, **상태 관리** |
| 8-code-editor | 25 | VSCode 사용 |
| **9-chat-project** | **26** | **GenAI AI Assistant 빌드 (raw 보관)** |

## 핵심 시사점

### 1. 의도적 "프레임워크 회피"

> "While we have purposefully avoided introducing JavaScript frameworks to concentrate on the basic skills needed as a web developer before adopting a framework, a good next step to completing this curriculum would be learning about Node.js..."

React/Vue 입문이 아닌 **DOM·closure·Pub/Sub·상태 관리 같은 본질**을 가르치는 결정. 이는 [[frontend-react]]에 들어가기 전 단계의 멘탈 모델을 짠다.

### 2. 03 = Accessibility (접근성)이 본문 세 번째

JS 시작 전에 **접근성**을 가르침. Data-Science-For-Beginners의 윤리(02번)와 같은 "기술 외 가치"를 입문 단계에 박는 페다고지.

### 3. 9-chat-project (lesson 26) = "AI Assistant 빌드" 신설

**Star Trek 컴퓨터** 비유로 시작 — 누구나 알던 SF가 이제 웹 기술로 구현 가능하다는 메시지로 학습자를 끌어들이는 hook. 26번 lesson 본문에서 직접 OpenAI/Azure 연동 → 채팅 UI 구현 → 파인튜닝 검토까지를 한 lesson에 담아내는 굵은 단원.

### 4. GitHub Copilot Agent mode 챌린지

대부분 챕터에 "GitHub Copilot Agent Challenge 🚀" 추가 — 학습자가 단순 코드 입력이 아닌 **에이전트와 페어 프로그래밍**하는 새 학습 방식을 코스 본문에 통합. Microsoft가 자사 도구(Copilot)를 입문 코스에 직접 결합하는 운영 패턴.

### 5. 6-space-game = Pub/Sub 패턴 + Inheritance vs Composition

게임 빌드를 통해 입문자에게 **Pub/Sub 패턴**과 **Inheritance vs Composition** 같은 OOP 디자인 결정을 가르침. 게임 BI 도메인의 석근에게 친숙한 발상.

## 석근에게 가장 가치있는 lesson

- **9-chat-project (26)** — GenAI 통합 웹앱 빌드 패턴, raw 보관
- **7-bank-project (21–24)** — HTML 템플릿 라우팅 + 상태 관리 (React 없이) — 백엔드 출신이 프론트엔드 mental model 재구성에 적합
- **3-accessibility (03)** — BI 대시보드의 접근성 체크
- **6-space-game/1-introduction** — Pub/Sub 디자인 패턴 (이벤트 기반 BI 파이프라인 발상)

## 관련 엔티티/개념

- [[microsoft]] / [[microsoft-for-beginners]]
- [[frontend-react]] — 이 코스 다음 단계 (프레임워크 진입 전 단계)
- [[microsoft-generative-ai-for-beginners]] — 9-chat-project가 그쪽의 lesson 7(Chat Apps)와 사실상 짝
- 회사 [[c2spf-analytics-renewal]]의 React/Vite 환경에 진입 전 vanilla JS 멘탈 모델로 보강 가능

## 인용

> "Remember in Star Trek when the crew would casually chat with the ship's computer, asking it complex questions and getting thoughtful responses? What seemed like pure science fiction in the 1960s is now something you can build using web technologies you already know."
> — Lesson 26 (9-chat-project)

## 메모

- 5개 시리즈 중 석근의 직무에 가장 거리가 있지만, **9-chat-project는 직접 응용 가능**. 회사 사이드 프로젝트나 개인 비서 AI에 그대로 이식 가능한 수준.
- 7-bank-project의 상태 관리 lesson은 [[frontend-react]] 학습 전 "왜 React가 필요한가"를 체감하는 단계로 가치 있음.
- 후속 탐구: 9-chat-project lesson을 raw 보관함 — code 부분이 길어 본문 lesson 길이가 매우 큼(2300+줄). 별도 lesson 발췌가 더 가치 있을 수 있음.
