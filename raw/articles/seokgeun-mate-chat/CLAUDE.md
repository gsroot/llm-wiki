# Claude 프로젝트 컨텍스트 - Mate Chat

## gstack

- 웹 브라우징은 항상 `/browse` 스킬을 사용하세요. `mcp__claude-in-chrome__*` 도구는 절대 사용하지 마세요.
- 사용 가능한 스킬: `/office-hours`, `/plan-ceo-review`, `/plan-eng-review`, `/plan-design-review`, `/design-consultation`, `/review`, `/ship`, `/land-and-deploy`, `/canary`, `/benchmark`, `/browse`, `/qa`, `/qa-only`, `/design-review`, `/setup-browser-cookies`, `/setup-deploy`, `/retro`, `/investigate`, `/document-release`, `/codex`, `/cso`, `/autoplan`, `/careful`, `/freeze`, `/guard`, `/unfreeze`, `/gstack-upgrade`
- gstack 스킬이 작동하지 않으면 `cd .claude/skills/gstack && ./setup`을 실행하여 바이너리를 빌드하고 스킬을 등록하세요.

## 프로젝트 개요

> **북극성 비전**: 대화의 시작은 AI, 끝은 사람. *(Start with AI. End with people.)*
> 자세한 근거는 [`docs/30-product-vision.md`](docs/30-product-vision.md) 참조.

**Mate Chat**은 실시간 통신과 AI 기반 대화를 가능하게 하는 글로벌 소셜 메시징 플랫폼입니다. AI가 사람을 대체하는 것이 아니라, 사람과 사람의 연결을 가능하게 만드는 사회적 윤활제로 작동합니다.

- **백엔드**: FastAPI (Python 3.13) + PostgreSQL + Redis
- **프론트엔드**: Flutter (Dart 3.10.1+)
- **실시간**: WebSocket 기반 메시징
- **AI**: OpenAI GPT-4 통합, 하이브리드 AI 채팅

## 현재 상태: v1.0.0 — Google Play Store 출시

| 영역 | 상태 | 상세 |
|------|------|------|
| 백엔드 인프라 | 운영 중 | FastAPI, PostgreSQL, Redis, Docker |
| 인증 시스템 | 운영 중 | OAuth (Google), 이메일/비밀번호, JWT, COPPA |
| 소셜 기능 | 운영 중 | 팔로우, 메이트, 차단, 신고 |
| 채팅 시스템 | 운영 중 | REST + WebSocket, 하이브리드 AI |
| AI 챗봇 | 운영 중 | GPT-4, 커스텀 봇, 메이트 시스템 |
| 가상 화폐 | 운영 중 | 클로버, IAP 검증 (Google Play / App Store) |
| 알림 | 운영 중 | REST API + FCM 푸시 (11개 언어 i18n) |
| Flutter 앱 | 운영 중 | Android 출시, 9개 언어 지원 |
| 보안 | 감사 완료 | 2차 보안 감사 완료, CRITICAL+HIGH 전체 수정 |
| 국제화 | 완료 | 9개 언어 ARB, 한국어 잔존 0개 |

---

## 핵심 기능

### 백엔드 인프라

- FastAPI 애플리케이션 구조
- 20개 테이블 PostgreSQL 데이터베이스
- Alembic 마이그레이션 (13개)
- Docker 컨테이너화 (4개 서비스)
- Redis 캐싱 및 Rate Limiting
- MinIO 객체 스토리지
- structlog 구조화 로깅
- Sentry 에러 추적

**파일 경로:**
- 앱 엔트리: `app/main.py`
- 설정: `app/core/config.py`
- 데이터베이스: `app/core/database.py`

### 인증 & 사용자

- **OAuth 2.0**: Google 완료, Apple 미구현 (iOS 출시 시 필요)
- **이메일/비밀번호 인증**: 회원가입, 로그인
- **이메일 인증**: 24시간 만료 토큰
- **비밀번호 재설정**: 1시간 만료 토큰, HTML 폼
- **JWT 토큰**: 액세스(7일) + 리프레시(6개월)
- 사용자 프로필 (공개/비공개 설정)
- 사용자 검색 및 탐색 (국가, 언어, 성별, 나이 필터)
- 프로필 이미지 업로드 (MinIO)
- Welcome 보너스: 이메일 인증 시 200 클로버

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/auth.py` (13개 API)
- 이메일 인증: `app/services/email_auth_service.py`
- 이메일 발송: `app/services/email_service.py`
- OAuth: `app/services/oauth_service.py`

### 소셜 기능

- 팔로우/언팔로우 시스템
- Mate(친구) 요청 시스템 (요청/수락/거절/취소)
- 차단 관리
- **쿨다운 시스템**: 메이트 24시간, 팔로우 1시간
- 양방향 Mate 관계 관리

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/social.py` (15개 API)
- 서비스: `app/services/social_service.py`

