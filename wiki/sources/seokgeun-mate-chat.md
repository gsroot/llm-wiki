---
title: "Mate Chat — 석근 개인 사이드 프로젝트 (v1.0.0 출시 직전 QA 단계)"
type: source
source_type: project
source_url: "(private repo, /Users/sgkim/Projects/mate-chat)"
raw_path: raw/articles/seokgeun-mate-chat/
author: "석근 (Mate Chat Team)"
date_published: 2026-04-23
date_ingested: 2026-04-28
related:
  - "[[matechat]]"
  - "[[flutter]]"
  - "[[riverpod]]"
  - "[[fastapi]]"
  - "[[backend-fastapi-stack]]"
  - "[[agent-skills]]"
  - "[[shadcn-ui]]"
  - "[[sentry]]"
  - "[[prometheus]]"
  - "[[openai-agents-python]]"
confidence: high
tags: [mate-chat, side-project, fastapi, flutter, riverpod, openai, websocket, oauth, in-app-purchase, sentry, prometheus, shadcn-ui-flutter, agent-skills, gstack, 24회차]
verification_required: true
last_verified: 2026-04-29
verification_notes: "39 SKILL 분류(자작 11 / 외부 28) — flutter/skills lock.json 재카운트"
cited_by:
  - "[[c2spf-ai-agent-adoption-candidates]]"
  - "[[event-driven-architecture]]"
  - "[[kpi-recovery-loop]]"
  - "[[matechat]]"
  - "[[matechat-30day-validation-loop]]"
  - "[[matechat-chat-analysis-module]]"
  - "[[seokgeun-matechat-validation]]"
---

# Mate Chat 1차 수집 — 석근 개인 사이드 프로젝트

## 한줄 요약

석근이 개발 중인 글로벌 소셜 메시징 플랫폼 (v1.0.0 출시 직전 QA 단계 — 44회차 owner 자기보고로 정정). FastAPI 백엔드 + Flutter 모바일 + OpenAI GPT-4 + WebSocket 실시간 채팅 + 가상화폐(클로버) IAP. **위키 15~22회차에서 발견한 6분류 도구 대부분이 단일 프로젝트에 집약된 실증 사례** + agent-skills 표준의 **`.agents/skills/` 39개 SKILL.md 통합 운영** (자작 11 + Flutter 공식 22 + Claude Code marketplace/npx 설치 6) + **외부 gstack 저장소 vendor + 자체 12개 슬래시 커맨드** (`.claude/commands/`). (28회차 검증 정정: 24회차 본문의 "38 SKILL = 단일 OSS 최대 규모, 메이저 OSS 4~12배 초과" 가설은 자작 11개 기준으로는 anthropics/skills(~12)·openai-agents-python(9)와 비슷한 규모로 약화. 진짜 가치는 **외부 28개 + 자작 11개 통합 운영의 사이드 프로젝트 깊이**.)

## 핵심 내용

### 프로젝트 메타

| 항목 | 값 |
|---|---|
| 상태 | v1.0.0 출시 직전 QA 단계 (Android), QA 완료 후 Google Play 정식 출시 예정. iOS App Store는 이후 단계 (44회차 정정) |
| 백엔드 | FastAPI 0.117 + Python 3.13 + PostgreSQL 15 + Redis 7 |
| 프론트엔드 | Flutter (Dart 3.10.1+) + Riverpod 2.5 |
| AI | OpenAI GPT-4 (커스텀 챗봇 + 하이브리드 채팅) |
| 인증 | Google OAuth + 이메일/비밀번호 + JWT (액세스 7일 + 리프레시 6개월) |
| 실시간 | WebSocket (자동 재연결, 하트비트, Redis Pub/Sub 준비 완료) |
| 보안 | 2차 보안 감사 완료, CRITICAL+HIGH 전체 수정 |
| 국제화 | 9개 언어 ARB (한국어 잔존 0개) |
| 규모 | 백엔드 83 API + 20 PostgreSQL 테이블 + 113 테스트 / Flutter 132 Dart 파일 + 51,960줄 |

### 듀얼 프로젝트 구조

