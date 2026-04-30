---
source_url: https://wikidocs.net/340824
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## Chapter 14. Codex로 코드 작성과 리팩토링

이 챕터에서는 Codex에 태스크를 효과적으로 할당하는 방법을 배우고, 코드 작성과 리팩토링 시나리오에서 Codex를 어떻게 활용하는지 실습합니다. Flask REST API에 CRUD 엔드포인트를 추가하는 전체 워크플로를 직접 따라해 봅니다.

* * *

## Codex에 태스크 할당하는 방법

Codex는 자연어 프롬프트로 지시합니다. 좋은 태스크 프롬프트는 Codex가 무엇을 해야 하는지 명확하게 이해할 수 있도록 다음 세 가지 요소를 포함합니다.

**좋은 태스크 프롬프트의 3요소**

요소 | 설명 | 예시  
---|---|---  
무엇을 할 것인가 | 작업의 목적과 내용 | "사용자 인증 API 추가"  
어떻게 할 것인가 | 기술 스택, 패턴, 컨벤션 | "JWT 기반, Flask-JWT-Extended 사용"  
어떻게 검증할 것인가 | 완료 기준, 테스트 방법 | "pytest로 테스트 커버리지 90% 이상"  
  
**나쁜 태스크 예시 vs 좋은 태스크 예시**
    
    
    # 나쁜 예시 (너무 모호함)
    로그인 기능 만들어줘
    
    # 좋은 예시 (구체적이고 검증 기준 포함)
    POST /api/auth/login 엔드포인트를 추가해주세요.
    - 요청 body: {"email": "string", "password": "string"}
    - 성공 시: {"access_token": "JWT 토큰", "expires_in": 3600} 반환 (HTTP 200)
    - 실패 시: {"error": "Invalid credentials"} 반환 (HTTP 401)
    - Flask-JWT-Extended 라이브러리 사용
    - tests/test_auth.py에 성공/실패 케이스 테스트 코드 포함
    

* * *

## 코드 작성 태스크 유형

Codex가 잘 처리하는 코드 작성 태스크 유형과 효과적인 프롬프트 패턴을 알아봅니다.

### 새로운 기능 구현

기존 코드베이스에 새로운 기능을 추가하는 가장 일반적인 태스크입니다.
    
    
    [프롬프트 템플릿]
    {기능 이름} 기능을 추가해주세요.
    
    요구사항:
    - {세부 요구사항 1}
    - {세부 요구사항 2}
    - {세부 요구사항 3}
    
    기술 조건:
    - 사용할 라이브러리: {라이브러리명}
    - 에러 처리: {에러 처리 방법}
    
    테스트:
    - {테스트 케이스 1}
    - {테스트 케이스 2}
    

**실제 예시:**
    
    
    사용자 프로필 조회 API를 추가해주세요.
    
    요구사항:
    - GET /api/users/{user_id} 엔드포인트
    - JWT 인증이 필요한 보호된 라우트
    - 존재하지 않는 user_id 요청 시 404 반환
    - 응답에 email, nickname, created_at 포함
    
    기술 조건:
    - Flask-JWT-Extended의 @jwt_required() 데코레이터 사용
    - SQLAlchemy ORM으로 데이터베이스 조회
    
    테스트:
    - 유효한 JWT로 본인 프로필 조회 성공
    - JWT 없이 요청 시 401 반환
    - 존재하지 않는 user_id 요청 시 404 반환
    

### 기존 코드 리팩토링

코드를 더 읽기 쉽고 유지보수하기 좋게 개선하는 태스크입니다.
    
    
    [비동기 변환 예시]
    user_service.py의 get_user_by_email() 함수를 async/await 패턴으로 변환해주세요.
    
    - 현재 동기 코드를 asyncio 기반 비동기 코드로 변경
    - 데이터베이스 호출에 asyncpg 사용
    - 기존 테스트 코드도 async 테스트로 업데이트 (pytest-asyncio 사용)
    - 함수 시그니처와 반환 타입은 유지
    
    
    
    [코드 구조 개선 예시]
    routes/users.py 파일의 라우트 핸들러를 리팩토링해주세요.
    
    현재 문제점:
    - 500줄 이상의 단일 파일에 모든 로직이 집중
    - 비즈니스 로직과 HTTP 처리 코드가 섞여 있음
    
    개선 방향:
    - 비즈니스 로직을 services/user_service.py로 분리
    - 데이터 검증 로직을 schemas/user_schema.py로 분리
    - 각 레이어에 대한 단위 테스트 추가
    

