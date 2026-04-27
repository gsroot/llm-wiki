---
title: "Obsidian 사용 가이드"
type: source
source_type: note
source_url: ""
raw_path: "raw/notes/OBSIDIAN_GUIDE.md"
author: "석근 (개인 정리)"
date_published: 2026-04-07
date_ingested: 2026-04-15
tags: [obsidian, 지식관리, knowledge-management, 마크다운, markdown, notion, 업무생산성]
related: [[obsidian]], [[llm-wiki-pattern]], [[obsidian-web-clipper]]
confidence: high
---

# Obsidian 사용 가이드

## 한줄 요약

> Obsidian은 "내 컴퓨터 폴더(vault)에 Markdown 노트를 저장하고, 노트끼리 링크해서 지식을 연결하는 도구". Notion 사용자가 부담 없이 적응할 수 있도록 **폴더 최소화 → 링크 → 템플릿 → 검색** 순으로 운영 감각을 쌓는 21개 섹션 실무 입문서.

## 핵심 내용

### Obsidian의 본질 4가지

1. 파일이 내 손에 남는다 (Markdown, 로컬)
2. 노트가 링크로 연결된다 (양방향 백링크)
3. Properties로 구조를 붙일 수 있다 (YAML frontmatter)
4. 검색으로 다시 꺼내 쓰기 쉽다

> 메모앱이 아니라 **개인/팀의 지식 운영 시스템**에 가까움.

### 언제 맞고 언제 덜 맞는가

| 잘 맞는 경우 | 덜 맞는 경우 |
|-------------|-------------|
| 파일로 남기고 싶다 | 실시간 공동편집 핵심 |
| 링크로 엮고 싶다 | 완성된 협업 DB UI 필요 |
| 오프라인 작업 | 구조를 스스로 설계하기 싫음 |
| 내 방식대로 폴더·속성·템플릿 설계 | |

**결론**: 개인 지식관리·실무 기록 축적에는 강력. 동시 협업이 핵심이면 Notion/Google Docs.

### 설치 후 우선순위

1. **Vault 1개만** 만들기 (여러 개로 시작하면 지침)
2. **폴더 최소화**: `00 Inbox`, `10 Projects`, `20 Knowledge`, `30 Meetings`, `40 Daily`, `Templates`, `Assets`, `90 Archive`
3. **코어 플러그인만**: Backlinks, Search, Quick switcher, Page preview, Templates, Daily notes, Outline, Tags view, Properties view

### 첫 5분

- 노트 3개 만들기 (프로젝트 허브, 회의 노트, 오늘 메모)
- `[[wikilink]]`로 노트끼리 연결
- 회의 노트 → 허브 노트 역방향 연결 → **백링크로 문맥이 반대로 모여든다**

### 링크 문법

```md
[[프로젝트 허브]]
[[프로젝트 허브|결제 개선 프로젝트]]   # 표시 이름 변경
[[프로젝트 허브#다음 액션]]            # 헤더로 점프
```

**링크 패턴 추천**:
- 회의 노트 → 프로젝트 허브
- 이슈 노트 → 서비스/기능 노트
- 의사결정 노트 → 관련 회의/요구사항/구현
- 데일리 노트 → 그날 작업한 프로젝트

### 파일명 규칙 (초반에 고정)

| 종류 | 예시 |
|------|------|
| 회의 | `2026-04-07 결제 개선 회의` |
| 데일리 | `2026-04-07` |
| 프로젝트 | `프로젝트 - 결제 개선` |
| 의사결정 | `Decision - 결제 실패 재시도 정책` |
| 개념 | `개념 - 리텐션 정의` |

날짜는 `YYYY-MM-DD` 통일. 특수문자 남발 금지. Quick switcher 효율을 위해 접두어가 유효.

### Properties vs Tags vs Links — 역할 구분

| 수단 | 역할 | 예 |
|------|------|---|
| **Properties** | 고정된 필드 (정렬·필터·Bases용) | `type`, `status`, `date`, `owner`, `tags` |
| **Tags** | 반복 분류 (짧고 자주) | `#meeting`, `#billing`, `#inbox/to-read` |
| **Links** | 문맥 연결 | `[[프로젝트 - 결제 개선]]` |

핵심 기준: **반복 분류는 태그, 고정 필드는 속성, 문맥 연결은 링크**.

### 검색 문법

```text
"결제 오류"               정확 문구
meeting OR 회의           OR
회의 -개인                제외
tag:#meeting             태그
file:2026-04             파일명
path:"30 Meetings"       폴더 경로
```

> 정리를 열심히 하는 사람보다 **검색을 잘 설계하는 사람이 나중에 더 편하다**.

### Quick switcher & Command palette

마우스만 쓰면 Obsidian의 장점 절반이 버려짐. 키보드 흐름 우선.

### 템플릿 3종 (필수)

1. **회의 노트**: frontmatter(type/status/date/tags) + 목적/논의/결정/액션/관련 문서
2. **프로젝트 허브**: type=project, status=active + 목표/현재 상태/핵심 링크/다음 액션
3. **참고·학습 노트**: type=reference + 한줄요약/핵심내용/실무 적용/관련 노트

### Daily Notes 효과

- 매일 무엇을 했는지 남음
- 프로젝트·회의 노트에 자연스럽게 링크가 걸림
- "언제 이 이슈를 봤지?" 복기 가능

### Canvas vs Bases — 역할 분리

