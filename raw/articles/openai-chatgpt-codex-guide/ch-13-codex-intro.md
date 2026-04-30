---
source_url: https://wikidocs.net/340823
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## Chapter 13. Codex 소개와 시작하기

이 챕터에서는 OpenAI Codex가 무엇인지, 기존 AI 코딩 도구와 어떻게 다른지 살펴보고, 직접 GitHub 리포지토리를 연동하여 첫 번째 Codex 태스크를 실행하는 실습까지 진행합니다.

* * *

## Codex란 무엇인가?

**OpenAI Codex**는 2025년 출시된 **클라우드 기반 자율 코딩 에이전트(Cloud-based Autonomous Coding Agent)** 입니다. 단순히 코드 자동완성을 제안하는 기존 AI 도구와 달리, Codex는 독립적인 클라우드 샌드박스 환경에서 실제로 코드를 읽고, 수정하고, 실행하며, 테스트까지 수행합니다.

개발자는 채팅창에 자연어로 "이 기능을 구현해줘", "이 버그를 수정해줘"라고 요청하면, Codex가 GitHub 리포지토리를 탐색하고 코드를 작성한 뒤 Pull Request(PR)를 직접 생성합니다. 개발자는 PR을 리뷰하고 승인만 하면 됩니다.

Codex의 핵심 특징을 정리하면 다음과 같습니다.

특징 | 설명  
---|---  
클라우드 샌드박스 실행 | 격리된 환경에서 코드 읽기/쓰기/실행을 자율적으로 처리  
codex-1 모델 기반 | o3 모델에서 파생된 코딩 특화 추론 모델  
GitHub 직접 연동 | 리포지토리를 클론하여 실제 코드베이스에서 작업  
병렬 태스크 처리 | 여러 태스크를 동시에 실행하여 개발 속도 향상  
  
* * *

## Codex vs GitHub Copilot vs Claude Code 비교

Codex를 처음 접하면 기존에 알고 있던 GitHub Copilot이나 Claude Code와 어떻게 다른지 궁금할 수 있습니다. 세 도구의 차이를 명확히 이해하면 상황에 맞게 적절한 도구를 선택할 수 있습니다.

구분 | Codex (OpenAI) | GitHub Copilot | Claude Code  
---|---|---|---  
동작 방식 | 클라우드 자율 에이전트 | IDE 인라인 자동완성 | CLI 인터랙티브 대화  
실행 환경 | 클라우드 샌드박스 (원격) | 로컬 IDE (VS Code 등) | 로컬 터미널  
GitHub 연동 | 자동 PR 생성 | 코드 제안 수준 | 수동 커밋/푸시 필요  
주요 강점 | 병렬 자율 처리, 대규모 작업 | 실시간 코드 제안, IDE 통합 | 대화형 정밀 제어  
주요 약점 | 세밀한 실시간 제어 어려움 | 복잡한 멀티파일 작업 한계 | 수동 조작 필요  
tip

세 도구는 서로 대체재가 아니라 **보완재** 입니다. 일상적인 코드 작성에는 Copilot, 정밀한 대화형 작업에는 Claude Code, 대규모 자동화 태스크에는 Codex를 사용하는 방식으로 조합하면 가장 효율적입니다.

* * *

## Codex 접근 방법과 요금제

Codex는 ChatGPT 인터페이스를 통해 사용합니다. 현재 다음 요금제에서 이용 가능합니다.

요금제 | Codex 접근 | 비고  
---|---|---  
ChatGPT Pro | 사용 가능 | 월 $200, 개인 고급 사용자  
ChatGPT Team | 사용 가능 | 월 $25/인, 팀 협업  
ChatGPT Enterprise | 사용 가능 | 기업용, 보안 강화  
ChatGPT Plus | 제한적 | 일부 기능만 제공  
  
ChatGPT에 로그인한 후 좌측 사이드바에서 **Codex** 메뉴를 클릭하거나, 대화창 상단의 모델 선택에서 **codex-1** 을 선택하여 시작할 수 있습니다.

* * *

## 환경 설정: GitHub 연동

Codex를 사용하려면 먼저 GitHub 리포지토리를 연동해야 합니다. 다음 단계를 따라 설정합니다.

**1단계: GitHub 연동 설정**

  1. ChatGPT에서 Codex 메뉴로 이동합니다.
  2. 화면 상단의 **Connect GitHub** 버튼을 클릭합니다.
  3. GitHub 계정으로 로그인하고 OpenAI 앱에 권한을 부여합니다.
  4. Codex가 접근할 리포지토리를 선택합니다 (전체 또는 특정 리포지토리).


**2단계: 리포지토리 선택**

연동이 완료되면 Codex 대화창에서 작업할 리포지토리를 선택합니다.
    
    
    1. Codex 화면에서 "New Task" 클릭
    2. "Repository" 드롭다운에서 연동된 리포지토리 선택
    3. 작업할 브랜치 선택 (기본값: main)
    

* * *

## AGENTS.md 파일 설정

**AGENTS.md**는 Codex에게 프로젝트의 코딩 컨벤션, 테스트 방법, 주의사항 등을 알려주는 **지시 문서** 입니다. 리포지토리 루트에 이 파일을 배치하면 Codex가 매 태스크마다 자동으로 읽고 참고합니다.

