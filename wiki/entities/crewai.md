---
title: "CrewAI"
type: entity
entity_type: tool
related:
  - "[[langchain]]"
  - "[[langgraph]]"
  - "[[pydantic-ai]]"
  - "[[agent-patterns]]"
  - "[[oss-saas-dual]]"
  - "[[crewaiinc-crewai]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 2
inbound_count: 23
created: 2026-04-28
updated: 2026-04-28
tags: [crewai, multi-agent, role-playing, flows, crews, langchain-independent, oss-saas-dual, control-plane, 18회차]
cited_by_count: 14
---

# CrewAI

**Role-playing 멀티 에이전트 협업 프레임워크** — LangChain 의존성 zero, 자체 abstraction stack. **Crews + Flows** 듀얼 메타포 + **Crew Control Plane SaaS**. 50K+ stars, MIT, 100,000+ 인증 개발자.

## 기본 정보

- **저장소**: [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)
- **언어**: Python
- **License**: MIT
- **PyPI**: `pip install crewai`
- **회사**: CrewAI Inc.
- **SaaS**: Crew Control Plane ([app.crewai.com](https://app.crewai.com))
- **학습**: [learn.crewai.com](https://learn.crewai.com) — 100,000+ 인증 개발자

## 역할 — "Crews + Flows"

CrewAI는 두 가지 메타포를 1급 추상화로 제공:

| 메타포 | 목적 | 비유 |
|--------|------|------|
| **Crews** | 자율성 + 협업 지능 | 사람 팀 (각자 역할/도구) |
| **Flows** | enterprise 정밀 제어, event-driven | 조립 라인 |

→ LangGraph의 "graph + production runtime"과 대응. CrewAI는 **두 메타포를 명시적으로 분리**.

## "독립" 자기 정체성

> "**completely independent of LangChain or other agent frameworks**"

→ README 첫 문장에 LangChain 의존성 없음을 박아둠. **17회차의 LangChain 진영 (LangChain/LangGraph/DeepAgents)과 명확히 대립**.

## 5번째 OSS+SaaS 듀얼 모델

| 사례 | OSS | SaaS |
|------|-----|------|
| Polars | `polars` | Polars Cloud |
| DuckDB | `duckdb` | MotherDuck |
| LangChain | `langchain` | LangSmith |
| FastMCP | `fastmcp` | Prefect Horizon |
| **CrewAI** | `crewai` | **Crew Control Plane** ← 신규 |

CrewAI AMP Suite의 핵심 기능:
- Tracing & Observability
- Unified Control Plane
- 24/7 Support
- On-premise + Cloud 듀얼

## "학습 인증 → SaaS 깔때기"

CrewAI는 **유일하게 학습 인증을 비즈니스 모델 깔때기에 통합**:

```
learn.crewai.com (100K+ 인증)
       ↓
  crewai (OSS, 50K stars)
       ↓
app.crewai.com (Control Plane SaaS)
```

→ LangChain Academy/PydanticAcademy도 학습 코스 있으나, **인증 규모 명시 + SaaS 직결 구조**는 CrewAI가 유일.

## 대안 / 비교

| 도구 | 강점 | 약점 |
|------|------|------|
| **CrewAI** | role-playing 자연스러움, 학습 자료 풍부, LangChain 독립 | LangChain 생태계와 단절 (모델 swap은 자체 통합) |
| [[langgraph]] | state graph, durable execution 1급 | 복잡 abstraction |
| [[deepagents]] | 한 줄 셋업 | LangGraph 종속 |
| [[pydantic-ai]] | type-safe, model-agnostic | abstraction 다층 |
| [[openai-agents-python]] | 11종 패턴 reference | OpenAI 락인 |

## 통합

- **모델**: 자체 통합 (OpenAI/Anthropic/Gemini/local 모두 지원)
- **MCP**: 직접 구현
- **관측**: Crew Control Plane (자체 SaaS) + OpenTelemetry

## 사용 예

```python
from crewai import Agent, Task, Crew

researcher = Agent(
    role="시장 분석가",
    goal="게임 산업 트렌드 분석",
    backstory="10년 경력의 게임 산업 분석가",
)
writer = Agent(role="보고서 작성자", goal="...", backstory="...")

task1 = Task(description="2026 게임 산업 동향 조사", agent=researcher)
task2 = Task(description="조사 결과로 보고서 작성", agent=writer)

crew = Crew(agents=[researcher, writer], tasks=[task1, task2])
result = crew.kickoff()
```

→ **role-playing이 명시적**. LangGraph는 노드/엣지로, CrewAI는 사람 팀 메타포로 작성.

## 의사결정 컨텍스트 (raw 인용)

> "CrewAI is a lean, lightning-fast Python framework built entirely from scratch—completely independent of LangChain or other agent frameworks. Role-playing 협업 메타포 + Flows enterprise 아키텍처 + Crew Control Plane SaaS. 50K+ stars, MIT, 100,000+ 인증 개발자."
> — [[crewaiinc-crewai]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] multi-agent 프레임워크 영역. [[matechat|MateChat 사이드 프로젝트]] AI 채팅 분석 multi-agent 후보 (역할 분담 시나리오). [[langchain]]·[[langgraph]]·[[deepagents]]와 [[agent-frameworks-matrix]] 6 프레임워크 비교. **Role-playing + OSS+SaaS dual 모델**은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 [[harness]] 진화 + 거버넌스 dual 사례 — [[oss-saas-dual]] 종합 분석 참조.

## 출처

- [[crewaiinc-crewai]] — CrewAI (18회차)

## 관련

- [[langchain]] — 명시적 대립 프레임워크
- [[langgraph]] — 가장 직접적 경쟁자
- [[oss-saas-dual]] — 5번째 사례
- [[agent-patterns]] — 멀티 에이전트 협업 패턴
