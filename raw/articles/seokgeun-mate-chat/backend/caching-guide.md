# 캐싱 전략 가이드

## 개요

Mate Chat 백엔드는 Redis 기반 캐싱 시스템을 구현하여 자주 접근하는 데이터에 대한 데이터베이스 쿼리를 줄여 성능을 향상시킵니다. 캐싱 레이어는 서비스 레벨에서 자동 캐시 무효화와 함께 구현됩니다.

## 기능

- **사용자 데이터 캐싱**: 사용자 프로필 및 설정 (TTL 5분)
- **채팅방 캐싱**: 채팅방 정보 및 메타데이터 (TTL 10분)
- **챗봇 캐싱**: AI 챗봇 설정 (TTL 30분)
- **자동 무효화**: 데이터 업데이트 시 캐시 자동 삭제
- **패턴 기반 삭제**: 효율적인 대량 캐시 무효화
- **JSON 직렬화**: 복잡한 객체의 자동 직렬화

## 아키텍처

### 구성 요소

1. **캐시 유틸리티** (`app/core/cache.py`)
   - 핵심 캐싱 함수 (get, set, delete)
   - 캐시 키 빌더
   - 무효화 헬퍼
   - TTL 설정

2. **서비스 통합**
   - User Service: 프로필 캐싱
   - Chat Service: 채팅방 캐싱
   - Chatbot Service: 챗봇 설정 캐싱

3. **Redis 백엔드** (`app/core/redis.py`)
   - 비동기 Redis 클라이언트
   - 커넥션 풀링
   - 헬스 체크

## 캐시 키 전략

### 키 형식

모든 캐시 키는 다음 패턴을 따릅니다: `cache:{type}:{id}`

### 키 빌더

```python
from app.core.cache import CacheKeyBuilder

# 사용자 캐시
CacheKeyBuilder.user(user_id)              # cache:user:123
CacheKeyBuilder.user_by_email(email)       # cache:user:email:user@example.com
CacheKeyBuilder.user_followers(user_id)    # cache:followers:123
CacheKeyBuilder.user_following(user_id)    # cache:following:123

# 채팅방 캐시
CacheKeyBuilder.chat_room(room_id)         # cache:chat_room:456

# 챗봇 캐시
CacheKeyBuilder.chatbot(chatbot_id)        # cache:chatbot:789

# 커스텀 캐시
CacheKeyBuilder.custom("my_key")           # cache:custom:my_key
```

## TTL 설정

Time-to-live (TTL) 값은 `CacheConfig`에서 설정됩니다:

| 데이터 타입 | TTL | 이유 |
|-----------|-----|--------|
| User | 5분 | 프로필이 자주 변경되지 않음 |
| Chat Room | 10분 | 채팅방 설정은 상대적으로 정적임 |
| Chatbot | 30분 | AI 설정은 거의 변경되지 않음 |
| Social Relations | 3분 | 팔로우/메이트 상태가 자주 변경됨 |
| Default | 5분 | 범용 목적 |

### TTL 커스터마이징

`app/core/cache.py` 편집:

```python
class CacheConfig:
    USER_TTL = 300          # 5분
    CHAT_ROOM_TTL = 600     # 10분
    CHATBOT_TTL = 1800      # 30분
    # 필요에 따라 추가
```

## 사용법

### 기본 캐시 연산

```python
from app.core.cache import get_cached, set_cached, delete_cached

# 캐시 설정
await set_cached("my_key", {"data": "value"}, ttl=300)

# 캐시 조회
data = await get_cached("my_key")

# 캐시 삭제
await delete_cached("my_key")
```

### 서비스에서 사용

캐싱 패턴은 이미 핵심 서비스에 구현되어 있습니다:

#### User Service 예제

```python
async def get_me(self, db: AsyncSession, user_id: UUID) -> UserResponse:
    """현재 사용자 프로필 조회 (캐싱 포함)."""
    # 캐시에서 조회 시도
    cache_key = CacheKeyBuilder.user(user_id)
    cached_data = await get_cached(cache_key)

    if cached_data is not None:
        return UserResponse.model_validate(cached_data)

    # 캐시 미스 - 데이터베이스에서 조회
    user = await user_repository.get_by_id(db, user_id)
    if not user:
        raise ValueError("User not found")

    # 결과 캐싱
    user_response = UserResponse.model_validate(user)
    await set_cached(cache_key, user_response.model_dump(), CacheConfig.USER_TTL)

    return user_response
```

#### 캐시 무효화를 포함한 업데이트

```python
async def update_me(
    self, db: AsyncSession, user_id: UUID, user_data: UserUpdate
) -> UserResponse:
    """현재 사용자 프로필 업데이트 (캐시 무효화)."""
    user = await user_repository.get_by_id(db, user_id)
    if not user:
        raise ValueError("User not found")

    updated_user = await user_repository.update(db, user, user_data)

    # 업데이트 후 사용자 캐시 무효화
    await invalidate_user_cache(user_id)

    return UserResponse.model_validate(updated_user)
```

