---
title: "Claude Code 개요"
type: source
source_type: article
source_url: "https://code.claude.com/docs/ko/overview"
author: "Anthropic"
date_published: 2026-04-09
date_ingested: 2026-04-09
tags: [claude-code, AI, 에이전트, agent, 코딩도구, coding-tool, Anthropic]
related: [[claude-code]], [[mcp]], [[llm-wiki-pattern]]
confidence: high
---

# Claude Code 개요

## 한줄 요약

> Claude Code는 코드베이스를 읽고, 파일을 편집하고, 명령을 실행하며, 외부 도구와 통합하는 에이전트 코딩 도구로, 터미널부터 웹까지 다양한 환경에서 사용할 수 있다.

## 핵심 내용

### 기본 기능

- **코드 작성 & 빌드**: 자연어로 기능을 설명하면, 접근 방식을 계획하고 여러 파일에 걸쳐 코드를 작성
- **디버깅**: 오류 메시지나 증상을 설명하면 코드베이스를 추적하여 근본 원인 파악 및 수정
- **자동화**: 테스트 작성, lint 수정, 병합 충돌 해결, 종속성 업데이트, 릴리스 노트 작성 등 반복 작업 처리
- **Git 통합**: 변경 사항 스테이징, 커밋 메시지 작성, 브랜치 생성, PR 오픈

### 사용 환경

| 환경 | 특징 |
|------|------|
| **Terminal CLI** | 모든 기능 갖춘 CLI. `curl`로 설치, `claude` 명령으로 시작 |
| **VS Code / JetBrains** | IDE 확장 |
| **Desktop 앱** | 시각적 diff 검토, 로컬 예약 작업 |
| **Web** | claude.ai/code에서 브라우저로 사용 |
| **iOS 앱** | 모바일에서 세션 시작/계속 |

### 확장 기능

- **[[mcp]]**: 외부 데이터 소스(Google Drive, Jira, Slack 등)를 네이티브 도구로 연결
- **CLAUDE.md**: 프로젝트 루트에 두는 마크다운 파일. 코딩 표준, 아키텍처 결정, 체크리스트를 세션 시작 시 자동 로드. 자동 메모리도 별도로 축적
- **Skills (커스텀 명령)**: `/review-pr`, `/deploy-staging` 같은 반복 워크플로우를 패키징하여 팀 공유
- **Hooks**: 도구 실행 전후에 셸 명령 자동 실행 (예: 편집 후 포맷팅, 커밋 전 lint)
- **서브 에이전트**: 여러 에이전트를 병렬 생성하여 작업 분산. 리드 에이전트가 조정
- **Agent SDK**: 완전 커스텀 에이전트 구축. 오케스트레이션, 도구 액세스, 권한 제어

### 자동화 & 크로스 디바이스

- **예약 작업**: 클라우드(컴퓨터 꺼져도 실행) / 데스크톱(로컬 파일 접근) / `/loop`(CLI 내 폴링)
- **CI/CD**: GitHub Actions, GitLab CI/CD로 PR 검토 및 이슈 분류 자동화
- **원격 제어**: 로컬 세션을 휴대폰/브라우저에서 계속
- **Dispatch**: 휴대폰에서 작업 보내고 데스크톱 세션으로 생성
- **Slack 연동**: `@Claude` 멘션으로 버그 보고서 → PR 자동 생성
- **Chrome 연동**: 라이브 웹 앱 디버깅

### Unix 철학

Claude Code는 파이프 가능한 CLI로 설계됨:
```
tail -200 app.log | claude -p "anomalies 있으면 Slack으로 보내"
git diff main --name-only | claude -p "보안 이슈 리뷰"
```

## 주요 인사이트

- **CLAUDE.md 패턴이 핵심**: 이 위키의 CLAUDE.md가 바로 이 기능을 활용한 것. 프로젝트별 지속적 지침을 마크다운 파일로 관리하는 설계가 LLM 위키 패턴과 자연스럽게 맞물린다.
- **에이전트 코딩의 범용성**: 단순한 코드 생성을 넘어, 도구 통합(MCP), 워크플로우 자동화(Hooks/Skills), 멀티 에이전트(서브 에이전트), 스케줄링까지 포괄하는 "개발 운영 체제"에 가까운 도구.
- **크로스 디바이스 연속성**: 터미널 → 데스크톱 → 모바일 → 웹 사이를 세션이 이동할 수 있는 구조. 위키 작업도 장소에 구애받지 않고 이어갈 수 있다.

## 관련 엔티티/개념

- [[claude-code]]: 이 문서의 주제
- [[mcp]]: Claude Code의 외부 도구 통합 프로토콜
- [[llm-wiki-pattern]]: 이 위키 자체가 Claude Code를 에이전트로 사용하는 구현체

## 인용할 만한 구절

해당 없음 (공식 문서이므로 기술적 설명 위주)

## 메모

- 이 문서는 Obsidian Web Clipper로 클리핑된 것으로, 일부 영어 원문이 번역되지 않고 남아 있음.
- Claude Code의 설치 방법(macOS/Linux/Windows)이 포함되어 있어 실전 참조용으로 유용.
