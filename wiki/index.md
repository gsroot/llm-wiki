---
title: "위키 인덱스"
type: index
updated: 2026-04-28 (15회차)
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
<!-- 수집일 2026-04-27 (7회차): github/spec-kit 수집 — 소스 1 + 엔티티 2 (github, spec-kit) + 개념 1 (spec-driven-development) 추가, claude-code/agent-skills/harness/agent-patterns 4개 페이지 보강. SDD 메소드론 + Codex Skills 모드(agent-skills 표준 첫 외부 채택) + 메타-하네스 사례(autoresearch 최소 하네스의 반대 극단) -->
<!-- 수집일 2026-04-27 (8회차): pandas-dev/pandas 수집 — 소스 1 + 엔티티 2 (pandas, pandas-dev) 추가, data-pipeline-bigquery/ml-ai/microsoft-data-science-for-beginners 3개 페이지 보강. BDFL+Core Team+NumFOCUS 3축 거버넌스 + PDEP 시스템(11개) + 101개 공개 API + scale.rst 메모리 폭발 결정 트리 + bigframes/Pandera/Modin BI 직결 라이브러리. 거버넌스 모델이 spec-kit Constitution(GitHub 단독)과 anthropics-skills(Anthropic 단독 큐레이션)와 본질적으로 다른 4번째 거버넌스 축 -->
<!-- 수집일 2026-04-27 (9회차): fastapi/fastapi 수집 — 소스 1 + 엔티티 2 (fastapi, tiangolo) 추가, agent-skills/backend-python-fastapi 2개 페이지 보강. 결정적 발견: fastapi/.agents/skills/fastapi/SKILL.md (10.4KB + references/) 라이브러리 self-hosted Agent Skill — agent-skills 표준 외부 채택 3단계 진화 완성 (anthropics/skills 표준 → spec-kit Codex Skills 외부 도구 통합 → fastapi 라이브러리 self-hosted). README는 사람용·SKILL.md는 에이전트용이라는 OSS 분업이 메인스트림 라이브러리에서 명시화. Tiangolo 디폴트 스택(FastAPI/SQLModel/Asyncer/HTTPX/Typer/uv/Ruff/ty)이 SKILL.md로 명문화 → c2spf analytics-common-api 점검 기준점 -->
<!-- 수집일 2026-04-27 (10회차): astral-sh/uv 수집 — 소스 1 + 엔티티 2 (astral, uv) + 개념 1 (python-packaging) 추가. uv는 7개 기존 도구(pip·pip-tools·pipx·poetry·pyenv·twine·virtualenv) Rust 단일 바이너리 통합. universal lockfile + PubGrub resolver + PEP 723 인라인 의존성 + Cargo-style workspace. 듀얼 지침서 패턴 발견: CLAUDE.md(1줄) = `@AGENTS.md` import — Anthropic AGENTS.md 표준의 외부 산업 채택 4단계 진화(anthropics/skills → spec-kit → fastapi self-hosted SKILL.md → uv 단일 진실원). [[astral]] 회사 ruff·uv·ty 3제품 모두 "Rust 재구현형 통합" 패턴. 9회차 fastapi 디폴트 스택 (FastAPI/SQLModel/.../uv/Ruff/ty)이 본 회차 수집의 우(uv)와 ruff/ty까지 위키에 박힘 → c2spf-analytics uv 마이그레이션 ROI 분석 후속 후보 -->
<!-- 수집일 2026-04-27 (11회차): scikit-learn/scikit-learn 수집 — 소스 1 + 엔티티 1 (scikit-learn) 추가, ml-ai/microsoft-ml-for-beginners/harness 3개 페이지 보강. 19년 변하지 않은 5가지 API 컨트랙트(fit/predict/transform/Pipeline/Meta-estimator)가 입문자 교재부터 회사 BI까지 같은 코드 모양 가능케 한 핵심. SLEP(Scikit-Learn Enhancement Proposal) 거버넌스가 spec-kit Constitution(2025)·anthropics-skills SKILL.md(2025)·pandas PDEP(2022)의 19년 선배 — "표준화 → 구현" 분리 패턴의 원형. AGENTS.md(965 bytes) = 메이저 OSS 첫 명문화 AI 작성 코드 disclosure 강제. harness 개념에 제3축 "library-as-harness" 추가 — autoresearch 최소 / spec-kit 표준화 / scikit-learn 컨트랙트 영구성. 5단 영속성 의사결정 트리(ONNX/skops/joblib/표준직렬화/cloudpickle)가 회사 BI 모델 운영 SOP로 차용 가능. probabl.ai 풀타임 8명 + INRIA·Chanel·BNP·NVIDIA·Microsoft·Quansight·CZI 다층 후원이 19년 안정성의 비밀 -->


