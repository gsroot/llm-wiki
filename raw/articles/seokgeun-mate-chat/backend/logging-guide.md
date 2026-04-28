# 로깅 시스템 가이드

## 개요

Mate Chat 백엔드는 구조화된 로깅을 위해 **structlog**를 사용하며, 프로덕션 환경에서는 JSON 형식의 로그를, 개발 환경에서는 색상이 있는 사람이 읽기 쉬운 출력을 제공합니다.

모든 로그에는 다음이 포함됩니다:

- 타임스탬프 (ISO 8601, UTC)
- 로그 레벨 (DEBUG, INFO, WARNING, ERROR)
- 로거 이름 (모듈 경로)
- 애플리케이션 컨텍스트 (앱 이름, 환경)
- 구조화된 키-값 데이터

## 아키텍처

### 구성 요소

1. **핵심 로깅 모듈** (`app/core/logging.py`)

   - 로깅 설정
   - 로거 팩토리
   - 일반적인 패턴을 위한 헬퍼 함수

2. **로깅 미들웨어** (`app/middleware/logging.py`)

   - HTTP 요청/응답 자동 로깅
   - 요청 소요 시간 추적
   - 상태 코드 기반 로그 레벨

3. **서비스 계층 통합**
   - 사용자 서비스: 프로필 작업, 캐시 히트/미스
   - WebSocket 관리자: 연결 이벤트
   - (로깅 통합 시 추가 예정)

## 설정

### 환경 기반 로깅

로깅 시스템은 `ENVIRONMENT` 설정에 따라 자동으로 적응합니다:

#### 개발 모드

```bash
ENVIRONMENT=development
```

출력 형식:

```
2025-11-27T12:34:56.789012Z [info     ] HTTP request received   app=mate-chat method=GET path=/v1/users/me environment=development [app.middleware.logging:46]
2025-11-27T12:34:56.823456Z [info     ] User profile retrieved  app=mate-chat user_id=123 username=john_doe environment=development [app.services.user_service:55]
```

특징:

- 색상이 있는 콘솔 출력
- 들여쓰기로 예쁘게 출력
- 파일:라인번호 정보 포함
- DEBUG 레벨 활성화

#### 프로덕션 모드

```bash
ENVIRONMENT=production
```

출력 형식 (JSON):

```json
{"event": "HTTP request received", "level": "info", "timestamp": "2025-11-27T12:34:56.789012Z", "app": "mate-chat", "environment": "production", "method": "GET", "path": "/v1/users/me"}
{"event": "User profile retrieved", "level": "info", "timestamp": "2025-11-27T12:34:56.823456Z", "app": "mate-chat", "environment": "production", "user_id": "123", "username": "john_doe"}
```

특징:

- JSON 출력 (로그당 한 줄)
- INFO 레벨 이상
- 로그 집계 시스템(Datadog, ELK 등)과 쉽게 통합

### 로그 레벨

시스템은 표준 Python 로그 레벨을 사용합니다:

| 레벨        | 용도                        | 예시                           |
| ----------- | --------------------------- | ------------------------------ |
| **DEBUG**   | 상세한 진단 정보            | 캐시 히트, 데이터베이스 쿼리   |
| **INFO**    | 일반적인 정보 메시지        | 사용자 로그인, 프로필 업데이트 |
| **WARNING** | 경고 메시지 (중요하지 않음) | 4xx HTTP 오류, rate limiting   |
| **ERROR**   | 오류 메시지 (중요함)        | 5xx 오류, 예외                 |

### 서드파티 라이브러리 로깅

노이즈를 줄이기 위해 서드파티 라이브러리는 더 높은 로그 레벨로 설정됩니다:

```python
# app/core/logging.py에 설정됨
uvicorn.access  → WARNING
uvicorn.error   → INFO
sqlalchemy      → WARNING
httpx           → WARNING
openai          → WARNING
```

## 사용법

### 기본 로깅

