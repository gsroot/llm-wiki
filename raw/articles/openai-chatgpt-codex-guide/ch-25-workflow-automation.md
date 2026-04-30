---
source_url: https://wikidocs.net/340837
book: ChatGPT & Codex 실무 활용 가이드
book_url: https://wikidocs.net/book/19558
author: 송영옥
license: CC-BY
license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. 출처 표기 + URL 명시로 attribution 요구사항 충족."
fetched_at: 2026-04-30
ingestion_mode: path-a-verbatim
---

## 자동화 플랫폼 선택 가이드

반복적인 업무를 자동화하는 방법은 크게 두 가지입니다. 코드 없이 GUI로 연결하는 **노코드/로우코드 플랫폼** 과, Python 스크립트로 직접 구현하는 **코드 방식** 입니다.

방법 | 도구 | 장점 | 적합한 상황  
---|---|---|---  
노코드 | Zapier, Make | 빠른 구축, 코딩 불필요 | 간단한 트리거-액션 연결  
로우코드 | Power Automate | MS 생태계 통합 | Office365 중심 업무 환경  
코드 | Python 스크립트 | 완전한 제어, 비용 절감 | 복잡한 로직, 대량 처리  
  
## 

## 노코드/로우코드 자동화 플랫폼 연동

### Zapier + ChatGPT

Zapier는 앱과 앱을 연결하는 노코드 자동화 플랫폼입니다. OpenAI Action을 기본 제공하므로 코드 없이 ChatGPT를 업무 흐름에 통합할 수 있습니다.