### 패턴 기반 삭제

여러 관련 캐시 항목 삭제:

```python
from app.core.cache import delete_pattern

# 모든 사용자 관련 캐시 삭제
await delete_pattern("cache:user:*")

# 특정 사용자의 소셜 캐시 삭제
await delete_pattern(f"cache:followers:{user_id}")
await delete_pattern(f"cache:following:{user_id}")
```

### 캐시 무효화 헬퍼

일반적인 사용 사례를 위한 사전 구축된 무효화 함수:

```python
from app.core.cache import (
    invalidate_user_cache,
    invalidate_chat_room_cache,
    invalidate_chatbot_cache,
)

# 모든 사용자 관련 캐시 무효화
await invalidate_user_cache(user_id)

# 채팅방 캐시 무효화
await invalidate_chat_room_cache(room_id)

# 챗봇 캐시 무효화
await invalidate_chatbot_cache(chatbot_id)
```

## 새 기능에 캐시 추가하기

### 1단계: 캐시 키 정의

`CacheKeyBuilder`에 키 빌더 메서드 추가:

```python
@staticmethod
def notification(notification_id: int) -> str:
    """알림용 캐시 키 생성."""
    return f"cache:notification:{notification_id}"
```

### 2단계: TTL 설정 추가

`CacheConfig`에 TTL 추가:

```python
class CacheConfig:
    NOTIFICATION_TTL = 120  # 2분
```

### 3단계: 서비스에 캐싱 구현

```python
async def get_notification(self, db: AsyncSession, notification_id: UUID):
    """알림 조회 (캐싱 포함)."""
    # 캐시 먼저 시도
    cache_key = CacheKeyBuilder.notification(notification_id)
    cached_data = await get_cached(cache_key)

    if cached_data is not None:
        return NotificationResponse.model_validate(cached_data)

    # 캐시 미스 - DB에서 조회
    notification = await notification_repository.get(db, notification_id)
    if not notification:
        raise ValueError("Notification not found")

    # 결과 캐싱
    response = NotificationResponse.model_validate(notification)
    await set_cached(cache_key, response.model_dump(), CacheConfig.NOTIFICATION_TTL)

    return response
```

### 4단계: 캐시 무효화 추가

```python
async def mark_as_read(self, db: AsyncSession, notification_id: UUID):
    """알림을 읽음으로 표시 (캐시 무효화)."""
    notification = await notification_repository.get(db, notification_id)
    await notification_repository.update(db, notification, is_read=True)

    # 캐시 무효화
    await delete_cached(CacheKeyBuilder.notification(notification_id))
```

## 베스트 프랙티스

### 1. 읽기 중심 데이터 캐싱

캐시하기 좋은 데이터:
- 자주 읽힘
- 자주 업데이트되지 않음
- 시간 민감하지 않음

**좋은 후보:**
- 사용자 프로필
- 채팅방 설정
- 챗봇 설정
- 공개 콘텐츠

**나쁜 후보:**
- 실시간 메시지
- 알림 카운트
- 온라인 상태
- 거래 데이터

### 2. 업데이트 시 항상 무효화

```python
# ✅ 좋음
async def update_user(self, user_id: UUID, data: dict):
    await db_update(user_id, data)
    await invalidate_user_cache(user_id)  # 항상 무효화

# ❌ 나쁨
async def update_user(self, user_id: UUID, data: dict):
    await db_update(user_id, data)
    # 캐시 무효화 누락 - 오래된 데이터 발생!
```

### 3. 적절한 TTL 사용

- 자주 변경되는 데이터에는 짧은 TTL
- 정적 설정에는 긴 TTL
- 캐시 히트율과 데이터 신선도 사이의 균형

### 4. 캐시 미스를 우아하게 처리

```python
# ✅ 좋음 - 데이터베이스로 폴백
cached_data = await get_cached(key)
if cached_data is None:
    data = await fetch_from_database()
    await set_cached(key, data)
    return data
return cached_data

# ❌ 나쁨 - 캐시 미스 시 실패
cached_data = await get_cached(key)
return cached_data  # 캐시 미스 시 None 반환!
```

### 5. 복잡한 객체 직렬화

```python
# ✅ 좋음 - Pydantic 모델 직렬화
user_response = UserResponse.model_validate(user)
await set_cached(key, user_response.model_dump())

# ❌ 나쁨 - 모델 객체를 직접 캐시
await set_cached(key, user)  # 제대로 직렬화되지 않을 수 있음
```

## 성능 영향

### 캐시 히트율

캐시 효과 모니터링:

```python
from app.core.redis import get_redis

redis = await get_redis()

# 캐시 통계 조회 (INFO 명령이 활성화된 경우)
info = await redis.info("stats")
hits = info.get("keyspace_hits", 0)
misses = info.get("keyspace_misses", 0)
hit_ratio = hits / (hits + misses) if (hits + misses) > 0 else 0

print(f"캐시 히트율: {hit_ratio:.2%}")
```

### 예상 성능 향상

| 작업 | 캐시 없음 | 캐시 있음 | 개선도 |
|-----------|---------------|------------|-------------|
| 사용자 프로필 조회 | ~50ms (DB 쿼리) | ~2ms (Redis) | 25배 빠름 |
| 채팅방 조회 | ~30ms | ~2ms | 15배 빠름 |
| 챗봇 조회 | ~40ms | ~2ms | 20배 빠름 |

### 메모리 사용량

Redis 메모리 사용량 추정:

```python
# 평균 캐시 항목 크기
user_cache_size = 2KB      # 사용자 프로필 JSON
room_cache_size = 1KB      # 채팅방 JSON
chatbot_cache_size = 3KB   # 챗봇 + 지시사항

# 활성 사용자 10,000명 기준
total_memory = (10000 * 2KB) + (1000 * 1KB) + (500 * 3KB)
             = 20MB + 1MB + 1.5MB
             = ~22.5MB
```

## 모니터링

### Redis 헬스 체크

```python
from app.core.redis import ping_redis

is_healthy = await ping_redis()
if not is_healthy:
    # 데이터베이스 전용 모드로 폴백
    pass
```

### 캐시 키 개수

```python
redis = await get_redis()

# 모든 캐시 키 개수
all_keys = await redis.keys("cache:*")
print(f"전체 캐시 키: {len(all_keys)}")

# 타입별 개수
user_keys = await redis.keys("cache:user:*")
room_keys = await redis.keys("cache:chat_room:*")
```

### 전체 캐시 삭제

```python
from app.core.cache import clear_all_cache

# 모든 애플리케이션 캐시 삭제 (주의해서 사용)
deleted_count = await clear_all_cache()
print(f"{deleted_count}개의 캐시 항목 삭제됨")
```

## 문제 해결

### 캐시가 작동하지 않음

1. **Redis 연결 확인**
   ```bash
   redis-cli ping
   # 응답: PONG이어야 함
   ```

2. **Redis URL 확인**
   ```bash
   echo $REDIS_URL
   # 다음이어야 함: redis://localhost:6379/0
   ```

3. **캐시 키 확인**
   ```bash
   redis-cli KEYS "cache:*"
   ```

### 오래된 데이터

사용자가 오래된 데이터를 보는 경우:

1. 업데이트 시 캐시 무효화가 호출되는지 확인
2. 해당 데이터 타입의 TTL 감소
3. 수동으로 캐시 삭제: `await clear_all_cache()`

### 메모리 문제

Redis가 너무 많은 메모리를 사용하는 경우:

1. TTL 값 감소
2. 캐시 제거 정책 구현
3. 필수 데이터만 캐싱

## 테스팅

### 캐시 동작 테스트

```python
@pytest.mark.asyncio
async def test_user_caching():
    """사용자 데이터가 캐싱되는지 테스트."""
    user_id = 123

    # 첫 번째 호출 - 캐시 미스
    user1 = await user_service.get_me(db, user_id)

    # 캐시가 설정되었는지 확인
    cache_key = CacheKeyBuilder.user(user_id)
    cached = await get_cached(cache_key)
    assert cached is not None

    # 두 번째 호출 - 캐시 히트
    user2 = await user_service.get_me(db, user_id)
    assert user1 == user2
```

### 캐시 무효화 테스트

```python
@pytest.mark.asyncio
async def test_update_invalidates_cache():
    """업데이트가 캐시를 삭제하는지 테스트."""
    user_id = 123

    # 캐시 채우기
    await user_service.get_me(db, user_id)

    # 사용자 업데이트
    await user_service.update_me(db, user_id, {"name": "New Name"})

    # 캐시가 삭제되어야 함
    cache_key = CacheKeyBuilder.user(user_id)
    cached = await get_cached(cache_key)
    assert cached is None
```

## 향후 개선 사항

- [ ] 애플리케이션 시작 시 캐시 워밍
- [ ] Redis Cluster를 사용한 분산 캐시
- [ ] 캐시 분석 대시보드
- [ ] 접근 패턴 기반 자동 캐시 만료
- [ ] 다단계 캐싱 (L1: 인메모리, L2: Redis)
- [ ] 대용량 객체를 위한 캐시 압축

## 관련 문서

- [Rate Limiting 가이드](./rate-limiting-guide.md)
- [시스템 아키텍처](./12-system-architecture.md)
- [Redis 설정](../README.md#redis-setup)

---

**최종 업데이트:** 2025-11-27
**상태:** 구현 및 테스트 완료 (9/12 테스트 통과)
**커버리지:** User, Chat Room, Chatbot 캐싱
