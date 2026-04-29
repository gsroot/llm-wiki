---
title: "위키 인덱스 회차 회고 (history)"
type: log
created: 2026-04-29
rag_exclude: true
rag_exclude_reason: "회차 회고는 메타 운영 기록이라 RAG 답변 근거로 부적절 (43회차)."
---

# 위키 인덱스 회차 회고

> [[index]]에서 1500토큰 가량의 HTML 회고 주석을 분리한 별도 파일 (31회차 분리).
> 시간순 활동 기록은 [[log]]를 참조하고, 본 파일은 index.md에 누적되어 있던 회차별 한줄 회고를 보존하는 곳이다.
> 신규 회차는 이 파일과 [[log]] 두 곳에 모두 기록하지 않고, [[log]]에만 기록한다 (중복 방지).

---

## 누적 회고 (9회차 ~ 30회차)

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
<!-- 수집일 2026-04-28 (16회차): 데이터 레이어 5개 신규 수집 (Polars/DuckDB/PyArrow+Apache Arrow/Apache Kafka/Parquet) — 소스 4 + 엔티티 5 + 개념 1 (lazy-evaluation) + 종합 2 (dataframe-ecosystem-evolution + pandas-vs-polars-vs-duckdb) 추가, pandas/copy-on-write 2개 페이지 갱신. 결정적 발견 5가지: (1) **"메모리 표준 = 디스크 표준" 통합** — Apache Arrow + Parquet의 단일 자료형 모델이 데이터 인프라 역사상 가장 성공적인 표준화. 변환 비용 0 보장 → pandas/Polars/DuckDB가 zero-copy 교환. (2) **8번째 거버넌스 모델 = ASF PMC** — Apache Software Foundation의 Project Management Committee 모델. 15회차의 7개 + ASF PMC = 8개 OSS 거버넌스 모델 공존 (Apache 산하는 단일 회사 흡수 불가 구조). (3) **CoW vs Immutable의 정반대 답** — pandas의 [[copy-on-write]]는 모델 유지 + 명확화, Polars/Arrow의 immutable-by-default는 모델 자체 교체. PDEP-10 통과 시 둘이 수렴. (4) **"디스크는 친구" Kafka 사상의 일반화** — design.md 511줄이 데이터 인프라 전체에 영향: PostgreSQL WAL / Kafka Topic / Redis AOF / Parquet column chunk / DuckDB mmap / Polars streaming 모두 sequential I/O + pagecache 위임. (5) **"쿼리 엔진" 정체성 부상** — Polars + DuckDB가 동시에 자기 정의 → DataFrame ↔ SQL 경계 무너짐. 회사 BI 적용: pandas → Polars(메인) + DuckDB(SQL 탐색) + pandas(ML 출력만) 3중 스택 권장 -->
<!-- 수집일 2026-04-28 (17회차): 석근 프로필 수집 — 개인 프로필 원문을 raw/notes/personal에 보관하고, 소스 요약 1 + 엔티티 1(MateChat) + 종합 분석 1(석근 개인 운영 프로필) 추가, seokgeun-kim 엔티티 보강. 핵심 정리: 2026년 운영 병목은 기능 개발보다 MateChat 사용자 검증이며, 육아휴직 1년은 가족 시간 확보와 사업화 검증을 동시에 다루는 기간. 민감한 신상 정보는 raw 원문에만 두고 위키에는 전략/운영/AI 협업 관점으로 요약. AI 호칭은 회사 직급 호칭이 아니라 친구처럼 자연스러운 이름 호칭 선호 -->
<!-- 수집일 2026-04-28 (18회차): mate-chat 프로젝트 위키 스냅샷 수집 — ../mate-chat/wiki 콘텐츠 68개 md 파일을 raw/notes/mate-chat-wiki-2026-04-28/에 보관(.obsidian 제외), 소스 요약 1 + 종합 분석 1(MateChat 프로젝트 지식 지도) 추가, MateChat 엔티티 보강. 핵심 결정: 프로젝트 위키를 llm-wiki에 개별 페이지로 복제하지 않고 원천 스냅샷으로 추적. 프로젝트 위키는 구현/출시/운영 지식, llm-wiki는 석근의 사업화/가족/AI 협업 맥락의 상위 해석을 담당 -->