좋은 AGENTS.md는 Codex의 작업 품질을 크게 향상시킵니다. 다음은 Python 프로젝트를 위한 AGENTS.md 예시입니다.
    
    
    # AGENTS.md
    
    ## 프로젝트 개요
    이 프로젝트는 Flask 기반 REST API 서버입니다.
    Python 3.11을 사용하며, 모든 코드는 PEP 8 스타일을 따릅니다.
    
    ## 코딩 컨벤션
    - 들여쓰기: 4 스페이스
    - 최대 줄 길이: 88자 (Black 포매터 기준)
    - 타입 힌트를 반드시 사용할 것
    - docstring은 Google 스타일로 작성
    
    ## 테스트
    - 테스트 프레임워크: pytest
    - 테스트 파일 위치: tests/ 디렉터리
    - 새 기능 추가 시 반드시 테스트 코드를 함께 작성
    - 테스트 실행 명령: `pytest tests/ -v`
    
    ## 환경 설정
    - 의존성 설치: `pip install -r requirements.txt`
    - 환경 변수: `.env.example` 참고
    
    ## 브랜치 전략
    - 기능 개발: feature/기능명
    - 버그 수정: fix/버그명
    - PR 생성 전 테스트를 반드시 통과할 것
    

tip

AGENTS.md에 테스트 실행 명령을 명시하면 Codex가 코드를 작성한 후 자동으로 테스트를 실행하고 결과를 확인합니다. 이 과정이 없으면 Codex가 테스트를 건너뛸 수 있으니 반드시 포함하세요.

* * *

## 환경 변수와 Setup Script

Codex 샌드박스 환경에서 API 키나 데이터베이스 연결 정보가 필요한 경우, ChatGPT Codex 설정 화면에서 **환경 변수** 를 등록할 수 있습니다.
    
    
    # 환경 변수 등록 예시 (Codex 설정 화면에서 입력)
    DATABASE_URL=postgresql://user:pass@localhost/mydb
    REDIS_URL=redis://localhost:6379
    SECRET_KEY=your-secret-key-here
    

또한 AGENTS.md에 **setup script** 를 지정하면 Codex가 태스크 시작 전 의존성을 자동으로 설치합니다.
    
    
    ## Setup
    태스크 시작 전 다음 명령을 실행하세요:
    ```bash
    pip install -r requirements.txt
    python manage.py migrate
    
    
    
    &nbsp;
    
    ---
    
    &nbsp;
    
    ## 실습: 첫 번째 Codex 태스크 실행하기
    
    지금까지 배운 내용을 바탕으로 실제 GitHub 리포지토리를 연동하고 첫 번째 Codex 태스크를 실행해 봅니다.
    
    **실습 목표**: 간단한 Python 프로젝트에 Codex를 연동하고, "Hello World" API 엔드포인트를 추가하는 태스크를 실행한다.
    
    **사전 준비**
    
    ```bash
    # 1. 실습용 리포지토리 생성 (GitHub에서)
    # Repository name: codex-practice
    # 초기화: README.md 포함
    
    # 2. 로컬에 클론
    git clone https://github.com/YOUR_USERNAME/codex-practice.git
    cd codex-practice
    
    # 3. 기본 Flask 앱 파일 생성
    
    
    
    # app.py (초기 파일)
    from flask import Flask
    
    app = Flask(__name__)
    
    @app.route('/')
    def index():
        return {'message': 'Welcome to Codex Practice!'}
    
    if __name__ == '__main__':
        app.run(debug=True)
    
    
    
    # requirements.txt
    flask==3.0.0
    pytest==7.4.0
    

**GitHub에 푸시하기**
    
    
    git add .
    git commit -m "Initial Flask app setup"
    git push origin main
    

**AGENTS.md 추가하기**
    
    
    # AGENTS.md
    
    ## 프로젝트 개요
    Flask 기반 REST API 실습 프로젝트입니다.
    
    ## 코딩 컨벤션
    - Python 3.11, PEP 8 준수
    - 타입 힌트 사용
    
    ## 테스트
    - 테스트 실행: `pytest tests/ -v`
    - 새 엔드포인트 추가 시 테스트 코드 포함
    
    ## Setup
    ```bash
    pip install -r requirements.txt
    
    
    
    **Codex에서 첫 번째 태스크 실행**
    
    ChatGPT Codex 화면에서 다음과 같이 입력합니다.
    
    

Repository: codex-practice Branch: main

Task: `/health` 엔드포인트를 app.py에 추가해주세요. 이 엔드포인트는 GET 요청을 받아 \{"status": "ok", "timestamp": "현재시각"\} 형태의 JSON을 반환합니다. tests/test\_app.py 파일에 이 엔드포인트에 대한 pytest 테스트 코드도 함께 작성해주세요. \`\`\`

**결과 확인**

태스크가 완료되면 Codex가 다음을 보여줍니다.

  1. **변경된 파일 목록** : `app.py`, `tests/test_app.py`
  2. **diff 뷰** : 추가/수정된 코드 한눈에 확인
  3. **터미널 로그** : 테스트 실행 결과 (`pytest` 통과 여부)
  4. **PR 링크** : 자동 생성된 Pull Request URL

tip

첫 번째 태스크는 비교적 단순한 작업으로 시작하는 것이 좋습니다. Codex의 작업 방식과 결과물 형태를 먼저 파악한 뒤, 점차 복잡한 태스크로 확장해 나가세요.

이제 Chapter 14에서는 더 다양한 코드 작성 및 리팩토링 태스크를 Codex에 할당하는 방법을 배워봅니다.

* * *

---

**원본**: https://wikidocs.net/340823  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
