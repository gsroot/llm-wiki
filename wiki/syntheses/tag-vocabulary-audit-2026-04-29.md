---
title: "태그 vocabulary 감사 — 2026-04-29"
type: synthesis
category: audit
tags: [tag-audit, vocabulary, obsidian, RAG, metadata, governance, 55회차]
aliases: [태그 감사, tag-vocabulary-audit, 태그 과밀 리포트, tag vocabulary audit]
sources:
  - "[[llm-wiki-pattern]]"
  - "[[using-llm-wiki-as-rag]]"
related:
  - "[[llm-wiki-pattern]]"
  - "[[rag]]"
  - "[[agent-skills]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[matechat]]"
  - "[[seokgeun-stack-guide]]"
created: 2026-04-29
updated: 2026-04-29
---

# 태그 vocabulary 감사 — 2026-04-29

## 요약

2026-04-29 현재 `wiki/**/*.md` 기준 태그 vocabulary는 **910개 unique tag / 2,174개 tag entry**다. case-duplicate는 0건이라 즉시 결함은 아니지만, singleton tag 449개와 2회 이하 저빈도 tag 696개가 있어 Obsidian 태그 탐색을 주 탐색 경로로 삼기에는 과밀하다.

결론: 지금은 태그 일괄 삭제보다 **역할 분리 정책**이 먼저다. 이 위키의 주 회수 경로는 `[[wikilink]]` / hub / `related` / `sources` / `inbound_count`이며, tags는 보조 검색 vocabulary로 제한하는 것이 맞다.

## 측정값

| 항목 | 값 | 해석 |
|---|---:|---|
| unique tags | 910 | 작은 개인 wiki 기준으로는 많음 |
| tag entries | 2,174 | 페이지당 평균 약 10.9개 |
| singleton tags | 449 | 전체 tag의 49.3%, 후보 검토 필요 |
| 2회 이하 저빈도 tags | 696 | 전체 tag의 76.5%, 자동 삭제 금지 |
| 회차 tags | 17종 / 97 entries | 지식 tag가 아니라 운영 이력 tag |
| 한글 포함 tags | 109 | 한국어 검색 편의성은 있음 |
| case duplicate | 0 | 회귀는 없음 |

## 상위 tag

| tag | 사용 수 | 판단 |
|---|---:|---|
| python | 25 | 유지 — 스택 축 core vocabulary |
| agents-md | 25 | 유지 — 5축 메타 vocabulary |
| agent-skills | 24 | 유지 — 5축 sub-hub |
| 에이전트 | 16 | 유지하되 `agent`와 역할 중복 감시 |
| mcp | 16 | 유지 — 5축 sub-hub |
| fastapi | 16 | 유지 — 백엔드 core vocabulary |
| agent | 16 | 유지하되 `에이전트`와 중복 감시 |
| openai | 15 | 유지 |
| claude-code | 15 | 유지 — 5축 sub-hub |
| matechat | 15 | 유지 — 4축 hub |

## 분류 정책

### 유지 tag

도메인, 기술, 제품, 핵심 개념을 직접 가리키고 여러 페이지에서 검색 축으로 작동하는 tag는 유지한다.

예: `agent-skills`, `harness`, `mcp`, `claude-code`, `matechat`, `fastapi`, `python`, `pandas`, `polars`, `duckdb`, `c2spf`, `portfolio`, `RAG`.

### alias로 이동 후보

표기 변종이나 빠른 열기 키워드는 tag보다 `aliases`에 두는 편이 낫다. 이미 48회차 이후 hub 페이지에 aliases가 도입됐으므로, tag는 검색 vocabulary, aliases는 표기 변종이라는 분리를 유지한다.

우선 검토 후보:

| tag | 현재 의미 | 권장 |
|---|---|---|
| 메이트챗 | `matechat` 표기 변종 | `matechat.md` aliases에 유지, tag에서는 제거 후보 |
| 석근 | `seokgeun-kim` 표기 변종 | aliases 우선 |
| owner | owner 페이지 별칭 | aliases 또는 본문 표현으로 충분 |
| portfolio-hub | hub 별칭 | aliases 우선 |
| retrieval-augmented-generation | `RAG` 풀네임 | `rag.md` aliases 우선, tag는 `RAG` / `검색증강생성` 중심 |

### 회차 tag

`16회차`, `17회차`, `25회차`, `53회차` 같은 tag는 지식 분류가 아니라 운영 이력이다. 현재 15종 / 92 entries로 크지는 않지만, 장기적으로는 `wiki/logs/by-session.md`와 `wiki/logs/log.md`가 source-of-truth가 되어야 한다.

권장 정책:

1. 새 콘텐츠에는 회차 tag를 기본 추가하지 않는다.
2. 회차 추적은 로그와 `created/updated`로 처리한다.
3. 이미 박힌 회차 tag는 일괄 제거하지 말고, 회차별 회귀 분석이 필요 없어지는 시점에만 정리한다.

### 저빈도 tag

singleton tag가 많지만 자동 삭제는 위험하다. `library-self-hosted-skill`, `pr-pattern-agents-md`, `event-driven-architecture`, `retrieval-augmented-generation`처럼 한 페이지에만 있어도 의미가 분명한 개념 tag가 있기 때문이다.

저빈도 tag 정리는 다음 기준을 동시에 만족할 때만 한다.

1. 같은 페이지의 `aliases` 또는 `title`로 이미 검색 가능하다.
2. tag가 도메인 분류가 아니라 표기 변종이다.
3. 다른 페이지와 묶는 연결 가치가 없다.
4. 제거해도 `rg` / Obsidian 검색 / LLM 회수에서 손실이 작다.

## 권장 실행 순서

1. `tags` 필드 누락 synthesis를 먼저 보강한다. 이미 결함에 가까운 구조 갭이므로 가장 안전하다.
2. 태그 삭제 전, 위 분류 정책을 `CLAUDE.md` 또는 별도 메타 페이지에 명문화한다.
3. 첫 정리 범위는 alias 이동 후보 10~20개로 제한한다.
4. 회차 tag는 바로 제거하지 말고 신규 추가 중단부터 적용한다.
5. 정리 후 `python3 scripts/wiki-lint.py --check --report`와 tag count를 재측정한다.

## 결론

태그 과밀은 현재 RAG 품질을 직접 깨는 P1 결함은 아니다. 이 위키는 tag보다 wikilink graph와 hub 페이지 중심으로 회수되기 때문이다. 하지만 Obsidian에서 tag pane을 본격적으로 쓸 생각이라면 P2로 올려도 된다.

가장 안전한 방향은 **삭제가 아니라 역할 분리**다. tags는 도메인 vocabulary, aliases는 표기 변종, logs는 회차 이력, wikilinks는 의미 연결이라는 네 역할을 분리해야 한다.

## 출처

- [[llm-wiki-pattern]] — 위키의 수동 인덱스 + 페이지 청킹 구조.
- [[using-llm-wiki-as-rag]] — LLM이 위키를 RAG처럼 사용하는 운영 방식.
- `wiki/**/*.md` live scan — 2026-04-29 태그 분포 측정.
