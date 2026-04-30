---
title: "위키 인덱스"
type: index
updated: 2026-04-30b
rag_exclude: true
rag_exclude_reason: "인덱스는 카탈로그·라우터 역할. RAG가 사실 답변을 만들 때는 hub/concept/entity 페이지를 직접 인용해야 하고, 인덱스의 통계 숫자나 표를 근거로 답변하면 stale 정보(예: 페이지 수)가 노출됨."
---

# 위키 인덱스

> 이 위키의 모든 페이지를 카테고리별로 정리한 카탈로그입니다.
> LLM은 질의 시 이 파일을 먼저 읽어서 관련 페이지를 찾습니다.

## 통계

- 총 페이지 수: 199
- 소스 요약: 66
- 엔티티: 77 (mate-chat은 [[matechat|MateChat 사이드 프로젝트]]로 redirect, codex 신설 2026-04-30)
- 개념: 35 (rcif-prompt-pattern, chain-of-thought-prompting 신설 2026-04-30, progressive-disclosure 신설 2026-04-30 — Phase B audit 결과)
- 종합 분석: 20

---

## 이 위키의 5개 핵심 축

이 위키는 **5개 핵심축**으로 구성된다.

| # | 축 | 핵심 hub 페이지 | 인바운드 합산 | 역할 |
|---|---|---|---:|---|
| 1 | 개인 프로필 | [[seokgeun-kim|석근 (이 위키 owner)]] · [[seokgeun-operating-profile-2026]] · [[career-timeline-seokgeun]] · [[seokgeun-kim-profile-2026]] | 195 | 위키 소유자 정체성·운영 원칙·9년 커리어 타임라인 |
| 2 | 포트폴리오 | [[portfolio]] · [[portfolio-seed]] · [[portfolio-resume-ko]] · [[portfolio-ko]] · [[portfolio-method]] · [[c2spf-analytics|c2spf 게임 데이터 BI]] · [[c2spf-analytics-common]] · [[c2spf-analytics-renewal]] · [[c2spf-nft-market]] · [[c2spf-xpla-platform]] | 340 | 회사 BI(c2spf-analytics)·블록체인·이력서·상세 포트폴리오 |
| 3 | 스택 가이드 | [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] | 155 | 32개 OSS 6분류 카탈로그 + 시나리오별 의사결정 트리 + 30분 부트스트랩 |
| 4 | MateChat | [[matechat]] · [[seokgeun-mate-chat|석근 MateChat 본진 raw]] · [[seokgeun-matechat-validation]] · [[matechat-chat-analysis-module]] · [[matechat-project-knowledge-map]] | 243 | 사이드 프로젝트 (AI 소셜 메시징, v1.0.0 출시 직전 QA 단계 / 39 SKILL 운영 SOP) |
| 5 | LLM 인프라 메타 (의도된 핵심축) | [[llm-infra-meta-cluster]] · [[agent-skills]] · [[harness]] · [[mcp]] · [[claude-code]] | 752 | 명시화된 5번째 축 — 4축에 직교하는 메타 layer |

> **읽기 순서 가이드**: (1) 5축 식별 → 본 표 / (2) 본인 정체성 → [[seokgeun-operating-profile-2026]] / (3) 기술 의사결정 → [[seokgeun-stack-guide]] / (4) 메타 인식 → [[llm-infra-meta-cluster]]

---

## 소스 요약 (Sources)

