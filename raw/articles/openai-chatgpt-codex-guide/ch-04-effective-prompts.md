---
source_url: https://wikidocs.net/340811
book: ChatGPT & Codex 실무 활용 가이드
author: 송영옥
license: CC-BY (wikidocs by.png 아이콘 표시)
fetched_at: 2026-04-30
ingestion_mode: path-b-summary
---

# Chapter 04. 효과적인 프롬프트 작성법 — AI와 잘 대화하는 기술

## 페이지 구조 (헤딩 outline)
- 프롬프트란 무엇인가
- 프롬프트의 4가지 핵심 구성 요소
  - Role (역할)
  - Context (맥락)
  - Instruction (지시)
  - Format (형식)
- Few-shot 프롬프팅: 예시를 보여주는 기법
- Chain-of-Thought: 단계별 사고를 유도하는 기법
- 시스템 프롬프트와 Custom Instructions 활용
  - 시스템 프롬프트란
  - Custom Instructions 고급 활용
- 나쁜 프롬프트 vs 좋은 프롬프트: Before/After 비교
- GPT-4o vs o3: 프롬프트 전략의 차이
- [실습] 업무 이메일 프롬프트를 단계적으로 개선하기

## 핵심 요약 (자가 작문)

이 장은 ChatGPT 결과물의 품질을 좌우하는 변수가 모델보다 프롬프트라는 전제에서 출발해, 저자가 RCIF라 부르는 4구성 요소 — Role(역할), Context(맥락), Instruction(지시), Format(형식) — 를 뼈대로 한 구조적 작성법을 제시한다. 그 위에 Few-shot으로 원하는 출력 패턴을 학습시키는 기법, Chain-of-Thought로 단계적 사고를 유도하는 기법을 얹어 복잡한 추론 작업에서의 효과를 보여준다. 시스템 프롬프트와 Custom Instructions를 통한 개인화, 나쁜 프롬프트 vs 좋은 프롬프트의 Before/After 비교, GPT-4o(빠른 다용도)와 o3(추론 특화)의 모델 특성에 맞춘 차별화된 전략까지 한 장에 묶어, 처음부터 완벽한 프롬프트를 노리기보다 기본형으로 시작해 결과를 보고 반복적으로 개선하는 실무 워크플로를 권장한다.

## 인용 (key quotes, 짧게)

> "단순히 '요약해줘'와 '마케팅 경험이 없는 스타트업 CEO에게 보내는 투자자 보고서 형식으로...' 의 결과는 전혀 다릅니다."

> "좋은 프롬프트를 처음부터 완벽하게 작성하려 하지 마세요. 기본 프롬프트로 시작하여 결과를 보고, 부족한 부분을 추가해 나가는 반복적 개선 방식이 실무에서 가장 효과적입니다."

## 메타 정보
- 표: 3개 (구성 요소 비교, Before/After 비교, 모델별 전략 비교)
- 코드블록: 12개 (프롬프트 예시)
- 이미지: 1개
- 마지막 편집: 2026-04-12

원본: https://wikidocs.net/340811