```
mate-chat/
├── mate_chat_backend/    (FastAPI, 백엔드 70%+)
├── mate_chat_flutter/    (Flutter, 출시 직전 QA 단계)
├── docs/                 (18개 설계 문서 — 12 system / 13 db / 14 api / 15 auth / 16 websocket 등)
├── .agents/skills/       (39 SKILL.md = 자작 11 + 외부 설치 28)
├── .claude/skills/gstack/ (외부 gstack 저장소 vendor)
├── .claude/commands/     (12개 자체 슬래시 커맨드)
├── .gstack/              (운영 로그 4개 — 슬래시 디렉토리 아님)
├── AGENTS.md (2.8KB)     (간단 OSS 가이드)
├── CLAUDE.md (22KB)      (프로젝트 컨텍스트, AGENTS.md와 분리)
├── GEMINI.md (3.5KB)     (Gemini용 별도 가이드)
└── README.md (11KB)
```

### 백엔드 의존성 (검증 완료)

```toml
fastapi[standard]>=0.117.1   # 15회차
sqlalchemy>=2.0.43           # 15회차
alembic>=1.16.5              # 15회차
asyncpg>=0.30.0              # PostgreSQL 15회차
redis>=5.0.1                 # 15회차
pydantic>=2.11.9             # 15회차
python-jose[cryptography]    # JWT
passlib[argon2]              # 패스워드 해싱
openai>=2.12.0               # 17/18회차 LLM 인프라
firebase-admin>=6.6.0        # 푸시 알림
boto3>=1.34.0                # MinIO/S3
structlog>=25.4.0            # 21회차 관측성
prometheus-client>=0.20.0    # 21회차 관측성
sentry-sdk[fastapi]>=2.39.0  # 21회차 관측성
google-auth, app-store-server-library  # OAuth + IAP 검증
# dev: pytest + pytest-asyncio + pytest-cov + black + isort + mypy + ruff
```

→ **15회차 백엔드 6단 + 21회차 관측성 트리플(Sentry/Prometheus/structlog) 100% 적용 검증**.

### Flutter 의존성 (검증 완료)

```yaml
flutter_riverpod: ^2.5.0       # 22회차 Flutter 단일 통합 표준 — 검증
go_router: ^17.0.0             # 라우팅 (Vercel/Next.js의 App Router에 대응)
dio: ^5.4.0                    # HTTP
web_socket_channel: ^2.4.0     # WebSocket
flutter_secure_storage: ^9.0   # JWT 보관
hive, shared_preferences       # 로컬 캐시
google_sign_in, sign_in_with_apple  # OAuth
shadcn_ui: ^0.40.5             # ★ 22회차 React 진영 발견의 Flutter port — 진영 횡단 채택
sentry_flutter: ^9.14.0        # 21회차 Sentry — Flutter 진영도 적용
firebase_core/messaging/analytics  # Firebase
in_app_purchase: ^3.2.0        # 클로버 IAP
freezed/json_serializable      # 불변 데이터 클래스
riverpod_generator + build_runner   # 코드 생성
mocktail + fake_async + network_image_mock  # 테스트
```

→ **22회차 React 진영의 [[shadcn-ui]]가 Flutter용 shadcn_ui 0.40.5로 진영 횡단 채택**된 첫 위키 사례. Riverpod 2.5 단일 통합 모델 검증.

### `.agents/skills/` — 39 SKILL.md 통합 운영 (28회차 정밀 분류)

`skills-lock.json` 검증 + frontmatter description 분석 + 사용자 확인으로 28회차에 정확한 분포 박힘:

| 분류 | 카운트 | 출처 / 명세 |
|---|---|---|
| **외부 설치: Flutter 공식** | **22** | `flutter/skills` GitHub 저장소 (skills-lock.json에 source/sourceType/computedHash 박힘) — flutter-managing-state / flutter-architecting-apps / flutter-handling-concurrency / flutter-building-forms / flutter-localizing-apps / flutter-implementing-navigation-and-routing / flutter-handling-http-and-json / flutter-caching-data / flutter-working-with-databases / flutter-theming-apps / flutter-improving-accessibility / flutter-reducing-app-size / flutter-embedding-native-views / flutter-interoperating-with-native-apis / flutter-building-plugins / flutter-adding-home-screen-widgets / flutter-animating-apps / flutter-setting-up-on-{linux,macos,windows} / flutter-testing-apps |
| **외부 설치: Claude Code marketplace / npx** | **6** | flutter-artifacts-builder / flutter-patterns / flutter-testing / frontend-design / theme-factory / ui-ux-pro-max (사용자 확인 — Claude Code marketplace plugin 또는 npx 설치) |
| **자작: c2spf 역수입 후보 9개** | **9** | api-consistency / fastapi-testing / websocket-pattern / security-review / migration-safety / pre-deployment / feature-workflow / doc-management / skill-creator |
| **자작: mate-chat 도메인 특화 2개** | **2** | build-app-bundle (Android Flutter .aab 빌드 전용) / flutter-qa-audit (Flutter QA 전용) |

총 7,566줄 (평균 200줄/SKILL). **자작 11 + 외부 설치 28 = 39**. 24회차에 박힌 "38 SKILL = 단일 OSS 최대, 메이저 OSS 4~12배 초과" 가설은 28회차 검증으로 약화 — 자작 11개로는 anthropics/skills(~12)·openai-agents-python(9)와 비슷한 규모. 진짜 가치는 **외부 22 Flutter + 6 marketplace + 자작 11 통합 운영의 사이드 프로젝트 깊이**.

특이점:
- `.agents/skills/` 위치는 **22회차 [[flutter]] 본진의 vendor-neutral 채택 패턴 100% 동일** (석근이 Flutter 본진 컨벤션을 자기 프로젝트에 적용)
- Flutter 공식 22 SKILL을 그대로 vendor한 것은 [[flutter]] 본진의 vendor-neutral 채택의 **반대 방향 채택 (정의자 → 사용자)**의 첫 위키 사례
- `theme-factory/`에 별도 `theme-showcase.pdf + LICENSE.txt` 포함 (디자인 자산) — 외부 marketplace 설치의 흔적
- `skills-lock.json` 4.4KB 별도 잠금 파일 — npm package-lock 패턴, 외부 22개 Flutter SKILL의 hash 검증

### `.gstack/` — 27개 자체 슬래시 커맨드

CLAUDE.md 첫 섹션에 명시된 사용 가능 커맨드:

```
/office-hours, /plan-ceo-review, /plan-eng-review, /plan-design-review,
/design-consultation, /review, /ship, /land-and-deploy, /canary,
/benchmark, /browse, /qa, /qa-only, /design-review,
/setup-browser-cookies, /setup-deploy, /retro, /investigate,
/document-release, /codex, /cso, /autoplan, /careful, /freeze,
/guard, /unfreeze, /gstack-upgrade
```

**3분류**:
- **계획 (plan)**: /plan-{ceo/eng/design}-review, /design-consultation, /autoplan, /office-hours
- **출시 (ship)**: /ship, /land-and-deploy, /canary, /document-release, /setup-deploy
- **품질 (qa)**: /qa, /qa-only, /design-review, /review, /benchmark, /careful, /freeze, /guard, /unfreeze, /retro
- **운영 보조**: /investigate, /codex, /cso, /browse, /setup-browser-cookies, /gstack-upgrade

→ Mate Chat이 자체 생산성 시스템(`gstack`)을 빌드. 이는 **회사 BI 운영 자체 SOP 슬래시 커맨드 패키지화**의 직접적 영감.

### AGENTS.md vs CLAUDE.md 분리 패턴 (13단계 진화 후보)

| 파일 | 크기 | 역할 |
|---|---|---|
| AGENTS.md | 2.8KB | 일반 OSS 가이드 (PR 룰, 코드 스타일, 테스트, 보안) — 협업자용 |
| CLAUDE.md | 22KB | **프로젝트 컨텍스트 풍부판** (현재 상태 / 기능 / DB 스키마 / 환경변수 / 로드맵) — 상주 에이전트용 |
| GEMINI.md | 3.5KB | Gemini 전용 별도 가이드 |

