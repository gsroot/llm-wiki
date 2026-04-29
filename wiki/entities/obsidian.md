---
title: "Obsidian"
type: entity
entity_type: tool
tags: [obsidian, 지식관리, knowledge-management, 마크다운, markdown, 노트앱, vault]
related:
  - "[[obsidian-web-clipper]]"
  - "[[llm-wiki-pattern]]"
  - "[[claude-code]]"
source_count: 1
observed_source_refs: 3
inbound_count: 9
created: 2026-04-15
updated: 2026-04-15
---

# Obsidian

## 개요

로컬 Markdown 파일 기반의 개인 지식 관리 앱. 폴더(vault)에 노트를 저장하고 `[[wikilink]]` 문법으로 연결한다. 이 위키가 Obsidian vault로 운영되고 있다.

본질 4가지:
1. **파일이 내 손에 남는다** — 로컬 Markdown, 앱 종속 없음
2. **노트가 링크로 연결된다** — 양방향 백링크 자동
3. **Properties로 구조를 붙일 수 있다** — YAML frontmatter
4. **검색으로 다시 꺼내 쓰기 쉽다** — 전문·태그·속성·경로 검색

## 핵심 기능

### Vault
노트 저장 폴더. 하나로 시작이 권장됨. `.obsidian/` 하위에 설정·테마·플러그인 정보가 들어감.

### 링크 문법
```md
[[파일명]]
[[파일명|표시이름]]
[[파일명#헤더]]
```

### Properties (YAML frontmatter)
정렬·필터·Bases용 구조 필드. 최소 권장: `type`, `status`, `date`, `owner`, `tags`.

### Tags
짧고 반복적인 분류 (`#meeting`, `#billing`). 중첩 허용 (`#inbox/to-read`).

### 백링크
현재 노트를 가리키는 다른 노트 목록을 자동으로 수집·표시. 직접 찾지 않아도 문맥이 반대로 모여드는 핵심 기능.

### Quick switcher & Command palette
노트 검색·이동, 명령 실행을 키보드로. Obsidian 장점 절반이 여기에.

### Templates / Daily Notes
반복 문서의 시작점. 회의·프로젝트·데일리 노트 템플릿이 생산성을 결정.

### Canvas vs Bases
- **Canvas**: 생각 펼치기 (마인드맵, 관계도)
- **Bases**: 정리된 데이터 조회 (카드/목록/상태별, properties 기반 필터)

## 이 위키에서의 역할

[[llm-wiki-pattern]]의 IDE/뷰어. LLM([[claude-code]])이 프로그래머이자 에이전트라면, Obsidian은 결과물을 보고 탐색하는 계층.

| 이 위키 구조 | Obsidian 기능 |
|--------------|--------------|
| `wiki/*/*.md` 파일들 | Vault 안의 노트 |
| `[[위키링크]]` | Obsidian 내부 링크 |
| YAML frontmatter | Properties |
| `tags: [...]` | Tags |
| `wiki/index.md` | 수동 구축 Bases (향후 Bases로 전환 가능) |
| `templates/*` | Templates |

## 권장 운영 패턴

- **Vault 1개, 폴더 최소화**: 처음부터 정교한 폴더 구조를 만들면 유지가 어렵다
- **태그 5~10개, 속성 4~5개**: 작게 시작해 필요한 것만 추가
- **의사결정 노트 분리**: `Decision - ...` 형식으로 별도 관리
- **프로젝트마다 허브 노트 1개**: 목표·회의·요구사항·결정·할 일·참고 링크 집중
- **회의는 무조건 프로젝트에 연결**: 고아 문서 방지
- **커뮤니티 플러그인은 늦게**: 1주차는 코어 플러그인만

## Sync/백업

동기화 전략은 **하나만 메인으로**. 옵션:
- Obsidian Sync (공식)
- iCloud / Dropbox / OneDrive
- Git (이 위키의 선택)

`.obsidian/` 포함 여부는 기기 간 설정 공유 여부에 따라 결정.

## 관련 도구

- [[obsidian-web-clipper]]: 웹 페이지를 Obsidian용 마크다운으로 클리핑 (이 위키 `raw/articles/`에 사용)
- [[qmd]]: 로컬 마크다운 검색 엔진. Obsidian 기본 검색이 부족해지면 대체/보완
- [[claude-code]]: Obsidian vault 안에서 LLM 에이전트로 작업 (이 위키 패턴)

## 출처

- [[obsidian-guide]] — 석근님이 정리한 21개 섹션 실무 입문 가이드

## 메모

- 석근님 장비 양쪽(회사 맥북, 집 윈도우)에서 같은 vault를 써야 하면 iCloud 또는 Git이 후보
- 이 위키는 Git + `.obsidian/` 포함 방식으로 운영 중 (`graph.json`이 untracked로 있는 상태)
- Bases 기능을 도입하면 `index.md`를 정적 테이블에서 동적 쿼리로 바꿀 수 있음
