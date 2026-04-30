---
source_url: https://wikidocs.net/340845
book: ChatGPT & Codex 실무 활용 가이드
author: 송영옥
license: CC-BY (wikidocs by.png 아이콘 표시)
fetched_at: 2026-04-30
ingestion_mode: path-b-summary
---

# C. OpenAI API 빠른 참조표

## 페이지 구조 (헤딩 outline)
- C. OpenAI API 빠른 참조표
  - 주요 모델 사양
  - API 가격표 (1M 토큰 기준)
  - 주요 API 엔드포인트
    - Chat Completions
    - Assistants API
    - Images (DALL-E)
    - Audio — Whisper (STT) & TTS
    - Embeddings
    - Moderation
  - Rate Limits 티어별 기준
  - 주요 에러 코드 및 대처법
    - 429 에러 처리 예시 (지수 백오프)

## 핵심 요약 (자가 작문)

이 부록은 OpenAI API를 다루는 개발자를 위한 즉시 활용 가능한 기술 참조표다. 모델 사양과 1M 토큰 기준 가격을 표로 정리했고, Chat Completions·Assistants·Images(DALL-E)·Audio(Whisper/TTS)·Embeddings·Moderation 등 주요 엔드포인트의 사용법을 짧은 코드 예시로 보여준다. Rate Limit 티어 체계를 통해 사용량 한도를 명확히 안내하며, Batch API를 활용한 비동기 처리로 비용을 최대 50% 절감하는 운영 팁도 포함한다. 마지막으로 429 같은 주요 에러 코드와 지수 백오프(exponential backoff) 재시도 전략을 코드와 함께 제시해 실무 장애 대응 능력을 보강한다.

## 인용 (key quotes, 짧게)

> "Batch API를 사용하면 비동기 처리로 최대 50% 비용 절감이 가능합니다."

> "Rate Limit은 모델별로 별도 적용됩니다."

## 메타 정보
- 표: 4개 (모델 사양 / 가격표 / Rate Limits / 에러 코드) / 코드블록: 6개 / 이미지: 1개
- 마지막 편집: 2026-04-12

원본: https://wikidocs.net/340845