### 채팅 시스템

- 채팅방 CRUD (1:1/메이트/공개)
- **WebSocket 실시간 메시징**
- 타이핑 인디케이터
- 읽음 표시
- 사용자 접속 상태 추적
- 다중 기기 지원
- 채팅방 초대 시스템
- **하이브리드 AI 채팅**: 채팅방에 AI 봇 추가 가능
- 트리거 프리픽스 (@botname)
- 컨텍스트 윈도우 설정 (1-100 메시지)
- Redis Pub/Sub (구현 완료, 분산 배포 대기)

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/chats.py` (16개 API)
- WebSocket: `app/api/v1/endpoints/websocket.py`
- 서비스: `app/services/chat_service.py`
- 하이브리드 AI: `app/services/hybrid_chat_service.py`
- 연결 관리자: `app/websocket/manager.py`
- Pub/Sub: `app/websocket/pubsub.py`

### AI 챗봇

- OpenAI GPT-4 통합
- 커스텀 챗봇 생성 (이름, 설명, 시스템 프롬프트)
- 공개/비공개 챗봇
- 클로버 사용량 추적 (usage_count, paid_usage_count)
- **챗봇 메이트 시스템**: AI와 친구 관계 맺기
- 전용 1:1 AI 채팅방

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/chatbots.py` (13개 API)
- 서비스: `app/services/chatbot_service.py`

### 가상 화폐 - 클로버

- Welcome 보너스: 200 클로버 (3일 만료)
- 잔액 조회 및 거래 내역
- **인앱 결제 검증**: Google Play & App Store
- 보너스/구매 분리 추적

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/clover.py` (5개 API)
- 서비스: `app/services/clover_service.py`

### 알림 시스템

- 알림 CRUD API
- 읽지 않은 알림 카운트
- 일괄 읽음 처리
- 알림 타입: follow, mate_request, mate, invite, chat, force_exit

**파일 경로:**
- 엔드포인트: `app/api/v1/endpoints/notifications.py` (5개 API)
- 서비스: `app/services/notification_service.py`

### 인프라 & 보안

- **Rate Limiting**: Redis 기반, 60 req/min (글로벌), 10 req/min (인증)
- **구조화된 로깅**: structlog
- **Sentry 통합**: 에러 추적
- 미들웨어: Rate Limit, Metrics, Logging

**파일 경로:**
- Rate Limiter: `app/core/rate_limiters.py`
- 미들웨어: `app/middleware/`
- 보안: `app/core/security.py`

### 테스트 & 문서

- **113개 테스트 함수** (16개 파일)
- 테스트 커버리지 목표: 70%+
- API 문서 (Swagger/ReDoc)
- 18개 설계 문서

**파일 경로:**
- 테스트: `tests/` (2,544줄)
- 문서: `docs/`

---

## Flutter 프론트엔드

### 기술 스택

| 영역 | 기술 |
|------|------|
| Framework | Flutter (stable) |
| 언어 | Dart 3.10.1+ |
| 상태관리 | Riverpod 2.5.0 |
| 라우팅 | GoRouter 17.0.0 (딥링크 지원) |
| HTTP | Dio 5.4.0 |
| WebSocket | web_socket_channel 2.4.0 |
| 로컬 저장소 | Hive, FlutterSecureStorage |
| 테마 | Material Design 3 + shadcn/ui |
| 폰트 | Pretendard (한국어 최적화) |

### 프로젝트 구조

```
mate_chat_flutter/
├── lib/
│   ├── core/
│   │   ├── auth/          # 토큰 저장 및 관리
│   │   ├── network/       # API 클라이언트, JWT 인터셉터
│   │   ├── websocket/     # WsClient, 자동 재연결
│   │   ├── theme/         # AppColors, Typography, AppSpacing
│   │   ├── routing/       # GoRouter 설정, 30+ 라우트
│   │   └── utils/         # 유틸리티 함수
│   ├── features/
│   │   ├── auth/          # 로그인, 회원가입, 인증 (8개 페이지)
│   │   ├── chat/          # 채팅, 방 관리, 탐색 (9개 페이지)
│   │   ├── chatbot/       # AI 챗봇 (4개 페이지)
│   │   ├── social/        # 메이트, 팔로우 (3개 페이지)
│   │   ├── profile/       # 프로필 관리 (3개 페이지)
│   │   ├── home/          # 홈 대시보드
│   │   ├── settings/      # 설정, 차단 사용자
│   │   └── purchase/      # 인앱 결제
│   ├── repositories/      # API 연동 (7개)
│   ├── models/            # 데이터 모델
│   └── ui/components/     # 50+ 재사용 컴포넌트
├── android/
├── test/
└── pubspec.yaml

