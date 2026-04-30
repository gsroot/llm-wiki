---
title: Chain-of-Thought 프롬프팅 (단계별 사고 유도)
type: concept
category: ai
aliases:
- Chain-of-Thought
- CoT
- chain-of-thought
- 단계별 사고 프롬프팅
- 연쇄 추론
tags:
- prompt-engineering
- chain-of-thought
- cot
- reasoning
- LLM
- chatgpt
- claude
- o3
- agent-patterns
related:
- "[[rcif-prompt-pattern]]"
- "[[context-engineering]]"
- "[[agent-patterns]]"
- "[[autonomous-research-loop]]"
- "[[openai]]"
- "[[anthropic]]"
- "[[claude-code]]"
- "[[openai-chatgpt-codex-guide]]"
source_count: 1
observed_source_refs: 2
inbound_count: 9
created: 2026-04-30
updated: 2026-04-30
cited_by_count: 7
---

# Chain-of-Thought 프롬프팅 (단계별 사고 유도)

## 정의

**Chain-of-Thought(CoT)** 프롬프팅은 LLM이 결론을 곧장 내리지 않고 **단계적으로 사고 과정을 거치도록 유도**하는 기법이다. 복잡한 분석·다단계 추론·문제 해결에서 답변 품질을 크게 향상시킨다. 가장 단순한 트리거는 프롬프트에 "단계별로 생각해줘" 또는 "Let's think step by step" 한 문장 추가.

## 왜 중요한가

- **추론 작업의 품질 결정 변수**: 복잡한 분석·코딩·수학 문제에서 CoT 유무가 결과 정확도를 가른다.
- **모델 진화 방향과 정합**: o1, o3 같은 추론 특화 모델은 내부적으로 CoT를 자동 적용. 즉 CoT는 임시 hack이 아닌 LLM 추론의 표준 패턴으로 정착했다.
- **owner 활용 시나리오**: [[matechat]] 챗봇 모듈, [[c2spf-analytics]] 데이터 분석 진단, [[claude-code]] 디버깅·리팩토링에서 단계별 사고 유도가 일상 작업.

## 핵심 내용

### CoT 없는 vs CoT 적용 비교

**CoT 없는 프롬프트** (얕은 결론):
```
이 사업 계획서의 실패 가능성을 분석해줘.
```

**CoT 적용 프롬프트** (단계별 분석):
```
이 사업 계획서의 실패 가능성을 분석해주세요.
다음 단계로 진행해주세요:

1단계: 시장 분석 — 시장 크기와 경쟁 환경 평가
2단계: 재무 검토 — 수익 모델과 비용 구조의 현실성 검토
3단계: 실행 가능성 — 팀 역량과 리소스의 적합성 평가
4단계: 리스크 요인 — 주요 위험 요소 3가지 도출
5단계: 종합 결론 — 위 분석을 바탕으로 전반적 평가
```

### 트리거 패턴

| 패턴 | 예시 | 적용 |
|---|---|---|
| **단순 문구** | "단계별로 생각해줘" / "Let's think step by step" | 프롬프트 끝에 한 문장 추가, 비용 0 |
| **명시적 단계 정의** | "1단계: X / 2단계: Y / ..." | 분석 프레임워크가 정해진 경우 |
| **사고 → 결론 분리** | "먼저 추론 과정을 적고 마지막에 최종 답을 따로 적어줘" | 결과 활용 시 추론 검토 가능 |
| **자기검증 결합** | "각 단계 끝에 검증 질문을 던지고 답해줘" | 자율 에이전트·복잡 추론 |

### 모델별 CoT 동작

| 모델 | CoT 동작 |
|---|---|
| **GPT-4o, Claude Sonnet 등 일반 모델** | 수동 트리거 필요. 명시적 "단계별로 생각해줘" 추가 시 효과 큼 |
| **OpenAI o1 / o3 (추론 특화)** | 내부적으로 자동 CoT. 수동 지정 불필요, 오히려 명시적 단계 정의가 도움 |
| **Claude Extended Thinking 모드** | 내부 thinking budget으로 자동 CoT, `thinking` 토큰 별도 노출 |

## 실전 적용

### [[rcif-prompt-pattern|RCIF]] + CoT 결합

CoT는 RCIF의 **Instruction(지시)** 슬롯에 단계 정의를 박는 방식으로 결합한다:

```
[Role] 당신은 PostgreSQL DB 인덱싱 전문가입니다.
[Context] 5천만 행 테이블, 날짜+사용자ID 복합 검색 90%, 전체 텍스트 검색 10%.
[Instruction]
  1단계: 현재 쿼리 패턴 분석
  2단계: 후보 인덱스 3개 도출 (각 장단점)
  3단계: 예상 P95 응답시간 비교
  4단계: 최종 추천 + SQL 인덱스 생성 쿼리
[Format] 표 + SQL 코드블록
```

### owner 활용 시나리오

- **[[c2spf-analytics]] BI 진단**: "DAU 하락 원인 분석" 같은 모호한 질의에 CoT 단계(데이터 → 가설 → 검증 → 결론)를 박아 분석 품질 일관화.
- **[[matechat]] 챗봇 답변**: 사용자 복합 질문에 CoT 단계를 백그라운드로 적용해 답변의 논리 일관성 확보.
- **[[claude-code]] 디버깅**: "이 함수가 왜 안 되는가" 같은 디버그 요청에 단계별 사고(가설 → 검증 → 수정)를 강제하면 잘못된 직진형 패치 회피.
- **자율 에이전트 ([[autonomous-research-loop]])**: 각 사이클마다 CoT 체크포인트를 두면 [[karpathy-autoresearch|autoresearch]] 식 연구 루프의 품질 향상.

### 한계 (over-CoT의 함정)

- **단순 작업에 CoT 강제** → 응답 시간 증가, 토큰 비용 증가, 효익 미미
- **정답이 직관적인 케이스** → 모델이 단계 만드느라 잘못된 추론 경로로 가는 case 존재
- **추론 특화 모델 + 명시적 CoT** → 중복 비용. o1·o3는 내부 CoT가 이미 작동하므로 외부 단계 정의는 가이드 역할만.

## 관련 개념

- [[rcif-prompt-pattern]]: CoT는 RCIF의 Instruction에 결합되는 보조 패턴
- [[context-engineering]]: CoT 단계가 길어질수록 컨텍스트 관리·압축 전략과 밀접
- [[agent-patterns]]: Building Effective Agents의 5 패턴 중 "Evaluator-Optimizer"·"Orchestrator-Workers" 모두 CoT 변형
- [[autonomous-research-loop]]: Karpathy의 자율 연구 루프는 본질적으로 long-horizon CoT
- [[harness]]: agent harness가 CoT 사이클별 메모리·도구 호출을 관리

## 출처

- [[openai-chatgpt-codex-guide]] — Ch 4. 효과적인 프롬프트 작성법 (송영옥, 2026). CoT 트리거 패턴과 모델별 차이 정리.

## 열린 질문

- "단계별로 생각해줘" 한 문장의 효과가 모델 발전에 따라 어떻게 진화할지 (o3 이후 세대에선 더 작아질 가능성).
- [[matechat]] 같은 사용자 대면 챗봇에서 CoT 추론 과정을 사용자에게 그대로 노출 vs 최종 답만 노출 — UX 트레이드오프.
