---
title: "LLM 위키 패턴"
type: concept
category: ai
tags: [지식관리, knowledge-management, LLM, 위키, obsidian, RAG, 하네스, harness]
related:
  - "[[wiki-bootstrap-log]]"
  - "[[memex]]"
  - "[[qmd]]"
  - "[[mcp]]"
  - "[[obsidian-web-clipper]]"
  - "[[harness]]"
  - "[[context-engineering]]"
source_count: 3
observed_source_refs: 19
inbound_count: 43
created: 2026-04-09
updated: 2026-04-15
---

# LLM 위키 패턴

## 정의

LLM이 **점진적으로 영속적인 위키를 구축하고 유지관리**하는 개인 지식 관리 패턴. 질문 시점에 원시 문서에서 검색하는 RAG와 달리, 지식을 한 번 컴파일하고 최신 상태로 유지한다.

## 왜 중요한가

기존 RAG 방식(NotebookLM, ChatGPT 파일 업로드 등)은 매 질문마다 LLM이 지식을 처음부터 다시 발견해야 한다. 축적이 없다. LLM 위키는 상호 참조가 이미 만들어져 있고, 모순점이 이미 표시되어 있으며, 종합 분석이 모든 소스를 반영하고 있다. 소스를 추가하고 질문을 할 때마다 위키는 복리로 풍부해진다.

## 핵심 내용

### 3레이어 아키텍처

1. **원시 소스(Raw)**: 큐레이션한 소스 문서 모음. 불변. LLM은 읽기만 함.
2. **위키(Wiki)**: LLM이 생성/관리하는 마크다운 파일들. 요약, 엔티티, 개념, 종합 분석.
3. **스키마(Schema)**: LLM에게 구조, 규칙, 워크플로우를 알려주는 설정 문서 (CLAUDE.md 등).

### 3대 오퍼레이션

1. **수집(Ingest)**: 소스를 읽고 → 요약 작성 → 기존 위키 페이지 업데이트 → 인덱스/로그 갱신
2. **질의(Query)**: 인덱스로 관련 페이지 탐색 → 읽고 종합 → 가치 있으면 위키에 저장
3. **점검(Lint)**: 모순, 고아 페이지, 빈약한 페이지, 누락된 상호참조 등 점검

### RAG와의 차이

| 항목 | RAG | LLM 위키 |
|------|-----|----------|
| 지식 상태 | 매번 재발견 | 컴파일 & 유지 |
| 상호 참조 | 질의 시 추론 | 사전 구축 |
| 모순 처리 | 발견 못할 수 있음 | 명시적 기록 |
| 축적 | 없음 | 복리 성장 |

### 적용 분야

개인 학습, 리서치, 독서, 비즈니스/팀 위키, 경쟁 분석, 여행 계획 등 시간에 걸쳐 지식을 축적하는 모든 분야.

## 실전 적용

현재 이 위키 자체가 LLM 위키 패턴의 구현체이다. Obsidian을 IDE로, LLM(Claude Code/Cowork)을 프로그래머로, 위키를 코드베이스로 운영한다.

### 핵심 도구

- **[[obsidian]]**: 위키 뷰어 겸 IDE (그래프 뷰, Dataview, Linter, Templater)
- **[[obsidian-web-clipper]]**: 웹 기사를 마크다운으로 변환하여 raw/에 저장
- **[[qmd]]**: 위키가 50페이지 이상 커지면 도입할 로컬 마크다운 검색 엔진 (BM25 + 벡터 검색)
- **[[mcp]]**: 위키 검색을 LLM의 네이티브 도구로 노출하는 프로토콜. qmd의 MCP 서버 모드와 연동
- **Git**: 수집 단위 커밋으로 변경 이력 추적

### 소스 수집 경로

Web Clipper 외에도 다양한 소스 형태별 수집 방법:
- **YouTube**: `yt-dlp --write-auto-sub`로 자막 추출 후 `.md` 저장
- **PDF 논문/보고서**: `marker`로 마크다운 변환
- **트위터/스레드**: Thread Reader App → Web Clipper
- **팟캐스트**: Whisper 트랜스크립트 생성

### RAG와의 관계

RAG는 대체재가 아닌 **보완재**이다:
- 위키 = 1차 지식 레이어 (컴파일된 지식)
- RAG = 2차 레이어 (원문 검증 도구)
- 위키에서 답을 찾되, 원문 확인이 필요하면 원시 소스를 RAG로 검색

### 세션 간 컨텍스트

LLM 위키가 해결하는 가장 큰 실전 문제는 **세션 간 컨텍스트 유실**이다. 스키마에 "세션 시작 시 `index.md`와 `log.md`를 먼저 읽어라"고 명시하면, 새 세션에서도 축적된 지식의 지도를 즉시 파악할 수 있다.

### RAG처럼 활용하기 (5단계)

이 위키는 "수작업 컴파일된 RAG"이므로, Claude Code의 Read/Grep/Glob가 retrieval 엔진 역할을 한다. 상황별 5가지 통합 방법:

| 단계 | 방법 | 적용 시점 |
|------|------|----------|
| 1 | 위키 디렉토리에서 직접 실행 (`cd ~/llm-wiki && claude`) | 위키 자체 관리 |
| 2 | 다른 프로젝트 CLAUDE.md에 "참조 지식 베이스" 경로 추가 | 회사 프로젝트에서 참조 |
| 3 | 세션 첫 메시지로 `index.md` 명시적 로드 | 가끔 한 번씩 |
| 4 | `~/.claude/skills/wiki/SKILL.md` 로 [[agent-skills]] 패키징 (자동 호출 + `context: fork`) | 반복 조회 |
| 5 | [[qmd]] + [[mcp]]로 네이티브 검색 도구화 | 50+ 페이지 이후 |

핵심 감각: **"위키에 물어본다"**. 일반 지식 질문보다 "`wiki/concepts/harness.md` 기준으로 ..." 같은 **페이지 기반 합성 질문**이 가장 강력하다.

자세한 예시는 [[using-llm-wiki-as-rag]] 참조.

## 하네스 관점에서 본 위키

[[claude-code-master-guide]]의 [[harness]] 개념으로 이 위키를 다시 읽으면:
- **지식 레이어**: `CLAUDE.md` (운영 계약) + `wiki/index.md` (탐색 진입점) + 각 페이지
- **도구 레이어**: Read/Write/Edit, Grep/Glob, 향후 [[mcp]] (qmd)
- **패키지 레이어**: `templates/*` (엔티티·개념·소스·종합 템플릿) + `~/.claude/skills/wiki/SKILL.md` ([[agent-skills]])
- **통제 레이어**: CLAUDE.md의 금지 사항, 수집 워크플로우 체크리스트, `log.md` 사후 흔적

즉 이 위키는 **개인 지식 관리용 하네스**이며, [[context-engineering]]의 전형적 적용 사례다.

### 위키 ↔ Agent Skill의 동형성

[[anthropics-skills]] 분석에서 발견한 핵심 통찰: 위키의 3레이어 아키텍처와 SKILL의 3-Level Progressive Disclosure가 동형이다.

| 위키 | SKILL.md |
|-----|---------|
| `wiki/index.md` (항상 읽힘) | Metadata (frontmatter, ~100w 상시) |
| `wiki/sources/`·`wiki/concepts/` 등 | SKILL.md body (트리거 시 로드, <500lines) |
| `raw/articles/` (필요 시 grep) | scripts·references·assets (필요 시 호출) |

이 동형성은 **위키 운영 자체를 SKILL.md로 패키징할 수 있음**을 시사. 실제로 `~/.claude/skills/wiki/SKILL.md`가 운영 중이며, [[agent-skills]] 페이지의 "description pushy 원칙"과 "20개 trigger 검증 쿼리" 루프를 적용해 자동 호출 정확도 튜닝 가능.

## 관련 개념

- [[harness]]: 이 위키의 상위 추상. 위키는 지식용 하네스의 한 구현
- [[context-engineering]]: CLAUDE.md, index.md, log.md 구성 원칙의 배경 이론
- [[wiki-bootstrap-log]]: 2026-04-09 초기 구축 기록. 이 패턴이 실제 볼트 구조로 처음 굳어진 출발점
- [[memex]]: 바네바 부시의 메멕스 (1945). 문서 간 연상적 경로를 가진 개인 지식 저장소의 원조 비전. LLM이 유지관리 문제를 해결
- Zettelkasten: 니클라스 루만의 메모 상자 시스템. LLM 위키는 이를 자동화한 것에 가까움
- [[mcp]]: 위키를 LLM의 네이티브 도구로 만드는 프로토콜

## 출처

- [[llm-wiki-idea-doc]] — 이 패턴을 제안한 원본 아이디어 문서 (원문 + 역자 주석 10개 항목)
- [[claude-code-master-guide]] — 하네스·파일 운영·기본 파일 8종 등 위키 패턴과 동형 구조 다수 제시
- [[using-llm-wiki-as-rag]] — 이 위키를 Claude Code에서 RAG처럼 쓰는 5단계 실전 가이드
- [[anthropics-skills]] — Anthropic 공식 Agent Skills 레퍼런스. 위키 3레이어와 SKILL 3-Level Progressive Disclosure의 동형성 발견
- [[anthropics-skills]] — Anthropic 공식 Agent Skills 레퍼런스. 위키 3레이어와 SKILL 3-Level Progressive Disclosure의 동형성 발견

## 열린 질문

- 위키가 수백 페이지로 커졌을 때 인덱스만으로 탐색이 충분한가? qmd 도입 시점은?
- LLM 모델 간(Claude vs GPT 등) 위키 운영 품질 차이는?
- 여러 LLM 에이전트가 같은 위키를 동시에 편집하면 충돌 관리는 어떻게?
