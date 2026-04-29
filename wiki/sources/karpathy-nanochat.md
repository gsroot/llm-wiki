---
title: "karpathy/nanochat — $100짜리 ChatGPT 풀 파이프라인"
type: source
source_type: article
source_url: "https://github.com/karpathy/nanochat"
raw_path: "raw/articles/karpathy-nanochat/"
author: "Andrej Karpathy"
date_published: 2025-10-13
date_ingested: 2026-04-27
tags: [nanochat, karpathy, LLM, gpt2-speedrun, depth-dial, 컴퓨트옵티멀, val-bpb, dclm-core, sft, rl, autoresearch]
related:
  - "[[karpathy]]"
  - "[[nanochat]]"
  - "[[nanogpt]]"
  - "[[autoresearch]]"
  - "[[autonomous-research-loop]]"
  - "[[ml-ai]]"
confidence: high
cited_by:
  - "[[agent-stack-evolution]]"
  - "[[autonomous-research-loop]]"
  - "[[karpathy]]"
  - "[[nanochat]]"
---

# karpathy/nanochat — $100짜리 ChatGPT 풀 파이프라인

## 한줄 요약

> "$100로 살 수 있는 가장 좋은 ChatGPT" — **단일 8×H100 GPU 노드에서 ~2시간(~$48)에 GPT-2급 LLM을 토큰화부터 사전학습·SFT·RL·평가·추론·웹 채팅 UI까지 풀 파이프라인으로 학습**할 수 있는 최소 실험 하네스. [[nanogpt]]의 후속 활성 주력.

## 핵심 내용

### 위치 (활성 주력)

- 2025-10-13 공개, 수집 시점 **52,557 stars**
- [[nanogpt]] (deprecated)이 사전학습만이었다면, nanochat은 **토큰화 → 사전학습 → SFT → RL → 평가 → 추론 → 웹 UI** 풀 스택
- [[autoresearch]]는 nanochat의 **단일-GPU 단순화판**. 즉 nanochat이 부모, autoresearch가 자식.

### 디자인 핵심: 단일 다이얼 `--depth`

> "nanochat is configured out of the box to train an entire miniseries of compute-optimal models by setting one single complexity dial: `--depth`, the number of layers in the GPT transformer model."

`--depth` 정수 하나만 주면:
- transformer width
- number of heads
- learning rate adjustments
- training horizons
- weight decays

가 모두 **자동으로 compute-optimal하게 산출**됨. GPT-2급 ≈ depth 24~26.

이 한 줄짜리 추상화가 nanochat을 "프레임워크"가 아닌 **"강한 baseline 코드베이스"**로 정의하는 핵심.

### Time-to-GPT-2 리더보드 (2026-03 기준)

| # | 시간 | val_bpb | CORE | 설명 | 날짜 | 기여자 |
|---|-----|---------|------|------|------|-------|
| 0 | 168시간 | - | 0.2565 | OpenAI GPT-2 (2019, ~$43,000) | 2019 | OpenAI |
| 1 | 3.04 | 0.74833 | 0.2585 | d24 baseline | 2026-01-29 | @karpathy |
| 2 | 2.91 | 0.74504 | 0.2578 | d26 + fp8 | 2026-02-02 | @karpathy |
| 3 | 2.76 | 0.74645 | 0.2602 | total batch 1M tokens | 2026-02-05 | @karpathy |
| 4 | 2.02 | 0.71854 | 0.2571 | NVIDIA ClimbMix 데이터셋 | 2026-03-04 | @ddudek @karpathy |
| **5** | **1.80** | 0.71808 | 0.2690 | **autoresearch round 1** | **2026-03-09** | @karpathy |
| **6** | **1.65** | 0.71800 | 0.2626 | **autoresearch round 2** | **2026-03-14** | @karpathy |

**핵심: 행 #5, #6이 [[autoresearch]]로 진행됨**. 즉 [[autonomous-research-loop]] 패턴이 실제 SOTA를 갱신한 검증 사례.