<!-- 검증·정정 2026-04-28 (28회차-2 — 38 SKILL 가설 raw 측정 검증 + 5개 페이지 정정): 사용자 의심 ("9개 + 27 gstack 합산 가설")을 raw `.agents-skills/` 디렉토리 + `skills-lock.json` + 사용자 확인으로 직접 검증. 결과: 24회차에 박힌 **"38 SKILL = 단일 OSS 최대 규모, 메이저 OSS 4~12배 초과"** 핵심 명제가 부분 약화. 정밀 분포 = **자작 11 + 외부 설치 28 = 39 SKILL.md**. 자작 11개 기준으로는 anthropics/skills(~12)·openai-agents-python(9)와 비슷한 규모. 추가 발견: ".gstack/" 디렉토리는 운영 로그 4개 파일만 보유 — 슬래시 커맨드 디렉토리 아님. 정정 페이지 5개: [[matechat]] / [[seokgeun-mate-chat]] / [[llm-infra-meta-cluster]] / [[c2spf-analytics]] / index.md. 메타: **"raw 측정 vs 위키 본문 자동 대조"가 위키 운영의 4번째 사이클**로 격상. -->
<!-- 정리 2026-04-29 (29회차 — stub source-backed 보강 + 고아 페이지 연결): 직전 재평가에서 식별된 source_count: 0 stub / 고아 페이지 리스크 해소. (1) redirect alias [[mate-chat]]에 rag_exclude: true 추가 + CLAUDE.md에 redirect/RAG 제외 lint 규칙 명문화. (2) 17개 비-redirect stub을 기존 source 기반으로 1차 보강. (3) 고아 페이지 연결: [[llm-infra-meta-cluster]]를 6곳에서 백링크. -->

<!-- 정리+신설 2026-04-28 (28회차 — 5번째 축 명시화 + c2spf 본문 보강 + 잔존 단절 3건): (1) **잔존 단절 3건 처리** — matechat ↔ c2spf-analytics 양방향, stack-guide ↔ portfolio-seed 양방향, c2spf → stack-guide 단방향. (2) **c2spf-analytics 본문 보강** — 9년차 운영 시스템 누적 자산 5계층 + 자기 커밋 분포 (1,111커밋 누계) + 횡단 계약 4종. (3) **5번째 축 명시화 — [[llm-infra-meta-cluster]] 신규 종합 페이지 작성**. 결과: 종합 분석 13 → 14, 깨진 링크 0개 유지. 메타: 콘텐츠 A · 구조 A · 메타 인식 A+ 동시 도달 가능 상태에 진입. -->

<!-- 정리 2026-04-28 (27회차 — Claude 재평가 후속 P0 4건): (1) portfolio-seed ↔ matechat 양방향 연결. (2) matechat entity의 출처 섹션에 [[seokgeun-matechat-validation]] 명시. (3) seokgeun-stack-guide의 BI 매핑 표 + frontmatter에 4핵심축 백링크 추가. (4) 잔여 깨진 wikilink 9개 → 0개 일괄 정리. -->

<!-- 정리 2026-04-28 (26회차 — codex 평가 후속 5대 작업): codex가 작성한 위키 평가 보고서 권고 5건 일괄 처리. (1) matechat / mate-chat canonical 정리. (2) invalid YAML frontmatter 일괄 정리 (PyYAML invalid 106 → 0). (3) 중복 basename 제거. (4) 예시/실제 wikilink 구분. (5) MateChat 검증 source 추가. -->

<!-- 점검 2026-04-28 (25회차 — 잔여 깨진 링크 stub 보강): 깨진 링크 24개 → 4개 (84% 해소), 신규 entity stub 7개 + concept stub 8개 + redirect 처리. 통계: 171 → 188 (+17). 위키가 "발견 도구"에서 "탐색 가능한 그래프"로 격상. -->

