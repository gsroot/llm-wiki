# Rate Limiting 가이드

## 개요

Mate Chat 백엔드는 API 남용을 방지하고 공정한 사용을 보장하기 위해 Redis 기반 rate limiting 시스템을 구현합니다. 이 시스템은 정확한 rate limiting을 위해 **슬라이딩 윈도우 알고리즘**을 사용합니다.

## 기능

- **글로벌 rate limiting**: 모든 API 엔드포인트에 적용 (기본값: 60 요청/분)
- **엔드포인트별 rate limiting**: 민감한 엔드포인트를 위한 커스텀 제한
- **IP 기반 제한**: 익명 요청에 대해
- **사용자 기반 제한**: 인증된 요청에 대해 (더 정확함)
- **Rate limit 헤더**: 응답에 `X-RateLimit-*` 헤더 포함
- **슬라이딩 윈도우 알고리즘**: 고정 윈도우보다 더 정확함

## 아키텍처

### 구성 요소

1. **Redis 클라이언트** (`app/core/redis.py`)
   - Redis 커넥션 풀 관리
   - 비동기 Redis 클라이언트 제공

2. **Rate Limit 미들웨어** (`app/middleware/rate_limit.py`)
   - 모든 요청에 적용되는 글로벌 미들웨어
   - 헬스체크 및 문서 엔드포인트 제외
   - 모든 응답에 rate limit 헤더 추가

3. **엔드포인트 Rate Limiter** (`app/middleware/rate_limit.py`)
   - `strict_rate_limit`: 10 요청/분 (민감한 엔드포인트)
   - `moderate_rate_limit`: 30 요청/분 (일반 엔드포인트)
   - `relaxed_rate_limit`: 100 요청/분 (공개 엔드포인트)

4. **Rate Limit 의존성** (`app/core/dependencies.py`)
   - Rate limit을 적용하기 위한 FastAPI 의존성
   - `Depends()`로 쉽게 사용 가능

## 설정

### 환경 변수

```bash
# Redis connection
REDIS_URL=redis://localhost:6379/0

# Global rate limit (requests per minute)
RATE_LIMIT_PER_MINUTE=60
```

### 글로벌 Rate Limit 조정

`app/core/config.py` 편집:

```python
class Settings(BaseSettings):
    RATE_LIMIT_PER_MINUTE: int = 60  # Change this value
```

### 제외 경로

다음 경로는 rate limiting에서 제외됩니다:

- `/` - 루트 엔드포인트
- `/health` - 헬스체크
- `/docs` - Swagger UI
- `/redoc` - ReDoc
- `/openapi.json` - OpenAPI 스키마

제외 경로를 수정하려면 `app/middleware/rate_limit.py` 편집:

```python
self.exclude_paths = exclude_paths or [
    "/",
    "/health",
    "/docs",
    "/redoc",
    "/openapi.json",
]
```

## 사용법

### 글로벌 Rate Limiting

모든 엔드포인트에 자동으로 적용됩니다. 코드 변경이 필요하지 않습니다.

**응답 헤더:**

```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1732600000
```

### 엔드포인트별 Rate Limiting

FastAPI 의존성을 사용하여 커스텀 rate limit 적용:

#### Strict Rate Limit (10/분)

민감한 엔드포인트에 사용:

```python
from fastapi import APIRouter, Depends
from app.core.dependencies import check_strict_rate_limit

router = APIRouter()

@router.post("/auth/oauth")
async def oauth_login(
    request: OAuthLoginRequest,
    _: None = Depends(check_strict_rate_limit),  # 10 requests/min
):
    # Your endpoint logic
    pass
```

**사용 사례:**
- OAuth 로그인
- 비밀번호 재설정
- 계정 삭제
- 결제 처리

#### Moderate Rate Limit (30/분)

일반 API 엔드포인트에 사용:

```python
from app.core.dependencies import check_moderate_rate_limit

@router.get("/users/me")
async def get_current_user(
    _: None = Depends(check_moderate_rate_limit),  # 30 requests/min
):
    pass
```

**사용 사례:**
- 사용자 프로필 업데이트
- 채팅방 생성
- AI 챗봇 쿼리

#### Relaxed Rate Limit (100/분)

공개 또는 높은 처리량의 엔드포인트에 사용:

```python
from app.core.dependencies import check_relaxed_rate_limit

@router.get("/public/chatbots")
async def list_public_chatbots(
    _: None = Depends(check_relaxed_rate_limit),  # 100 requests/min
):
    pass
```

**사용 사례:**
- 공개 챗봇 탐색
- 메시지 목록 페이지네이션
- 사용자 검색

### 커스텀 Rate Limiter

커스텀 rate limiter 생성:

```python
from app.middleware.rate_limit import EndpointRateLimiter

# 5 requests per minute
very_strict_limiter = EndpointRateLimiter(requests_per_minute=5)

@router.post("/admin/dangerous-action")
async def dangerous_action(request: Request):
    # Check rate limit manually
    result = await very_strict_limiter(request)
    if result is not None:
        return result  # Rate limit exceeded

    # Your endpoint logic
    pass
```