168시간 → 1.65시간 = **102배 단축**, 비용은 $43,000 → ~$48 = **900배 절감**.

### 풀 파이프라인 구성 (`nanochat/` 모듈)

| 파일 | 역할 |
|------|------|
| `gpt.py` | GPT `nn.Module` (Transformer) |
| `optim.py` | AdamW + Muon 옵티마이저 |
| `dataloader.py` | 토크나이즈 분산 데이터 로더 |
| `dataset.py` | 사전학습 데이터 다운로드/리드 |
| `tokenizer.py` | GPT-4 스타일 BPE 토크나이저 래퍼 |
| `loss_eval.py` | val_bpb 평가 |
| `core_eval.py` | DCLM CORE score 평가 |
| `engine.py` | KV 캐시 추론 엔진 |
| `execution.py` | LLM의 Python tool use |
| `checkpoint_manager.py` | 체크포인트 |
| `report.py` | 학습 리포트 자동 생성 |
| `ui.html` | 채팅 프론트엔드 |

`scripts/`는 학습/평가 진입점:
- `tok_train.py`/`tok_eval.py`(토크나이저)
- `base_train.py`/`base_eval.py`(사전학습)
- `chat_sft.py`/`chat_rl.py`/`chat_eval.py`(채팅 모델)
- `chat_cli.py`/`chat_web.py`(추론 UI)

`tasks/`는 평가 데이터셋:
- `arc.py`, `mmlu.py`(객관식), `gsm8k.py`(수학), `humaneval.py`(코딩), `smoltalk.py`(SmolTalk), `spellingbee.py`(철자/카운팅)

`runs/`는 시나리오 스크립트:
- `speedrun.sh` — $100 GPT-2 재현 표준 경로
- `miniseries.sh` — depth 다양화 스윕
- `scaling_laws.sh` — 스케일링 법칙 실험
- `runcpu.sh` — CPU/MPS 축소 학습

### 정밀도(dtype) 자동 감지

```
hardware            COMPUTE_DTYPE
CUDA SM 80+         bfloat16  (A100/H100 native bf16)
CUDA SM < 80        float32   (V100/T4)
CPU / MPS           float32
```

`NANOCHAT_DTYPE` 환경변수로 강제 가능. Karpathy는 `torch.amp.autocast` 대신 **단일 글로벌 `COMPUTE_DTYPE`**을 두고 `Linear` 레이어가 forward 시점에 캐스팅하는 명시적 설계 선택.

### 운영 권장: 빠른 반복은 d12 (GPT-1 사이즈)

> "For quick experimentation (~5 min pretraining runs) my favorite scale is to train a 12-layer model (GPT-1 sized)."

5분 단위 사전학습 실험으로 변경 효과를 빠르게 확인. autoresearch의 5분 시간 예산도 같은 사상.

## 주요 인사이트

### 1. autoresearch 검증 — 자율 루프가 SOTA를 갱신

리더보드 #5, #6이 [[autoresearch]]로 갱신된 사실은 [[autonomous-research-loop]] 패턴의 **실증 데이터**. 위키에서 이 패턴을 "사변적 가능성"이 아니라 "검증된 운영 모델"로 격상시킬 근거.

특히 행 #4(human, 2.02h) → 행 #5(autoresearch, 1.80h)에서 **사람 최고 기록을 자율 루프가 능가**. 이건 결정적.

### 2. 단일 다이얼 = compute-optimal 자동화

`--depth` 한 정수로 모든 하이퍼파라미터가 결정되는 디자인은 [[harness]]의 "통제 레이어 단순화" 정수. 사용자는 "더 큰 모델 / 더 작은 모델"만 결정하고 나머지 trade-off는 코드가 처리. 이게 곧 **하네스가 사용자의 인지 부담을 흡수**하는 표준.

### 3. "프레임워크가 아니라 강한 baseline"

