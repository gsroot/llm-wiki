---
title: "langchain-ai/langchain — The agent engineering platform"
type: source
source_type: article
source_url: "https://github.com/langchain-ai/langchain"
raw_path: "raw/articles/langchain-ai-langchain/"
author: "LangChain Inc. (Harrison Chase 외)"
date_published: 2022-10-17
date_ingested: 2026-04-28
tags: [langchain, llm-framework, agent, monorepo, langchain-inc, langsmith, agents-md, claude-md, 17회차]
related:
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[ml-ai]]"
  - "[[agent-skills]]"
  - "[[mcp]]"
confidence: high
---

# langchain-ai/langchain — The agent engineering platform

## 한줄 요약

> **2022년 10월 출범 후 LLM 프레임워크의 사실상 표준**으로 자리잡은 monorepo. "agent engineering platform" 슬로건과 함께 v1 출시 + AGENTS.md=CLAUDE.md 동기화로 LLM 협업 표준 패턴 채택.

## 핵심 내용

### 정체성
- **The agent engineering platform** (README 첫 줄)
- LLM-powered application + agent를 빌드하기 위한 프레임워크
- "interoperable components + 3rd-party integrations"가 핵심
- 슬로건 변화: 초기 "framework for LLM apps" → 현재 "agent engineering platform"

### Quickstart (현재 v1)
```bash
pip install langchain
# or
uv add langchain
```

```python
from langchain.chat_models import init_chat_model
model = init_chat_model("openai:gpt-5.4")
result = model.invoke("Hello, world!")
```

### 모노레포 구조
```
langchain/
├── libs/
│   ├── core/             # langchain-core: 기반 추상화
│   ├── langchain/        # langchain-classic (legacy, no new features)
│   ├── langchain_v1/     # langchain (active)
│   ├── partners/         # 3rd-party 통합
│   │   ├── openai/
│   │   ├── anthropic/
│   │   ├── ollama/
│   │   └── ...
│   ├── text-splitters/
│   ├── standard-tests/
│   └── model-profiles/
├── .github/
└── README.md
```

- **별도 repo로 분리된 통합**: `langchain-google`, `langchain-aws` (필요 시 monorepo 외부에서 클론)
- **개발 도구**: uv (의존성) / make (작업) / ruff (린트) / mypy (타입) / pytest (테스트)
- **편집 가능 설치**: `[tool.uv.sources]`로 로컬 개발

### LangChain 생태계 (5개)
1. **Deep Agents** — plan + subagents + 파일시스템을 갖춘 복잡 작업용 에이전트
2. **LangGraph** — low-level orchestration (별도 repo, [[langgraph]] 참조)
3. **Integrations** — 채팅·임베딩 모델, 도구·툴킷
4. **LangSmith** — agent evals + observability + debugging (제품)
5. **LangSmith Deployment** — long-running, stateful workflow 배포 플랫폼

### 6가지 가치 제안
1. Real-time data augmentation (다양한 데이터 소스 통합)
2. Model interoperability (모델 swap 용이)
3. Rapid prototyping (modular 컴포넌트)
4. Production-ready features (LangSmith)
5. Vibrant community
6. Flexible abstraction layers (high-level chain ↔ low-level component)

### AGENTS.md = CLAUDE.md (동기화 패턴, 292줄)
- 모노레포 전역 개발 가이드
- 14회차 OpenAI Agents Python에서 발견된 패턴이 **LangChain Org에서 확산** (LangChain + LangGraph + DeepAgents 모두 채택)
- 핵심 규칙:
  - uv sync --all-groups
  - make test / make lint / make format
  - mypy 통과
  - 각 패키지는 독립 versioned (pyproject.toml + uv.lock)

### License
- MIT

## 주요 인사이트

1. **"agent engineering platform" 포지셔닝**: 초기에는 LLM chain 구축 도구였으나, 2024-2025년을 거치며 "agent" 중심으로 재포지셔닝. [[openai-agents-python]] 출현 이후 경쟁 압박이 가속화.
2. **LangChain Org의 거버넌스 패턴 확산**: monorepo (libs/) + AGENTS.md=CLAUDE.md sync + uv 채택 — 14회차 [[openai-agents-python]]와 거의 같은 패턴. **LLM 코딩 에이전트 협업 표준이 빠르게 수렴 중**.
3. **partners/ 패턴**: 모델 제공자별 통합을 별도 패키지로 분리. OpenAI/Anthropic/Ollama가 1급, Google/AWS는 별도 repo. **벤더 락인 회피의 모듈성 설계**.
4. **legacy + active 분리**: `langchain` (classic, no new features) + `langchain_v1` (active) 공존 — 마이그레이션 부담 최소화 + 새 API 동시 진행. v0 → v1 진화 패턴.
5. **LangSmith는 별도 SaaS 제품**: OSS는 LangChain (코드), SaaS는 LangSmith (관측성·평가·배포) — Polars Cloud / MotherDuck과 같은 OSS+SaaS 듀얼 모델.

## 관련 엔티티/개념

- [[langchain]] — 본 소스의 대상
- [[langgraph]] — LangChain의 low-level orchestration 형제
- [[openai-agents-python]] — 직접 경쟁 프레임워크
- [[mcp]] — LangChain v1이 MCP 통합 지원 (partners/anthropic 등)
- [[agent-skills]] — AGENTS.md=CLAUDE.md 패턴은 14회차 발견의 9번째 진화 단계
- [[uv]] — LangChain monorepo 의존성 관리

## 인용할 만한 구절

> "LangChain is a framework for building agents and LLM-powered applications. It helps you chain together interoperable components and third-party integrations to simplify AI application development — all while future-proofing decisions as the underlying technology evolves."
> — README.md

> "Swap models in and out as your engineering team experiments to find the best choice for your application's needs."
> — README.md (Why use LangChain)

## 메모

- 17회차 LLM 인프라 수집의 핵심.
- LangChain의 "agent platform" 슬로건은 2024년 후반 LLM 시장이 "에이전트"로 재정의되면서 발생한 포지션 변화. 이전 슬로건 "framework for LLM apps"는 이제 부차적.
- 향후 위키 확장 후보: LangSmith 별도 entity 페이지, LangServe deprecated 여부, langchain.js의 위치, langgraph의 sub-agent 패턴.
