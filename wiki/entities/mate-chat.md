---
title: "Mate Chat"
type: entity
entity_type: project
tags: [mate-chat, side-project, personal, flutter, riverpod, fastapi, openai, websocket, oauth, in-app-purchase, sentry, prometheus, shadcn-ui-flutter, agent-skills, gstack, v1.0.0, 24회차]
related: [[flutter]], [[riverpod]], [[fastapi]], [[backend-fastapi-stack]], [[flutter-nextjs-fullstack-pattern]], [[shadcn-ui]], [[sentry]], [[prometheus]], [[openai-agents-python]], [[agent-skills]], [[seokgeun-stack-guide]], [[matechat-project-knowledge-map]]
source_count: 1
created: 2026-04-28
updated: 2026-04-28
---

# Mate Chat

## 개요

**Mate Chat**은 석근이 개발·운영하는 **글로벌 소셜 메시징 플랫폼** — v1.0.0 Google Play Store 출시 완료 (Android, 9개 언어 지원). 23회차에서 stub으로 등록됐고, 24회차에 raw 1차 수집(`/Users/sgkim/Projects/mate-chat/`)으로 정식 격상.

> 북극성 비전: **대화의 시작은 AI, 끝은 사람.** *(Start with AI. End with people.)*
> AI가 사람을 대체하는 것이 아니라, 사람과 사람의 연결을 가능하게 만드는 사회적 윤활제.

## 핵심 위상

본 위키에서 Mate Chat은 단순 사이드 프로젝트를 넘어 **위키 15~22회차 발견 도구의 종합 실증 사례**. [[seokgeun-stack-guide]] 6분류 카탈로그 권장 스택과 1:1 일치.

## 검증된 스택

### 백엔드 ([[fastapi]] + 6단 + 관측성 트리플)

| 도구 | 버전 | 위키 회차 |
|---|---|---|
| [[fastapi]] | 0.117.1+ | 15 |
| [[pydantic]] | 2.11.9 | 15 |
| [[sqlalchemy]] | 2.0.43 (async) | 15 |
| [[alembic]] | 1.16.5 | 15 |
| [[postgresql]] | 15 | 15 |
| [[redis]] | 5.0.1+ | 15 |
| [[uv]] | 사용 (pip 금지 명문화) | 15 |
| [[ruff]] | + black + isort + mypy | 15 |
| [[sentry]] | sentry-sdk[fastapi] 2.39 | 21 |
| [[prometheus]] | prometheus-client 0.20 | 21 |
| structlog | 25.4 | 21 |
| openai (Python) | 2.12+ | 17/18 |
| firebase-admin | 6.6 (FCM 푸시) | (신규) |
| boto3 | MinIO/S3 | (신규) |

### Flutter 모바일 ([[riverpod]] 단일 통합 + Sentry + shadcn_ui)

| 도구 | 버전 | 위키 회차 |
|---|---|---|
| [[flutter]] (Dart 3.10.1+) | stable | 22 |
| [[riverpod]] (flutter_riverpod) | 2.5.0 | 22 |
| [[shadcn-ui]] (shadcn_ui Flutter port) | 0.40.5 | 22 (진영 횡단) |
| sentry_flutter | 9.14 | 21 |
| go_router | 17.0 | (신규) |
| dio | 5.4 (HTTP) | (신규) |
| web_socket_channel | 2.4 | (신규) |
| hive | 2.2 (로컬 캐시) | (신규) |
| firebase_core/messaging/analytics | 3.x | (신규) |
| in_app_purchase | 3.2 | (신규) |
| google_sign_in / sign_in_with_apple | OAuth | (신규) |
| Pretendard 폰트 | 한국어 최적화 | (신규) |

### AI·결제·인프라

- OpenAI GPT-4 (커스텀 챗봇 + 하이브리드 채팅 @botname 멘션)
- Google Play / App Store IAP 검증 (`app-store-server-library`)
- Firebase FCM 푸시 (11개 언어 i18n)
- MinIO (S3 호환 스토리지, 프로필 이미지)
- Docker Compose (4 서비스: backend / postgres / redis / minio)

## 규모 (CLAUDE.md 기준 2026-04-23)

| 영역 | 수치 |
|---|---|
| 백엔드 API | 83 endpoints |
| 백엔드 PostgreSQL | 20 테이블 / 13 마이그레이션 |
| 백엔드 테스트 | 113 테스트 (커버리지 ~61%) |
| Flutter Dart | 132 파일 / 51,960줄 |
| 백엔드 docs | 18 설계 문서 |
| `.agents/skills/` | **38 SKILL.md** (단일 OSS 최대) |
| `.gstack/` | 27 슬래시 커맨드 |
| 국제화 | 9개 언어 ARB |

## 핵심 발견 (24회차)

### 1. 위키 발견의 종합 실증

