---
title: MateChat
type: entity
entity_type: project
aliases:
- MateChat
- 메이트챗
- mate-chat
- matechat
- 메트챗
- 매트챗
tags:
- matechat
- mate-chat
- AI
- fastapi
- flutter
- riverpod
- openai
- websocket
- iap
- clover
- side-project
- project-wiki
- sentry
- prometheus
- agent-skills
- gstack
related:
- '[[seokgeun-kim]]'
- '[[seokgeun-kim-profile-2026]]'
- '[[seokgeun-operating-profile-2026]]'
- '[[mate-chat-project-wiki-2026]]'
- '[[matechat-project-knowledge-map]]'
- '[[seokgeun-mate-chat]]'
- '[[seokgeun-matechat-validation]]'
- '[[backend-python-fastapi]]'
- '[[backend-fastapi-stack]]'
- '[[ml-ai]]'
- '[[flutter]]'
- '[[riverpod]]'
- '[[fastapi]]'
- '[[pydantic]]'
- '[[openai]]'
- '[[postgresql]]'
- '[[redis]]'
- '[[sqlalchemy]]'
- '[[alembic]]'
- '[[uv]]'
- '[[ruff]]'
- '[[sentry]]'
- '[[prometheus]]'
- '[[shadcn-ui]]'
- '[[agent-skills]]'
- '[[harness]]'
- '[[mcp]]'
- '[[claude-code]]'
- '[[seokgeun-stack-guide]]'
- '[[c2spf-analytics]]'
- '[[com2us-platform]]'
- '[[token-economy]]'
- '[[portfolio]]'
- '[[portfolio-seed]]'
- '[[llm-infra-meta-cluster]]'
- '[[portfolio-resume-ko]]'
- '[[portfolio-ko]]'
source_count: 6
observed_source_refs: 38
inbound_count: 193
created: 2026-04-28
updated: 2026-04-29
verification_required: true
last_verified: 2026-04-29
verification_notes: 현재 v1.0.0 출시 직전 QA 단계, QA 완료 후 Google Play 출시 예정. 39 SKILL 자작/외부 분류는 lock.json 재검증.
verification_procedure: Google Play Console에서 v1.0.0 출시 상태 확인 (QA 단계 → 정식 출시 → 다운로드 추이). raw/notes/matechat/INDEX.md의 최근 갱신일 비교. 변동 시 본 페이지 첫 callout 출시 상태 문구·last_verified 갱신 + matechat-launch-metrics-ledger 실측 ledger 추가.
cited_by_count: 73
---

# MateChat

> [!info] 4축 hub — 사이드 프로젝트
> AI 소셜 메시징. 39 SKILL.md 운영 SOP (자작 11 + 외부 28). FastAPI + Flutter + Riverpod + OpenAI + WebSocket. 회사 BI([[c2spf-analytics|c2spf 게임 데이터 BI]])와 "기술 스택 검증의 쌍"으로 동작. 자작 SKILL 9개가 c2spf 차용 후보. 출시 상태는 `verification_required: true`.
> 
> 한국어 표기: **메이트챗**(또는 메트챗·매트챗).

> [!tldr]
> **MateChat** = [[seokgeun-kim|석근]]의 사이드 프로젝트 AI 소셜 메시징 앱 (v1.0.0 QA 단계, Google Play 정식 출시 임박). 회사 BI(c2spf)와 "기술 스택 쌍 검증" 모델 동작.
> - **판단**: FastAPI + Flutter + Riverpod + OpenAI + WebSocket / 39 SKILL.md SOP / 페르소나·KPI·수익화 모델
> - **근거**: 자작 11 + 외부 28 = 39 SKILL 운영 / [[seokgeun-mate-chat]] 1차 수집 source / [[matechat-launch-metrics-ledger]] 실측 ledger
> - **히스토리**: 출시 상태 정정(QA 단계) / page_intent 분리 / `last_verified` 신선도 추적
> - **이 위키 맥락**: 4축 hub (inbound 172). 자작 SKILL 9개의 c2spf 역수입은 [[c2spf-analytics]] 검증 환경. RAG 답변 시 출시 상태는 `last_verified` 확인 필수.

