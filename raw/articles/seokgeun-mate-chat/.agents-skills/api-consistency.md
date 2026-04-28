---
name: api-consistency
description: >
  Mate Chat에서 FastAPI 엔드포인트를 추가하거나 수정할 때 API 표준을 자동으로 적용합니다.
  타입 힌트, Pydantic 스키마, async/await 사용, 네이밍 규칙, 에러 처리 패턴을 자동으로 검사합니다.
  API 엔드포인트를 생성하거나 수정할 때 자동으로 실행됩니다.
allowed-tools:
  - Read
  - Grep
  - Edit
---

# API 일관성 검사기

Mate Chat의 API 엔드포인트 표준을 자동으로 적용하여 일관성 있고 고품질의 코드를 보장합니다.

## 개요

**Mate Chat**: 10개의 엔드포인트 파일에 **83개의 API 엔드포인트**

이 스킬은 [AGENTS.md](/home/ubuntu/projects/mate-chat/AGENTS.md)에 정의된 프로젝트 표준에 따라 새로운 또는 수정된 FastAPI 엔드포인트를 자동으로 검사합니다.

**일관성의 중요성**:
- 유지보수성 향상
- 코드 품질 보장
- 개발자 온보딩 가속화
- API 사용성 개선

---

## 관련 시스템

**Slash Command:** `/api` (사용자 명시적 호출)
- 사용자가 `/api create user endpoint` 형식으로 API 작업 시작
- FastAPI 엔드포인트 생성/수정 작업을 명시적으로 시작

**Sub-Agent:** `fastapi-backend-expert` (자동 호출)
- 복잡한 API 설계 및 구현 시 자동으로 호출되는 전문가 에이전트
- Router → Service → Repository → Model 전체 아키텍처 구현
- 트리거 조건: 새 엔드포인트 생성, 복잡한 비즈니스 로직, 다중 레이어 구현

**Agent Skill:** `api-consistency` (이 스킬 - 자동 트리거)
- 트리거: API 엔드포인트 코드 작성 완료 시 자동 실행
- 역할: 타입 힌트, Pydantic 스키마, async/await 패턴 표준 준수 자동 검증

**차이점:**
- **Slash Command (`/api`)**: 사용자가 명시적으로 입력하여 작업 시작
- **Sub-Agent (`fastapi-backend-expert`)**: 복잡한 구현 시 자동 호출되는 전문가
- **Agent Skill (`api-consistency`)**: 코드 작성 후 자동으로 표준 검증

---

## Mate Chat API 표준

상세한 예제와 패턴은 [api-patterns.md](./references/api-patterns.md)를 참조하세요.

### 1. 타입 힌트 (필수)

**요구사항**:
- 모든 매개변수에 타입 힌트 필수
- 반환 타입 명시 (`-> UserResponse`)
- 데코레이터에 `response_model` 사용
- 적절한 모듈에서 타입 임포트

```python
@router.get("/users/{user_id}", response_model=UserResponse)
async def get_user(
    user_id: int,
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
) -> UserResponse:
    ...
```

### 2. Async/Await (필수)

**요구사항**:
- 모든 엔드포인트 함수는 `async def`
- `Session`이 아닌 `AsyncSession` 사용
- 데이터베이스 호출에 `await` 사용
- 블로킹 작업 금지

```python
async def get_users(db: AsyncSession = Depends(get_db)) -> list[UserResponse]:
    result = await db.execute(select(User))
    return result.scalars().all()
```

### 3. Pydantic 스키마 (필수)

**요구사항**:
- 요청 본문에 Pydantic 스키마 사용
- 응답에 Pydantic 스키마 사용 (`response_model`)
- `dict` 또는 `Any` 타입 사용 금지
- `app/schemas/`에 스키마 정의

```python
@router.post("/users", response_model=UserResponse, status_code=201)
async def create_user(
    user_data: UserCreate,  # Pydantic 스키마
    db: AsyncSession = Depends(get_db)
) -> UserResponse:
    ...
```

### 4. 에러 처리 (필수)

**요구사항**:
- 에러 처리에 `HTTPException` 사용
- `fastapi.status`의 상태 코드 사용
- 의미 있는 에러 메시지 제공
- 모든 에러 케이스 처리

