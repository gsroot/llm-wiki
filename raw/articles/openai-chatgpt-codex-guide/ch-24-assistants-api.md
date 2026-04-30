---
source_url: https://wikidocs.net/340836
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## Assistants API란?

Chat Completions API가 단발성 질문-답변에 특화되어 있다면, **Assistants API** 는 상태(state)를 유지하는 AI 어시스턴트를 구축하기 위한 고수준 API입니다. 다음과 같은 기능이 내장되어 있습니다.

  * 대화 히스토리 자동 관리 (메시지를 직접 누적할 필요 없음)
  * 문서 업로드 및 검색 (File Search, RAG)
  * 코드 실행 및 데이터 분석 (Code Interpreter)
  * 외부 시스템 연동 (Function Calling)

tip

Assistants API는 "베타" 딱지를 달고 있지만 이미 프로덕션에서 널리 사용되고 있습니다. 고객 상담 봇, 사내 지식 베이스 챗봇, 코드 리뷰 에이전트 등에 적합합니다.

## 

## 핵심 개념 4가지

Assistants API는 4개의 객체로 구성됩니다.

객체 | 역할 | 비유  
---|---|---  
Assistant | AI의 정체성·도구 설정 | 직원 채용 계약서  
Thread | 하나의 대화 세션 | 대화방(채팅방)  
Message | 대화 내의 개별 메시지 | 채팅 메시지  
Run | Thread에서 Assistant를 실행 | 대화 처리 요청  
  
흐름을 정리하면 다음과 같습니다.
    
    
    Assistant 생성 (1회)
        ↓
    Thread 생성 (사용자별 또는 세션별)
        ↓
    Message 추가 (사용자 질문)
        ↓
    Run 생성 및 완료 대기
        ↓
    응답 Message 조회
    

## 

## 기본 코드 예시
    
    
    from openai import OpenAI
    client = OpenAI()
    
    # 1. Assistant 생성 (한 번만 생성, ID를 저장해두고 재사용)
    assistant = client.beta.assistants.create(
        name="고객 상담 봇",
        instructions="당신은 전자제품 고객 상담 전문가입니다. 친절하고 정확하게 답변하세요.",
        model="gpt-4o",
        tools=[{"type": "file_search"}, {"type": "code_interpreter"}]
    )
    print(f"Assistant ID: {assistant.id}")
    
    # 2. Thread 생성 (대화 세션 시작)
    thread = client.beta.threads.create()
    
    # 3. 사용자 메시지 추가
    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="세탁기가 작동하지 않아요. E3 에러가 뜹니다."
    )
    
    # 4. Run 생성 및 완료까지 대기
    run = client.beta.threads.runs.create_and_poll(
        thread_id=thread.id,
        assistant_id=assistant.id
    )
    
    # 5. 응답 메시지 조회
    if run.status == "completed":
        messages = client.beta.threads.messages.list(thread_id=thread.id)
        # 가장 최근 assistant 메시지 출력
        for msg in messages.data:
            if msg.role == "assistant":
                print(msg.content[0].text.value)
                break
    

tip

`create_and_poll()`은 Run이 완료될 때까지 자동으로 폴링합니다. 단순 구현에 편리하지만, 프로덕션 환경에서는 웹훅(Webhook) 방식이 더 효율적입니다.

### 대화 이어가기

같은 Thread에 메시지를 계속 추가하면 이전 대화 내용을 기억한 채로 대화를 이어갈 수 있습니다.
    
    
    def chat(thread_id: str, assistant_id: str, user_message: str) -> str:
        """Thread에 메시지를 추가하고 응답을 반환합니다."""
    
        # 메시지 추가
        client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=user_message
        )
    
        # 실행 및 대기
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
    
        # 응답 반환
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content[0].text.value
    
    
    # 연속 대화 테스트
    thread = client.beta.threads.create()
    
    print(chat(thread.id, assistant.id, "세탁기가 E3 에러가 떠요"))
    print(chat(thread.id, assistant.id, "혹시 제 모델은 WF-5500이에요"))  # 이전 맥락 유지
    

## 

## 내장 도구 활용

### File Search — 문서 기반 답변 (RAG)