## 언제 읽어야 하는가

- "MateChat은 무엇이고 현재 출시 상태는?" — 첫 callout(요약) 직행, `last_verified` 필드로 신선도 확인.
- "MateChat이 어떤 페르소나를 노리는가?" — "핵심 페르소나" 섹션.
- "MateChat 자작 SKILL이 c2spf로 역수입 가능한 후보는?" — "위키 발견의 종합 실증" 섹션 + [[c2spf-analytics|c2spf 게임 데이터 BI]] 본문 표.
- "MateChat KPI는 무엇이고 어떻게 측정하나?" — "KPI와 수익화" 섹션 + (P1-2 신설 예정 [[matechat-30day-validation-loop]]).
- "MateChat 출시·운영 리스크는?" — "리스크" 섹션.

## 개요

**MateChat**은 석근이 개발·운영하는 소셜+AI 하이브리드 모바일 서비스다. 제품 슬로건은 "대화의 시작은 AI, 끝은 사람." / "Start with AI. End with people."이며, 핵심 정체성은 **AI가 사람을 대체하는 앱이 아니라 사람과 사람의 연결을 돕는 앱**이다.

기존 AI 컴패니언 앱은 AI와의 관계 자체를 끝점으로 삼고, 기존 소셜/채팅 앱은 사용자가 어색함과 대화 시작의 부담을 직접 감당하게 만든다. MateChat은 그 사이에서 AI가 사회적 어색함을 완충하고, 최종적으로 실제 인간 대화를 만들도록 돕는 것을 목표로 한다.

이 페이지가 MateChat의 canonical 엔티티다. 과거 `mate-chat` slug는 raw 수집에서 생긴 중복 노드였고, 2026-04-28 정리에서 이 페이지로 병합했다.

## 주요 특징

### 제품 포지셔닝

- Character.AI/Replika의 더 좋은 버전이 아니다.
- Maum/Azar의 텍스트 버전도 아니다.
- Discord에 AI를 붙인 범용 채팅 앱도 아니다.
- 더 정확한 포지션은 **"AI 시대에 사람과 다시 연결되도록 돕는 앱"**이다.

### 핵심 페르소나

- 20대 후반~30대 대도시 거주자.
- ChatGPT, Character.AI, Replika 등과 긴 시간 대화하지만 실제 인간 친구를 만들고 싶은 사람.
- Tinder/Bumble은 부담스럽고, Discord 신규 그룹 진입은 어색하며, 직장 동료와는 거리감이 있는 사람.
- AI 대화 후 재미는 있지만 공허함을 느끼는 사람.

확장 페르소나는 외국 워홀러/이민자, 사회 불안이 있는 학생, 새 도시 이주자, 사람과 대화하고 싶지만 시작이 어려운 사람이다.

### 기술 스택

- **Backend**: [[fastapi]], Python 3.13, [[postgresql]] 15, [[redis]] 7, [[sqlalchemy]] 2.0 async, [[alembic]], [[pydantic]]
- **Mobile App**: [[flutter]], [[riverpod]], shadcn_ui Flutter port
- **AI**: [[openai]] GPT-4 계열 API
- **Storage/Infra**: MinIO, Redis, PostgreSQL, Docker Compose
- **Tooling**: [[uv]], [[ruff]], black, isort, mypy
- **Observability**: [[sentry]], [[prometheus]], structlog
- **주요 기능**: OAuth, JWT, WebSocket 실시간 채팅, AI 챗봇, 가상 화폐 클로버, IAP, FCM 푸시 알림

### 현재 상태

2026-04 기준 백엔드·Flutter 앱·인증·실시간 채팅·AI 챗봇·클로버·IAP·푸시 알림·다국어화 등 핵심 기능 대부분이 구현되어 있고, **현재 v1.0.0 출시 직전 QA 단계**다. QA 완료 후 Google Play Store에 정식 출시할 예정이며, App Store 배포는 이후 단계다.

