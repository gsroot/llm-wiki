---
title: nanoGPT (karpathy/nanoGPT)
type: entity
entity_type: project
tags:
- nanogpt
- karpathy
- gpt
- LLM
- 교육코드
- deprecated
- mingpt
- 단일파일
- mps
- MIT
related:
- '[[karpathy]]'
- '[[nanochat]]'
- '[[autoresearch]]'
- '[[ml-ai]]'
- '[[karpathy-nanogpt]]'
source_count: 1
observed_source_refs: 7
inbound_count: 16
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 7
---

# nanoGPT (karpathy/nanoGPT)

## 개요

Karpathy가 2022-12-28 공개한 GPT 학습/파인튜닝 저장소. **`train.py` ~300줄 + `model.py` ~300줄**로 GPT-2(124M)를 8×A100 노드에서 4일이면 재현 가능. minGPT의 후계로 "교육보다 이빨 우선"(prioritizes teeth over education)이 모토.

수집 시점 **57,222 stars** / MIT 라이선스 / Python.

**상태: deprecated** — 2025-11 README 최상단에 Karpathy가 직접 "now very old and deprecated, kept for posterity" 표기. 후속작 [[nanochat]] 사용 권장.

## 주요 특징

### 디자인 원칙

- **두 파일 본체**: `train.py`(학습 루프) + `model.py`(GPT 모델). "if-then-else 괴물" 없음.
- **단일 GPU → 분산까지 동일 코드**: `python train.py` / `torchrun --nproc_per_node=8` / 멀티노드까지.
- **PyTorch 2.0 `torch.compile()` 활용**: iter당 250ms → 135ms로 자동 가속.
- **MPS 지원**: `--device=mps`로 Apple Silicon 2~3배 가속(Issue #28). 이게 후대 [[autoresearch]] macOS 포크들의 시발점.

### 학습 진입 단계 (README 인용)

| 환경 | 시간 | val loss |
|------|-----|---------|
| 1×A100, Shakespeare-char | ~3분 | 1.4697 |
| MacBook CPU, dialed-down | ~3분 | 1.88 |
| 8×A100, GPT-2 124M | 4일 | ~2.85 (OWT) |

### 사전학습 베이스라인 (OpenAI 체크포인트 평가)

| 모델 | params | val loss |
|------|-------|---------|
| gpt2 | 124M | 3.12 |
| gpt2-medium | 350M | 2.84 |
| gpt2-large | 774M | 2.67 |
| gpt2-xl | 1558M | 2.54 |

### 의존성

```
torch numpy transformers datasets tiktoken wandb tqdm
```

분산은 PyTorch DDP 직접 사용. FSDP는 미구현(todo).

### 한계 (deprecated 사유)

- **사전학습만** — finetune까지는 있으나 SFT/RL/inference UI/tool use 없음 → 모두 [[nanochat]]에서 구현
- **GPT-2 시대 아키텍처** — RoPE, GQA, Muon optimizer 등 2024~2026 표준 미반영
- **단일 다이얼 추상화 부재** — 모든 하이퍼파라미터를 사용자가 직접 설정
- **벤치마크 평가 미내장** — DCLM CORE 같은 표준 평가 없음

## 관련 개념

- [[ml-ai]]: 석근의 ML/AI 영역 학습 자료 후보
- [[harness]]: 단일 파일 수정 패턴의 시조 — `train.py` 한 파일로 GPT 학습이 가능하다는 디자인
- [[autonomous-research-loop]]: 그 디자인 유전자가 [[autoresearch]]의 단일 메트릭+시간 예산까지 진화

## 자손 계보

```
minGPT (교육 우선)
  ↓
nanoGPT (이빨 우선) ← 이 페이지
  ↓
nanochat (풀 파이프라인, 활성)
  ↓
autoresearch (단일-GPU 단순화 + 자율 실험)
```

각 단계마다 **"단일 파일 + 최소 의존성 + 해킹 가능"** 디자인 미학이 누적되며 진화.

## 출처

- [[karpathy-nanogpt]] — 2022-12 공개, 2025-11 deprecated 처리. README 13.8KB.

## 메모

- **deprecated이지만 위키에 보존하는 이유**:
  1. [[autoresearch]]·[[nanochat]] 페이지가 "nanoGPT 후속작" 맥락을 빈번히 참조
  2. LLM 입문 표준 경로의 일부 — [Zero to Hero 비디오 시리즈](https://karpathy.ai/zero-to-hero.html)와 짝지어 학습 가능
  3. `--device=mps` 같은 디테일이 Apple Silicon ML 학습의 표준 경로 정착에 기여
- **석근 액션 없음**: 학습 의도가 있다면 nanochat으로 직행 권장. nanoGPT는 코드 읽기 자료로만.
- **후속 탐구**: minGPT(전신)도 raw에 보관할 가치가 있는지 — 패턴 계보의 처음이지만 실용성은 nanoGPT보다 낮음. 지금은 보류.
