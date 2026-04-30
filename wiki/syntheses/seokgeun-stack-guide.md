---
title: 석근 스택 가이드 — 마무리 종합
type: synthesis
category: hub
aliases:
- 석근 스택 가이드
- seokgeun-stack-guide
- 32 OSS 카탈로그
- 30분 부트스트랩
- stack-guide
sources:
- '[[backend-fastapi-stack]]'
- '[[dataframe-ecosystem-evolution]]'
- '[[agent-frameworks-matrix]]'
- '[[observability-and-cicd-stack]]'
- '[[flutter-nextjs-fullstack-pattern]]'
source_count: 5
observed_source_refs: 10
inbound_count: 144
related:
- '[[python]]'
- '[[fastapi]]'
- '[[pandas]]'
- '[[duckdb]]'
- '[[langgraph]]'
- '[[openai-agents-python]]'
- '[[flutter]]'
- '[[nextjs]]'
- '[[matechat]]'
- '[[seokgeun-kim]]'
- '[[c2spf-analytics]]'
- '[[com2us-platform]]'
- '[[portfolio]]'
- '[[portfolio-seed]]'
- '[[llm-infra-meta-cluster]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[mcp]]'
- '[[claude-code]]'
created: 2026-04-28
updated: 2026-04-29
tags:
- decision-tree
- side-project
- hub
verification_required: true
last_verified: 2026-04-29
verification_notes: '32 OSS 라이브러리 버전 + 새 도구 출현 (예: ty 정식 출시) — 분기별 재카탈로그'
verification_procedure: 32 OSS 카탈로그 라이브러리의 GitHub release 페이지 분기별 점검 (메이저 버전 변동·deprecated 신호·라이선스 변경). 신규 OSS 출현 시 6분류 카탈로그 진입 검토. 변동 시 OSS entity 페이지·본 페이지 카탈로그 표·last_verified 갱신.
cited_by_count: 60
---

# 석근 스택 가이드 — 마무리 종합

> [!info] 3축 hub — 스택 의사결정 트리
> 32 OSS 6분류 카탈로그 + 시나리오별 의사결정 트리 + 30분 부트스트랩. [[seokgeun-kim|석근 (이 위키 owner)]]의 9년 경험과 [[matechat|MateChat 사이드 프로젝트]]·[[c2spf-analytics|c2spf 게임 데이터 BI]] 양 프로젝트에서 검증된 스택만 수록. 새 프로젝트 시작 시 1-hop 진입점. OSS 버전·신규 도구 출현은 `verification_required: true`.
> 
> 한국어 표기: **석근 스택 가이드** 또는 **32 OSS 카탈로그**.

> [!tldr]
> **석근 스택 가이드** = 걸쳐 수집한 **32 OSS + 기존 8개**를 6분류 카탈로그 + 시나리오별 의사결정 트리 + 30분 부트스트랩 명령으로 재정리한 위키 3축의 단일 hub.
> - **판단**: 6분류(백엔드/프론트/데이터/관측성/AI/모바일) 진입점 / 시나리오 4종 의사결정 / 라이선스 주의 표
> - **근거**: 32 OSS entity 페이지 역참조 + 회사 BI(c2spf-analytics)·사이드(MateChat) 양 프로젝트 검증
> - **히스토리**: 마무리 종합 → 35 OSS entity 역참조 보강(+36%) → 상세 포트폴리오 cross-axis 인용 추가
> - **이 위키 맥락**: 3축 단일 hub (inbound 155). 신규 OSS 출현 시 분기별 재카탈로그(`verification_required: true`).

## 언제 읽어야 하는가

- "새 사이드 프로젝트를 30분 안에 시작하고 싶다" — "30분 부트스트랩 명령" 섹션 직행.
- "OSS 도구를 평가해야 하는데 어느 카테고리에 속하는가?" — 6분류 카탈로그 진입.
- "사이드와 회사 BI 양쪽에서 검증된 스택만 알고 싶다" — "회사 BI 적용 매핑" 섹션.
- "라이선스가 변동성 있는 OSS는 무엇인가?" — "라이선스 주의 표" 직행.
- "신규 OSS 출현이 카탈로그에 영향이 있나?" — `verification_required: true` (분기별 재카탈로그).

