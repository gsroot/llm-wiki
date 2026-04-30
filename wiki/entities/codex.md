---
title: Codex (OpenAI 클라우드 자율 코딩 에이전트)
type: entity
entity_type: tool
aliases:
- Codex
- codex
- OpenAI Codex
- codex-cli
tags:
- codex
- openai
- coding-agent
- cloud-agent
- agents-md
- pull-request-automation
- agent-patterns
related:
- "[[openai]]"
- "[[claude-code]]"
- "[[github]]"
- "[[microsoft]]"
- "[[agent-skills]]"
- "[[agent-patterns]]"
- "[[harness]]"
- "[[openai-cookbook]]"
- "[[openai-agents-python]]"
- "[[openai-chatgpt-codex-guide]]"
source_count: 1
observed_source_refs: 2
inbound_count: 16
created: 2026-04-30
updated: 2026-04-30
verification_required: true
last_verified: 2026-04-30
verification_notes: "Codex 제품 라인업·요금제·기능은 OpenAI가 빠르게 갱신 중. 90일마다 wikidocs 책·OpenAI 공식 문서로 재검증."
cited_by_count: 10
---

# Codex (OpenAI 클라우드 자율 코딩 에이전트)

## 개요

**Codex**는 [[openai]]가 공개한 **클라우드 기반 자율 코딩 에이전트**다. 개발자가 채팅창에 자연어로 요청하면, Codex가 [[github]] 리포지토리를 탐색해 코드를 작성하고 **Pull Request를 직접 생성**한다. 2021년 GPT-3 기반 코드 생성 모델로 첫 공개됐고, 이후 GitHub Copilot의 엔진으로 발전, 2025~2026년에 들어 자율 클라우드 에이전트 형태로 진화했다.

owner 입장에서 의미는 **3대 코딩 도구의 보완재 포지셔닝** — Codex는 IDE 인라인([[github]] Copilot) 영역도, 로컬 터미널 페어 프로그래밍([[claude-code]]) 영역도 아닌, **클라우드 비동기 백그라운드 자율 태스크** 영역을 차지한다.

## 주요 특징

### 3대 코딩 도구 포지셔닝

| 도구 | 실행 위치 | 인터랙션 | 적합 작업 |
|---|---|---|---|
| **GitHub Copilot** | IDE (VS Code, JetBrains 등) | 인라인 자동완성·인라인 채팅 | 타이핑 중 즉시 보조, 줄 단위 제안 |
| **[[claude-code]]** | 로컬 터미널 | 대화형 페어 프로그래밍 | 다파일 리팩토링, 디버깅, 탐색적 작업 |
| **Codex** | 클라우드 (브라우저·CLI) | 비동기 태스크 → PR 자동 생성 | 백그라운드 기능 추가·버그 수정·테스트 작성 |

세 도구는 **대체재가 아닌 보완재**. 동일 개발자가 IDE에선 Copilot, 터미널에선 Claude Code, 클라우드에선 Codex를 병행 활용 가능.

### 핵심 워크플로

1. **요청 입력**: ChatGPT 인터페이스 또는 codex CLI에 자연어로 태스크 입력
2. **저장소 탐색**: Codex가 연결된 GitHub 리포 전체를 자율 탐색·이해
3. **AGENTS.md 참조**: 프로젝트 루트의 `AGENTS.md` (코딩 컨벤션·테스트 명령 정의)를 읽어 가이드라인 준수
4. **Setup Script 실행**: 샌드박스 부팅 시 의존성 설치·환경 구성
5. **코드 작성·수정**: 멀티 파일 변경, 테스트 작성, 빌드 검증
6. **PR 생성**: 변경 내용을 묶어 GitHub에 Pull Request 자동 제출

### AGENTS.md 컨벤션

Codex는 **`AGENTS.md`** 파일을 프로젝트 컨텍스트의 single source of truth로 사용. 이 파일은 [[agent-skills]]의 13단계 vendor-neutral 진화 흐름과 직접 결합된다 — [[openai-cookbook]], [[openai-agents-python]] 등 OpenAI 자체 레포뿐 아니라 [[fastapi]], [[astral-sh-uv|uv]], [[langchain]], [[pydantic-ai]] 등 6+ OSS가 같은 컨벤션을 채택해 사실상 표준화 진행 중.