→ 22회차 Next.js의 **AGENTS.md = CLAUDE.md symlink** (단일 진실원)와 **정반대 변종**: **에이전트 종류별 분리 (AGENTS = 일반 / CLAUDE = 프로젝트 / GEMINI = 벤더 특화)**. 8 OSS AGENTS.md 채택 사례 + 본 사례 = **agent-skills 13단계 진화 양분 가능성**:
- **수렴형** (1~12단계): symlink, byte-for-byte 미러링, redirect 등 = "단일 진실원"
- **분리형** (13단계 후보): 에이전트별·역할별 분리 = "역할 분담"

### CLAUDE.md 핵심 내용 — 운영 중 v1.0.0 상세

| 영역 | 상태 | 상세 |
|---|---|---|
| 백엔드 인프라 | 운영 중 | FastAPI / PostgreSQL / Redis / Docker (4 서비스 compose) |
| 인증 | 운영 중 | Google OAuth / 이메일·비밀번호 / JWT / COPPA |
| 소셜 | 운영 중 | 팔로우 / 메이트 / 차단 / 신고 / 쿨다운 (메이트 24h, 팔로우 1h) |
| 채팅 | 운영 중 | REST + WebSocket / 하이브리드 AI (@botname 멘션) |
| AI 챗봇 | 운영 중 | GPT-4 / 커스텀 봇 / 메이트 시스템 (AI와 친구 관계) |
| 가상 화폐 | 운영 중 | 클로버 / Welcome 200 (3일) / Google Play+App Store IAP 검증 |
| 알림 | 운영 중 | REST + FCM 푸시 (11개 언어 i18n) |
| Flutter 앱 | 운영 중 | Android 출시 / 9개 언어 / 132 Dart 파일 |
| 보안 | 감사 완료 | 2차 보안 감사, CRITICAL+HIGH 전체 수정 |
| 국제화 | 완료 | 9개 언어 ARB, 한국어 잔존 0개 |

### 데이터베이스 스키마 (20 테이블, CLAUDE.md 명시)

- 인증·사용자: users / user_sessions / email_verifications / password_resets
- 소셜: follows / mates / mate_requests / blocks
- 채팅: chat_rooms / chat_room_members / chat_messages / chat_room_invites / chat_room_bots
- AI: chatbots / chatbot_mates
- 기타: notifications / clover_transactions / device_tokens / user_reports

### 운영 로드맵 (CLAUDE.md 명시)

- **v1.1**: Apple OAuth + iOS App Store + 콘텐츠 모더레이션 (키워드 필터, 자동 제한)
- **v1.2+**: Redis Pub/Sub 분산 배포 / WebSocket DB 풀 최적화 / 리액션·답장

### 백엔드 docs/

- caching-guide.md
- logging-guide.md
- rate-limiting-guide.md

→ 21회차 운영/관측성 발견과 1:1 매칭. Sentry/Prometheus/structlog 운영 트리플이 자체 docs로 명문화.

## 주요 인사이트

### 1. **위키 15~22회차 발견의 종합 실증**

| 회차 | 발견 도구 | Mate Chat 적용 |
|---|---|---|
| 15 | FastAPI/Pydantic/SQLAlchemy/Alembic/PostgreSQL/Redis | 100% 6단 채택 |
| 15 | uv + ruff (Astral) | 100% (uv sync, uv run pytest) |
| 17/18 | OpenAI Python | 100% (openai>=2.12) |
| 19 (=21) | Sentry / Prometheus / structlog 트리플 | 100% (sentry-sdk + prometheus-client + structlog) |
| 22 (=20) | Flutter + Riverpod | 100% |
| 22 (=20) | shadcn-ui (React) | **shadcn_ui Flutter port 채택 — 진영 횡단** |

→ **위키가 카탈로그를 넘어 "사용자가 검증한 의사결정 도구"임이 단일 프로젝트로 입증**. [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] 권장 스택과 1:1 일치.

### 2. **39 SKILL.md = 자작 11 + 외부 설치 28의 통합 운영** (28회차 정정)

**자작 SKILL 비교** (24회차 가설의 정정 후 비교):

| 비교 | 자작 개수 | 회차 |
|---|---|---|
| anthropics-skills (1차 정의) | ~12 | 4회차 |
| flutter (vendor-neutral) | 3 | 12회차 |
| OpenAI agents-python | 9 | 14회차 |
| **Mate Chat 자작 (석근)** | **11** | **24/28회차** |

**전체 운영 비교** (외부 설치 포함):