총: 132개 Dart 파일, 51,960줄 코드
```

### 구현된 기능

| 기능 | 상세 |
|------|------|
| 인증 | Google OAuth, 이메일/비밀번호, 인증/재설정 |
| 실시간 채팅 | WebSocket (자동 재연결, 하트비트, 메시지 큐) |
| 채팅방 관리 | 생성, 편집, 탐색, 초대, 정보 |
| 소셜 | 메이트, 팔로우, 프로필 보기/편집 |
| AI 챗봇 | 탐색, 대화, 메이트 관계 |
| 알림 | 알림 목록, 읽음 처리 |
| 설정 | 프로필 설정, 차단 사용자 관리 |
| 인앱 결제 | 클로버 구매 |
| 테마 | 다크/라이트 모드 |

### 주요 파일 경로

- 앱 엔트리: `lib/main.dart`, `lib/app.dart`
- 라우팅: `lib/core/routing/app_router.dart`
- API 클라이언트: `lib/core/network/api_client.dart`
- WebSocket: `lib/core/websocket/ws_client.dart`
- 인증 상태: `lib/features/auth/application/auth_notifier.dart`
- 채팅 페이지: `lib/features/chat/presentation/chat_page.dart`
- 테마: `lib/core/theme/app_colors.dart`

### WebSocket 구현

```dart
// 연결 URL
ws://[host]:8000/v1/ws/chat/{roomId}?token={jwt}

// 기능
- 자동 재연결 (지수 백오프: 1s, 2s, 4s, 8s, max 30s)
- 하트비트 (30초 간격)
- 오프라인 메시지 큐잉
- 상태 스트리밍 (connecting, connected, reconnecting, disconnected)
```

---

## 기술 스택

### 백엔드

| 영역 | 기술 | 버전 |
|------|------|------|
| 프레임워크 | FastAPI | 0.117.1+ |
| 언어 | Python | 3.11+ |
| 데이터베이스 | PostgreSQL | 15 |
| ORM | SQLAlchemy | 2.0.43+ (async) |
| 마이그레이션 | Alembic | 1.16.5+ |
| 캐시 | Redis | 7 |
| AI | OpenAI | 2.12.0+ |
| 로깅 | structlog | 25.4.0 |
| 모니터링 | Sentry | 2.39.0 |
| 패키지 관리자 | uv | - |

### DevOps

| 영역 | 기술 |
|------|------|
| 컨테이너화 | Docker & Docker Compose |
| 객체 스토리지 | MinIO (S3 호환) |
| CI/CD | 준비 중 |

---

## 프로젝트 구조 (백엔드)

```
mate-chat/
├── mate_chat_backend/
│   ├── app/
│   │   ├── api/v1/
│   │   │   ├── endpoints/
│   │   │   │   ├── auth.py        (13개 엔드포인트)
│   │   │   │   ├── users.py       (7개 엔드포인트)
│   │   │   │   ├── social.py      (15개 엔드포인트)
│   │   │   │   ├── chats.py       (16개 엔드포인트)
│   │   │   │   ├── websocket.py   (1개 엔드포인트)
│   │   │   │   ├── chatbots.py    (13개 엔드포인트)
│   │   │   │   ├── clover.py      (5개 엔드포인트)
│   │   │   │   ├── notifications.py (5개 엔드포인트)
│   │   │   │   ├── uploads.py     (1개 엔드포인트)
│   │   │   │   └── dev.py         (2개 엔드포인트)
│   │   │   └── router.py
│   │   ├── models/        (20개 SQLAlchemy 모델)
│   │   ├── schemas/       (10개 Pydantic 스키마)
│   │   ├── services/      (15개 서비스 클래스)
│   │   ├── repositories/  (6개 리포지토리)
│   │   ├── websocket/     (연결 관리자 + Pub/Sub)
│   │   ├── middleware/    (3개 미들웨어)
│   │   └── core/          (설정, 보안, 데이터베이스)
│   ├── migrations/        (13개 Alembic 마이그레이션)
│   ├── tests/             (113개 테스트, 16개 파일)
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── pyproject.toml
├── mate_chat_flutter/     (Flutter 앱)
├── docs/                  (18개 설계 문서)
└── CLAUDE.md