```python
from app.core.logging import get_logger

logger = get_logger(__name__)

# 간단한 로그
logger.info("User logged in")

# 컨텍스트가 포함된 구조화된 로그
logger.info("User logged in", user_id=123, ip="192.168.1.1")

# 다양한 레벨
logger.debug("Debug info", details="...")
logger.warning("Warning message", reason="...")
logger.error("Error occurred", error=str(e))
```

### 헬퍼 함수

로깅 모듈은 일반적인 패턴을 위한 헬퍼 함수를 제공합니다:

#### HTTP 요청/응답 로깅

```python
from app.core.logging import log_request, log_response

# 요청 로그
log_request("POST", "/v1/users/123", user_id=123)

# 응답 로그
log_response("POST", "/v1/users/123", status_code=200, duration_ms=45.2, user_id=123)
```

#### 캐시 작업

```python
from app.core.logging import log_cache_operation

# 캐시 히트
log_cache_operation("GET", "cache:user:123", hit=True)

# 캐시 미스
log_cache_operation("GET", "cache:user:123", hit=False)

# 캐시 설정
log_cache_operation("SET", "cache:user:123", ttl=300)
```

#### WebSocket 이벤트

```python
from app.core.logging import log_websocket_event

# 연결
log_websocket_event("connect", room_id="room_123", user_id="user_456", connection_count=5)

# 연결 해제
log_websocket_event("disconnect", room_id="room_123", user_id="user_456")

# 메시지
log_websocket_event("message", room_id="room_123", user_id="user_456", message_type="text")
```

#### 인증 이벤트

```python
from app.core.logging import log_auth_event

# 성공적인 로그인
log_auth_event("login", user_id="123", success=True, provider="google", ip="192.168.1.1")

# 실패한 로그인
log_auth_event("login", success=False, provider="google", reason="invalid_token")

# 토큰 갱신
log_auth_event("token_refresh", user_id="123", success=True)
```

#### 오류 로깅

```python
from app.core.logging import log_error

try:
    risky_operation()
except Exception as e:
    log_error(e, context="User profile update", user_id=123)
    raise
```

## 통합 예제

### 서비스 계층

```python
from app.core.logging import get_logger, log_cache_operation

logger = get_logger(__name__)

class UserService:
    async def get_user(self, user_id: UUID):
        logger.debug("Fetching user", user_id=str(user_id))

        # 캐시 시도
        cached = await get_cached(f"user:{user_id}")
        if cached:
            log_cache_operation("GET", f"user:{user_id}", hit=True)
            logger.info("User retrieved from cache", user_id=str(user_id))
            return cached

        # DB에서 가져오기
        log_cache_operation("GET", f"user:{user_id}", hit=False)
        logger.debug("Cache miss, fetching from database", user_id=str(user_id))

        user = await db.get(user_id)
        if not user:
            logger.warning("User not found", user_id=str(user_id))
            raise NotFoundError()

        logger.info("User retrieved", user_id=str(user_id), username=user.username)
        return user
```

### WebSocket 관리자

```python
from app.core.logging import get_logger, log_websocket_event

logger = get_logger(__name__)

class ConnectionManager:
    async def connect(self, websocket, room_id, user_id):
        await websocket.accept()
        self.connections[room_id].add(websocket)

        log_websocket_event(
            "connect",
            room_id,
            user_id,
            connection_count=len(self.connections[room_id])
        )

    def disconnect(self, websocket, room_id):
        user_id = self.get_user_id(websocket)
        self.connections[room_id].remove(websocket)

        log_websocket_event("disconnect", room_id, user_id)
```

### 오류 핸들러

```python
from app.core.logging import get_logger

logger = get_logger(__name__)

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(
        "Unhandled exception",
        method=request.method,
        path=str(request.url.path),
        error_type=type(exc).__name__,
        error_message=str(exc),
        exc_info=True,  # 스택 트레이스 포함
    )
    return JSONResponse(status_code=500, content={"error": "Internal server error"})
```

## 미들웨어 로깅

로깅 미들웨어는 모든 HTTP 요청과 응답을 자동으로 로깅합니다:

```python
# app/main.py에 설정됨
app.add_middleware(LoggingMiddleware)
```

**로깅 내용:**