## 한줄 요약

걸쳐 수집한 32개 OSS + 기존 8개를 **6분류 카탈로그** + **시나리오별 의사결정 트리**로 재정리. 사이드 프로젝트(개인 비서, [[matechat|MateChat 사이드 프로젝트]] 등) 30분 부트스트랩과 회사 BI(컴투스플랫폼 게임 데이터) 적용 매핑 동시 제공.

## 6분류 카탈로그

### ① 백엔드 코어

| 도구 | 역할 | 라이선스 | 위키 |
|---|---|---|---|
| [[fastapi]] | 비동기 웹 프레임워크 | MIT | 핵심 |
| [[pydantic]] | 데이터 검증·직렬화 | MIT | 핵심 |
| [[sqlalchemy]] | ORM·SQL toolkit | MIT | 핵심 |
| [[alembic]] | DB 마이그레이션 | MIT | 핵심 |
| [[postgresql]] | RDBMS | PostgreSQL | 핵심 |
| [[redis]] | 캐시·메시지 브로커 | RSALv2/SSPL | 보조 |
| [[uv]] | 패키지·환경 관리 | Apache-2.0/MIT | 도구 |
| [[ruff]] | 린터·포매터 | MIT | 도구 |

→ **3축 백엔드 sub-hub**: [[backend-fastapi-stack]]

### ② 데이터 레이어

| 도구 | 역할 | 라이선스 | 위키 |
|---|---|---|---|
| [[pandas]] | 표준 dataframe | BSD-3 | Eager 표준 |
| [[polars]] | Lazy + Rust 가속 dataframe | MIT | 신표준 |
| [[duckdb]] | 임베디드 OLAP DB | MIT | SQL 기반 분석 |
| [[pyarrow]] | 컬럼 메모리 표준 | Apache-2.0 | 백엔드 |
| [[parquet]] | 컬럼 파일 포맷 | Apache-2.0 | 저장 |
| [[kafka]] | 분산 이벤트 스트리밍 | Apache-2.0 | 메시징 |

→ **종합 페이지**: [[dataframe-ecosystem-evolution]] + [[pandas-vs-polars-vs-duckdb]] 비교

### ③ ML 클래식 + 인프라

| 도구 | 역할 | 라이선스 |
|---|---|---|
| [[scikit-learn]] | 표준 ML 알고리즘 | BSD-3 |
| [[lightgbm]] | Gradient boosting (LightGBM Org) | MIT |

### ④ LLM 인프라 + 에이전트 프레임워크

| 도구 | 역할 | 라이선스 | 진영 |
|---|---|---|---|
| [[langchain]] | LLM 통합 (legacy `langchain` + 신규 `langchain_v1`) | MIT | LangChain Inc |
| [[langgraph]] | State-machine 에이전트 | MIT | LangChain Inc |
| [[fastmcp]] | MCP 서버 표준 (70% 점유) | Apache-2.0 | 단독 |
| [[openai-agents-python]] | OpenAI 공식 에이전트 SDK | Apache-2.0 | OpenAI |
| [[deepagents]] | LangGraph 위 멀티에이전트 (AGENTS.md 364줄) | MIT | LangChain Inc |
| [[crewai]] | 역할 기반 멀티에이전트 | MIT | crewAIInc |
| [[pandas-ai]] | 데이터 분석 에이전트 | MIT | sinaptik-ai |
| [[pydantic-ai]] | Pydantic 기반 에이전트 | MIT | Pydantic |

→ **비교 매트릭스**: [[agent-frameworks-matrix]] (8 프레임워크 × N 평가축)

### ⑤ 운영·CI/CD·관측성

