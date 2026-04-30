---
title: nanochat (karpathy/nanochat)
type: entity
entity_type: project
tags:
- nanochat
- karpathy
- LLM
- gpt2-speedrun
- depth-dial
- 컴퓨트옵티멀
- val-bpb
- dclm-core
- sft
- rl
- MIT
related:
- '[[karpathy]]'
- '[[nanogpt]]'
- '[[autoresearch]]'
- '[[autonomous-research-loop]]'
- '[[ml-ai]]'
- '[[harness]]'
- '[[karpathy-nanochat]]'
source_count: 1
observed_source_refs: 10
inbound_count: 27
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 8
---

# nanochat (karpathy/nanochat)

## 개요

Karpathy가 2025-10-13 공개한 LLM 풀 파이프라인 학습 저장소. 슬로건은 **"The best ChatGPT that $100 can buy."** 단일 8×H100 노드에서 ~2시간(~$48)에 토큰화·사전학습·SFT·RL·평가·추론·웹 UI까지 풀 스택 학습. [[nanogpt]] (deprecated)의 활성 후속.

수집 시점 **52,557 stars** / MIT / Python. [[autoresearch]]가 이 저장소의 단일-GPU 단순화판이며, **nanochat의 Time-to-GPT-2 리더보드 #5, #6 행에 autoresearch가 직접 기여**.

## 주요 특징

### 풀 파이프라인 (nanoGPT vs nanochat)

| 영역 | nanoGPT | nanochat |
|------|---------|---------|
| 토큰화 | tiktoken 사용 | 자체 BPE 학습 (`tok_train.py`) |
| 사전학습 | ✓ | ✓ (`base_train.py`) |
| 평가 | val loss만 | val_bpb + DCLM CORE + ARC/MMLU/GSM8K/HumanEval |
| SFT | ✗ | ✓ (`chat_sft.py`) |
| RL | ✗ | ✓ (`chat_rl.py`) |
| 추론 엔진 | sample.py | KV 캐시 엔진 (`engine.py`) |
| Tool use | ✗ | ✓ (`execution.py` — Python 실행) |
| 채팅 UI | ✗ | ✓ (`chat_web.py` + `ui.html`) |
| 자동 리포트 | ✗ | ✓ (`report.py`) |

### 단일 다이얼 디자인 `--depth`

`--depth` 한 정수만 정하면:
- transformer width
- number of heads
- learning rate adjustments
- training horizons
- weight decays

가 모두 **자동으로 compute-optimal 산출**. GPT-2급 ≈ depth 24~26. 이게 [[harness]]의 "통제 레이어 단순화" 정수.

### 옵티마이저 / 정밀도

- **AdamW + Muon** (`optim.py`) — 1GPU와 분산 양쪽 지원
- **단일 글로벌 `COMPUTE_DTYPE`** — `torch.amp.autocast` 대신 명시적 캐스팅, `Linear` 레이어가 forward 시점에 변환
- 자동 감지: CUDA SM 80+ → bf16 / SM<80 → fp32 / CPU/MPS → fp32. `NANOCHAT_DTYPE` 환경변수로 강제 가능.

### Time-to-GPT-2 리더보드 (활성 진행 중)

- 행 #0: OpenAI GPT-2 (2019, 168시간, ~$43,000)
- 행 #1~4: 사람 손으로 진척 (3.04h → 2.02h)
- **행 #5, #6: autoresearch round 1, 2가 갱신 (2.02h → 1.65h)**

총 168h → 1.65h = **102배 단축**, 비용 $43k → ~$48 = **900배 절감**. 현재 활성 발전 중.

### 하드웨어 가이드

| 하드웨어 | 동작 |
|---------|------|
| 8×H100 (권장) | speedrun 표준 |
| 8×A100 | OK, 약간 느림 |
| 1×GPU | OK, gradient accumulation 자동, 8배 느림 |
| <80GB VRAM | `--device-batch-size`를 16/8/4/2/1로 낮춰야 함 |
| CPU/MPS | `runs/runcpu.sh`로 축소판 가능 (학습 효과는 약함) |

