---
source_url: https://wikidocs.net/340825
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## Chapter 15. Codex로 버그 수정과 테스트 자동화

이 챕터에서는 Codex를 활용하여 버그를 체계적으로 수정하고, 기존 코드에 대한 테스트를 자동으로 생성하는 방법을 배웁니다. GitHub Issue 기반의 버그 수정 워크플로를 실습하고, CI/CD 파이프라인과 Codex를 연동하는 방법도 살펴봅니다.

* * *

## 버그 수정 워크플로

Codex를 활용한 버그 수정은 다음 흐름으로 진행됩니다.
    
    
    GitHub Issue 생성
           ↓
    Codex 태스크 할당 (Issue 내용 + 에러 로그 첨부)
           ↓
    Codex: 코드 분석 → 원인 파악 → 수정 → 테스트 실행
           ↓
    결과 리뷰 (diff + 터미널 로그 확인)
           ↓
    PR 생성 → 코드 리뷰 → 머지 → Issue 자동 클로즈
    

### GitHub Issue 기반 버그 수정

GitHub Issue를 Codex 태스크의 출발점으로 활용하면 버그 추적과 수정 이력을 한 곳에서 관리할 수 있습니다.

**효과적인 버그 리포트 Issue 작성법:**
    
    
    ## 버그 설명
    로그인 시 비밀번호 검증이 대소문자를 구분하지 않는 버그
    
    ## 재현 방법
    1. 사용자 등록: email=test@example.com, password=MyPass123
    2. 다음 비밀번호로 로그인 시도: mypass123 (소문자)
    3. 로그인 성공됨 (기대 결과: 401 Unauthorized)
    
    ## 기대 결과
    비밀번호는 대소문자를 구분해야 하며, 잘못된 비밀번호로 로그인 시 401을 반환해야 함
    
    ## 실제 결과
    잘못된 비밀번호로도 로그인에 성공함
    
    ## 에러 로그
    없음 (서버 로그에 에러 없이 200 반환)
    
    ## 환경
    - Python 3.11
    - Flask 3.0.0
    - OS: Ubuntu 22.04
    

### 에러 메시지 기반 디버깅 요청

에러 로그가 있는 경우, 로그를 그대로 Codex 태스크에 포함하면 더 정확한 수정이 가능합니다.
    
    
    다음 에러를 수정해주세요.
    
    에러 메시지:
    

Traceback (most recent call last): File "app.py", line 47, in get\_user user = User.query.filter\_by(id=user\_id).first() File "/usr/local/lib/python3.11/site-packages/sqlalchemy/orm/query.py", line 1234 raise TypeError("unsupported operand type(s)") TypeError: unsupported operand type(s) for user\_id comparison
    
    
    발생 상황: GET /api/users/{user_id} 호출 시 user_id가 문자열로 전달될 때 발생
    
    수정 내용:
    - user_id를 정수로 변환하는 검증 추가
    - 변환 실패 시 400 Bad Request 반환
    - 해당 케이스에 대한 테스트 추가
    

* * *

## 테스트 자동화

테스트 코드가 없거나 부족한 프로젝트에 Codex를 활용하면 빠르게 테스트 커버리지를 높일 수 있습니다.

### 기존 코드에 대한 테스트 자동 생성
    
    
    [테스트 생성 태스크 예시]
    services/user_service.py 파일의 모든 함수에 대한 pytest 테스트를 생성해주세요.
    
    대상 함수:
    - create_user(email, password, nickname)
    - get_user_by_id(user_id)
    - update_user_profile(user_id, nickname)
    - delete_user(user_id)
    - verify_password(plain_password, hashed_password)
    
    테스트 요구사항:
    - 각 함수에 대해 정상 케이스 1개 이상
    - 예외 케이스 (존재하지 않는 user_id, 유효하지 않은 입력 등) 포함
    - pytest fixture를 활용하여 테스트 데이터 설정
    - tests/test_user_service.py 파일에 작성
    
    현재 테스트 커버리지 목표: 80% 이상
    커버리지 확인 명령: pytest --cov=services tests/ --cov-report=term-missing
    

### pytest를 활용한 테스트 프레임워크 구성

