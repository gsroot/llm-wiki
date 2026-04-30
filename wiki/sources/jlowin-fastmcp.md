---
title: jlowin/fastmcp — The standard framework for MCP
type: source
source_type: article
source_url: https://github.com/jlowin/fastmcp
raw_path: raw/articles/jlowin-fastmcp/
author: Jeremiah Lowin (Prefect)
date_published: 2024-04-01
date_ingested: 2026-04-28
tags:
- fastmcp
- mcp
- prefect
- jlowin
- model-context-protocol
- agents-md
- claude-md
- prefect-horizon
related:
- '[[fastmcp]]'
- '[[mcp]]'
- '[[ml-ai]]'
- '[[agent-skills]]'
confidence: high
inbound_count: 15
cited_by:
- '[[agent-frameworks-matrix]]'
- '[[agent-skills]]'
- '[[fastmcp]]'
- '[[mcp]]'
- '[[ml-ai]]'
- '[[oss-saas-dual]]'
cited_by_count: 6
aliases:
- Jlowin Fastmcp
- jlowin fastmcp
- jlowin/fastmcp — The standard framework for MCP
---

# jlowin/fastmcp — The standard framework for MCP

## 한줄 요약

> **MCP 서버 70%가 사용**하는 표준 프레임워크. 1.0이 2024년 공식 MCP Python SDK에 통합 완료 후, **2.0으로 standalone 재시작**한 OSS 진화 패턴. Prefect가 후원.

## 핵심 내용

### 정체성
- **"Move fast and make things"** — Prefect의 모토 차용
- Python ≥3.10 프레임워크
- Model Context Protocol(MCP) 서버 + 클라이언트 + Apps 빌드용
- 일일 100만 다운로드, 모든 언어 MCP 서버의 70% 점유
- 저자: Jeremiah Lowin (Prefect 창업자)

### 1.0 → 2.0 진화 (OSS 졸업의 또 다른 형태)
- **FastMCP 1.0** (2024 초) → **2024년 공식 MCP Python SDK에 통합**
- **현재 standalone v2.0** — 새 기능 + 더 많은 추상화
- 즉 1.0은 "졸업 후 표준에 흡수", 2.0은 "다음 세대 standalone"
- 9번째 OSS 거버넌스 모델: **"공식 SDK에 흡수 → 다음 버전으로 재시작"**

### 3-pillars (FastMCP의 핵심 추상화)
1. **Servers** — Python 함수를 MCP-compliant tool/resource/prompt로 wrap
2. **Apps** — 도구가 대화 안에서 직접 렌더링되는 interactive UI
3. **Clients** — 모든 MCP 서버 연결 (local/remote, programmatic/CLI)

### Quickstart
```python
from fastmcp import FastMCP

mcp = FastMCP("Demo 🚀")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

if __name__ == "__main__":
    mcp.run
```

### 저장소 구조
```
src/fastmcp/
├── server/         # 서버 구현
│   ├── auth/       # 인증 제공자
│   └── middleware/ # 에러 처리, 로깅, rate limiting
├── client/
│   └── auth/       # 클라이언트 인증
├── tools/          # Tool 정의
├── resources/      # Resource + Resource Template
├── prompts/        # Prompt 템플릿
├── cli/            # CLI 명령
├── apps/           # Apps (대화 내 UI)
├── contrib/        # 커뮤니티 기여
├── experimental/   # 실험 기능
└── utilities/      # 공유 유틸 (FastMCPComponent 베이스 클래스)
```

### `FastMCPComponent` 정체성 모델
- 모든 MCP 객체의 공통 기반 클래스 (`src/fastmcp/utilities/components.py`)
- 공유 표면: `name`, `version`, `tags`, `meta`, `key`
- `key` property가 canonical MCP identity (type + identifier + version 인코딩)
- 즉 **버전 차이가 다른 컴포넌트로 처리됨** — 같은 `name`이라도 `v1.0`과 `v2.0`은 다른 key

