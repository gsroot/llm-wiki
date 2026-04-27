---
title: "위키 인덱스"
type: index
updated: 2026-04-27 (6회차)
---

# 위키 인덱스

<!-- 수집일 2026-04-15: 클로드코드 가이드북(CHOI, 848페이지 PDF) 수집으로 페이지 다수 추가 -->
<!-- 수집일 2026-04-24: portfolio 커리어 자료 베이스 통합 수집 — 소스 8 + 엔티티 4 + 개념 6 + 종합분석 1 추가 -->
<!-- 수집일 2026-04-27: karpathy/autoresearch 수집 — 소스 1 + 엔티티 2 (karpathy, autoresearch) + 개념 1 (autonomous-research-loop) 추가 -->
<!-- 수집일 2026-04-27 (2회차): karpathy/nanoGPT + karpathy/nanochat 수집 — 소스 2 + 엔티티 2 (nanogpt, nanochat) 추가, 자율 루프 실증(nanochat 리더보드 #5/#6) 반영 -->
<!-- 수집일 2026-04-27 (3회차): anthropics/skills 수집 — 소스 1 + 개념 1 (agent-skills) 추가, claude-code 갱신 -->
<!-- 수집일 2026-04-27 (4회차): microsoft for-beginners 5종 수집 — 소스 5 + 엔티티 2 (microsoft, microsoft-for-beginners) 추가, mcp·context-engineering 보강 -->
<!-- 수집일 2026-04-27 (5회차): anthropics/claude-cookbooks 수집 — 소스 1 + 엔티티 2 (anthropic, claude-agent-sdk) + 개념 1 (agent-patterns) 추가, claude-code/agent-skills/harness/context-engineering/token-economy/mcp 6개 페이지 보강 -->
<!-- 후속 분석 2026-04-27 (5회차 후속): synthesis/agent-stack-evolution.md 신설 — Microsoft "단일 운영체계" / Anthropic "표준-구현 분리" / Karpathy "minimal harness" 3축 비교 종합 분석 -->


> 이 위키의 모든 페이지를 카테고리별로 정리한 카탈로그입니다.
> LLM은 질의 시 이 파일을 먼저 읽어서 관련 페이지를 찾습니다.

## 통계

- 총 페이지 수: 61
- 소스 요약: 25
- 엔티티: 18
- 개념: 14
- 종합 분석: 3

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

## 개념 (Concepts)

| 파일 | 제목 | 태그 | 소스 수 | 최종 수정 |
|------|------|------|---------|-----------|
| [[llm-wiki-pattern]] | LLM 위키 패턴 | 지식관리, LLM, 위키, RAG, 하네스 | 3 | 2026-04-15 |
| [[mcp]] | MCP (Model Context Protocol) | MCP, LLM, 도구, 프로토콜, agentic-protocols, claude-cookbooks | 6 | 2026-04-27 |
| [[harness]] | 하네스 (Harness) | 하네스, 에이전트, 작업운영, 자율연구, bare-metal-harness, claude-cookbooks | 4 | 2026-04-27 |
| [[token-economy]] | 토큰 경제학 (Token Economy) | 토큰, 비용, 컨텍스트, prompt-caching, claude-cookbooks | 2 | 2026-04-27 |
| [[context-engineering]] | 컨텍스트 엔지니어링 | 컨텍스트엔지니어링, 프롬프트엔지니어링, 자율연구, memory-cookbook, claude-cookbooks | 4 | 2026-04-27 |
| [[autonomous-research-loop]] | 자율 연구 루프 (Autonomous Research Loop) | 자율연구, agent, 메트릭주도, 시간예산, harness, gpt2-speedrun | 2 | 2026-04-27 |
| [[agent-skills]] | Agent Skills (SKILL.md 패키지) | agent-skills, skills, claude-code, anthropic, progressive-disclosure, agentskills.io, harness, claude-cookbooks | 3 | 2026-04-27 |
| [[agent-patterns]] | Building Effective Agents — 5 패턴 | agent-patterns, building-effective-agents, anthropic, prompt-chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer | 1 | 2026-04-27 |
| [[backend-python-fastapi]] | Python 백엔드 (FastAPI · Spring Boot) | backend, python, fastapi, spring-boot | 5 | 2026-04-24 |
| [[frontend-react]] | 프론트엔드 (React + TS + Vite + TanStack) | frontend, react, typescript, vite, tanstack, ag-grid | 4 | 2026-04-24 |
| [[data-pipeline-bigquery]] | 데이터 파이프라인 (BigQuery 중심 BI) | data-pipeline, bigquery, mysql, BI, mmp | 4 | 2026-04-24 |
| [[devops-cicd]] | DevOps & CI/CD (Docker · Jenkins · Loki) | devops, cicd, docker, jenkins, loki, grafana | 3 | 2026-04-24 |
| [[blockchain-xpla]] | 블록체인 (XPLA · Rust · NFT) | blockchain, xpla, nft, smart-contract, rust, gas-fee | 3 | 2026-04-24 |
| [[ml-ai]] | ML/AI (AutoML · LangGraph · OpenAI) | ml, ai, automl, langgraph, openai, llm, mlops | 3 | 2026-04-24 |

## 엔티티 (Entities)

| 파일 | 제목 | 유형 | 태그 | 소스 수 | 최종 수정 |
|------|------|------|------|---------|-----------|
| [[claude-code]] | Claude Code | tool | claude-code, AI, 에이전트, Anthropic, agent-skills, plugin-marketplace, claude-agent-sdk, bare-metal-harness | 7 | 2026-04-27 |
| [[claude-agent-sdk]] | Claude Agent SDK | tool | claude-agent-sdk, anthropic, sdk, agent, claude-code, mcp, hooks, plan-mode, output-styles, subagent | 1 | 2026-04-27 |
| [[anthropic]] | Anthropic | organization | anthropic, AI, AI연구소, claude, claude-code, agent-skills, mcp, building-effective-agents | 4 | 2026-04-27 |
| [[cowork]] | Cowork | tool | cowork, AI, Anthropic, 지식업무 | 1 | 2026-04-15 |
| [[obsidian]] | Obsidian | tool | obsidian, 지식관리, 마크다운, vault | 1 | 2026-04-15 |
| [[memex]] | 메멕스 (Memex) | project | 지식관리, 정보검색, 역사 | 1 | 2026-04-09 |
| [[qmd]] | qmd | tool | 검색, 마크다운, CLI, MCP | 1 | 2026-04-09 |
| [[obsidian-web-clipper]] | Obsidian Web Clipper | tool | obsidian, 웹클리핑, 소스수집 | 1 | 2026-04-09 |
| [[seokgeun-kim]] | 김석근 (Seokgeun Kim) | person | 석근, owner, 백엔드, 풀스택, BI | 5 | 2026-04-24 |
| [[com2us-platform]] | 컴투스플랫폼 (Com2usPlatform, c2spf) | organization | 컴투스플랫폼, c2spf, 게임플랫폼, BI, 블록체인 | 6 | 2026-04-24 |
| [[c2spf-analytics]] | c2spf 애널리틱스 (게임 데이터 BI) | service | analytics, c2spf, BI, 게임데이터, fastapi, react | 4 | 2026-04-24 |
| [[xpla-platform]] | XPLA 플랫폼 (블록체인 통합 서비스) | service | xpla, blockchain, nft, smart-contract, c2spf | 3 | 2026-04-24 |
| [[karpathy]] | Andrej Karpathy | person | karpathy, AI, llm, openai, tesla, 교육콘텐츠, nanogpt, nanochat | 3 | 2026-04-27 |
| [[autoresearch]] | autoresearch (karpathy/autoresearch) | project | autoresearch, llm, agent, 자율연구, val-bpb, 단일파일 | 1 | 2026-04-27 |
| [[nanogpt]] | nanoGPT (karpathy/nanoGPT) | project | nanogpt, gpt, llm, 교육코드, deprecated, 단일파일 | 1 | 2026-04-27 |
| [[nanochat]] | nanochat (karpathy/nanochat) | project | nanochat, llm, gpt2-speedrun, depth-dial, 풀파이프라인 | 1 | 2026-04-27 |
| [[microsoft]] | Microsoft | organization | microsoft, microsoft-cloud-advocates, microsoft-for-beginners, openai, azure, github, devrel | 5 | 2026-04-27 |
| [[microsoft-for-beginners]] | microsoft-for-beginners (시리즈) | project | microsoft-for-beginners, microsoft, curriculum, 무료교육, project-based-learning, co-op-translator | 5 | 2026-04-27 |

## 종합 분석 (Syntheses)

| 파일 | 제목 | 태그 | 최종 수정 |
|------|------|------|-----------|
| [[wiki-bootstrap-log]] | 위키 부트스트랩 기록 | 메타, 운영 | 2026-04-09 |
| [[career-timeline-seokgeun]] | 석근 커리어 타임라인 (2016-2026) | career, timeline, evolution | 2026-04-24 |
| [[agent-stack-evolution]] | 에이전트 스택의 3축 진화 — Microsoft · Anthropic · Karpathy 비교 | 비교분석, agent-stack, microsoft, anthropic, karpathy, harness, BI, 개인비서 | 2026-04-27 |