따라서 다음 단계는 기능 추가보다 **closed alpha 또는 내부 테스트**다. 우선 단위는 1개 공개 채팅방, 1개 Mate-Bot, 10명 이내 사용자로 잡는 것이 현실적이다.

### 프로젝트 위키 스냅샷

`mate-chat/wiki`는 MateChat 전용 LLM-maintained wiki이며, 2026-04-28 스냅샷 기준 68개 마크다운 파일을 가진다. 구조는 `sources/` 19개, `entities/` 22개, `concepts/` 22개, `synthesis/` 2개와 메타 파일 3개다.

이 프로젝트 위키는 FastAPI 앱, Flutter 앱, WebSocket, Redis Pub/Sub, PostgreSQL, IAP, Clover, FCM, i18n, Google Play Store, 배포 파이프라인, 글로벌 출시 준비를 세부적으로 다룬다. `llm-wiki`에서는 이를 개별 페이지로 복제하지 않고, [[mate-chat-project-wiki-2026]] 원천 스냅샷과 [[matechat-project-knowledge-map]] 종합 분석으로 추적한다.

### 본진 raw 수집 결과

`/Users/sgkim/Projects/mate-chat/` 저장소의 README, AGENTS.md, CLAUDE.md, GEMINI.md, TODO.md, skills-lock.json, `.agents/skills/` 39개 SKILL.md, 백엔드 README/pyproject/docs, Flutter README/pubspec.yaml을 raw로 수집했다.

핵심 규모:

| 영역 | 수치 |
|---|---|
| 백엔드 API | 83 endpoints |
| PostgreSQL | 20 테이블 / 13 마이그레이션 |
| 백엔드 테스트 | 113 테스트, 커버리지 약 61% |
| Flutter Dart | 132 파일 / 51,960줄 |
| 백엔드 docs | 18 설계 문서 |
| `.agents/skills/` | **39 SKILL.md** (자작 11 + 외부 설치 28) |
| `.claude/skills/gstack/` | gstack 외부 저장소 vendor (자체 LICENSE/CLAUDE.md/package.json 포함) |
| `.claude/commands/` | 12개 자체 슬래시 커맨드 (api/commit/debug/deploy/explain/flutter/migrate/refactor/review/test-gen/test/ui) |
| `.gstack/` | 운영 로그 4개 파일 (browse-network.log/browse-console.log/qa-reports/) — 슬래시 커맨드 디렉토리 아님 |
| 국제화 | 9개 언어 ARB |

### 위키 발견의 종합 실증

MateChat은 [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]]가 정리한 백엔드 6단, Flutter+Riverpod 모바일, 관측성 트리플, OpenAI 통합, agent-skills 운영 패턴이 실제 개인 프로젝트에 적용된 사례다. 이 점에서 MateChat은 단순 사이드 프로젝트가 아니라, 이 위키가 수집한 기술 판단의 실증 프로젝트다.

검증으로 정확한 분포가 박혔다 — `.agents/skills/` 39 SKILL = **자작 11개 + 외부 설치 28개**:

- **자작 11개**: `api-consistency` / `fastapi-testing` / `websocket-pattern` / `security-review` / `migration-safety` / `pre-deployment` / `feature-workflow` / `doc-management` / `skill-creator` / `build-app-bundle` / `flutter-qa-audit`
- **외부 설치 28개**: Flutter 공식 22개 (`flutter/skills` GitHub, `skills-lock.json`에 hash 박힘) + Claude Code marketplace plugin / npx 설치 6개 (`flutter-artifacts-builder`, `flutter-patterns`, `flutter-testing`, `frontend-design`, `theme-factory`, `ui-ux-pro-max`)

