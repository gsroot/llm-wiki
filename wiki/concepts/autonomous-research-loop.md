---
title: 자율 연구 루프 (Autonomous Research Loop)
aliases:
- Autonomous Research Loop
- 자율 연구 루프
- ARL
type: concept
category: ai
tags:
- 자율연구
- agent
- 실험루프
- 시간예산
- harness
- gpt2-speedrun
related:
- '[[harness]]'
- '[[context-engineering]]'
- '[[token-economy]]'
- '[[claude-code]]'
- '[[autoresearch]]'
- '[[nanochat]]'
- '[[karpathy]]'
- '[[karpathy-autoresearch]]'
- '[[karpathy-nanochat]]'
source_count: 2
observed_source_refs: 19
inbound_count: 58
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 25
---

# 자율 연구 루프 (Autonomous Research Loop)

## 정의

AI 에이전트가 **단일 정량 메트릭**과 **고정 시간 예산** 아래에서 코드를 직접 수정·실행·평가하고, 결과 비교 후 keep/discard를 스스로 결정하며 무한 반복하는 운영 패턴. 사람은 파이썬을 만지지 않고 **에이전트 지침서(skill 형태의 마크다운)** 만 다듬는다.

[[autoresearch]] (Karpathy, 2026-03)가 이 패턴의 표준적 시제품.

## 왜 중요한가

이전까지의 "AI 보조 코딩"이 사람-에이전트 페어 프로그래밍에 가까웠다면, 자율 연구 루프는 **사람이 자는 동안 실험이 12회/시간 누적되는** 운영 모델이다. 이는 [[harness]] 개념의 극한 — 하네스를 잘 짜면 사람의 시간이 풀린다.

### 실증: nanochat 리더보드 #5, #6

이 패턴이 사변적이지 않다는 가장 강한 근거 — [[nanochat]]의 Time-to-GPT-2 리더보드(README 공개):

| # | 시간 | 설명 | 날짜 | 기여자 |
|---|-----|------|------|-------|
| 4 | 2.02h | NVIDIA ClimbMix 데이터셋 | 2026-03-04 | @ddudek @karpathy (사람 손) |
| **5** | **1.80h** | **autoresearch round 1** | **2026-03-09** | @karpathy (자율 루프) |
| **6** | **1.65h** | **autoresearch round 2** | **2026-03-14** | @karpathy (자율 루프) |

행 #4가 사람의 손으로 도달한 최고 기록(2.02h). 행 #5에서 [[autoresearch]]가 그걸 능가(1.80h). 즉 **자율 루프가 사람 SOTA를 갱신한 첫 공개 사례**. autoresearch가 발견한 개선은 nanochat master로 머지되어 다음 라운드의 베이스라인이 된다 — **자기 강화 순환**.

[[karpathy]] 본인이 양쪽 저장소를 함께 운영하면서 이 순환을 시연. 행 #4 → #5에서 약 11% 시간 단축. 작아 보이지만 사람 손으로 1년에 한 번 나올 발견을 5일 만에 만들어 냈다는 의미.

석근 관점에서 중요한 이유:
1. **BI 자동화**의 다음 단계: 대시보드 자동 갱신 → 쿼리 자동 튜닝 → 메트릭 주도 자율 실험.
2. **개인 비서 AI**의 운영 모델: 만족도 메트릭 + 시간 예산만 정의하면 prompt/skill을 자가 진화시킬 수 있음.
3. 이 위키 자체가 [[harness]] 사례인데, 자율 연구 루프는 위키 운영의 미래 형태일 가능성.

## 핵심 내용

### 4중 제약 (이게 다 걸려야 작동)

| 제약 | 역할 | autoresearch 사례 |
|------|------|-----------------|
| **단일 정량 메트릭** | 비교 가능성 — 더 좋은가/나쁜가에 모호함 없음 | `val_bpb` (낮을수록 좋음) |
| **고정 시간 예산** | 실험 비교 가능성 + 시간당 처리량 보장 | 5분/실험 (시간당 ~12회) |
| **단일 파일 수정** | diff 리뷰 가능성 / 변경 추적 단순화 | `train.py` 1개 파일만 |
| **무한 루프** | 사람이 끄지 않으면 무기한 진척 | NEVER STOP 원칙 |

4개 중 하나라도 빠지면 폭주(메트릭 부재) 또는 정체(시간 무한정) 또는 디버깅 불가(다중 파일 동시 수정) 또는 단발성(루프 없음)으로 무너진다.

### 5단계 루프 골격

1. **상태 확인**: `git status`, 현재 브랜치 / 커밋
2. **수정**: 가설 1개를 단일 파일에 직접 적용
3. **실행**: 시간 예산 안에서 1회 실행, **출력은 파일로 격리**(`> log 2>&1`)
4. **평가**: `grep` 등으로 메트릭 1줄만 본문 노출
5. **판정 & 분기**: 개선 → 커밋 advance / 동일·악화 → `git reset` / 크래시 → 한 번 시도 후 포기

### 컨텍스트 보호 3원칙

