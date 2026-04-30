---
title: 포트폴리오 방법론 (docs/00-meta 합본)
type: source
source_type: note
source_url: ''
source_scope: local
raw_path: raw/notes/portfolio/docs/00-meta/
author: 석근
date_published: 2026-04-24
date_ingested: 2026-04-24
tags:
- methodology
- 3-layer
- johnny-decimal
- STAR
related:
- '[[seokgeun-kim]]'
- '[[portfolio-seed]]'
- '[[llm-wiki-pattern]]'
confidence: high
inbound_count: 13
cited_by:
- '[[career-timeline-seokgeun]]'
- '[[portfolio]]'
- '[[portfolio-seed]]'
- '[[seokgeun-kim]]'
cited_by_count: 4
aliases:
- Portfolio Method
- portfolio method
- 포트폴리오 방법론 (docs/00-meta 합본)
---

# 포트폴리오 방법론 (docs/00-meta 합본)

## 한줄 요약

> portfolio 저장소가 어떻게 구성·유지되는지를 정의한 메타 문서 4종의 합본. 3-Layer(Raw → Synthesis → Output) + Johnny.Decimal 파일 구조, 증거 기반 frontmatter, STAR 포맷 스토리텔링, 주기 업데이트 절차를 담는다.

## 핵심 내용

- **collection-strategy.md** — 소스별 수집 전략. Jira JQL, Confluence CQL, GitHub Search 쿼리 예시. 수집 주기(월간/분기), 민감도 분류(`docs/` 공개 vs `private/` 로컬 전용).
- **analysis-methodology.md** — STAR(Situation/Task/Action/Result) 프레임워크로 스토리 기록, 프로젝트-스킬 매핑 역링크 생성, metric 추출 규칙(숫자 근거 표기 의무).
- **document-conventions.md** — 파일 네이밍(`<period>-<slug>.md`), 프론트매터 스키마(`title`, `type`, `company`, `period`, `role`, `tech_stack`, `sources{}`, `tags`, `metrics`, `related_projects`, `star{}`), 마크다운 스타일 가이드.
- **update-workflow.md** — 주기적 업데이트 절차: 새 원천 수집 → `10-sources` 갱신 → `20-projects` 반영 → `30-skills`/`40-stories` 재생성 → `50-portfolio` 최종 렌더링. 단방향 의존성 강조.

## 주요 인사이트

- **llm-wiki와의 구조적 유사성**: portfolio의 3-Layer(Raw/Synthesis/Output)는 llm-wiki의 raw/(원시) → wiki/sources/(요약) → wiki/syntheses/(종합)과 정확히 매핑됨. 둘 다 "증거 기반"과 "단방향 가공 흐름"을 공유.
- **Johnny.Decimal (00–50)** 채택으로 AI 에이전트가 디렉토리 의미를 문맥 없이도 추론 가능 — LLM 친화적 IA.
- **Frontmatter `sources:` 필드의 역할**: 모든 합성 문서가 원천 증거 링크를 반드시 포함하도록 강제 → 최종 포트폴리오에서 "근거 없는 주장" 방지.

## 관련 엔티티/개념

- [[seokgeun-kim|석근 (이 위키 owner)]] — 이 방법론의 설계자이자 운영자
- [[llm-wiki-pattern]] — 동일한 "원천 → 요약 → 종합" 패턴의 일반화
- [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] — 본 방법론의 STAR 포맷이 32 OSS 의사결정 트리에서 "어떤 도구를 어떤 시나리오에 적용했는가"의 근거 형식으로 재사용됨 (3축↔이 source 교차 인용)
- [[matechat]] — 본 방법론을 사이드 프로젝트 운영 기록(matechat-launch-metrics-ledger 등)에 그대로 적용한 사례 (4축↔이 source 교차 인용)

## 메모

- 원본 경로: `raw/notes/portfolio/docs/00-meta/{collection-strategy,analysis-methodology,document-conventions,update-workflow}.md`.
- 개별 파일이 아닌 합본 형태로 수집: 각 파일이 자체로 독립된 가치를 갖기보다 4종이 한 세트로 작동하기 때문.