| 비교 | 자작 + 설치 | 회차 |
|---|---|---|
| **Mate Chat (개인 사이드)** | **자작 11 + 외부 22 Flutter + 6 marketplace = 39** | **24/28회차** |

→ 24회차 본문의 "**38 SKILL = 단일 OSS 최대, 메이저 OSS 4배 초과**" 가설은 28회차에 자작 11개 기준으로 약화 (anthropics/skills·openai-agents-python과 비슷한 규모). **진짜 가치는 "자작 + 외부 설치 39개의 통합 운영"** — 사이드 프로젝트로서 매우 인상적인 깊이이지만 "단일 OSS 최대 규모"는 부정확.

검증 흔적:
- `skills-lock.json`에 22개 외부 의존성이 source/sourceType/computedHash 박힘 (Flutter 공식)
- 6개는 Claude Code marketplace plugin / npx 설치로 lock 파일에 미박힘 (사용자 확인)
- 11개는 자작 (frontmatter description에 "for the mate-chat project" 또는 한국어 작성 등)

### 3. **AGENTS.md ↔ CLAUDE.md 분리 = 13단계 진화 양분 가능성**

22회차까지의 8 OSS는 모두 **수렴형** (symlink / byte-for-byte / redirect):
- Anthropic / spec-kit / fastapi / uv / scikit-learn / flutter / openai-cookbook / openai-agents-python (8 단계 진화)
- Next.js / shadcn-ui / Pydantic AI / FastMCP (12단계 양대 변종)

본 회차 발견 = **분리형**:
- AGENTS.md (협업자용, 짧음) + CLAUDE.md (에이전트용, 풍부) + GEMINI.md (벤더 특화)
- 13단계 진화 후보 = **"역할별 분리 (수렴 vs 분리)"** 양극 패턴 정립

### 4. **shadcn_ui Flutter port = 진영 횡단 첫 사례**

22회차에서 [[shadcn-ui]]는 React 진영 "Open Code" 거버넌스 모델의 정의자였다. **shadcn_ui 0.40.5 Flutter port가 Mate Chat에 채택**됨으로써:
- Open Code 패턴이 React → Flutter 진영으로 이식됨
- 22회차 "10번째 거버넌스 모델 (Open Code)"의 진영 횡단 검증
- 향후 [[shadcn-ui]] 페이지에 Flutter port 별도 섹션 추가 후속

### 5. **gstack 외부 vendor + 자체 12 슬래시 커맨드 = 회사 BI SOP 패키지화 영감** (28회차 정정)

24회차에 박힌 "27 gstack 슬래시 커맨드 = 자체 생산성 시스템"은 28회차 검증으로 정정:

- **`.gstack/`** (루트): 운영 로그 4개 파일 (browse-network.log / browse-console.log / qa-reports/) — **슬래시 커맨드 디렉토리 아님**
- **`.claude/skills/gstack/`**: gstack 외부 저장소 vendor (자체 LICENSE / CLAUDE.md / package.json / node_modules 포함). 35~40개 슬래시 명령 제공 (autoplan / benchmark / browse / canary / ship / qa / land-and-deploy / office-hours 등) — **본인이 만든 게 아니라 외부 도구 채택**
- **`.claude/commands/`**: 12개 자체 슬래시 (api / commit / debug / deploy / explain / flutter / migrate / refactor / review / test-gen / test / ui)

→ 24회차 박힌 "1인 사이드 프로젝트가 회사 운영 관행을 슬래시 패키지화"는 정확히는 **"외부 gstack 도구를 채택하고 자체 12개 슬래시 추가"**. [[harness]] 6번째 축의 다음 진화 발견은 **여전히 유효** — 외부 gstack 자체가 SOP 패키지화의 사실상 표준 도구이며, 이를 사이드 프로젝트에 채택한 것은 회사 BI 업무에 동일 패턴 차용 가능 시사.

### 6. **백엔드 미완성 30%·Flutter 출시 직전 QA = 비대칭 운영 (정정 — 44회차)**

