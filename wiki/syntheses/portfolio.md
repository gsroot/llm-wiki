---
title: "포트폴리오 (Portfolio Hub)"
type: synthesis
category: guide
aliases: [포트폴리오, portfolio, 석근 포트폴리오, portfolio-hub, 9년 커리어 의사결정 지도]
tags: [포트폴리오, portfolio, career, 3-layer, johnny-decimal, STAR, hub, 33회차]
sources:
  - "[[portfolio-seed]]"
  - "[[portfolio-resume-ko]]"
  - "[[portfolio-ko]]"
  - "[[portfolio-method]]"
  - "[[c2spf-analytics-renewal]]"
  - "[[c2spf-analytics-common]]"
  - "[[c2spf-nft-market]]"
  - "[[c2spf-xpla-platform]]"
  - "[[mate-chat-project-wiki-2026]]"
related:
  - "[[seokgeun-kim]]"
  - "[[seokgeun-stack-guide]]"
  - "[[matechat]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[agent-skills]]"
  - "[[harness]]"
  - "[[mcp]]"
  - "[[claude-code]]"
created: 2026-04-29
updated: 2026-04-29
cited_by:
  - "[[agent-skills]]"
  - "[[backend-fastapi-stack]]"
  - "[[c2spf-analytics]]"
  - "[[c2spf-analytics-common]]"
  - "[[c2spf-analytics-renewal]]"
  - "[[c2spf-nft-market]]"
  - "[[c2spf-xpla-platform]]"
  - "[[claude-code]]"
  - "[[flutter-nextjs-fullstack-pattern]]"
  - "[[harness]]"
  - "[[kpi-recovery-loop]]"
  - "[[llm-infra-meta-cluster]]"
  - "[[mate-chat-project-wiki-2026]]"
  - "[[matechat]]"
  - "[[matechat-business-validation]]"
  - "[[mcp]]"
  - "[[nextjs]]"
  - "[[parental-leave-2026-operating-plan]]"
  - "[[portfolio-ko]]"
  - "[[portfolio-method]]"
  - "[[portfolio-resume-ko]]"
  - "[[portfolio-seed]]"
  - "[[seokgeun-kim]]"
  - "[[seokgeun-operating-profile-2026]]"
  - "[[seokgeun-stack-guide]]"
---

# 포트폴리오 (Portfolio Hub)

## 언제 읽어야 하는가

- "석근의 9년 커리어를 한 화면에 보고 싶다" — 이력서·면접·외부 소개에 인용할 때.
- "회사 c2spf와 사이드 MateChat이 어떻게 기술 스택을 검증하는가?" — 쌍 검증 매트릭스 표 (Layer 4) 진입.
- "포트폴리오 저장소(2개)와 위키가 어떻게 동기화되는가?" — 3-Layer 구조 (Layer 1) 진입.
- "다음 1인 사업화 의사결정에 어떤 입력이 필요한가?" → 열린 질문 + [[seokgeun-operating-profile-2026]] 연결.

> 33회차 신설 — "포트폴리오란?" 질의에 1-hop으로 도달하는 진입점. 4개 source 페이지(seed/resume/ko/method) + 5개 프로젝트 source를 통합한다.

## 요약

석근의 포트폴리오는 **2개 저장소가 동기화되는 3-Layer 구조**다. (1) `portfolio/` git 저장소(Johnny.Decimal IA + STAR 스토리)와 (2) `llm-wiki/` Obsidian 위키가 동일한 "Raw → Synthesis → Output" 흐름을 공유하며, 한쪽이 변경되면 다른 쪽이 감시·정정한다. 9년차 백엔드/풀스택 + 게임 데이터 BI + 블록체인 + AI 협업 운영의 4개 강점 축으로 구성되며, MateChat(사이드)과 c2spf(회사)가 동시에 "기술 스택 검증의 쌍"으로 작동한다.

## 배경

