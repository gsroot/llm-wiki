---
name: feature-workflow
description: >
  Mate Chat에서 새로운 기능을 추가하거나 기능을 구현할 때 전체 스택 개발 워크플로우를 자동으로 안내합니다.
  트리거 키워드: "새 기능", "기능 추가", "새로운 기능", "feature", "implement", "add feature",
  "build feature". 백엔드 API, 프론트엔드 UI, 테스트, 문서 업데이트를 포함하여 Mate Chat
  소셜 메시징 플랫폼의 전체 개발 과정을 다룹니다.
allowed-tools:
  - Read
  - Glob
  - Grep
  - TodoWrite
context:
  fork: false
model: sonnet
user-invocable: true
---

# Feature 개발 워크플로우

Mate Chat에서 새로운 기능을 구현할 때, 전체 스택에 걸쳐 일관성, 품질, 완성도를 보장하기 위해 이 포괄적인 워크플로우를 따르세요.

## 개요

Mate Chat은 85% 완성된 풀스택 소셜 메시징 플랫폼입니다:
- **백엔드**: FastAPI (Python 3.13) + PostgreSQL + Redis
- **프론트엔드**: Flutter (Dart 3.10.1+) with Riverpod 상태 관리
- **실시간**: WebSocket 기반 메시징
- **AI 통합**: OpenAI GPT-4 하이브리드 채팅

## 워크플로우 단계

### 1. 요구사항 분석

먼저 기능 요구사항을 명확히 하세요:
- 사용자 대상 기능은 무엇인가?
- 어떤 컴포넌트가 영향을 받는가 (백엔드, 프론트엔드, 또는 둘 다)?
- 보안 고려사항이 있는가?
- 실시간 기능이 필요한가?
- AI 기능이 포함되는가?

### 2. 백엔드 개발 (해당되는 경우)

다음을 위해 [백엔드 체크리스트](./references/checklist.md#backend-checklist)를 따르세요:

1. **데이터 모델** (`app/models/`)
   - SQLAlchemy async 모델
   - 적절한 관계 및 인덱스
   - Created_at, updated_at 타임스탬프

2. **Pydantic 스키마** (`app/schemas/`)
   - Request/Response 모델
   - 검증 규칙
   - 타입 힌트 (필수!)

3. **서비스 레이어** (`app/services/`)
   - 비즈니스 로직 구현
   - Async 함수만 사용
   - HTTPException으로 에러 처리

4. **API 엔드포인트** (`app/api/v1/endpoints/`)
   - RESTful 설계
   - 적절한 HTTP 메서드
   - 인증/권한 부여
   - **AGENTS.md 코드 스타일 규칙을 반드시 따를 것**

5. **테스트** (`tests/`)
   - 서비스 단위 테스트
   - 엔드포인트 통합 테스트
   - 70%+ 커버리지 목표

### 3. 프론트엔드 개발 (해당되는 경우)

다음을 위해 [프론트엔드 체크리스트](./references/checklist.md#frontend-checklist)를 따르세요:

1. **Feature 구조** (`lib/features/{feature_name}/`)
   - `presentation/` - UI 화면 및 위젯
   - `application/` - Riverpod provider 및 상태
   - `data/` - API repository (선택사항)

2. **상태 관리** (Riverpod)
   - 복잡한 상태를 위한 StateNotifierProvider
   - 단순 값을 위한 Provider
   - 비동기 데이터를 위한 FutureProvider

3. **API 통합** (`lib/repositories/`)
   - Repository 패턴
   - 에러 처리
   - 로딩 상태

4. **라우팅** (`lib/core/routing/app_router.dart`)
   - GoRouter에 새 라우트 추가
   - 필요한 경우 Deep link 지원

5. **UI 컴포넌트**
   - `lib/ui/components/`에서 재사용
   - Material Design 3 테마
   - 반응형 레이아웃

### 4. 코드 품질 검사

**완료로 간주하기 전 필수:**

- ✅ 모든 타입 힌트 존재 (Python)
- ✅ Async/await 올바르게 사용
- ✅ `print()` 문 없음 (logger 사용)
- ✅ 적절한 에러 처리
- ✅ 테스트 작성 및 통과
- ✅ 린팅 에러 없음 (`ruff check .`)
- ✅ 코드 포맷팅 완료 (`ruff format .`)
- ✅ 타입 체크 통과 (`mypy .`)

### 5. 문서 업데이트

관련 문서 업데이트:
- AGENTS.md (완료율 % 변경 시)
- docs/ 디렉토리 (아키텍처 변경 시)
- API 문서 (Swagger 자동 문서)
- 사용자 대상 변경 시 README

### 6. 테스트

**백엔드:**
```bash
cd mate_chat_backend
uv run pytest -x -v tests/
```

**프론트엔드:**
```bash
cd mate_chat_flutter
flutter test
```

### 7. 리뷰

완료 전:
- [checklist.md](./references/checklist.md) 대조 검토
- 보안 고려사항 확인
- WebSocket 통합 확인 (해당되는 경우)
- AI 통합 작동 확인 (해당되는 경우)

## 예제 워크플로우

실제 기능(채팅방 초대)을 구현하는 전체 과정은 [examples/feature-example.md](./references/examples/feature-example.md)를 참조하세요.

## 주요 주의사항

1. **항상 `uv` 사용, `pip` 사용 금지** Python 패키지 관리용
2. **타입 힌트는 필수** 모든 Python 코드에
3. **Async/await 사용** - 동기 데이터베이스 호출 금지
4. **AGENTS.md 따르기** 코드 스타일 규칙 엄격히 준수
5. **테스트 커버리지 중요** - 70%+ 목표
6. **작업하면서 문서화** - 나중으로 미루지 말 것

## 다음 단계

기능 완료 후:
1. Todo 항목을 완료로 표시
2. 전체 테스트 스위트 실행
3. AGENTS.md 완료율 % 업데이트
4. `/commit` 실행하여 커밋 생성 고려
5. `/review` 실행하여 코드 리뷰 고려

## 관련 Skill

- **security-review**: 인증/보안 코드에 대해 자동 트리거
- **api-consistency**: API 엔드포인트 표준 검사
- **flutter-patterns**: Flutter 코드 패턴 강제
- **doc-sync**: 문서 업데이트 알림

---
