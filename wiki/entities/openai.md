---
title: "OpenAI"
type: entity
entity_type: organization
tags: [openai, AI, AI연구소, 샌프란시스코, gpt, chatgpt, dall-e, codex, gpt-oss, agents-SDK, responses-api, harmony-format, openai-cookbook]
related:
  - "[[openai-cookbook]]"
  - "[[karpathy]]"
  - "[[anthropic]]"
  - "[[ml-ai]]"
  - "[[mcp]]"
  - "[[agent-skills]]"
  - "[[harness]]"
source_count: 1
observed_source_refs: 4
inbound_count: 25
created: 2026-04-27
updated: 2026-04-27
verification_required: true
last_verified: 2026-04-29
verification_notes: "OpenAI 모델 릴리스(GPT-5/codex/gpt-oss/agents-sdk) 빠르게 변동 — 분기별 모델 라인업 재검증"
---

# OpenAI

## 개요

OpenAI는 2015-12 샌프란시스코에서 설립된 AI 연구·개발 회사로, GPT 시리즈 / ChatGPT / DALL-E / Codex / Sora / gpt-oss 등을 출시하며 현재 LLM 시장의 양대 산맥(Anthropic과 함께) 중 하나다. 본 위키에서는 [[openai-cookbook]]을 통한 OSS 거버넌스 패턴과, [[ml-ai]] 분야 표준 API 제공자 두 측면에서 다룬다.

## 주요 특징

### LLM 모델 라인업 (2026-04 기준 cookbook 태그 등장 빈도순)

- **GPT 시리즈** — 2018 GPT-1 → 2019 GPT-2 → 2020 GPT-3 (text-davinci-003) → 2023 GPT-4 → 2024 GPT-4o → 2025 GPT-5 시리즈 → 2026 GPT-5.1/5.2/5.4
- **o-series** — `o1` (2024) / `o3` 등 추론 강화 모델 (cookbook tag `reasoning` 12건)
- **gpt-oss** — 2025 첫 오픈 가중치 모델, harmony format 자체 대화 포맷 사용 (cookbook tag 13건)
- **임베딩** — text-embedding-ada-002 / text-embedding-3 시리즈 (cookbook tag `embeddings` 99건 — 가장 많음)
- **음성** — Whisper (STT) / TTS / Realtime API (cookbook tag `audio` 12건)
- **이미지** — DALL-E 시리즈 / GPT Image / Sora (영상)

### 주요 API / SDK

- **Chat Completions API** — 초기 표준 (cookbook tag `completions` 94건)
- **Responses API** — 2025 신규 (cookbook tag `responses` 32건). [[mcp]] 통합·도구 호출 통합 모델
- **Assistants API** — 사이드 stream
- **Function Calling** — 2023 출시 (cookbook tag `functions` 27건)
- **Agents SDK** — 2025 신규 (cookbook tag `agents-sdk` 16건). 본 위키의 [[agent-patterns]] Anthropic 5 패턴과 비교 대상
- **Realtime API** — 음성 양방향
- **Codex** — `gpt-5.2-codex` 등 코딩 전용 (cookbook tag `codex` 8건)

### 거버넌스·문서화 패턴

- **AGENTS.md "Recent Learnings"** — [[openai-cookbook]] AGENTS.md(5.5KB) 안에 운영 중 발견 함정·솔루션을 누적하는 살아있는 운영 노트. [[agent-skills]] 외부 채택 7단계 진화의 7번째이자 첫 살아있는 사례.
- **PLANS.md / ExecPlans** — Codex 7시간+ 단일 작업을 가능케 하는 living document 거버넌스. [[harness]] 6번째 거버넌스 축.
- **registry.yaml + authors.yaml** — cookbook.openai.com 정적 사이트 자동 생성용 메타데이터 거버넌스. 289개 콘텐츠 / 115명 저자 강제 등록.
- **agents.md (https://github.com/openai/agents.md)** — OpenAI가 별도 저장소로 운영하는 AGENTS.md 표준 정의 자체.

### Anthropic과의 비교

| 측면 | OpenAI | Anthropic |
|---|---|---|
| LLM 라인업 폭 | 매우 넓음 (GPT/o/gpt-oss/Whisper/DALL-E/Sora) | 좁고 깊음 (Claude 시리즈 단일) |
| 코드 협업 도구 | Codex CLI / `gpt-5.2-codex` | [[claude-code]] / [[claude-agent-sdk]] |
| 문서 거버넌스 | registry.yaml 정적 강제 + AGENTS.md 살아있는 운영 노트 | SKILL.md 패키지 + Constitution + Hooks |
| 표준 푸시 | AGENTS.md (별도 저장소) | Skills marketplace · MCP |
| OSS 모델 | gpt-oss (2025 첫 공개) | 없음 |
| 양식 | Cookbook 4년 ★73K | claude-cookbooks |

## 관련 개념

- [[ml-ai]]: OpenAI = 가장 대표적 LLM API 제공자
- [[agent-skills]]: AGENTS.md 별도 표준 저장소(agents.md) 운영 + cookbook AGENTS.md 살아있는 운영 노트 사례
- [[harness]]: PLANS.md ExecPlan 6번째 거버넌스 축 제공
- [[mcp]]: Anthropic 표준이지만 OpenAI Responses API에서도 통합 (cookbook tag `mcp` 8건)
- [[agent-patterns]]: Anthropic 5 패턴의 OpenAI 측 비교 대상 (Agents SDK)
- [[prompt-cache]]: Prompt_Caching101.ipynb / 201.ipynb 직접 사례
- [[context-engineering]]: Sessions API 패턴

## 출처

- [[openai-openai-cookbook]] — OpenAI 공식 4년차 cookbook 저장소 (★73K, 289 콘텐츠, MIT). 본 위키의 OpenAI 1차 자료.
- [[openai-openai-agents-python]] — OpenAI 공식 1년차 멀티 에이전트 Python SDK 저장소 (★25K, v0.14.6, MIT). 14회차 수집. cookbook이 메소드론 정의(가이드 단)라면 본 SDK는 그 메소드론을 자기 핵심 SDK 운영에 풀스택 적용한 본체 단 — `AGENTS.md = CLAUDE.md` 동기화 + `.agents/skills/` 9개 운영 SOP 스킬 + PLANS.md 5,485B + Codex hooks 통합 + `examples/agent_patterns/` 11종 패턴 reference 구현으로 OpenAI 거버넌스의 self-application 결정적 증거.

## 논쟁/모순

- (없음)

## 메모

- **회사 BI 적용**: OpenAI API를 c2spf-analytics에 도입할 때, cookbook의 registry.yaml에서 동일 태그(`embeddings`, `clustering`, `evals`)로 검색해 가장 최근 ipynb를 1차 자료로 활용. cookbook = 검색 가능한 사례 데이터베이스.
- **창립 인물**: Sam Altman(CEO) / Greg Brockman / Ilya Sutskever / Andrej [[karpathy]] (초창기, 후 Tesla 거쳐 독립) 등.
- **후속 수집 후보**:
  - https://github.com/openai/agents.md (AGENTS.md 표준 자체)
  - https://github.com/openai/openai-python (공식 Python SDK)
  - ~~https://github.com/openai/openai-agents-python~~ → **수집 완료 (14회차, 2026-04-28)** → [[openai-agents-python]]
  - https://github.com/openai/codex (Codex CLI)
  - https://github.com/openai/evals (Evals 프레임워크)
  - https://github.com/openai/whisper, openai/tiktoken, openai/gpt-oss