<!-- 수집일 2026-04-27 (12회차): flutter/flutter 수집 — 소스 1 + 엔티티 3 (flutter, dart, google) 추가, agent-skills/harness 2개 개념 + agent-stack-evolution 종합 분석 보강. Google 멀티플랫폼 UI SDK (★176K 11년차). 결정적 발견 2가지: (1) **agent-skills 표준의 vendor-neutral 채택** — `.agents/skills/` 3 SKILL.md (find-release/rebuilding-flutter-tool/upgrade-browser) + `.claude/skills` → `../.agents/skills` 심볼릭 링크 + agentskills.io 표준 명시 인용 + `dart_skills_lint` 자체 검증 도구. **표준 채택자가 정의자의 위치 컨벤션을 누른 첫 사례**. agent-skills 외부 채택 4단계 진화 완성: anthropics/skills(표준 정의) → spec-kit(메소드론 어댑터) → fastapi(라이브러리 self-hosted) → flutter(vendor-neutral asset). (2) **`docs/rules/` 4계층 토큰 예산 룰** — rules.md(30K) → 10k → 4k → 1k 동일 룰을 도구별 한계(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K) 매트릭스에 자동 매칭 — progressive disclosure를 토큰 단위로 더 세분화. agent-stack-evolution 3축 → 5축 확장 (Microsoft·Anthropic·Karpathy + GitHub spec-kit + Google flutter). Flutter Values 5개 + 차등 지원 4단계 모델 + agent-artifacts/ 격리 패턴은 위키 운영 차용 후보 -->

<!-- 점검 2026-04-27: lint 결과 후속 조치 — (1) 깨진 위키링크 7개 해소: 핵심 3개(copy-on-write/dataframe/prompt-cache) 페이지 신설 + 약어 4개(BDFL/NumFOCUS/PDEP/CMA) 일반 텍스트화. (2) 고아 페이지 career-timeline-seokgeun에 entities/seokgeun-kim.md 백링크 추가. (3) CLAUDE.md frontmatter 규칙을 타입별로 명확화 (source는 date_ingested 사용 명시). (4) obsidian-guide.md 표 안 예시 위키링크 백틱 처리. 위키 페이지 81 → 84개 -->
<!-- 점검 후속 2026-04-27: 이전 평가 우선순위 미완료 항목 반영 — agent-stack-evolution 중복 섹션 제거 및 제목 5축으로 정정, BDFL/NumFOCUS/PDEP/CMA 4개 페이지 신설, 모든 source 페이지에 raw_path 추가, source 템플릿/CLAUDE.md raw_path 규칙 반영. 위키 페이지 84 → 88개 -->
<!-- 수집일 2026-04-28 (13회차): openai/openai-cookbook 수집 — 소스 1 + 엔티티 2 (openai 조직 + openai-cookbook 프로젝트) 추가, agent-skills/harness/ml-ai/agent-patterns/agent-stack-evolution 5개 페이지 보강. ★73K 4년차 cookbook (289 콘텐츠 / 115명 저자 / MIT). 결정적 발견 2가지: (1) **AGENTS.md "Recent Learnings" 섹션 — 살아있는 운영 노트 패턴** = AGENTS.md 외부 채택 7단계 진화의 7번째이자 첫 살아있는 사례 (1~6번째 anthropics-skills/spec-kit/fastapi/uv/scikit-learn/flutter는 모두 정적 가이드, 7번째 OpenAI에서 처음으로 운영 중 발견을 즉시 반영). (2) **PLANS.md / ExecPlans = 6번째 거버넌스 축** — 단일 LLM 작업 7시간+를 가능케 하는 자기완결 living document. NON-NEGOTIABLE 5 요건(자기완결 / 살아있는 / 초보자 구현 / 관찰 가능한 동작 / 본문 용어 정의). [[harness]] 5축에 6번째로 추가, [[agent-stack-evolution]] 5축 → 6축 확장. 부수: registry.yaml 3,180줄 + authors.yaml 583줄 + check_notebooks.py 콘텐츠 거버넌스 자동화는 본 위키 index.md 자동 생성 PoC 후속 후보. 회사 BI 적용 가설: c2spf-analytics 분기/연간 대형 분석에 PLANS.md ExecPlan 패턴 적용 시 7시간+ 단일 작업 가능 -->