[[seokgeun-stack-guide]]가 권장하는 6분류 도구 중 백엔드+데이터+LLM+운영+프론트 5분류가 단일 프로젝트에 적용. ML 클래식([[scikit-learn]] / [[lightgbm]])만 미적용 — 채팅 서비스 본질상 ML 클래식 부재는 정합적.

### 2. 38 SKILL.md = 단일 OSS 최대 규모

- Flutter 본진 3개 SKILL을 **19개로 fork·확장** (관리 상태 / 아키텍처 / 동시성 / 테스트 / 폼 / 국제화 / 라우팅 / HTTP·JSON / 캐싱 / DB / 테마 / 접근성 / 사이즈 / 임베딩 / 네이티브 API / 플러그인 / 홈 위젯 / 애니메이션 / 패턴)
- 도메인 SOP 15개: api-consistency / fastapi-testing / websocket-pattern / security-review / migration-safety / pre-deployment / feature-workflow / doc-management / skill-creator / theme-factory / ui-ux-pro-max / build-app-bundle / frontend-design / flutter-qa-audit / flutter-testing-apps
- Flutter 도구·환경 4개

→ 위키 ([[agent-skills]]) **13단계 진화 = "개인 사이드 프로젝트의 본진 fork·확장"** 후보.

### 3. AGENTS.md ↔ CLAUDE.md 분리형

22회차 Next.js의 symlink (수렴형)와 정반대. 본 프로젝트는:
- AGENTS.md (2.8KB, 협업자용 일반 가이드)
- CLAUDE.md (22KB, 상주 에이전트용 풍부 컨텍스트)
- GEMINI.md (3.5KB, 벤더 특화)

→ **에이전트 종류별 분리** = 13단계 진화 양분 (수렴 vs 분리) 가능성.

### 4. 27 gstack 슬래시 커맨드 = 자체 생산성 시스템

`/office-hours` `/plan-{ceo,eng,design}-review` `/ship` `/canary` `/qa` `/review` `/benchmark` `/document-release` 등 — 회사 운영 관행을 1인 사이드 프로젝트가 슬래시 커맨드로 패키지화. 이는 [[harness]] 6번째 축(PLANS.md ExecPlan)의 다음 단계 진화.

### 5. shadcn-ui 진영 횡단 (React → Flutter)

22회차 [[shadcn-ui]]의 "Open Code" 거버넌스 모델이 `shadcn_ui` Dart 패키지로 Flutter에 이식. **개인 프로젝트가 진영 횡단 채택의 첫 위키 사례**.

## 주요 기능 (CLAUDE.md 명시)

- **인증**: Google OAuth + 이메일/비밀번호 + JWT (액세스 7일 / 리프레시 6개월) + COPPA + 이메일 인증 (24h 만료) + 비밀번호 재설정 (1h 만료) + Welcome 보너스 200 클로버
- **소셜**: 팔로우 / 메이트(친구) 요청·수락·거절·취소 / 차단 / 신고 / 쿨다운 (메이트 24h, 팔로우 1h) / 양방향 메이트 관계
- **채팅**: 1:1 / 메이트 / 공개 채팅방 + WebSocket 실시간 + 타이핑 인디케이터 + 읽음 표시 + 다중 기기 + 채팅방 초대 + Redis Pub/Sub (분산 배포 준비)
- **AI 챗봇**: GPT-4 + 커스텀 봇 + 공개/비공개 + 클로버 사용량 추적 + **챗봇 메이트** (AI와 친구 관계) + 하이브리드 채팅 (@botname 멘션)
- **가상 화폐**: 클로버 / Welcome 200 (3일 만료) / Google Play+App Store IAP 검증 / 보너스·구매 분리 추적
- **알림**: REST API + FCM 푸시 (11개 언어) / 6 타입 (follow / mate_request / mate / invite / chat / force_exit)

## 운영 로드맵 (CLAUDE.md)

### v1.1 (단기)
1. Apple OAuth 구현 (iOS 출시 필수)
2. iOS 앱 빌드·App Store 제출
3. 콘텐츠 모더레이션 강화 (키워드 필터, 자동 제한)

### v1.2+ (중기)
4. Redis Pub/Sub 분산 배포 (다중 서버 WebSocket)
5. WebSocket DB 풀 최적화 (연결별 → 작업별 세션)
6. 리액션·답장 (채팅 UX)

## 알려진 제한사항

- Apple OAuth 미구현 → iOS 출시 시 필수
- Redis Pub/Sub 분산 배포 미구현 (단일 서버에서는 정상)
- iOS 앱 빌드·배포 대기
- WebSocket이 DB 풀 슬롯을 연결 수명 동안 점유 (pool_size 주의)

## 듀얼 프로젝트 구조

