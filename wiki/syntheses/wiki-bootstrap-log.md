---
title: "위키 부트스트랩 기록"
type: synthesis
category: guide
tags: [메타, 운영, meta, setup, archive, 53회차]
sources: [[llm-wiki-idea-doc]]
page_intent: archive
page_intent_note: "2026-04-09 부트스트랩 시점 기록. 더 이상 갱신하지 않는 역사 기록 (synthesis 카테고리지만 archive 의도). 본문은 부트스트랩 의사결정 추적 자료로 보존."
created: 2026-04-09
updated: 2026-04-29
cited_by_count: 2
---

# 위키 부트스트랩 기록

## 요약

2026-04-09에 LLM 위키 패턴을 기반으로 개인 종합 위키를 초기 구축했다. 디렉토리 구조, 스키마, 템플릿, 인덱스/로그를 설계하고 생성했다.

## 배경

"LLM 위키" 아이디어 문서를 읽고, 이를 실제로 구현하기로 결정. 석근님의 관심사(AI, 데이터 분석, 게임 BI, 개인 성장)를 포괄하는 범용 개인 위키로 설계했다.

## 설계 결정 사항

### 도구 선택
- **Obsidian**: 위키 뷰어/탐색기. 그래프 뷰, Dataview, 위키링크 활용
- **Claude Code + Cowork**: 위키 작성/관리 에이전트. 집에서는 Claude Code(윈도우), 외출 시 Cowork 사용
- **Git**: 버전 관리. 수집 단위로 커밋

### 디렉토리 구조
- `raw/` 4개 하위 폴더 (articles, papers, notes, assets)
- `wiki/` 5개 하위 폴더 (entities, concepts, sources, syntheses, logs)
- `templates/` 4종 (source, entity, concept, synthesis)

### 한국어 위키 운영 원칙
- 파일명은 영어 kebab-case (URL/git 호환성)
- 제목(H1)은 한국어
- 태그는 한영 병기

## 다음 단계

1. ~~Obsidian에서 이 폴더를 볼트로 열기~~ *(완료)*
2. 추천 플러그인 설치: Linter, Templater, Dataview, Web Clipper
3. ~~첫 번째 소스를 `raw/`에 추가하고 수집 워크플로우 실행~~ *(완료 — llm_wiki.md 수집)*
4. 3~5개 소스를 수집한 후 스키마 개선 (첫 번째 반복)
5. 위키가 50페이지를 넘기면 [[qmd]] 검색 엔진 도입 검토

## 출처

- [[llm-wiki-idea-doc]] — 원본 아이디어 문서 (원문 + 역자 주석)
- [[llm-wiki-pattern]] — 이 패턴의 개념 정리