이 hub는 30~32회차 7축 평가에서 **"포트폴리오란?"이라는 자연 질의로 1-hop 도달이 불가능한 구조 결함**으로 식별되어 신설되었다. 기존에는 `portfolio-seed`(시드 문서)·`portfolio-resume-ko`(이력서)·`portfolio-ko`(상세본)·`portfolio-method`(방법론) 4개 source 페이지가 `wiki/sources/`에 흩어져 있었고, concept/synthesis 계층의 통합 hub가 없었다. RAG 회수 시 사용자가 "포트폴리오"로 질의해도 어느 source부터 봐야 할지 라우팅이 모호했다.

## 분석

### Layer 1: 포트폴리오의 3-Layer 구조 ([[portfolio-method]])

| Layer | portfolio/ 저장소 | llm-wiki/ 매핑 |
|---|---|---|
| **Raw (원천)** | `10-sources/` (Jira/Confluence/GitHub 추출) | `raw/notes/portfolio/` (불변) |
| **Synthesis (종합)** | `20-projects/` `30-skills/` `40-stories/` | `wiki/sources/` + `wiki/entities/` |
| **Output (산출)** | `50-portfolio/` (이력서·포트폴리오 최종본) | 본 hub + [[seokgeun-kim|석근 (이 위키 owner)]] |

**구조적 동치**: Raw → Synthesis → Output 단방향 가공 흐름이 두 저장소에서 동일. 이 동치성이 양 저장소의 자동 정합성 검증을 가능케 한다 (예: portfolio 저장소가 c2spf-analytics를 갱신하면 wiki/entities/c2spf-analytics.md도 갱신되어야 함).

### Layer 2: 4개 강점 축 ([[portfolio-seed]] + [[portfolio-ko]])

석근 9년 커리어의 자기 정의 강점 (출처: portfolio-seed 한줄 요약):

1. **백엔드/풀스택** — Python·FastAPI·Node.js·React. [[c2spf-analytics-renewal]](2025 React 리뉴얼)에서 풀스택 단독 운영 사례.
2. **게임 데이터 BI** — pandas·BigQuery·MMP. [[c2spf-analytics|c2spf 게임 데이터 BI]] 본진 + [[c2spf-analytics-common]](공통 모듈)이 핵심 자산.
3. **블록체인** — Rust·NestJS·XPLA. [[c2spf-nft-market]](가스비 절감)·[[c2spf-xpla-platform]](SDK)가 검증.
4. **AI/Agent 운영** — [[matechat|MateChat 사이드 프로젝트]] 사이드 프로젝트(39 SKILL 통합) + [[llm-infra-meta-cluster|LLM 인프라 메타 5축]] 메타 운영 체계. 1-hop 직결 도구: [[agent-skills|Claude Agent Skills]](39 skill 운영 표준) · [[harness|Agent Harness]](settings/hooks/output-styles 묶음) · [[mcp|Model Context Protocol]](외부 자원 연결 표준) · [[claude-code|Claude Code]](메인 IDE).

### Layer 3: STAR 스토리 + 증거 기반 metric ([[portfolio-method]])

`portfolio/40-stories/`의 모든 스토리는 STAR(Situation/Task/Action/Result) 프레임워크로 기록되며, Result에 반드시 정량 metric이 들어간다. 핵심 정량 주장 3건은 다음과 같은 검증 경로를 가진다 (49회차 P0-3 명시화):

| 주장 | 값 | 재현 경로 |
|---|---|---|
| c2spf 조직 본인 커밋 누계 | 1,111건 | `git log --author='석근' --oneline \| wc -l` (c2spf 조직 모든 리포지토리 합) |
| MateChat 통합 SKILL | 39개 (자작 11 + 외부 28) | `find mate-chat/.agents/skills -name 'SKILL.md' \| wc -l` 또는 `skills-lock.json § dependencies` |
| ML 유저 예측 평균 정확도 | 85%+ | GCP AutoML `evaluation_dashboard` 또는 `model_evaluation.json` |