| 파일 | 제목 | 유형 | 저자 | 수집일 | 태그 |
|------|------|------|------|--------|------|
| [[llm-wiki-idea-doc]] | LLM 위키 아이디어 문서 | note | 원저자 미상 (역자 주석 포함) | 2026-04-09 | 지식관리, LLM, 위키, RAG, obsidian |
| [[claude-code-overview]] | Claude Code 개요 | article | Anthropic | 2026-04-09 | claude-code, AI, 에이전트, 코딩도구 |
| [[claude-code-quickstart]] | Claude Code 빠른 시작 | article | Anthropic | 2026-04-15 | claude-code, 가이드, tutorial |
| [[claude-code-master-guide]] | 클로드 코드 중심 실전 마스터 가이드 | book | CHOI (@choi.openai) | 2026-04-15 | claude-code, cowork, 하네스, 거버넌스, 실무운영 |
| [[obsidian-guide]] | Obsidian 사용 가이드 | note | 석근 | 2026-04-15 | obsidian, 지식관리, 마크다운, notion |
| [[using-llm-wiki-as-rag]] | 이 LLM 위키를 Claude Code에서 RAG처럼 쓰는 법 | note | 석근 (Claude Code 세션) | 2026-04-16 | llm-wiki, RAG, claude-code, agent-skills, 운영가이드 |
| [[slash-commands-vs-agent-skills]] | Claude Code: Slash Commands vs Agent Skills | note | 석근 (Claude Code 세션) | 2026-04-16 | claude-code, skills, slash-command, 자동호출 |
| [[seokgeun-kim-profile-2026]] | 석근 프로필 (2026) | note | 석근 | 2026-04-28 | 개인프로필, seokgeun-kim, matechat, 육아휴직, 사업화, AI, fastapi, flutter, 가족, 생산성 |
| [[mate-chat-project-wiki-2026]] | mate-chat 프로젝트 위키 스냅샷 (2026-04-28) | note | 석근 + LLM-maintained Mate Chat wiki | 2026-04-28 | matechat, project-wiki, obsidian, fastapi, flutter, launch, architecture, iap, websocket, i18n, clover |
| [[portfolio-seed]] | 포트폴리오 시드 문서 | note | 석근 | 2026-04-24 | 포트폴리오, career, backend, data, ml, blockchain |
| [[portfolio-resume-ko]] | 포트폴리오 — 이력서(한국어) | note | 석근 | 2026-04-24 | 포트폴리오, resume, career, 이직 |
| [[portfolio-ko]] | 포트폴리오 — 상세 포트폴리오(한국어) | note | 석근 | 2026-04-24 | 포트폴리오, detailed-portfolio, selected-work |
| [[portfolio-method]] | 포트폴리오 방법론 (docs/00-meta 합본) | note | 석근 | 2026-04-24 | 방법론, 3-layer, johnny-decimal, STAR |
| [[c2spf-nft-market]] | 컴투스플랫폼 NFT 마켓 | note | 석근 | 2026-04-24 | com2us-platform, nft, blockchain, rust, 가스비절감 |
| [[c2spf-xpla-platform]] | 컴투스플랫폼 XPLA 플랫폼 | note | 석근 | 2026-04-24 | com2us-platform, xpla, blockchain, nestjs, SDK |
| [[c2spf-analytics-common]] | 컴투스플랫폼 애널리틱스 공통 모듈 & 배포 (2024-08) | note | 석근 | 2026-04-24 | com2us-platform, analytics, fastapi, jenkins, loki |
| [[c2spf-analytics-renewal]] | 컴투스플랫폼 애널리틱스 React 리뉴얼 + Airbridge (2025) | note | 석근 | 2026-04-24 | com2us-platform, analytics, react, vite, airbridge |
| [[karpathy-autoresearch]] | karpathy/autoresearch — 자율 LLM 실험 루프 | article | Andrej Karpathy | 2026-04-27 | autoresearch, karpathy, llm, 자율연구, agent, harness, val-bpb |
| [[karpathy-nanogpt]] | karpathy/nanoGPT — 가장 단순한 GPT 학습 코드 (deprecated) | article | Andrej Karpathy | 2026-04-27 | nanogpt, karpathy, gpt, llm, 교육코드, deprecated |
| [[karpathy-nanochat]] | karpathy/nanochat — $100짜리 ChatGPT 풀 파이프라인 | article | Andrej Karpathy | 2026-04-27 | nanochat, karpathy, llm, gpt2-speedrun, depth-dial, autoresearch |
| [[anthropics-skills]] | anthropics/skills — Anthropic 공식 Agent Skills 레퍼런스 | article | Anthropic | 2026-04-27 | agent-skills, anthropic, claude-code, marketplace, plugin, progressive-disclosure, skill-creator |
| [[microsoft-generative-ai-for-beginners]] | microsoft/generative-ai-for-beginners — 21 Lessons GenAI 입문 | article | Microsoft Cloud Advocates | 2026-04-27 | generative-ai, microsoft, microsoft-for-beginners, openai, prompt-engineering, rag, ai-agents |
| [[microsoft-ai-agents-for-beginners]] | microsoft/ai-agents-for-beginners — 12+ Lessons AI 에이전트 입문 | article | Microsoft Cloud Advocates | 2026-04-27 | ai-agents, microsoft, microsoft-agent-framework, mcp, a2a, nlweb, context-engineering |
| [[microsoft-ml-for-beginners]] | microsoft/ML-For-Beginners — 12 weeks, 26 Lessons 클래식 ML | article | Microsoft Cloud Advocates | 2026-04-27 | machine-learning, microsoft, scikit-learn, python, r, time-series, classification, clustering, nlp |
| [[microsoft-web-dev-for-beginners]] | microsoft/Web-Dev-For-Beginners — 12 weeks, 24 Lessons 웹 개발 입문 | article | Microsoft Cloud Advocates | 2026-04-27 | web-dev, microsoft, html, css, javascript, vanilla-js, project-based, github-copilot |
| [[microsoft-data-science-for-beginners]] | microsoft/Data-Science-For-Beginners — 10 weeks, 20 Lessons 데이터과학 입문 | article | Microsoft Cloud Advocates | 2026-04-27 | data-science, microsoft, pandas, sql, matplotlib, data-lifecycle, azure-ml, BI |
| [[anthropics-claude-cookbooks]] | anthropics/claude-cookbooks — Claude API · Agent SDK · Managed Agents 실습 노트북 모음 | article | Anthropic | 2026-04-27 | claude-cookbooks, anthropic, claude-agent-sdk, managed-agents, agent-patterns, prompt-caching, memory, tool-use, rag, multimodal |
| [[github-spec-kit]] | github/spec-kit — Spec-Driven Development 툴킷 (Specify CLI · 9개 슬래시 명령 · 30+ 에이전트 통합) | article | GitHub | 2026-04-27 | spec-kit, github, spec-driven-development, sdd, specify-cli, slash-command, agent-skills, claude-code, copilot, gemini, codex, harness, agent-patterns |
| [[pandas-dev-pandas]] | pandas-dev/pandas — Python 데이터 분석 표준 라이브러리 (BDFL+NumFOCUS+PDEP 3축 거버넌스) | article | The pandas development team (BDFL: Wes McKinney) | 2026-04-27 | pandas, python, dataframe, data-analysis, time-series, bigquery, BI, numfocus, bdfl, pdep, pyarrow, copy-on-write, ecosystem, scikit-learn, modin, dask, bigframes, pandera |
| [[fastapi-fastapi]] | fastapi/fastapi — 표준 기반 모던 Python 웹 프레임워크 (라이브러리 번들 SKILL.md) | article | Sebastián Ramírez (tiangolo) | 2026-04-27 | fastapi, tiangolo, python, pydantic, starlette, openapi, async, dependency-injection, agent-skills, SKILL.md, editor-support |
| [[astral-sh-uv]] | astral-sh/uv — Rust로 작성된 초고속 Python 패키지·프로젝트 관리자 | article | Astral | 2026-04-27 | uv, astral, python, package-manager, rust, pubgrub, universal-lockfile, pep-723, agents-md, virtualenv, pyenv, poetry, pipx, pip-tools |
| [[scikit-learn-scikit-learn]] | scikit-learn/scikit-learn — Python 머신러닝의 사실상 표준 라이브러리 (BSD-3, 2007~) | article | scikit-learn community (David Cournapeau / INRIA / NumFOCUS / probabl.ai) | 2026-04-27 | scikit-learn, sklearn, machine-learning, python, classic-ml, fit-predict-transform, pipeline, estimator-api, slep, governance, numfocus, probabl, agents-md, ai-disclosure |
| [[flutter-flutter]] | flutter/flutter — 단일 코드베이스 멀티플랫폼 UI SDK + vendor-neutral .agents/ 스킬 표준 | article | Google (Flutter Team) | 2026-04-27 | flutter, dart, google, multiplatform, ui-toolkit, mobile, web, desktop, skia, impeller, hot-reload, agent-skills, agentskills.io, vendor-neutral, progressive-disclosure, token-budget |
| [[openai-openai-cookbook]] | openai/openai-cookbook — OpenAI API 활용 코드·기사 4년 모음 + 살아있는 AGENTS.md | article | OpenAI (community resource) | 2026-04-27 | openai-cookbook, openai, openai-api, prompt-engineering, embeddings, fine-tuning, agents-sdk, codex, gpt-5, gpt-oss, harmony, evals, agents-md, plans-md, exec-plans, registry-yaml, recent-learnings |
| [[openai-openai-agents-python]] | openai/openai-agents-python — OpenAI Agents SDK 본체 + AGENTS.md=CLAUDE.md 동기화 + 9개 운영 SOP 스킬 | article | OpenAI (Agents Team) | 2026-04-28 | openai-agents-python, openai, agents-sdk, python, multi-agent, agent-framework, agent-skills, agents-md, plans-md, exec-plans, vendor-neutral, codex, mcp, uv, pyright, agent-patterns, guardrails, human-in-the-loop, runtime-behavior-probe, implementation-strategy |
| [[astral-sh-ruff]] | astral-sh/ruff — Rust로 작성된 초고속 Python 린터·포매터 (Astral 회사 차원 표준화) | article | Astral (Charlie Marsh 외) | 2026-04-28 | ruff, astral, python, linter, formatter, rust, ty, type-checker, agents-md, agent-skills, claude-md-import, monorepo, 800-rules, 10-100x, fastapi, pandas |
| [[pydantic-pydantic]] | pydantic/pydantic — Python 타입 힌트 기반 데이터 검증의 사실상 표준 (V2 ground-up rewrite + Logfire) | article | Samuel Colvin (Pydantic team) | 2026-04-28 | pydantic, python, validation, type-hints, json-schema, fastapi, openai-agents-python, mypy, pyright, logfire, v1-to-v2-migration, version-policy, llms-txt, hyperlint, vale, pydantic-core, rust-extension |
| [[sqlalchemy-sqlalchemy]] | sqlalchemy/sqlalchemy — Python SQL Toolkit + ORM (Core/ORM 이중 레이어 + 21년 관계형 추상화) | article | Mike Bayer (zzzeek) | 2026-04-28 | sqlalchemy, python, sql, orm, core, unit-of-work, identity-map, data-mapper, declarative, async, sqlmodel, alembic, mike-bayer, postgresql, dialect, dbapi, 2-0-style, annotated-mapped |
| [[sqlalchemy-alembic]] | sqlalchemy/alembic — SQLAlchemy 진영 데이터베이스 마이그레이션 도구 (autogenerate · transactional DDL · branch merging · offline SQL) | article | Mike Bayer (zzzeek) | 2026-04-28 | alembic, migration, sqlalchemy, python, ddl, transactional-ddl, autogenerate, branch-merging, sql-script-output, batch-migration, offline-migration, cookbook |
| [[postgres-postgres]] | postgres/postgres — PostgreSQL 본체 GitHub 미러 (★20.7K, ML+미러 거버넌스, 30년 보수파) | article | PostgreSQL Global Development Group (PGDG) | 2026-04-28 | postgresql, postgres, sql, rdbms, oss, mailing-list-governance, github-mirror, c-language, object-relational, mvcc, jsonb, replication, pgdg, pgvector, timescaledb |
| [[redis-redis]] | redis/redis — In-Memory Data Structure Server (★74K, 17년차 MANIFESTO 10항목 철학 + 단일 스레드 + Vector Search 전환) | article | Salvatore Sanfilippo (antirez 원저자) + Redis Labs | 2026-04-28 | redis, cache, in-memory-database, key-value-store, data-structure-server, message-broker, vector-databases, antirez, single-thread, manifesto, valkey, license-change-2024 |
| [[pola-rs-polars]] | pola-rs/polars — Rust 분석 쿼리 엔진 (Lazy + Eager + Streaming 3중 모델 + Apache Arrow immutable) | article | pola-rs (Ritchie Vink + 컨트리뷰터) | 2026-04-28 | polars, dataframe, rust, lazy-evaluation, query-optimization, apache-arrow, streaming, simd, multi-threaded, pyo3 |
| [[duckdb-duckdb]] | duckdb/duckdb — 임베디드 OLAP DB ("분석용 SQLite") + 풍부한 SQL 방언 + 파일=테이블 패러다임 | article | duckdb 개발팀 (Hannes Mühleisen + Mark Raasveldt + DuckDB Labs) | 2026-04-28 | duckdb, embedded, sql, analytical, columnar, vectorized, in-process, mit-license, c++17, cmake |
| [[apache-arrow]] | apache/arrow + apache/parquet-format — 인메모리/온디스크 컬럼 표준 통합 (Wes McKinney 발기, 11+ 언어, ASF PMC) | article | Apache Software Foundation (Wes McKinney 발기, Arrow PMC) | 2026-04-28 | apache-arrow, pyarrow, parquet, columnar, in-memory, ipc, flatbuffers, zero-copy, language-agnostic, asf, dremel |
| [[apache-kafka]] | apache/kafka — 분산 이벤트 스트리밍 플랫폼 ("Don't fear the filesystem!" + zero-copy + KRaft) | article | Apache Software Foundation + Confluent | 2026-04-28 | kafka, event-streaming, distributed-log, jvm, scala, zero-copy, sendfile, pagecache, pub-sub, asf, kraft, kip |
| [[microsoft-lightgbm]] | lightgbm-org/LightGBM — 2017 NIPS GBDT 표준 + Microsoft 졸업 (2026-03) + EffVer 버전 체계 | article | lightgbm-org (formerly Microsoft Research, Guolin Ke 외) | 2026-04-28 | lightgbm, gradient-boosting, gbdt, machine-learning, ml, microsoft, lightgbm-org, neurips, effver |
| [[langchain-ai-langchain]] | langchain-ai/langchain — The agent engineering platform (monorepo + AGENTS.md=CLAUDE.md + partners/ 모델) | article | LangChain Inc. (Harrison Chase 외) | 2026-04-28 | langchain, llm-framework, agent, monorepo, langchain-inc, langsmith, agents-md, claude-md |
| [[langchain-ai-langgraph]] | langchain-ai/langgraph — Pregel + Apache Beam + NetworkX 영감의 stateful agent 그래프 (Klarna/Replit/Elastic production) | article | LangChain Inc. | 2026-04-28 | langgraph, langchain-inc, agent, state-machine, durable-execution, pregel, apache-beam, networkx |
| [[jlowin-fastmcp]] | jlowin/fastmcp — MCP 사실 표준 (70% 점유, 일일 100만 다운로드) + 1.0 SDK 흡수 → 2.0 standalone | article | Jeremiah Lowin (Prefect) | 2026-04-28 | fastmcp, mcp, prefect, jlowin, model-context-protocol, agents-md, claude-md, prefect-horizon |
| [[langchain-ai-deepagents]] | langchain-ai/deepagents — batteries-included agent harness (LangGraph Native + 4종 도구 빌트인 + Deep Agents CLI) | article | LangChain Inc. | 2026-04-28 | deepagents, langchain-ai, langgraph-native, agent-harness, planning, filesystem, sub-agents, claude-code-pattern |
| [[crewaiinc-crewai]] | crewAIInc/crewAI — LangChain 독립 멀티 에이전트 프레임워크 (Crews+Flows) + Crew Control Plane SaaS (★50K, 100K+ 인증) | article | CrewAI Inc. | 2026-04-28 | crewai, multi-agent, role-playing, flows, crews, langchain-independent, oss-saas-dual, control-plane |
| [[sinaptik-ai-pandas-ai]] | sinaptik-ai/pandas-ai — DataFrame 자연어 대화 어댑터 (df.chat) + LiteLLM 다중 모델 (★23.5K) | article | Sinaptik AI | 2026-04-28 | pandas-ai, nl2sql, conversational-data, litellm, dataframe, bi-chatbot |
| [[pydantic-pydantic-ai]] | pydantic/pydantic-ai — Pydantic 팀의 type-safe agent framework + 11가지 강점 + AGENTS.md=CLAUDE.md 동기화 (★16.7K) | article | Pydantic Services Inc. (Samuel Colvin) | 2026-04-28 | pydantic-ai, type-safe-agent, model-agnostic, durable-execution, mcp, a2a, logfire, agents-md, claude-md |
| [[moby-moby]] | Moby (Docker Engine 업스트림) — 컨테이너 생태계의 레고 키트 (Docker v29에서 8년 분리 완성) | article | Moby Project (Docker Inc. + 커뮤니티) | 2026-04-28 | docker, moby, container, devops, runtime |
| [[github-actions-docs]] | GitHub Actions — Runner + Toolkit 양대 OSS + GHA 분산 생태계 | article | GitHub (actions/runner + actions/toolkit) | 2026-04-28 | github-actions, ci-cd, runner, toolkit, devops |
| [[prometheus-prometheus]] | Prometheus — CNCF 졸업 모니터링 시스템 + PR-패턴 AGENTS.md (148줄) | article | Prometheus Authors (CNCF) | 2026-04-28 | prometheus, cncf, monitoring, observability, time-series, promql, agents-md |
| [[grafana-grafana]] | Grafana — 멀티 데이터소스 시각화 + 계층화 AGENTS.md + `<!-- version: 2.0.0 -->` 버저닝 | article | Grafana Labs | 2026-04-28 | grafana, observability, dashboard, agents-md, hierarchical-agents |
| [[getsentry-sentry]] | Sentry — 에러 트래킹 + 반-fragmentation AGENTS.md SSOT (4-tier hierarchy + "do not add to CLAUDE.md") | article | Sentry (Functional Software, Inc.) | 2026-04-28 | sentry, error-tracking, observability, agents-md, anti-fragmentation, viewer-context |
| [[rrousselGit-riverpod]] | rrousselGit/riverpod — Flutter Favorite reactive caching + DI (Provider 후속작, Remi Rousselet) | article | Remi Rousselet | 2026-04-28 | riverpod, flutter, dart, state-management, reactive, dependency-injection |
| [[vercel-next.js]] | vercel/next.js — The React Framework + AGENTS.md 12단계 진화 (`$skill` 인덱싱 + LLM PR HTML 마커) | article | Vercel | 2026-04-28 | nextjs, react, vercel, ssr, app-router, turbopack, agents-md, skill-indexing, llm-pr-marker |
| [[tanstack-tanstack-query]] | TanStack/query — 서버 상태 관리 사실상 표준 (멀티 프레임워크 어댑터, TanStack 12 패키지) | article | Tanner Linsley + TanStack Team | 2026-04-28 | tanstack-query, react-query, server-state, async-state, multi-framework |
| [[pmndrs-zustand]] | pmndrs/zustand — React 클라이언트 상태 미니멀 챔피언 ("Bear necessities", providerless) | article | Daishi Kato + Poimandres | 2026-04-28 | zustand, react, state-management, hooks, flux, minimal |
| [[shadcn-ui-ui]] | shadcn-ui/ui — Open Code 패러다임 | article | shadcn | 2026-04-28 | shadcn-ui, react, components, tailwind, radix, open-code, code-distribution |
| [[seokgeun-mate-chat]] | Mate Chat — 석근 개인 사이드 프로젝트 | project | 석근 (Mate Chat Team) | 2026-04-29 | mate-chat, side-project, fastapi, flutter, riverpod, openai, websocket, oauth, in-app-purchase, sentry, prometheus, shadcn-ui-flutter, agent-skills, gstack |
| [[seokgeun-matechat-validation]] | MateChat v1.0 검증·출시 자료 (비전 / 구현 / 체크리스트 / 경쟁 / 매출 / 출시 진단 6 docs) | project | 석근 (Mate Chat Team) | 2026-04-28 | matechat, validation, kpi, release-checklist, competitive-analysis, revenue-projection, product-vision |
| [[openai-chatgpt-codex-guide]] | ChatGPT & Codex 실무 활용 가이드 (송영옥, wikidocs.net) — 8 Parts 28챕터 + 5부록 한국어 OpenAI 실무서, Path B 요약 수집 | book | 송영옥 | 2026-04-30 | openai, chatgpt, codex, prompt-engineering, 한국어자료, wikidocs, dall-e, custom-gpts, multimodal, agent, api |