| 도구 | 역할 | 라이선스 |
|---|---|---|
| [[docker]] | 컨테이너 런타임·이미지 | Apache-2.0 |
| [[github-actions]] | CI/CD 호스팅 | (SaaS) |
| [[prometheus]] | 메트릭 수집·시계열 DB | Apache-2.0 |
| [[grafana]] | 시각화·알림 | AGPL-3.0 |
| [[sentry]] | 에러·트레이스 추적 | BSL-1.1 → Apache-2.0 |

→ **종합 페이지**: [[observability-and-cicd-stack]]

### ⑥ 프론트엔드·모바일

| 진영 | 도구 | 역할 | 라이선스 |
|---|---|---|---|
| Flutter | [[flutter]] | 멀티플랫폼 UI SDK | BSD-3 |
| Flutter | [[riverpod]] | 단일 통합 상태관리 | MIT |
| React | [[nextjs]] | 풀스택 프레임워크 | MIT |
| React | [[zustand]] | 클라이언트 상태 | MIT |
| React | [[tanstack-query]] | 서버 상태 | MIT |
| React | [[shadcn-ui]] | UI 컴포넌트 (Open Code) | MIT |

→ **3축 프론트·모바일 sub-hub**: [[flutter-nextjs-fullstack-pattern]]

## 사이드 프로젝트 의사결정 트리

```
질문 1: 모바일 우선? 또는 웹 우선?
├─ 모바일 우선 → 시나리오 A (Flutter+Riverpod, mate-chat 패턴)
├─ 웹 우선 → 시나리오 B (Next.js+shadcn-ui+Zustand+TanStack Query)
└─ 둘 다 → 시나리오 C (단일 FastAPI 백엔드 + 듀얼 클라이언트)

질문 2: LLM 에이전트 필요?
├─ Y → ④ LangGraph 또는 OpenAI Agents SDK 선택
│   ├─ 멀티 에이전트 + 복잡 워크플로우 → LangGraph + DeepAgents
│   ├─ 단일 에이전트 + 간단 도구 → OpenAI Agents SDK
│   ├─ 데이터 분석 자동화 → Pandas AI
│   └─ 타입 안전 + 검증 우선 → Pydantic AI
└─ N → 단순 API + DB만으로 충분

질문 3: 분석 워크로드 비중?
├─ 작음 (사용자 입력 위주) → PostgreSQL만
├─ 중간 (수만~수십만 행) → DuckDB embedded
└─ 큼 (수백만+ 행, 컬럼 분석) → DuckDB + Parquet 파일 + (옵션) Polars

질문 4: 운영 단계?
├─ 프로토타입 → Docker Compose + Vercel free tier
├─ 베타 → + GitHub Actions CI + Sentry 무료
└─ 정식 → + Prometheus + Grafana + Kubernetes
```

## 30분 부트스트랩 명령

### 시나리오 B (웹 우선) — 추천

```bash
# 1. Next.js + TypeScript 프로젝트
pnpm create next-app@latest my-app --typescript --tailwind --app

# 2. UI 컴포넌트
cd my-app
pnpm dlx shadcn@latest init
pnpm dlx shadcn@latest add button card input form

# 3. 상태관리
pnpm add zustand @tanstack/react-query

# 4. 백엔드 (별도 디렉토리)
uv init backend && cd backend
uv add fastapi[standard] sqlalchemy alembic asyncpg pydantic-settings
uv add --dev pytest ruff
```

### 시나리오 A (모바일 우선, mate-chat 패턴)

```bash
flutter create my_app
cd my_app
flutter pub add flutter_riverpod riverpod_annotation
flutter pub add --dev riverpod_generator build_runner

# 백엔드는 시나리오 B의 backend 부분과 동일
```

## 회사 BI 적용 매핑 ([[com2us-platform|컴투스플랫폼]] / [[c2spf-analytics|c2spf 게임 데이터 BI]] — 사용 주체: [[seokgeun-kim|석근 (이 위키 owner)]])

