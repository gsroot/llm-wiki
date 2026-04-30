---
title: Claude Code 빠른 시작
type: source
source_type: article
source_url: https://code.claude.com/docs/ko/quickstart
raw_path: raw/articles/claude-code/빠른 시작.md
author: Anthropic
date_published: 2026-04-15
date_ingested: 2026-04-15
tags:
- claude-code
- AI
- agent
- 코딩도구
- coding-tool
- anthropic
related:
- '[[claude-code]]'
- '[[claude-code-overview]]'
confidence: high
inbound_count: 5
cited_by:
- '[[claude-code]]'
- '[[claude-code-overview]]'
cited_by_count: 2
aliases:
- Claude Code Quickstart
- Claude Code 빠른 시작
- claude code quickstart
---

# Claude Code 빠른 시작

## 한줄 요약

> 설치 → 로그인 → 첫 질문 → 코드 변경 → Git 작업까지, Claude Code를 일상적으로 사용하기 위한 8단계 실전 온보딩 가이드.

## 핵심 내용

### 온보딩 8단계

1. **설치**: OS별 원라이너 (`curl ... | bash`, `irm ... | iex`, `install.cmd`). 네이티브 설치는 백그라운드 자동 업데이트.
2. **로그인**: `claude` 첫 실행 시 프롬프트, 이후 `/login`으로 계정 전환. Pro/Max/Teams/Enterprise, Console(API 크레딧), Bedrock/Vertex AI/Foundry 지원.
3. **첫 세션**: 프로젝트 디렉토리에서 `claude` 실행 → 환영 화면, `/help`로 명령 탐색, `/resume`으로 이전 대화 재개.
4. **첫 질문**: "이 프로젝트는 무엇을 하나요?" 같은 자연어 질문. 필요 파일을 Claude가 스스로 읽으므로 수동 컨텍스트 추가 불필요.
5. **첫 코드 변경**: 파일 수정 전 항상 권한 요청. 개별 승인 or 세션 단위 "모두 수락" 모드.
6. **Git 작업**: "변경사항 설명적 메시지로 커밋", "feature/X 브랜치 생성", "병합 충돌 해결" 같은 대화형 요청 지원.
7. **버그 수정/기능 추가**: 자연어 설명 → 관련 코드 탐색 → 컨텍스트 이해 → 솔루션 구현 → 가능 시 테스트 실행.
8. **일반 워크플로우**: 리팩토링, 테스트 작성, 문서 업데이트, 코드 리뷰를 같은 방식으로.

### 필수 CLI 명령

| 명령 | 기능 |
|------|------|
| `claude` | 대화형 모드 시작 |
| `claude "task"` | 일회성 작업 실행 |
| `claude -p "query"` | 일회성 쿼리 실행 후 종료 (파이프라인용) |
| `claude -c` | 현재 디렉토리에서 최근 대화 계속 |
| `claude -r` | 이전 대화 재개 (선택) |
| `claude commit` | Git 커밋 생성 |
| `/clear` | 대화 기록 지우기 |
| `/help` | 사용 가능한 명령 표시 |
| `exit` / Ctrl+C | 종료 |

### 프롬프팅 팁 (초보자용)

- **구체적으로**: "버그 수정" ❌ → "사용자가 잘못된 자격 증명 입력 후 빈 화면을 보는 로그인 버그 수정" ✅
- **단계로 나누기**: 복잡한 작업은 1) DB 테이블 생성 2) API 엔드포인트 3) UI 구축처럼 분해.
- **이해 먼저**: 변경 전에 "데이터베이스 스키마 분석" 같은 탐색 요청으로 컨텍스트 확보.
- **동료처럼 대화**: 달성 목표를 설명하는 방식이 명령형보다 효과적.

### 키보드 단축키

- `?`: 전체 단축키 목록
- `Tab`: 명령 자동 완성
- `↑`: 명령 기록
- `/`: 모든 명령 및 skills 보기

## 주요 인사이트

- **온보딩이 "동료처럼 대화하기" 철학을 강화한다**: 각 단계가 명령 구문이 아니라 "이 프로젝트는 뭐하나요?" 같은 평문 요청으로 시작. 도구라기보다 페어 프로그래머 메타포를 일관되게 유지.
- **`claude -p` + 파이프**: 일회성 쿼리 모드는 [[claude-code-overview]]의 Unix 철학과 직결. `git diff | claude -p "리뷰"` 같은 조합 가능.
- **권한 모델**: 파일 수정 전 항상 승인. "모두 수락" 모드는 세션 범위로 제한되어 신뢰·속도 사이의 조절점 제공.
- **프롬프팅 팁이 곧 위키 운영 팁**: "구체적으로", "단계 분해", "이해 먼저"는 이 위키의 수집 워크플로우(읽기→논의→요약→업데이트)와 동일한 발상.

## 관련 엔티티/개념

- [[claude-code]]: 이 문서의 주제
- [[claude-code-overview]]: 개념적 개요. 이 빠른 시작은 그 실전 적용판

## 인용할 만한 구절

> "도움이 되는 동료처럼 Claude와 대화하십시오. 달성하고 싶은 것을 설명하면 도움을 드릴 것입니다."
> — Anthropic, Claude Code 빠른 시작

## 메모

- Obsidian Web Clipper로 클리핑됨. 일부 영어 원문 미번역 구역(설치 단락)이 남아 있음.
- 이 위키를 운영하는 석근님 입장에서는 이미 일상 사용 중인 도구이지만, CLI 플래그 레퍼런스(`-p`, `-c`, `-r`)로 유용.
