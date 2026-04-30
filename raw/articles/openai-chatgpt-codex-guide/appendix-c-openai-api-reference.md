---
source_url: https://wikidocs.net/340845
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## C. OpenAI API 빠른 참조표

OpenAI API를 활용할 때 즉시 참조할 수 있도록 모델 사양, 가격, 엔드포인트, Rate Limits, 에러 코드를 한데 모았습니다.

tip

API 가격과 모델 사양은 수시로 업데이트됩니다. 최신 정보는 https://platform.openai.com/docs/models 와 https://openai.com/api/pricing 에서 확인하세요.

* * *

## 주요 모델 사양

모델 | 컨텍스트 윈도우 | 최대 출력 토큰 | 학습 데이터 기준  
---|---|---|---  
gpt-4o | 128,000 토큰 | 16,384 토큰 | 2023년 10월  
gpt-4o-mini | 128,000 토큰 | 16,384 토큰 | 2023년 10월  
o3 | 200,000 토큰 | 100,000 토큰 | 2024년 6월  
o3-mini | 200,000 토큰 | 100,000 토큰 | 2024년 6월  
gpt-4.5-preview | 128,000 토큰 | 16,384 토큰 | 2024년 6월  
  
* * *

## API 가격표 (1M 토큰 기준)

모델 | 입력 토큰 | 출력 토큰  
---|---|---  
gpt-4o | $2.50 | $10.00  
gpt-4o-mini | $0.15 | $0.60  
o3 | $10.00 | $40.00  
o3-mini | $1.10 | $4.40  
gpt-4.5-preview | $75.00 | $150.00  
tip

Batch API를 사용하면 비동기 처리로 **최대 50% 비용 절감**이 가능합니다. 실시간 응답이 필요 없는 작업(데이터 전처리, 대량 분류 등)에 활용하세요.

* * *

## 주요 API 엔드포인트

### Chat Completions

가장 범용적으로 사용되는 엔드포인트입니다.
    
    
    POST https://api.openai.com/v1/chat/completions
    
    
    
    from openai import OpenAI
    
    client = OpenAI()
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "당신은 도움이 되는 어시스턴트입니다."},
            {"role": "user", "content": "안녕하세요!"}
        ]
    )
    print(response.choices[0].message.content)
    

### Assistants API

대화 스레드·파일·도구 호출을 상태 관리와 함께 사용할 수 있는 고수준 API입니다.
    
    
    POST https://api.openai.com/v1/assistants
    POST https://api.openai.com/v1/threads
    POST https://api.openai.com/v1/threads/{thread_id}/runs
    

주요 특징: 파일 검색(File Search), Code Interpreter, Function Calling 내장 지원

### Images (DALL-E)
    
    
    POST https://api.openai.com/v1/images/generations
    
    
    
    response = client.images.generate(
        model="dall-e-3",
        prompt="[이미지 설명 프롬프트]",
        size="1024x1024",   # 256x256, 512x512, 1024x1024, 1024x1792, 1792x1024
        quality="standard", # standard | hd
        n=1
    )
    print(response.data[0].url)
    

### Audio — Whisper (STT) & TTS
    
    
    POST https://api.openai.com/v1/audio/transcriptions  # Whisper STT
    POST https://api.openai.com/v1/audio/speech          # TTS
    
    
    
    # Whisper 음성 → 텍스트
    with open("audio.mp3", "rb") as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
            language="ko"
        )
    print(transcript.text)
    
    # TTS 텍스트 → 음성
    response = client.audio.speech.create(
        model="tts-1",         # tts-1 | tts-1-hd
        voice="alloy",         # alloy, echo, fable, onyx, nova, shimmer
        input="안녕하세요, 반갑습니다."
    )
    response.stream_to_file("output.mp3")
    

### Embeddings
    
    
    POST https://api.openai.com/v1/embeddings
    
    
    
    response = client.embeddings.create(
        model="text-embedding-3-small",  # text-embedding-3-small | text-embedding-3-large
        input="임베딩할 텍스트"
    )
    vector = response.data[0].embedding  # 1536차원 벡터
    

### Moderation

콘텐츠 안전성 검사 (무료 제공)
    
    
    POST https://api.openai.com/v1/moderations
    
    
    
    response = client.moderations.create(
        model="omni-moderation-latest",
        input="검사할 텍스트"
    )
    result = response.results[0]
    print(result.flagged)           # True/False
    print(result.categories)        # 카테고리별 위반 여부
    

* * *

## Rate Limits 티어별 기준

티어 | 조건 | RPM (gpt-4o) | TPM (gpt-4o)  
---|---|---|---  
Tier 1 | $5 충전 후 | 500 | 30,000  
Tier 2 | $50 사용 후 | 5,000 | 450,000  
Tier 3 | $100 사용 후 | 5,000 | 800,000  
Tier 4 | $250 사용 후 | 10,000 | 2,000,000  
Tier 5 | $1,000 사용 후 | 10,000 | 30,000,000  
  
  * **RPM** : Requests Per Minute (분당 요청 수)
  * **TPM** : Tokens Per Minute (분당 토큰 수)

tip

Rate Limit은 모델별로 별도 적용됩니다. gpt-4o와 gpt-4o-mini는 별도의 한도를 가지므로, 비용이 저렴한 mini 모델로 트래픽을 분산하면 효율적입니다.

* * *

## 주요 에러 코드 및 대처법

에러 코드 | 의미 | 대처 방법  
---|---|---  
400 Bad Request | 잘못된 요청 파라미터 | 요청 본문과 파라미터 형식 확인  
401 Unauthorized | API 키 오류 | API 키 유효성 및 환경변수 설정 확인  
403 Forbidden | 접근 권한 없음 | 해당 모델/기능 접근 권한 확인  
429 Too Many Requests | Rate Limit 초과 | 지수 백오프(Exponential Backoff) 로직 적용  
500 Internal Server Error | OpenAI 서버 오류 | 잠시 후 재시도, https://status.openai.com 확인  
503 Service Unavailable | 서비스 일시 중단 | https://status.openai.com 에서 장애 확인 후 대기  
  
### 429 에러 처리 예시 (지수 백오프)
    
    
    import time
    import openai
    
    def call_with_retry(prompt, max_retries=5):
        for attempt in range(max_retries):
            try:
                return client.chat.completions.create(
                    model="gpt-4o",
                    messages=[{"role": "user", "content": prompt}]
                )
            except openai.RateLimitError:
                wait_time = 2 ** attempt  # 1, 2, 4, 8, 16초
                print(f"Rate limit 초과. {wait_time}초 후 재시도...")
                time.sleep(wait_time)
        raise Exception("최대 재시도 횟수 초과")

---

**원본**: https://wikidocs.net/340845  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
