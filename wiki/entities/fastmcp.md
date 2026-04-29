---
title: "FastMCP"
type: entity
entity_type: tool
tags: [fastmcp, mcp, prefect, jlowin, model-context-protocol, agents-md, claude-md, prefect-horizon, oss-evolution, 17회차]
related:
  - "[[mcp]]"
  - "[[ml-ai]]"
  - "[[agent-skills]]"
  - "[[openai-agents-python]]"
  - "[[langchain]]"
  - "[[jlowin-fastmcp]]"
  - "[[seokgeun-stack-guide]]"
source_count: 1
observed_source_refs: 4
inbound_count: 26
created: 2026-04-28
updated: 2026-04-28
verification_required: true
last_verified: 2026-04-29
verification_notes: "MCP 70% 점유 변동 + 2.0 standalone 안정성 + Prefect Horizon 통합 — 분기별 재검증"
---

# FastMCP

## 개요

**The standard framework for MCP** — Jeremiah Lowin (Prefect)이 개발한 Model Context Protocol Python 프레임워크. 일일 100만 다운로드, **MCP 서버의 70% 점유**. **1.0이 2024년 공식 MCP Python SDK에 통합 → 2.0 standalone 재시작**으로 OSS 진화의 새 패턴 정립.

## 주요 특징

### 진화 (OSS 거버넌스 9번째 모델)
- **FastMCP 1.0** (2024 초) — 새 프레임워크
- **2024년**: 1.0이 공식 MCP Python SDK에 통합 (졸업)
- **현재 standalone v2.0** — 다음 세대 추상화 + 더 풍부한 기능
- 의미: "공식 표준에 흡수 → 다음 버전으로 재시작"

### 3-pillars
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
    mcp.run()
```

### `FastMCPComponent` versioned identity
- 모든 MCP 객체의 공통 베이스 클래스
- `key` property = canonical MCP identity (type + identifier + version)
- → 같은 `name`이라도 v1과 v2는 다른 컴포넌트로 처리

### 저장소 구조
```
src/fastmcp/
├── server/   ├── auth/, middleware/
├── client/   └── auth/
├── tools/    resources/    prompts/
├── apps/     # 대화 내 UI 렌더링
├── cli/
├── contrib/  experimental/
└── utilities/  # FastMCPComponent 베이스
```

### 기술 스택
- Python 3.10+
- 의존성: [[uv]]
- 린터·포맷터·타입: prek (Ruff + Prettier + ty)
- 테스트: pytest -n auto (병렬)

### 거버넌스
- **회사**: PrefectHQ (Jeremiah Lowin)
- **License**: Apache 2.0
- **AGENTS.md = CLAUDE.md symlink** (168줄)
- **Prefect Horizon** = enterprise MCP gateway (별도 SaaS)

### Prefect Horizon (Enterprise gateway)
- GitHub에서 FastMCP 서버 배포 + branch preview + instant rollback
- 사내 MCP 서버 private registry
- SSO + tool-level RBAC + 감사 로그
- 승인된 도구를 팀·에이전트별로 remix하는 endpoint

### 메타-가이드 (AGENTS.md 발견)
- "Be constructively skeptical of bot review comments on your own PRs" — bot review 자체에 대한 가이던스
- "The title pun is critical" — release 네이밍 문화
- "Improvements = enhancements (not features)" — PR 라벨 규칙

## 관련 개념

- [[mcp]]: FastMCP가 구현하는 프로토콜 — Anthropic이 정한 표준 + Prefect가 정한 사실 구현 표준
- [[openai-agents-python]]: agents-python도 MCP 코어 의존
- [[langchain]]: partners/ 경유 MCP 통합
- [[agent-skills]]: AGENTS.md=CLAUDE.md 패턴 5번째 적용
- [[ruff]]: prek 통한 통합 (Ruff + Prettier + ty)
- [[uv]]: 의존성 관리

## 의사결정 컨텍스트 (raw 인용)

> "MCP 서버 70%가 사용하는 표준 프레임워크. 1.0이 2024년 공식 MCP Python SDK에 통합 완료 후, 2.0으로 standalone 재시작한 OSS 진화 패턴. Prefect가 후원."
> — [[jlowin-fastmcp]] 한줄 요약

[[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] [[mcp]] 프로토콜 영역의 사실상 표준. [[matechat|MateChat 사이드 프로젝트]] 39 SKILL 운영에서 외부 도구 통합 후보. **공식 SDK 흡수 후 standalone 재시작**은 OSS 진화의 드문 패턴 — [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 5축의 mcp 진화 사례 (claude-cookbooks·spec-kit과 함께 [[agent-skills]] 외부 도구 표준화의 한 축).

## 출처

- [[jlowin-fastmcp]] — 17회차 수집, README + AGENTS.md (288줄)

## 메모

- **석근님 사이드 프로젝트 적용**: 개인 MCP 서버 (메모/일정/문서/Notion/Confluence 통합) 빌드의 가장 빠른 경로. uv + FastMCP + Cursor/Claude Code 클라이언트 sandbox.
- **vs MCP Python SDK 직접**: 1.0이 SDK에 흡수됐지만, 실무는 FastMCP 2.0 standalone이 더 풍부 (Apps, FastMCPComponent.key, prek 등). SDK 직접 사용은 라이브러리 개발자용.
- **70% 점유의 의미**: 단순 Anthropic 프로토콜이 아닌 사실 표준이 형성됨. 대안 프레임워크는 차별화가 매우 어려운 상황.
- 향후 위키 확장: Prefect entity, Prefect Horizon vs LangSmith 비교, MCP Apps interactive UI 별도 페이지, prek toolchain.
