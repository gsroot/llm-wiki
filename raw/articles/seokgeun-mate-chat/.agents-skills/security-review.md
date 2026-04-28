---
name: security-review
description: >
  Mate Chat에서 인증, 비밀번호, 토큰, OAuth, 개인정보, 또는 보안에 민감한 코드 작업 시 자동으로
  보안 검토를 수행합니다. 트리거 키워드: "인증", "auth", "password", "token", "OAuth", "보안",
  "security", "개인정보", "personal data", "JWT", "비밀번호", "sensitive".
  OWASP Top 10 기반으로 FastAPI 백엔드 및 Flutter 프론트엔드의 일반적인 취약점을 검사합니다.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Security Review

Mate Chat의 보안에 민감한 코드에 대해 일반적인 취약점을 자동으로 검토합니다.

## 개요

**Mate Chat 소셜 메시징 플랫폼이 처리하는 데이터**:
- 사용자 인증 (이메일/비밀번호, OAuth)
- 개인정보 (프로필, 메시지)
- 결제 데이터 (클로버 화폐 인앱 결제)
- 실시간 통신 (WebSocket)

**보안은 가장 중요합니다.** 이 스킬은 보안에 민감한 코드 작업 시 OWASP Top 10 기반으로 취약점을 자동 검사합니다.

---

## 관련 시스템

**Slash Command:** 없음 (자동 트리거만)
- 보안 관련 키워드 감지 시 자동으로 이 스킬이 트리거됨

**Sub-Agent:** `fastapi-backend-expert`, `flutter-app-expert` (연계)
- 인증/보안 기능 구현 시 해당 에이전트가 먼저 호출됨
- 코드 작성 완료 후 이 스킬이 보안 검증 수행

**Agent Skill:** `security-review` (이 스킬 - 자동 트리거)
- 트리거: 인증, 비밀번호, 토큰, OAuth, 개인정보 관련 코드 작성 시 자동 실행
- 역할: OWASP Top 10 기반 보안 취약점 자동 검증

**관련 스킬:**
- `api-consistency`: API 엔드포인트 표준 검증
- `flutter-patterns`: Flutter 보안 패턴 검증
- `migration-safety`: 데이터베이스 보안 (민감한 데이터 마이그레이션)

---

## 보안 체크리스트

전체 상세 체크리스트는 [security-checklist.md](./references/security-checklist.md)를 참조하세요.

### 핵심 체크리스트

#### 1. 인증 및 권한 부여
- [ ] 비밀번호 bcrypt 해시 (평문 금지)
- [ ] JWT 시크릿 환경 변수에 저장 (하드코딩 금지)
- [ ] 토큰 적절한 만료 시간 설정
- [ ] OAuth 토큰 서버 측 검증
- [ ] 보호된 엔드포인트에 `get_current_user` 의존성

#### 2. 데이터 보호
- [ ] SQLAlchemy ORM 사용 (SQL Injection 방지)
- [ ] 사용자 입력 Pydantic 스키마로 검증
- [ ] 로그에 민감한 데이터 포함 금지
- [ ] HTTPS 강제 (TLS 1.2+)

#### 3. API 보안
- [ ] 모든 엔드포인트에 Rate Limiting
- [ ] 인증 엔드포인트 더 엄격한 제한 (10 req/min)
- [ ] 프로덕션에서 스택 트레이스 노출 금지
- [ ] 에러 메시지에서 민감한 정보 제외

#### 4. WebSocket 보안
- [ ] JWT 토큰으로 연결 인증
- [ ] 메시지 전달 전 방 멤버십 확인
- [ ] 메시지 전송 Rate Limiting

#### 5. 의존성
- [ ] 알려진 취약점 없음
- [ ] 정기적인 보안 업데이트 적용

---

## 일반적인 취약점 예제

상세한 예제는 [security-checklist.md](./references/security-checklist.md)를 참조하세요.

### SQL Injection 방지

```python
# ❌ 절대 금지
query = f"SELECT * FROM users WHERE email = '{user_email}'"

# ✅ SQLAlchemy ORM 사용
result = await db.execute(select(User).where(User.email == user_email))
```

### 비밀번호 해시

```python
# ❌ 평문 저장 금지
user.password = password_from_request

# ✅ bcrypt 해시 사용
from app.core.security import get_password_hash
user.password_hash = get_password_hash(password_from_request)
```

### JWT 시크릿

```python
# ❌ 하드코딩 금지
JWT_SECRET = "my-super-secret-key"

# ✅ 환경 변수에서 로드
from app.core.config import settings
JWT_SECRET = settings.JWT_SECRET_KEY
```