- 요청: method, path, query 파라미터
- 응답: 상태 코드, 밀리초 단위 소요 시간
- 오류: 예외 타입, 메시지, 스택 트레이스

**로그 레벨:**

- 2xx-3xx: INFO
- 4xx: WARNING
- 5xx: ERROR

**제외된 경로:**

- `/` (root)
- `/health`
- `/docs`
- `/redoc`
- `/openapi.json`

## 모범 사례

### 1. 구조화된 로깅 사용

```python
# ✅ 좋음 - 구조화됨
logger.info("User created", user_id=123, username="john", role="user")

# ❌ 나쁨 - 비구조화됨
logger.info(f"User {username} (id={user_id}) created with role {role}")
```

구조화된 로그는:

- 검색 및 필터링이 쉬움
- 로그 집계 도구로 파싱 가능
- 더 일관성 있음

### 2. 관련 컨텍스트 포함

```python
# ✅ 좋음 - 컨텍스트 포함
logger.error(
    "Failed to send email",
    user_id=user.id,
    email=user.email,
    error=str(e),
    exc_info=True
)

# ❌ 나쁨 - 컨텍스트 누락
logger.error("Email send failed")
```

### 3. 적절한 로그 레벨 사용

```python
# ✅ 좋음
logger.debug("Cache hit", key="user:123")  # 디버그 정보
logger.info("User logged in", user_id=123)  # 중요한 이벤트
logger.warning("Rate limit exceeded", ip="...")  # 중요하지 않은 문제
logger.error("Database connection failed", exc_info=True)  # 중요한 오류

# ❌ 나쁨
logger.info("Debugging variable x", x=value)  # DEBUG여야 함
logger.error("User not found")  # WARNING이어야 함 (예상된 오류)
```

### 4. 민감한 데이터를 로깅하지 않기

```python
# ✅ 좋음
logger.info("User authenticated", user_id=user.id)

# ❌ 나쁨 - 민감한 데이터 로깅
logger.info("User logged in", password=password, token=jwt_token)
```

**절대 로깅하지 말 것:**

- 비밀번호
- 토큰 (JWT, OAuth, API 키)
- 신용카드 번호
- 개인 식별 정보 (필요하고 규정 준수하지 않는 한)

### 5. 예외에 exc_info 사용

```python
# ✅ 좋음 - 스택 트레이스 포함
try:
    risky_operation()
except Exception as e:
    logger.error("Operation failed", error=str(e), exc_info=True)
    raise

# ❌ 나쁨 - 스택 트레이스 없음
try:
    risky_operation()
except Exception as e:
    logger.error(f"Error: {e}")
```

### 6. 서비스 경계에서 로깅

로깅 중점:

- **진입점**: HTTP 요청, WebSocket 연결
- **외부 호출**: 데이터베이스 쿼리, API 호출, 캐시 작업
- **중요한 비즈니스 로직**: 사용자 생성, 트랜잭션
- **오류 및 예외**: 모든 오류 조건

과도한 로깅 피하기:

- 내부 함수 호출
- 루프 반복
- 사소한 작업

## 로그 확인

### 개발 환경

로그는 색상과 함께 stdout에 출력됩니다:

```bash
uv run uvicorn app.main:app --reload
```

### 프로덕션 환경

stdout에서 JSON 로그 수집:

```bash
# Kubernetes
kubectl logs deployment/mate_chat_backend -f

# 파일로 리다이렉트
python -m app.main >> logs/app.log 2>&1
```

### 로그 필터링

JSON 출력을 사용하면 `jq`로 필터링할 수 있습니다:

```bash
# 모든 ERROR 로그
cat logs/app.log | jq 'select(.level == "error")'

# 특정 사용자에 대한 로그
cat logs/app.log | jq 'select(.user_id == "123")'

# 사용자 서비스의 로그
cat logs/app.log | jq 'select(.logger_name | contains("user_service"))'

# HTTP 500 오류
cat logs/app.log | jq 'select(.status_code >= 500)'
```

## 로그 집계

### ELK 스택과의 통합