### 코드 변환 (마이그레이션)

기술 스택이나 언어 버전을 업그레이드할 때 활용하는 태스크입니다.
    
    
    [Python 2 → Python 3 마이그레이션 예시]
    src/ 디렉터리의 모든 Python 2 코드를 Python 3.11 호환 코드로 변환해주세요.
    
    변환 항목:
    - print 문 → print() 함수
    - unicode/str 타입 통일
    - dict.items() / dict.values() 이터레이터 처리
    - 예외 처리 구문 (except Exception, e → except Exception as e)
    - f-string 활용으로 문자열 포매팅 현대화
    
    변환 후 검증:
    - python -m py_compile으로 문법 오류 확인
    - 기존 테스트 전체 통과 여부 확인
    

* * *

## 효과적인 태스크 작성 팁

### 팁 1: 코딩 컨벤션을 AGENTS.md에 위임하라

매번 태스크 프롬프트에 코딩 스타일을 명시하는 대신, AGENTS.md에 한 번만 정의해 두면 Codex가 자동으로 참고합니다. 태스크 프롬프트는 **무엇을 할 것인가** 에만 집중할 수 있습니다.

### 팁 2: 완료 기준을 구체적으로 명시하라
    
    
    # 모호한 완료 기준 (피할 것)
    테스트를 작성해주세요.
    
    # 명확한 완료 기준 (권장)
    다음 테스트를 작성해주세요:
    1. 정상 케이스: 유효한 입력으로 200 반환 확인
    2. 경계 케이스: 빈 문자열, null 값 입력 처리
    3. 에러 케이스: 중복 이메일 등록 시 409 반환 확인
    pytest 실행 시 모든 테스트가 통과해야 합니다.
    

### 팁 3: 단계적으로 태스크를 분할하라

대규모 기능을 한 번에 요청하기보다, 작은 단위로 나눠 순차적으로 실행하는 것이 더 안정적입니다.
    
    
    # 비추천: 한 번에 모두 요청
    사용자 관리 시스템 전체를 구현해주세요 (회원가입, 로그인, 프로필, 탈퇴)
    
    # 추천: 단계적 분할
    1단계: 사용자 모델과 데이터베이스 스키마 생성
    2단계: 회원가입 API 구현
    3단계: 로그인 및 JWT 인증 구현
    4단계: 프로필 조회/수정 API 구현
    5단계: 회원 탈퇴 및 토큰 무효화 구현
    

tip

각 단계를 완료한 후 코드를 리뷰하고 머지하는 방식으로 진행하면, 문제가 생겼을 때 어느 단계에서 발생했는지 쉽게 파악할 수 있습니다. 큰 PR 하나보다 작은 PR 여럿이 리뷰하기도 훨씬 편합니다.

* * *

## Codex 작업 결과 리뷰 방법

Codex가 태스크를 완료하면 결과를 꼼꼼히 검토해야 합니다. 검토 순서는 다음과 같습니다.

**1. 터미널 로그 확인**

Codex가 작업 중 실행한 명령어와 출력 결과를 확인합니다. 테스트가 실패했거나 오류가 발생한 경우 이 로그에서 확인할 수 있습니다.
    
    
    # 터미널 로그 예시
    $ pip install -r requirements.txt
    Successfully installed flask-3.0.0 pytest-7.4.0
    
    $ pytest tests/ -v
    PASSED tests/test_app.py::test_health_endpoint
    PASSED tests/test_users.py::test_create_user
    PASSED tests/test_users.py::test_get_user
    
    3 passed in 0.52s
    

**2. diff 뷰로 변경 사항 확인**

Codex 화면에서 파일별 변경 사항(diff)을 확인합니다.

  * 초록색 줄(+): 추가된 코드
  * 빨간색 줄(-): 삭제된 코드
  * 의도하지 않은 변경이 없는지 주의 깊게 확인


**3. 승인 / 수정 요청 / 거부 결정**

결정 | 상황 | 액션  
---|---|---  
승인 | 결과물이 요구사항을 충족 | PR 머지 또는 승인 클릭  
수정 요청 | 작은 수정이 필요 | 추가 프롬프트로 수정 지시  
거부 | 결과물이 크게 벗어남 | 태스크 취소 후 재작성  
  
