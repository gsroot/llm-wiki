---
title: "활동 로그"
type: log
---

# 활동 로그

> 위키의 모든 활동(수집, 질의, 점검 등)을 시간순으로 기록합니다.
> 각 항목은 `## [날짜] 유형 | 제목` 형식을 따릅니다.

---

## [2026-04-09] ingest | Claude Code 개요 수집

- **소스**: `raw/articles/Claude Code 개요.md`
- **작업**: Anthropic 공식 문서 클리핑 수집
- **생성된 파일**:
  - `wiki/sources/claude-code-overview.md` — 소스 요약
  - `wiki/entities/claude-code.md` — Claude Code 엔티티 페이지
- **업데이트된 파일**:
  - `wiki/concepts/mcp.md` — source_count 1→2, Claude Code의 MCP 활용 범위 추가, 출처 추가
  - `wiki/index.md` — 총 페이지 수 8→10, 새 페이지 2건 등록
- **메모**: 이 위키를 운영하는 도구 자체에 대한 문서. CLAUDE.md, MCP, Skills, Hooks 등 위키 운영과 직결되는 기능이 다수 포함됨.

---

## [2026-04-09] ingest | LLM 위키 아이디어 문서 수집

- **소스**: `raw/notes/llm_wiki.md`
- **작업**: 첫 번째 정식 수집(Ingest) 워크플로우 실행
- **생성된 파일**:
  - `wiki/sources/llm-wiki-idea-doc.md` — 소스 요약 페이지
  - `wiki/entities/memex.md` — 바네바 부시의 메멕스 (1945)
  - `wiki/entities/qmd.md` — 마크다운 검색 엔진
  - `wiki/entities/obsidian-web-clipper.md` — 웹 클리핑 도구
  - `wiki/concepts/mcp.md` — Model Context Protocol 개념
- **업데이트된 파일**:
  - `wiki/concepts/llm-wiki-pattern.md` — 역자 주석의 실전 팁 반영 (소스 수집 경로, RAG 보완 관계, 세션 간 컨텍스트, 관련 엔티티 링크 추가)
  - `wiki/syntheses/wiki-bootstrap-log.md` — 소스 참조 추가, 다음 단계 진행 상태 갱신
  - `wiki/index.md` — 총 페이지 수 2→8, 새 페이지 6건 등록
- **메모**: 원문(패턴 설명) + 역자 주석(실전 가이드 10개 항목) 구조. 이 문서가 현재 위키의 CLAUDE.md 설계의 직접적 기반이었으므로, 부트스트랩 시 이미 반영된 내용과 새로 추가된 실전 팁을 구분하여 수집.

---

## [2026-04-09] init | 위키 부트스트랩

- **작업**: LLM 위키 초기 구조 생성
- **생성된 파일**:
  - `CLAUDE.md` — 스키마 (운영 규칙 및 워크플로우)
  - `templates/` — 소스, 엔티티, 개념, 종합 분석 템플릿 4종
  - `wiki/index.md` — 위키 카탈로그
  - `wiki/logs/log.md` — 이 로그 파일
  - `wiki/concepts/llm-wiki-pattern.md` — 첫 번째 개념 페이지
  - `wiki/syntheses/wiki-bootstrap-log.md` — 부트스트랩 기록
- **메모**: "LLM 위키" 아이디어 문서를 기반으로 개인 종합 위키 초기 구축. Obsidian 볼트로 사용할 수 있도록 디렉토리 구조와 스키마를 설계함. Claude Code와 Cowork 양쪽에서 운영 가능하도록 설계.