```yaml
filebeat.inputs:
  - type: filestream
    enabled: true
    paths:
      - ./logs/app.log
```

### Datadog과의 통합

```python
# Datadog 핸들러 추가 (선택 사항)
import structlog

# configure_logging()에 추가:
processors.append(
    structlog.processors.JSONRenderer()
)
```

그런 다음 Datadog 에이전트를 설정하여 stdout에서 로그를 수집합니다.

## 성능 고려사항

### 프로덕션 환경의 로그 레벨

프로덕션에서는 로그 볼륨을 줄이기 위해 INFO 또는 WARNING으로 설정합니다:

```python
# app/core/logging.py에서
log_level = logging.INFO if settings.ENVIRONMENT == "production" else logging.DEBUG
```

### 로그에서 비용이 많이 드는 작업 피하기

```python
# ✅ 좋음
logger.debug("Processing items", count=len(items))

# ❌ 나쁨 - 비용이 많이 드는 직렬화
logger.debug("Processing items", items=[item.to_dict() for item in items])
```

### 비동기 로깅 (향후 개선)

처리량이 높은 애플리케이션의 경우 블로킹 I/O를 피하기 위해 비동기 로깅을 고려하세요.

## 로깅 테스트

### 테스트에서 로그 캡처

```python
import logging
from structlog.testing import LogCapture

def test_logging(caplog):
    caplog.set_level(logging.INFO)

    # 로깅하는 코드
    logger.info("Test message", user_id=123)

    # 로그 확인
    assert "Test message" in caplog.text
    assert any(record.user_id == 123 for record in caplog.records)
```

### 로그 출력 테스트

```python
from app.core.logging import configure_logging, get_logger

def test_log_structure():
    configure_logging()
    logger = get_logger("test")

    with LogCapture() as log_queue:
        logger.info("Test event", user_id=123, action="login")

        assert len(log_queue.entries) == 1
        entry = log_queue.entries[0]
        assert entry["event"] == "Test event"
        assert entry["user_id"] == 123
```

## 문제 해결

### 로그가 나타나지 않음

1. **로그 레벨 확인**: 개발 환경에서 DEBUG 로그가 활성화되어 있는지 확인

   ```python
   # app/core/logging.py
   log_level = logging.DEBUG
   ```

2. **로깅 설정 확인**: 시작 시 `configure_logging()`이 호출되는지 확인

   ```python
   # app/main.py (맨 위에 있어야 함)
   from app.core.logging import configure_logging
   configure_logging()
   ```

3. **출력 스트림 확인**: 로그는 stdout으로 가므로 리다이렉트되지 않았는지 확인

### 중복 로그

중복 로그 항목이 표시되는 경우:

1. **핸들러 설정 확인**: 핸들러가 여러 번 추가되지 않았는지 확인
2. **로거 전파 확인**: 필요한 경우 `propagate=False` 설정

### 성능 저하

로깅으로 인해 성능 문제가 발생하는 경우:

1. **로그 레벨 낮추기**: 프로덕션에서 INFO 또는 WARNING 사용
2. **비용이 많이 드는 작업 제거**: 로그 메시지에서 무거운 직렬화 피하기
3. **지연 평가 사용**: 기본 타입으로만 로그 구조화

## 향후 개선사항

계획된 개선사항:

- [ ] 높은 처리량을 위한 비동기 로깅
- [ ] 대량 이벤트를 위한 로그 샘플링
- [ ] 분산 추적 통합 (OpenTelemetry)
- [ ] 요청 ID 추적을 위한 커스텀 프로세서
- [ ] 파일 기반 로깅을 위한 로그 로테이션
- [ ] 로그로부터 성능 메트릭

## 관련 문서

- [시스템 아키텍처](./12-system-architecture.md)
- [캐싱 가이드](./caching-guide.md)
- [Rate Limiting 가이드](./rate-limiting-guide.md)

---

**최종 업데이트:** 2025-11-27
**상태:** 구현 및 테스트 완료 (57/57 테스트 통과)
**커버리지:** 메인 앱 (57%), 미들웨어 (88%), 핵심 로깅 (68%)