| 영역 | 도구 | 적용 사례 |
|---|---|---|
| 분석 백엔드 | [[fastapi]] + [[duckdb]] | BigQuery 결과 캐시 + 사내 API |
| 대용량 분석 | [[polars]] (CPU) / [[duckdb]] (SQL) | 게임 로그 일배치 분석 |
| 컬럼 저장 | [[parquet]] + [[pyarrow]] | GCS 적재 표준 |
| 메시지 큐 | [[kafka]] | 실시간 이벤트 (장기) |
| 사내 대시보드 | [[nextjs]] + [[shadcn-ui]] | 게임 데이터 시각화 |
| 비동기 쿼리 표시 | [[tanstack-query]] | 30초+ BigQuery 캐시·refetch |
| 필터 클라이언트 상태 | [[zustand]] | 기간/게임/지표 필터 보존 |
| 모바일 알림 (가설) | [[flutter]] + [[riverpod]] | BI 임계치 알림 앱 |
| ML 클래식 | [[scikit-learn]] / [[lightgbm]] | 이탈 예측 모델 |
| LLM 분석 자동화 | [[pandas-ai]] / [[langgraph]] | 자연어 → SQL → 차트 파이프라인 |
| CI/CD | [[github-actions]] + [[docker]] | 컨테이너 빌드·배포 |
| 관측성 | [[grafana]] (가능하면 Sentry 추가) | 운영 BI 대시보드 자체 |

## 누적 메타 결론

| | 핵심 발견 |
|---|---|
| 15 | Astral(Ruff/UV)이 Rust로 Python 도구 체인 가속 — [[backend-fastapi-stack]] 6단 정리 |
| 16 | "디스크는 친구" 사상이 Kafka·Parquet·DuckDB의 공통 설계 — [[dataframe-ecosystem-evolution]] |
| 17 | LangChain "Agent Engineering Platform" 리브랜딩 + LangGraph AGENTS.md 등장 |
| 18 | 8 프레임워크 매트릭스 — DeepAgents AGENTS.md 364줄 (가장 긴 케이스) |
| 19 | AGENTS.md "Recent Learnings"·계층화·anti-fragmentation·Open Code = 11단계 진화 |
| 21 (=19) | 운영/Observability OSS 채택률 60% (양극화 가설) |
| 22 (=20) | Next.js의 `$skill` hub + LLM PR HTML 마커 = 12단계 진화 양대 변종 |
| 23 (=21) | 본 페이지 — 32개 OSS + 8개 기존을 6분류로 재정리 |

## 라이선스 주의 표

| 라이선스 | 위키 OSS | 상용 영향 |
|---|---|---|
| MIT / BSD / Apache-2.0 | 대다수 | 거의 없음 |
| **AGPL-3.0** | [[grafana]] | 변경 시 소스 공개 의무 — 사외 SaaS 제공 시 주의 |
| **BSL-1.1 → Apache-2.0** | [[sentry]] | 4년 후 자동 OSS — 신규 버전은 BSL |
| **RSALv2/SSPL** | [[redis]] (8.0+) | DBaaS 운영자 대상 — 자체 사용은 무관 |
| **PostgreSQL** | [[postgresql]] | MIT-like, 무관 |

## 위키 사용법 (마무리 메모)

1. **신규 도구 발견 시**: `wiki/index.md` → 카테고리 확인 → 비슷한 entity 페이지 1개 읽고 영향 추정
2. **의사결정 시**: 본 페이지의 의사결정 트리 → 시나리오 B/C → 30분 부트스트랩
3. **종합 비교 필요 시**: [[agent-frameworks-matrix]] / [[pandas-vs-polars-vs-duckdb]] / [[flutter-nextjs-fullstack-pattern]]
4. **회사 BI 적용 시**: 본 페이지 "회사 BI 적용 매핑" 표 + 라이선스 주의

## 관련 메타 운영 축

