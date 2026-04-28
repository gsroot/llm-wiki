---
title: "활동 로그"
type: log
---

# 활동 로그

> 위키의 모든 활동(수집, 질의, 점검 등)을 시간순으로 기록합니다.
> 각 항목은 `## [날짜] 유형 | 제목` 형식을 따릅니다.

---

## [2026-04-28] ingest | Docker / GitHub Actions / Prometheus / Grafana / Sentry 5개 신규 수집 — 운영/Observability 5단 스택 (21회차 / Plan 19회차)

- **트리거**: `/Users/sgkim/.claude/plans/cozy-swinging-donut.md` Plan 19회차 — Operations/Observability 5개 OSS. 13~20회차 LLM/데이터 진영의 AGENTS.md 표준화를 발견한 후, 운영 진영도 동일한 패턴이 진행 중인지 검증하는 회차.

### 수집 대상 (5개)

- **Moby (Docker Engine 업스트림)** ([moby/moby](https://github.com/moby/moby)) — README 102줄 + CONTRIBUTING.md. Apache-2.0, 71.5K stars. Docker v29(2025-11)에서 `github.com/docker/docker` deprecated → `github.com/moby/moby/v2` 8년 분리 완성. AGENTS.md 미채택.
- **GitHub Actions** ([actions/runner](https://github.com/actions/runner) + [actions/toolkit](https://github.com/actions/toolkit)) — runner README 39줄 (.NET Core C#) + toolkit README 250줄 (TypeScript SDK). 분산 OSS 생태계. AGENTS.md 미채택.
- **Prometheus** ([prometheus/prometheus](https://github.com/prometheus/prometheus)) — README 229줄 + **AGENTS.md 148줄 (PR 패턴 가이드)**. Apache-2.0, 63.8K stars. CNCF graduated (2018, Kubernetes 다음 두 번째). DCO 강제.
- **Grafana** ([grafana/grafana](https://github.com/grafana/grafana)) — README 51줄 + **AGENTS.md 161줄 (계층화 + redirect, `<!-- version: 2.0.0 -->`)** + **CLAUDE.md = `@AGENTS.md` 1줄**. AGPL-3.0, 73.5K stars. 디렉토리별 AGENTS.md (docs/, alerting/).
- **Sentry** ([getsentry/sentry](https://github.com/getsentry/sentry)) — README 62줄 + **AGENTS.md 256줄 (8927B, 19회차 OSS 중 최장)** + **CLAUDE.md = `@AGENTS.md` 1줄**. BSL → Apache-2.0(3년), 43.7K stars. 4-tier 계층화 + "Do not add to CLAUDE.md or Cursor rules" 명문화.

### 결정적 발견 5가지

1. **agent-skills 11단계 진화 = 운영 진영 확산 + 4가지 새 변종 동시 등장**
   - 운영 진영 5개 중 3개(Prometheus/Grafana/Sentry) AGENTS.md 동시 채택 — LLM 프레임워크 진영을 넘어 운영 진영으로 표준 확산
   - 4가지 새 변종:
     - **PR-패턴 가이드** (Prometheus): "최근 merge된 PR로부터 maintainer 선호 패턴 추출" — 가장 데이터 기반, 가장 유지비 낮음
     - **`@AGENTS.md` redirect CLAUDE.md** (Grafana/Sentry): CLAUDE.md = 1줄로 축소 → SSOT 일원화
     - **계층화 AGENTS.md** (Grafana 2-tier, Sentry 4-tier): 모노레포 영역별 분산
     - **Anti-fragmentation 명문화** (Sentry): "Do not add to CLAUDE.md or Cursor rules" — AI agent별 룰 파일 drift 방지
   - 추가: **AGENTS.md 자체 버저닝** (Grafana `<!-- version: 2.0.0 -->`) 첫 도입

2. **AGENTS.md 양극화 (애플리케이션 vs 인프라)**
   - 채택: Prometheus / Grafana / Sentry (애플리케이션 코드에 가까운 운영 OSS)
   - 미채택: Docker/Moby / GitHub Actions (인프라 코어 OSS)
   - CI/CD 진영 전체(Jenkins/CircleCI/GitLab CI)도 미채택과 일치 → "상업/정치적 이유로 신중" 가설

3. **9번째 거버넌스 모델 = CNCF graduated**
   - Prometheus = CNCF 두 번째 졸업 프로젝트 (Kubernetes 다음, 2018)
   - 1~8 (Anthropic/OpenAI/Pydantic Foundation/Astral/커뮤니티/NumFOCUS/ASF PMC/LangChain Inc.) + 9 = 9개 거버넌스 모델 공존
   - 16회차 ASF PMC와 함께 vendor-neutral 재단 양대 산맥: ASF=데이터/JVM, CNCF=클라우드 네이티브 인프라/런타임
   - Linux Foundation 우산 아래 vendor-neutrality

4. **5단 흐름 = Docker → GHA → Prometheus → Grafana → Sentry**
   - 빌드 → CI/CD → 메트릭 → 시각화 → 에러 추적
   - `observability-and-cicd-stack.md` = 본 회차의 종합 산출 (5번째 종합 축: 15 backend / 16 dataframe / 17~18 agent / 19 observability)
   - 사이드 프로젝트 30분 부트스트랩: FastAPI에 prometheus-fastapi-instrumentator + sentry-sdk + Grafana Cloud 무료 티어
   - 5축 관측 데이터(metrics/logs/traces/errors/RUM) 중 3축 30분 만에 확보

5. **Sentry Feature Flag 5단계 + viewer_context contextvar — c2spf-analytics 직접 응용**
   - Feature Flag 5단계: register → Python check → Frontend check → Test → Rollout
   - "PR/commit/code 모두 anonymize" 룰 = PHI/PII 컴플라이언스 자동화 단서
   - viewer_context contextvar = FastAPI dependency injection 패턴과 결합 가능
   - `prek run -q` (pre-commit fork) = 단일 CLI lint/format/typecheck 통합

### 산출 페이지

- **소스 5개**: [[moby-moby]] / [[github-actions-docs]] / [[prometheus-prometheus]] / [[grafana-grafana]] / [[getsentry-sentry]]
- **엔티티 5개**: [[docker]] / [[github-actions]] / [[prometheus]] / [[grafana]] / [[sentry]]
- **개념 1개 신규**: [[observability]] — 5축 관측 데이터(metrics/logs/traces/errors/RUM) + AGENTS.md 양극화 분석
- **종합 1개**: [[observability-and-cicd-stack]] — 5단 흐름 + 11단계 진화 + 9번째 거버넌스 모델 + BI 적용 매핑
- **갱신 2개**: [[agent-skills]] (11단계 진화 추가, source_count 12→15) / [[devops-cicd]] (19회차 source 5개 + 종합 1개 추가, source_count 3→8)

### 통계 변화

- 페이지: 141 → 153 (+12: source +5 + entity +5 + concept +1 + synthesis +1)
- 소스: 53 → 58
- 엔티티: 55 → 60
- 개념: 22 → 23 (observability 신규)
- 종합: 9 → 10 (observability-and-cicd-stack 신규)

### 부수 발견

- Docker → Moby 분리(2017~2025)의 8년 여정 = OSS와 상업 분리 운영 케이스 스터디
- GHA OIDC 기반 클라우드 인증 (AWS STS / GCP Workload Identity) — 정적 credential 제거
- Grafana AGPL-3.0 라이선스 주의 — SaaS 제공 시 소스 공개 의무, Grafana Cloud는 다른 트랙
- Sentry BSL → Apache-2.0 (3년 후 자동 전환) 라이선스 트랙
- OpenTelemetry 통합 layer 가능성 — Prometheus/Grafana/Sentry 모두 OTLP 입력 지원

### 다음 단서

- **22회차 / Plan 20회차** — 프론트엔드 (Riverpod / Next.js / Tanstack Query / Zustand / Shadcn/ui)
- **23회차 / Plan 21회차** — 마무리 (seokgeun-stack-guide.md + 9단계 점검 워크플로우 + 최종 종합)
- 22회차 시점에 Docker/GHA AGENTS.md 재확인 (양극화 추적)
- 21회차 점검 시 "AGENTS.md 채택자별 fragmentation 룰 비교 매트릭스" 작성 (Sentry strict / Grafana silent / Pydantic AI byte-sync / Prometheus PR-only 4가지 모드)

---

## [2026-04-28] ingest | DeepAgents / CrewAI / PandasAI / Pydantic AI 4개 신규 수집 — LLM Agent Frameworks 확장 (20회차 / Plan 18회차)

- **트리거**: `/Users/sgkim/.claude/plans/cozy-swinging-donut.md` Plan 18회차 — LLM 에이전트 프레임워크 확장. 19회차 (Plan 17회차) LangGraph + OpenAI Agents SDK 비교를 6 프레임워크로 확장하여 agent-frameworks-matrix.md를 결정 가능한 도구로 격상.

### 수집 대상

- **DeepAgents** ([langchain-ai/deepagents](https://github.com/langchain-ai/deepagents)) — LangChain Inc.의 batteries-included agent harness. README 134줄 + AGENTS.md 364줄 (monorepo `libs/{deepagents, cli, evals}`). `create_deep_agent()` 한 줄 셋업, 4종 도구 빌트인 (planning + filesystem + shell + sub-agents). LangGraph compiled graph 반환 → durable execution 자동 상속. Deep Agents CLI는 Claude Code/Cursor 직접 경쟁.
- **CrewAI** ([crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)) — LangChain 명시적 독립 멀티 에이전트 프레임워크 (★50K, MIT). README 807줄. **"completely independent of LangChain or other agent frameworks"** README 첫 문장에 명시. Crews(role-playing) + Flows(enterprise event-driven) 듀얼 메타포. **Crew Control Plane SaaS** = 5번째 OSS+SaaS 듀얼 모델. 100,000+ 인증 개발자 학습 깔때기.
- **PandasAI** ([sinaptik-ai/pandas-ai](https://github.com/sinaptik-ai/pandas-ai)) — DataFrame 자연어 대화 어댑터 (★23.5K, MIT). README 203줄. `df.chat("질문")` 한 줄로 NL2DataFrame. LiteLLM 경유 다중 모델. Python 3.8~3.11만 지원 (보수적). AGENTS.md/CLAUDE.md 없음 — 18회차 6 OSS 동기화 그룹 미합류.
- **Pydantic AI** ([pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)) — Pydantic 팀이 직접 출시한 type-safe agent framework (★16.7K, MIT). README 220줄 + **AGENTS.md = CLAUDE.md byte-for-byte 10K 동기화** (6번째 동기화 사례). 11가지 자기 강점 (durable execution + graph support + YAML/JSON agent 정의 포함). 25개 provider model-agnostic. Capability 추상화 1급. A2A(Agent2Agent) 표준 첫 등장.

### 결정적 발견 5가지

1. **AGENTS.md=CLAUDE.md 동기화 6 OSS 표준화 = agent-skills 외부 채택 10단계 진화의 10번째**:
   - 18회차 추가: DeepAgents (AGENTS.md 364줄, monorepo guide) + Pydantic AI (10K byte-for-byte)
   - 합쳐서 6 OSS 동시 채택: LangChain / LangGraph / DeepAgents / FastMCP / OpenAI Agents Python / Pydantic AI
   - **CrewAI / PandasAI 미채택** = LangChain 진영 + OpenAI/Pydantic 진영 vs 독립 진영의 거버넌스 분기점 시사
   - 9단계 (3 OSS 동시) → 10단계 (6 OSS 표준화) — 이제 AGENTS.md=CLAUDE.md는 **LLM 프레임워크 OSS의 사실상 표준**

2. **5번째 OSS+SaaS 듀얼 모델 = Crew Control Plane**:
   - 기존: Polars/Polars Cloud, DuckDB/MotherDuck, LangChain/LangSmith, FastMCP/Prefect Horizon
   - 18회차 추가: CrewAI/Crew Control Plane (`app.crewai.com`), Pydantic AI/Pydantic Logfire (6번째)
   - **OSS+SaaS 듀얼은 이제 사실상 LLM 프레임워크 표준** — 6/8 프레임워크가 채택

3. **12번째 패턴(durable execution) 양강 구도**:
   - Pydantic AI README 11가지 강점 9번에서 durable execution 1급 명시 ("preserve their progress across transient API failures and application errors or restarts")
   - **이제 12번째 패턴은 [[langgraph]] 단독이 아닌 [[langgraph]] + [[pydantic-ai]] 양강**
   - DeepAgents는 LangGraph 위 프리셋으로 **12번째 패턴 자동 상속** → 채택 OSS 3개
   - 차별점: Pydantic AI는 type-safety ★★★ 압도적 + Graph Support 11번 강점 + YAML/JSON 정의

4. **YAML/JSON agent 정의 1급 = Pydantic AI 단독**:
   - 다른 5개 프레임워크 모두 코드 우선
   - Pydantic AI만 [agent-spec](https://ai.pydantic.dev/agent-spec) 1급 — "코드 없는 agent 정의" 가능
   - **agent-skills SKILL.md 패키징 사상의 다음 진화 방향** — agent를 SKILL.md처럼 packaging 가능

5. **CrewAI "학습 인증 → SaaS 깔때기"**:
   - 100,000+ 인증 개발자 (`learn.crewai.com`) → `app.crewai.com` 직결
   - 다른 프레임워크에 없는 비즈니스 모델 — LangChain Academy/Pydantic Academy도 코스 있으나 인증 규모 미공개

### 부수 발견

- **Capability vs Harness 추상화 비교**: Pydantic AI Capability (tools+hooks+instructions+settings 번들) > DeepAgents harness (도구 빌트인). Capability가 더 fine-grained.
- **A2A(Agent2Agent) 표준 첫 등장**: Pydantic AI가 README 7번 강점에서 명시 — agent 간 통신 표준
- **Pydantic 영향력 자기 명시**: README가 OpenAI SDK / Google ADK / Anthropic SDK / LangChain / LlamaIndex / AutoGPT / Transformers / CrewAI / Instructor 모두를 "validation layer derivative"로 호출 → "원천에서 직접 시작"

### 산출물

- 신규 raw: `raw/articles/{langchain-ai-deepagents,crewaiinc-crewai,sinaptik-ai-pandas-ai,pydantic-pydantic-ai}/`
- 신규 위키 페이지 8개:
  - `wiki/sources/{langchain-ai-deepagents,crewaiinc-crewai,sinaptik-ai-pandas-ai,pydantic-pydantic-ai}.md`
  - `wiki/entities/{deepagents,crewai,pandas-ai,pydantic-ai}.md`
- 갱신:
  - `wiki/syntheses/agent-frameworks-matrix.md` 6×N 확장 (4 → 6 프레임워크 + 2 직교 layer × ~22축 정량 비교 + 7-step 의사결정 트리 + 단계별 c2spf-analytics 마이그레이션 권장)
  - `wiki/entities/openai-agents-python.md` (18회차 형제 프레임워크 cross-link 5개)
  - `wiki/entities/pydantic.md` (Pydantic AI 연계 추가)
  - `wiki/concepts/agent-skills.md` (10단계 진화 사례 추가)
  - `wiki/concepts/agent-patterns.md` (12번째 패턴 양강 구도 추가)
  - `wiki/concepts/ml-ai.md` (4개 출처 추가)

### BI 적용 (석근님 c2spf-analytics)

- **Stage 1 (PoC, 1주)**: PandasAI + LiteLLM → `df.chat()` 한 줄로 BigQuery NL 결과 즉시 검증
- **Stage 2 (개발, 1개월)**: Pydantic AI + Logfire → BaseModel structured output, A2A로 다른 시스템 통신, durable 1급 → 운영 안정성
- **Stage 3 (운영, 분기)**: LangGraph + FastMCP + LangChain init_chat_model → checkpoint-postgres 영속성, MCP 도구, 모델 swap 실험

→ **각 단계별 권장 프레임워크가 다름** — 정답이 하나가 아닌 단계별 진화 모델

### 통계 변화

- 페이지: 132 → 141 (+9, source 4 + entity 4 + index/log 갱신 1)
- 소스: 49 → 53 (+4)
- 엔티티: 51 → 55 (+4)
- 종합 분석: 9 (변화 없음, agent-frameworks-matrix.md 확장만)

---

## [2026-04-28] ingest | LightGBM / LangChain / LangGraph / FastMCP 4개 신규 수집 — ML 클래식 + LLM 인프라 (19회차 / Plan 17회차)

- **트리거**: `/Users/sgkim/.claude/plans/cozy-swinging-donut.md` Plan 17회차 — ML 클래식 + LLM 인프라 (LightGBM / LangChain / LangGraph / FastMCP). 14회차 OpenAI Agents Python에서 발견된 패턴이 여러 OSS에 확산되었는지 검증 + LangGraph state machine 패턴이 [[agent-patterns]]에 추가될 가치 있는지 평가.
- **수집된 raw 폴더 4개**:
  - `raw/articles/microsoft-LightGBM/` — README + MAINTAINING.md + CONTRIBUTING.md (총 280줄)
  - `raw/articles/langchain-ai-langchain/` — README + AGENTS.md (376줄)
  - `raw/articles/langchain-ai-langgraph/` — README + AGENTS.md (139줄)
  - `raw/articles/jlowin-fastmcp/` — README + AGENTS.md (288줄)
- **생성된 파일 (9건)**:
  - sources 4개: `microsoft-lightgbm.md` / `langchain-ai-langchain.md` / `langchain-ai-langgraph.md` / `jlowin-fastmcp.md`
  - entities 4개: `lightgbm.md` / `langchain.md` / `langgraph.md` / `fastmcp.md`
  - synthesis 1개: `agent-frameworks-matrix.md` (1차, 18회차에 6×N 확장 예정)
- **업데이트된 파일 (4건)**:
  - `wiki/entities/scikit-learn.md` — sklearn vs LightGBM 보완 관계 표 추가, related에 [[lightgbm]]/[[pandas]]/[[polars]] 추가
  - `wiki/concepts/ml-ai.md` — source_count 7→11, "17회차 추가 — LLM 인프라 + 클래식 ML 보강" 섹션 신설, 4개 출처 추가
  - `wiki/concepts/agent-patterns.md` — source_count 4→5, "12번째 패턴: State-Machine + Durable Execution" 섹션 신설 (Anthropic 5 + OpenAI 6 + LangGraph 1)
  - `wiki/concepts/agent-skills.md` — source_count 8→11, "9단계 진화" 항목 추가 (LangChain/LangGraph/FastMCP 동시 채택 = 패턴 확산)
- **핵심 발견 5가지**:
  1. **agent-skills 9단계 진화 = "패턴 확산"** — LangChain/LangGraph/FastMCP 3개 OSS가 동시에 `AGENTS.md = CLAUDE.md` 동기화 채택. 1~7 단발 사례, 8 OpenAI byte-for-byte 미러링, 9 동시 채택. → **OpenAI 사내 패턴이 다국적 OSS 협업 컨벤션으로 격상**.
  2. **OSS 거버넌스 9번째 모델 = "회사 졸업 → 독립 조직"** — Microsoft/LightGBM → lightgbm-org/LightGBM (2026-03). 같은 메인테이너 유지 + GitHub org 이전. ASF PMC와 차이: 법적 형태 그대로 (ASF는 법인 이전).
  3. **OSS 거버넌스 모델 후보 — "공식 SDK 흡수 → 다음 버전 재시작"** — FastMCP 1.0이 2024 공식 MCP Python SDK에 통합 → 2.0 standalone 재출시. 일일 100만 다운로드, MCP 서버 70% 점유.
  4. **12번째 agent 패턴 = State-Machine + Durable Execution** — LangGraph가 Pregel + Apache Beam + NetworkX 학술 계보로 정립. checkpoint(Postgres/SQLite) 1급. Klarna/Replit/Elastic production 검증. Anthropic 5 + OpenAI 6 + LangGraph 1 = 12 패턴.
  5. **EffVer 발견** — LightGBM이 SemVer 대신 채택한 사용자 영향 중심 버전 체계 (jacobtomlinson.dev/effver). uv/ruff의 0.x 빠른 반복, pandas/sklearn의 SemVer 변형과 함께 버전 정책 다양화.
- **부수 발견**:
  - **Bot review 시대 메타-가이던스** — FastMCP AGENTS.md "Be constructively skeptical of bot review comments on your own PRs" — CodeRabbit/Codex/claude-bot 일상화 시대의 워크플로우 진화.
  - **OSS+SaaS 듀얼 패턴 4번째 사례 확정** — Polars/Polars Cloud, DuckDB/MotherDuck, LangChain/LangSmith, FastMCP/Prefect Horizon.
  - **"agent engineering platform" 슬로건** — LangChain이 2024-2025년 "framework for LLM apps"에서 "agent engineering platform"으로 재포지셔닝.
- **회사 BI 적용 (석근님 c2spf-analytics)**:
  - 게임 데이터 BI 챗봇 = **LangGraph state machine + FastMCP BI 도구 + LangChain 모델 추상화** 3-layer 권장. checkpoint-postgres로 대화 영속성, MCP로 BigQuery/Grafana 연결, init_chat_model로 OpenAI/Anthropic 동시 실험.
  - LightGBM은 churn/LTV/매출 예측 모델 1순위. sklearn Pipeline 통합 가능.
- **위키 통계 변화**: 123 → **132 페이지** (+9). 소스 45→49 (+4) / 엔티티 47→51 (+4) / 개념 22 (변경 없음, 갱신만) / 종합 8→9 (+1).
- **다음 회차 예정**: 18회차 LLM Agent Frameworks 확장 (DeepAgents / Crew AI / Pandas AI / Pydantic AI) → agent-frameworks-matrix.md 6×N 확장.

---

## [2026-04-28] ingest | mate-chat 프로젝트 위키 스냅샷 수집 — 프로젝트 전용 위키를 llm-wiki 원천 데이터로 편입 (18회차)

- **트리거**: 소유자 요청 — 현재 폴더 `llm-wiki`의 형제 폴더 `mate-chat/wiki`는 MateChat 프로젝트 전용 Obsidian/LLM 위키이므로, 그 데이터를 `llm-wiki` 원천 데이터로 가져와 수집.
- **판단**:
  - `mate-chat/wiki`는 프로젝트 전용 위키이고 `llm-wiki`는 개인 전체 위키이므로, 68개 페이지를 `llm-wiki`에 개별 페이지로 중복 생성하지 않음.
  - 대신 프로젝트 위키 전체를 날짜 스냅샷으로 `raw/`에 보관하고, `llm-wiki`에는 소스 요약 + MateChat 엔티티 보강 + 상위 종합 분석만 유지.
- **원천 스냅샷**:
  - `raw/notes/mate-chat-wiki-2026-04-28/`
  - `.obsidian/` 설정은 제외.
  - 보관 파일: 68개 마크다운 (`SCHEMA.md`, `index.md`, `log.md`, `sources/` 19개, `entities/` 22개, `concepts/` 22개, `synthesis/` 2개).
- **생성된 파일** (2건):
  - `wiki/sources/mate-chat-project-wiki-2026.md` — 프로젝트 위키 스냅샷 요약. 구조, 아키텍처, Hybrid AI Chat, Clover/IAP, 구현/출시 상태, 남은 과제, source conflict 기록.
  - `wiki/syntheses/matechat-project-knowledge-map.md` — MateChat 프로젝트 지식 지도. 프로젝트 위키와 개인 운영 프로필의 역할 분리, 핵심 시스템 노드, 다음 수집 우선순위 정리.
- **업데이트된 파일** (3건):
  - `wiki/entities/matechat.md` — source_count 4→5, 프로젝트 위키 스냅샷 섹션 추가, 출시 상태 기록 차이 명시.
  - `wiki/syntheses/seokgeun-operating-profile-2026.md` — sources에 프로젝트 위키 스냅샷 추가, 열린 질문에 출시 상태 차이 확인 항목 추가.
  - `wiki/index.md` — 18회차 표기, 통계 121→123 / 소스 44→45 / 종합 7→8, 신규 페이지 2건 등록.
- **핵심 발견**:
  - `mate-chat/wiki`는 구현/아키텍처/출시/운영 지식이 충분히 축적된 프로젝트 전용 지식 베이스다.
  - 프로젝트 위키는 v1.0.0 Google Play Store 출시 완료 및 운영 모드로 기록하지만, [[seokgeun-kim-profile-2026]]은 출시 직전 수준으로 기록한다. 최신 상태를 말할 때는 Play Console, 배포 태그, mate-chat 최신 문서로 확인 필요.
  - 프로젝트 위키 `index.md`는 Entities 21개로 표기하지만 실제 스냅샷 파일은 22개다. `clover-system.md` 추가 후 카운트만 덜 갱신된 상태로 보인다.
- **메모**: 이후 MateChat 관련 세부 구현 질문은 [[mate-chat-project-wiki-2026]]의 `raw_path` 아래 개별 프로젝트 위키 파일로 내려가고, 사업/육아휴직/AI 협업 맥락은 [[seokgeun-operating-profile-2026]]과 [[matechat-project-knowledge-map]]에서 본다.

---

## [2026-04-28] ingest | 석근 프로필 수집 — MateChat·육아휴직·AI 협업 운영 프로필 (17회차)

- **트리거**: 소유자 요청 — "마크다운 형태로 적은 내 프로필 정보"를 적절한 경로에 원본 파일로 만들고 수집.
- **소스**:
  - `raw/notes/personal/seokgeun-kim-profile-2026-04-28.md` — 개인 기본 정보, 가족, 커리어, MateChat 비전/사업화, 육아휴직 계획, 생산성/건강, 커뮤니케이션 취향, AI에게 기대하는 역할까지 포함한 2026년 개인 프로필 원문.
- **작업 방침**:
  - 원문에는 민감한 개인 식별 정보가 포함되어 있으므로 `raw/`에 보존.
  - 위키 페이지에는 정확한 주소·가족 세부 신상·출생 세부 정보 등을 반복하지 않고, 전략·운영·AI 협업에 필요한 구조화 정보만 반영.
- **생성된 파일** (3건):
  - `wiki/sources/seokgeun-kim-profile-2026.md` — 원문 소스 요약. MateChat 사업화, 육아휴직 운영, 커뮤니케이션 선호, 번아웃 리스크, AI 협업 기대를 요약.
  - `wiki/entities/matechat.md` — MateChat 프로젝트 엔티티. "대화의 시작은 AI, 끝은 사람" 포지셔닝, 기술 스택, KPI, 리스크, closed alpha 우선순위 정리.
  - `wiki/syntheses/seokgeun-operating-profile-2026.md` — 2026년 개인 운영 프로필 종합 분석. 가족 시간·경제적 독립·MateChat 검증·주 20~25시간 현실 예산·AI 협업 원칙 통합.
- **업데이트된 파일** (2건):
  - `wiki/entities/seokgeun-kim.md` — source_count 5→8, related에 MateChat/개인 운영 프로필 추가, 2026년 운영 키워드와 AI 협업 기대 반영.
  - `wiki/index.md` — 17회차 표기, 통계 118→121 / 소스 43→44 / 엔티티 46→47 / 종합 6→7, 신규 페이지 3건 등록.
- **핵심 판단**:
  - MateChat은 기능이 부족한 앱이라기보다 사용자 검증이 부족한 앱이다.
  - 2026년 육아휴직의 성공 기준은 "더 많이 개발"이 아니라, 작은 closed alpha로 실제 인간-인간 대화와 재방문/결제 가능성을 확인하는 것이다.
  - 번아웃은 개인 컨디션 문제가 아니라 MateChat 사업화의 직접 리스크다. 작업 계획은 주 20~25시간 기준으로 보수적으로 잡는 것이 안전하다.
- **메모**: 이 회차는 기존 커리어 중심 [[career-timeline-seokgeun]]에 이어, 석근의 2026-2027 개인 운영체계와 AI 협업 선호를 위키에 박은 첫 수집이다.

### 호칭 정정

- **후속 정정**: 원문에 들어간 "책임님" 호칭은 회사 직급 기반 AI 호칭 요청이 잘못 섞인 내용으로 확인됨.
- **수정**: 원문과 위키 요약을 "석근 프로필"로 정리하고, AI가 회사 직급 호칭보다 친구처럼 자연스럽게 "석근" 또는 이름으로 부르는 것을 선호한다고 명시.

---

## [2026-04-28] ingest | 데이터 레이어 5개 신규 수집 — Polars/DuckDB/PyArrow+Apache Arrow/Apache Kafka/Parquet (16회차)

- **트리거**: 15회차 종료 직후 사용자 "계속 진행해줘" → Auto Mode에서 16회차(데이터 레이어) 즉시 실행. 계획 `cozy-swinging-donut.md` 16회차 명세 그대로 진행.
- **소스** (4개 신규 raw 폴더, 약 21개 파일):
  - `raw/articles/pola-rs-polars/` (6개 파일) — README.md 160줄 (정체성 + 7대 핵심 특징 + 임포트 시간 70/104/520ms) / CONTRIBUTING.md / **lazy-api.md** ★ predicate/projection pushdown / **expressions-and-contexts.md** ★ 4 컨텍스트 / data-types-and-structures.md / streaming.md
  - `raw/articles/duckdb-duckdb/` (3개 파일) — README.md 51줄 (4축 정체성 + 파일=테이블 패러다임) / **CONTRIBUTING.md 132줄** ★ README보다 길다 (게이트키핑 진지함) / SECURITY.md
  - `raw/articles/apache-arrow/` (6개 파일) — apache/arrow README.md (5대 컴포넌트 + 11+ 언어 매트릭스) / format-README.rst / **Schema.fbs 571줄** ★ FlatBuffers 자료형 명세 / **parquet-README.md 284줄** ★ Dremel + 4계층 구조 / **parquet-Encodings.md 393줄** ★ 8개+ 인코딩 / parquet-CHANGES.md
  - `raw/articles/apache-kafka/` (4개 파일) — README.md 362줄 / **design.md 511줄** ★ 분산 시스템 설계 교과서 (Don't fear the filesystem! / pagecache 위임 / O(1) Persistent Queue / sendfile / Message Set / End-to-end Compression) / design-index.md / docs-index.md
- **작업**: 4개 GitHub 저장소(pola-rs/polars, duckdb/duckdb, apache/arrow + apache/parquet-format 통합, apache/kafka) raw 수집 + 위키 페이지 12종 신규 + 2종 갱신.
- **생성된 파일** (12건):
  - `wiki/sources/pola-rs-polars.md` — Polars 소스 요약 (쿼리 엔진 정체성 + lazy + immutable)
  - `wiki/sources/duckdb-duckdb.md` — DuckDB 소스 요약 (SQLite for OLAP + Lakehouse Lite)
  - `wiki/sources/apache-arrow.md` — Arrow + Parquet 통합 소스 요약 (메모리 = 디스크 표준)
  - `wiki/sources/apache-kafka.md` — Kafka 소스 요약 (design.md = 분산 시스템 교과서)
  - `wiki/entities/polars.md` — Polars tool 엔티티 (Eager + Lazy + Streaming 3중 모드)
  - `wiki/entities/duckdb.md` — DuckDB tool 엔티티 (OLAP × Embedded 사분면)
  - `wiki/entities/pyarrow.md` — PyArrow tool 엔티티 (3개 DataFrame 라이브러리 공통 다리)
  - `wiki/entities/kafka.md` — Apache Kafka tool 엔티티 (6대 핵심 설계 결정)
  - `wiki/entities/parquet.md` — Apache Parquet tool 엔티티 (4계층 + 8 인코딩 + Dremel)
  - `wiki/concepts/lazy-evaluation.md` — Lazy Evaluation 개념 (Polars/DuckDB/Spark 공통 패턴)
  - `wiki/syntheses/dataframe-ecosystem-evolution.md` — DataFrame 18년 진화사 (4단계 + ASF PMC 8번째 거버넌스 + Kafka 사상 일반화)
  - `wiki/syntheses/pandas-vs-polars-vs-duckdb.md` — 정량 비교 매트릭스 (PDS-H 벤치마크 + 의사결정 트리 + 마이그레이션 ROI)
- **업데이트된 파일** (2건):
  - `wiki/entities/pandas.md` — related +[[polars]]/[[duckdb]]/[[pyarrow]]/[[parquet]]/[[lazy-evaluation]] (5개 추가), updated 2026-04-27→2026-04-28. "자매 도구 비교" 섹션 추가 (pandas/polars/duckdb 6축 비교)
  - `wiki/concepts/copy-on-write.md` — related +[[polars]]/[[apache-arrow]]/[[lazy-evaluation]] (3개 추가), source_count 1→2, "CoW vs Immutable-by-Default 비교" 섹션 추가, 열린 질문 "다른 데이터프레임 라이브러리 메모리 모델"에 답 박힘 (Polars=immutable, Dask=chunked CoW)
- **거버넌스 모델 8번째 발견 — ASF PMC**:
  | # | 모델 | 사례 | 특징 |
  |---|------|------|------|
  | 1 | BDFL | python, pandas (초기) | 단일 결정자 |
  | 2 | BDFL + Core Team | pandas (현재) | 위임 구조 |
  | 3 | Core Team + PEP | python | 절차적 의사결정 |
  | 4 | 회사 + OSS | fastapi, pydantic (Pydantic Inc) | 창립자 회사 + OSS 본체 |
  | 5 | VC-backed 회사 | astral (uv/ruff/ty) | 기업 통합 |
  | 6 | 메일링 리스트 | postgresql | PR 받지 않음, 30년 |
  | 7 | 라이센스 변경 | redis (2024 SSPL) | OSS → 유사 OSS |
  | 8 | **ASF PMC** | **arrow, kafka, parquet** | **재단 + PMC + Apache Way** |
- **메타 발견 5가지**:
  1. **"메모리 표준 = 디스크 표준" 통합**: Apache Arrow + Parquet 단일 자료형 모델 → 변환 비용 0 → pandas/Polars/DuckDB zero-copy 교환 → GB/s IO 처리량
  2. **CoW vs Immutable의 정반대 답**: pandas는 모델 유지 + 명확화, Polars/Arrow는 모델 자체 교체. PDEP-10 통과 시 둘이 수렴
  3. **"디스크는 친구" Kafka 사상의 일반화**: design.md 511줄이 데이터 인프라 전체에 영향. PostgreSQL WAL / Kafka Topic / Redis AOF / Parquet column chunk / DuckDB mmap / Polars streaming 모두 sequential I/O + pagecache 위임
  4. **"쿼리 엔진" 정체성 부상**: Polars + DuckDB 동시 자기 정의 → DataFrame ↔ SQL 경계 무너짐. 둘 다 옵티마이저 + 벡터화 + Arrow 위에 빌드
  5. **단일 노드 한계 = 4.2B 행**: Polars bigidx, pandas 64bit, DuckDB in-process 모두 2^32에서 한계. 그 너머는 분산 (Spark/Dask)
- **회사 BI 적용 가설** ([[c2spf-analytics]]):
  - **권장 스택**: pandas (ML 출력만) + Polars (메인 변환, lazy + streaming) + DuckDB (SQL 탐색, BQ 비용 절감)
  - **마이그레이션 ROI**: cold start 520ms → 70ms · 200GB+ 일일 로그 streaming 가능 · BQ 슬롯 -30% 추정
  - **마이그레이션 비용**: ~3-4주 (1인 풀타임, 학습 + 변환 + 검증 + 배포)
  - **Risk**: Polars DSL ≠ pandas (학습), Plotly/Geopandas 일부 pandas-only (변환 레이어)
- **위키 통계**: 106 → **118** 페이지 (소스 39→43, 엔티티 41→46, 개념 21→22, 종합 4→6)
- **메모**: PEP 723 + uv run 패턴이 데이터 레이어에서도 작동 — 단일 파일 분석 스크립트의 표준화 가능성. 다음 17회차는 ML 클래식 + LLM 인프라 (LightGBM/LangChain/LangGraph/FastMCP) → Polars/Pandas와의 통합 패턴 검토 예정.

---

## [2026-04-28] ingest | 백엔드 코어 6개 신규 수집 — Ruff/Pydantic/SQLAlchemy/Alembic/PostgreSQL/Redis (15회차)

- **트리거**: 소유자 요청 — "다음 기술 스택에 대해 원천 데이터를 추출하고 수집해서 위키를 더 풍부하게 만드려고 하는데 그렇게 하기 위한 계획을 세워줘. 백엔드: UV, Ruff, FastAPI, Pydantic, SQLAlchemy, Alembic, PostgreSQL, Redis [데이터/ML/LLM/운영/프론트 32개 추가]" → 6회차 분할 (15~21회차) 표준 깊이 계획 수립 → Auto Mode 승인 → 15회차 백엔드 코어 즉시 실행.
- **소스** (6개 신규 raw 폴더, 약 712KB 보관):
  - `raw/articles/astral-sh-ruff/` (12개 파일, 232KB) — README.md 39KB / **AGENTS.md 4.2KB** ★ 14항목 개발 가이드라인 + ty mdtest + Salsa incrementality / **CLAUDE.md 12B = `@AGENTS.md`** ★ uv 10회차 패턴 답습 / Cargo.toml / pyproject.toml / mkdocs.yml / docs (configuration / linter / formatter / preview)
  - `raw/articles/pydantic-pydantic/` (10개 파일, 168KB) — README.md / **HISTORY** / **docs_why.md** / **docs_migration.md** / **docs_version-policy.md** ★ 명시 버전 정책 / pyproject.toml / mkdocs.yml / CITATION.cff
  - `raw/articles/sqlalchemy-sqlalchemy/` (12개 파일, 148KB) — README.rst 4.5KB / README.dialects.rst / pyproject.toml / AUTHORS / CHANGES / docs (index / intro / contents / glossary / faq / tutorial)
  - `raw/articles/sqlalchemy-alembic/` (10개 파일, 232KB) — README.rst 4KB / pyproject.toml / docs (index / tutorial / **autogenerate** ★ / **branches** / **cookbook** / batch / **offline** ★ / ops)
  - `raw/articles/postgres-postgres/` (6개 파일, 24KB) — README.md / COPYRIGHT / HISTORY / doc_TODO / doc_MISSING_FEATURES / doc_KNOWN_BUGS (GitHub 미러 한계로 양적 적음)
  - `raw/articles/redis-redis/` (6개 파일, 68KB) — README.md 39KB / **MANIFESTO 6.9KB** ★ 10항목 철학 / CONTRIBUTING.md / RELEASENOTES / SECURITY.md / TLS.md
- **작업**: 6개 GitHub 저장소 메타데이터 + README + AGENTS.md/MANIFESTO/핵심 docs 1차 수집. 본 회차 **3개 결정적 발견 + 1개 단일 타입 체인 패턴**으로 위키의 백엔드 도메인이 풀스택으로 박힘.
- **생성된 파일** (13건):
  - `wiki/sources/astral-sh-ruff.md` — Ruff 소스 요약 (Astral 회사 차원 표준화 발견)
  - `wiki/sources/pydantic-pydantic.md` — Pydantic 소스 요약 (V2 ground-up + Annotated)
  - `wiki/sources/sqlalchemy-sqlalchemy.md` — SQLAlchemy 소스 요약 (Core/ORM 이중 + 21년 BDFL)
  - `wiki/sources/sqlalchemy-alembic.md` — Alembic 소스 요약 (autogenerate + Offline Mode)
  - `wiki/sources/postgres-postgres.md` — PostgreSQL 소스 요약 (메일링 리스트 거버넌스)
  - `wiki/sources/redis-redis.md` — Redis 소스 요약 (MANIFESTO 10항목)
  - `wiki/entities/ruff.md` — Ruff tool 엔티티 (8개 주요 특징)
  - `wiki/entities/pydantic.md` — Pydantic tool 엔티티 (8개 주요 특징, 자매 제품 일체화)
  - `wiki/entities/sqlalchemy.md` — SQLAlchemy tool 엔티티 (8개 주요 특징)
  - `wiki/entities/alembic.md` — Alembic tool 엔티티 (7개 주요 특징)
  - `wiki/entities/postgresql.md` — PostgreSQL tool 엔티티 (8개 주요 특징, 첫 메일링 거버넌스)
  - `wiki/entities/redis.md` — Redis tool 엔티티 (8개 주요 특징, 첫 MANIFESTO/라이선스 변경)
  - `wiki/syntheses/backend-fastapi-stack.md` — Python 백엔드 표준 스택 종합 분석 (9개 단락 / 7개 거버넌스 모델 / Annotated 통합 / Rust 가속 / 결정 트리)
- **업데이트된 파일** (4건):
  - `wiki/entities/fastapi.md` — related +[[pydantic]]/[[sqlalchemy]]/[[postgresql]]/[[ruff]]/[[uv]] (5개 추가), updated 2026-04-27→2026-04-28. 메모 섹션에 15회차 백엔드 의존성 통합 단락 추가
  - `wiki/entities/uv.md` — related +[[ruff]]/[[fastapi]]/[[pydantic]] (3개 추가), updated 2026-04-27→2026-04-28
  - `wiki/entities/astral.md` — related +[[ruff]]/[[fastapi]]/[[pydantic]] (3개 추가), source_count 1→2 (astral-sh-ruff 출처 추가), updated 2026-04-27→2026-04-28
  - `wiki/index.md` — 15회차 표기, 통계 93/33/35/21/3 → 106/39/41/21/4, 신규 13페이지 등록 (소스 6 + 엔티티 6 + 종합 1), 갱신 2개 페이지 source_count·tags·updated 동기화 (fastapi/astral), 헤더 코멘트 15회차 추가 (4개 결정적 발견 명시)
- **결정적 발견 4가지**:
  1. **agent-skills 외부 채택 8단계 → 9번째 "회사 차원 표준화"** — astral-sh/ruff의 `CLAUDE.md = @AGENTS.md` 12바이트 1줄이 같은 회사 [[uv]] (10회차 발견)와 정확히 동일. 즉 새 패턴이 아닌 **같은 회사의 또 다른 제품**. 진정한 새 패턴은 "조직 외부 채택" → "조직 내 표준화"로 한 단계 진화. Astral의 uv·ruff·ty 3제품 모두 같은 컨벤션 채택. 향후 회차에서 같은 회사 여러 제품 수집 시 (Pydantic 진영 / OpenAI / Google 등) 추가 검증 가설.
  2. **PEP 593 Annotated = 단일 타입 체인 사실상 표준** — Pydantic V2 (`Annotated[float, Gt(0)]`) / SQLAlchemy 2.0 (`Mapped[int] = mapped_column(...)`) / FastAPI DI (`Annotated[AsyncSession, Depends(get_db)]`)가 **같은 표현으로 통합**. SQLModel (Tiangolo)이 한 클래스로 합성. **Type-First Python Backend**의 결정적 패턴.
  3. **PostgreSQL = 메일링 리스트 거버넌스 첫 사례 (위키 6번째 거버넌스 모델)** — Pull Request 받지 않음, 패치는 pgsql-hackers 메일링 리스트 + .patch 파일 첨부. GitHub은 단순 미러 (공식 명시). 30년 보수파 거버넌스와 agent-skills 모던파의 **정반대 극단**. 회사 BI 도구 선택 시 **거버넌스 모델 매칭** 추가 변수.
  4. **Redis = MANIFESTO 철학 명문화 첫 사례 (위키 7번째 거버넌스 모델)** — 10항목 ("DSL for Abstract Data Types" / "Memory storage is #1" / "Single-threaded core" / "Code is like a poem" / "Against complexity" / "We optimize for joy" / "Two levels of API" / "Opportunistic programming") + 2024 라이선스 변경 (BSD 3-Clause → RSAL/SSPL dual) → **AWS fork Valkey 출시**. 8번째 거버넌스 모델 = "라이선스 변경 + Fork 사례" 추가 박힘.
- **단일 백엔드 도메인에 7개 거버넌스 모델 공존** — BDFL (fastapi/pydantic/sqlalchemy/alembic) / 회사 차원 표준화 (Astral) / 표준+구현 분리 (anthropics-skills) / 명시 버전 정책 (Pydantic V2) / 메일링 리스트 보수파 (PostgreSQL ★) / MANIFESTO 철학 명문화 (Redis ★) / 라이선스 변경+Fork (Redis 2024 ★).
- **회사 BI 적용 가설** (3건, [[backend-fastapi-stack]]에 통합):
  - **c2spf-analytics ruff/uv 마이그레이션** — pylint+black+isort 분리 → ruff 통합으로 CI 53s → 3s (15~20x 단축)
  - **pgvector로 위키 RAG 자체 구현** — 본 위키 (~106 페이지) PostgreSQL + pgvector 적재 → 별도 벡터 DB 회피
  - **Alembic Offline Mode = c2spf-platform 결제 DB 마이그레이션 표준** — DBA 권한 분리 환경 자동화
- **메모**: 15회차는 백엔드 코어 6개 + 기존 fastapi/uv 종합으로 위키 첫 풀스택 도메인 종합 페이지 [[backend-fastapi-stack]] 산출. 16회차 (데이터 레이어: Polars/DuckDB/PyArrow/Parquet/Kafka)에서 Pandas와 묶이며 비교 매트릭스 페이지 신설 예정. 21회차 마무리에서 [[seokgeun-stack-guide]] (석근님 개인 스택 통합 가이드) 산출 예정. 본 회차 4개 결정적 패턴이 다음 회차 데이터/LLM/운영/프론트에서 반복 검증될지 추적.

---

## [2026-04-28] ingest | openai/openai-agents-python — OpenAI Agents SDK 본체 + AGENTS.md=CLAUDE.md 동기화 + 9개 운영 SOP 스킬 (14회차)

- **트리거**: 소유자 요청 — "https://github.com/openai/openai-agents-python 의 내용을 살펴보고 이 프로젝트의 적절한 경로에 원본 자료를 넣어두고 수집을 진행해줘."
- **소스**: `raw/articles/openai-openai-agents-python/` (36개 파일, 약 250KB 보관)
  - 루트 메타 9종: `README.md` (6.0KB), `AGENTS.md` (12.9KB ★ 9개 스킬 + ExecPlan + Public API Positional 정책), `CLAUDE.md` (12.9KB ← AGENTS.md와 byte-for-byte 동일), `PLANS.md` (5.5KB ★ NON-NEGOTIABLE 4 + Skeleton), `LICENSE` (MIT), `Makefile` (1.8KB), `pyproject.toml` (5.7KB), `pyrightconfig.json` (469B, mypy 아닌 pyright), `mkdocs.yml` (15.4KB)
  - `docs/` 14개 핵심 문서: agents.md (16.9KB), tools.md (37.9KB ★ 가장 큼), running_agents.md (27.1KB), mcp.md (18.8KB), index.md, quickstart.md, handoffs.md, guardrails.md, tracing.md, context.md, multi_agent.md, sandbox_agents.md, llms.txt (6.8KB ★ llms.txt 표준 채택)
  - `.codex/` (Codex CLI 통합): config.toml (codex_hooks=true), hooks.json (Stop 훅 → uv run python stop_repo_tidy.py)
  - `.agents-skills/` 9개 SKILL.md (통합 46.3KB): runtime-behavior-probe (13.4KB ★ 가장 큼) / final-release-review (8.0KB) / pr-draft-summary (5.7KB) / implementation-strategy (4.5KB) / docs-sync (4.3KB) / examples-auto-run (3.2KB) / test-coverage-improver (2.7KB) / code-change-verification (2.5KB) / openai-knowledge (1.9KB)
  - `examples-readmes/agent_patterns_README.md` (4.5KB) + `src_agents__init__.py` (15KB, public surface)
  - **제외**: `examples/agent_patterns/` 16개 .py 본체 (매핑 표만 보관), `tests/`, `docs/scripts/`, `site/`, 9개 스킬 각각의 `agents/`·`scripts/`·`references/` 서브디렉토리, `uv.lock` (831KB), `src/agents/` 본체 (`run_state.py` 129KB / `run.py` 92KB / `tool.py` 72KB / `agent.py` 42KB 등 50+ 파일)
- **작업**: openai/openai-agents-python GitHub 저장소 (2025-03-11 창설, MIT, Python, ★25,440 / fork 3,883 / pushedAt 2026-04-27, PyPI 패키지 `openai-agents` v0.14.6 — 1년 사이 14 메이저 버전, 28.7MB 저장소) 통합 수집. openai.github.io/openai-agents-python/ 공식 문서. raw 경로: 기존 `<org>-<repo>` 컨벤션 따라 `raw/articles/openai-openai-agents-python/` 채택.
- **생성된 파일** (2건):
  - `wiki/sources/openai-openai-agents-python.md` — 소스 요약 (메타 / raw 파일 구조 / 7개 핵심 내용 단락 / 7개 인사이트 / 5개 인용 / 10개 후속 탐구 / 3개 회사 BI 적용 가설 / 메모)
  - `wiki/entities/openai-agents-python.md` — openai-agents-python tool 엔티티 (8개 주요 특징 / 관련 개념·엔티티 / 메모 + 다음 수집 후보)
- **업데이트된 파일** (7건):
  - `wiki/entities/openai.md` — source_count 1→2, tags +openai-agents-python/openai-agents, related +[[openai-agents-python]]/[[agent-patterns]], updated 2026-04-27→2026-04-28. 출처에 [[openai-openai-agents-python]] 추가 (cookbook 메소드론 정의 단 ↔ 본 SDK 본체 단 self-adoption 직접 증거). 후속 수집 후보 4번을 "수집 완료(14회차) → [[openai-agents-python]]"로 갱신
  - `wiki/concepts/agent-skills.md` — source_count 7→8, tags +openai-agents-python/9-sop-skills/skill-chaining/agents-md-claude-md-mirror, related +[[openai-agents-python]]. **8단계 진화 도식 완성** ([[openai-openai-agents-python]] 8번째 사례로 출처 섹션 추가) — anthropics-skills(1) → spec-kit(2) → fastapi(3) → uv(4) → scikit-learn(5) → flutter(6) → openai-cookbook(7, 살아있는 운영 노트) → openai-agents-python(8, **9개 본격 운영 SOP + AGENTS.md=CLAUDE.md 미러링 + 스킬 체이닝**)
  - `wiki/concepts/harness.md` — source_count 7→8, tags +openai-agents-python/9-sop-skills/skill-chaining, related +[[openai-agents-python]]. **5축 PLANS.md를 본체 단 풀스택 적용** 사례로 출처 섹션 추가 — 메소드론 정의자가 자기 본체에 동일 패턴을 풀스택 채택 (PLANS.md 5,485B + AGENTS.md ExecPlan 자동 호출 + .codex/hooks.json + 9개 운영 SOP 스킬). 회사 BI 적용 가설 보강
  - `wiki/concepts/agent-patterns.md` — source_count 3→4, tags +openai-agents-python/guardrails/human-in-the-loop/forced-tool-use/11-patterns, related +[[openai-agents-python]]. **Anthropic 5패턴 + OpenAI 6확장 = 11종 reference 구현** 사례 출처 섹션 추가 — Anthropic 5(deterministic/routing/parallelization/agents_as_tools 4종/llm_as_a_judge) + OpenAI 6확장(Guardrails 3종 + Human-in-the-loop 3종 + Forced tool use). 회사 BI 응용 가설 (Guardrails는 BigQuery 비용 검증, HITL은 BI 승인 워크플로우)
  - `wiki/concepts/ml-ai.md` — source_count 6→7, tags +openai-agents-python/multi-agent-framework/guardrails/human-in-the-loop, related +[[openai-agents-python]]. 출처에 [[openai-openai-agents-python]] 추가 (회사 BI에 LLM 에이전트 적용 시 1차 후보 SDK)
  - `wiki/syntheses/agent-stack-evolution.md` — sources +[[openai-openai-agents-python]], tags +self-adoption/9-sop-skills/agents-md-claude-md-mirror. **6축 표 OpenAI 행 보강** ("openai-cookbook + openai-agents-python" 묶음으로 가이드 단 + 본체 단 명시), "OpenAI agents-python (6번째 축 보강, 14회차)" 단락 신설 (4중 풀스택 채택 사례), "### 소스 (13)" → "(14)" + 출처 리스트에 [[openai-openai-agents-python]] 1행 추가 (메소드론 ↔ 본체 한 묶음 self-adoption 본체 적용 단)
  - `wiki/index.md` — 14회차 표기, 통계 91/32/34/21/3 → 93/33/35/21/3, 신규 2페이지 등록 (소스 1 + 엔티티 1), 갱신 5개 페이지 source_count·tags 동기화 (openai/agent-skills/harness/agent-patterns/ml-ai), agent-stack-evolution 행 태그 보강, 헤더 코멘트 14회차 추가
- **결정적 발견 3가지**:
  1. **AGENTS.md = CLAUDE.md byte-for-byte 동기화 패턴** — 12,900B 양쪽 미러링이 [[uv]]의 `@AGENTS.md` import (1줄)와 [[flutter]]의 `.agents/` 심볼릭 링크의 중간 형태. **agent-skills 외부 채택 8단계 진화의 8번째 사례** (1~7번째 anthropics-skills/spec-kit/fastapi/uv/scikit-learn/flutter/openai-cookbook의 끝, 가장 단순한 vendor-neutral 적응). Claude Code/Codex/vendor-neutral 도구 어느 쪽이든 100% 동일 정보 보장.
  2. **`.agents/skills/` 9개 운영 SOP 스킬 + 스킬 간 호출 (skill chaining)** — `code-change-verification` / `openai-knowledge` / `implementation-strategy` / `pr-draft-summary` / `runtime-behavior-probe` (13.4KB ★) / `docs-sync` / `examples-auto-run` / `final-release-review` / `test-coverage-improver`. AGENTS.md "Mandatory Skill Usage" 섹션이 각 스킬을 `$skill-name` 명령형으로 호출 + 트리거/스킵 조건 명시 + 스킬 간 체이닝(예: `$implementation-strategy`가 내부에서 `$final-release-review/scripts/find_latest_release_tag.sh` 호출). flutter 3개의 3배 규모, **첫 "9개 본격 운영 SOP" 사례** — 실무 운영 워크플로우 전체를 SKILL.md로 풀스택 명문화.
  3. **examples/agent_patterns/ 16개 .py = Anthropic 5패턴 + OpenAI 6확장 = 11종 reference 구현** — Anthropic 5: deterministic(prompt-chaining)/routing/parallelization/agents_as_tools 4종(orchestrator-workers + 변형)/llm_as_a_judge(evaluator-optimizer). OpenAI 6확장: Guardrails 3종(input/output/streaming, tripwire 메커니즘) + Human-in-the-loop 3종(승인/거절/스트림, RunState 일시정지·재개) + Forced tool use(tool_choice 강제). cookbook의 sample 노트북과 달리 SDK 본체와 한 묶음으로 박혀 **API 안정성 보장된 reference 구현**. [[agent-patterns]]에 OpenAI 확장 6패턴 명시 추가.
- **부수 발견**:
  - **PLANS.md 5,485B** — cookbook `articles/codex_exec_plans.md` (16KB)를 본 SDK 운영용으로 응축. 같은 NON-NEGOTIABLE 4 + Living Sections 4 + 단일 fenced code block 강제. AGENTS.md "ExecPlans" 섹션이 자동 호출.
  - **`.codex/hooks.json` Stop 훅 자동화** — `uv run python "$(git rev-parse --show-toplevel)/.codex/hooks/stop_repo_tidy.py"`. Codex가 자체 SDK 개발 운영에 사용되는 첫 명시 사례.
  - **Public API Positional Compatibility** — dataclass 필드 순서를 호환성 계약으로 격상한 첫 명시 사례. `RunConfig`/`FunctionTool`/`AgentHookContext`. 1년 14 메이저 버전(약 26일에 1 버전) 빠른 반복을 가능케 하는 호환성 boundary.
  - **uv + ruff + pyright 도구 스택** — uv.lock 831KB, Makefile 모든 명령이 `uv` 기반 (`uv sync`/`uv run`). pyright (mypy 아님). [[fastapi]] 디폴트 스택과 동일 방향.
  - **`docs/llms.txt` (6.8KB) + `docs/llms-full.txt` (15KB)** — llms.txt 표준 채택 (llmstxt.org). MkDocs 사람용 사이트와 LLM용 색인 양쪽 운영.
  - **RunState `CURRENT_SCHEMA_VERSION` + `SCHEMA_VERSION_SUMMARIES`** — 직렬화 스키마 버전 관리. AGENTS.md가 변경 시 두 상수 동시 갱신 의무화.
- **회사 BI 적용 가설 (3건)**:
  - **9개 스킬 중 4개를 c2spf-analytics에 차용**: `$code-change-verification`(BigQuery SQL 변경 시 dbt test+pytest+linter 자동), `$docs-sync`(대시보드 변경 시 README/Confluence 자동 갱신), `$runtime-behavior-probe`(BigQuery 쿼리 배포 전 dry-run+EXPLAIN+샘플 검증 매트릭스), `$pr-draft-summary`(BI PR 작성 시 결과 메트릭 변화 자동 요약). 도입 ROI: PR 작성·코드 검증·문서 동기화 시간 50%↓ 추정.
  - **PLANS.md ExecPlan을 분기 대형 분석에 적용 (cookbook 13회차 가설 보강)**: 13회차 가설이 OpenAI 자체 SDK self-adoption 증거(본 회차)로 신뢰도 상승. c2spf-analytics 분기 코호트 분석 1건에 ExecPlan 양식 적용 PoC.
  - **API Positional Compatibility를 Analytics API에 적용**: c2spf-analytics가 외부에 노출하는 dataclass·Pydantic 모델 필드 순서를 release 이후 호환성 계약으로 명시. 게임 데이터 BI 외부 소비자 보호 + 빠른 반복 양립.
- **메모**: 본 회차는 13회차 [[openai-openai-cookbook]]의 후속이자 한 쌍. cookbook이 "OpenAI는 살아있는 운영 노트 + PLANS.md 메소드론 도입"이라고 박았다면, 본 회차는 **그 정의자가 자기 핵심 SDK 본체에 풀스택 적용한 직접 증거**. 두 회차로 OpenAI의 거버넌스 통합이 명확해짐 — (가이드 단) cookbook + (본체 단) agents-python의 한 묶음 거버넌스. 같은 [[agent-stack-evolution]] 종합 분석을 4번째(spec-kit), 5번째(flutter), 6번째(openai-cookbook), 6번째 보강(agents-python) 4회 연속 갱신 — 위키 내 같은 종합 페이지 단기 반복 확장의 두 번째 사례. 다음 회차 후보: [[anthropics-claude-cookbooks]] 14 디렉토리 본체 단독 (Claude SDK 측 reference) / 9개 sub-agent prompts 단독 수집 / openai/agents.md 표준 자체 / agentskills.io 표준 정의자 본체.

---

## [2026-04-28] ingest | openai/openai-cookbook — OpenAI API 4년차 cookbook + 살아있는 AGENTS.md (13회차)

- **트리거**: 소유자 요청 — "https://github.com/openai/openai-cookbook 의 내용을 살펴보고 이 프로젝트의 적절한 경로에 원본 자료를 넣어두고 수집을 진행해줘."
- **소스**: `raw/articles/openai-openai-cookbook/` (11개 파일, 약 100KB 보관)
  - 루트 메타 7종: `README.md` (1.2KB), `AGENTS.md` (5.5KB ★ Recent Learnings 섹션 포함), `CONTRIBUTING.md` (425B), `LICENSE` (MIT), `authors.yaml` (19.9KB / 115명), `registry.yaml` (78.7KB / 289 콘텐츠), `.gitignore` (2KB)
  - `articles/` 7편: `chatgpt-agents-sales-meeting-prep.md` (14KB, 2026-04-22 최신 ChatGPT Workspace Agents), `codex_exec_plans.md` (16KB ★ PLANS.md 메소드론), `how_to_work_with_large_language_models.md` (8KB, LLM 입문서 4 모드), `openai-harmony.md` (29KB, gpt-oss 5 roles + 3 channels), `related_resources.md` (9KB, LangChain/LlamaIndex/Outlines 등 외부 큐레이션), `techniques_to_improve_reliability.md` (42KB, CoT/Self-consistency/Tree of Thoughts), `what_makes_documentation_good.md` (9KB ★ 위키 운영 차용 가치)
  - **제외**: `examples/` 243개 ipynb 본체 (수십 MB, 메소드론·거버넌스 자료에 집중), `images/`, `.github/`
- **작업**: openai/openai-cookbook GitHub 저장소(2022-03-11 창설, MIT, 주 언어 Jupyter Notebook, ★73,042 / fork 12,325 / pushedAt 2026-04-26) 통합 수집. cookbook.openai.com 정적 사이트 source. raw 경로 결정: 기존 `<org>-<repo>` 컨벤션 따라 `raw/articles/openai-openai-cookbook/` 채택.
- **생성된 파일** (3건):
  - `wiki/sources/openai-openai-cookbook.md` — 소스 요약 (메타 / 7개 핵심 내용 단락 / 7개 인사이트 / AGENTS.md 7단계 진화 도식 / 인용 5개 / 후속 탐구 10건 / 회사 BI 적용 가설 2건)
  - `wiki/entities/openai.md` — OpenAI organization 엔티티 (LLM 라인업 / API/SDK / 거버넌스 패턴 3축 / Anthropic 비교 표)
  - `wiki/entities/openai-cookbook.md` — openai-cookbook project 엔티티 (콘텐츠 구조 / 거버넌스 3축 / 4년 진화 태그 분포 / articles 7편)
- **업데이트된 파일** (5건):
  - `wiki/concepts/agent-skills.md` — source_count 6→7, tags +openai/openai-cookbook/agents-md-living/recent-learnings/exec-plans, related +[[openai]]/[[openai-cookbook]]. **출처 섹션에 [[openai-openai-cookbook]] 7번째 사례로 박음 — agent-skills 외부 채택 7단계 진화 완성** (1~6번째 anthropics-skills/spec-kit/fastapi/uv/scikit-learn/flutter는 모두 정적 가이드, 7번째 OpenAI에서 처음으로 살아있는 운영 노트 모드)
  - `wiki/concepts/harness.md` — source_count 6→7, tags +openai/openai-cookbook/plans-md/exec-plans/living-document/7-hour-task, related +[[openai]]/[[openai-cookbook]]. **신규 "제5의 축 — PLANS.md / ExecPlans" 섹션 신설** (5축 비교 표 — autoresearch/spec-kit/scikit-learn/flutter/openai-cookbook). 출처에 [[openai-openai-cookbook]] 5축 사례로 추가
  - `wiki/concepts/ml-ai.md` — source_count 5→6, tags +openai-cookbook/embeddings/agents-sdk/prompt-caching/gpt-5/gpt-oss, related +[[openai]]/[[openai-cookbook]]. LLM 시대 단락에 **"OpenAI Cookbook 사례 검색"** 항목 추가 (회사 BI 의사결정 워크플로우 명문화). 출처에 [[openai-openai-cookbook]] 추가
  - `wiki/concepts/agent-patterns.md` — source_count 2→3, tags +openai/openai-cookbook/agents-sdk/exec-plans, related +[[openai]]/[[openai-cookbook]]. 출처에 [[openai-openai-cookbook]] **Anthropic 5 패턴의 OpenAI 측 reference 구현** 사례 (parallel_agents.ipynb / evaluate_agents.ipynb / multi-agent-portfolio-collaboration / orchestrating_agents.ipynb 매핑) + PLANS.md = 6번째 거버넌스 패턴 명시
  - `wiki/syntheses/agent-stack-evolution.md` — **5축 → 6축 확장**. title `"5축 진화 — Microsoft · Anthropic · Karpathy · GitHub · Google 비교"` → `"6축 진화 — Microsoft · Anthropic · Karpathy · GitHub · Google · OpenAI 비교"`. tags +github/google/openai/exec-plans/plans-md/recent-learnings/agents-md-living, sources +[[github-spec-kit]]/[[flutter-flutter]]/[[openai-openai-cookbook]] (4축·5축 후속 추가에서 본문 인용은 됐으나 frontmatter 미반영 일괄 정합). updated 2026-04-27→2026-04-28. 본문: 5축 표 → 6축 표 확장 (OpenAI 행 추가), "4·5축 추가의 의미" → "4·5·6축 추가의 의미"로 갱신, 결론 갱신("정적 가이드 5 사례 vs 살아있는 운영 노트 1 사례 갈림" + "시간 기반 검증의 등장" + 회사 BI 도입 가이드 보강 3건). 출처 소스(10→13)·엔티티(7→13) 표 확장
  - `wiki/index.md` — 13회차 표기, 통계 88/31/32/21/3 → 91/32/34/21/3, 신규 3페이지 등록 (소스 1 + 엔티티 2), 갱신 4개 페이지 source_count·tags 동기화 (agent-skills/harness/ml-ai/agent-patterns), agent-stack-evolution 행 제목 6축으로 갱신, 헤더 코멘트 13회차 추가
- **결정적 발견 2가지**:
  1. **AGENTS.md 외부 채택 7단계 진화의 7번째 단계 — 첫 살아있는 사례**. 1~6번째 모두 정적 가이드(SKILL.md 패키지 / SLEP / Constitution / rules.md / .agents 자산)였으나, OpenAI는 `AGENTS.md` 안에 `Recent Learnings` 섹션을 두어 운영 중 발견을 즉시 누적 ("현상 → 대응 → 이유" 6개 항목). 변경 비용 0의 살아있는 작업기억 모드. Anthropic 진영도 같은 방향으로 따라올 가능성 신호.
  2. **PLANS.md / ExecPlans = 6번째 거버넌스 축**. 단일 LLM 작업 7시간+를 가능케 하는 자기완결 living document. NON-NEGOTIABLE 5 요건 + 단일 fenced code block 형식 강제. autoresearch(분~시간) / spec-kit(시간~일) / scikit-learn(19년) / flutter(11년) / anthropics-skills(단발) 5축에 시간 기반 검증의 6번째 축 추가.
- **회사 BI 적용 가설** (3건):
  - **PLANS.md 도입 PoC**: c2spf-analytics 분기/연간 대형 분석(예: 게임 출시 전후 코호트 분석)에 ExecPlan 패턴 적용. 단일 분석가 + LLM 협업으로 7시간+ 작업 수행 가능. NON-NEGOTIABLE "관찰 가능한 동작" = BI 대시보드/보고서 산출물 매핑.
  - **AGENTS.md "Recent Learnings" 본 위키 차용**: `wiki/AGENTS.md` 또는 CLAUDE.md에 Recent Learnings 섹션 신설. 13회차 누적 운영 메타 메모.
  - **registry.yaml 차용**: `wiki/registry.yaml` 신설 후 `wiki/index.md` 자동 생성 PoC. `python .github/scripts/check_notebooks.py` 패턴을 `lint` 워크플로우에 차용 (등록 누락 자동 검출).
- **메모**: 13회차에서 위키가 박은 결정적 발견 2가지가 [[agent-stack-evolution]] 종합 분석을 5축에서 6축으로 확장시킴 — 같은 종합 분석 페이지를 4번째(spec-kit), 5번째(flutter), 6번째(openai-cookbook) 회차에서 연속 갱신. 7번째 축 후보: Cursor/Cline IDE-에이전트, OpenAI Custom GPTs/AssistantsAPI, Microsoft Foundry. 다음 회차 후보로 [[anthropics-claude-cookbooks]] 14 디렉토리 본체 단독 수집 또는 OpenAI agents.md 별도 표준 저장소 수집(7번째 축 정의자 본체 1차 자료) 가능. 본 회차 raw 보관 100KB 가벼움 — examples/ 본체 cherry-pick은 회사 BI 적용 시점에 별도 회차로 분리.

---

## [2026-04-27] lint-followup | 평가 우선순위 미완료 항목 반영 — 4개 페이지 신설 + raw_path 추적성 보강

- **트리거**: 소유자 요청 — "지금 로컬에 변경사항들이 있는데 확인해보고 너가 말한 우선순위에서 아직 진행되지 않은 부분들은 진행해줘."
- **로컬 변경 확인**:
  - 이미 반영됨: `copy-on-write` / `dataframe` / `prompt-cache` 3개 개념 페이지, `career-timeline-seokgeun` 역링크, source frontmatter 규칙 명확화, obsidian 예시 링크 처리.
  - 미완료로 확인됨: `agent-stack-evolution.md` 중복 섹션, `BDFL`/`NumFOCUS`/`PDEP`/`Claude Managed Agents` 페이지 신설, source 원본 경로 일관 기록.
- **후속 수정**:
  - `wiki/syntheses/agent-stack-evolution.md` — 중복된 "스냅샷 이후 — 4축·5축 확장 노트" 섹션 제거, 제목을 3축에서 5축으로 정정.
  - 신규 페이지 4건:
    - `wiki/concepts/bdfl.md`
    - `wiki/concepts/pdep.md`
    - `wiki/entities/numfocus.md`
    - `wiki/entities/claude-managed-agents.md`
  - 관련 문서 재연결: `pandas.md`, `pandas-dev.md`, `pandas-dev-pandas.md`, `anthropic.md`, `claude-agent-sdk.md`, `anthropics-claude-cookbooks.md`, `scikit-learn.md`, `data-pipeline-bigquery.md`.
  - `templates/source.md`와 `CLAUDE.md`에 `raw_path` 필드 추가.
  - `wiki/sources/*.md` 31개 전부에 로컬 원본 `raw_path` 추가.
- **인덱스/통계 갱신**:
  - `wiki/index.md` — 통계 88/31/32/21/3으로 갱신, 신규 4페이지 등록, `agent-stack-evolution` 제목 갱신.
- **검증**:
  - 깨진 위키링크(코드블록/inline-code 제외): 0건
  - source `raw_path` 누락/존재 오류: 0건
  - 인덱스 미등록/파일 없음: 0건
  - 프론트매터 필수 필드 누락: 0건
  - `git diff --check`: 통과

---

## [2026-04-27] lint | 위키 전체 점검 — 깨진 링크 해소 + 스키마 명확화 + 신규 개념 3종

- **트리거**: 소유자 요청 — "llm-wiki 가 전체적으로 깨지거나 이상이 있는 부분이 혹시 있는지 확인해주고, obsidian에서 잘 활용될 수 있는 상태인지, 혹시 필요한 작업이 있을지 검토해줘."
- **점검 결과 (자동 분석)**:
  - 위키링크 무결성: 깨진 링크 16건 → 실질 누락 7건 + 코드 예시 9건(코드블록 안전)
  - 인덱스 ↔ 파일 동기화: 누락/미등록 0건 ✓
  - 프론트매터 type 일관성: entity/concept/source/synthesis 분류 정확 ✓
  - 고아 페이지: 1건 (career-timeline-seokgeun)
  - 스키마 드리프트: CLAUDE.md "필수 필드: created/updated"가 source 31개 실제 사용 패턴(`date_ingested`)과 불일치
- **P0 즉시 수정**:
  - `wiki/sources/obsidian-guide.md:86` — 표 안 예시 위키링크를 inline code로 처리
  - `wiki/entities/seokgeun-kim.md` — "종합 분석" 섹션 신설 + `[[career-timeline-seokgeun]]` 백링크 (고아 페이지 해소)
- **P1 스키마 명확화**:
  - `CLAUDE.md` 프론트매터 규칙 갱신 — 공통 필수(`title`/`type`/`tags`) + 타입별 필수 필드 명세 (entity/concept = `created`+`updated`, source = `date_ingested`, synthesis = `created`+`updated`). source가 `date_ingested`로 시간 추적함을 명시.
- **P2 옵션 B (선택적 페이지화)**:
  - **신규 페이지 3건 (개념적 깊이 있는 보편 추상)**:
    - `wiki/concepts/copy-on-write.md` — pandas 2.0 PDEP-7 메모리 모델, OS/FS/VCS 등 보편 적용
    - `wiki/concepts/dataframe.md` — pandas/Polars/Dask/Ibis 공통 추상, R `data.frame`에서 시작된 계보
    - `wiki/concepts/prompt-cache.md` — Anthropic 5분 TTL · prefix-based · 90% 비용 절감, 에이전트 경제성 핵심
  - **약어 4종 일반 텍스트화 (단일 컨텍스트, ROI 낮음)**:
    - `BDFL` (Benevolent Dictator For Life) — `pandas-dev.md`
    - `NumFOCUS` — `pandas.md`, `pandas-dev.md` (frontmatter related + 본문 + 관련 개념)
    - `PDEP` (Pandas Enhancement Proposal) — `pandas.md`, `pandas-dev.md`
    - `Claude Managed Agents` — `claude-agent-sdk.md`
- **검증**: 깨진 링크 16 → 9 (남은 9건 모두 코드블록 안 의도된 예시), 페이지 81 → 84
- **인덱스/통계 갱신**: `wiki/index.md` — frontmatter `(12회차 + 점검)`, 통계 84/31/30/19/3, 개념 표에 copy-on-write/dataframe/prompt-cache 3행 추가, 점검 코멘트 헤더 추가
- **다음 점검 후보**:
  - `career-timeline-seokgeun`을 `c2spf-analytics`/`com2us-platform` 등 업무 엔티티에서도 백링크 (현재 `seokgeun-kim`만 연결)
  - source 31개의 `date_ingested` 형식 일관성 (날짜만? 회차 표기?) 정형화
  - `templates/lesson.md` 등록 후 사용 사례 추적

---

## [2026-04-27] ingest | flutter/flutter — Google 멀티플랫폼 UI SDK + vendor-neutral .agents/ 표준 (12회차)

- **소스**: `raw/articles/flutter-flutter/` (28개 파일 보관)
  - 루트 6종: `README.md` (7KB), `CONTRIBUTING.md` (13KB), `CODE_OF_CONDUCT.md` (2.9KB), `CHANGELOG.md` (105KB), `LICENSE` (BSD-3, 1.5KB), `pubspec.yaml` (6.2KB)
  - `.agents/` 5종: `dart-editing.md` (309B, `trigger: always_on`), `skills/README.md` (3.8KB, agentskills.io 표준 인용 + 5 채택 요건), `skill-find-release.md` (2.1KB), `skill-rebuilding-flutter-tool.md` (792B), `skill-upgrade-browser.md` (4.3KB)
  - `docs/about/` 5종: `Values.md` (6.7KB, 5 가치 + 4단 지원 모델), `Repository-architecture.md` (2.5KB), `Glossary.md` (6.2KB), `Framework-architecture.md` (468B), `Engine-architecture.md` (17.7KB)
  - `docs/contributing/` 2종: `Design-Documents.md` (6.8KB), `Tree-hygiene.md` (38KB, PR 절차 풀파이프라인)
  - `docs/rules/` 5종: `README.md` (2.3KB, 도구별 한계 매트릭스), `rules-1k.md` (799B), `rules-4k.md` (3.5KB), `rules-10k.md` (9.4KB), `rules-full.md` (30.7KB)
  - `docs/` 2종: `README.md` (2.7KB, contributor wiki entry), `Self-Service-Index.md` (9.1KB)
  - `.gemini/` 2종: `config.yaml` (785B), `styleguide.md` (6.9KB)
  - `agent-artifacts/` 2종: `.gitignore` (25B), `README.md` (227B)
  - **제외**: `engine/` C++ 소스, `packages/` Dart 소스, `examples/` 앱, `third_party/` 의존성 (메타·거버넌스 자료가 위키 관심사)
- **작업**: flutter/flutter 공식 GitHub 저장소 수집. ★176,117 / fork 30,289 / open issues 12,587 (2026-04-27 기준), BSD-3-Clause, 2015-03-06 창설 11년차, 440MB 저장소. raw 경로: 기존 `<org>-<repo>` 컨벤션 따라 `raw/articles/flutter-flutter/` (org=repo 두 번째 사례, scikit-learn-scikit-learn 패턴 자연 확장).
- **생성된 파일**:
  - `wiki/sources/flutter-flutter.md` — 소스 요약 (저장소 핵심 디렉토리 표 + 4기둥 기술 스택 + 5 Values + 4단 지원 모델 + .agents/ vendor-neutral 채택 + 토큰 예산 4계층 + agent-artifacts 격리 + Contributing design doc 절차 + 7개 인사이트 + 위키 갱신 포인트 + 6 활용 시나리오 + 7개 인용)
  - `wiki/entities/flutter.md` — Flutter framework/tool 엔티티 (Skia/Impeller, Material/Cupertino, hot reload, .agents/ 채택, docs/rules 4계층)
  - `wiki/entities/dart.md` — Dart language 엔티티 (4-target compile AOT/JIT/JS/WASM, sound null safety, Isolates, dart_format/analyze)
  - `wiki/entities/google.md` — Google organization 엔티티 (Microsoft·Anthropic·GitHub와 균형, Gemini/Antigravity/Skia/Android/GCP)
- **업데이트된 파일**:
  - `wiki/concepts/agent-skills.md` — source_count 5→6, tags에 vendor-neutral/dart-skills-lint/flutter/token-budget-tiers 추가, related에 [[flutter]]/[[google]] 추가, 출처에 **flutter-flutter를 외부 채택 4단계 진화 4번째 사례**로 박음 ("표준 채택자가 정의자의 위치 컨벤션을 누른 첫 사례")
  - `wiki/concepts/harness.md` — source_count 6→7, tags에 flutter/vendor-neutral/token-budget-tiers 추가, related에 [[flutter]]/[[google]] 추가, **"제4의 축 — vendor-neutral 자산 + 토큰 예산 다층화"** 섹션 신설 (4축 비교 표), 출처에 [[flutter-flutter]] 4번째 축으로 추가
  - `wiki/syntheses/agent-stack-evolution.md` — tags에 github/spec-kit/google/flutter/vendor-neutral 추가, sources에 [[github-spec-kit]]/[[flutter-flutter]] 추가, **"스냅샷 이후 — 4축·5축 확장 노트"** 섹션 신설 (3축 → 5축 진화, GitHub spec-kit + Google Flutter 추가, 결론 갱신)
  - `wiki/index.md` — 12회차 표기, 통계 77/30/27/16/3 → 81/31/30/16/3, 신규 4 페이지 등록 (flutter-flutter source + flutter/dart/google entity), harness/agent-skills 행 source_count·tags 동기화
- **메모**: 12회차 핵심 발견 2가지가 위키에 큰 변화를 박음. (1) **agent-skills 외부 채택 4단계 진화 완성** — anthropics/skills(표준 정의 2025) → github-spec-kit Codex(메소드론 → 다중 어댑터, 2025) → fastapi(라이브러리 self-hosted, 2025) → **flutter(거대 OSS의 vendor-neutral asset, 2025)**. 마지막 단계가 "표준 채택자가 정의자를 누른" 첫 사례 — `.agents/skills`가 `.claude/skills`를 누르고, 후자가 전자로 심볼릭 링크. (2) **토큰 예산 4계층(rules_1k/4k/10k/full)이 AI 도구 시장 매트릭스에 자동 매칭** — Antigravity 12K/OpenAI 1.5K/CodeRabbit 1K/Copilot 4K. 거대 OSS가 다중 AI 도구 환경을 운영하는 첫 표준 사례. agent-stack-evolution 페이지가 3축에서 5축으로 확장(Microsoft·Anthropic·Karpathy + GitHub·Google) — 같은 스냅샷을 한 회차 안에 5번이나 갱신해야 했던 회차. 후속 탐구 후보: (a) `dart_skills_lint` 소스 1회독으로 마크다운 lint 패턴 추출 → 위키 자체 .agents/skills/lint 도구 구축, (b) Flutter `docs/rules/` 4계층을 위키 CLAUDE.md 4계층화로 직접 차용 (CLAUDE_1k.md/4k.md/10k.md), (c) Flutter `agent-artifacts/` 격리 패턴을 위키 `wiki/.agent-artifacts/`로 차용 (LLM 임시 분석 격리), (d) 개인 비서 AI 모바일 앱 PoC — Flutter + FastAPI 스택으로 회사 BI(React) 외 다른 길 형성.

---

## [2026-04-27] ingest | scikit-learn/scikit-learn — Python ML 사실상 표준 라이브러리 (11회차)

- **소스**: `raw/articles/scikit-learn-scikit-learn/` (20개 파일 보관)
  - 루트 7종: `README.rst` (215줄), `AGENTS.md` (24줄, AI disclosure 강제), `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, `CITATION.cff`, `COPYING` (BSD-3)
  - `doc/` 13종: `governance.rst` (10.6KB, SLEP+TC+4팀), `roadmap.rst` (8.8KB, 18 항목), `faq.rst` (28.4KB, scope 잠금 명시), `getting_started.rst` (10.6KB, fit/predict 입문), `related_projects.rst` (15.3KB, 30+ 호환 라이브러리), `common_pitfalls.rst` (25.1KB, data leakage 방지), `machine_learning_map.rst` (2.4KB), `model_persistence.rst` (18.5KB, 5단 의사결정 트리), `metadata_routing.rst` (15.8KB, 1.3+ 신규 API), `about.rst` (16.5KB, 다층 자금 + GSoC 기원), `install.rst` (14.2KB), `maintainers.rst` (현재 19명), `presentations.rst`
  - **제외**: `sklearn/` 핵심 코드, `glossary.rst` (94KB, 너무 큼), `examples/` (notebook 다수)
- **작업**: scikit-learn 공식 GitHub 저장소 수집. ★65,932 / fork 26,974 / open issues 2,048 (2026-04-27 기준), BSD-3-Clause, 2007 GSoC 시작 / 2010-02-01 v0.1 / 약 3개월 릴리스 주기 / DOI 보유. raw 경로 결정: 기존 `<org>-<repo>` 컨벤션 따라 `raw/articles/scikit-learn-scikit-learn/` (org=repo 첫 사례, [[pandas-dev-pandas]] 패턴의 자연스러운 확장).
- **생성된 파일**:
  - `wiki/sources/scikit-learn-scikit-learn.md` — 소스 요약 (5가지 API 컨트랙트, SLEP 거버넌스 4 룰, 다층 자금 모델, 2018 Roadmap 9년 후 평가, model_persistence 5단 의사결정, AGENTS.md 메이저 OSS 첫 사례, 30+ 호환 생태계, 석근 BI 적용 6가지). 파일명은 wikilink 충돌 회피 위해 entity와 분리.
  - `wiki/entities/scikit-learn.md` — sklearn tool 엔티티 (5+1 API 컨트랙트, 의도적 범위 잠금, SLEP 4가지 룰, 5단 영속성 의사결정, 회사 BI 적용 후보)
- **업데이트된 파일**:
  - `wiki/concepts/ml-ai.md` — source_count 4→5, tags에 sklearn/slep/fit-predict 추가, related에 [[scikit-learn]] 추가, 본문에 "scikit-learn 직접 사용 가능성" 단락 신설(GCP AutoML 대안 검토), 출처에 [[scikit-learn-scikit-learn]] 추가. (병렬로 진행된 pandas 수집과 충돌 없이 통합)
  - `wiki/concepts/harness.md` — source_count 5→6, tags에 library-as-harness/scikit-learn/slep 추가, **"제3의 축 — 라이브러리 자체가 하네스"** 신설 (autoresearch 최소 / spec-kit 표준화 / scikit-learn 컨트랙트 영구성 — 5축 비교표). 출처에 [[scikit-learn]] 추가
  - `wiki/sources/microsoft-ml-for-beginners.md` — 관련 엔티티/개념에 [[scikit-learn]] 한 줄 추가 (26 lesson 전체가 sklearn API 컨트랙트에 의존)
  - `wiki/index.md` — 11회차 표기, 통계 75/29/26/16/3 → 77/30/27/16/3, 신규 2 페이지 등록 + harness/ml-ai 행 source_count·tags 동기화
- **메모**: 11회차에서 위키가 두 가지 뼈대를 동시에 박음 — (1) **표준화 분리 패턴 4번째 사례** ([[anthropics-skills]] SKILL.md 2025 / [[github-spec-kit]] Constitution 2025 / [[pandas-dev-pandas]] PDEP 2022 / **[[scikit-learn]] SLEP 2007**), (2) **"라이브러리가 하네스" 제3축**으로 [[harness]] 개념 양극이 3축으로 확장. AGENTS.md 패턴은 [[fastapi-fastapi]] (라이브러리 self-hosted SKILL.md), [[astral-sh-uv]] (single source of truth), **[[scikit-learn]] (AI disclosure 강제)** 3 단계 OSS 진화. 후속 탐구 후보: (a) SLEP 별도 repo 수집 → 4축 거버넌스 종합 분석 (BDFL+PDEP / TC+SLEP / Anthropic 큐레이션 / GitHub Constitution), (b) `model_persistence.rst` 5단 트리를 c2spf BI 모델 운영 SOP로 차용 PoC, (c) AGENTS.md 패턴을 트래블메이트/Mate Chat OSS 공개 시 차용.

---

## [2026-04-27] ingest | astral-sh/uv — Rust 단일 바이너리 Python 도구체인 통합 (10회차)

- **소스**: `raw/articles/astral-sh-uv/` (37개 파일, 416KB 보관)
  - 루트 메타 9종: `README.md` (329줄), `AGENTS.md` (20줄, single source of truth), `CLAUDE.md` (1줄, `@AGENTS.md` import만), `CHANGELOG.md` (742줄, v0.5.0~v0.11.8), `CONTRIBUTING.md` (356줄), `BENCHMARKS.md` (117줄), `STYLE.md` (134줄), `SECURITY.md` (15줄), `pyproject.toml` (115줄), `mkdocs.yml` (278줄)
  - `docs/index.md` + `docs/getting-started/` 3종 (`installation.md`, `features.md`, `help.md`)
  - `docs/concepts/` 8종 (`build-backend`, `cache`, `configuration-files`, `indexes`, `preview`, `python-versions` 498줄, `resolution` 856줄, `tools`)
  - `docs/concepts/projects/` 10종 (`build`, `config` 619줄, `dependencies` 967줄, `export`, `index`, `init`, `layout`, `run`, `sync`, `workspaces`)
  - `docs/guides/` 5종 (`install-python`, `package`, `projects`, `scripts`, `tools`)
  - **제외**: `crates/` Rust 워크스페이스(거대), `python/` 트램폴린, `assets/`, `scripts/` 벤치마크 도구, `docs/pip/` 호환 가이드 일부, `docs/reference/` 자동생성 CLI 레퍼런스
- **작업**: Astral 회사의 두 번째 제품 uv 수집. ★84,003 / fork 3,006 (2026-04-27 기준), Apache-2.0 OR MIT 듀얼, 첫 커밋 2023-10-02. **수집일 당일 v0.11.8 릴리스** (CHANGELOG `Released on 2026-04-27`). raw 경로 결정: `<org>-<repo>` 컨벤션 따라 `raw/articles/astral-sh-uv/`.
- **생성된 파일**:
  - `wiki/sources/astral-sh-uv.md` — 소스 요약 (7개 도구 통합 야망, universal lockfile uv.lock, 10-100x 성능 4가지 벤치마크 시나리오, 듀얼 지침서 패턴 AGENTS.md+CLAUDE.md, PEP 723 인라인 의존성, Cargo-style workspace, GHSA-pjjw 보안 advisory 5일 패치, 6개 인사이트 + 5개 후속 탐구 후보)
  - `wiki/entities/astral.md` (organization) — Astral Software Inc. 3제품 라인업(ruff/uv/ty), VC-backed OSS, "Rust 재구현형 통합" 5요소 시그니처 패턴, Python fragmentation 사후 해체 가설
  - `wiki/entities/uv.md` (tool) — 6개 기능군 표, universal lockfile, PubGrub resolver, AGENTS.md 외부 채택 사례, PEP 723 자급자족, c2spf-analytics 마이그레이션 ROI 가설
  - `wiki/concepts/python-packaging.md` — PEP 진화 타임라인 8개(440/508/517/518/621/660/723/735), 의존성 해석 알고리즘 3종(Backtracking/PubGrub/Greedy), Lockfile 전략 5도구 비교, Wheel 메타데이터 보안(RECORD), 도구별 포지셔닝 매트릭스 5x8, 4가지 실전 시나리오 + 6개 열린 질문
- **업데이트된 파일**:
  - `wiki/index.md` — 10회차 표기, 통계 71→75 / 28→29 / 24→26 / 15→16, 신규 4페이지 등록 (소스 표·개념 표·엔티티 표 2행)
  - `wiki/logs/log.md` — 본 항목
- **결정적 발견**: **AGENTS.md 외부 산업 채택 4단계 진화** 완성:
  1. [[anthropics-skills]] (3회차) — Anthropic 자체 표준 정의
  2. [[github-spec-kit]] (7회차) — Codex Skills 모드로 외부 도구 통합 (1차 외부 채택)
  3. [[fastapi-fastapi]] (9회차) — `.agents/skills/fastapi/SKILL.md` 라이브러리 self-hosted (2차 외부 채택)
  4. **[[astral-sh-uv]] (본 회차) — `CLAUDE.md` (1줄: `@AGENTS.md`) + `AGENTS.md` (20줄, single source of truth)** — 듀얼 지침서 단일 진실원 패턴 (3차 외부 채택)

  4단계 진화는 [[anthropic]]이 push 중인 표준이 OSS 라이브러리 → 메타-하네스 → 라이브러리 self-hosted skill → minimal single-source dual-pointer로 형태가 다양화하면서도 **표준 자체는 견고**함을 입증한다. 이는 위키의 [[agent-stack-evolution]] 종합 분석에 새 차원을 추가할 가치 있는 발견.
- **메모**:
  - **9회차→10회차 연쇄**: fastapi 9회차 [[tiangolo]] 디폴트 스택의 `uv/Ruff/ty`가 본 회차에 모두 위키에 박힘 (uv 직접, ruff/ty는 [[astral]] 페이지 내부에서). 회차 간 자기일관성이 자연스럽게 형성됨.
  - **c2spf-analytics 마이그레이션 ROI 가설**: pyproject.toml만 정비하면 거의 drop-in. Cold install 5분 → 10초 추정, lockfile universal로 macOS dev / Linux Docker 일관성. 적용 가능성 High. 후속 실험 후보로 분리.
  - **위키 자기 적용**: 향후 `/wiki-ingest`, `/wiki-lint` 슬래시 커맨드를 Python 스크립트로 구현한다면 PEP 723 + `uv run` 단일 파일 패턴이 답.
  - **수집일 당일 v0.11.8 릴리스 — 변경 추적 가치 매우 높음**. CHANGELOG 케이던스 2~3주 패치/마이너 사이클. 향후 lint 시 CHANGELOG 신규 항목 자동 인지 후속 탐구 후보.
  - **후속 탐구 후보 5종** (소스 페이지 메모에 박음):
    - (a) `synthesis/python-toolchain-evolution.md` — pip→poetry→uv 진화의 fragmentation 해체와 통합 패턴
    - (b) `synthesis/rust-rewrite-pattern.md` — Astral + bun + deno + pnpm + Rome(실패) 메타 패턴
    - (c) `concepts/lockfile-strategies.md` — universal vs platform-specific lockfile 5도구 심화
    - (d) `entities/charlie-marsh.md` — Astral 창립자, ruff·uv·ty 3연속 hit 인물
    - (e) `entities/ruff.md`, `entities/ty.md` — Astral 다른 두 제품 별도 수집

---

## [2026-04-27] ingest | fastapi/fastapi — 표준 기반 모던 Python 웹 프레임워크 (9회차)

- **소스**: `raw/articles/fastapi-fastapi/` (19개 파일 보관)
  - 루트 4종: `README.md` (24KB — 핵심 가치 7개 + 기업 채택 인용 + 스폰서 매트릭스), `pyproject.toml` (의존성, classifiers, optional `[standard]`), `SECURITY.md`, `CONTRIBUTING.md`
  - 핵심 docs 10종 (`docs/`): `index.md` (메인 랜딩), `features.md` (FastAPI/Starlette/Pydantic 3계층 기능), `history-design-future.md` (★ Tiangolo의 표준 우선 설계 철학 — OpenAPI/JSON Schema/OAuth2 사전 학습), `alternatives.md` (Flask, DRF, APIStar 등 비교), `async.md` (24KB — `async def` vs `def` 결정 트리), `python-types.md` (타입힌트 활용), `fastapi-cli.md`, `benchmarks.md`, `_llm-test.md` (★ 번역 LLM 회귀 테스트 골든셋 — i18n LLM 파이프라인 사례), `management.md`
  - **결정적 발견 — `agents-dir/`** (`fastapi/.agents/skills/fastapi/`): `SKILL.md` (10.4KB) + `references/{dependencies,streaming,other-tools}.md`. **메인스트림 OSS 라이브러리가 LLM 에이전트용 사용 매뉴얼을 직접 출하한 첫 사례**. frontmatter `name: fastapi` + `description: FastAPI best practices and conventions...`로 자동 호출 트리거.
  - 코드 진입점: `fastapi/__init__.py` (Public API 25개 심볼 + Starlette `status` 재노출). 코어 3대 파일은 `applications.py` (181KB) + `routing.py` (197KB) + `param_functions.py` (69KB)에 집중.
- **작업**: fastapi/fastapi GitHub 저장소(2018-12 출시, MIT, v0.136.1, Python 3.10~3.14, ★80k+) 통합 수집. raw 경로 컨벤션 `<org>-<repo>` 형식 → `raw/articles/fastapi-fastapi/` 채택. 핵심 발견은 라이브러리 디렉토리 안에 [[anthropics-skills]] 표준에 맞춘 self-hosted SKILL.md 패키지가 번들링되어 있다는 점.
- **생성된 파일**:
  - `wiki/sources/fastapi-fastapi.md` — 소스 요약 (메타 / 6단 핵심 내용 / 6개 인사이트 / SKILL.md 강제 컨벤션 매트릭스 / 인용 / 후속 작업 후보 4건). agent-skills 표준 외부 채택 3단계 진화 도식 (anthropics/skills → spec-kit → fastapi self-hosted) 정립.
  - `wiki/entities/fastapi.md` — tool 페이지 (설계 4원칙 + 핵심 기술 5종 + Public API 25개 심볼 표 + `.agents/skills/` 구조 + SKILL.md 권장 컨벤션 14항 + 채택 사례 5사).
  - `wiki/entities/tiangolo.md` — person 페이지 (Sebastián Ramírez OSS 5종 출하 표: FastAPI/Typer/SQLModel/Asyncer/fastapi-cli + "Tiangolo 양식" 6원칙 + i18n LLM 자동화 + agent-skills 출하 사례).
- **업데이트된 파일**:
  - `wiki/concepts/agent-skills.md` — source_count 4→5, tags +library-self-hosted-skill/fastapi, related +[[fastapi]]/[[tiangolo]]. 출처 섹션에 [[fastapi-fastapi]] 추가하며 **외부 채택 3단계 진화 완성** 명시: ① anthropics/skills(표준 정의) → ② github/spec-kit(외부 도구 통합) → ③ fastapi/fastapi(라이브러리 self-hosted).
  - `wiki/concepts/backend-python-fastapi.md` — source_count 5→6, tags +tiangolo/agent-skills/annotated/pydantic2, related +[[fastapi]]/[[tiangolo]], updated 2026-04-24→2026-04-27. 신규 섹션 **"공식 SKILL.md가 제시하는 코딩 컨벤션 (2026-04 갱신)"** 추가 (Annotated 강제, def 디폴트, ORJSONResponse deprecation, Asyncer/SQLModel/HTTPX 추천, c2spf 점검 기준점). 열린 질문 +2건(envelope generic 모델화, SQLAlchemy→SQLModel 마이그레이션 비용).
  - `wiki/index.md` — 9회차 표기, 통계 68→71 / 27→28 소스 / 22→24 엔티티, 신규 3페이지 등록 + 갱신 2개 페이지 source_count·tags·updated 동기화.
- **메모**: 9회차의 결정적 시사점은 **`fastapi/.agents/skills/fastapi/SKILL.md` 발견** — [[agent-stack-evolution]] 분석의 "표준-구현 분리(Anthropic축)" 명제가 OSS 라이브러리 코어까지 침투했다는 정량적 증거. README는 사람용·SKILL.md는 에이전트용이라는 **OSS 분업의 명시화**가 메인스트림에서 처음 일어난 것. 후속 작업 후보 4건: (a) [[agent-stack-evolution]]에 "library self-hosted skill" 4번째 사례 반영, (b) c2spf `analytics-common-api` 코드베이스가 SKILL.md 권장과 어디서 일치/충돌하는지 점검(특히 Annotated/response_model/def 분포), (c) "Tiangolo Default Stack"(fastapi/SQLModel/Asyncer/HTTPX/Typer + uv/Ruff/ty)을 별도 종합 페이지로 정리, (d) `_llm-test.md` 패턴을 위키 자체 lint 워크플로우(LLM 출력 회귀 검사)에 응용.

---

## [2026-04-27] ingest | pandas-dev/pandas — Python 데이터 분석 표준 라이브러리 (8회차)

- **소스**: `raw/articles/pandas-dev-pandas/` (24개 파일 / 1,700줄 보관)
  - 루트 정체성 4종: `README.md`, `AGENTS.md` (★ AI 코딩 에이전트 가이드 발견 — pandas도 AGENTS.md 표준 채택), `AUTHORS.md` (Copyright 모델: 2008-2011 AQR / 2011-2012 Lambda Foundry / 2011- PyData), `CITATION.cff` (DOI 10.5281/zenodo.3509134, McKinney 2010 SciPy)
  - 거버넌스 7종: `governance.md` (★ BDFL+Core Team+NumFOCUS Subcommittee 3축, 산업 표준 거버넌스), `about-index.md` (Mission/Vision/Values + 타임라인 2008→2009→2012→2015→2018), `roadmap.md` (PDEP 시스템), `team.md` (활성 메인테이너 15명 + pandas-stubs 3명 + 비활성 20명 + 4 워크그룹), `sponsors.md` (Tier 1/2 Institutional Partners), `coc.md`, `citing.md` (브랜드/로고/색상)
  - 커뮤니티 2종: `ecosystem.md` (★ 28k → BI 직결 라이브러리 50개 — pandas-gbq, bigframes, Modin, Dask, Bodo, Pandera, Hugging Face `hf://`, marimo, skrub), `benchmarks.md`
  - 사용자 가이드 5종: `overview.rst`, `install.rst` (전체 의존성 매트릭스), `10min.rst`, `scale.rst` (★ 4단계 메모리 폭발 결정 트리: load less → efficient dtypes → chunking → other libraries), `pyarrow.rst`
  - 거버넌스 본체: `pdep-0001-purpose-and-guidelines.md` (★ Quorum=lower(11, 50%), Majority=70% non-abstaining, 60+15일 워크플로우)
  - 메타 3종: `versions.json` (3.0 stable), `config-web.yml` (메인테이너/스폰서/워크그룹 단일 진실 공급원), `pandas-init-public-api.py` (★ pandas/__init__.py의 __all__ 101개 공개 API 카테고리화 — IO read 20개 vs write 3개로 pandas의 본질 = "데이터 게이트웨이" 시사)
  - **제외**: pandas/core 본체 코드, doc/source/whatsnew (CHANGELOG 50+개 리비전), asv_bench, ci, scripts (메소드론은 위 24개에 다 있음)
- **작업**: pandas-dev/pandas GitHub + pandas.pydata.org 공식 사이트 통합 수집. 2008 AQR Capital Management 사내 시작 → 2009 오픈소스 → 2015 NumFOCUS sponsored project → 2026-04-27 v3.0 stable. BSD-3, ★91k+, 2,000+ 컨트리뷰터. raw 경로 결정: 기존 컨벤션 `<org>-<repo>` 형식 따라 `raw/articles/pandas-dev-pandas/` 채택 ([[anthropics-claude-cookbooks]], [[github-spec-kit]], [[microsoft-data-science-for-beginners]] 등과 일관)
- **생성된 파일**:
  - `wiki/sources/pandas-dev-pandas.md` (193줄) — 소스 요약 (한줄 요약 / 메타 / 4축 정체성 / 거버넌스 3축 / PDEP 11개 표 / 에코시스템 BI 매핑 / 핵심 시사점 5개 / AI 에이전트 통합 / 인용할 만한 구절 4개 / 후속 탐구 4건)
  - `wiki/entities/pandas.md` — tool 페이지 (Mission/Vision, Series/DataFrame, 101 공개 API 카테고리화, 시계열 BI 핵심, 4축 정체성 비교, 학술 인용)
  - `wiki/entities/pandas-dev.md` — organization 페이지 (산하 11 저장소, 거버넌스 3축, 4 워크그룹, Institutional Partners Tier 1/2, PDEP 워크플로우, PyData shared copyright)
- **업데이트된 파일**:
  - `wiki/concepts/data-pipeline-bigquery.md` — source_count 4→5, tags 확장(+pandas, pandas-gbq, bigframes, modin, dask, pyarrow), related +[[pandas]], [[pandas-dev]]. **새 섹션 "pandas 통합 — 도구 레이어 표준"** (BigQuery 진입 포인트 표 / scale.rst 4단계 결정 트리 / PyArrow 통합 PDEP-10 / Pandera 검증 코드 예시). 출처 +[[pandas-dev-pandas]]. 열린 질문 +2건
  - `wiki/concepts/ml-ai.md` — source_count 3→4, tags +pandas/scikit-learn/dataframe, related +[[pandas]]. "데이터 분석 도구" 단락 확장 (DataFrame이 scikit-learn first-class citizen). 출처 +[[pandas-dev-pandas]]
  - `wiki/sources/microsoft-data-science-for-beginners.md` — related +[[pandas]], [[pandas-dev-pandas]]
  - `wiki/index.md` — 8회차 표기, 통계 65→68 / 26→27 소스 / 20→22 엔티티, 신규 3페이지 등록 + 갱신 2개 페이지 source_count·tags·updated 동기화
- **메모**: pandas의 거버넌스(BDFL+Core Team+NumFOCUS Subcommittee)는 [[github-spec-kit]] Constitution(GitHub 단독)과 [[anthropics-skills]](Anthropic 단독 큐레이션)와 본질적으로 다른 4번째 거버넌스 축 — 향후 [[agent-stack-evolution]]에 4축 거버넌스 비교축 추가 가치 있음. PDEP-1의 "메트릭 게이밍 명시적 거부"("100 commits"같은 자의적 임계치 거부)는 [[autonomous-research-loop]]의 메트릭 잠금과 정반대 — 인간 거버넌스 vs 메트릭 거버넌스 대비. scale.rst의 "Load less data → efficient dtypes → chunking → other libraries" 4단계는 BI 데이터 처리의 메모리 폭발 대응 표준. 후속 탐구 후보 4건: (a) `synthesis/data-analysis-essentials.md` 신설(Microsoft 라이프사이클 + pandas 도구 레이어 + BigQuery 운영 종합), (b) PDEP-7 Copy-on-Write 단독 raw 보관 (27kB), (c) pandas-stubs 별도 entity, (d) [[agent-stack-evolution]]에 4축 거버넌스 비교축 추가.

---

## [2026-04-27] ingest | github/spec-kit — Spec-Driven Development 툴킷 (7회차)

- **소스**: `raw/articles/github-spec-kit/` (32개 파일 보관)
  - 루트 메타 6종: `README.md` (765줄), `spec-driven.md` (412줄, SDD 메소드론 정통 정의), `AGENTS.md` (451줄, 통합 아키텍처), `CHANGELOG.md` (1,368줄), `DEVELOPMENT.md`, `CONTRIBUTING.md`
  - `docs/` 5종: `index.md`, `quickstart.md`, `installation.md`, `upgrade.md` (462줄), `local-development.md`
  - `templates/` 5 템플릿: `spec-template.md` (128줄), `plan-template.md` (104줄), `tasks-template.md` (251줄), `constitution-template.md` (50줄), `checklist-template.md` (40줄)
  - `templates/commands/` 9개 슬래시 명령 정의 마크다운: `analyze.md` (252줄), `checklist.md` (364줄), `clarify.md` (250줄), `constitution.md` (150줄), `implement.md` (201줄), `plan.md` (152줄), `specify.md` (327줄), `tasks.md` (203줄), `taskstoissues.md` (99줄)
  - `workflows/` 3종: `README.md`, `ARCHITECTURE.md`, `speckit-workflow.yml`
  - `presets/` 2종: `README.md`, `ARCHITECTURE.md`
  - `integrations/` 2종: `README.md`, `catalog.json`
  - **제외**: `src/specify_cli/` Python 소스 (메소드론은 마크다운에 다 있음 — Python은 thin wrapper)
- **작업**: GitHub 공식 SDD 툴킷 수집. ★91k+ / fork 7.8k (2026-04-27 기준), MIT, 2025-08 시작 / 2026-04-24 v0.8.1. raw 경로 결정: 기존 컨벤션 `<org>-<repo>` 형식 따라 `raw/articles/github-spec-kit/` 채택 ([[anthropics-claude-cookbooks]], [[microsoft-for-beginners]] 시리즈와 동일)
- **생성된 파일**:
  - `wiki/sources/github-spec-kit.md` — 소스 요약 (SDD 4 + 5 단계, 7가지 LLM 출력 제약 메커니즘, 9 Articles Constitution, 5가지 Integration Base Class, 4층 Override Stack, Codex Skills 모드 = agent-skills 표준 첫 외부 채택, Microsoft·Anthropic·Karpathy·GitHub 4축 비교)
  - `wiki/entities/github.md` — GitHub organization 페이지 (인프라 노드 + 조직 노드, spec-kit/Copilot/Marketplace/CLI/Codespaces, Microsoft 모회사와의 전략 추상화 비교)
  - `wiki/entities/spec-kit.md` — Spec Kit + Specify CLI tool 페이지 (9 슬래시 명령, 5 템플릿, 5 base class, 4층 override, 40+ 커뮤니티 확장)
  - `wiki/concepts/spec-driven-development.md` — SDD 메소드론 (Power Inversion, 6 Core Principles, 9 Articles, Template-Driven Quality, 5 패턴 사전 합성, 3가지 개발 단계, 6가지 안티패턴, 6가지 열린 질문)
- **업데이트된 파일**:
  - `wiki/entities/claude-code.md` — source_count 7→8, spec-kit `--integration claude` 통합 사례 추가, 출처에 `[[github-spec-kit]]` 추가
  - `wiki/concepts/agent-skills.md` — source_count 3→4, **agent-skills 표준의 첫 외부 채택 사례**(Codex Skills 모드)로 spec-kit 박음, "agent-skills = Anthropic-only" 가설 명확히 깸
  - `wiki/concepts/harness.md` — source_count 4→5, "**하네스 스펙트럼 — 양극 사례**" 섹션 신설(autoresearch 최소 극단 ↔ spec-kit 표준화 극단 8개 축 비교표), [[spec-driven-development]] 링크
  - `wiki/concepts/agent-patterns.md` — source_count 1→2, spec-kit가 5 패턴을 "메소드론으로 사전 합성한 결과물"이라는 관점 추가
  - `wiki/index.md` — 7회차 표기, 통계 65/26/20/15, 신규 4페이지 등록 + 갱신 4페이지 source_count·tags 동기화
- **메모**: 이 위키 자체에 spec-kit 패턴을 차용할 강한 근거 발견 — `templates/commands/`에 `/wiki-ingest`, `/wiki-lint`, `/wiki-synthesize`, `/wiki-query` 4개 LLM 지침서를 spec-kit `templates/commands/specify.md` 스타일로 작성하면 CLAUDE.md 워크플로우의 코드화. 후속 탐구 후보로 분리. SDD vs vibe coding ROI 경계는 [[spec-driven-development]] 열린 질문에 박음. v0.8.1이 3일 전(2026-04-24) 릴리스 — 활발한 변경 추적 가치.

---

## [2026-04-27] synthesis | 에이전트 스택의 3축 진화 — Microsoft · Anthropic · Karpathy 비교

직전 5회차 anthropics/claude-cookbooks 수집의 후속 분석. 사용자 의사결정 가치 검토 후 후속 탐구 (b) 진행. (a) `claude-managed-agents` entity는 source_count 1 회피로 보류, (c) `/wiki-lint`는 위키 100 페이지 후로 보류.

- **신규 종합 분석**: `wiki/syntheses/agent-stack-evolution.md` (174 lines) — 8개 비교 축으로 3축 분석:
  1. 표준-구현 관계 (분리 안 함 / 명확 분리 / 표준=구현)
  2. 최소 단위 (lesson.md / SKILL.md+notebook / 단일 파일)
  3. 페다고지 위계 (입문자 6단 / API 개발자 노트북 / 연구자 read the source)
  4. CI-로컬 통합 채널 (GitHub Action / 슬래시 커맨드 / 평가 스크립트)
  5. 다국어/접근성 정책 (50+ 언어 + 02·03번 가치 박기 / 영어 only / 비고려)
  6. 메트릭과 객관성 (인간 평가 / 자동+인간 / 메트릭 잠금)
  7. [[harness]] 4층 레이어 비교 (지식 두꺼움 / 패키지 두꺼움 / 통제 가벼움)
  8. 자기 정의 인용 비교 ("free of charge" / "bare metal harness" / "Read the source")
- **결론 핵심 5가지 + 실전 가이드**:
  - "3축은 보완 관계, 경쟁 관계가 아니다" — 사용자 단계에 따라 다른 축
  - 회사 BI 시나리오별 권장 축 표 (자연어 SQL=MS, 쿼리 표준화=Anthropic, 지표 자동화=Karpathy)
  - **개인 비서 = "Anthropic 70% + Karpathy 30%"**, **회사 BI = "Microsoft 50% + Anthropic 30% + Karpathy 20%"** 일차 가설
  - 위키 자기 차용 분석 (한영 병기=MS, CLAUDE.md=Karpathy, 향후 /wiki-lint=Anthropic)
- **업데이트된 파일**:
  - `wiki/index.md` — 종합 분석 표에 [[agent-stack-evolution]] 행 추가, 통계 60→61, HTML 주석 후속 분석 줄 추가
  - `wiki/logs/log.md` — 본 항목
- **후속 합성 후보** (이 페이지 본문 메모에 박음): (a) `synthesis/llm-eval-objectivity.md` — 메트릭 객관성 3축 비교 심화, (b) `synthesis/wiki-operating-model.md` — 위키 자체가 3축을 어떤 비율로 차용 중인지 자기 분석.

---

## [2026-04-27] ingest | anthropics/claude-cookbooks — Claude API · Agent SDK · Managed Agents 실습 노트북 모음

5회차 수집. anthropics/skills(3회차) + microsoft for-beginners(4회차)와의 짝을 이루는 anthropic 측 두 번째 큰 자료. 14개 디렉토리 ~100 노트북 카탈로그.

- **소스 (raw 신규 보관)** — `raw/articles/anthropics-claude-cookbooks/` (17개 파일, 3,410 lines):
  - 루트 메타 5종: README.md, CLAUDE.md, CONTRIBUTING.md, Makefile, pyproject.toml
  - 디렉토리 README 5종: patterns-agents, claude_agent_sdk, managed_agents, skills, capabilities
  - 카탈로그 메타 2종: registry.yaml(노트북 단일 진실원, 23KB), authors.yaml(기여자 메타)
  - 노트북 마크다운 추출 5종: basic-workflows(Building Effective Agents 5 패턴), research-agent, chief-of-staff, memory-cookbook, prompt-caching
  - **선택 근거**: 거대 ipynb 본체(3MB+ 멀티모달 스크린샷 등)는 본질이 마크다운에 다 있고 보관 시 무게 폭발 → 마크다운 셀만 jq로 추출. ipynb의 `source` 필드가 string 또는 array 양형식이라 파이프라인에 type 분기 필요(`if type=="array" then join else .source end`)
- **생성된 파일 (4개)**
  - **소스 (1)**: `wiki/sources/anthropics-claude-cookbooks.md` — 14 디렉토리 카탈로그, "Building Effective Agents 5 패턴" 정의, claude_agent_sdk 6단계 튜토리얼 표, managed_agents 8개 학습 포인트 표, skills 3 노트북, Anthropic의 노트북 운영 표준(슬래시 커맨드 = CI = 로컬 / 모델 ID 정책 / registry.yaml)
  - **엔티티 (2)**:
    - `wiki/entities/anthropic.md` (organization) — Microsoft 페이지와 균형. "표준 vs 구현" 분리 운영 패턴, "Claude Code = bare-metal harness" 자기 정의 인용, Microsoft와의 운영 차이 표
    - `wiki/entities/claude-agent-sdk.md` (tool) — Python SDK 인터페이스 3개(`query()` · `ClaudeSDKClient` · `ClaudeAgentOptions`), Claude Code 운영 기법의 SDK화, 6단계 튜토리얼, "Beyond Coding: The Agent Builder's Toolkit" 자기 정의
  - **개념 (1)**: `wiki/concepts/agent-patterns.md` — Building Effective Agents 5 패턴(Prompt Chaining/Routing/Parallelization/Orchestrator-Workers/Evaluator-Optimizer), Basic 3 + Advanced 2 위계, autoresearch과의 매핑 표, BI/개인비서 적용 예, 안티패턴 4종
- **업데이트된 파일 (6개)**
  - `wiki/entities/claude-code.md` — frontmatter related/tags/source_count 5→7/updated 갱신, 개요에 "bare-metal harness" 인용 + [[claude-agent-sdk]] 추가, 멀티 에이전트 섹션의 "Agent SDK"가 [[claude-agent-sdk]] 위키링크로 격상, 출처에 [[anthropics-claude-cookbooks]] 추가, 중복 [[anthropics-skills]] 1개 제거 (1276 버그 픽스)
  - `wiki/concepts/agent-skills.md` — frontmatter source_count 2→3, related에 [[claude-agent-sdk]]·[[anthropic]] 추가, 출처에 [[anthropics-claude-cookbooks]] 추가 (skills/ 노트북 3종 + custom_skills 사례 3종 reference)
  - `wiki/concepts/harness.md` — frontmatter source_count 3→4, related에 [[claude-agent-sdk]]·[[anthropic]]·[[agent-patterns]] 추가, **신규 섹션 "Anthropic의 자기 정의 (claude-cookbooks)"** — bare-metal harness 인용 + Claude Code/Agent SDK가 하네스의 anthropic-side 정통 정의라는 자리매김
  - `wiki/concepts/context-engineering.md` — frontmatter source_count 3→4, related에 [[claude-agent-sdk]]·[[anthropic]]·[[anthropics-claude-cookbooks]] 추가, 출처에 memory_cookbook + automatic-context-compaction + session_memory_compaction 3종 추가
  - `wiki/concepts/token-economy.md` — frontmatter source_count 1→2, updated 2026-04-15→2026-04-27, related에 [[claude-agent-sdk]]·[[anthropic]]·[[agent-patterns]] 추가, **신규 섹션 "Prompt Caching 운영 핸들"** — TTL 5분/1시간, 4 breakpoint 한도, 1024 토큰 최소, 0.1× 적중 비용 정량 수치
  - `wiki/concepts/mcp.md` — frontmatter source_count 5→6, related에 [[claude-agent-sdk]]·[[anthropic]]·[[agent-patterns]] 추가, 출처에 Observability Agent(13+/100+ tools) + SRE Agent(자체 JSON-RPC subprocess MCP) + CMA_operate_in_production(vault-backed credentials) reference 추가
- **메모**: 핵심 발견 5가지.
  1. **"skills 리포 ↔ cookbooks 리포" 분업이 명료** — skills = 배포 채널(SKILL.md 패키지 17개), cookbooks = 실습 채널(노트북 ~100). 두 리포 합쳐 "Anthropic 표준 스택" 완성. 위키 4개 entity([[claude-code]]/[[agent-skills]]/[[claude-agent-sdk]]/(추후 claude-managed-agents))가 이 스택의 짝.
  2. **Building Effective Agents 5 패턴이 위키의 빈자리를 정확히 채움** — [[autonomous-research-loop]]은 "한 종류의 자율 루프"였지, 일반 분류는 부재했음. Anthropic 5 패턴(Schluntz·Zhang)이 위키의 1차 분류 체계로 자리잡고, autoresearch는 "Evaluator-Optimizer + Orchestrator-Workers의 도메인 특화 합성"으로 자리매김.
  3. **"Claude Code = bare-metal harness for Claude's raw agentic power"** 자기 정의 입수 — `claude_agent_sdk/README.md`에 박힌 한 문장이 [[harness]]·[[claude-code]]·[[claude-agent-sdk]] 세 페이지의 정통 정의가 됨. 가장 인용 가치 높은 문장.
  4. **Anthropic의 운영 표준 자체가 자료** — `/notebook-review`·`/model-check`·`/link-review` 슬래시 커맨드를 .claude/commands/에 정의해 Claude Code(로컬)와 GitHub Actions(CI)가 같은 정의를 호출하는 패턴. 위키에 그대로 차용 가능 (예: `/wiki-lint`).
  5. **Memory Cookbook이 Microsoft lesson 13의 코드 짝** — 7가지 메모리 타입을 코드 인터페이스로 구현. context-engineering의 "Memories" strategy 항목이 이론(Microsoft) + 코드(Anthropic) 짝으로 완성.
- **후속 탐구 후보**: (a) `claude-managed-agents` entity 분리 — 현재 cookbooks 소스 안에만 정리, "에이전트의 PaaS" 추상화로 별도 페이지 가치 있음. (b) `synthesis/agent-stack-evolution.md` — Microsoft for-beginners ↔ Anthropic skills/cookbooks ↔ Karpathy autoresearch 3축 비교 종합 분석. (c) `/wiki-lint` 슬래시 커맨드 시도 (CLAUDE.md "lint" 워크플로우 코드화).

---

## [2026-04-27] follow-up | lesson 13 (Agentic Memory) 보강 + templates/lesson.md 신설

직전 microsoft for-beginners 통합 수집의 후속 탐구 2건을 즉시 진행.

- **신규 raw 파일**:
  - `raw/articles/microsoft-ai-agents-for-beginners/lesson-13-agent-memory.md` (163줄) — 7가지 메모리 타입 정의(Working/Short-term/Long-term/Persona/Episodic/Entity/Structured RAG), Mem0/Cognee/Azure AI Search 구현 도구, "Knowledge Agent" Self-Improving 4단계 패턴, latency/cold-storage 최적화 가이드
- **갱신된 파일**:
  - `wiki/concepts/context-engineering.md` — "Memories Strategy 심화 — 7가지 메모리 타입 (lesson 13)" 서브섹션 신규 추가 (Failure Mode 표 뒤, 자율 루프 보호 3원칙 앞). 7가지 메모리 타입 분류 표, Mem0/Cognee/Azure AI Search 도구 목록, Knowledge Agent 4단계 패턴 + latency/cold storage 최적화. [[harness]]의 "다단계 검증 게이트"와 같은 발상의 메모리 버전이라는 연결 포인트 명시
  - `wiki/sources/microsoft-ai-agents-for-beginners.md` — Lesson 카탈로그 표 13번 행 강조 + "(raw 보관)" 마킹 추가 (기존 11/12번과 동일 처리)
- **신규 템플릿**:
  - `templates/lesson.md` (5번째 페이지 템플릿) — Microsoft for-beginners 페다고지 6단(pre-quiz / 본문 / knowledge checks / challenge / supplemental reading / assignment / post-quiz)을 위키용으로 응용한 7섹션 구조 (Warmup → 본문 → Knowledge Check → Challenge → 추가 자료 → Assignment → Wrap-up). 신규 frontmatter 필드: `type: lesson`, `difficulty` (beginner/intermediate/advanced), `duration_min` (예상 학습 시간). 헤더 주석에 응용 의도와 기존 4종(entity/concept/source/synthesis)과의 차이 명시
  - `CLAUDE.md` — 디렉토리 구조 ASCII 트리에 `lesson.md` 한 줄 추가 (templates 카탈로그 4종→5종)
- **메모**: lesson 13 자체가 [[context-engineering]]의 "Memories" strategy 한 항목을 구현 깊이까지 펼친 것이라, 이번 보강은 12번 lesson(전체 카탈로그) + 13번 lesson(한 strategy 심화)을 같은 페이지에서 추상화 레이어 차이를 살리며 통합. 추후 메모리 토픽이 더 무거워지면 별도 `concepts/agent-memory.md` 분리 검토 가능.
- **lesson.md 응용 시나리오**: 가장 적합한 첫 사용처는 (a) microsoft-data-science-for-beginners의 lesson 14(Lifecycle)을 회사 BI에 매핑한 자기 학습 페이지, 또는 (b) microsoft-generative-ai-for-beginners의 lesson 15(RAG)을 [[llm-wiki-pattern]]에 직접 응용한 실습 페이지. 둘 다 "교과서 형식"의 1회 학습 자원이라 lesson 타입에 맞음.

---

## [2026-04-27] ingest | microsoft for-beginners 5종 통합 수집 — Cloud Advocates 무료 커리큘럼 시리즈

- **소스 (raw 신규 보관)** — `raw/articles/microsoft-*-for-beginners/` 5개 디렉토리:
  - `microsoft-generative-ai-for-beginners/` — README.md (24KB) + lesson-15-rag-and-vector-databases.md + lesson-17-ai-agents.md
  - `microsoft-ai-agents-for-beginners/` — README.md (20KB) + lesson-11-agentic-protocols.md (13KB) + lesson-12-context-engineering.md (13KB)
  - `microsoft-ml-for-beginners/` — README.md (31KB) + lesson-21-timeseries-intro.md
  - `microsoft-web-dev-for-beginners/` — README.md (33KB) + lesson-26-chat-project.md
  - `microsoft-data-science-for-beginners/` — README.md (27KB) + lesson-14-lifecycle-intro.md
- **선택 근거**:
  - 5개 시리즈 합 1.5–6.5GB 규모 (50+ 언어 자동 번역으로 비대) — README 본체 + 석근(BI 개발자, AI 관심사) 직결 lesson만 선별 보관
  - lesson 선정 기준: [[mcp]] 정확화에 직결되는 11(Agentic Protocols), [[context-engineering]] 보강하는 12(Context Engineering for AI Agents), BI 직결 7-TimeSeries, Data Science 라이프사이클 14, GenAI 통합 lesson(15 RAG/17 Agents/26 chat-project)
  - 거대 코드/notebook은 raw 보관 제외 — 불변성 + 본질 압축 원칙 (기존 `raw/articles/karpathy-*/`, `raw/articles/anthropics-skills/` 관례와 일치)
- **생성된 파일 (7개)**
  - **소스 (5)**:
    - `wiki/sources/microsoft-generative-ai-for-beginners.md` — 21 Lesson 카탈로그, "Learn/Build" 명시 분리, 다중 백엔드(Azure/GitHub Models/OpenAI), 19–21=SLM/Mistral/Meta 모델 단원
    - `wiki/sources/microsoft-ai-agents-for-beginners.md` — 12+ Lesson, 11 Agentic Protocols 3종(MCP/A2A/NLWeb), 12 Context Engineering 5 type/6 strategy/4 failure 카탈로그
    - `wiki/sources/microsoft-ml-for-beginners.md` — 26 Lesson 클래식 ML, 의도적 딥러닝 회피, R lesson 병행, "세계 문화" 데이터셋
    - `wiki/sources/microsoft-web-dev-for-beginners.md` — 24 Lesson 의도적 프레임워크 회피, 7개 프로젝트, 9-chat-project = AI Assistant 신설
    - `wiki/sources/microsoft-data-science-for-beginners.md` — 20 Lesson, 02=Data Ethics 본문 두 번째, 4-Lifecycle 3단계(Introduction→Analyzing→Communication)
  - **엔티티 (2)**:
    - `wiki/entities/microsoft.md` (organization) — Microsoft Cloud Advocates DevRel 운영체계, Azure AI Foundry/Microsoft Agent Framework, GitHub 자회사 인프라(Copilot/Codespaces/Marketplace), MCP/A2A/NLWeb 카탈로그화 신호
    - `wiki/entities/microsoft-for-beginners.md` (project) — 5개 시리즈 통합 표(107 lessons, 386,000+ stars), 공통 인프라(co-op-translator GitHub Action, ff-quizzes, Foundry Discord), 페다고지(project-based + frequent quizzes), 살아있는 커리큘럼(v3, "Coming Soon", Copilot 챌린지 사후 추가)
- **업데이트된 파일**
  - `wiki/concepts/mcp.md` — source_count 4→5, updated 2026-04-15→2026-04-27, tags에 a2a/nlweb/agentic-protocols 추가, related에 [[microsoft-for-beginners]]·[[context-engineering]] 추가, 본문에 **3 Primitives**(Tools/Resources/Prompts) + **클라이언트-서버 아키텍처**(Hosts/Clients/Servers) + **MCP의 3가지 이점 표** + **자매 프로토콜 A2A/NLWeb 섹션** 신규
  - `wiki/concepts/context-engineering.md` — source_count 2→3, updated 2026-04-27 (재갱신), tags에 agent-memory/scratchpad/microsoft-for-beginners 추가, related에 [[mcp]]·[[microsoft-ai-agents-for-beginners]] 추가, 본문에 **5가지 Context Type 표 + Planning 3단계 + 6가지 Practical Strategy + 4가지 Failure Mode 표** 섹션 신규
  - `wiki/index.md` — 통계 49→56 / 소스 19→24 / 엔티티 14→16, 소스 표에 5행, 엔티티 표에 2행 추가, HTML 주석에 4회차 수집 기록
- **메모**: 핵심 발견 4가지.
  1. **MCP가 단독이 아니라 "Agentic Protocols" 카탈로그의 한 축** — Microsoft가 lesson 11에서 MCP/A2A/NLWeb를 묶어 가르치는 구도는 [[mcp]]가 위키에서 더 큰 카테고리(수직-LLM↔도구 / 수평-에이전트↔에이전트 / 수직-에이전트↔웹) 안에 자리잡게 한다. Anthropic이 만든 표준이 Microsoft 입문 자료에 정식 편입되는 표준 확산 신호.
  2. **Context Engineering이 운영 카탈로그로 체계화** — Karpathy의 컨텍스트 보호 3원칙(stdout 격리·메트릭 1줄·크래시시 tail)이 운영 휴리스틱이라면, Microsoft lesson 12는 5 type / 6 strategy / 4 failure mode로 분류 체계를 제공. 두 추상화가 보완.
  3. **Microsoft Cloud Advocates의 "단일 운영체계"** — 5개 시리즈가 같은 GitHub Action·같은 Discord·같은 퀴즈 앱·같은 페다고지를 공유. Anthropic의 [[claude-code]] + Skills + Plugin Marketplace + Cowork와 비교하면 Microsoft는 "**인프라+표준 카탈로그**" 추상화 레벨에서 운영.
  4. **데이터 윤리/접근성을 본문 02·03번에 배치** — Data Science(02=Ethics)·Web Dev(03=Accessibility) 모두 입문 단계에 가치(values)를 박는 페다고지. 회사 BI에 적용 가능한 메타 패턴.
- **후속 탐구**:
  1. lesson 13 (Agentic Memory) raw 보관 검토 — [[context-engineering]]의 "Memories" strategy를 구현 수준으로 확장
  2. `microsoft/mcp-for-beginners` 수집 검토 — MCP 전용 입문 코스
  3. `microsoft/AI-For-Beginners` 수집 검토 — 딥러닝까지 보강 (현재 ML-For-Beginners는 의도적 회피)
  4. `templates/lesson.md` 신설 검토 — Microsoft 페다고지 6단(pre-quiz / 본문 / knowledge checks / challenge / assignment / post-quiz) 위키 응용
  5. **컴투스플랫폼 BI 응용**: Data Science lesson 14(Lifecycle) 3단계를 회사 BI 라이프사이클에 1:1 매핑한 [[c2spf-analytics]] 보강 가능

---

## [2026-04-27] ingest | anthropics/skills 수집 — Agent Skills 표준·마켓플레이스·skill-creator

- **소스 (raw 신규 보관)** — `raw/articles/anthropics-skills/` (8 파일):
  - `README.md` (5.5KB) — 마켓플레이스 등록·스킬 작성 가이드·document-skills 라이선스 안내
  - `marketplace.json` — 3개 플러그인(document-skills 4개, example-skills 12개, claude-api 1개) 정의
  - `template-skill.md` — 7줄 placeholder
  - `spec-redirect.md` — `spec/agent-skills-spec.md`가 agentskills.io/specification으로 리다이렉트되는 안내문
  - `skill-creator-skill.md` (33KB) — 가장 풍부한 메타-스킬, 5단계 루프·description 최적화·Claude.ai/Cowork specific 분기
  - `mcp-builder-skill.md` (9KB) — multi-domain reference 분리 패턴
  - `frontend-design-skill.md` (4.4KB) — 짧고 강한 단일 SKILL.md 패턴
  - `webapp-testing-skill.md` (3.9KB) — "scripts는 읽지 마라" 블랙박스 패턴
- **선택 근거**: 17개 스킬 전부를 raw에 두면 과적재 — 4가지 SKILL.md 패턴(메타-스킬·multi-domain·짧은 단일 파일·블랙박스) 대표 사례만 선별. 마켓플레이스 메타·README·spec 리다이렉트는 표준 진입점이라 보존 필수. 기존 `raw/articles/karpathy-*/` 관례와 일치.
- **생성된 파일 (2개)**
  - **소스 (1)**: `wiki/sources/anthropics-skills.md` — 리포 구조·17개 스킬 4갈래 분류·4개 SKILL.md 사례 분석·SKILL 작성 표준·spec 분리의 의미·document-skills source-available 라이선스의 비즈니스 신호·위키에 직접 응용 가능한 4가지 패턴
  - **개념 (1)**: `wiki/concepts/agent-skills.md` — Agent Skills 정의·3-Level Progressive Disclosure·14개 frontmatter 필드·호출 제어 매트릭스·Skill 저장 위치 우선순위·content lifecycle·description 작성 4룰·description 자동 최적화 루프·Slash Command vs Skill 비교·SKILL.md 패턴 4가지·석근 시나리오 4종(위키·BI·비서·templates/skill.md)·5가지 안티패턴
- **업데이트된 파일**
  - `wiki/entities/claude-code.md` — source_count 5→6, updated 2026-04-16→2026-04-27, tags에 agent-skills·plugin-marketplace 추가, Skills 항목 본문에 progressive disclosure 3-level 명시 + [[agent-skills]] 링크, **Plugin Marketplace 항목 신규** (anthropics-skills 등록 명령·플러그인 3종), 출처에 [[anthropics-skills]] 추가, 관련 개념에 [[agent-skills]] 추가
  - `wiki/index.md` — 통계 47→49 / 소스 18→19 / 개념 12→13. 소스 표·개념 표에 신규 행 추가
- **메모**: 핵심 발견 3가지.
  1. **spec 분리 = 표준 오너십 분리** — Anthropic이 SKILL.md 표준의 단일 운영자가 되는 걸 의도적으로 피한 흔적 (agentskills.io). [[mcp]]가 Anthropic 발이지만 modelcontextprotocol.io에서 운영되는 패턴과 동일.
  2. **document-skills "source-available, not open source"** — xlsx/docx/pptx/pdf는 Claude.ai 문서 생성 production 코드. 라이선스로 fork·재배포 통제. Anthropic의 비즈니스 라인이 어디서 시작되는지 노출.
  3. **skill-creator의 자기참조 구조** — 스킬 작성을 가르치는 스킬이 다시 SKILL.md 형식으로 쓰여 있고, 자기 자신을 평가·개선하는 검증 루프를 본문에서 주도. 이게 [[autonomous-research-loop]] (program.md)와 같은 자기 진화 패턴이지만 **코드가 아닌 지침서를 진화**시킨다는 차이.
- **후속 탐구**:
  1. `~/.claude/skills/wiki/SKILL.md` description을 "pushy" 원칙으로 재작성 + 20개 trigger 검증 쿼리로 trigger rate 측정
  2. 위키에 `templates/skill.md` 추가 검토 (entity/concept/source/synthesis 4종 + skill 1종)
  3. **컴투스플랫폼 BI 스킬** 후보: `bi-query-patterns/SKILL.md` — KPI 조회/코호트/retention 패턴, references에 BigQuery 슬롯 최적화·MMP 데이터 조인
  4. Partner Skills 첫 사례 Notion이 향후 확장 시그널 — 사내 도구 스킬 패키징 가능성

---

## [2026-04-27] ingest | karpathy/nanoGPT + karpathy/nanochat 수집

- **소스 (raw 신규 보관)**:
  - `raw/articles/karpathy-nanogpt/README.md` (13.8KB, 234줄) — `gh api repos/karpathy/nanoGPT/contents/README.md`로 base64 디코드 보관. 라이선스 MIT.
  - `raw/articles/karpathy-nanochat/README.md` (16.5KB, 222줄) — `gh api repos/karpathy/nanochat/contents/README.md`로 보관. 라이선스 MIT.
- **선택 근거**: 기존 `raw/articles/karpathy-autoresearch/` 관례와 일치. 두 저장소 모두 README가 운영 패턴의 본질 — 무거운 Python 코드(`train.py`, `model.py`, `prepare.py` 등) 및 `uv.lock`은 보관 제외.
- **생성된 파일 (4개)**
  - **소스 (2)**:
    - `wiki/sources/karpathy-nanogpt.md` — 2025-11 deprecated 명시, ~300줄 train.py + model.py 디자인, MPS 지원 디테일, 한계 4가지(사전학습만/구식 아키텍처/단일 다이얼 부재/평가 미내장) — 모두 nanochat에서 해결됨
    - `wiki/sources/karpathy-nanochat.md` — $100 GPT-2 풀 파이프라인, 단일 `--depth` 다이얼 디자인, **Time-to-GPT-2 리더보드** 표(행 #5, #6이 autoresearch 라운드 1, 2), AI Policy disclosure 정책
  - **엔티티 (2)**:
    - `wiki/entities/nanogpt.md` (project) — deprecated 상태 마킹, 자손 계보(minGPT → nanoGPT → nanochat → autoresearch), 위키 보존 사유 명시
    - `wiki/entities/nanochat.md` (project) — 활성 주력, 풀 파이프라인 모듈 매핑, 리더보드 표, 정밀도/하드웨어 가이드, AI Policy
- **업데이트된 파일 (3 + 1)**
  - `wiki/entities/karpathy.md` — source_count 1→3, 교육 자산 항목을 자손 계보로 구체화(minGPT → nanoGPT → nanochat → autoresearch), AI Policy 명문화 사실 추가, related에 [[nanogpt]]·[[nanochat]] 추가, 출처 2건 추가
  - `wiki/entities/autoresearch.md` — 부모 저장소 nanochat을 위키링크화([[nanochat]]), **"자기 강화 순환" 섹션 신규 추가** (autoresearch round 1·2가 nanochat 리더보드 #5·#6를 갱신했다는 사실)
  - `wiki/concepts/autonomous-research-loop.md` — source_count 1→2, **"실증: nanochat 리더보드 #5, #6" 섹션 신규** (자율 루프가 사람 SOTA를 갱신한 첫 공개 사례), 출처에 [[karpathy-nanochat]] 추가
  - `wiki/index.md` — 통계 43→47 / 소스 16→18 / 엔티티 12→14. 4개 카테고리 테이블 행 추가/갱신
- **메모**: 핵심 발견은 **autoresearch가 nanochat 리더보드 #4(사람) → #5(자율) → #6(자율)에서 사람 SOTA를 능가하고 그 결과가 부모 저장소로 머지되는 자기 강화 순환을 만든다는 점**. 이로써 [[autonomous-research-loop]] 패턴이 사변적이지 않고 실증된 운영 모델임이 위키에 박힘. 또한 nanoGPT의 deprecated 처리(2025-11)를 위키에 그대로 반영하여 사용자가 잘못된 출발점을 선택하지 않도록 함.
- **후속 탐구**:
  1. autoresearch round 3+ 결과를 정기 추적 → nanochat 페이지 리더보드 표 / autoresearch 페이지 / autonomous-research-loop 페이지 3곳 동기 갱신
  2. minGPT(전신) raw 보관은 보류 — 패턴 계보 시작점이지만 실용성이 nanoGPT보다 낮음
  3. micrograd, llm.c, Zero to Hero 등 Karpathy의 다른 교육 자산은 [[ml-ai]] 페이지 보강용으로 별도 수집 가치 있음
  4. **Karpathy의 두 작업(nanochat ↔ autoresearch)이 자기 강화 순환을 이루는 점**은 별도 종합 분석(`wiki/syntheses/`)으로 정리할 가치 있음 — "사람-자율 루프 협업의 첫 공개 사례"라는 큰 그림으로

---

## [2026-04-27] ingest | karpathy/autoresearch 수집

- **소스 (raw 신규 보관)**: `raw/articles/karpathy-autoresearch/README.md` (8.0KB) + `raw/articles/karpathy-autoresearch/program.md` (7.0KB) — `gh api repos/karpathy/autoresearch/contents/...` 로 base64 디코드해 그대로 복사. 라이선스 MIT.
- **선택 근거**: GitHub 프로젝트의 공식 문서라서 `raw/articles/`에 두는 게 기존 `raw/articles/claude-code/` 관례와 일치. 무거운 파이썬 코드(`prepare.py` 15KB, `train.py` 26KB, `uv.lock` 443KB)와 `progress.png`는 raw에 두지 않음 — 위키는 운영 패턴이 본질이므로 마크다운 2개로 충분.
- **생성된 파일 (4개)**
  - **소스 (1)**: `wiki/sources/karpathy-autoresearch.md` — 5분 시간 예산 / `val_bpb` 단일 메트릭 / `train.py` 단일 파일 수정 / `program.md` = "lightweight skill" / NEVER STOP 원칙 정리
  - **엔티티 (2)**: `wiki/entities/karpathy.md` (person — OpenAI 창립 멤버, Tesla AI 디렉터 출신, 교육 자산 nanoGPT/micrograd/llm.c/Zero to Hero 보유) · `wiki/entities/autoresearch.md` (project — 76,912 stars, MIT, 4개 포크 macos/mlx/win-rtx/amd 노출)
  - **개념 (1)**: `wiki/concepts/autonomous-research-loop.md` — 4중 제약(단일 메트릭·고정 시간 예산·단일 파일·무한 루프) / 5단계 루프 골격 / 컨텍스트 보호 3원칙 / 석근 응용 시나리오 3종(BI 쿼리 자율 튜닝, 비서 AI prompt 진화, 위키 운영 — 위키는 메트릭 부재로 직접 적용 불가)
- **업데이트된 파일**
  - `wiki/concepts/harness.md` — source_count 1→2, "극한 사례: autoresearch의 초경량 하네스" 섹션 추가, related에 [[autoresearch]]·[[autonomous-research-loop]] 추가
  - `wiki/concepts/context-engineering.md` — source_count 1→2, "자율 루프 컨텍스트 보호 3원칙" 섹션 추가 (`> run.log 2>&1` + `grep` 1줄 발췌 + 크래시 시에만 tail), 출처에 [[karpathy-autoresearch]] 추가
  - `wiki/index.md` — 통계 39→43 / 소스 15→16 / 엔티티 10→12 / 개념 11→12. 4개 카테고리 테이블에 행 추가, harness/context-engineering 행 갱신.
- **메모**: 이번 수집의 진짜 가치는 [[autonomous-research-loop]]를 위키의 새 지층으로 자리잡힌 것. **"단일 메트릭 + 시간 예산 + 단일 파일 + 무한 루프"** 4중 제약은 [[harness]] 개념을 극한으로 압축한 형태이며, 석근의 BI 자동화·개인 비서 AI 양쪽에 직접 이식 후보. 위키 자체는 메트릭 정의가 어려워 자율 루프 적용 전에 평가축을 먼저 정의해야 함을 본문에 명시.
- **후속 탐구**:
  1. macOS / MLX 포크 1종을 회사 맥북에서 실제 가동 → 1박 ~100실험 재현해보기
  2. nanochat 본 저장소 raw 보관 여부 결정 (별도 가치 검증 후)
  3. 위키 운영용 메트릭 후보(고정 질의 세트 정답률, 토큰/질의)를 3개월 운영하며 검증

---

## [2026-04-24] ingest | portfolio 커리어 자료 베이스 통합 수집

- **소스 (raw 신규 복사, 공개 자료만)**:
  - `raw/notes/portfolio/README.md` — portfolio 저장소 README
  - `raw/notes/portfolio/old-portfolio.md` — 시드 포트폴리오(22KB)
  - `raw/notes/portfolio/docs/**` — 3-Layer + Johnny.Decimal 구조 문서 미러 (총 47개 파일)
- **민감 자료 제외**: portfolio/private/ (Jira 22 + Confluence 10 + Google Drive 3)는 공개 GitHub 원격(`gsroot/llm-wiki`) 누출 방지를 위해 복사 제외. portfolio 저장소의 로컬 전용 폴더에만 보존.
- **수집 전략**: 계층적 — 개별 Jira/Confluence dump마다 source 페이지를 만들지 않고, 핵심 산출물(이력서·상세 포트폴리오·시드)과 프로젝트 통합 문서만 source 페이지로 요약. 세부 증거는 portfolio 내 `20-projects/*.md`의 `sources:` 필드에서 역추적 가능.
- **생성된 파일** (총 19개)
  - **소스 (8)**: `wiki/sources/portfolio-seed.md` · `portfolio-resume-ko.md` · `portfolio-ko.md` · `portfolio-method.md` · `c2spf-nft-market.md` · `c2spf-xpla-platform.md` · `c2spf-analytics-common.md` · `c2spf-analytics-renewal.md`
  - **엔티티 (4)**: `wiki/entities/seokgeun-kim.md` (위키 소유자) · `com2us-platform.md` (현 재직사) · `c2spf-analytics.md` (BI 서비스) · `xpla-platform.md` (블록체인 플랫폼)
  - **개념 (6)**: `wiki/concepts/backend-python-fastapi.md` · `frontend-react.md` · `data-pipeline-bigquery.md` · `devops-cicd.md` · `blockchain-xpla.md` · `ml-ai.md`
  - **종합 분석 (1)**: `wiki/syntheses/career-timeline-seokgeun.md` — 2016~2026 9년 커리어 타임라인, 4 패턴(역할 진화/스택 누적/정량 지표/회사+개인) 분석
- **업데이트된 파일**
  - `wiki/index.md` — 총 페이지 20→39, 소스 7→15, 엔티티 6→10, 개념 5→11, 종합 분석 1→2. 4개 카테고리 테이블에 19행 추가.
- **메모**: portfolio 저장소(3-Layer + Johnny.Decimal)와 llm-wiki(raw → sources → syntheses)는 같은 "원천 → 요약 → 종합" 패턴을 공유하므로 통합이 자연스러웠음. 향후 portfolio가 갱신되면 같은 source 페이지를 업데이트하는 방식으로 동기화 가능. 본 수집으로 LLM이 "내 커리어/프로젝트/스킬" 질의에 portfolio 저장소까지 가지 않고도 wiki 내에서 답변 생성 가능.

---

## [2026-04-16] ingest | Slash Commands vs Agent Skills 조사 수집 + RAG 가이드 재수집

- **소스 1 (신규)**: `raw/notes/slash-commands-vs-agent-skills.md` — 공식 문서(code.claude.com/docs/en/skills) 기반 조사·분석
- **소스 2 (업데이트)**: `raw/notes/using-llm-wiki-as-rag.md` — 방법 4를 "Slash Command"에서 "Agent Skill"로 승격, 새 소스 참조 추가
- **생성된 파일**:
  - `wiki/sources/slash-commands-vs-agent-skills.md` — 통합 경위, 기능 비교표, 위키 조회에 Skill이 유리한 4가지, frontmatter 핵심 필드, 호출 제어 매트릭스, 동적 context injection
- **업데이트된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 방법 4 전체 재작성(Agent Skill), 선택 매트릭스·인사이트·관련 링크 갱신
  - `wiki/entities/claude-code.md` — source_count 4→5, Skills 설명 보강(통합 경위·자동 호출·context:fork·paths·agentskills.io 표준), 출처 2건 추가
  - `wiki/index.md` — 총 페이지 19→20, 소스 6→7
- **raw/ 수정 참고**: `using-llm-wiki-as-rag.md`는 석근 본인+Claude 세션이 원저자인 메모이므로 업데이트를 허용. 외부 클리핑이었으면 불변 원칙 적용.
- **핵심 판단**: "어떤 도구든 Skills로 시작한다. 예외는 기존 commands 자산이 많아 이관 비용이 큰 경우뿐" — 이것이 이 조사의 결론이자 위키 전체의 새 운영 원칙

---

## [2026-04-16] setup | `wiki` Agent Skill 생성 (방법 4 구현)

- **작업**: [[using-llm-wiki-as-rag]]의 "방법 4"로 제안됐던 slash command를 **Agent Skill**로 승격하여 구현
- **생성된 파일**: `~/.claude/skills/wiki/SKILL.md` (Personal scope — 모든 프로젝트에서 자동 사용)
- **설계 결정**:
  - **Slash command가 아니라 Skill 선택**: 공식 문서 확인 결과 "Custom commands have been merged into skills"로 통합됐고 Skills가 권장됨. 자동 호출·supporting files·context:fork·paths 제한 등 Skill 전용 기능이 위키 조회에 특히 유용
  - **광범위한 description**: 초기 안은 "AI/LLM 질문"으로 좁혔으나, 개인 위키는 BI·업무·학습·독서·사이드 프로젝트 등 모든 주제로 확장될 예정이므로 description에 전 카테고리 열거
  - **"빈 조회" 방지 로직**: SKILL.md 1단계에서 `index.md` Read 후 관련 페이지 없으면 즉시 종료. Claude가 자동 호출해도 토큰 낭비 최소
  - **`context: fork` + `agent: Explore`**: 조회를 서브에이전트로 격리해 메인 세션 컨텍스트 오염 방지. [[harness]] 원칙 중 세션 분리 적용
  - **Personal scope 선택**: `~/.claude/skills/wiki/`에 두어 회사·개인 프로젝트 구분 없이 작동
- **업데이트된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 후속 과제 중 방법 4 완료 표시
- **의미**: 이 위키가 Claude Code의 네이티브 retrieval 경로로 **제품화**된 시점. 이제 어느 프로젝트에서든 `claude` 실행 후 관련 질문이 들어오면 자동으로 이 위키가 참조됨
- **후속 과제**:
  - 실사용하며 자동 호출의 정확도 관찰 → description 조정 여부 판정
  - 패턴이 쌓이면 `~/.claude/skills/wiki/query-patterns.md` supporting file 추가 검토
  - `context: fork` 비용이 과하다 싶으면 inline 모드로 전환 실험

---

## [2026-04-15] ingest | 이 위키를 Claude Code에서 RAG처럼 쓰는 법 (자기참조)

- **소스**: `raw/notes/using-llm-wiki-as-rag.md` (석근이 Claude Code 세션 대화 답변을 본인이 수집 대상으로 지정)
- **성격**: 자기참조적 수집 — 위키 운영 메타 문서. 이 위키의 활용법이 위키 자체의 한 페이지가 됨.
- **생성된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 5가지 통합 방법(디렉토리 실행 / 프로젝트 참조 / 명시적 로드 / slash command / MCP) + 선택 매트릭스
- **업데이트된 파일**:
  - `wiki/concepts/llm-wiki-pattern.md` — source_count 2→3, "RAG처럼 활용하기 (5단계)" 섹션 추가
  - `wiki/entities/claude-code.md` — source_count 3→4, 출처에 사용 가이드 추가
  - `wiki/concepts/mcp.md` — source_count 3→4, `.mcp.json` 예시 소스로 사용 가이드 추가
  - `wiki/index.md` — 총 페이지 18→19, 소스 5→6
- **후속 과제**:
  - 방법 4 구현: `~/.claude/commands/wiki.md` 실제 생성 (비용 대비 이득이 큼)
  - 방법 2 지원: 회사 프로젝트 CLAUDE.md 템플릿에 "참조 지식 베이스" 섹션 추가
  - qmd 도입 트리거 기준: 페이지 50개 또는 "index.md 읽는 데 5초 이상"
- **메모**: 수집하면서 확인된 것 — 이 위키는 이미 RAG 역할을 하고 있고, 18페이지 규모에서는 벡터 검색보다 index.md + Read가 오히려 빠르고 정확함. MCP 도입은 성급하지 않게.

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