이 분포가 [[c2spf-analytics|회사 BI]] 쪽으로 역수입할 후보를 정확히 좁힌다 — **자작 11개 중 mate-chat 도메인 특화 2개(`build-app-bundle`은 Android Flutter 전용, `flutter-qa-audit`는 Flutter QA 전용) 제외 9개가 c2spf 직접 적용 가능**. 9개 c2spf 적용 시나리오는 [[c2spf-analytics]] 본문 "MateChat 자작 SKILL → c2spf 역수입 후보" 표 참고.

→ 박힌 "38 SKILL = 단일 OSS 최대 규모, 메이저 OSS 4~12배 초과" 가설은 검증으로 부분 약화: **자작 11개로는 anthropics/skills(~12) / openai-agents-python(9) 자작과 비슷한 규모**. 진짜 가치는 **외부 28개 설치 + 자작 11개의 통합 운영 39개**라는 사이드 프로젝트로는 매우 인상적인 깊이.

### 주요 기능

- **인증**: Google OAuth, 이메일/비밀번호, JWT, COPPA, 이메일 인증, 비밀번호 재설정, Welcome 보너스 200 클로버
- **소셜**: 팔로우, 메이트 요청/수락/거절/취소, 차단, 신고, 쿨다운, 양방향 메이트 관계
- **채팅**: 1:1, 메이트, 공개 채팅방, WebSocket 실시간, 타이핑 인디케이터, 읽음 표시, 다중 기기, 채팅방 초대, Redis Pub/Sub
- **AI 챗봇**: GPT-4, 커스텀 봇, 공개/비공개 봇, 클로버 사용량 추적, 챗봇 메이트, 하이브리드 채팅 `@botname` 멘션
- **가상 화폐**: 클로버, Welcome 보너스, Google Play + App Store IAP 검증, 보너스/구매 분리 추적
- **알림**: REST API + FCM 푸시, 11개 언어, follow / mate_request / mate / invite / chat / force_exit 타입

### 운영 로드맵과 제한사항

단기 v1.1 후보는 Apple OAuth, iOS 앱 빌드·App Store 제출, 콘텐츠 모더레이션 강화다. 중기 v1.2+ 후보는 Redis Pub/Sub 분산 배포, WebSocket DB 풀 최적화, 채팅 리액션·답장이다.

알려진 제한사항:

- Apple OAuth 미구현은 iOS 출시 시 필수 차단 항목이다.
- Redis Pub/Sub 분산 배포는 다중 서버 WebSocket 운영 전 보강이 필요하다.
- WebSocket이 DB 풀 슬롯을 연결 수명 동안 점유하는 구조는 접속자 증가 시 병목이 될 수 있다.
- Android v1.0.0은 현재 출시 직전 QA 단계로, 출시 후 Play Console·배포 태그를 기준으로 운영 상태를 다시 추적해야 한다.

## 핵심 검증 질문

1. 외로운 AI 의존자 페르소나가 실제로 존재하는가?
2. 그들이 MateChat을 설치하고 계속 사용할 이유가 있는가?
3. AI가 사람 간 대화를 실제로 촉진하는가?
4. 첫 7일 안에 인간-인간 양방향 메시지 5회 이상이 발생하는가?
5. 사용자가 클로버에 돈을 낼 만큼 AI/소셜 경험에 가치를 느끼는가?

## KPI와 수익화

MateChat은 클로버라는 가상 화폐 기반 IAP 모델을 포함한다. AI 메시지 사용량, 클로버 소비, 유료 전환, 리텐션이 주요 수익 변수다.

현재 관점에서 수익은 후행 지표다. 먼저 확인해야 할 것은 제품이 실제로 유지율, 결제 사용자, 자연 확산을 만들어내는지 여부다.

중요 KPI:

- Paying user count 1,000명
- D30 retention 8%+
- Organic K-factor 0.3+
- 첫 7일 내 인간-인간 양방향 메시지 5회 이상 비율

## 리스크

