---
title: "Claude Managed Agents"
type: entity
entity_type: service
tags: [claude-managed-agents, cma, anthropic, hosted-runtime, agent, stateful-agent, sandbox, human-in-the-loop]
related: [[anthropic]], [[claude-agent-sdk]], [[claude-code]], [[agent-patterns]], [[harness]], [[mcp]], [[context-engineering]], [[token-economy]]
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# Claude Managed Agents

## 개요

**Claude Managed Agents(CMA)**는 Anthropic의 hosted runtime for stateful, tool-using agents다. 에이전트와 sandboxed environment를 한 번 정의하고, 이후 세션 단위로 파일·도구 상태·대화를 영속시키며 실행하는 구조다.

[[claude-agent-sdk]]가 "에이전트를 만드는 SDK"라면, CMA는 "에이전트를 운영하는 PaaS"에 가깝다. 로컬 [[claude-code]] 하네스가 사람이 직접 세션을 운전하는 모델이라면, CMA는 서버 사이드에서 세션·환경·권한·휴먼 승인 흐름을 관리한다.

## 주요 특징

- **상태 영속 세션**: 파일, 도구 상태, conversation이 세션 사이에서 유지된다.
- **Sandboxed environment**: 에이전트 실행 환경을 분리해 파일 마운트와 도구 접근을 제어한다.
- **Human-in-the-loop**: 비용 승인, 머지 승인, 위험 작업 등에서 `decide()` / `escalate()` 같은 사용자 결정을 흐름 안에 넣는다.
- **운영형 워크플로우**: issue → fix → PR → CI → review → merge, SRE incident response, data analyst report 같은 장기 작업을 예제로 다룬다.
- **서버사이드 운영 기능**: 프롬프트 버전 관리, rollback, vault-backed credentials, `session.status_idled` 웹훅 패턴.

## 왜 중요한가

개인 에이전트나 회사 BI 에이전트를 실제 서비스로 배포하려면 "모델 호출"보다 **세션 상태, 권한, 자격 증명, 사용자 승인, 실패 복구**가 더 어려워진다. CMA는 이 운영 층을 Anthropic이 제품화한 사례다.

석근의 관심사 기준으로는 개인 비서 AI와 사내 BI 에이전트 PoC의 비교 기준점이 된다. 단순히 Claude API를 호출하는 것과, 세션을 가진 agent runtime을 운영하는 것은 추상화 레벨이 다르다.

## 관련 개념

- [[claude-agent-sdk]]: CMA와 함께 Anthropic의 에이전트 개발·운영 스택을 이룬다.
- [[harness]]: CMA는 hosted harness / runtime 층.
- [[agent-patterns]]: Orchestrator-Workers, Evaluator-Optimizer 같은 장기 워크플로우를 실제 운영으로 옮긴다.
- [[mcp]]: 운영 환경에서 GitHub, Slack, 데이터 소스 등 외부 도구 연결에 사용된다.

## 출처

- [[anthropics-claude-cookbooks]] — `managed_agents/` 8개 노트북과 운영 패턴 정리.

## 논쟁/모순

현재 위키 안에서 CMA에 대한 상충 정보는 없음. 다만 hosted runtime이므로 비용·데이터 보안·사내망 접근성은 실제 도입 전에 별도 검토가 필요하다.

## 메모

- "에이전트의 백엔드 hosting"이라는 표현이 위키 내 요약으로 가장 적합하다.