Codex가 테스트를 잘 생성하려면 테스트 인프라가 갖춰져 있어야 합니다. 다음은 Flask 프로젝트의 표준 테스트 구성입니다.
    
    
    # tests/conftest.py
    import pytest
    from app import create_app
    
    @pytest.fixture
    def app():
        """테스트용 Flask 앱 인스턴스 생성"""
        app = create_app(config='testing')
        yield app
    
    @pytest.fixture
    def client(app):
        """테스트 HTTP 클라이언트"""
        return app.test_client()
    
    @pytest.fixture
    def sample_user():
        """테스트용 사용자 데이터"""
        return {
            'email': 'test@example.com',
            'password': 'TestPass123!',
            'nickname': '테스트유저'
        }
    
    
    
    # tests/test_auth.py (Codex가 생성하는 테스트 예시)
    import pytest
    
    def test_login_success(client, sample_user):
        """정상적인 로그인 테스트"""
        # 사용자 등록
        client.post('/api/auth/register', json=sample_user)
    
        # 로그인
        response = client.post('/api/auth/login', json={
            'email': sample_user['email'],
            'password': sample_user['password']
        })
    
        assert response.status_code == 200
        data = response.get_json()
        assert 'access_token' in data
    
    def test_login_wrong_password(client, sample_user):
        """잘못된 비밀번호로 로그인 실패 테스트"""
        client.post('/api/auth/register', json=sample_user)
    
        response = client.post('/api/auth/login', json={
            'email': sample_user['email'],
            'password': 'wrongpassword'
        })
    
        assert response.status_code == 401
    
    def test_login_case_sensitive_password(client, sample_user):
        """비밀번호 대소문자 구분 테스트"""
        client.post('/api/auth/register', json=sample_user)
    
        # 소문자로 변환된 비밀번호로 로그인 시도
        response = client.post('/api/auth/login', json={
            'email': sample_user['email'],
            'password': sample_user['password'].lower()
        })
    
        # 반드시 실패해야 함
        assert response.status_code == 401
    

### Jest를 활용한 JavaScript 테스트

JavaScript/Node.js 프로젝트의 경우에도 동일하게 활용할 수 있습니다.
    
    
    [Jest 테스트 생성 태스크]
    src/utils/validation.js 파일의 모든 유틸리티 함수에 대한 Jest 테스트를 생성해주세요.
    
    - tests/__tests__/validation.test.js 파일에 작성
    - describe/it 블록으로 구조화
    - 각 함수에 대해 유효/무효 입력 케이스 포함
    - 테스트 실행: npm test
    

tip

테스트 생성 태스크를 실행하기 전에 `conftest.py` (pytest) 또는 `jest.config.js` (Jest) 등 테스트 설정 파일을 미리 만들어두면 Codex가 더 일관성 있는 테스트를 생성합니다. 설정 파일이 없으면 Codex가 임의의 방식으로 테스트 구조를 잡을 수 있습니다.

* * *

## CI/CD 파이프라인과의 연동

### GitHub Actions와 Codex 활용

GitHub Actions를 설정하면 Codex가 생성한 PR에 대해 자동으로 테스트가 실행되어, 코드 품질을 지속적으로 검증할 수 있습니다.
    
    
    # .github/workflows/ci.yml
    name: CI Pipeline
    
    on:
      pull_request:
        branches: [ main ]
      push:
        branches: [ main ]
    
    jobs:
      test:
        runs-on: ubuntu-latest
    
        steps:
        - uses: actions/checkout@v4
    
        - name: Python 설정
          uses: actions/setup-python@v5
          with:
            python-version: '3.11'
    
        - name: 의존성 설치
          run: pip install -r requirements.txt
    
        - name: 테스트 실행
          run: pytest tests/ -v --cov=. --cov-report=xml
    
        - name: 커버리지 리포트 업로드
          uses: codecov/codecov-action@v4
          with:
            file: ./coverage.xml
    

이 설정을 AGENTS.md에 명시해두면 Codex가 PR 생성 후 CI가 통과하는지 스스로 확인합니다.
    
    
    # AGENTS.md 추가 내용
    ## CI/CD
    - PR 생성 후 GitHub Actions CI가 통과해야 합니다
    - 테스트 실패 시 수정 후 재실행
    - 커버리지 80% 미만 시 추가 테스트 작성 필요
    

### PR 자동 생성과 리뷰 요청

Codex는 태스크 완료 후 자동으로 PR을 생성합니다. PR에는 다음이 포함됩니다.

