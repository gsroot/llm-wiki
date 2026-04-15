---
title: "활동 로그"
type: log
---

# 활동 로그

> 위키의 모든 활동(수집, 질의, 점검 등)을 시간순으로 기록합니다.
> 각 항목은 `## [날짜] 유형 | 제목` 형식을 따릅니다.

---

## [2026-04-15] ingest | Obsidian 사용 가이드 수집

- **소스**: `raw/notes/OBSIDIAN_GUIDE.md` (석근 개인 정리, 21개 섹션)
- **작업**: Notion 사용자 관점 Obsidian 실무 입문 가이드 수집. 이 위키 자체가 Obsidian vault로 운영되고 있으므로 구조적으로 중요.
- **생성된 파일**:
  - `wiki/sources/obsidian-guide.md` — 21개 섹션 요약 (설치, 링크, Properties/Tags/Links 구분, 검색, 템플릿, Canvas/Bases, Sync, 실무 운영 규칙)
  - `wiki/entities/obsidian.md` — Obsidian 본체 엔티티 (그동안 누락됐던 핵심 엔티티)
- **업데이트된 파일**:
  - `wiki/entities/obsidian-web-clipper.md` — 관련 엔티티에 `[[obsidian]]` 추가 (확장이 본체 vault에 저장한다는 관계 명시)
  - `wiki/concepts/llm-wiki-pattern.md` — "Obsidian" 언급을 `[[obsidian]]` 위키링크로 승격
  - `wiki/index.md` — 총 페이지 16→18 (소스 4→5, 엔티티 5→6)
- **메모**: 이 가이드의 원칙("작고 일관된 규칙을 오래 지킨 사람"이 잘 쓴다, Properties/Tags/Links 역할 분리)이 이 위키 설계와 정확히 일치. 사실상 이 위키 설계의 개인적 배경 문서.
- **후속 탐구**: Bases 기능을 도입하면 `wiki/index.md`의 정적 테이블을 frontmatter 기반 동적 쿼리로 전환 가능. 현재 유지보수 비용 대비 이득이 크면 검토 가치 있음.

---

## [2026-04-15] ingest | 클로드 코드 중심 실전 마스터 가이드 수집

- **소스**: `raw/articles/claude-code/클로드코드_가이드북.pdf` (CHOI, 848페이지, 82.7MB)
- **변환 도구**: [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) (Python 래퍼, Java JAR 기반)
  - 명령: `opendataloader-pdf -f markdown --image-output off -q -o /tmp/claude-guidebook-md/ ...`
  - 출력: 15,148줄 / 934KB 마크다운 (이미지 제외)
  - 변환 출력물은 raw/ 원칙 준수를 위해 프로젝트 외부 `/tmp/`에 보관하고 위키에는 요약만 반영
- **생성된 파일**:
  - `wiki/sources/claude-code-master-guide.md` — 12장 구조 요약, 핵심 개념, 운영 인사이트
  - `wiki/entities/cowork.md` — Anthropic Cowork (비개발 지식 업무용 자매 작업 경로)
  - `wiki/concepts/harness.md` — 이 책의 중심 개념. AI 에이전트 작업장 전체 구조
  - `wiki/concepts/token-economy.md` — 토큰 경제학 (비용 단위 + 작업 범위 신호)
  - `wiki/concepts/context-engineering.md` — 프롬프트/컨텍스트/하네스 엔지니어링 3층 구분
- **업데이트된 파일**:
  - `wiki/entities/claude-code.md` — source_count 2→3, 운영 보강 섹션(허용/질문/차단, scope 우선순위, 세션 재개, Worktree) 추가, 관련 개념에 harness/cowork/token-economy/context-engineering 연결
  - `wiki/concepts/mcp.md` — source_count 2→3, "MCP → Skill → Plugin" 사용 순서와 managed 설정 추가
  - `wiki/concepts/llm-wiki-pattern.md` — source_count 1→2, 이 위키를 하네스 관점으로 재해석하는 섹션 추가
  - `wiki/index.md` — 총 페이지 11→16 (소스 3→4, 엔티티 4→5, 개념 2→5)
- **변환 품질 메모**: 한국어 단어가 줄바꿈에서 잘리는 경우 있음(예: "어받기(Channels)", "classier"). `--use-struct-tree` 옵션을 향후 시도해볼 가치 있음. 표 구조 일부 깨짐.
- **교차 참고**: 석근님이 별도로 만든 `/Users/sgkim/Downloads/클로드코드 가이드북.md` 요약(전반부 1~6장 중심)과 교차 확인. 본 수집은 opendataloader-pdf 변환본(15,148줄)을 1차 소스로 하여 후반부 7~11장까지 포함.
- **메모**: 이 위키가 이미 적용 중인 운영 원칙(CLAUDE.md·index.md·log.md·templates·handoff)이 가이드북의 "기본 파일 8종"과 "4층 하네스 레이어"에 정확히 대응함을 확인. 즉 이 위키는 [[harness]] 개념의 개인 지식 관리용 구현체.

---

## [2026-04-15] ingest | Claude Code 빠른 시작 수집

- **소스**: `raw/articles/claude-code/빠른 시작.md`
- **작업**: Anthropic 공식 빠른 시작 가이드 클리핑 수집
- **생성된 파일**:
  - `wiki/sources/claude-code-quickstart.md` — 소스 요약 (8단계 온보딩, CLI 명령표, 프롬프팅 팁)
- **업데이트된 파일**:
  - `wiki/entities/claude-code.md` — source_count 1→2, 필수 CLI 명령표·단축키·프롬프팅 원칙 섹션 추가, 출처 추가
  - `wiki/index.md` — 총 페이지 수 10→11, 소스 2→3, Claude Code 엔티티 소스 수·수정일 갱신
- **메모**: [[claude-code-overview]]와 주제는 겹치나, 이 문서는 실전 온보딩(설치→로그인→첫 세션→Git)과 CLI 플래그 레퍼런스(`-p`, `-c`, `-r`) 중심. 개요 페이지와 역할이 분명히 다르므로 별도 소스로 보존. 새 엔티티·개념 페이지는 생성하지 않고 기존 [[claude-code]] 엔티티를 보강.

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
