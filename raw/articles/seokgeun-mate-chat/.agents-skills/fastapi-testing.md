---
name: fastapi-testing
description: >
  FastAPI 백엔드 테스팅 가이드와 예시를 제공합니다.
  pytest와 pytest-asyncio를 사용한 Unit, Integration, E2E 테스트 작성 패턴과 모범 사례를 제공하여
  FastAPI 백엔드의 품질을 보장합니다. 사용자가 FastAPI 엔드포인트 테스트를 작성하거나
  API 기능 검증이 필요할 때 사용합니다.
---

# FastAPI Testing

## 개요

FastAPI 백엔드의 단위 테스트, 통합 테스트, E2E 테스트를 작성하기 위한 가이드입니다.

**사용 시나리오:**
- FastAPI 엔드포인트 테스트 작성
- 서비스 로직 단위 테스트
- 데이터베이스 통합 테스트
- API 회귀 테스트 자동화

---

## 관련 시스템

**Slash Command:** `/test-gen` (사용자 명시적 호출)
- 사용자가 `/test-gen app/api/v1/endpoints/users.py` 형식으로 테스트 생성 요청

**Sub-Agent:** `fullstack-qa-engineer` (자동 호출)
- 복잡한 테스트 케이스 설계 및 커버리지 분석 시 자동으로 호출
- 트리거: 새 기능 테스트 작성, 테스트 실패 디버깅, 커버리지 분석

**Agent Skill:** `fastapi-testing` (이 스킬)
- FastAPI 테스트 작성 패턴 및 모범 사례 가이드 제공

**관련 스킬:**
- `api-consistency`: API 엔드포인트 표준
- `feature-workflow`: 전체 기능 개발 프로세스

---

## 테스트 유형

### 1. Unit Testing (단위 테스트)

**목적:** 개별 함수, 서비스 메서드, 유틸리티 테스트

**특징:**
- 가장 빠름
- 외부 의존성 없음 (모킹 사용)
- 비즈니스 로직 검증

**예시:**
```python
# tests/test_security.py
import pytest
from app.core.security import hash_password, verify_password

def test_hash_password():
    password = "SecurePass123!"
    hashed = hash_password(password)
    assert hashed != password
    assert verify_password(password, hashed) is True
```

**실행:**
```bash
uv run pytest tests/test_user_service.py -v
```

---

### 2. Integration Testing (통합 테스트)

**목적:** API 엔드포인트와 데이터베이스 통합 테스트

**특징:**
- 실제 데이터베이스 사용 (테스트 DB)
- HTTP 요청/응답 검증
- 엔드포인트 전체 플로우 테스트

**예시:**
```python
# tests/test_auth.py
@pytest.mark.asyncio
async def test_login_success(client: AsyncClient, db_session: AsyncSession):
    """로그인 성공 테스트"""
    user = User(
        email="test@example.com",
        password_hash=hash_password("password123"),
        email_verified=True
    )
    db_session.add(user)
    await db_session.commit()

    response = await client.post(
        "/v1/auth/login",
        json={"email": "test@example.com", "password": "password123"}
    )

    assert response.status_code == 200
    assert "access_token" in response.json()
```

**실행:**
```bash
uv run pytest tests/test_auth.py -v
```

---

### 3. E2E Testing (End-to-End 테스트)

**목적:** 전체 사용자 플로우를 순차적으로 테스트

**특징:**
- 여러 엔드포인트 연계 테스트
- 실제 사용자 시나리오 검증
- 가장 느리지만 가장 현실적

**예시:** 메이트 요청 → 수락 → 확인 전체 플로우

**실행:**
```bash
uv run pytest tests/test_social_flow.py -v
```

---

## 모범 사례

### 1. AAA 패턴 (Arrange-Act-Assert)

```python
@pytest.mark.asyncio
async def test_example(client: AsyncClient):
    # Arrange - 테스트 준비
    user = create_user(...)

    # Act - 실제 동작
    response = await client.post("/endpoint", json={...})

    # Assert - 검증
    assert response.status_code == 200
```

### 2. Fixtures 활용