> "nanochat is not an exhaustively configurable LLM 'framework'; there are no giant configuration objects, model factories, or if-then-else monsters."

이 한 줄이 [[karpathy]]의 일관된 코딩 미학. configurable framework는 사용자에게 N×M 결정점을 떠넘기지만, **strong baseline은 좋은 기본값과 단일 다이얼**을 제공한다. 위키 운영에도 적용 가능 — CLAUDE.md를 "강한 baseline"으로 두고 사용자 결정점을 최소화.

### 4. $100 GPT-2 재현은 접근성 사건

2019년 GPT-2가 $43k였던 게 2026년 $48로 떨어진 건 **하드웨어 + 알고리즘 + 데이터 + 코드 효율의 누적 효과**. 7년 만에 ~900배. 개인 학습자가 ChatGPT급 모델을 $100 미만으로 직접 학습 가능한 시대 — [[ml-ai]] 페이지의 후속 동향으로 기록 가치.

### 5. AI Policy 명시

> "Current AI policy: disclosure. When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand."

LLM 시대의 **이해 못 한 코드 제출 금지** 원칙. 이게 오픈소스 운영 정책으로 명문화된 사례. 위키 운영(Claude Code로 작성하지만 검증 책임은 석근)에도 동일 원칙 적용 가능.

## 관련 엔티티/개념

- [[karpathy]]: 저자
- [[nanochat]]: 이 저장소 자체 (entity 페이지)
- [[nanogpt]]: 사전학습만 다룬 전작 (deprecated)
- [[autoresearch]]: nanochat의 단일-GPU 단순화판 + 자율 실험 — 리더보드 #5, #6 기여
- [[autonomous-research-loop]]: nanochat 리더보드로 검증된 패턴
- [[harness]]: `--depth` 단일 다이얼 = 통제 레이어 압축 사례
- [[ml-ai]]: 석근의 ML/AI 영역에 직접 들어가는 자료

## 인용할 만한 구절

> "nanochat is the simplest experimental harness for training LLMs."
> — README

> "All other hyperparameters (...) are calculated automatically in an optimal way."
> — README on `--depth`

> "It is a single, cohesive, minimal, readable, hackable, maximally-forkable 'strong baseline' codebase designed to run start to end and produce a ChatGPT model you can talk to."
> — README on contribution philosophy

> "Current AI policy: disclosure. When submitting a PR, please declare any parts that had substantial LLM contribution and that you have not written or that you do not fully understand."
> — README

## 메모

- **시민 LLM 학습의 표준 출발점**: nanochat은 향후 [[ml-ai]] 페이지에서 "개인이 LLM 학습을 처음 해본다면 어디서 시작하는가"의 답.
- **autoresearch와의 동기화**: nanochat README가 갱신되면 [[autoresearch]] 페이지의 "부모 저장소" 섹션, [[autonomous-research-loop]]의 "실증" 섹션도 동기화 필요.
- **석근 응용 가능성**:
  - **학습/실습**: 8×H100을 빌릴 일은 거의 없으나, `runcpu.sh`로 MacBook M4 Pro에서 축소판 학습 직접 시도 가능 — Karpathy 표현 "you will not get strong results in this way"이지만 코드 흐름 체감엔 충분.
  - **단일 다이얼 디자인 차용**: 회사 BI 도구나 개인 비서 AI에 "사용자는 --priority만 정하고 나머지는 자동" 같은 추상화 도입 검토.
  - **DeepWiki 활용**: README가 [DeepWiki](https://deepwiki.com/karpathy/nanochat) 링크를 안내. 코드 질문은 그쪽에 위임 가능.
- **후속 탐구**:
  1. `runs/runcpu.sh` 실제 가동 → MacBook M4 Pro에서 어디까지 되는가
  2. autoresearch round 3 이후 결과가 나오면 리더보드 행 추적
  3. nanochat의 `tasks/spellingbee.py` 같은 기능별 학습 패턴은 [[ml-ai]]에서 응용 가능