## 개념 (Concepts)

| 파일 | 제목 | 태그 | 소스 수 | 최종 수정 |
|------|------|------|---------|-----------|
| [[llm-wiki-pattern]] | LLM 위키 패턴 | 지식관리, LLM, 위키, RAG, 하네스 | 3 | 2026-04-15 |
| [[mcp]] | MCP (Model Context Protocol) | MCP, LLM, 도구, 프로토콜, agentic-protocols, claude-cookbooks | 6 | 2026-04-27 |
| [[harness]] | 하네스 (Harness) | 하네스, 에이전트, 작업운영, 자율연구, bare-metal-harness, meta-harness, claude-cookbooks, spec-kit, library-as-harness, scikit-learn, slep, flutter, vendor-neutral, token-budget-tiers, openai-cookbook, openai-agents-python, plans-md, exec-plans, living-document, 9-sop-skills, skill-chaining | 8 | 2026-04-28 |
| [[token-economy]] | 토큰 경제학 (Token Economy) | 토큰, 비용, 컨텍스트, prompt-caching, claude-cookbooks | 2 | 2026-04-27 |
| [[context-engineering]] | 컨텍스트 엔지니어링 | 컨텍스트엔지니어링, 프롬프트엔지니어링, 자율연구, memory-cookbook, claude-cookbooks | 4 | 2026-04-27 |
| [[autonomous-research-loop]] | 자율 연구 루프 (Autonomous Research Loop) | 자율연구, agent, 메트릭주도, 시간예산, harness, gpt2-speedrun | 2 | 2026-04-27 |
| [[agent-skills]] | Agent Skills (SKILL.md 패키지) | agent-skills, skills, claude-code, anthropic, progressive-disclosure, agentskills.io, harness, claude-cookbooks, spec-kit, codex-skills, library-self-hosted-skill, fastapi, flutter, vendor-neutral, dart-skills-lint, token-budget-tiers, openai, openai-cookbook, openai-agents-python, agents-md-living, recent-learnings, exec-plans, 9-sop-skills, skill-chaining, agents-md-claude-md-mirror | 8 | 2026-04-28 |
| [[progressive-disclosure]] | 점진적 공개 (Progressive Disclosure) | progressive-disclosure, LLM, context, agent-skills, token-economy, ux-design, lazy-loading | 3 | 2026-04-30 |
| [[agent-patterns]] | Building Effective Agents — 5 패턴 | agent-patterns, building-effective-agents, anthropic, prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer, spec-kit, sdd, openai, openai-cookbook, openai-agents-python, agents-sdk, exec-plans, guardrails, human-in-the-loop, forced-tool-use, 11-patterns | 4 | 2026-04-28 |
| [[spec-driven-development]] | Spec-Driven Development (SDD) | spec-driven-development, sdd, spec-kit, prd, prompt-engineering, intent-driven-development, executable-specification, constitution, harness, methodology | 1 | 2026-04-27 |
| [[backend-python-fastapi]] | Python 백엔드 (FastAPI · Spring Boot) | backend, python, fastapi, spring-boot, tiangolo, agent-skills, annotated, pydantic2 | 6 | 2026-04-27 |
| [[frontend-react]] | 프론트엔드 (React + TS + Vite + TanStack) | frontend, react, typescript, vite, tanstack, ag-grid | 4 | 2026-04-24 |
| [[data-pipeline-bigquery]] | 데이터 파이프라인 (BigQuery 중심 BI) | data-pipeline, bigquery, mysql, BI, mmp, pandas, pandas-gbq, bigframes, pyarrow | 5 | 2026-04-27 |
| [[devops-cicd]] | DevOps & CI/CD (Docker · Jenkins · Loki) | devops, cicd, docker, jenkins, loki, grafana | 3 | 2026-04-24 |
| [[blockchain-xpla]] | 블록체인 (XPLA · Rust · NFT) | blockchain, xpla, nft, smart-contract, rust, gas-fee | 3 | 2026-04-24 |
| [[ml-ai]] | ML/AI (AutoML · LangGraph · OpenAI) | ml, ai, automl, langgraph, openai, llm, mlops, pandas, scikit-learn, sklearn, dataframe, slep, fit-predict, openai-cookbook, openai-agents-python, embeddings, agents-sdk, prompt-caching, gpt-5, gpt-oss, multi-agent-framework, guardrails, human-in-the-loop | 7 | 2026-04-28 |
| [[python-packaging]] | Python 패키징 (Python Packaging) | python-packaging, pip, poetry, uv, pyproject-toml, lockfile, pep-517, pep-518, pep-621, pep-723, pep-735, virtualenv, pyenv, pipx, dependency-resolution, supply-chain | 1 | 2026-04-27 |
| [[copy-on-write]] | Copy-on-Write (CoW) | copy-on-write, cow, pandas, 메모리관리, 성능, optimization | 1 | 2026-04-27 |
| [[dataframe]] | DataFrame | dataframe, pandas, polars, dask, 데이터분석, 자료구조, tabular-data | 1 | 2026-04-27 |
| [[prompt-cache]] | Prompt Caching | prompt-cache, claude, anthropic, llm-api, 토큰경제, latency, optimization | 1 | 2026-04-27 |
| [[pdep]] | PDEP (Pandas Enhancement Proposal) | pdep, pandas, governance, decision-record, proposal, open-source, roadmap | 1 | 2026-04-27 |
| [[bdfl]] | BDFL (Benevolent Dictator For Life) | bdfl, governance, open-source, decision-making, pandas, python | 1 | 2026-04-27 |
| [[lazy-evaluation]] | Lazy Evaluation (지연 평가) | lazy-evaluation, query-optimization, predicate-pushdown, projection-pushdown, dataframe, sql, polars, duckdb, spark | 2 | 2026-04-28 |
| [[observability]] | Observability — 메트릭/로그/트레이스 + 에러 + RUM | observability, monitoring, metrics, logs, traces, error-tracking, sre, prometheus, grafana, sentry, otel | 3 | 2026-04-28 |
| [[lakehouse]] | Lakehouse — Data Lake + Data Warehouse 통합 (Delta/Iceberg/Hudi) | lakehouse, data-warehouse, data-lake, parquet, delta-lake, iceberg | 3 | 2026-04-29 |
| [[streaming]] | Streaming (메시지 + 분석 엔진 두 의미) | streaming, kafka, polars, pubsub, real-time | 4 | 2026-04-29 |
| [[zero-copy]] | Zero-copy — Arrow/Parquet 변환 비용 0 | zero-copy, arrow, parquet, memory-model, performance | 4 | 2026-04-29 |
| [[append-only-log]] | Append-only Log — Kafka/WAL/AOF 공통 자료구조 | append-only-log, wal, kafka, log-structured, sequential-io | 4 | 2026-04-29 |
| [[predicate-pushdown]] | Predicate Pushdown — WHERE를 데이터 소스로 밀기 | predicate-pushdown, sql-optimization, parquet, duckdb, polars | 3 | 2026-04-29 |
| [[query-optimization]] | Query Optimization — 5대 표준 룰 | query-optimization, sql, planner, optimizer | 3 | 2026-04-29 |
| [[event-driven-architecture]] | Event-driven Architecture — EDA + CQRS + Event Sourcing | event-driven-architecture, eda, event-sourcing, cqrs, kafka, pubsub | 4 | 2026-04-29 |
| [[oss-saas-dual]] | OSS+SaaS 듀얼 모델 (5+1 사례) | oss-saas-dual, governance, business-model, langchain, polars, crewai | 5 | 2026-04-29 |

