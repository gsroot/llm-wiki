---
title: "LangChain"
type: entity
entity_type: tool
tags: [langchain, LLM-framework, agent, langchain-inc, monorepo, langsmith, deepagents, agents-md, claude-md, 17회차, 에이전트]
related:
  - "[[langgraph]]"
  - "[[openai-agents-python]]"
  - "[[ml-ai]]"
  - "[[mcp]]"
  - "[[uv]]"
  - "[[langchain-ai-langchain]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
created: 2026-04-28
updated: 2026-04-28
verification_required: true
last_verified: 2026-04-29
verification_notes: "LangChain Inc. 리브랜딩 + langchain_v1 채택률 + monorepo 구조 변경 — 분기별 재검증"
---

# LangChain

## 개요

**The agent engineering platform** — 2022년 10월 Harrison Chase가 출범한 LLM 애플리케이션 프레임워크. 초기 "프롬프트 체이닝 도구"에서 2024-2025년 **"agent engineering platform"으로 재포지셔닝**. monorepo 구조 + uv 의존성 + AGENTS.md=CLAUDE.md 동기화로 LLM 협업 표준 컨벤션 채택.

## 주요 특징

### 정체성 변화
- **2022 출범**: "framework for LLM apps" (프롬프트 체이닝 표준)
- **2024-2025**: agents 중심 재포지셔닝 ([[openai-agents-python]] 등 경쟁 압박)
- **현재 v1**: "agent engineering platform" + LangGraph 위에 빌드된 `create_agent`

### 생태계 구성 (5개)
1. **LangChain** (이 entity) — 코어 프레임워크
2. **[[langgraph]]** — low-level orchestration (별도 repo)
3. **DeepAgents** — plan + subagents + 파일시스템
4. **LangSmith** — agent evals + observability + debugging (SaaS)
5. **LangSmith Deployment** — long-running, stateful workflow 배포

### 모노레포 구조
```
libs/
├── core/             # 기반 추상화 (langchain-core)
├── langchain/        # legacy (no new features)
├── langchain_v1/     # active 패키지
├── partners/         # OpenAI/Anthropic/Ollama 등
├── text-splitters/
├── standard-tests/
└── model-profiles/
```

### 거버넌스
- **회사**: LangChain Inc. (창업자 Harrison Chase)
- **License**: MIT
- **모델**: OSS + SaaS 듀얼 (OSS=LangChain, SaaS=LangSmith)
- **AGENTS.md = CLAUDE.md 동기화** (292줄, 14회차 OpenAI Agents Python 패턴 확산)

### 기술 스택
- 언어: Python 3.10+ (별도 langchain.js)
- 의존성: [[uv]]
- 린터: [[ruff]]
- 타입: mypy
- 테스트: pytest

### partners/ 모델
- 1급 통합: OpenAI, Anthropic, Ollama
- 별도 repo: `langchain-google`, `langchain-aws` (monorepo 외부)
- → 벤더 락인 회피 + 모듈성

## 관련 개념

- [[langgraph]]: LangChain의 저수준 엔진 (LangChain v1의 `create_agent`가 LangGraph prebuilt)
- [[openai-agents-python]]: 직접 경쟁 (OpenAI 진영의 stateful agent SDK)
- [[mcp]]: partners/ 경유 통합 (Anthropic 등)
- [[agent-skills]]: AGENTS.md=CLAUDE.md 패턴 — LLM 협업 표준
- [[ml-ai]]: LLM-powered application의 핵심 추상화 계층
- [[uv]]: monorepo 의존성 관리 표준

## 의사결정 컨텍스트 (raw 인용)

> "2022년 10월 출범 후 LLM 프레임워크의 사실상 표준으로 자리잡은 monorepo. 'agent engineering platform' 슬로건과 함께 v1 출시 + AGENTS.md=CLAUDE.md 동기화로 LLM 협업 표준 패턴 채택."
> — [[langchain-ai-langchain]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] LLM 프레임워크 영역의 사실상 표준. [[matechat|MateChat 사이드 프로젝트]] AI 채팅 분석 모듈에서 후보 검토. [[langgraph]] 산하 + [[deepagents]] 직접 종속. **AGENTS.md=CLAUDE.md 동기화 패턴**은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 운영 표준 — [[ruff]]·[[uv]]·[[fastmcp]] 등과 같은 동기화 모델 채택.

## 출처

- [[langchain-ai-langchain]] — 17회차 수집, README + AGENTS.md (376줄)

## 메모

- **석근님 사이드 프로젝트 적용**: AI 비서 프로젝트의 "프레임워크 선택"에서 LangChain은 최대 통합 폭. 단점은 추상화 깊이 → 디버깅 난이도. 단순 프로젝트는 [[openai-agents-python]] 또는 [[fastmcp]] 직접 사용이 더 빠를 수 있음.
- **LangSmith 의존성 주의**: production observability를 LangSmith에 의존하면 SaaS 락인. self-hosted 옵션 확인 필요.
- **classic vs v1**: `langchain` (classic, no new features)에서 마이그레이션 부담 있음. 새 프로젝트는 `langchain_v1` 시작.
- 향후 위키 확장: LangSmith 별도 entity, langchain.js, DeepAgents 별도 entity (18회차 예정).