**수정 요청 예시:**
    
    
    이전 태스크 결과에서 수정이 필요합니다:
    - create_user() 함수에서 email 중복 체크가 빠져 있습니다.
      users 테이블에서 동일 email이 있으면 409 Conflict를 반환하도록 추가해주세요.
    - test_create_user_duplicate_email() 테스트 케이스도 추가해주세요.
    

* * *

## 실습: Flask REST API에 CRUD 엔드포인트 추가하기

Chapter 13에서 만든 `codex-practice` 리포지토리에 할 일(Todo) 관리를 위한 CRUD API를 추가하는 실습을 진행합니다.

**실습 목표** : Codex를 사용하여 Todo CRUD API를 구현하고, 테스트를 통과한 PR을 생성한다.

**현재 파일 구조 준비**

먼저 기본 모델 파일을 추가합니다. (이 파일은 직접 작성하여 GitHub에 푸시합니다)
    
    
    # models.py
    from datetime import datetime
    from typing import Optional
    
    # 실습에서는 간단히 메모리 딕셔너리를 DB 대신 사용합니다
    todos_db: dict = {}
    next_id: int = 1
    
    def get_all_todos() -> list:
        return list(todos_db.values())
    
    def get_todo(todo_id: int) -> Optional[dict]:
        return todos_db.get(todo_id)
    
    
    
    git add models.py
    git commit -m "Add basic Todo model structure"
    git push origin main
    

**Codex 태스크 프롬프트**
    
    
    Repository: codex-practice
    Branch: main
    
    Task:
    models.py를 활용하여 Todo CRUD REST API를 app.py에 구현해주세요.
    
    엔드포인트 명세:
    1. POST /api/todos
       - body: {"title": "string", "done": false}
       - 성공: 생성된 todo 객체 반환 (HTTP 201)
    
    2. GET /api/todos
       - 모든 todo 목록 반환 (HTTP 200)
    
    3. GET /api/todos/{id}
       - 특정 todo 반환 (HTTP 200)
       - 없으면 {"error": "Not found"} (HTTP 404)
    
    4. PUT /api/todos/{id}
       - body: {"title": "string", "done": boolean}
       - 수정된 todo 반환 (HTTP 200)
       - 없으면 404
    
    5. DELETE /api/todos/{id}
       - 성공: {"message": "Deleted"} (HTTP 200)
       - 없으면 404
    
    구현 조건:
    - Flask의 jsonify() 사용
    - 입력 검증: title이 빈 문자열이면 400 Bad Request 반환
    - models.py의 함수들 활용
    
    테스트:
    tests/test_todos.py 파일에 각 엔드포인트의 성공/실패 케이스 테스트 작성
    pytest 실행 시 전체 통과해야 함
    

**Codex 결과 확인 과정**

태스크가 완료되면 다음을 단계별로 확인합니다.
    
    
    1. 터미널 로그 확인
       → pytest 전체 통과 여부 확인
    
    2. diff 확인
       → app.py: 5개 엔드포인트 추가 여부
       → tests/test_todos.py: 테스트 케이스 충분한지 확인
    
    3. 누락된 케이스 추가 요청 (필요시)
       예: "POST /api/todos에서 done 필드가 없을 때 기본값 false로 설정하는 처리를 추가해주세요"
    

**PR 생성과 머지**

Codex가 생성한 PR로 이동하여 다음을 확인합니다.
    
    
    PR 체크리스트:
    [ ] PR 제목이 변경 사항을 잘 설명하는가
    [ ] 모든 테스트가 통과하는가 (CI 초록불)
    [ ] 코드 리뷰: 의도하지 않은 변경이 없는가
    [ ] AGENTS.md의 컨벤션을 준수하는가
    

모든 항목을 확인한 후 **Merge pull request** 를 클릭하여 main 브랜치에 머지합니다.

tip

Codex가 생성한 PR을 무조건 신뢰하지 마세요. 특히 보안과 관련된 코드(인증, 권한, SQL 쿼리 등)는 반드시 사람이 직접 리뷰해야 합니다. Codex는 강력한 보조 도구이지만 최종 책임은 개발자에게 있습니다.

이제 Chapter 15에서는 Codex를 활용하여 버그를 수정하고 테스트를 자동화하는 방법을 배워봅니다.

* * *

---

**원본**: https://wikidocs.net/340824  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:10 오후**