## Rate Limit 키

시스템은 요청 타입에 따라 다른 키를 사용합니다:

### 익명 요청 (IP 기반)

```
rate_limit:ip:192.168.1.100
```

### 인증된 요청 (사용자 기반)

```
rate_limit:user:12345
```

### 엔드포인트별

```
rate_limit:endpoint:/v1/auth/oauth:user:12345
rate_limit:endpoint:/v1/auth/oauth:ip:192.168.1.100
```

## 슬라이딩 윈도우 알고리즘

구현은 Redis Sorted Set을 사용하여 요청을 추적합니다:

1. 각 요청은 타임스탬프를 점수로 하여 sorted set에 추가됩니다
2. 시간 윈도우 밖의 오래된 요청은 제거됩니다
3. 현재 요청 수가 제한과 비교됩니다
4. 허용되면 요청이 set에 추가됩니다

**장점:**
- 고정 윈도우보다 더 정확함
- 윈도우 경계에서의 버스트 공격 방지
- 요청의 공정한 분배

**Redis 작업:**

```python
# Remove old entries
ZREMRANGEBYSCORE rate_limit:user:123 0 {window_start}

# Count current requests
ZCARD rate_limit:user:123

# Add new request
ZADD rate_limit:user:123 {current_time} {request_id}

# Set expiration (cleanup)
EXPIRE rate_limit:user:123 120
```

## 에러 응답

### Rate Limit 초과

**상태 코드:** `429 Too Many Requests`

**응답 본문:**

```json
{
  "error": {
    "code": "RATE_LIMIT_EXCEEDED",
    "message": "Too many requests. Please try again later.",
    "retry_after": 1732600060
  }
}
```

**헤더:**

```http
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 0
X-RateLimit-Reset: 1732600060
```

## 모범 사례

### 1. 적절한 제한 선택

- **Strict (10/분)**: 인증, 결제, 민감한 작업
- **Moderate (30/분)**: 표준 CRUD 작업
- **Relaxed (100/분)**: 읽기 중심의 공개 엔드포인트
- **Global (60/분)**: 모든 엔드포인트의 기본값

### 2. 사용자 기반 vs IP 기반

- 사용자 기반 제한이 더 정확함 (공유 IP 문제 없음)
- IP 기반은 인증되지 않은 엔드포인트에 필요함
- 시스템은 인증 상태에 따라 자동으로 선택함

### 3. 모니터링

Rate limit 위반 모니터링:

```python
# Add logging in rate_limit.py
import logging

logger = logging.getLogger(__name__)

if not is_allowed:
    logger.warning(
        f"Rate limit exceeded for key: {rate_limit_key}",
        extra={"key": rate_limit_key, "limit": self.requests_per_minute}
    )
```

### 4. 테스트

개발 중 항상 rate limit을 테스트하세요:

```python
# tests/test_rate_limit.py
async def test_rate_limit_exceeded():
    # Make 61 requests (global limit is 60)
    for i in range(61):
        response = await client.get("/v1/users")
        if i < 60:
            assert response.status_code == 200
        else:
            assert response.status_code == 429
```

## 트러블슈팅

### Rate Limiting이 작동하지 않음

1. **Redis 연결 확인:**
   ```bash
   redis-cli ping
   ```

2. **미들웨어 순서 확인** in `main.py`:
   ```python
   # Rate limit should be BEFORE CORS
   app.add_middleware(RateLimitMiddleware)
   app.add_middleware(CORSMiddleware)
   ```

3. **Redis URL 확인:**
   ```bash
   echo $REDIS_URL
   # Should output: redis://localhost:6379/0
   ```

### 오탐지

정당한 사용자가 rate limit에 걸리는 경우:

1. 설정에서 글로벌 제한 증가
2. IP 기반 대신 사용자 기반 제한 사용
3. 특정 IP 또는 사용자를 화이트리스트에 추가
4. 엔드포인트별 제한 조정

### 성능 영향

Redis 작업은 매우 빠르지만, 다음을 모니터링하세요:

- Redis 메모리 사용량 (`INFO memory`)
- 응답 시간 증가 (1ms 미만이어야 함)
- Redis 커넥션 풀 고갈

## 향후 개선 사항

- [ ] 특정 사용자에 대한 rate limit 우회 (프리미엄, 관리자)
- [ ] 서버 부하에 따른 동적 rate limit
- [ ] Rate limit 분석 대시보드
- [ ] Redis Cluster를 사용한 분산 rate limiting
- [ ] 엔드포인트별 커스텀 에러 메시지
- [ ] Rate limit 워밍 (버스트 허용량)

## 관련 문서

- [시스템 아키텍처](./12-system-architecture.md)
- [API 설계](./14-api-design.md)
- [Redis 설정](./redis-setup.md)

---

**최종 업데이트:** 2025-11-26
**상태:** 구현 및 테스트 완료