| 도구 | 용도 |
|------|------|
| **Canvas** | 생각을 **펼칠 때** (마인드맵, 관계도) |
| **Bases** | 정리된 데이터를 **조회할 때** (카드/목록/상태별) |

추천 순서: 노트+링크+속성 먼저 → Bases → Canvas. 초반부터 Bases 꽂히면 구조만 만들다 끝남.

### Sync/백업 3원칙

1. 동기화 전략은 **하나만 메인으로** (섞다 충돌이 제일 피곤)
2. `.obsidian/` 포함 여부 결정 (기기 간 설정 공유 vs 분리)
3. 중요 vault는 정기 백업 (회사 업무, 장기 연구, 멀티 기기, 플러그인 다수)

### 커뮤니티 플러그인 도입 타이밍

- **1주차**: 없이 사용, 기본 흐름 익히기
- **이후**: 불편이 명확할 때만, 하나씩
- **팀/업무**: 검증·권한·유지보수 확인, 도입 이유 기록

### 실무 운영 규칙 4가지

1. **프로젝트마다 허브 노트 1개** (목표/회의/요구사항/결정/할 일/참고 링크)
2. **회의는 무조건 프로젝트에 연결** (고아 문서 방지)
3. **의사결정은 분리** (`Decision - ...` 형식, 정책 변경 이력 추적용)
4. **태그 5~10개, 속성 4~5개로 시작** (작게 시작해 필요한 것만 추가)

### Notion → Obsidian 사고 전환

| Notion | Obsidian |
|--------|---------|
| 블록 조립 | 파일/노트 중심 |
| 페이지 + DB | 노트 + 링크 + 얇은 속성 |
| 완성형 DB 먼저 | 노트·링크 먼저, Bases는 나중 |

### 흔한 실수 6가지

1. 폴더 너무 많이 만들기
2. 태그 과다
3. 플러그인 과속 설치
4. 링크를 안 걸어서 그냥 Markdown 폴더가 됨
5. 템플릿 없이 빈 페이지에서 시작
6. 파일명 규칙 부재

### 1주차 체크리스트

| Day | 작업 |
|-----|------|
| 1 | Vault·폴더·프로젝트 허브 생성 |
| 2 | 회의 노트 템플릿 + 실제 기록 |
| 3 | 데일리 노트 템플릿 + 작업 로그 |
| 4 | 링크 10개+ 연결, 백링크 확인 |
| 5 | 속성 4종 + 태그 3~5개 |
| 6 | 검색 예시 5개 + Quick switcher |
| 7 | 안 쓰는 구조 삭제, 플러그인 필요성 판단 |

## 주요 인사이트

- **"작고 일관된 규칙을 오래 지킨 사람"이 Obsidian을 잘 쓴다** — 복잡한 시스템을 만든 사람이 아니라. [[claude-code-master-guide]]의 "짧고 강한 CLAUDE.md" 원칙과 동형.
- **파일·링크·속성·검색의 4축**이 이 가이드의 뼈대. 이 위키도 동일 축 위에 구축됨: 파일(`wiki/*.md`), 링크(`[[wikilink]]`), 속성(YAML frontmatter), 검색(`index.md` + 향후 [[mcp]] 검색).
- **Properties/Tags/Links 역할 구분**이 실질적으로 가장 중요한 실무 지식. 이 위키는 셋 다 사용 중 (frontmatter `type`, `tags:` 배열, 본문 `[[wikilink]]`).
- **Canvas vs Bases의 역할 분리**: Canvas는 펼치기, Bases는 조회. 이 위키의 `wiki/index.md`는 Bases 계열 접근(카탈로그), 향후 `wiki/graph`나 `wiki/canvas` 디렉토리가 Canvas 계열이 될 수 있음.
- **검색이 정리를 대체한다**: 이 위키의 `index.md` 중심 운영 + [[qmd]] MCP 연동 구상과 정확히 일치.
- **Sync 전략은 하나만**: 이 위키는 Git을 메인으로 씀 (이미 `aa654f5 docs: README.md 추가` 등 커밋 진행 중).

## 관련 엔티티/개념

- [[obsidian]]: 이 가이드의 주제 (신규 엔티티)
- [[llm-wiki-pattern]]: 이 위키의 운영 패턴. Obsidian의 원칙을 LLM 협업에 확장
- [[obsidian-web-clipper]]: Obsidian 생태계의 클리핑 도구
- [[claude-code-master-guide]]: "짧고 강한 운영 계약서" 원칙이 이 가이드의 "작고 일관된 규칙"과 동형

## 인용할 만한 구절

> "Obsidian을 잘 쓰는 사람은 복잡한 시스템을 만든 사람이 아니다. 작고 일관된 규칙을 오래 지킨 사람이다."

> "정리를 열심히 하는 사람보다, 검색을 잘 설계하는 사람이 나중에 더 편하다."

## 메모

- 저자 표기가 본문에 없지만 Properties 예시에 `owner: 석근`이 있고 전체 톤이 석근님 개인 정리체이므로 본인 저작으로 판단.
- 이 위키의 현재 구조(`wiki/index.md`, `wiki/logs/log.md`, 템플릿 4종, frontmatter 필수)와 거의 모든 원칙이 일치 → 이 가이드가 이 위키 설계의 배경 중 하나로 보임.
- **후속 탐구**: Obsidian의 Bases 기능을 도입하면 `wiki/index.md`를 정적 테이블에서 동적 쿼리로 바꿀 수 있음 (예: `type: concept AND source_count >= 2`).