### Prefect Horizon (Enterprise gateway)
- FastMCP 팀이 만든 **enterprise MCP gateway** (별도 SaaS)
- GitHub에서 FastMCP 서버 배포 + branch preview + instant rollback
- 사내 MCP 서버 private registry
- SSO + tool-level RBAC
- 감사 로그 + observability + governance
- 승인된 도구를 팀·에이전트별로 remix하는 endpoint

### AGENTS.md = CLAUDE.md (symlink, 168줄)
- "AGENTS.md is a symlink to this file. Edit CLAUDE.md directly."
- 매우 구체적 운영 규칙:
 - `uv sync` → `uv run pytest -n auto` → `uv run prek run --all-files`
 - prek (pre-commit hook) 필수
 - `[DRAFT]`/`[DNM]` 라벨 가진 PR은 절대 머지 금지 (case-insensitive)
 - **"Be constructively skeptical of bot review comments on your own PRs"** — bot review에 대한 메타 가이던스
 - "**The title pun is critical**" — release 네이밍 문화
 - "Improvements = enhancements (not features)"

### License
- Apache 2.0 (PrefectHQ가 후원)

## 주요 인사이트

1. **OSS 진화의 9번째 모델**: "1.0이 공식 SDK에 흡수 → 2.0으로 재시작" — 일반적인 fork/abandon이 아닌 **자발적 표준화 후 재진입**. ASF PMC를 8번째로 추가한 후 9번째 모델.
2. **70% 점유율의 의미**: MCP가 표준 프로토콜이지만 실제 구현 다수가 FastMCP라는 것은, **Anthropic이 정한 프로토콜 + Prefect가 정한 구현 표준**의 이중 표준. 즉 [[mcp]] 페이지는 프로토콜만으로 충분치 않고 FastMCP 사실 표준 언급 필수.
3. **Bot review에 대한 메타-가이던스**: AGENTS.md에 "bot review 자체에 비판적이어라"라는 항목이 있다는 것은, **CodeRabbit/Codex/Claude bot이 일상화된 시대의 새 워크플로우**. `code-reviewer` 에이전트와 인간 리뷰의 새 균형.
4. **`FastMCPComponent.key`의 versioned identity**: 같은 도구의 다른 버전을 별개로 처리하는 모델은, **MCP 도구 호환성 매트릭스를 versioned하게 관리**하는 인프라 — 향후 MCP 도구 마켓플레이스의 핵심 데이터 모델.
5. **Prefect Horizon은 FastMCP의 Polars Cloud / MotherDuck**: OSS + SaaS 듀얼 모델. 이로써 발견한 **OSS+SaaS 듀얼 패턴 4번째 사례** ([[polars]]/[[duckdb]]/[[langchain]]+LangSmith/[[fastmcp]]+Horizon).

## 관련 엔티티/개념

- [[fastmcp]] — 본 소스의 대상
- [[mcp]] — FastMCP가 구현하는 프로토콜
- [[openai-agents-python]] — agents-python도 MCP 코어 의존
- [[langchain]] — partners/ 경유 MCP 통합
- [[agent-skills]] — AGENTS.md=CLAUDE.md 패턴 5번째 적용 ([[openai-agents-python]] / langchain / langgraph / fastmcp)

## 인용할 만한 구절

> "FastMCP 1.0 was incorporated into the official MCP Python SDK in 2024. Today, the actively maintained standalone project is downloaded a million times a day, and some version of FastMCP powers 70% of MCP servers across all languages."
> — README.md

> "Be constructively skeptical of bot review comments on your own PRs."
> — AGENTS.md (Git & CI)

> "The title pun is critical. Titles follow `v<version>: <pun>` where the pun relates to the most important theme of the release."
> — AGENTS.md (Releases)

## 메모

- LLM 인프라 수집의 마지막. MCP 생태계의 사실 표준.
- 석근님 사이드 프로젝트 활용: 개인 MCP 서버 (메모/일정/문서) → FastMCP가 가장 빠른 구현 경로. uv + FastMCP + Prefect Horizon으로 sandbox 가능.
- 향후 확장: Apps의 interactive UI 패턴 별도 페이지, FastMCP v3 변경사항, Horizon vs LangSmith 비교.
