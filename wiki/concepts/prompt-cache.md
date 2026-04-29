---
title: "Prompt Caching"
type: concept
category: ai
tags: [prompt-cache, claude, anthropic, LLM-api, 토큰경제, latency, optimization]
related:
  - "[[token-economy]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[context-engineering]]"
  - "[[anthropics-claude-cookbooks]]"
source_count: 1
observed_source_refs: 4
inbound_count: 12
created: 2026-04-27
updated: 2026-04-27
---

# Prompt Caching

## 정의

**Prompt Caching(프롬프트 캐싱)**은 LLM API 호출 시 동일한 컨텍스트(시스템 프롬프트, 도구 정의, 긴 문서 등)가 반복 전송될 때, 이를 서버 측에서 미리 가공·저장해두고 다음 호출에서 재사용함으로써 **비용과 지연 시간을 크게 줄이는** 기법이다.

## 왜 중요한가

- **비용 절감**: Anthropic 기준 캐시 히트는 일반 입력 토큰의 **약 10% 비용**. 100만 토큰 컨텍스트를 매 턴 다시 보내는 에이전트라면 수십 배 비용 절감 가능.
- **레이턴시 감소**: 캐시 히트 시 prefill 단계가 사실상 생략되어 첫 토큰 시간(TTFT)이 큰 폭으로 단축됨.
- **에이전트 워크플로우의 경제성**: [[claude-code]] 같은 멀티턴 에이전트는 동일한 도구 정의·시스템 프롬프트·읽은 파일을 매 턴 다시 보내기 때문에, 캐시 없으면 비용이 폭증. 캐싱이 사실상 에이전트 비즈니스 모델을 가능하게 함.

## 핵심 내용

### Anthropic Claude의 캐시 모델 (2024-08~)

- **수동 마크업**: `cache_control: {"type": "ephemeral"}`을 메시지/시스템/도구 블록에 명시.
- **TTL**: 5분 기본. 같은 프리픽스로 5분 안에 다시 호출하면 캐시 히트.
- **계층 구조**: 캐시는 **prefix-based**. 메시지 배열의 앞쪽이 동일하면 거기까지 히트하고, 다른 부분부터 새로 prefill.
- **가격**:
  - Cache write: 일반 입력의 **1.25배** (한 번만 발생)
  - Cache read: 일반 입력의 **0.1배** (반복 호출 시)
- **최소 토큰**: 1024 (Sonnet/Opus) 또는 2048 (Haiku) 미만 블록은 캐시되지 않음.

### 어디에 캐싱을 거는가

```
[ 시스템 프롬프트 (캐시) ]
[ 도구 정의 (캐시) ]
[ 긴 문서/지식 (캐시) ]
[ 대화 히스토리 (캐시) ]
[ 새 사용자 메시지 ] ← 매번 새로 prefill
```

### 다른 LLM 제공자의 패턴

- **OpenAI**: 자동 prefix 캐싱(2024-10~). 명시적 마크업 없이 1024 토큰 이상 동일 prefix를 자동 감지·할인.
- **Google Gemini**: 명시적 컨텍스트 캐시 API. 별도 캐시 객체로 관리 가능.
- **트레이드오프**: 자동(OpenAI) = 사용 편의성 ↑, 제어성 ↓ / 수동(Anthropic) = 명확한 비용 예측 ↑, 구현 부담 ↑.

## 실전 적용

```python
# Anthropic Python SDK 예시
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="claude-opus-4-7",
    max_tokens=1024,
    system=[
        {
            "type": "text",
            "text": "당신은 코드 리뷰 전문가입니다.",
            "cache_control": {"type": "ephemeral"}  # ← 캐시 마킹
        }
    ],
    messages=[{"role": "user", "content": "이 PR을 리뷰해줘"}]
)
```

### 에이전트 워크플로우에서의 캐싱 전략

- **시스템 프롬프트와 도구 정의는 항상 캐시**: 거의 모든 호출에서 변하지 않음.
- **읽은 파일/문서도 캐시**: 같은 세션 안에서 반복 참조됨.
- **TTL 5분을 넘기지 않도록 호출 간격 관리**: 폴링 간격을 4분 이하로 유지하면 캐시가 항상 따뜻함.
- **TodoList 같은 변동 부분은 캐시 뒤에 배치**: prefix-based이므로 변하는 부분이 앞에 오면 뒤가 모두 무효화됨.

## 관련 개념

- [[token-economy]]: 토큰 기반 가격 모델의 핵심 최적화 수단.
- [[context-engineering]]: 캐시 친화적인 컨텍스트 배치가 중요한 설계 결정.
- [[claude-code]]·[[claude-agent-sdk]]: 캐싱을 적극 활용하는 대표 워크플로우.

## 출처

- [[anthropics-claude-cookbooks]] — Anthropic 공식 prompt caching 패턴 예시

## 열린 질문

- 더 긴 TTL(1시간) 옵션이나 영구 캐시는 언제 의미 있는가?
- prefix-based 캐싱의 한계 — 도구 호출 결과가 매번 다른 multi-turn 에이전트에서 캐시 히트율을 어떻게 끌어올릴 수 있는가?
- 모델 버전(`claude-opus-4-6` → `claude-opus-4-7`) 마이그레이션 시 캐시는 무효화되는데, 비용 평탄화를 위한 점진 전환 전략은?
