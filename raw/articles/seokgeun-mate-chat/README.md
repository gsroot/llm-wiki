# 🌍 Mate Chat

> **대화의 시작은 AI, 끝은 사람.**
> *Start with AI. End with people.*
>
> AI 시대의 친구 찾기 — AI가 어색함을 풀고, 사람이 당신의 친구가 됩니다.
> 자세한 비전은 [`docs/30-product-vision.md`](docs/30-product-vision.md) 참조.

[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393?logo=fastapi)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.13+-blue?logo=python)](https://www.python.org)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-336791?logo=postgresql)](https://www.postgresql.org)

## ✨ 주요 기능

### 🔐 인증

- OAuth 2.0 (Google, Apple)
- JWT 기반 세션 (HS256)
- 리프레시 토큰 로테이션

### 👥 소셜 기능

- 공개/비공개 사용자 프로필
- 팔로우/언팔로우 시스템
- "Mate" 친구 요청 시스템
- 차단 관리

### 💬 실시간 채팅

- **WebSocket** 실시간 메시징
- 타이핑 인디케이터
- 읽음 표시
- 그룹 채팅방
- 채팅방 초대

### 🤖 AI 챗봇

- **OpenAI GPT-4** 기반 커스텀 AI 챗봇
- 성격 커스터마이징
- 공개/비공개 챗봇
- 가상 화폐(클로버) 사용량 추적

---

## 🏗️ 아키텍처

```
mate-chat/
├── flutter-test.sh             # Flutter 테스트 실행 스크립트
├── mate_chat_backend/          # FastAPI 백엔드
│   ├── app/
│   │   ├── api/v1/             # API 엔드포인트
│   │   ├── models/             # SQLAlchemy 모델 (20개 테이블)
│   │   ├── schemas/            # Pydantic 스키마
│   │   ├── services/           # 비즈니스 로직
│   │   ├── repositories/       # 데이터 접근 계층
│   │   ├── websocket/          # WebSocket 관리자
│   │   └── core/               # 설정, 보안, 데이터베이스
│   ├── migrations/             # Alembic 마이그레이션
│   └── tests/                  # 113개 테스트 함수
├── mate_chat_flutter/          # Flutter 모바일 앱
│   ├── lib/                    # 앱 소스 코드
│   └── test/                   # Flutter 테스트
└── docs/                       # 문서
```

### 기술 스택

**백엔드:**

- FastAPI 0.104+
- Python 3.13
- PostgreSQL 15
- Redis 7
- SQLAlchemy 2.0 (async)
- Alembic (마이그레이션)

**AI & ML:**

- OpenAI GPT-4 API

**DevOps:**

- MinIO (S3 호환 스토리지)
- uv (패키지 매니저)

---

## 🚀 빠른 시작

### 필수 요구사항

| 도구 | 버전 | 용도 |
|------|------|------|
| Python | 3.13+ | 백엔드 |
| uv | 최신 | Python 패키지 매니저 |
| Flutter | stable (3.10.1+) | 모바일 앱 |
| Android Studio | 최신 | Android 개발 및 에뮬레이터 |

### 1. 저장소 클론

```bash
git clone https://github.com/yourusername/mate-chat.git
cd mate-chat
```

---

### 2. 백엔드 설정

#### 2-1. Python 패키지 매니저 (uv) 설치

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

#### 2-2. 가상환경 및 의존성 설치

```bash
cd mate_chat_backend

# 가상환경 생성
uv venv

# 가상환경 활성화
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows

# 의존성 설치
uv pip install -e ".[dev]"
```

#### 2-3. 환경 변수 설정

```bash
# 환경 변수 템플릿 복사
cp .env.example .env
```

`.env` 파일을 편집하여 필요한 값들을 설정:

```bash
# 필수 설정
JWT_SECRET_KEY=your-secure-secret-key    # 프로덕션에서는 반드시 변경

# 선택 설정 (기능별로 필요시)
GOOGLE_CLIENT_ID=xxx                      # Google OAuth 사용시
OPENAI_API_KEY=sk-xxx                     # AI 챗봇 사용시
SMTP_USER=xxx                             # 이메일 인증 사용시
SMTP_PASSWORD=xxx                         # 이메일 인증 사용시
```

#### 2-4. 지원 서비스 준비

백엔드는 로컬 `uvicorn` 프로세스로 실행합니다. PostgreSQL, Redis, MinIO는 로컬 설치 또는 외부 호스트/컨테이너로 준비하고, `mate_chat_backend/.env`에 접속 정보를 직접 설정하세요.

예시:

```bash
POSTGRES_SERVER=localhost
POSTGRES_PORT=5432
REDIS_URL=redis://localhost:6379/0
MINIO_ENDPOINT=localhost:9000
```

#### 2-5. 데이터베이스 마이그레이션

```bash
# 마이그레이션 실행
alembic upgrade head
```

#### 2-6. 백엔드 서버 시작

```bash
uvicorn app.main:app --reload
```

**서비스 URL:**

| 서비스 | URL |
|--------|-----|
| 백엔드 API | http://localhost:8000 |
| API 문서 (Swagger) | http://localhost:8000/docs |
| API 문서 (ReDoc) | http://localhost:8000/redoc |
| PostgreSQL | localhost:5432 |
| Redis | localhost:6379 |
| MinIO Console | http://localhost:9001 |

---

### 3. Flutter 앱 설정

#### 3-1. 의존성 설치

```bash
cd mate_chat_flutter
flutter pub get
```

#### 3-2. 코드 생성 (선택)

모델 파일을 수정한 경우에만 필요:

```bash
dart run build_runner build --delete-conflicting-outputs
```

#### 3-3. 앱 실행

**Android Studio에서 실행:**

1. Android Studio에서 `mate_chat_flutter` 폴더 열기
2. Run/Debug Configurations 설정
3. Additional run args에 다음 추가:

```
--dart-define=API_BASE_URL=http://10.0.2.2:8000/v1
```

> `10.0.2.2`는 Android 에뮬레이터에서 호스트 머신의 localhost를 가리킵니다.

**CLI에서 실행:**

```bash
cd mate_chat_flutter
./scripts/run_android.sh --api-base-url http://10.0.2.2:8000/v1
```

직접 `flutter run`을 사용해도 되지만, 릴리즈/스테이징에서는 define 누락을 막기 위해 스크립트 사용을 권장합니다.

**실제 기기에서 실행:**

호스트 머신의 IP 주소를 사용:

```bash
cd mate_chat_flutter
./scripts/run_android.sh --api-base-url http://192.168.x.x:8000/v1
```

**스테이징/프로덕션 Sentry 포함 실행:**

```bash
cd mate_chat_flutter
./scripts/run_android.sh \
  --mode release \
  --api-base-url https://api.example.com/v1 \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment staging
```

**Android App Bundle 빌드:**

```bash
cd mate_chat_flutter
./scripts/build_appbundle.sh \
  --version 1.0.0+10 \
  --update-pubspec \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment production
```

---

### 4. 설정 체크리스트

**백엔드:**
- [ ] PostgreSQL, Redis, MinIO 접속 정보가 `mate_chat_backend/.env`에 올바르게 설정됨
- [ ] `mate_chat_backend/.env` 파일 확인 및 필수 값 설정
- [ ] http://localhost:8000/docs 접속 확인

**Flutter 앱:**
- [ ] `flutter pub get` 실행
- [ ] `mate_chat_flutter/scripts/run_android.sh --dry-run` 으로 define 확인
- [ ] 에뮬레이터 또는 실제 기기에서 앱 실행

**테스트:**
- [ ] 백엔드 테스트: `cd mate_chat_backend && uv run pytest`
- [ ] Flutter 테스트: `./flutter-test.sh`

### Git에 포함된 파일 (별도 설정 불필요)

| 파일 | 설명 |
|------|------|
| `google-services.json` | Firebase/Google 서비스 설정 |
| Pretendard 폰트 | 한국어 최적화 폰트 |
| `.freezed.dart`, `.g.dart` | 생성된 Dart 코드 |

---

## 📖 API 문서

### 인터랙티브 문서

- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### 엔드포인트 개요

| 카테고리      | 엔드포인트 수 | 설명                        |
| ------------- | ------------- | --------------------------- |
| 인증          | 3             | OAuth, JWT 토큰, 로그아웃   |
| 사용자        | 5             | 프로필, 검색, 이미지 업로드 |
| 소셜          | 7             | 팔로우, Mate 요청, 차단     |
| 채팅 (REST)   | 7             | 방, 메시지, 초대            |
| **WebSocket** | 1             | **실시간 메시징**           |
| AI 챗봇       | 5             | 생성, 채팅, 관리            |

### WebSocket 연결

```javascript
// 채팅방 연결
ws://localhost:8000/v1/ws/chat/{room_id}?token={jwt_token}

// 메시지 전송
{
  "type": "message",
  "content": "안녕하세요!",
  "message_type": 0
}

// 타이핑 인디케이터
{
  "type": "typing",
  "is_typing": true
}
```

---

## 🧪 테스트

```bash
# 모든 테스트 실행
pytest tests/ -v

# 커버리지 포함
pytest tests/ --cov=app

# 특정 테스트 파일
pytest tests/test_users.py -v
```

**테스트 커버리지:** 61% (30/30 테스트 통과)

---

## 📊 데이터베이스 스키마

16개 테이블 구성:

- **인증 & 사용자:** users, user_sessions
- **소셜:** follows, mates, mate_requests, blocks
- **채팅:** chat_rooms, chat_room_members, chat_messages, chat_room_invites
- **AI:** chatbots, ai_chat_sessions
- **기타:** notifications, user_reports, clover_transactions, device_tokens

자세한 내용은 [docs/13-database-schema.md](./docs/13-database-schema.md)를 참조하세요.

---

## 🔧 개발

### 프로젝트 구조

```
app/
├── api/v1/endpoints/      # API 라우트 핸들러
├── services/              # 비즈니스 로직 계층
├── repositories/          # 데이터베이스 접근 계층
├── models/                # SQLAlchemy ORM 모델
├── schemas/               # Pydantic 검증 스키마
├── core/                  # 설정 & 유틸리티
└── websocket/             # WebSocket 연결 관리자
```

### 주요 디자인 패턴

- **Repository 패턴:** 비즈니스 로직과 데이터 접근 분리
- **Service 계층:** 비즈니스 규칙 캡슐화
- **의존성 주입:** FastAPI의 Depends 시스템
- **Async/Await:** 논블로킹 I/O 연산

---

## 📈 진행 상황

**전체 완료율: 85%**

| 영역 | 완료도 | 상태 |
|------|--------|------|
| 백엔드 인프라 | 100% | ✅ FastAPI, PostgreSQL, Redis, MinIO |
| 인증 시스템 | 95% | ✅ OAuth (Google), 이메일/비밀번호, JWT |
| 소셜 기능 | 100% | ✅ 팔로우, 메이트, 차단 |
| 채팅 시스템 | 95% | ✅ REST + WebSocket, 하이브리드 AI |
| AI 챗봇 | 100% | ✅ GPT-4, 커스텀 봇 |
| 가상 화폐 | 100% | ✅ 클로버, IAP 검증 |
| 알림 | 90% | ✅ REST API 완료 |
| Flutter 앱 | 90% | ✅ 핵심 기능 완료 |

### 남은 작업 (15%)

- 🔜 Apple OAuth 구현
- 🔜 푸시 알림 (FCM/APNs)
- 🔜 iOS 앱 배포
- 🔜 프로덕션 배포

---

## 📚 문서

- [시스템 아키텍처](./docs/12-system-architecture.md)
- [데이터베이스 스키마](./docs/13-database-schema.md)
- [API 설계](./docs/14-api-design.md)
- [인증 시스템](./docs/15-auth-system.md)
- [WebSocket 실시간](./docs/16-realtime-websocket.md)

---

## 🤝 기여

기여를 환영합니다! 기여 가이드라인을 읽어주세요.

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.

---

## 🙏 감사의 말

- 훌륭한 프레임워크를 제공한 FastAPI
- GPT-4 API를 제공한 OpenAI
- 오픈소스 커뮤니티

---

**❤️ Mate Chat 팀이 만듭니다**