- 기능 부족보다 사용자 검증 부족
- 출시 지연
- 마케팅/포지셔닝 미정
- 혼자 운영하면서 생길 수 있는 번아웃
- IAP 실제 검증, 개인정보처리방침/이용약관, 콘텐츠 모더레이션, 신고 처리, COPPA 13세 확인, 다국어 품질, 앱스토어 메타데이터 등 출시 전 최종 재확인 필요 항목
- 출시 후 사용자 확보·마케팅 단계가 본격 시작되지 않으면 "기능은 완성됐지만 쓰는 사람이 없는 앱" 위험

## 관련 개념

- [[ml-ai]]: OpenAI 기반 AI 챗봇과 AI→사람 연결 전략
- [[backend-python-fastapi]]: MateChat 백엔드의 기본 기술 축
- [[backend-fastapi-stack]]: FastAPI/Pydantic/SQLAlchemy/Alembic/PostgreSQL/Redis 6단의 직접 실증
- [[flutter]] · [[riverpod]]: 모바일 앱 구현 스택
- [[observability-and-cicd-stack]]: Sentry/Prometheus 운영 패턴
- [[agent-skills]]: 38 SKILL.md 기반 개인 프로젝트 SOP 체계
- [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]]: 이 위키의 기술 스택 판단과 MateChat 실제 스택의 연결
- [[token-economy]]: 클로버 기반 AI 사용량 과금과 LLM 비용 구조

## 출처

- [[seokgeun-kim-profile-2026]] — 제품 비전, 사업화 목표, KPI, 리스크, 육아휴직 기간 운영 계획의 1차 소스
- [[mate-chat-project-wiki-2026]] — 프로젝트 전용 위키 스냅샷. 구현, 아키텍처, 출시 준비, 운영 지식의 세부 소스
- [[seokgeun-mate-chat|석근 MateChat 본진 raw]] — MateChat 본진 저장소 raw 수집. README/AGENTS.md/CLAUDE.md/GEMINI.md/TODO.md, 38 SKILL.md, 백엔드/Flutter 메타 자료
- [[seokgeun-matechat-validation]] — 사업화·검증 1차 자료 (비전 / 구현 현황 2,084줄 / 출시 체크리스트 / 글로벌 출시 진단 / 경쟁 분석 / 매출 예측 702줄). KPI 4개와 1:1 매칭되는 정량 모델 + "Do Not Ship If" 출시 거버넌스
- [[portfolio-seed]] — 개인 프로젝트로서 Mate Chat 언급
- [[portfolio-resume-ko]] — 이력서의 Mate Chat 요약
- [[portfolio-ko]] — 상세 포트폴리오의 Mate Chat 기술 스택 요약

## 논쟁/모순

> [!warning] 논쟁/모순
> - **정합 완료**: 한때 [[mate-chat-project-wiki-2026]] source의 일부 raw 문서(`synthesis/implementation-status.md`)가 v1.0.0을 "Google Play Store 출시 완료"로 잘못 기록했으나, owner 자기보고로 **현재는 출시 직전 QA 단계임이 확정**됐다. [[seokgeun-kim-profile-2026]]의 "출시 직전" 표현이 정확하다. 본 위키의 모든 hub 표현을 "출시 직전 QA 단계, QA 완료 후 출시 예정"으로 통일.
> - IAP/푸시/법적 문서/모더레이션 등 출시 차단 가능 항목은 QA 단계에서 최종 확인 중이다. 실제 출시 전에는 mate-chat 저장소의 최신 코드와 Play Console 검수 상태로 재확인한다.

## 메모

- 단기 최우선은 "더 많은 기능"이 아니라 실제 사람 간 대화가 만들어지는지 확인하는 것이다.
- 포지셔닝 문장은 "AI 친구 앱"보다 "AI가 사람 친구를 만들어주는 앱" 쪽이 핵심 가설과 더 잘 맞는다.
- 사업화가 가족 시간 확보 전략과 직접 연결되어 있으므로, 운영 계획에는 개발뿐 아니라 마케팅·QA·지표 분석·번아웃 방지 루틴이 함께 들어가야 한다.
- `mate-chat` slug는 이 페이지로 병합 완료. 앞으로 새 링크는 `[[matechat]]`을 사용한다.