### 평가 태스크 (`tasks/`)

`arc.py`(객관식 과학), `mmlu.py`(다영역 객관식), `gsm8k.py`(수학), `humaneval.py`(Python 코딩), `smoltalk.py`(SmolTalk), `spellingbee.py`(철자/카운팅), `customjson.py`(커스텀 jsonl).

## 관련 개념

- [[autonomous-research-loop]]: nanochat 리더보드 #5, #6에서 검증된 패턴
- [[harness]]: `--depth` 단일 다이얼 = 통제 레이어 압축의 정수
- [[ml-ai]]: 석근의 ML/AI 영역. nanochat은 "$100 GPT-2"라는 접근성 사건으로 한 시대를 정의

## 자손 계보 (전체)

```
minGPT (교육 우선)
  ↓
nanoGPT (이빨 우선, deprecated 2025-11)
  ↓
nanochat (풀 파이프라인, 활성) ← 이 페이지
  ↓
autoresearch (단일-GPU 단순화 + 자율 실험)
```

[[autoresearch]]가 nanochat에 다시 영향을 주는 **순환** — autoresearch가 발견한 개선이 nanochat 마스터로 머지되는 구조(리더보드 #5, #6).

## AI Policy (Karpathy 명문화)

> "When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand."

LLM 시대 오픈소스 공헌 정책의 표준 사례. 위키 운영(Claude Code로 작성하지만 검증 책임은 석근)도 동일 원칙 적용 가능.

## 외부 참고

- [DeepWiki(nanochat)](https://deepwiki.com/karpathy/nanochat) — Devin/Cognition이 만든 코드 Q&A 페이지. README가 직접 안내.
- [#nanochat Discord](https://discord.com/channels/1020383067459821711/1427295580895314031)
- [Feb 1 2026: Beating GPT-2 for <<$100: the nanochat journey](https://github.com/karpathy/nanochat/discussions/481) — 가이드 글
- 인용: `@misc{nanochat, author = {Andrej Karpathy}, year = {2025}, ...}`

## 출처

- [[karpathy-nanochat]] — 2025-10 공개, 활성 발전 중. README 16.5KB. 리더보드 / 단일 다이얼 / 풀 파이프라인 / autoresearch 기여 사실 모두 포함.

## 메모

- **시민 LLM 학습의 표준 출발점**: 향후 [[ml-ai]] 페이지에서 "개인이 LLM 학습을 처음 해본다면 어디서?"의 답.
- **autoresearch와의 동기화**: nanochat이 활성이고 리더보드가 갱신되면 [[autoresearch]] 페이지의 "부모 저장소" 섹션 / [[autonomous-research-loop]] "실증" 섹션 / 본 페이지 리더보드 표 — 3곳을 함께 갱신해야 함.
- **석근 응용**:
  - **MacBook M4 Pro**: `runs/runcpu.sh`로 축소판 학습 시도 가능 (~10분, 약한 결과). 코드 흐름 체감용.
  - **단일 다이얼 차용**: 회사 BI 도구나 개인 비서 AI에 "사용자는 우선순위 한 가지만 정하고 나머지는 자동" 같은 추상화 — 의외로 [[harness]] 설계의 가장 중요한 한 줄.
  - **AI policy**: 위키 페이지/CLAUDE.md에 "LLM이 작성한 부분은 명시" 같은 정책 추가 검토.
- **후속 탐구**:
  1. autoresearch round 3+ 결과를 정기 추적 (리더보드 갱신 시 본 페이지 표 업데이트)
  2. `runcpu.sh`로 M4 Pro 축소판 한 번 돌려보기 (실측 + 페이지 보강)
  3. nanochat의 `tasks/spellingbee.py`처럼 "특정 능력 학습" 패턴을 [[ml-ai]] 응용 가설로 정리