```
mate-chat/
├── mate_chat_backend/       # FastAPI, 70%+ 구현
├── mate_chat_flutter/       # Flutter, 출시 완료
├── docs/                    # 18 설계 문서 (12 system / 13 db / 14 api / 15 auth / 16 websocket 등)
├── .agents/skills/          # 38 SKILL.md
├── .gstack/                 # 27 슬래시 커맨드
├── AGENTS.md (2.8KB)        # 협업자용 가이드
├── CLAUDE.md (22KB)         # 에이전트용 컨텍스트
├── GEMINI.md (3.5KB)        # Gemini 별도 가이드
├── README.md (11KB)
└── skills-lock.json (4.4KB) # SKILL 잠금 파일
```

## 위치

- 저장소: private repo, 로컬 `/Users/sgkim/Projects/mate-chat/`
- raw 디렉토리: `raw/articles/seokgeun-mate-chat/` (24회차 수집 — README/AGENTS.md/CLAUDE.md/GEMINI.md/TODO.md/skills-lock.json + 38 SKILL.md + backend/{README,pyproject,3 docs} + flutter/{README,pubspec.yaml})
- 18회차 보완 자료: `raw/notes/mate-chat-wiki-2026-04-28/` (소비자 wiki 68 md 스냅샷)

## 관련 개념

- [[flutter]] / [[riverpod]] — 모바일 클라이언트
- [[fastapi]] / [[pydantic]] / [[sqlalchemy]] / [[alembic]] / [[postgresql]] / [[redis]] — 백엔드 6단
- [[uv]] / [[ruff]] — 도구 체인 (Astral)
- [[sentry]] / [[prometheus]] — 운영 트리플
- [[shadcn-ui]] — Flutter port 진영 횡단
- [[openai-agents-python]] — OpenAI 직접 통합 (SDK 미사용, 직접 API)
- [[agent-skills]] — 38 SKILL = 단일 OSS 최대 + 13단계 분리형 진화 후보
- [[backend-fastapi-stack]] — 15회차 6단의 직접 실증
- [[observability-and-cicd-stack]] — 21회차 운영 트리플의 직접 실증
- [[flutter-nextjs-fullstack-pattern]] — 22회차 Flutter 단일 통합 모델의 실증
- [[seokgeun-stack-guide]] — 6분류 권장 스택의 1:1 매칭 실증
- [[matechat-project-knowledge-map]] — 18회차 wiki 스냅샷 종합
- [[matechat-chat-analysis-module]] — 24회차 신규 종합 (T4 산출, 채팅 분석 7축 + BigQuery 파이프라인)

## 출처

- [[seokgeun-mate-chat]] — 24회차 1차 수집. README/AGENTS.md/CLAUDE.md(22KB)/GEMINI.md/TODO.md + .agents/skills/ 38 SKILL + backend pyproject.toml + Flutter pubspec.yaml + 백엔드 3 docs

## 메모

- **24회차 정식 격상**: 23회차 stub(추정 스택)이 100% 정확했음을 raw 수집으로 검증. 백엔드 6단 + 운영 트리플 + Flutter+Riverpod 모두 적용 확인.
- **위키 가설의 자기 검증**: [[seokgeun-stack-guide]]가 사이드 프로젝트 권장 스택을 제시했으나, **본인의 실제 운영 프로젝트가 그 권장 스택과 1:1 일치**한다는 사실은 가이드의 신뢰도를 강하게 뒷받침. 동시에 가이드가 외부 OSS 분석 결론이 아니라 본인 운영 경험의 사후 명문화일 가능성도 시사.
- **38 SKILL의 활용**: 한 번씩 1회독해 회사 BI 차용 가능 SOP 후보 식별 — fastapi-testing / api-consistency / websocket-pattern / security-review / migration-safety / pre-deployment / feature-workflow / doc-management / skill-creator 9개가 1순위.
- **사업화 우선·기능 후속 패턴**: 백엔드 70%·Apple OAuth 미구현 상태에서 Android 단일 플랫폼으로 v1.0.0 선출시. 컴투스플랫폼 BI 신규 기능 출시 의사결정에도 적용 가능 — "완성도 100%보다 사용자 검증 우선".
- **민감 정보 격리**: 환경변수 키 / Sentry DSN / Firebase 프로젝트 ID / Apple Team·Key ID / OAuth Client ID 등은 raw 원문에만 보관, 위키에는 필드 명만 인용.
- **23회차 stub 메모와의 차이**: 23회차에서 "BigQuery 파이프라인 (가설)"이라 적었으나 실제 raw에는 BigQuery 통합이 보이지 않음. 채팅 분석 모듈은 별도 형제 프로젝트(`mate-katok-analysis-{backend,flutter}`)에 분리됐을 가능성. T4 종합에서 추적.
- **형제 프로젝트 4개 발견** (`/Users/sgkim/Projects/` 트리): mate-chat / mate-katok-analysis-backend / mate-katok-analysis-flutter / mate_chat / mate_chat_cloud_functions. 본 entity는 메인 mate-chat만 다루고, 분석 모듈은 [[matechat-chat-analysis-module]]에서 정리.