`frontmatter.sources{}` 필드가 각 주장의 원천 증거 링크를 강제하여 "근거 없는 주장" 방지. RAG 답변 시 위 명령/경로를 함께 인용하면 사용자가 즉시 재현 가능.

### Layer 4: c2spf(회사) ↔ MateChat(사이드) 쌍 검증

| 영역 | 회사 (c2spf) | 사이드 (MateChat) | 시너지 |
|---|---|---|---|
| 백엔드 | FastAPI + PostgreSQL + Redis | 동일 스택 | 양방향 검증 (사이드가 더 민첩하게 신기능 검증 → 회사 차용) |
| AI/Agent | 미적용 (보수적) | 39 SKILL + 11 자작 | MateChat 자작 SKILL 9개가 c2spf 차용 후보 |
| 데이터 | BigQuery + pandas | SQLite + DuckDB | 규모 차이로 ETL 패턴 분기 |
| 출시 | B2B 내부 사용 | B2C Google Play v1.0.0 | 사용자 검증 SOP 학습 |

**핵심 발견**: 회사 시스템과 사이드 프로젝트가 **기술 스택 검증의 쌍**으로 동작한다. 사이드에서 검증된 패턴(예: agent-skills 통합)이 회사로 역수입되는 단방향 펌프가 형성됨.

## 결론

1. **포트폴리오 = 의사결정 지도**: 단순 이력 나열이 아닌, "다음 무엇을 할지" 판단할 수 있는 의사결정 자료. 9년 커리어가 4개 축으로 구조화되어 있어 신규 기회 평가 시 즉시 매핑 가능.
2. **2개 저장소 동기화가 핵심 자산**: portfolio/ + llm-wiki/ 양쪽이 동일 3-Layer 구조를 공유하므로 한쪽의 결함이 다른 쪽으로 자동 감지된다. 다른 개발자 포트폴리오에 없는 독자성.
3. **회사·사이드 쌍 검증 모델**: c2spf와 MateChat이 서로의 기술 검증 환경 — 이 모델은 [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]]의 "30분 부트스트랩" 시나리오로 정형화되어 있다.

## 열린 질문

- portfolio 저장소(`raw/notes/portfolio/`)와 wiki/syntheses/portfolio.md 간 자동 동기화 도구 도입 여부 — 현재는 수동 정합 보장.
- MateChat → c2spf 역수입 후보 9개 SKILL 중 실제 회사 도입된 항목 추적 (verification_required).
- 1인 사업화(2026) 시 포트폴리오 활용 방향: B2B 컨설팅 vs 자체 SaaS — [[seokgeun-operating-profile-2026]]에서 추적.

## 출처

- [[portfolio-seed]] — 9년 커리어의 시드 문서 (2025-11 작성, 4개 강점 축 정의)
- [[portfolio-resume-ko]] — 한국어 이력서 최종본 (이직 대비)
- [[portfolio-ko]] — 상세 포트폴리오 (selected-work 형식)
- [[portfolio-method]] — 방법론 (3-Layer + Johnny.Decimal + STAR + frontmatter 스키마)
- [[c2spf-analytics-renewal]] — 2025 React 리뉴얼 + Airbridge MMP 통합
- [[c2spf-analytics-common]] — 2024-08 공통 모듈 + Jenkins/Loki 배포
- [[c2spf-nft-market]] — 2022-05 NFT 마켓 가스비 절감
- [[c2spf-xpla-platform]] — 2024-04 XPLA SDK
- [[mate-chat-project-wiki-2026]] — MateChat 2026-04-28 스냅샷
- [[seokgeun-kim|석근 (이 위키 owner)]] — 본인 정체성 hub (1축)
- [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] — 32 OSS 스택 의사결정 트리 (3축)
- [[matechat|MateChat 사이드 프로젝트]] — MateChat canonical (4축)
- [[c2spf-analytics|c2spf 게임 데이터 BI]] — 회사 BI 본진 entity
- [[seokgeun-operating-profile-2026]] — 2026 운영 프레임 (1축)
