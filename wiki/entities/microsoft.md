---
title: Microsoft
aliases:
- Microsoft
- 마이크로소프트
- MS
type: entity
entity_type: organization
tags:
- microsoft
- microsoft-cloud-advocates
- microsoft-for-beginners
- openai
- github
- devrel
related:
- '[[microsoft-for-beginners]]'
- '[[claude-code]]'
- '[[mcp]]'
- '[[agent-skills]]'
- '[[microsoft-generative-ai-for-beginners]]'
- '[[microsoft-ml-for-beginners]]'
- '[[microsoft-web-dev-for-beginners]]'
- '[[microsoft-ai-agents-for-beginners]]'
- '[[microsoft-data-science-for-beginners]]'
source_count: 5
observed_source_refs: 15
inbound_count: 39
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 14
---

# Microsoft

## 개요

미국 워싱턴주 레드먼드에 본사를 둔 글로벌 기술 기업. 위키 맥락에서는 **AI/개발 도구·교육 커리큘럼** 측면이 주된 관심 — 특히 **Cloud Advocates(DevRel 조직)**가 운영하는 무료 학습 커리큘럼 시리즈([[microsoft-for-beginners]]), **Azure AI Foundry**(이전 Azure OpenAI Service), **Microsoft Agent Framework(MAF)**, **GitHub** 인프라(Copilot, Codespaces, Marketplace) 등이 주요 노출 면.

## 주요 특징

### 1. Microsoft Cloud Advocates — 무료 교육 인프라 운영

내부 DevRel 조직이 GitHub 위에서 **무료 입문 커리큘럼 시리즈**를 양산.

- 별 합계만 386,000+ (5개 시리즈 통합 기준, 2026-04-27)
- 50+ 언어 자동 번역(Azure co-op-translator GitHub Action)
- 모두 MIT 라이선스
- 공통 페다고지: 프로젝트 기반 + pre/post 퀴즈 + sketchnote + assignment + Discord/Foundry Forum

자세한 시리즈 카탈로그는 [[microsoft-for-beginners]] 참조.

### 2. Azure AI 스택

- **Azure OpenAI Service** → **Azure AI Foundry**로 리브랜딩 (2024–2025)
- **Azure AI Foundry Agent Service V2** — [[microsoft-ai-agents-for-beginners]]의 기본 백엔드
- **Microsoft Agent Framework (MAF)** — Azure 위 에이전트 프레임워크
- **Azure ML Studio** — Low-Code 모델 학습/배포

### 3. GitHub 인프라 (자회사)

- **GitHub Copilot** — 입문 코스에 "Copilot Agent Challenge"로 통합 ([[microsoft-web-dev-for-beginners]])
- **GitHub Marketplace Model Catalog** — Azure 외 백엔드로 [[microsoft-generative-ai-for-beginners]]에 배리언트 제공
- **GitHub Codespaces** — 입문 코스의 기본 실행 환경

### 4. AI 에이전트 프로토콜 카탈로그화

[[microsoft-ai-agents-for-beginners]] lesson 11에서 [[mcp]] / **A2A** / **NLWeb** 3종을 묶어 가르침. **MCP는 Anthropic이 만든 표준이지만 Microsoft가 입문 자료에 정식 편입**하여 표준 확산을 가속화.

## 위키 맥락에서의 역할

석근의 직무(컴투스플랫폼 게임 데이터 BI 서비스 개발자)에서 Microsoft Azure는 직접 사용 스택은 아니지만, 다음 면에서 영향이 있다:

- **VS Code + GitHub Copilot** — IDE 환경
- **Microsoft Cloud Advocates 무료 커리큘럼** — 자기 학습 자원
- **Microsoft Agent Framework / Azure AI Foundry** — Anthropic 외 에이전트 생태계의 메이저 흐름 추적
- **MCP/A2A/NLWeb 카탈로그화** — 표준 채택의 신호

## 관련 개념

- [[microsoft-for-beginners]]: Cloud Advocates 운영 시리즈 통합 엔티티
- [[mcp]]: Anthropic 표준이지만 Microsoft 입문 코스에 편입
- [[agent-skills]]: Anthropic 표준 + Microsoft가 자체 변종 미보유 (vs Anthropic이 [[claude-code]] + Skills + Plugin 통합)
- [[claude-code]]: Anthropic의 에이전트 IDE — Microsoft의 Agent Framework + Copilot과 경쟁/보완 구도

## 출처

- [[microsoft-generative-ai-for-beginners]] — Cloud Advocates 운영 21 lesson GenAI 코스
- [[microsoft-ml-for-beginners]] — 26 lesson 클래식 ML 코스
- [[microsoft-web-dev-for-beginners]] — 24 lesson 웹 개발 코스
- [[microsoft-ai-agents-for-beginners]] — 12+ lesson AI 에이전트 코스 (가장 최신)
- [[microsoft-data-science-for-beginners]] — 20 lesson 데이터과학 코스

## 메모

- 5개 시리즈가 동일 페다고지·동일 GitHub Action·동일 Discord로 묶여 있어 "단일 운영체계" 성격이 강하다. [[microsoft-for-beginners]] 엔티티가 사실상 그 운영체계를 표현.
- Anthropic이 [[claude-code]] + Skills + Plugin Marketplace + Cowork로 **응용 도구 생태계**를 짠다면, Microsoft는 **Azure + GitHub + Copilot + Foundry + MAF + MCP/A2A 카탈로그**로 **인프라+표준 카탈로그**를 짠다. 두 회사의 전략 추상화 레벨이 다르다.
- 후속 탐구: `microsoft/AI-For-Beginners`, `microsoft/mcp-for-beginners`, `microsoft/edgeai-for-beginners` 등 미수집 시리즈 목록 정리 필요.
