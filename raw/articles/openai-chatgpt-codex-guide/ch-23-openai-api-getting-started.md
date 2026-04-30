---
source_url: https://wikidocs.net/340835
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## OpenAI API란?

OpenAI API는 GPT-4o, o3 같은 OpenAI의 AI 모델을 여러분의 코드에서 직접 호출할 수 있는 인터페이스입니다. 웹 브라우저에서 ChatGPT와 대화하는 것과 원리는 같지만, API를 사용하면 다음과 같은 일이 가능해집니다.

  * 내 서비스나 앱에 AI 기능을 내장
  * 반복 작업(이메일 분류, 문서 요약 등)을 자동화
  * 외부 데이터베이스나 시스템과 AI를 연결
  * 수백 건의 요청을 배치로 처리


## 

## API 키 발급하기

OpenAI API를 사용하려면 먼저 API 키를 발급받아야 합니다.

**1단계: 계정 생성**

[platform.openai.com](https://platform.openai.com)에 접속하여 Sign Up을 클릭합니다. 기존 ChatGPT 계정이 있다면 같은 계정으로 로그인할 수 있습니다.

**2단계: API 키 생성**

  1. 로그인 후 우측 상단 프로필 → **API keys** 메뉴로 이동
  2. **Create new secret key** 버튼 클릭
  3. 키 이름을 입력하고 **Create secret key** 클릭
  4. 생성된 키를 **즉시 복사**합니다 — 창을 닫으면 다시 볼 수 없습니다

tip

API 키는 비밀번호와 같습니다. 코드에 직접 입력하지 말고 반드시 환경 변수나 별도의 설정 파일로 관리하세요. GitHub에 키가 노출되면 즉시 폐기하고 새로 발급받아야 합니다.

**3단계: 결제 수단 등록**

API 사용은 유료입니다. **Billing → Add payment method** 에서 카드를 등록하고, **Usage limits** 에서 월 사용 한도를 설정해두는 것을 권장합니다.

## 

## 개발 환경 설정

### Python 환경
    
    
    # OpenAI Python 라이브러리 설치
    pip install openai
    
    # 버전 확인
    python -c "import openai; print(openai.__version__)"
    

API 키를 환경 변수로 설정합니다.
    
    
    # macOS / Linux
    export OPENAI_API_KEY="sk-proj-..."
    
    # Windows (Command Prompt)
    set OPENAI_API_KEY=sk-proj-...
    
    # Windows (PowerShell)
    $env:OPENAI_API_KEY="sk-proj-..."
    

또는 프로젝트 루트에 `.env` 파일을 생성하고 `python-dotenv` 라이브러리를 활용합니다.
    
    
    pip install python-dotenv
    
    
    
    # .env 파일 내용
    OPENAI_API_KEY=sk-proj-...
    
    
    
    # Python 코드에서 불러오기
    from dotenv import load_dotenv
    load_dotenv()  # .env 파일 자동 로드
    

### JavaScript / Node.js 환경
    
    
    # Node.js 프로젝트 초기화 후 설치
    npm install openai
    
    # 환경 변수 설정 (.env 파일 사용 시)
    npm install dotenv
    
    
    
    // .env 파일
    OPENAI_API_KEY=sk-proj-...
    
    
    
    // Node.js 코드
    import OpenAI from "openai";
    
    const client = new OpenAI({
      apiKey: process.env.OPENAI_API_KEY,
    });
    

## 

## 첫 번째 API 호출

이제 실제로 GPT 모델을 호출해봅니다.
    
    
    from openai import OpenAI
    
    client = OpenAI()  # OPENAI_API_KEY 환경 변수 자동 인식
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 친절한 비서입니다."},
            {"role": "user", "content": "오늘 날씨 좋은데 점심 메뉴 추천해줘"}
        ]
    )
    
    print(response.choices[0].message.content)
    

코드를 실행하면 GPT-4o가 점심 메뉴를 추천해주는 응답이 출력됩니다.

## 

## Chat Completions API 구조 이해

### messages 배열과 역할(role)

역할 | 설명  
---|---  
system | AI의 성격, 역할, 행동 지침을 정의  
user | 사용자 입력 메시지  
assistant | AI의 이전 응답 (대화 히스토리 유지에 사용)  
  
대화 히스토리를 유지하려면 이전 메시지를 messages 배열에 누적해서 전달합니다.
    
    
    messages = [
        {"role": "system", "content": "당신은 요리 전문가입니다."},
        {"role": "user", "content": "파스타 레시피 알려줘"},
        {"role": "assistant", "content": "네! 기본 토마토 파스타 레시피를 알려드릴게요..."},
        {"role": "user", "content": "채식주의자 버전으로 수정해줘"}  # 이전 맥락을 기억
    ]
    

### 주요 파라미터

파라미터 | 설명 | 기본값  
---|---|---  
model | 사용할 모델 이름 | 필수  
temperature | 창의성 수준 (0.0~2.0, 낮을수록 일관성) | 1.0  
max\_tokens | 응답 최대 토큰 수 | 모델 기본값  
top\_p | 확률 누적 샘플링 (0.0~1.0) | 1.0  
tip

**temperature** 설정 가이드:

  * 0.0~0.3: 코드 생성, 데이터 분류 등 일관성이 중요한 작업
  * 0.7~1.0: 일반 대화, 설명
  * 1.2~1.8: 창의적 글쓰기, 브레인스토밍