항목 | 내용  
---|---  
PR 제목 | 태스크 내용을 요약한 제목  
PR 설명 | 변경 사항 요약, 테스트 결과  
관련 Issue | "Closes \#이슈번호" 자동 링크  
  
* * *

## 실습: GitHub Issue 기반 버그 수정과 PR 생성

**실습 시나리오** : 로그인 시 비밀번호 검증이 대소문자를 구분하지 않는 버그를 수정하고, 관련 테스트를 추가한 후 PR을 생성합니다.

**1단계: 버그가 있는 코드 준비**

다음 코드를 `auth.py`로 만들어 GitHub에 푸시합니다.
    
    
    # auth.py - 버그가 있는 버전
    def verify_password(plain_password: str, stored_password: str) -> bool:
        """
        비밀번호를 검증합니다.
        버그: 대소문자를 구분하지 않는 비교를 사용하고 있음
        """
        # 버그: lower()로 변환하여 대소문자 구분이 사라짐
        return plain_password.lower() == stored_password.lower()
    
    
    
    git add auth.py
    git commit -m "Add auth module (with known bug for practice)"
    git push origin main
    

**2단계: GitHub Issue 생성**

GitHub 리포지토리의 Issues 탭에서 새 이슈를 생성합니다.
    
    
    제목: [Bug] 로그인 비밀번호 검증이 대소문자를 구분하지 않음
    
    본문:
    ## 버그 설명
    verify_password() 함수가 비밀번호를 소문자로 변환하여 비교하고 있어,
    대소문자가 다른 비밀번호로도 로그인이 성공합니다.
    
    ## 재현 방법
    ```python
    from auth import verify_password
    result = verify_password("mypass123", "MyPass123")
    print(result)  # True가 출력됨 (기대값: False)
    

## 기대 결과

비밀번호는 정확히 일치해야 합니다 (대소문자 포함). verify\_password("mypass123", "MyPass123") → False

## 수정 방법 제안

auth.py의 verify\_password() 함수에서 .lower() 변환 제거
    
    
    **3단계: Codex 태스크 작성**
    
    

Repository: codex-practice Branch: main

Task: Fix \#1 - 비밀번호 검증 대소문자 구분 버그 수정

버그 내용: auth.py의 verify\_password() 함수가 비밀번호를 lower()로 변환하여 비교하고 있어 대소문자가 다른 비밀번호로도 인증이 통과됩니다.

수정 내용: 1. auth.py의 verify\_password() 함수에서 .lower() 변환 제거 2. 실제 서비스에서는 해시 비교를 사용해야 하므로, bcrypt를 사용하는 올바른 구현으로 교체 (bcrypt.checkpw(plain\_password.encode(), hashed\_password))

테스트 추가 (tests/test\_auth.py): - test\_password\_case\_sensitive: 대소문자 다른 비밀번호로 검증 실패 확인 - test\_password\_exact\_match: 동일한 비밀번호로 검증 성공 확인 - test\_password\_different: 완전히 다른 비밀번호로 검증 실패 확인

PR 설명에 "Closes \#1" 포함
    
    
    **4단계: 결과 확인**
    
    

확인 체크리스트: [ ] auth.py에서 .lower() 코드가 제거되었는가 [ ] bcrypt 기반 비교로 올바르게 수정되었는가 [ ] 3개의 테스트 케이스가 모두 PASSED인가 [ ] PR 설명에 "Closes \#1"이 포함되어 있는가 \`\`\`

**5단계: PR 승인 및 머지**

모든 확인이 끝나면 PR을 머지합니다. GitHub에서 Issue \#1이 자동으로 Closed 상태로 변경되는 것을 확인합니다.

tip

실무에서는 버그를 수정할 때 반드시 **회귀 테스트(regression test)** 를 추가해야 합니다. 회귀 테스트란 해당 버그가 다시 발생하지 않는지 확인하는 테스트입니다. Codex에게 태스크를 지시할 때 "이 버그가 재현되지 않는지 확인하는 회귀 테스트를 포함해주세요"라고 명시하면 자동으로 추가됩니다.

이제 Chapter 16에서는 Codex를 더 넓은 범위의 실전 업무에 적용하는 고급 패턴을 배워봅니다.

* * *

---

**원본**: https://wikidocs.net/340825  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