## 엔티티 (Entities)

| 파일 | 제목 | 유형 | 태그 | 소스 수 | 최종 수정 |
|------|------|------|------|---------|-----------|
| [[claude-code]] | Claude Code | tool | claude-code, AI, 에이전트, Anthropic, agent-skills, plugin-marketplace, claude-agent-sdk, bare-metal-harness, spec-kit | 8 | 2026-04-27 |
| [[claude-agent-sdk]] | Claude Agent SDK | tool | claude-agent-sdk, anthropic, sdk, agent, claude-code, mcp, hooks, plan-mode, output-styles, subagent | 1 | 2026-04-27 |
| [[claude-managed-agents]] | Claude Managed Agents | service | claude-managed-agents, cma, anthropic, hosted-runtime, agent, stateful-agent, sandbox, human-in-the-loop | 1 | 2026-04-27 |
| [[anthropic]] | Anthropic | organization | anthropic, AI, AI연구소, claude, claude-code, agent-skills, mcp, building-effective-agents | 4 | 2026-04-27 |
| [[cowork]] | Cowork | tool | cowork, AI, Anthropic, 지식업무 | 1 | 2026-04-15 |
| [[obsidian]] | Obsidian | tool | obsidian, 지식관리, 마크다운, vault | 1 | 2026-04-15 |
| [[memex]] | 메멕스 (Memex) | project | 지식관리, 정보검색, 역사 | 1 | 2026-04-09 |
| [[qmd]] | qmd | tool | 검색, 마크다운, CLI, MCP | 1 | 2026-04-09 |
| [[obsidian-web-clipper]] | Obsidian Web Clipper | tool | obsidian, 웹클리핑, 소스수집 | 1 | 2026-04-09 |
| [[seokgeun-kim]] | 김석근 (Seokgeun Kim) | person | 석근, owner, 백엔드, 풀스택, BI, matechat | 8 | 2026-04-28 |
| [[matechat]] | MateChat (canonical) — v1.0.0 출시 직전 QA 단계 + 39 SKILL (자작 11 + 외부 28) + 위키 발견 종합 실증 | project | matechat, mate-chat, 메이트챗, AI, social, fastapi, flutter, riverpod, openai, websocket, iap, clover, sentry, prometheus, agent-skills, gstack, v1.0.0, project-wiki | 6 | 2026-04-29 |
| [[mate-chat]] | (redirect → [[matechat]]) | redirect | redirect, alias, matechat | 0 | 2026-04-28 |
| [[com2us-platform|컴투스플랫폼 c2spf]] | 컴투스플랫폼 (Com2usPlatform, c2spf) | organization | 컴투스플랫폼, c2spf, 게임플랫폼, BI, 블록체인 | 6 | 2026-04-24 |
| [[c2spf-analytics]] | c2spf 애널리틱스 (게임 데이터 BI) | service | analytics, c2spf, BI, 게임데이터, fastapi, react | 4 | 2026-04-24 |
| [[xpla-platform]] | XPLA 플랫폼 (블록체인 통합 서비스) | service | xpla, blockchain, nft, smart-contract, c2spf | 3 | 2026-04-24 |
| [[karpathy]] | Andrej Karpathy | person | karpathy, AI, llm, openai, tesla, 교육콘텐츠, nanogpt, nanochat | 3 | 2026-04-27 |
| [[autoresearch]] | autoresearch (karpathy/autoresearch) | project | autoresearch, llm, agent, 자율연구, val-bpb, 단일파일 | 1 | 2026-04-27 |
| [[nanogpt]] | nanoGPT (karpathy/nanoGPT) | project | nanogpt, gpt, llm, 교육코드, deprecated, 단일파일 | 1 | 2026-04-27 |
| [[nanochat]] | nanochat (karpathy/nanochat) | project | nanochat, llm, gpt2-speedrun, depth-dial, 풀파이프라인 | 1 | 2026-04-27 |
| [[microsoft]] | Microsoft | organization | microsoft, microsoft-cloud-advocates, microsoft-for-beginners, openai, azure, github, devrel | 5 | 2026-04-27 |
| [[microsoft-for-beginners]] | microsoft-for-beginners (시리즈) | project | microsoft-for-beginners, microsoft, curriculum, 무료교육, project-based-learning, co-op-translator | 5 | 2026-04-27 |
| [[github]] | GitHub | organization | github, microsoft, copilot, spec-kit, marketplace, codespaces, octoverse, devops | 1 | 2026-04-27 |
| [[spec-kit]] | Spec Kit (Specify CLI) | tool | spec-kit, specify-cli, github, spec-driven-development, sdd, slash-command, agent-skills, claude-code, copilot, gemini, codex, multi-agent | 1 | 2026-04-27 |
| [[pandas]] | pandas (데이터 분석 라이브러리) | tool | pandas, python, dataframe, data-analysis, time-series, BI, scikit-learn, numpy, pyarrow, bigquery, copy-on-write | 1 | 2026-04-27 |
| [[pandas-dev]] | pandas-dev (GitHub 조직) | organization | pandas-dev, github-org, numfocus, bdfl, pdep, governance, oss-governance, wes-mckinney | 1 | 2026-04-27 |
| [[numfocus]] | NumFOCUS | organization | numfocus, pydata, nonprofit, open-source, governance, pandas, scikit-learn | 2 | 2026-04-27 |
| [[fastapi]] | FastAPI | tool | fastapi, python, web-framework, asgi, openapi, pydantic, starlette, tiangolo, agent-skills, SKILL.md, dependency-injection, type-hints, sqlalchemy, postgresql, ruff, uv | 1 | 2026-04-28 |
| [[tiangolo]] | Sebastián Ramírez (tiangolo) | person | tiangolo, sebastian-ramirez, python, oss, fastapi, pydantic-contributor, starlette-contributor, typer, sqlmodel, asyncer, fastapi-cloud | 1 | 2026-04-27 |
| [[astral]] | Astral | organization | astral, charlie-marsh, ruff, uv, ty, python, rust, dev-tools, open-source, vc-backed, company-level-standardization | 2 | 2026-04-28 |
| [[uv]] | uv (astral-sh/uv) | tool | uv, astral, python, package-manager, rust, pubgrub, universal-lockfile, pep-723, virtualenv, pyenv, poetry, pipx, pip-tools, twine, agents-md | 1 | 2026-04-27 |
| [[flutter]] | Flutter | tool | flutter, dart, google, ui-toolkit, multiplatform, mobile, web, desktop, skia, impeller, hot-reload, material-design, cupertino, agent-skills, agentskills.io, vendor-neutral | 1 | 2026-04-27 |
| [[dart]] | Dart | tool | dart, programming-language, google, flutter, aot, jit, javascript-compile, wasm, sound-null-safety, isolates | 1 | 2026-04-27 |
| [[google]] | Google | organization | google, alphabet, big-tech, gemini, antigravity, flutter, dart, android, chrome, skia, deepmind, cloud, devrel, ai | 1 | 2026-04-27 |
| [[scikit-learn]] | scikit-learn (sklearn) | tool | scikit-learn, sklearn, machine-learning, python, library, classic-ml, fit-predict-transform, pipeline, BSD-3, numfocus, probabl, slep, agents-md | 2 | 2026-04-27 |
| [[openai]] | OpenAI | organization | openai, AI, AI연구소, 샌프란시스코, gpt, chatgpt, dall-e, codex, gpt-oss, agents-sdk, responses-api, harmony-format, openai-cookbook, openai-agents-python, openai-agents | 2 | 2026-04-28 |
| [[openai-cookbook]] | openai-cookbook (OpenAI Cookbook) | project | openai-cookbook, openai, cookbook, mit, jupyter-notebook, registry-yaml, authors-yaml, agents-md, plans-md, exec-plans, recent-learnings, embeddings, agents-sdk, evals, codex | 1 | 2026-04-27 |
| [[openai-agents-python]] | openai-agents-python (OpenAI Agents SDK) | tool | openai-agents-python, openai-agents, openai, agents-sdk, python, multi-agent, agent-framework, mit-license, mcp, uv, pyright, agents-md, plans-md, exec-plans, agent-skills, codex, runtime-behavior-probe, implementation-strategy | 1 | 2026-04-28 |
| [[ruff]] | Ruff (astral-sh/ruff) | tool | ruff, astral, python, linter, formatter, rust, ty, mdtest, salsa-incrementality, agents-md, claude-md-import, monorepo-cascading, 800-rules, preview-mode | 1 | 2026-04-28 |
| [[pydantic]] | Pydantic (pydantic/pydantic) | tool | pydantic, python, validation, type-hints, json-schema, fastapi, openai-agents-python, mypy, pyright, pydantic-core, rust-extension, v1-to-v2-migration, version-policy, samuel-colvin, llms-txt, hyperlint, vale, logfire, pydantic-ai, annotated, pep-593 | 1 | 2026-04-28 |
| [[sqlalchemy]] | SQLAlchemy (sqlalchemy/sqlalchemy) | tool | sqlalchemy, python, sql, orm, core, unit-of-work, identity-map, data-mapper, declarative, async, sqlmodel, alembic, mike-bayer, postgresql, dialect, dbapi, 2-0-style, annotated-mapped, bdfl | 1 | 2026-04-28 |
| [[alembic]] | Alembic (sqlalchemy/alembic) | tool | alembic, migration, sqlalchemy, python, ddl, transactional-ddl, autogenerate, branch-merging, sql-script-output, batch-migration, sqlite-batch, mike-bayer, postgresql, offline-migration, cookbook | 1 | 2026-04-28 |
| [[postgresql]] | PostgreSQL | tool | postgresql, postgres, sql, rdbms, oss, mailing-list-governance, github-mirror, sqlalchemy, c-language, object-relational, mvcc, fdw, jsonb, replication, pgdg, pgvector, timescaledb, postgis, extension-system, bsd-license, no-pull-requests, stonebraker | 1 | 2026-04-28 |
| [[redis]] | Redis | tool | redis, cache, in-memory-database, key-value-store, data-structure-server, message-broker, vector-databases, vector-search, json, time-series, antirez, single-thread, manifesto, valkey, license-change-2024, rdb, aof, redis-cluster | 1 | 2026-04-28 |
| [[polars]] | Polars | tool | polars, dataframe, rust, lazy-evaluation, query-optimization, apache-arrow, streaming, simd, multi-threaded, pyo3, immutable, pola-rs | 1 | 2026-04-28 |
| [[duckdb]] | DuckDB | tool | duckdb, embedded, sql, analytical, columnar, vectorized, in-process, mit-license, c++17, olap, sqlite-for-olap, motherduck | 1 | 2026-04-28 |
| [[pyarrow]] | PyArrow | tool | pyarrow, apache-arrow, columnar, in-memory, zero-copy, parquet, ipc, python, pandas-backend, adbc, gandiva | 1 | 2026-04-28 |
| [[kafka]] | Apache Kafka | tool | kafka, event-streaming, distributed-log, jvm, scala, zero-copy, sendfile, pagecache, pub-sub, asf, kraft, kip, confluent | 1 | 2026-04-28 |
| [[parquet]] | Apache Parquet | tool | parquet, columnar, on-disk, file-format, dremel, thrift, compression, encoding, hadoop, asf, big-data | 1 | 2026-04-28 |
| [[lightgbm]] | LightGBM | tool | lightgbm, ml, gbdt, gradient-boosting, decision-tree, machine-learning, microsoft, lightgbm-org, neurips, effver | 1 | 2026-04-28 |
| [[langchain]] | LangChain | tool | langchain, llm-framework, agent, langchain-inc, monorepo, langsmith, deepagents, agents-md, claude-md | 1 | 2026-04-28 |
| [[langgraph]] | LangGraph | tool | langgraph, langchain-inc, agent, state-machine, durable-execution, pregel, apache-beam, networkx, checkpoint | 1 | 2026-04-28 |
| [[fastmcp]] | FastMCP | tool | fastmcp, mcp, prefect, jlowin, model-context-protocol, agents-md, claude-md, prefect-horizon, oss-evolution | 1 | 2026-04-28 |
| [[deepagents]] | DeepAgents | tool | deepagents, langchain-ai, langgraph-native, agent-harness, planning, filesystem, sub-agents, claude-code-pattern | 1 | 2026-04-28 |
| [[crewai]] | CrewAI | tool | crewai, multi-agent, role-playing, flows, crews, langchain-independent, oss-saas-dual, control-plane | 1 | 2026-04-28 |
| [[pandas-ai]] | PandasAI | tool | pandas-ai, nl2dataframe, conversational-data, litellm, sinaptik-ai, bi-chatbot | 1 | 2026-04-28 |
| [[pydantic-ai]] | Pydantic AI | tool | pydantic-ai, type-safe-agent, model-agnostic, durable-execution, mcp, a2a, logfire, agents-md, claude-md, capability | 1 | 2026-04-28 |
| [[docker]] | Docker / Moby | tool | docker, moby, container, runtime, devops | 1 | 2026-04-28 |
| [[github-actions]] | GitHub Actions | service | github-actions, ci-cd, runner, toolkit, devops, oidc | 1 | 2026-04-28 |
| [[prometheus]] | Prometheus | tool | prometheus, cncf, monitoring, observability, time-series, promql, agents-md | 1 | 2026-04-28 |
| [[grafana]] | Grafana | tool | grafana, observability, dashboard, agents-md, hierarchical-agents | 1 | 2026-04-28 |
| [[sentry]] | Sentry | tool | sentry, error-tracking, observability, agents-md, anti-fragmentation, viewer-context | 1 | 2026-04-28 |
| [[riverpod]] | Riverpod | tool | riverpod, flutter, dart, state-management, dependency-injection, reactive | 1 | 2026-04-28 |
| [[nextjs]] | Next.js | tool | nextjs, react, vercel, ssr, app-router, turbopack, agents-md, skill-indexing | 1 | 2026-04-28 |
| [[tanstack-query]] | TanStack Query | tool | tanstack-query, react-query, server-state, async-state, multi-framework | 1 | 2026-04-28 |
| [[zustand]] | Zustand | tool | zustand, react, state-management, hooks, flux, minimal, providerless | 1 | 2026-04-28 |
| [[shadcn-ui]] | shadcn/ui | tool | shadcn-ui, react, components, tailwind, radix, open-code, code-distribution | 1 | 2026-04-28 |
| [[turbopack]] | Turbopack | tool | turbopack, vercel, rust, bundler, nextjs, build-tool | 1 | 2026-04-29 |
| [[radix-ui]] | Radix UI | tool | radix-ui, react, primitives, accessibility, headless | 1 | 2026-04-29 |
| [[tailwindcss]] | Tailwind CSS | tool | tailwindcss, css, utility-first, atomic-css | 2 | 2026-04-29 |
| [[poimandres]] | Poimandres | organization | poimandres, collective, react, three-fiber, zustand, jotai, valtio | 1 | 2026-04-29 |
| [[tanstack]] | TanStack | organization | tanstack, tanner-linsley, react, query, table, router, form | 1 | 2026-04-29 |
| [[sqlite]] | SQLite | tool | sqlite, embedded-database, sql, c, single-file | 3 | 2026-04-29 |
| [[apache-foundation]] | Apache Software Foundation | organization | apache-software-foundation, asf, oss-governance, pmc, vendor-neutral | 2 | 2026-04-29 |
| [[vercel]] | Vercel | organization | vercel, organization, frontend, edge, nextjs, turbopack, ai-sdk | 1 | 2026-04-28 |
| [[react]] | React | tool | react, javascript, ui-library, meta, frontend, hooks, jsx | 5 | 2026-04-29 |
| [[python]] | Python | language | python, language, dynamic-typing, gil, asyncio | 8 | 2026-04-29 |