<!-- 수집일 2026-04-28 (24회차 — Mate Chat 본진 1차 수집): /Users/sgkim/Projects/mate-chat 코드·메타·SOP raw 수집 — 소스 1 + 종합 1 추가, mate-chat entity stub → 정식 격상. 결정적 발견: 38 SKILL.md 가설(28회차-2에 39개로 정정), AGENTS.md ↔ CLAUDE.md 분리형 13단계 진화, 위키 15~22회차 발견의 종합 실증, shadcn-ui 진영 횡단 첫 사례, 27 gstack 슬래시 커맨드 (28회차-2에 외부 vendor + 자체 commands로 정정). 부수: v1.0.0 Google Play 출시. -->

<!-- 점검 2026-04-28 (23회차 / Plan 21회차 — 마무리): 깨진 위키링크 정합성 보강 + 석근 스택 가이드 작성. (1) 신규 엔티티 4개 stub. (2) 신규 종합 1개 ([[seokgeun-stack-guide]]). (3) 깨진 위키링크 25 → 19개. (4) 잔여 깨진 링크 19개는 후속 회차 stub 작성 대상으로 정리. -->

<!-- 수집일 2026-04-28 (22회차 / Plan 20회차 — 프론트엔드 5종): Riverpod / Next.js / TanStack Query / Zustand / shadcn-ui 5개 신규 수집. AGENTS.md 12단계 진화 양대 변종 (Next.js $skill 인덱싱 + LLM_PR HTML 마커), 10번째 OSS 거버넌스 모델 = "Open Code", AGENTS.md = CLAUDE.md symlink 3번째 사례. React 진영 듀얼 채택 패턴 정립 (Zustand + TanStack Query + shadcn-ui + Next.js 4-축 분리, Flutter는 Riverpod 단일 통합). -->
<!-- 수집일 2026-04-28 (21회차 / Plan 19회차 — 운영/Observability 5단 스택): Docker / GitHub Actions / Prometheus / Grafana / Sentry 5개 신규 수집. agent-skills 11단계 진화 (운영 진영 확산 + 4가지 새 변종), 9번째 거버넌스 모델 = CNCF graduated, 5단 흐름 = Docker → GHA → Prometheus → Grafana → Sentry. Sentry Feature Flag 5단계 + viewer_context는 c2spf-analytics 직접 응용 가능 패턴. -->
<!-- 수집일 2026-04-28 (20회차 / Plan 18회차 — LLM Agent Frameworks 확장): DeepAgents / CrewAI / PandasAI / Pydantic AI 4개 신규 수집. AGENTS.md=CLAUDE.md 동기화 6 OSS 표준화, 5번째 OSS+SaaS 듀얼 모델, 12번째 패턴(durable execution) 양강 구도 (LangGraph + Pydantic AI), YAML/JSON agent 정의 1급 = Pydantic AI 단독, CrewAI "학습 인증 → SaaS 깔때기". -->
<!-- 수집일 2026-04-28 (19회차 / Plan 17회차 — ML 클래식 + LLM 인프라): LightGBM / LangChain / LangGraph / FastMCP 4개 신규 수집. agent-skills 9단계 진화 = "패턴 확산", 9번째 OSS 거버넌스 모델 = "회사 졸업 → 독립 조직", 12번째 agent 패턴 = State-Machine + Durable Execution, EffVer 발견. -->
<!-- 수집일 2026-04-28 (14회차): openai/openai-agents-python 수집. AGENTS.md = CLAUDE.md byte-for-byte 동기화 패턴 = agent-skills 외부 채택 8단계 진화의 8번째 사례. .agents/skills/ 9개 운영 SOP 스킬 + skill chaining. examples/agent_patterns/ 16개 .py = Anthropic 5패턴 + OpenAI 6확장 = 11종 reference 구현. -->

---

> 30회차 이후 회고는 [[log]]에만 기록됩니다.