총: 83개 API 엔드포인트, 85% 완료
```

---

## 주요 구현 세부사항

### WebSocket 실시간 채팅

**파일:** `app/websocket/manager.py`, `app/api/v1/endpoints/websocket.py`

```python
# 연결 URL
ws://localhost:8000/v1/ws/chat/{room_id}?token={jwt}

# 메시지 타입
- message: 채팅 메시지 (DB 저장 + 브로드캐스트)
- typing: 타이핑 인디케이터 (브로드캐스트만)
- read: 읽음 표시 (브로드캐스트 + DB 업데이트)
- ping/pong: 하트비트
```

**기능:**
- 방별 활성 연결 추적
- 사용자-연결 매핑 (다중 기기)
- 방 멤버에게 메시지 브로드캐스트
- AI 트리거 감지 및 응답 (@botname 멘션)
- Redis Pub/Sub (분산 배포 준비)

### 하이브리드 AI 채팅

**파일:** `app/services/hybrid_chat_service.py`

일반 채팅방에 AI 봇을 추가하여 대화 가능:
1. 채팅방에 봇 추가 (트리거 프리픽스 설정)
2. 사용자가 "@봇이름" 으로 멘션
3. 최근 N개 메시지 컨텍스트 수집
4. OpenAI API 호출
5. AI 응답 저장 및 브로드캐스트

### 인증 흐름

**OAuth 로그인:**
1. 클라이언트에서 Google/Apple 토큰 획득
2. 백엔드에서 OAuth 토큰 검증
3. 데이터베이스에서 사용자 생성/조회
4. JWT 토큰 발급 (액세스 7일, 리프레시 6개월)

**이메일 로그인:**
1. 회원가입 시 이메일 인증 메일 발송
2. 인증 링크 클릭 → 이메일 인증 완료 + Welcome 보너스
3. 로그인 시 JWT 토큰 발급

**비밀번호 재설정:**
1. 재설정 요청 → 이메일 발송 (1시간 만료)
2. 링크 클릭 → HTML 폼에서 새 비밀번호 입력
3. 딥링크로 앱 복귀

---

## 데이터베이스 스키마

20개 테이블:

### 인증 & 사용자
- **users**: id, email, nickname, introduction, country_code, languages, tags, gender, age, profile_image_url, provider, provider_id, password_hash, email_verified, profile_visibility, notification_enabled, clover_balance, created_at, updated_at, deleted_at
- **user_sessions**: id, user_id, refresh_token, created_at, expires_at
- **email_verifications**: id, user_id, token_hash, expires_at, created_at
- **password_resets**: id, user_id, token_hash, used, expires_at, created_at

### 소셜
- **follows**: id, follower_id, following_id, created_at, unfollowed_at
- **mates**: id, user_id_a, user_id_b, created_at
- **mate_requests**: id, requester_id, target_id, status, created_at, updated_at
- **blocks**: id, blocker_id, blocked_id, created_at

### 채팅
- **chat_rooms**: id, name, description, type, image_url, tags, creator_id, manager_id, is_ai_room, primary_chatbot_id, created_at, updated_at, deleted_at
- **chat_room_members**: id, room_id, user_id, notification_enabled, last_read_at, joined_at, left_at
- **chat_messages**: id, room_id, sender_id, content, message_type, read_count, created_at
- **chat_room_invites**: id, room_id, inviter_id, invitee_id, status, created_at
- **chat_room_bots**: id, room_id, chatbot_id, trigger_prefix, context_window, is_active, created_at

### AI
- **chatbots**: id, name, description, instructions, model, is_public, profile_image_url, tags, creator_id, usage_count, paid_usage_count, created_at, updated_at, deleted_at
- **chatbot_mates**: id, user_id, chatbot_id, created_at

### 기타
- **notifications**: id, user_id, type, title, body, image_url, data, read_at, clicked_at, created_at
- **clover_transactions**: id, user_id, type, amount, reason, related_to, platform, created_at
- **device_tokens**: id, user_id, token, platform, created_at
- **user_reports**: id, reporter_id, target_id, reason, evidence_urls, status, created_at

---

## 운영 로드맵

### 단기 (v1.1)
1. **Apple OAuth 구현** — iOS App Store 출시 필수
2. **iOS 앱 빌드 및 배포** — App Store 제출
3. **콘텐츠 모더레이션 강화** — 키워드 필터, 자동 제한

### 중기 (v1.2+)
4. **Redis Pub/Sub 분산 배포** — 다중 서버 WebSocket
5. **WebSocket DB 풀 최적화** — 연결별 세션 → 작업별 세션
6. **리액션/답장 기능** — 채팅 UX 개선

---

## 개발 환경

| 항목 | 기술 |
|------|------|
| 언어 | Python 3.13+ |
| 패키지 관리자 | uv (pip 사용 금지!) |
| 린터 | ruff |
| 포매터 | ruff format |
| 타입 체커 | mypy |
| 테스트 | pytest + pytest-asyncio |

---

## 필수 명령어

**중요: `pip` 대신 항상 `uv`를 사용하세요.**

```bash
# 의존성 설치
uv sync