### 응답 구조
    
    
    response = client.chat.completions.create(...)
    
    # 응답 텍스트
    print(response.choices[0].message.content)
    
    # 토큰 사용량 확인
    print(f"입력 토큰: {response.usage.prompt_tokens}")
    print(f"출력 토큰: {response.usage.completion_tokens}")
    print(f"총 토큰: {response.usage.total_tokens}")
    
    # 종료 이유 (stop / length / content_filter)
    print(f"종료 이유: {response.choices[0].finish_reason}")
    

## 

## 모델 선택 가이드

모델 | 특징 | 적합한 용도  
---|---|---  
gpt-4o | 최고 성능, 멀티모달 | 복잡한 분석, 이미지 처리  
gpt-4o-mini | 빠르고 저렴 | 간단한 분류, 요약, 대량 처리  
o3-mini | 추론 특화, 저렴 | 수학, 코딩, 논리 문제  
o3 | 최고 추론 능력 | 고난도 연구, 복잡한 계획  
  
일반적인 업무 자동화에는 **gpt-4o-mini** 가 속도와 비용 면에서 가장 효율적입니다. 복잡한 분석이나 고품질 결과가 필요할 때 **gpt-4o** 를 사용하세요.

## 

## 비용 관리

### 토큰 개념

API 비용은 토큰(token) 단위로 계산됩니다. 토큰은 단어보다 작은 텍스트 단위로, 영어는 약 4글자, 한국어는 약 2~3글자가 1토큰에 해당합니다.

  * "Hello world" → 약 2토큰
  * "안녕하세요" → 약 3~4토큰
  * A4 1페이지 분량 → 약 500~700토큰


### 비용 절감 전략
    
    
    # 1. max_tokens으로 응답 길이 제한
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 저렴한 모델 우선 사용
        messages=[...],
        max_tokens=200  # 필요한 만큼만 제한
    )
    
    # 2. 대량 처리 시 gpt-4o-mini 활용
    # 분류, 요약 등 단순 작업에는 미니 모델로도 충분
    

**Usage Limits 설정 방법** : platform.openai.com → Billing → Usage limits에서 월별 하드 한도를 설정하면 예상치 못한 과금을 방지할 수 있습니다.

### Rate Limit 이해와 대응

Rate Limit은 분당/일당 처리 가능한 요청 수와 토큰 수의 제한입니다. 제한에 걸리면 429 오류가 발생합니다.
    
    
    import time
    from openai import RateLimitError
    
    def call_with_retry(client, messages, max_retries=3):
        for attempt in range(max_retries):
            try:
                return client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages
                )
            except RateLimitError:
                wait_time = 2 ** attempt  # 지수 백오프: 1, 2, 4초
                print(f"Rate limit 초과. {wait_time}초 후 재시도...")
                time.sleep(wait_time)
        raise Exception("최대 재시도 횟수 초과")
    

## 

## 실습: 이메일 자동 분류기 만들기

이메일 내용을 입력하면 문의 / 불만 / 칭찬 / 기타 중 하나로 분류하는 프로그램을 만들어봅니다.
    
    
    from openai import OpenAI
    import json
    
    client = OpenAI()
    
    def classify_email(email_content: str) -> dict:
        """이메일 내용을 분류하고 요약을 반환합니다."""
    
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.1,  # 분류 작업은 낮은 temperature
            messages=[
                {
                    "role": "system",
                    "content": """이메일 내용을 분석하여 JSON 형식으로 반환하세요.
    
    반환 형식:
    {
      "category": "문의" | "불만" | "칭찬" | "기타",
      "priority": "높음" | "보통" | "낮음",
      "summary": "이메일 핵심 내용 한 줄 요약",
      "action_needed": true | false
    }"""
                },
                {
                    "role": "user",
                    "content": f"다음 이메일을 분류해주세요:\n\n{email_content}"
                }
            ],
            response_format={"type": "json_object"}  # JSON 응답 강제
        )
    
        return json.loads(response.choices[0].message.content)
    
    
    # 테스트
    emails = [
        "제품을 구매한 지 일주일도 안 됐는데 벌써 고장났어요. 정말 실망입니다.",
        "지난번에 구매한 노트북 정말 만족스럽습니다. 다음에도 여기서 살게요!",
        "A4 용지 대량 구매 시 할인이 되나요? 견적서도 받을 수 있을까요?"
    ]
    
    for i, email in enumerate(emails, 1):
        result = classify_email(email)
        print(f"\n[이메일 {i}]")
        print(f"  분류: {result['category']} | 우선순위: {result['priority']}")
        print(f"  요약: {result['summary']}")
        print(f"  조치 필요: {'예' if result['action_needed'] else '아니오'}")
    

실행 결과 예시:
    
    
    [이메일 1]
      분류: 불만 | 우선순위: 높음
      요약: 구매 일주일 내 제품 고장으로 인한 불만 접수
      조치 필요: 예
    
    [이메일 2]
      분류: 칭찬 | 우선순위: 낮음
      요약: 노트북 구매 만족도 높음, 재구매 의사 표시
      조치 필요: 아니오
    
    [이메일 3]
      분류: 문의 | 우선순위: 보통
      요약: A4 용지 대량 구매 할인 및 견적서 문의
      조치 필요: 예
    

tip

`response_format={"type": "json_object"}`를 지정하면 AI가 항상 유효한 JSON을 반환합니다. 단, system 또는 user 메시지에 반드시 "JSON 형식으로 반환" 등의 지시가 포함되어야 합니다.

이 분류기를 Gmail API나 Outlook Graph API와 연결하면 수신 이메일을 실시간으로 자동 분류하는 시스템을 구축할 수 있습니다. Chapter 25에서 자동화 파이프라인으로 확장하는 방법을 다룹니다.

---

**원본**: https://wikidocs.net/340835  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