### 토큰 검증

```python
# ❌ 검증 없이 신뢰 금지
user_id = decode_jwt(token)["user_id"]

# ✅ 검증 포함
try:
    payload = decode_access_token(token)
    user_id = payload["sub"]
except JWTError:
    raise HTTPException(401, "Could not validate credentials")
```

### 로그에 민감한 데이터 포함 금지

```python
# ❌ 절대 금지
logger.info(f"User login: {email}, password: {password}")

# ✅ 비밀번호 제외
logger.info("user_login_attempt", email=email)
```

### Rate Limiting

```python
# ❌ 인증 엔드포인트에 Rate Limiting 없음
@router.post("/login")
async def login(...):
    ...

# ✅ Rate Limiter 적용
from app.core.rate_limiters import auth_limiter

@router.post("/login")
@auth_limiter  # 분당 10회 요청
async def login(...):
    ...
```

---

## OWASP Top 10 커버리지

각 취약점에 대한 상세 가이드는 [owasp-guide.md](./references/owasp-guide.md)를 참조하세요.

**OWASP Top 10 (2021)**:
1. **A01** - Broken Access Control (권한 부여 검사)
2. **A02** - Cryptographic Failures (HTTPS, bcrypt)
3. **A03** - Injection (ORM, 입력 검증)
4. **A04** - Insecure Design (보안 패턴)
5. **A05** - Security Misconfiguration (안전한 기본값)
6. **A06** - Vulnerable Components (의존성 최신 상태)
7. **A07** - Authentication Failures (강력한 인증)
8. **A08** - Data Integrity Failures (입력 검증)
9. **A09** - Logging Failures (보안 이벤트 로깅)
10. **A10** - Server-Side Request Forgery (URL 검증)

---

## Mate Chat 특정 보안 규칙

### 백엔드 (FastAPI)

1. **항상 async/await 사용** - 블로킹 공격 방지
2. **모든 엔드포인트에 Rate Limiting** - Redis 기반
3. **JWT 검증** - `get_current_user` 의존성
4. **WebSocket 인증** - 쿼리 파라미터 JWT 검증
5. **구조화된 로깅만** - structlog, 민감한 데이터 금지

### 프론트엔드 (Flutter)

1. **FlutterSecureStorage 사용** - SharedPreferences 금지
2. **모든 서버 응답 검증** - API를 신뢰하지 않음
3. **HTTPS만 사용** - 평문 HTTP 금지
4. **사용자 입력 검증** - XSS 방지
5. **생체 인증** - 플랫폼 API 안전하게 사용

---

## 검토 프로세스

1. 보안 도메인 식별 (인증/데이터/API/결제)
2. 관련 체크리스트 확인 - [security-checklist.md](./references/security-checklist.md)
3. 일반적인 취약점 검색
4. OWASP Top 10 커버리지 확인 - [owasp-guide.md](./references/owasp-guide.md)
5. 보안 관점 테스트: 무엇이 잘못될 수 있는가?
6. 발견 사항 문서화 및 수정 제안

---

## 보안 테스팅

배포 전 필수 확인:

```bash
# 백엔드
cd mate_chat_backend
uv run pytest -x -v              # 모든 테스트 실행
uv run pip-audit                 # 의존성 보안 검사

# 프론트엔드
cd mate_chat_flutter
flutter test                     # 테스트 실행
flutter analyze                  # 보안 문제 분석
```

---

## 즉시 보고해야 할 치명적 보안 문제

다음을 발견하면 **즉시 보고**:
- ❗ 하드코딩된 시크릿 또는 API 키
- ❗ 암호화되지 않은 비밀번호
- ❗ SQL Injection 취약점
- ❗ 민감한 엔드포인트 인증 누락
- ❗ 로그/에러에 노출된 PII
- ❗ 치명적인 의존성 취약점

---

## 참조 파일

### 상세 가이드
- **[security-checklist.md](./references/security-checklist.md)** - 완전한 OWASP Top 10 기반 체크리스트, 상세 예제
- **[owasp-guide.md](./references/owasp-guide.md)** - OWASP Top 10 각 항목 상세 가이드, 공격 시나리오, 방어 전략

### 외부 리소스
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/)
- [FastAPI Security](https://fastapi.tiangolo.com/tutorial/security/)
- [Flutter Security Best Practices](https://flutter.dev/docs/deployment/security)

---

**기억하세요**: 보안은 기능이 아니라 필수 요구사항입니다. 의심스러울 때는 신중한 쪽을 선택하세요!