도구 선택 자체는 본 페이지가 담당하지만, LLM과 함께 일하는 운영 방식은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]가 담당한다. 신규 OSS나 프로젝트를 평가할 때는 **본 페이지로 도구 분류 → [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]로 agent-skills/harness/MCP/거버넌스 모델 위치 확인** 순서가 가장 안정적이다.

## 미래 작업

1. **[[matechat]] 1차 수집**: 저장소 노출 시 raw → source → entity 보강. 채팅 분석 모듈 7가지 축 별도 종합 페이지.
2. **6번째 사이클**: Web3/블록체인 / 결제 / 인증/SSO / 검색(Elastic/Meilisearch) 별도 카테고리 검토.
3. **AGENTS.md 13단계 모니터링**: Vercel 산하 다른 OSS (turbo, swr 등) + 다른 진영의 양대 변종 동시 채택 사례.
4. **점검 후속**: turbopack/radix-ui/tailwindcss/poimandres/tanstack 등 5개 stub 추가 작성.

## 출처

- [[backend-fastapi-stack]] — 백엔드 6단
- [[dataframe-ecosystem-evolution]] — 데이터 진화
- [[agent-frameworks-matrix]] — LLM 에이전트 비교
- [[observability-and-cicd-stack]] — 운영 5단
- [[flutter-nextjs-fullstack-pattern]] — 듀얼 클라이언트

## 인용한 페이지 (cited_by)

- [[agent-skills]]
- [[alembic]]
- [[backend-fastapi-stack]]
- [[c2spf-analytics]]
- [[career-timeline-seokgeun]]
- [[claude-code]]
- [[com2us-platform]]
- [[crewai]]
- [[deepagents]]
- [[docker]]
- [[duckdb]]
- [[fastapi]]
- [[fastmcp]]
- [[flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[github-actions]]
- [[grafana]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[langchain]]
- [[langgraph]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[matechat]]
- [[matechat-chat-analysis-module]]
- [[mcp]]
- [[nextjs]]
- [[openai-agents-python]]
- [[pandas]]
- [[pandas-ai]]
- [[parquet]]
- [[polars]]
- [[portfolio]]
- [[portfolio-seed]]
- [[postgresql]]
- [[prometheus]]
- [[pyarrow]]
- [[pydantic]]
- [[pydantic-ai]]
- [[rag]]
- [[redis]]
- [[riverpod]]
- [[ruff]]
- [[scikit-learn]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-mate-chat]]
- [[seokgeun-matechat-validation]]
- [[seokgeun-operating-profile-2026]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[tailwindcss]]
- [[tanstack]]
- [[tanstack-query]]
- [[uv]]
- [[zustand]]

## 인용한 페이지

- [[agent-skills]]
- [[alembic]]
- [[backend-fastapi-stack]]
- [[c2spf-analytics]]
- [[career-timeline-seokgeun]]
- [[claude-code]]
- [[com2us-platform]]
- [[crewai]]
- [[deepagents]]
- [[docker]]
- [[duckdb]]
- [[fastapi]]
- [[fastmcp]]
- [[flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[github-actions]]
- [[grafana]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[langchain]]
- [[langgraph]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[matechat]]
- [[matechat-chat-analysis-module]]
- [[mcp]]
- [[nextjs]]
- [[openai-agents-python]]
- [[pandas]]
- [[pandas-ai]]
- [[parquet]]
- [[polars]]
- [[portfolio]]
- [[portfolio-ko]]
- [[portfolio-method]]
- [[portfolio-resume-ko]]
- [[portfolio-seed]]
- [[postgresql]]
- [[prometheus]]
- [[pyarrow]]
- [[pydantic]]
- [[pydantic-ai]]
- [[rag]]
- [[redis]]
- [[riverpod]]
- [[ruff]]
- [[scikit-learn]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-mate-chat]]
- [[seokgeun-matechat-validation]]
- [[seokgeun-operating-profile-2026]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[tailwindcss]]
- [[tanstack]]
- [[tanstack-query]]
- [[uv]]
- [[zustand]]

