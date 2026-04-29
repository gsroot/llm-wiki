---
title: "karpathy/nanoGPT — 가장 단순한 GPT 학습 코드 (deprecated)"
type: source
source_type: article
source_url: "https://github.com/karpathy/nanoGPT"
raw_path: "raw/articles/karpathy-nanogpt/"
author: "Andrej Karpathy"
date_published: 2022-12-28
date_ingested: 2026-04-27
tags: [nanogpt, karpathy, gpt, LLM, 교육코드, deprecated, mingpt, 단일파일, mps]
related:
  - "[[karpathy]]"
  - "[[nanogpt]]"
  - "[[nanochat]]"
  - "[[autoresearch]]"
confidence: high
cited_by:
  - "[[agent-stack-evolution]]"
  - "[[harness]]"
  - "[[karpathy]]"
  - "[[nanogpt]]"
---

# karpathy/nanoGPT — 가장 단순한 GPT 학습 코드 (deprecated)

## 한줄 요약

> 2022년 말 Karpathy가 공개한, **`train.py` ~300줄 + `model.py` ~300줄로 GPT-2(124M)를 재현**할 수 있는 학습/파인튜닝 저장소. 2025년 11월부로 **공식 deprecated** — 후속작 [[nanochat]]을 사용 권장.

## 핵심 내용

### 위치 (deprecated 상태)

README 최상단(2025-11):

> "nanoGPT has a new and improved cousin called [nanochat](https://github.com/karpathy/nanochat). It is very likely you meant to use/find nanochat instead. nanoGPT (this repo) is now very old and deprecated but I will leave it up for posterity."

따라서 **신규 학습은 nanochat 권장**, nanoGPT는 역사·교육 자료로만 보존됨. 그럼에도 57k+ stars 규모이며 LLM 입문 표준 경로의 일부.

### 디자인 원칙

- **두 파일이 본체**: `train.py` ~300줄(학습 루프) + `model.py` ~300줄(GPT 모델 정의). "if-then-else 괴물" 없음.
- **선조 minGPT의 후계**: minGPT가 "교육 우선"이라면 nanoGPT는 "이빨 우선"(prioritizes teeth over education) — 실제 GPT-2 124M을 8×A100 40GB 노드에서 4일이면 재현 가능한 수준.
- **단일 GPU 시작 → 분산까지**: `python train.py`(단일) / `torchrun --nproc_per_node=8`(노드) / `--nnodes=2`(멀티노드) 모두 같은 코드.
- **Apple Silicon 지원 추가**: `--device=mps` 플래그로 MacBook에서 2~3배 가속(Issue #28).

### 진입 단계

| 환경 | 학습 시간 | 결과 |
|------|----------|------|
| 1× A100, Shakespeare-char | ~3분 | val loss 1.4697 (캐릭터 단위, 6층 GPT) |
| MacBook CPU, dialed-down | ~3분 | val loss 1.88 (~ "그럴듯한 문자 패턴") |
| 8× A100, GPT-2 124M | 4일 | val loss ~2.85 (OWT, GPT-2 ~2.85와 매치) |

### 의존성 (가벼움)

```
torch numpy transformers datasets tiktoken wandb tqdm
```

분산 학습은 PyTorch DDP 직접 사용. FSDP는 todo.

### 한계 (deprecated 사유)

- **사전학습만** — finetune까지는 있으나 SFT/RL/inference UI/tool use 없음
- **GPT-2 시대 아키텍처** — RoPE / GQA / Muon optimizer 등 2024~2026 표준이 빠짐
- **단일 다이얼 추상화 부재** — 모든 하이퍼파라미터를 사용자가 직접 조정
- **벤치마크 평가 미내장** — 사용자가 직접 추가해야 함

이 모든 항목이 [[nanochat]]에서 해결됨.

## 주요 인사이트

### 1. nanoGPT 디자인이 후속 모든 작업의 DNA

`train.py`/`model.py`/`prepare.py` 트라이어드 + uv/pyproject.toml 단순화 + 단일 파일 수정 패턴은 [[nanochat]]에 그대로 계승되고, [[autoresearch]]에서 극단적으로 단순화됐다. 즉 **이 위키가 다루는 "단일 파일 + 단일 메트릭" 패턴의 시조**.

### 2. "Teeth over education"의 의미

minGPT가 학습용 코드(가독성 최우선)였다면 nanoGPT는 **실제 SOTA를 재현 가능한 수준의 단순 코드**. 이 균형이 후속 [[nanochat]]에서 한 번 더 옮겨감 — "최소이면서도 풀 파이프라인($100 GPT-2)".

### 3. MacBook 학습 가능성을 처음 정착시킨 코드

`--device=mps` 플래그로 Apple Silicon에서 LLM 사전학습이 가능함을 일반화. 이후 [[autoresearch]] macOS 포크들도 같은 흐름의 연장.

### 4. 작은 코드베이스 = 큰 fork 생태계

57k+ stars / 수많은 fork. 코드가 작을수록 **개인이 손대볼 수 있는 영역이 커지고, 개인 fork의 학습 경로가 풍부해진다**. 이 위키 운영 원칙(작은 페이지 우선)과 같은 사상.

## 관련 엔티티/개념

- [[karpathy]]: 저자
- [[nanogpt]]: 이 저장소 자체 (entity 페이지)
- [[nanochat]]: 후속작, 활성 주력 — nanoGPT는 사전학습만이지만 nanochat은 풀 파이프라인
- [[autoresearch]]: nanochat의 단일-GPU 단순화판 + 자율 실험 — nanoGPT 디자인 유전자의 두 번째 자손
- [[ml-ai]]: 석근의 ML/AI 영역 학습 자료 후보
- [[harness]] / [[autonomous-research-loop]]: 단일 파일 수정 패턴의 시조 코드

## 인용할 만한 구절

> "It is a rewrite of [minGPT](https://github.com/karpathy/minGPT) that prioritizes teeth over education."
> — README

> "Because the code is so simple, it is very easy to hack to your needs, train new models from scratch, or finetune pretrained checkpoints."
> — README

> "For some context on this repository, GPT, and language modeling it might be helpful to watch my [Zero To Hero series](https://karpathy.ai/zero-to-hero.html)."
> — README

## 메모

- **deprecated 상태이지만 raw/에 보존**: 역사적 가치 + 위키의 [[autoresearch]]·[[nanochat]] 페이지가 nanoGPT를 빈번히 참조하므로 1차 자료가 있어야 함.
- **석근 입장**: nanoGPT를 굳이 돌릴 필요 없음 — nanochat이 동일 코드 구조를 더 풍부하게 제공. 다만 [[karpathy]]의 [Zero to Hero 비디오 시리즈](https://karpathy.ai/zero-to-hero.html)와 함께 학습 자료로는 여전히 가치 있음 (특히 [GPT 비디오](https://www.youtube.com/watch?v=kCc8FmEb1nY)).
- **후속 탐구**: minGPT(전신)도 raw 보관 가치가 있는가? — 패턴 계보의 처음이 minGPT이지만, 위키 운영상 nanoGPT가 표준 출발점이 된 만큼 minGPT까지는 보류.
