---
title: "Claude Code"
type: entity
entity_type: tool
tags: [claude-code, AI, 에이전트, agent, 코딩도구, coding-tool, Anthropic, CLI]
related: [[mcp]], [[llm-wiki-pattern]], [[obsidian-web-clipper]]
source_count: 1
created: 2026-04-09
updated: 2026-04-09
---

# Claude Code

## 개요

Anthropic이 개발한 에이전트 코딩 도구. 전체 코드베이스를 이해하고, 파일 편집, 명령 실행, 외부 도구 통합을 수행한다. Terminal CLI, VS Code, JetBrains, Desktop 앱, Web, iOS 등 다양한 환경에서 동일한 엔진으로 작동한다.

이 위키 자체가 Claude Code를 에이전트로 사용하여 운영되고 있다.

## 주요 특징

### 핵심 기능
- **에이전트 코딩**: 자연어 지시로 코드 작성, 디버깅, 리팩토링
- **코드베이스 이해**: 여러 파일과 도구에 걸쳐 작업 가능
- **Git 통합**: 스테이징, 커밋, 브랜치, PR을 직접 수행
- **Unix 철학**: 파이프 가능한 CLI. 다른 도구와 조합 가능

### 확장 시스템
- **CLAUDE.md**: 프로젝트 루트의 마크다운 파일로 세션마다 자동 로드. 코딩 표준, 아키텍처, 워크플로우 규칙 정의. 이 위키의 스키마가 바로 이 기능을 활용
- **자동 메모리**: 빌드 명령, 디버깅 인사이트 등을 자동 축적
- **[[mcp]]**: 외부 서비스(Google Drive, Jira, Slack 등)를 네이티브 도구로 연결. 프로젝트 루트 `.mcp.json`에 등록
- **Skills (커스텀 명령)**: `/review-pr`, `/deploy-staging` 같은 반복 워크플로우를 팀과 공유
- **Hooks**: 도구 실행 전후에 셸 명령 자동 실행

### 멀티 에이전트
- **서브 에이전트**: 여러 에이전트를 병렬 생성. 리드 에이전트가 조정하고 결과 병합
- **Agent SDK**: 완전 커스텀 에이전트 구축. 오케스트레이션·도구 액세스·권한 제어

### 자동화 & 크로스 디바이스
- **예약 작업**: 클라우드(서버) / 데스크톱(로컬) / `/loop`(CLI 폴링)
- **CI/CD**: GitHub Actions, GitLab CI/CD 연동
- **원격 제어**: 로컬 세션을 휴대폰/브라우저에서 계속
- **Slack 연동**: `@Claude` 멘션으로 버그 → PR 자동화

### 설치

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

설치 후 프로젝트 디렉토리에서 `claude` 명령으로 시작.

## 관련 개념

- [[llm-wiki-pattern]]: 이 위키의 운영 패턴. Claude Code가 에이전트 역할 수행
- [[mcp]]: Claude Code의 외부 도구 통합 프로토콜
- [[obsidian-web-clipper]]: 소스 수집 후 Claude Code가 위키에 통합하는 워크플로우

## 출처

- [[claude-code-overview]] — Anthropic 공식 문서 개요 페이지

## 메모

- 석근님의 주요 개발 도구 중 하나. 회사 맥북에서 사용.
- LLM 위키에서의 역할: Obsidian이 IDE, Claude Code가 프로그래머, 위키가 코드베이스.
- Cowork도 위키 에이전트로 병행 사용 가능 (외출 시).