- **stdout 격리**: 학습 로그가 에이전트 컨텍스트에 절대 들어오지 않게 함
- **메트릭 발췌**: `grep "^val_bpb:"` 같이 1줄 패턴으로 결과만 끌어옴
- **크래시 시에만 tail**: 정상 시 로그 자체를 안 봄 → [[token-economy]] 정수

### 결과 기록은 외부 (commit 안 함)

- `results.tsv` 같은 누적 기록은 git untracked
- 이유: 코드 git reset으로 출발점 복귀해도 누적 데이터는 살아남음
- 단순한 트릭이지만 자율 루프 안정성에 직결

### 사람의 역할 = `program.md` 진화

> "The default `program.md` in this repo is intentionally kept as a bare bones baseline, though it's obvious how one would iterate on it over time to find the 'research org code' that achieves the fastest research progress." — autoresearch README

사람이 만지는 건 파이썬이 아니라 **에이전트의 지침서(skill 마크다운)**. 이 사실 자체가 하네스 엔지니어링의 정의 그대로.

## 실전 적용

### 적용 가능 영역

자율 연구 루프가 작동하는 조건:
1. 변경 → 실행 → 메트릭이 짧은 시간 내 닫히는가 (분 단위 권장)
2. 단일 정량 메트릭으로 좋고 나쁨이 명확히 정의되는가
3. 변경 범위가 단일 파일/모듈로 좁혀지는가
4. 평가가 결정론적이거나 노이즈가 충분히 작은가

### 석근 시나리오

**A. BI 쿼리 자율 튜닝**
- 단일 파일: `analytics_query.py` 안의 SQL/조인 전략
- 메트릭: 쿼리 wall-clock latency (10회 평균)
- 시간 예산: 2분/실험
- 평가축: 결과셋 동등성 검증(`prepare.py` 역할)
- 응용: BigQuery slot 사용량 최소화 자율 실험

**B. 개인 비서 AI prompt 진화**
- 단일 파일: `assistant_prompt.md` (또는 skill SKILL.md)
- 메트릭: LLM-as-judge 만족도 점수 + 응답 latency 가중평균
- 시간 예산: 30초/실험 × 평가 N회
- 평가축: 고정 테스트 대화 100개 (`prepare.py` 역할)
- 자가 진화하는 프롬프트로 발전

**C. 위키 운영 진화 (가설)**
- 단일 파일: `~/.claude/skills/wiki/SKILL.md` ([[slash-commands-vs-agent-skills]] 참조)
- 메트릭: ??? — 정의가 가장 어려운 부분. 후보: "정답률"(고정 질의 세트 기반), "토큰/질의" (적을수록 좋음)
- 메트릭 정의가 안 되는 한 자율 루프 적용 불가. 이 점이 위키 운영을 자동화하기 어려운 본질적 이유.

### 안티패턴

- 메트릭이 모호한 영역(디자인 품질, 글의 좋음)에 그대로 적용 → 평가축 부재로 폭주
- 다중 파일 변경 허용 → diff가 폭발하고 git reset이 깨끗하지 않게 됨
- stdout을 그대로 받기 → 컨텍스트 윈도우가 1~2회 만에 고갈
- 무한 루프에 사람이 자주 개입 → 자율성의 의미 자체 상실

## 관련 개념

- [[harness]]: 자율 연구 루프는 하네스를 극한으로 압축한 형태
- [[context-engineering]]: 로그 격리·메트릭 발췌가 컨텍스트 엔지니어링의 모범
- [[token-economy]]: 실험당 토큰 예산을 메트릭 1줄로 압축
- [[claude-code]]: 실행 에이전트 후보. autoresearch가 명시
- [[slash-commands-vs-agent-skills]]: program.md = "lightweight skill"이라는 호명에서 직접 연결

## 출처

- [[karpathy-autoresearch]] — Karpathy의 autoresearch (2026-03), 이 패턴의 표준 시제품
- [[karpathy-nanochat]] — 부모 저장소. README의 Time-to-GPT-2 리더보드 #5/#6 행이 autoresearch 라운드로 갱신됨 (실증 데이터)

## 열린 질문

- **메트릭이 모호한 영역의 자율 연구**: 위키 운영, 글쓰기, 디자인처럼 평가가 주관적인 영역에서 자율 루프는 어떻게 가능한가? LLM-as-judge로 충분한가?
- **여러 에이전트의 협업**: program.md를 1개가 아니라 N개로 늘리고 역할을 분리(planner/runner/reviewer)하면 진척이 빨라지는가, 아니면 통신 오버헤드가 더 커지는가?
- **메트릭 게이밍 방지**: val_bpb를 hack하는 변경(예: 평가 데이터를 학습에 노출)을 에이전트가 자발적으로 발견할 가능성은? prepare.py 잠금만으로 충분한가?
- **시간 예산의 합리적 길이**: 5분이 LLM 학습엔 적당하지만, BI 쿼리는 30초, prompt 평가는 10초가 더 맞을 수 있다. 하한선이 있는가?