```python
from fastapi import HTTPException, status

user = await db.get(User, user_id)
if not user:
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )
```

### 5. 네이밍 규칙 (필수)

**요구사항**:
- 함수명: `snake_case`
- 경로 매개변수: `snake_case` (`/users/{user_id}`)
- 쿼리 매개변수: `snake_case`
- 변수명: `snake_case`
- 클래스명 (스키마): `PascalCase`

```python
@router.get("/users/{user_id}")  # ✅ snake_case 경로
async def get_user(user_id: int):  # ✅ snake_case 함수명
    ...
```

### 6. HTTP 메서드 & 상태 코드 (필수)

**요구사항**:
- 작업에 맞는 올바른 HTTP 메서드 사용
- 적절한 상태 코드 반환
  - 생성: 201 Created
  - 성공적인 삭제: 204 No Content
  - 성공적인 조회/업데이트: 200 OK

```python
# POST - 생성 (201)
@router.post("/users", status_code=status.HTTP_201_CREATED)

# DELETE - 삭제 (204)
@router.delete("/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
```

### 7. 인증 (보호된 엔드포인트에 필수)

**요구사항**:
- 보호된 엔드포인트에 `get_current_user` 의존성 사용
- `current_user` 매개변수로 사용자 전달
- 공개 엔드포인트는 명시적으로 문서화

```python
from app.core.auth import get_current_user

@router.get("/users/me", response_model=UserResponse)
async def get_current_user_profile(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)  # 인증
) -> UserResponse:
    return current_user
```

### 8. OpenAPI 문서 (필수)

**요구사항**:
- `summary` 매개변수 (짧은 제목)
- `description` 매개변수 (상세 설명)
- 함수 docstring
- 스키마의 매개변수 설명

```python
@router.get(
    "/users/{user_id}",
    response_model=UserResponse,
    summary="ID로 사용자 조회",
    description="사용자 ID로 사용자의 공개 프로필 정보를 조회합니다"
)
async def get_user(user_id: int, ...) -> UserResponse:
    """ID로 사용자를 조회합니다."""
    ...
```

전체 예제 및 CRUD 패턴은 [api-patterns.md](./references/api-patterns.md)를 참조하세요.

---

## 체크리스트

엔드포인트를 생성하거나 수정할 때:

- [ ] **타입 힌트**: 모든 매개변수와 반환 타입
- [ ] **Async/Await**: `async def` + `await` 사용
- [ ] **Pydantic 스키마**: 요청/응답에 스키마 사용
- [ ] **에러 처리**: HTTPException으로 모든 에러 케이스 처리
- [ ] **네이밍**: snake_case (함수, 경로, 매개변수)
- [ ] **HTTP 메서드**: 올바른 메서드 (GET/POST/PUT/PATCH/DELETE)
- [ ] **상태 코드**: 적절한 상태 코드 (200/201/204)
- [ ] **인증**: 보호된 엔드포인트에 `get_current_user`
- [ ] **문서화**: summary, description, docstring
- [ ] **Rate Limiting**: 필요시 rate limiter 적용
- [ ] **테스트**: 새 엔드포인트에 대한 테스트 작성

---

## 자동 검사 항목

이 스킬은 다음을 자동으로 검사합니다:

1. ✅ 타입 힌트 누락
2. ✅ 동기 함수 (`def` 대신 `async def`)
3. ✅ response_model 누락
4. ✅ dict 타입 사용
5. ✅ 인증 누락 (보호된 엔드포인트)
6. ✅ Docstring 누락

---

## 참조 파일

### 상세 가이드
- **[api-patterns.md](./references/api-patterns.md)** - 완전한 CRUD 패턴, 상세 예제, 모범 사례, 안티패턴
- **[AGENTS.md](/home/ubuntu/projects/mate-chat/AGENTS.md)** - 프로젝트 전체 코드 스타일 규칙

---

## 관련 스킬

- **feature-workflow**: 전체 기능 개발 프로세스
- **security-review**: 인증 엔드포인트 보안 검사
- **doc-sync**: API 변경 후 문서 업데이트

---

**기억하세요**: 83개의 엔드포인트에서 일관성을 유지하려면 규율이 필요합니다!