File Search는 업로드한 문서에서 관련 내용을 검색해 답변하는 기능입니다. 사내 매뉴얼, 제품 설명서, 정책 문서를 기반으로 답변하는 챗봇을 만들 수 있습니다.
    
    
    # 파일 업로드
    with open("product_manual.pdf", "rb") as f:
        file = client.files.create(file=f, purpose="assistants")
    
    # Vector Store 생성 및 파일 연결
    vector_store = client.beta.vector_stores.create(name="제품 매뉴얼")
    client.beta.vector_stores.files.create_and_poll(
        vector_store_id=vector_store.id,
        file_id=file.id
    )
    
    # Assistant에 Vector Store 연결
    assistant = client.beta.assistants.create(
        name="매뉴얼 기반 상담 봇",
        instructions="업로드된 제품 매뉴얼을 참고하여 답변하세요.",
        model="gpt-4o",
        tools=[{"type": "file_search"}],
        tool_resources={
            "file_search": {"vector_store_ids": [vector_store.id]}
        }
    )
    

### Code Interpreter — 코드 실행과 데이터 분석

Code Interpreter는 Python 코드를 실행하고, 그래프·차트 생성, CSV 파일 처리, 수학 계산 등을 수행할 수 있는 도구입니다.
    
    
    assistant = client.beta.assistants.create(
        name="데이터 분석 봇",
        instructions="업로드된 데이터를 분석하고 인사이트를 제공하세요.",
        model="gpt-4o",
        tools=[{"type": "code_interpreter"}]
    )
    
    # CSV 파일 업로드
    with open("sales_data.csv", "rb") as f:
        file = client.files.create(file=f, purpose="assistants")
    
    # 메시지에 파일 첨부
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content="이 매출 데이터를 분석해서 월별 트렌드를 알려주세요.",
        attachments=[{"file_id": file.id, "tools": [{"type": "code_interpreter"}]}]
    )
    

## 

## Function Calling — 외부 시스템 연동

Function Calling을 사용하면 AI가 직접 외부 API를 호출하거나 데이터베이스를 조회하도록 만들 수 있습니다. 날씨 정보 조회, 주문 현황 확인, 예약 시스템 연동 등이 가능합니다.

### 날씨 API 연동 예시

**1단계: 함수 정의**
    
    
    # AI에게 사용 가능한 함수를 설명
    weather_function = {
        "name": "get_current_weather",
        "description": "특정 도시의 현재 날씨를 조회합니다.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "도시 이름 (예: 서울, 부산)"
                },
                "unit": {
                    "type": "string",
                    "enum": ["celsius", "fahrenheit"],
                    "description": "온도 단위"
                }
            },
            "required": ["city"]
        }
    }
    
    assistant = client.beta.assistants.create(
        name="날씨 안내 봇",
        instructions="날씨를 조회하여 친절하게 안내해주세요.",
        model="gpt-4o",
        tools=[{"type": "function", "function": weather_function}]
    )
    

**2단계: Function Call 처리**
    
    
    import json
    
    def get_weather(city: str, unit: str = "celsius") -> dict:
        """실제 날씨 API 호출 (여기서는 예시 데이터 반환)"""
        return {"city": city, "temperature": 22, "condition": "맑음", "unit": unit}
    
    def run_with_function_calling(thread_id: str, assistant_id: str) -> str:
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
    
        # Run이 완료되거나 function call이 필요할 때까지 반복
        while run.status in ["queued", "in_progress", "requires_action"]:
            run = client.beta.threads.runs.retrieve(
                thread_id=thread_id, run_id=run.id
            )
    
            if run.status == "requires_action":
                tool_calls = run.required_action.submit_tool_outputs.tool_calls
                tool_outputs = []
    
                for tool_call in tool_calls:
                    if tool_call.function.name == "get_current_weather":
                        args = json.loads(tool_call.function.arguments)
                        result = get_weather(**args)  # 실제 함수 실행
                        tool_outputs.append({
                            "tool_call_id": tool_call.id,
                            "output": json.dumps(result, ensure_ascii=False)
                        })
    
                # 실행 결과 제출
                run = client.beta.threads.runs.submit_tool_outputs(
                    thread_id=thread_id,
                    run_id=run.id,
                    tool_outputs=tool_outputs
                )
    
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data[0].content[0].text.value
    