**Zap 만들기 기본 흐름:**

  1. [zapier.com](https://zapier.com)에 로그인 후 **Create Zap** 클릭
  2. **Trigger** 선택: 이메일 수신(Gmail), 폼 제출(Typeform), 슬랙 메시지 등
  3. **Action** 추가: OpenAI → **ChatGPT** 선택
  4. 프롬프트 필드에 이전 단계의 데이터를 변수로 삽입
  5. 결과를 다음 액션(슬랙 전송, 구글 시트 저장 등)으로 연결


예시 Zap: "Gmail 수신 → ChatGPT로 요약 → Slack에 요약본 전송"

tip

Zapier의 OpenAI 연동은 월 무료 티어(100 Task)가 제한적입니다. 대량 처리가 필요하다면 Make 또는 Python 스크립트 방식이 더 경제적입니다.

### Make(Integromat) + OpenAI 모듈

Make는 Zapier보다 복잡한 로직(조건 분기, 반복, 데이터 변환)을 시각적으로 구현할 수 있는 플랫폼입니다.

**설정 방법:**

  1. [make.com](https://make.com)에서 새 시나리오 생성
  2. OpenAI 모듈 추가 → **Create a Completion** 또는 **Create a Message** 선택
  3. API 키 연결: Connections → Add → OpenAI API key 입력
  4. Model, Messages 필드 설정 및 이전 모듈 데이터와 연결


Make의 강점은 **라우터(Router)** 모듈로 조건에 따라 다른 경로를 실행할 수 있다는 점입니다. 예를 들어 AI 분류 결과에 따라 "불만 → 담당자 알림", "문의 → 자동 응답"처럼 분기 처리가 가능합니다.

### Microsoft Power Automate + AI Builder

Microsoft 365를 사용하는 기업 환경에서는 Power Automate가 최적의 선택입니다.

  1. [flow.microsoft.com](https://flow.microsoft.com) → **새 흐름 만들기**
  2. AI Builder → **GPT로 텍스트 만들기** 액션 추가
  3. 또는 HTTP 커넥터로 OpenAI API를 직접 호출


## 

## Slack 봇 만들기

Slack 봇을 만들면 팀원들이 슬래시 명령어로 AI를 바로 활용할 수 있습니다.

### Slack App 설정

  1. [api.slack.com/apps](https://api.slack.com/apps) → **Create New App** → **From scratch**
  2. 앱 이름 입력 후 워크스페이스 선택
  3. **OAuth & Permissions** → Bot Token Scopes에 `chat:write`, `commands` 추가
  4. **Install to Workspace** 클릭 → Bot User OAuth Token 복사
  5. **Slash Commands** → `/ask` 명령어 추가, Request URL에 서버 주소 입력


### Python Flask로 Slack 봇 구현
    
    
    from flask import Flask, request, jsonify
    from openai import OpenAI
    import os
    
    app = Flask(__name__)
    client = OpenAI()
    
    SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
    
    @app.route("/slack/ask", methods=["POST"])
    def handle_ask_command():
        """'/ask 질문' 슬래시 명령어를 처리합니다."""
    
        user_question = request.form.get("text", "")
        user_name = request.form.get("user_name", "사용자")
    
        if not user_question:
            return jsonify({"text": "질문을 입력해주세요. 예: /ask 파이썬으로 CSV 파일 읽는 방법"})
    
        # OpenAI API 호출
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "당신은 업무를 돕는 AI 비서입니다. 간결하고 명확하게 답변하세요."},
                {"role": "user", "content": user_question}
            ],
            max_tokens=500
        )
    
        answer = response.choices[0].message.content
    
        # Slack 형식으로 응답
        return jsonify({
            "response_type": "in_channel",  # 채널에 공개 표시
            "text": f"*{user_name}님의 질문:* {user_question}\n\n*AI 답변:*\n{answer}"
        })
    
    
    if __name__ == "__main__":
        app.run(port=3000)
    

Slack 봇을 외부에서 접근 가능하게 하려면 **ngrok** 으로 로컬 서버를 임시 공개하거나, AWS Lambda / Google Cloud Run 같은 서버리스 서비스에 배포하면 됩니다.

## 

## Google Sheets / Notion 자동화

### Google Apps Script + OpenAI API

Google Sheets에 내장된 Apps Script를 사용하면 스프레드시트에서 바로 AI를 호출할 수 있습니다.
    
    
    // Google Apps Script (Tools → Script Editor에 붙여넣기)
    const OPENAI_API_KEY = PropertiesService.getScriptProperties().getProperty("OPENAI_API_KEY");
    
    function classifyText(text) {
      const url = "https://api.openai.com/v1/chat/completions";
    
      const payload = {
        model: "gpt-4o-mini",
        messages: [
          {role: "system", content: "텍스트를 긍정/부정/중립 중 하나로 분류하세요. 단어 하나만 반환하세요."},
          {role: "user", content: text}
        ],
        max_tokens: 10,
        temperature: 0
      };
    
      const options = {
        method: "post",
        headers: {
          "Authorization": `Bearer ${OPENAI_API_KEY}`,
          "Content-Type": "application/json"
        },
        payload: JSON.stringify(payload)
      };
    
      const response = UrlFetchApp.fetch(url, options);
      const data = JSON.parse(response.getContentText());
      return data.choices[0].message.content.trim();
    }
    
    // 시트의 A열 텍스트를 분류하여 B열에 결과 저장
    function classifySheet() {
      const sheet = SpreadsheetApp.getActiveSheet();
      const lastRow = sheet.getLastRow();
    
      for (let i = 2; i <= lastRow; i++) {
        const text = sheet.getRange(i, 1).getValue();
        if (text) {
          const result = classifyText(text);
          sheet.getRange(i, 2).setValue(result);
          Utilities.sleep(500); // Rate limit 방지
        }
      }
      SpreadsheetApp.getUi().alert("분류 완료!");
    }
    

API 키 저장: Apps Script → 프로젝트 설정 → 스크립트 속성에 `OPENAI_API_KEY` 추가

## 

## 실습: "이메일 수신 → AI 분류 → 자동 응답" 파이프라인 구축

이메일이 수신되면 AI가 내용을 분류하고, 카테고리에 따라 자동 응답을 보내는 파이프라인을 구축합니다. 노코드(Zapier)와 Python 스크립트 두 가지 방식으로 구현합니다.

### 방식 1: Zapier 노코드 구현

**Zap 구성:**
    
    
    [Trigger] Gmail - New Email
        ↓
    [Action 1] OpenAI - ChatGPT
        프롬프트: "다음 이메일을 분류하세요: {{Body Plain}}
        카테고리: 문의/불만/칭찬/스팸
        JSON으로 반환: {"category": "...", "auto_reply": "..."}"
        ↓
    [Action 2] Filter - category가 스팸이 아닌 경우만 진행
        ↓
    [Action 3] Gmail - Send Email
        To: {{From Email}}
        Subject: Re: {{Subject}}
        Body: {{auto_reply}}  ← OpenAI 응답에서 추출
        ↓
    [Action 4] Google Sheets - Add Row
        이메일 수신 로그 기록
    

Zapier 설정 팁: OpenAI Action의 응답은 텍스트이므로, JSON 파싱이 필요하면 **Formatter → Text → Extract Pattern** 으로 원하는 값을 추출합니다.

### 방식 2: Python 스크립트 구현

Gmail API와 OpenAI API를 연결한 완전한 파이프라인입니다.
    
    
    import json
    import base64
    from openai import OpenAI
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    
    client = OpenAI()
    
    def analyze_email(subject: str, body: str) -> dict:
        """이메일을 분류하고 자동 응답 초안을 생성합니다."""
    
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0.2,
            messages=[
                {
                    "role": "system",
                    "content": """이메일을 분석하여 JSON으로 반환하세요.
    
    형식:
    {
      "category": "문의" | "불만" | "칭찬" | "스팸",
      "priority": "높음" | "보통" | "낮음",
      "summary": "핵심 내용 한 줄",
      "auto_reply": "적절한 자동 응답 메시지 (스팸은 빈 문자열)",
      "needs_human": true | false
    }"""
                },
                {
                    "role": "user",
                    "content": f"제목: {subject}\n\n내용:\n{body}"
                }
            ],
            response_format={"type": "json_object"}
        )
    
        return json.loads(response.choices[0].message.content)
    
    
    def send_auto_reply(gmail_service, message_id: str, thread_id: str,
                        to: str, subject: str, reply_text: str):
        """Gmail API로 자동 응답을 발송합니다."""
    
        reply_body = f"""안녕하세요,
    
    {reply_text}
    
    감사합니다.
    자동 응답 시스템 드림
    ---
    이 메시지는 자동으로 발송된 응답입니다."""
    
        message_content = (
            f"To: {to}\n"
            f"Subject: Re: {subject}\n"
            f"Content-Type: text/plain; charset=utf-8\n\n"
            f"{reply_body}"
        )
    
        encoded = base64.urlsafe_b64encode(message_content.encode()).decode()
    
        gmail_service.users().messages().send(
            userId="me",
            body={"raw": encoded, "threadId": thread_id}
        ).execute()
    
    
    def process_inbox(gmail_service, max_emails: int = 10):
        """받은 편지함의 미읽음 이메일을 처리합니다."""
    
        # 미읽음 이메일 조회
        results = gmail_service.users().messages().list(
            userId="me",
            q="is:unread",
            maxResults=max_emails
        ).execute()
    
        messages = results.get("messages", [])
    
        for msg_ref in messages:
            msg = gmail_service.users().messages().get(
                userId="me",
                id=msg_ref["id"],
                format="full"
            ).execute()
    
            # 제목, 발신자, 본문 추출
            headers = {h["name"]: h["value"] for h in msg["payload"]["headers"]}
            subject = headers.get("Subject", "제목 없음")
            sender = headers.get("From", "")
    
            # 본문 디코딩 (간략화)
            body = ""
            if "parts" in msg["payload"]:
                for part in msg["payload"]["parts"]:
                    if part["mimeType"] == "text/plain":
                        body = base64.urlsafe_b64decode(
                            part["body"]["data"]
                        ).decode("utf-8", errors="ignore")
                        break
    
            # AI 분석
            analysis = analyze_email(subject, body[:2000])  # 처음 2000자만
    
            print(f"\n처리 중: {subject}")
            print(f"  분류: {analysis['category']} | 우선순위: {analysis['priority']}")
            print(f"  요약: {analysis['summary']}")
    
            # 스팸이 아니고 자동 응답이 있는 경우
            if analysis["category"] != "스팸" and analysis["auto_reply"]:
                send_auto_reply(
                    gmail_service,
                    msg_ref["id"],
                    msg["threadId"],
                    sender,
                    subject,
                    analysis["auto_reply"]
                )
                print(f"  자동 응답 발송 완료")
    
            # 담당자 확인이 필요한 경우 표시
            if analysis["needs_human"]:
                print(f"  *** 담당자 검토 필요 ***")
    
    
    # Gmail API 인증 후 실행
    # creds = Credentials.from_authorized_user_file("token.json")
    # gmail_service = build("gmail", "v1", credentials=creds)
    # process_inbox(gmail_service)
    