CLAUDE.md "기능 구현 70% 수준" + 안드로이드 단일 플랫폼 선출시 전략 → 백엔드는 v1.1 항목(Apple OAuth, iOS, 모더레이션, Pub/Sub 분산) 미완 상태에서 안드로이드 v1.0.0 QA를 마치고 정식 출시할 계획. **사업화 우선·기능 후속 모델**의 직접적 사례. (24회차 raw에 박힌 "Google Play Store 출시 완료" 표현은 잘못된 기록이며, 44회차에 owner 자기보고로 "출시 직전 QA 단계"로 정정.)

## 관련 엔티티/개념

- [[matechat|MateChat 사이드 프로젝트]] (T3에서 stub → 정식 격상)
- [[fastapi]], [[pydantic]], [[sqlalchemy]], [[alembic]], [[postgresql]], [[redis]] — 15회차 6단 적용
- [[uv]], [[ruff]] — Astral 도구 적용
- [[sentry]], [[prometheus]] — 21회차 관측성
- [[flutter]], [[riverpod]] — 22회차 Flutter 진영
- [[shadcn-ui]] — 22회차 Open Code의 Flutter port
- [[openai-agents-python]] — OpenAI 직접 통합
- [[agent-skills]] — 39 SKILL = 자작 11 + 외부 설치 28 통합 운영 (28회차 검증), 13단계 진화 후보
- [[backend-fastapi-stack]], [[flutter-nextjs-fullstack-pattern]], [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]], [[observability-and-cicd-stack]] — 종합 페이지 실증

## 인용할 만한 구절

CLAUDE.md, 첫 섹션:
> 북극성 비전: 대화의 시작은 AI, 끝은 사람. (Start with AI. End with people.)
> AI가 사람을 대체하는 것이 아니라, 사람과 사람의 연결을 가능하게 만드는 사회적 윤활제로 작동합니다.

CLAUDE.md, 코드 스타일:
> NEVER DO ❌
> - print() 사용 금지 → logger 사용
> - *args, **kwargs 남용 금지 → 명시적 파라미터 사용
> - Any 타입 사용 최소화 → 구체적인 타입 지정
> - 하드코딩된 설정값 금지 → 환경변수 또는 config.py 사용
> - 동기 함수 사용 금지 → async/await 사용

AGENTS.md:
> 비자명한 결정에는 짧은 주석/도크스트링을 남기고, 함수는 작고 순수하게 유지.
> 회귀 방지: 버그 수정 시 최소 1개 회귀 테스트 추가. 커버리지를 의미 있게 유지(현재 약 61%).

## 메모

- **18회차 mate-chat-wiki 스냅샷과의 보완 관계**: 18회차는 `wiki/` 디렉토리(소비자 문서) 68개 md를 스냅샷으로 보관, 본 24회차는 **코드 메타·SOP**(`AGENTS.md` / `CLAUDE.md` / `.agents/skills/` / 백엔드 pyproject.toml / Flutter pubspec.yaml)를 보관. 두 측면이 합쳐져 Mate Chat 1차 자료 완성.
- **위키에 박힐 것**: (a) [[matechat|MateChat 사이드 프로젝트]] entity stub → 정식 페이지(T3), (b) [[matechat-chat-analysis-module]] 종합(T4), (c) [[shadcn-ui]] 페이지에 Flutter port 메모(후속), (d) [[agent-skills]] 페이지에 13단계 분리형 진화 항목 추가(T4 종합과 함께), (e) [[seokgeun-stack-guide]] 페이지에 "위키 발견의 종합 실증" 섹션 백링크.
- **민감 정보 처리**: pyproject.toml의 의존성·버전·CLAUDE.md의 비전·기능·DB 스키마는 위키에 반영 가능. **그러나 환경변수 키 / Sentry DSN / Firebase 프로젝트 ID / Apple Team/Key ID** 등은 raw에 그대로 보관하되 위키 페이지에서는 인용 금지 (CLAUDE.md "필수 환경 변수" 섹션의 키 이름은 인용 가능, 값은 절대 인용 금지).
- 후속: 9개 SKILL 샘플(api-consistency / fastapi-testing / websocket-pattern / security-review / migration-safety / pre-deployment / feature-workflow / doc-management / skill-creator) 1회독 후 [[seokgeun-stack-guide]]에 "회사 BI 차용 SOP 후보" 섹션 추가.