## 

## 실습: 제품 매뉴얼 기반 고객 상담 봇 구축

실제 제품 매뉴얼(PDF)을 업로드하고, 사용자의 질문에 매뉴얼 기반으로 답변하는 상담 봇을 만들어봅니다.

### 전체 구현 코드
    
    
    from openai import OpenAI
    import os
    
    client = OpenAI()
    
    def setup_support_bot(manual_path: str) -> tuple:
        """제품 매뉴얼을 업로드하고 상담 봇을 초기화합니다."""
    
        print("1. 매뉴얼 파일 업로드 중...")
        with open(manual_path, "rb") as f:
            file = client.files.create(file=f, purpose="assistants")
    
        print("2. Vector Store 생성 중...")
        vector_store = client.beta.vector_stores.create(name="제품 매뉴얼 DB")
        client.beta.vector_stores.files.create_and_poll(
            vector_store_id=vector_store.id,
            file_id=file.id
        )
    
        print("3. 상담 봇 Assistant 생성 중...")
        assistant = client.beta.assistants.create(
            name="제품 고객 상담 봇",
            instructions="""당신은 친절한 고객 상담 전문가입니다.
    
    업로드된 제품 매뉴얼을 기반으로 답변하세요.
    매뉴얼에 없는 내용은 "해당 내용은 매뉴얼에서 확인되지 않습니다"라고 솔직히 말하세요.
    답변 시 매뉴얼의 몇 페이지를 참고했는지 알려주세요.""",
            model="gpt-4o",
            tools=[{"type": "file_search"}],
            tool_resources={
                "file_search": {"vector_store_ids": [vector_store.id]}
            }
        )
    
        thread = client.beta.threads.create()
        print(f"초기화 완료! Thread ID: {thread.id}\n")
    
        return assistant, thread
    
    
    def ask_support_bot(assistant, thread, question: str) -> str:
        """상담 봇에 질문하고 답변을 반환합니다."""
    
        client.beta.threads.messages.create(
            thread_id=thread.id,
            role="user",
            content=question
        )
    
        run = client.beta.threads.runs.create_and_poll(
            thread_id=thread.id,
            assistant_id=assistant.id
        )
    
        if run.status == "completed":
            messages = client.beta.threads.messages.list(thread_id=thread.id)
            return messages.data[0].content[0].text.value
        else:
            return f"오류 발생: {run.status}"
    
    
    # 실행
    # assistant, thread = setup_support_bot("product_manual.pdf")
    
    # 질문 테스트
    questions = [
        "세탁기 E3 에러는 어떻게 해결하나요?",
        "탈수 기능은 어떻게 사용하나요?",
        "에너지 효율 등급은 어떻게 되나요?"
    ]
    
    # for q in questions:
    #     print(f"Q: {q}")
    #     print(f"A: {ask_support_bot(assistant, thread, q)}\n")
    

### 대화형 CLI 인터페이스 추가
    
    
    def run_chat_interface(assistant, thread):
        """터미널에서 대화형으로 상담 봇과 대화합니다."""
        print("=== 제품 고객 상담 봇 ===")
        print("질문을 입력하세요. 종료하려면 'quit'을 입력하세요.\n")
    
        while True:
            user_input = input("고객: ").strip()
    
            if user_input.lower() == "quit":
                print("상담을 종료합니다.")
                break
    
            if not user_input:
                continue
    
            print("봇: ", end="", flush=True)
            response = ask_support_bot(assistant, thread, user_input)
            print(response)
            print()
    

tip

실제 서비스에서는 Thread ID를 데이터베이스에 저장하여 사용자별로 대화 세션을 유지하는 것이 중요합니다. Thread는 생성 후 삭제하지 않으면 유지되므로, 재방문 사용자에게 이전 대화 이어가기 기능을 제공할 수 있습니다.

이처럼 Assistants API를 활용하면 복잡한 대화 상태 관리 코드 없이도 강력한 AI 에이전트를 빠르게 구축할 수 있습니다. 다음 Chapter 25에서는 이 기능들을 노코드 자동화 플랫폼과 연결하여 업무 전반에 활용하는 방법을 배웁니다.

---

**원본**: https://wikidocs.net/340836  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