## 인용한 페이지 (cited_by)

- [[agent-skills]]
- [[alembic]]
- [[backend-fastapi-stack]]
- [[c2spf-ai-agent-adoption-candidates]]
- [[c2spf-analytics]]
- [[career-timeline-seokgeun]]
- [[claude-code]]
- [[com2us-platform]]
- [[crewai]]
- [[deepagents]]
- [[docker]]
- [[duckdb]]
- [[event-driven-architecture]]
- [[fastapi]]
- [[fastmcp]]
- [[flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[grafana]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[langchain]]
- [[langgraph]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[mate-chat-project-wiki-2026]]
- [[matechat-30day-validation-loop]]
- [[matechat-business-validation]]
- [[matechat-chat-analysis-module]]
- [[matechat-launch-metrics-ledger]]
- [[matechat-project-knowledge-map]]
- [[mcp]]
- [[nextjs]]
- [[openai-agents-python]]
- [[pandas-ai]]
- [[parental-leave-2026-operating-plan]]
- [[parquet]]
- [[polars]]
- [[portfolio]]
- [[portfolio-ko]]
- [[portfolio-method]]
- [[portfolio-resume-ko]]
- [[portfolio-seed]]
- [[postgresql]]
- [[prometheus]]
- [[pydantic]]
- [[pydantic-ai]]
- [[redis]]
- [[riverpod]]
- [[rrousselGit-riverpod]]
- [[ruff]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-kim-profile-2026]]
- [[seokgeun-mate-chat]]
- [[seokgeun-matechat-validation]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[sqlite]]
- [[tailwindcss]]
- [[tanstack-query]]
- [[uv]]
- [[zustand]]

## 인용한 페이지

- [[agent-sdk-comparison]]
- [[agent-skills]]
- [[alembic]]
- [[backend-fastapi-stack]]
- [[c2spf-ai-agent-adoption-candidates]]
- [[c2spf-analytics]]
- [[career-timeline-seokgeun]]
- [[chain-of-thought-prompting]]
- [[claude-code]]
- [[codex]]
- [[com2us-platform]]
- [[crewai]]
- [[deepagents]]
- [[docker]]
- [[duckdb]]
- [[event-driven-architecture]]
- [[fastapi]]
- [[fastmcp]]
- [[flutter]]
- [[flutter-nextjs-fullstack-pattern]]
- [[governance-axis-comparison]]
- [[grafana]]
- [[harness]]
- [[kafka]]
- [[kpi-recovery-loop]]
- [[langchain]]
- [[langgraph]]
- [[lightgbm]]
- [[llm-infra-meta-cluster]]
- [[mate-chat-project-wiki-2026]]
- [[matechat-30day-validation-loop]]
- [[matechat-business-validation]]
- [[matechat-chat-analysis-module]]
- [[matechat-launch-metrics-ledger]]
- [[matechat-project-knowledge-map]]
- [[mcp]]
- [[nextjs]]
- [[openai-agents-python]]
- [[openai-chatgpt-codex-guide]]
- [[pandas-ai]]
- [[parental-leave-2026-operating-plan]]
- [[parquet]]
- [[polars]]
- [[portfolio]]
- [[portfolio-ko]]
- [[portfolio-method]]
- [[portfolio-resume-ko]]
- [[portfolio-seed]]
- [[postgresql]]
- [[progressive-disclosure]]
- [[prometheus]]
- [[pydantic]]
- [[pydantic-ai]]
- [[rcif-prompt-pattern]]
- [[redis]]
- [[riverpod]]
- [[rrousselGit-riverpod]]
- [[ruff]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-kim-profile-2026]]
- [[seokgeun-mate-chat]]
- [[seokgeun-matechat-validation]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[shadcn-ui]]
- [[sqlalchemy]]
- [[sqlite]]
- [[tailwindcss]]
- [[tanstack-query]]
- [[uv]]
- [[vendor-neutral]]
- [[zustand]]