# 개발 서버 실행
cd mate_chat_backend
uv run uvicorn app.main:app --reload

# 테스트 실행
uv run pytest -x -v tests/

# 단일 테스트 파일
uv run pytest -x -v tests/test_auth.py

# 특정 테스트 함수
uv run pytest -x -v tests/test_auth.py::test_register

# 커버리지 포함 테스트
uv run pytest --cov=app --cov-report=term-missing

# 린트 & 포매팅
uv run ruff check .              # 린트 검사
uv run ruff check . --fix        # 자동 수정
uv run ruff format .             # 코드 포매팅

# 타입 체크
uv run mypy app/
uv run mypy .                    # 전체 체크
```

---

## 코드 스타일 규칙

### MUST DO ✅

- **타입 힌트**: 모든 함수에 타입 힌트 필수
- **Pydantic 모델**: request/response는 Pydantic 스키마로 정의
- **Async/Await**: async def 사용 (sync 함수 금지, 외부 라이브러리 제외)
- **에러 처리**: HTTPException으로 에러 처리
- **환경변수**: pydantic-settings로 관리 (app/core/config.py)
- **로깅**: structlog 사용

### NEVER DO ❌

- `print()` 사용 금지 → `logger` 사용
- `*args`, `**kwargs` 남용 금지 → 명시적 파라미터 사용
- `Any` 타입 사용 최소화 → 구체적인 타입 지정
- 하드코딩된 설정값 금지 → 환경변수 또는 config.py 사용
- 동기 함수 사용 금지 → async/await 사용

### 네이밍 규칙

| 대상 | 규칙 | 예시 |
|------|------|------|
| 함수/변수 | snake_case | `get_user_by_id()`, `user_id` |
| 클래스 | PascalCase | `UserService`, `ChatMessage` |
| 상수 | UPPER_SNAKE_CASE | `MAX_PAGE_SIZE`, `DEFAULT_LIMIT` |
| 파일 | snake_case.py | `chat_service.py`, `user_schema.py` |
| Pydantic 모델 | PascalCase | `UserCreate`, `ChatMessageResponse` |

### 코드 구조 패턴

```python
# ✅ Good: 타입 힌트 + async + 명시적 파라미터
async def get_user(
    user_id: int,
    db: AsyncSession
) -> User | None:
    return await db.get(User, user_id)

# ❌ Bad: 타입 힌트 없음 + sync 함수
def get_user(user_id, db):
    return db.query(User).filter(User.id == user_id).first()