tip

Gmail API 사용을 위한 OAuth 인증 설정은 [Google Cloud Console](https://console.cloud.google.com)에서 프로젝트 생성 → Gmail API 활성화 → OAuth 2.0 클라이언트 자격 증명 생성 순으로 진행합니다. `google-auth-oauthlib` 라이브러리로 인증 흐름을 처리하세요.

### 두 방식 비교

항목 | Zapier 노코드 | Python 스크립트  
---|---|---  
구축 시간 | 30분 | 2~4시간  
월 비용 | $20~50 (Zapier 요금) | API 비용만  
커스터마이징 | 제한적 | 완전 자유  
  
간단한 파이프라인 시작은 Zapier로 빠르게 검증하고, 사용량이 늘거나 복잡한 로직이 필요해지면 Python 스크립트로 전환하는 전략이 효과적입니다.

Part 7을 마치며, 여러분은 이제 OpenAI API를 활용한 다양한 자동화 워크플로를 직접 설계하고 구현할 수 있는 기반을 갖추었습니다. **API 호출 → 결과 처리 → 외부 시스템 연동**의 패턴을 익혔으니, 이를 응용하여 자신의 업무에 맞는 나만의 AI 자동화 시스템을 구축해보세요.

---

**원본**: https://wikidocs.net/340837  
**저자**: 송영옥 (CC BY)  
**책 페이지**: https://wikidocs.net/book/19558  
**마지막 편집일시 : 2026년 4월 12일 8:09 오후**
