---
title: "Hybrid AI Chat"
type: concept
source_count: 2
tags: [ai, chatbot, openai, gpt-4, hybrid]
related:
  - "../entities/fastapi-app.md"
  - "../concepts/websocket-realtime.md"
---

# Hybrid AI Chat

## Definition

일반 사용자 간 채팅방에 AI 챗봇을 추가하여, 사람과 AI가 같은 대화에 참여하는 하이브리드 채팅 방식이다.

## How It Works in Mate Chat

### 흐름

1. 채팅방에 AI 봇을 추가 (트리거 프리픽스 설정, 예: `@botname`)
2. 사용자가 `@botname` 으로 메시지에 멘션
3. WebSocket Handler가 AI 트리거를 감지
4. `hybrid_chat_service`가 최근 N개 메시지를 컨텍스트로 수집
5. OpenAI GPT-4 API 호출 (챗봇의 시스템 프롬프트 + 컨텍스트)
6. AI 응답을 DB에 저장하고 같은 방 멤버에게 브로드캐스트

### 설정 가능 항목

- **트리거 프리픽스**: 봇마다 고유 (`@botname`)
- **컨텍스트 윈도우**: 1-100 메시지 (최근 대화 몇 개를 AI에게 전달할지)
- **공개/비공개 봇**: 다른 사용자도 사용할 수 있는 공개 봇 생성 가능

### 관련 테이블

- `chat_room_bots`: room_id, chatbot_id, trigger_prefix, context_window, is_active
- `chatbots`: name, description, instructions(시스템 프롬프트), model, is_public
- `chatbot_mates`: 사용자-챗봇 친구 관계

### 클로버 연동

- AI 호출 시 클로버 사용량 추적 (usage_count, paid_usage_count)
- 전용 1:1 AI 채팅방도 지원 (챗봇 메이트 시스템)

## Trade-offs

**장점**:
- 사람과 AI의 자연스러운 혼합 대화
- 커스텀 봇 생성으로 다양한 AI 페르소나 활용
- 채팅방별 독립적인 AI 설정

**단점**:
- OpenAI API 비용 (사용량에 비례)
- 컨텍스트 윈도우 크기와 응답 품질/비용 간 트레이드오프
- AI 응답 지연이 실시간 채팅 UX에 영향

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- hybrid_chat_service 구현
- [WebSocket Realtime](../concepts/websocket-realtime.md) -- AI 응답 브로드캐스트
