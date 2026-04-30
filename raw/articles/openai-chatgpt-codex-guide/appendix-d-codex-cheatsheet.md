---
source_url: https://wikidocs.net/340846
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

# D. Codex 명령어 및 워크플로 치트시트

## Codex 태스크 작성 패턴

### 기능 구현
```
Add [기능 이름] to [파일명 또는 모듈명]

예시:
Add pagination support to the UserListView in views/users.py
Add input validation for email and phone fields in models/user.py
Add retry logic with exponential backoff to api/client.py
```

### 버그 수정
```
Fix [이슈 설명] in [파일명]

예시:
Fix NullPointerException when user profile is missing in services/auth.py
Fix incorrect date format parsing in utils/datetime_helper.py
Fix memory leak in WebSocket connection handler in server/ws.py
```

### 리팩토링
```
Refactor [대상] to use [패턴 또는 기술]

예시:
Refactor UserService to use dependency injection pattern
Refactor database queries in models/order.py to use async/await
Refactor duplicated validation logic into a shared BaseValidator class
```

### 테스트 작성
```
Write tests for [모듈 또는 함수명]

예시:
Write unit tests for the calculate_discount function in utils/pricing.py
Write integration tests for the /api/v1/orders endpoint
Write edge case tests for the CSV parser in utils/importer.py
```

### 문서화
```
Generate [문서 유형] for [모듈 또는 파일]

예시:
Generate API docs for all endpoints in routes/api.py
Generate docstrings for all public functions in utils/helpers.py
Generate a README for the /scripts directory
```

---

## AGENTS.md 작성 가이드

AGENTS.md는 프로젝트 지침서로, Codex가 프로젝트를 이해하고 올바른 방식으로 작업할 수 있도록 안내합니다.

### AGENTS.md 기본 구조

```markdown
# AGENTS.md

## 프로젝트 개요
[프로젝트의 목적과 주요 기능을 2~3문장으로 설명]

예시:
이 프로젝트는 소상공인을 위한 재고 관리 SaaS 서비스입니다.
FastAPI 백엔드와 React 프론트엔드로 구성되어 있으며,
PostgreSQL을 주 데이터베이스로 사용합니다.

## 기술 스택
- Backend: Python 3.11, FastAPI, SQLAlchemy 2.0
- Frontend: React 18, TypeScript, Tailwind CSS
- Database: PostgreSQL 15, Redis (캐싱)
- 테스트: pytest, React Testing Library

## 코딩 컨벤션
- Python: PEP 8 준수, 타입 힌트 필수
- 함수명: snake_case, 클래스명: PascalCase
- 커밋 메시지: Conventional Commits 형식
- 줄 길이: 최대 88자 (black 포매터 기준)
- import 순서: stdlib → third-party → local

## 디렉토리 구조
src/
  api/        # FastAPI 라우터
  models/     # SQLAlchemy 모델
  services/   # 비즈니스 로직
  utils/      # 공통 유틸리티
tests/
  unit/
  integration/

## 테스트 명령어
# 전체 테스트 실행
pytest tests/ -v

# 특정 모듈 테스트
pytest tests/unit/test_inventory.py -v

# 커버리지 포함
pytest tests/ --cov=src --cov-report=term-missing

## 빌드 및 실행
# 개발 서버 실행
uvicorn src.main:app --reload --port 8000

# 도커 빌드
docker build -t inventory-api .
docker-compose up -d

## 주의 사항
- .env 파일에 민감 정보 저장 (절대 커밋 금지)
- 데이터베이스 마이그레이션은 Alembic 사용
- API 변경 시 반드시 OpenAPI 스펙 업데이트
```

---

## 효과적인 태스크 작성 팁 10가지

1. **구체적인 파일 경로를 명시하세요** — "src/models/user.py의 User 클래스에 last_login 필드 추가"처럼 구체적으로 작성

2. **기대하는 동작을 명확히 설명하세요** — "로그인 실패 5회 이상 시 계정을 10분간 잠금"처럼 구체적 기술

3. **관련 파일을 함께 언급하세요** — services/user.py, repositories/user.py 등 연관 파일 명시

4. **완료 조건을 포함하세요** — "pytest 테스트가 모두 통과해야 함" 같은 완료 기준 명시

5. **변경하지 말아야 할 것을 명시하세요** — 보존할 인터페이스와 API 응답 형식 명확화

6. **코딩 스타일 기준을 AGENTS.md에 정의하세요** — 매 태스크마다 지정하는 대신 미리 한 번 정의

7. **크고 복잡한 태스크는 분리하세요** — 작은 단위로 순차 분해 (1. 모델 → 2. 서비스 → 3. API → 4. 테스트)

8. **에러 메시지를 그대로 붙여넣으세요** — 실제 스택 트레이스 포함으로 정확한 원인 파악

9. **예상 입출력을 예시로 제공하세요** — "[1,3,2]를 받아 [1,2,3]을 반환" 같은 구체적 예시

10. **샌드박스 모드로 먼저 검토하세요** — `codex --sandbox` 옵션으로 변경 내용 사전 확인

---

## 자주 하는 실수와 해결법

| 실수 | 증상 | 해결 방법 |
|------|------|---------|
| 모호한 태스크 설명 | 엉뚱한 파일이 수정됨 | 파일 경로와 함수명을 명시 |
| AGENTS.md 미작성 | 컨벤션 불일치, import 오류 | 프로젝트 루트에 AGENTS.md 생성 |
| 테스트 명령어 누락 | 기존 테스트가 깨져도 모름 | AGENTS.md에 테스트 명령어 기재 |
| 너무 큰 태스크 | 중간에 실패하거나 불완전한 구현 | 태스크를 작은 단위로 분리 |
| 환경 변수 미설정 | 실행 중 인증 오류 | .env 파일 확인 및 AGENTS.md에 필요 변수 목록 기재 |

---

**원본**: https://wikidocs.net/340846
**저자**: 송영옥 (CC BY)
**책 페이지**: https://wikidocs.net/book/19558
**마지막 편집**: 2026-04-12