`AGENTS.md` 표준 구조:
- 프로젝트 개요
- 기술 스택
- 코딩 컨벤션 (스타일·네이밍·import 순서 등)
- 디렉토리 구조
- 테스트 명령어
- 빌드·실행 명령어
- 주의 사항 (`.env` 처리, DB 마이그레이션 도구 등)

### 효과적인 태스크 작성 패턴

Codex 태스크는 짧을수록 결과 품질이 떨어진다. 다음 5가지 패턴 권장:

| 패턴 | 템플릿 |
|---|---|
| 기능 구현 | `Add [기능 이름] to [파일명 또는 모듈명]` |
| 버그 수정 | `Fix [이슈 설명] in [파일명]` |
| 리팩토링 | `Refactor [대상] to use [패턴 또는 기술]` |
| 테스트 작성 | `Write tests for [모듈 또는 함수명]` |
| 문서화 | `Generate [문서 유형] for [모듈 또는 파일]` |

상세 패턴·치트시트는 [[openai-chatgpt-codex-guide]] 부록 D 참조.

## 관련 개념

- [[claude-code]]: 로컬 터미널 페어 프로그래밍 도구. Codex와 보완재 — 같은 개발자가 작업 단계별로 병행 사용.
- [[github]]: Codex의 PR 생성·리포 탐색 기반 플랫폼. Copilot과의 관계도 GitHub 통해 매개.
- [[microsoft]]: GitHub의 모회사. Microsoft 2023 연구는 GitHub Copilot 사용자 코드 작성 속도가 평균 55% 빠르다고 보고.
- [[agent-skills]]: AGENTS.md vendor-neutral 컨벤션의 13단계 진화 흐름 — Codex의 AGENTS.md 채택은 그 흐름의 핵심 사례.
- [[agent-patterns]]: Codex가 구현한 자율 PR 생성 워크플로는 Anthropic의 Building Effective Agents 5 패턴 중 "Orchestrator-Workers"·"Evaluator-Optimizer"의 변형.
- [[harness]]: Codex의 클라우드 샌드박스 + Setup Script + AGENTS.md 결합은 본질적으로 agent harness의 OpenAI 측 구현.
- [[openai-cookbook]] / [[openai-agents-python]]: OpenAI 자체 레포가 모두 Codex 친화적 AGENTS.md 구조 채택 — Codex의 도그푸딩.

## 출처

- [[openai-chatgpt-codex-guide]] — Part 5 전체(Ch 13~16) + 부록 D. Codex 소개, 코드 작성·리팩토링·버그 수정·테스트, 실전 활용 패턴, 명령어·워크플로 치트시트.

## 논쟁/모순

- **요금·플랜 정보 변동성**: 책 기준(2026-04 편집)과 OpenAI 공식 사이트 사이에 차이 발생 가능. `verification_required: true` 박힌 이유.
- **Claude Code와의 경계**: 책은 "보완재"로 설명하지만, 실제 워크플로에선 owner가 Codex로 작성한 PR을 [[claude-code]]로 로컬 검토·수정하는 식의 결합도 가능 — 보완재 vs 단계별 결합 양쪽 다 성립.

## 메모

- **owner 활용 우선순위**: 백그라운드 클라우드 자율 태스크가 일상이 되면 [[matechat]] 사이드 프로젝트 야간 작업 자동화에 1순위 후보. 다만 [[claude-code]] 가 이미 daily driver로 정착해 있어 Codex는 보조 위치로 시작.
- **재검증 트리거**: OpenAI Codex 제품 라인업·요금제·CLI 기능은 빠르게 갱신. 90일마다 [[openai-chatgpt-codex-guide]] (책이 계속 업데이트 중)와 OpenAI 공식 사이트로 cross-check.
- **AGENTS.md 도그푸딩 관찰**: [[openai-cookbook]]·[[openai-agents-python]] 모두 Codex가 따르는 AGENTS.md를 자기 레포에 박아둠 — owner도 [[matechat]]·[[c2spf-analytics]]에 AGENTS.md를 박으면 Codex뿐 아니라 [[claude-code]]까지 같은 가이드를 공유.