<!-- 수집일 2026-04-28 (15회차): 백엔드 코어 6개 신규 수집 (Ruff/Pydantic/SQLAlchemy/Alembic/PostgreSQL/Redis) — 소스 6 + 엔티티 6 + 종합 분석 1 (backend-fastapi-stack) 추가, fastapi/uv/astral 3개 엔티티 갱신. 결정적 발견 4가지: (1) **agent-skills 외부 채택 8단계 → 9번째 "회사 차원 표준화"** — astral-sh/ruff가 같은 회사 [[uv]] (10회차)와 동일한 `CLAUDE.md = @AGENTS.md` 1줄 import 패턴 채택 → 진정한 새 패턴은 "조직별 채택" → "조직 내 표준화" 진화. (2) **PEP 593 Annotated = 단일 타입 체인 사실상 표준** — Pydantic V2 / SQLAlchemy 2.0 / FastAPI DI가 같은 표현으로 통합 (Type-First Python Backend). (3) **PostgreSQL = 메일링 리스트 거버넌스 첫 사례 (6번째 모델)** — Pull Request 받지 않음, pgsql-hackers 메일링 + GitHub 미러 30년 보수파. (4) **Redis = MANIFESTO 철학 명문화 첫 사례 (7번째 모델)** — 10항목 ("DSL for Abstract Data Types" / "Memory storage is #1" / "We optimize for joy") + 2024 라이선스 변경 → Valkey fork. 단일 백엔드 도메인에 7개 거버넌스 모델 공존이 [[backend-fastapi-stack]]에 박힘 -->
<!-- 수집일 2026-04-28 (14회차): openai/openai-agents-python 수집 — 소스 1 + 엔티티 1 (openai-agents-python tool) 추가, openai 엔티티 + agent-skills/harness/agent-patterns/ml-ai 4개 개념 + agent-stack-evolution 종합 분석 보강 (총 6개 페이지 갱신). ★25K 1년차 OpenAI 공식 멀티 에이전트 Python SDK (v0.14.6 / MIT / 1년 14 메이저 버전). 13회차 cookbook과 한 쌍 — cookbook이 메소드론 정의 단(가이드)이라면 본 SDK는 같은 회사가 자기 핵심 SDK 본체에 동일 패턴을 풀스택 적용한 **거버넌스 자기 채택 (self-adoption)** 직접 증거. 결정적 발견 3가지: (1) **AGENTS.md = CLAUDE.md byte-for-byte 동기화 패턴 (12,900B 양쪽 미러링)** = agent-skills 외부 채택 **8단계 진화의 8번째 사례** (1~7번째 anthropics-skills/spec-kit/fastapi/uv/scikit-learn/flutter/openai-cookbook의 끝, 가장 단순한 vendor-neutral 적응). (2) **`.agents/skills/` 9개 운영 SOP 스킬 + 스킬 간 호출 (skill chaining)** — `$skill-name` 명령형 호출 + 트리거/스킵 조건 명시. flutter 3개의 3배 규모, **첫 "9개 본격 운영 SOP" 사례**. (3) **examples/agent_patterns/ 16개 .py = Anthropic 5패턴 + OpenAI 6확장 (Guardrails 3종 / Human-in-the-loop 3종 / Forced tool use) = 11종 reference 구현** — [[agent-patterns]]에 OpenAI 확장 6패턴 명시 추가. 부수: PLANS.md 5,485B (cookbook 16KB 응축) + .codex/hooks.json Stop 훅 자동화 + Public API Positional Compatibility 정책 (dataclass 필드 순서 호환성 계약 격상) + uv+ruff+pyright 도구 스택 + llms.txt 표준 채택. 회사 BI 적용 가설 강화: 9개 스킬 중 4개(`code-change-verification`/`docs-sync`/`runtime-behavior-probe`/`pr-draft-summary`)가 c2spf-analytics SOP에 직접 매핑, 13회차 PLANS.md 가설은 self-adoption 증거로 신뢰도 상승 -->


> 이 위키의 모든 페이지를 카테고리별로 정리한 카탈로그입니다.
> LLM은 질의 시 이 파일을 먼저 읽어서 관련 페이지를 찾습니다.

## 통계

- 총 페이지 수: 106
- 소스 요약: 39
- 엔티티: 41
- 개념: 21
- 종합 분석: 4

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

## 종합 분석 (Syntheses)

| 파일 | 제목 | 태그 | 최종 수정 |
|------|------|------|-----------|
| [[wiki-bootstrap-log]] | 위키 부트스트랩 기록 | 메타, 운영 | 2026-04-09 |
| [[career-timeline-seokgeun]] | 석근 커리어 타임라인 (2016-2026) | career, timeline, evolution | 2026-04-24 |
| [[agent-stack-evolution]] | 에이전트 스택의 6축 진화 — Microsoft · Anthropic · Karpathy · GitHub · Google · OpenAI 비교 | 비교분석, agent-stack, microsoft, anthropic, karpathy, github, google, openai, harness, BI, 개인비서, exec-plans, recent-learnings, self-adoption, 9-sop-skills, agents-md-claude-md-mirror | 2026-04-28 |
| [[backend-fastapi-stack]] | Python 백엔드 표준 스택 — FastAPI + Pydantic + SQLAlchemy + Alembic + PostgreSQL + Redis (Astral 도구 + 7개 거버넌스 모델 공존) | backend-stack, fastapi, pydantic, sqlalchemy, alembic, postgresql, redis, ruff, uv, ty, astral, type-first-python, annotated-pep-593, async-python, oltp, cache, governance-models, bdfl, mailing-list, manifesto, agent-skills, rust-extensions | 2026-04-28 |