Mate Chat 프로젝트의 주요 fixtures:
- `db_session`: 테스트 DB 세션
- `client`: HTTP 클라이언트
- `authenticated_client`: 인증된 클라이언트

**상세 가이드:** [fixtures_and_mocking.md](references/fixtures_and_mocking.md)

### 3. Mocking 전략

- **외부 API**: `@patch` 데코레이터 사용
- **Redis**: `FakeRedis` 사용
- **데이터베이스**: `AsyncMock` 사용

**상세 가이드:** [fixtures_and_mocking.md](references/fixtures_and_mocking.md)

### 4. Parametrize로 여러 케이스 테스트

```python
@pytest.mark.parametrize("email,password,expected_status", [
    ("valid@example.com", "ValidPass123!", 201),
    ("invalid-email", "ValidPass123!", 422),
    ("", "ValidPass123!", 422),
])
async def test_register_validation(client, email, password, expected_status):
    response = await client.post("/v1/auth/register", json={...})
    assert response.status_code == expected_status
```

### 5. 비동기 테스트

**올바른 사용:**
```python
# ✅ Good
@pytest.mark.asyncio
async def test_async_operation(db_session: AsyncSession):
    user = await create_user(db_session, "test@example.com")
    assert user.id is not None

# ❌ Bad - await 누락
@pytest.mark.asyncio
async def test_sync_style(db_session: AsyncSession):
    user = create_user(db_session, "test@example.com")  # 에러!
```

---

## 테스트 실행

### 기본 명령어

```bash
# 모든 테스트
uv run pytest

# 특정 파일
uv run pytest tests/test_auth.py -v

# 특정 함수
uv run pytest tests/test_auth.py::test_login_success -v

# 빠른 실패 (첫 실패 시 중단)
uv run pytest -x

# 상세 출력
uv run pytest -vv
```

### 커버리지

```bash
uv run pytest --cov=app --cov-report=term-missing
uv run pytest --cov=app --cov-report=html
open htmlcov/index.html
```

### 마커 필터링

```bash
# 느린 테스트 제외
uv run pytest -m "not slow"

# 통합 테스트만
uv run pytest -m integration
```

### 병렬 실행

```bash
uv run pytest -n auto  # CPU 코어 수만큼
```

---

## 테스트 데이터베이스 설정

### 환경변수

```bash
# .env.test
TEST_DATABASE_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/matechat_test
```

### 마이그레이션

```bash
alembic upgrade head
```

---

## 디버깅 팁

### Print 디버깅

```python
@pytest.mark.asyncio
async def test_with_debug(client: AsyncClient):
    response = await client.get("/v1/users/me")
    print(f"Status: {response.status_code}")
    print(f"Body: {response.json()}")
    assert response.status_code == 200
```

### 실패한 테스트만 재실행

```bash
uv run pytest --lf  # last failed
uv run pytest --ff  # failed first
```

---

## 체크리스트

새 기능에 테스트를 추가할 때:

- [ ] **Unit Tests**: 서비스 로직, 유틸리티 함수
- [ ] **Integration Tests**: API 엔드포인트 (성공/실패 케이스)
- [ ] **E2E Tests**: 전체 사용자 플로우 (필요 시)
- [ ] **Edge Cases**: 경계값, 에러 케이스
- [ ] **Parametrize**: 여러 입력값 테스트
- [ ] **Mocking**: 외부 의존성 모킹
- [ ] **Cleanup**: 테스트 후 데이터 정리 (롤백)
- [ ] **Coverage**: 70%+ 커버리지 목표

---

## 상세 예시

더 많은 예시와 패턴은 다음 파일을 참조하세요:

- **[test_examples.md](references/test_examples.md)** - Unit, Integration, E2E 테스트 전체 예시
- **[fixtures_and_mocking.md](references/fixtures_and_mocking.md)** - Fixtures와 Mocking 상세 가이드

---

## 참조

- **pytest**: https://docs.pytest.org/
- **pytest-asyncio**: https://pytest-asyncio.readthedocs.io/
- **HTTPX**: https://www.python-httpx.org/
- **Mate Chat 테스트**: `mate_chat_backend/tests/`
- **conftest.py**: `mate_chat_backend/tests/conftest.py`