## 종합 분석 (Syntheses)

| 파일 | 제목 | 태그 | 최종 수정 |
|------|------|------|-----------|
| [[career-timeline-seokgeun]] | 석근 커리어 타임라인 (2016-2026) | career, timeline, evolution | 2026-04-24 |
| [[seokgeun-operating-profile-2026]] | 석근 개인 운영 프로필 (2026) | personal-operating-profile, matechat, 육아휴직, 사업화, 가족, ai-collaboration | 2026-04-28 |
| [[matechat-project-knowledge-map]] | MateChat 프로젝트 지식 지도 | matechat, project-knowledge-map, architecture, launch, user-validation, business-strategy | 2026-04-28 |
| [[agent-stack-evolution]] | 에이전트 스택의 6축 진화 — Microsoft · Anthropic · Karpathy · GitHub · Google · OpenAI 비교 | 비교분석, agent-stack, microsoft, anthropic, karpathy, github, google, openai, harness, BI, 개인비서, exec-plans, recent-learnings, self-adoption, 9-sop-skills, agents-md-claude-md-mirror | 2026-04-28 |
| [[backend-fastapi-stack]] | Python 백엔드 표준 스택 — FastAPI + Pydantic + SQLAlchemy + Alembic + PostgreSQL + Redis (Astral 도구 + 7개 거버넌스 모델 공존) | backend-stack, fastapi, pydantic, sqlalchemy, alembic, postgresql, redis, ruff, uv, ty, astral, type-first-python, annotated-pep-593, async-python, oltp, cache, governance-models, bdfl, mailing-list, manifesto, agent-skills, rust-extensions | 2026-04-28 |
| [[dataframe-ecosystem-evolution]] | DataFrame 생태계 진화사 — Pandas → PyArrow → Polars → DuckDB (4단계 18년 진화 + ASF PMC 8번째 거버넌스) | dataframe, pandas, polars, duckdb, pyarrow, parquet, apache-arrow, kafka, lazy-evaluation, columnar, ecosystem-evolution | 2026-04-28 |
| [[pandas-vs-polars-vs-duckdb]] | Pandas vs Polars vs DuckDB — 정량 비교 매트릭스 (의사결정 트리 + 마이그레이션 ROI) | comparison, pandas, polars, duckdb, dataframe, decision-matrix | 2026-04-28 |
| [[agent-frameworks-matrix]] | Agent Frameworks Matrix — 6 프레임워크 정량 비교 | comparison, agent-framework, langgraph, openai-agents-python, fastmcp, langchain, deepagents, crewai, pydantic-ai, pandas-ai, decision-matrix, durable-execution, state-machine, mcp | 2026-04-28 |
| [[observability-and-cicd-stack]] | Observability + CI/CD Stack — Docker → GHA → Prometheus → Grafana → Sentry 5단 흐름 (AGENTS.md 11단계 진화 + 4가지 새 변종) | observability, cicd, docker, github-actions, prometheus, grafana, sentry, agents-md, anti-fragmentation, hierarchical-agents-md, cncf | 2026-04-28 |
| [[flutter-nextjs-fullstack-pattern]] | Flutter + Next.js 듀얼 클라이언트 풀스택 패턴 (AGENTS.md 12단계 진화 + Open Code 10번째 거버넌스 모델) | frontend, fullstack, flutter, nextjs, react, state-management, riverpod, zustand, tanstack-query, shadcn-ui | 2026-04-28 |
| [[seokgeun-stack-guide]] | 석근 스택 가이드 — 6분류 카탈로그 + 사이드 프로젝트 30분 부트스트랩 + 회사 BI 적용 | personal-stack, decision-tree, side-project, c2spf-bi, seokgeun | 2026-04-28 |
| [[matechat-chat-analysis-module]] | Mate Chat 채팅 분석 모듈 — 7축 분석 + BigQuery 파이프라인 (3 형제 프로젝트 발견 + 회사 BI 4축 차용) | matechat, chat-analysis, bigquery, analytics, kakao-talk, ml, side-project, c2spf-bi-applicable | 2026-04-28 |
| [[llm-infra-meta-cluster]] | LLM 인프라 메타 클러스터 — 위키의 숨은 5번째 축 (agent-skills 58 + harness 49 + mcp 36 + claude-code 36 = 인바운드 179) | meta-cluster, llm-infrastructure, agent-skills, harness, mcp, claude-code, governance, evolution-axis, hidden-axis | 2026-04-28 |
| [[portfolio]] | 포트폴리오 (Portfolio Hub) — 4개 source + 5개 프로젝트를 통합한 1-hop 진입점 | 포트폴리오, portfolio, career, 3-layer, johnny-decimal, STAR, hub | 2026-04-29 |
| [[parental-leave-2026-operating-plan]] | 2026 육아휴직 1년 운영 계획 (월간 회고로 갱신 + verification_required) | 육아휴직, 운영계획, 가족, matechat, 사업화, 시간예산, burnout-risk, operating-plan | 2026-04-29 |
| [[matechat-30day-validation-loop]] | MateChat 30일 검증 루프 — 알파 KPI 회수 SOP | matechat, 30일검증, alpha-validation, kpi, 검증루프, retention, conversion, post-launch | 2026-04-29 |
| [[c2spf-ai-agent-adoption-candidates]] | c2spf AI Agent 도입 후보 — MateChat 자작 SKILL 9건 + 차용 매트릭스 | c2spf, agent-adoption, matechat, agent-skills, skill, 차용매트릭스, poc, company-bi | 2026-04-29 |
| [[kpi-recovery-loop]] | KPI 측정값 회수 루프 — 의사결정 → 실측 → 위키 갱신 SOP | kpi, 측정, 회수루프, sop, 의사결정, verification-required, matechat, c2spf | 2026-04-29 |
| [[matechat-business-validation]] | MateChat 사업 검증 카탈로그 (4축 sub-cluster) | matechat, 사업검증, business-validation, 4축, 출시후, post-launch, retention, conversion, marketing | 2026-04-29 |
| [[matechat-launch-metrics-ledger]] | MateChat 출시 후 실측 ledger (D+1/D+7/D+30 KPI 회수) | matechat, 실측, ledger, post-launch, retention, conversion, funnel, 인터뷰, 4축, raw-metrics | 2026-04-29 |