```

---

## Git 워크플로우

### 브랜치 전략

- **main**: 프로덕션 브랜치
- **dev**: 개발 브랜치 (기본 작업 브랜치)
- **feature/기능명**: 새 기능 개발
- **fix/버그명**: 버그 수정
- **hotfix/긴급수정명**: 프로덕션 긴급 수정

### 커밋 메시지 규칙 (Conventional Commits)

```bash
feat: 새로운 기능 추가
fix: 버그 수정
docs: 문서 변경
style: 코드 포매팅 (기능 변경 없음)
refactor: 코드 리팩토링
test: 테스트 추가/수정
chore: 빌드, 설정 변경
```

**예시:**
```bash
feat: 채팅방 초대 API 추가
fix: WebSocket 재연결 로직 수정
docs: API 문서 업데이트
refactor: 인증 서비스 리팩토링
test: 소셜 기능 테스트 추가
```

### PR 생성 전 체크리스트

**필수 체크:**
```bash
# 1. 모든 테스트 통과
uv run pytest

# 2. 타입 체크 통과
uv run mypy .

# 3. 린트 체크 통과
uv run ruff check .
```

**PR 템플릿:**
- 변경 사항 요약
- 관련 이슈 번호
- 테스트 방법
- 스크린샷 (UI 변경시)

---

## 개발 워크플로우

### 백엔드 빠른 시작

```bash
cd mate_chat_backend
./docker-setup.sh   # Windows: docker-compose up -d
```

서비스:
- 백엔드: http://localhost:8000
- API 문서: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- MinIO: http://localhost:9001

### Flutter 개발

```bash
cd mate_chat_flutter
flutter pub get                  # 의존성 설치
flutter run                      # 앱 실행
flutter build apk                # Android 빌드
flutter test                     # 테스트 실행
```

### 코드 패턴

**백엔드:**
- Repository 패턴: 데이터 접근 계층
- Service 계층: 비즈니스 로직
- 의존성 주입: FastAPI Depends
- Async/Await: 논블로킹 I/O

**Flutter:**
- Feature-based 모듈 구조
- Repository 패턴: API 연동
- Riverpod: 상태 관리
- Freezed: 불변 데이터 클래스

---

## 필수 환경 변수

```bash
# 데이터베이스
DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/matechat
TEST_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/matechat_test

# Redis
REDIS_URL=redis://localhost:6379/0

# JWT
JWT_SECRET_KEY=your-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=10080    # 7일
REFRESH_TOKEN_EXPIRE_DAYS=180        # 6개월

# OAuth
GOOGLE_CLIENT_ID=your-google-client-id
APPLE_TEAM_ID=your-apple-team-id
APPLE_KEY_ID=your-apple-key-id

# OpenAI
OPENAI_API_KEY=your-openai-key

# 이메일 (SMTP)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your-email@gmail.com
SMTP_PASSWORD=your-app-password
EMAIL_FROM=your-email@gmail.com

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET_NAME=matechat

# Rate Limiting
RATE_LIMIT_PER_MINUTE=60

# 모니터링
SENTRY_DSN=your-sentry-dsn
LOG_LEVEL=INFO

# 앱 설정
APP_SCHEME=matechat://
BACKEND_URL=http://localhost:8000
CORS_ORIGINS=["http://localhost:3000"]
```

---

## 알려진 제한사항

- Apple OAuth 미구현 (iOS App Store 출시 시 필요)
- Redis Pub/Sub 분산 배포 미구현 (단일 서버에서는 정상 동작)
- iOS 앱 빌드 및 배포 대기
- WebSocket이 DB 풀 슬롯을 연결 수명 동안 점유 (pool_size 주의)

---

## 문서 링크

- 시스템 아키텍처: `docs/12-system-architecture.md`
- 데이터베이스 스키마: `docs/13-database-schema.md`
- API 설계: `docs/14-api-design.md`
- 인증 시스템: `docs/15-auth-system.md`
- WebSocket 설계: `docs/16-realtime-websocket.md`
- Docker 가이드: `mate_chat_backend/docs/docker-quick-reference.md`

---

**최종 업데이트:** 2026-04-02
**상태:** v1.0.0 Google Play Store 출시
**다음 마일스톤:** v1.1 — Apple OAuth + iOS App Store 배포
