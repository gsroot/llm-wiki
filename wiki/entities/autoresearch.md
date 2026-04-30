---
title: "autoresearch (karpathy/autoresearch)"
type: entity
entity_type: project
tags: [autoresearch, karpathy, LLM, agent, 자율연구, nanochat, val-bpb, gpu, 단일파일, MIT, nanochat-leaderboard, 에이전트]
related:
  - "[[karpathy]]"
  - "[[autonomous-research-loop]]"
  - "[[harness]]"
  - "[[claude-code]]"
  - "[[nanochat]]"
  - "[[nanogpt]]"
source_count: 1
observed_source_refs: 15
inbound_count: 44
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 15
---

# autoresearch (karpathy/autoresearch)

## 개요

Andrej Karpathy가 2026-03-06 공개한 GitHub 저장소(MIT). **단일 NVIDIA GPU + 5분 시간 예산** 위에서 LLM 학습 실험을 AI 에이전트가 자율 반복하게 만드는 시제품. 사람은 파이썬을 안 만지고 `program.md`(에이전트 지침서)만 다듬는다.

수집 시점 76,912 stars. 노출된 포크 4종(macos / mlx / win-rtx / amd)으로 단일-GPU 환경 다변화에 대응 중.

## 주요 특징

### 저장소 구성

| 파일 | 역할 | 누가 만지나 |
|------|------|------------|
| `prepare.py` | 고정 평가축(데이터, 토크나이저, `evaluate_bpb`) | 절대 안 만짐 |
| `train.py` | GPT 모델·Muon+AdamW 옵티마이저·학습 루프 (단일 파일) | 매 실험마다 에이전트가 수정 |
| `program.md` | 에이전트 지시서 — 셋업·실험·로깅 워크플로우 | 사람이 시간을 들여 다듬음 |
| `pyproject.toml` | 최소 의존성, 추가 금지 | 고정 |
| `analysis.ipynb` | 실험 결과 분석용 | 보조 |

### 운영 원칙 (program.md)

- 브랜치 격리: `autoresearch/<tag>` 브랜치를 독립적으로 사용
- 메트릭 단일화: `val_bpb` (validation bits per byte, vocab-size 독립)
- 시간 예산: 5분 고정 — 시간당 ~12 실험, 평균 수면 동안 ~100 실험
- 컨텍스트 절약: `> run.log 2>&1`로 출력 격리, `grep` 1줄 발췌만 본문 노출
- 결과는 untracked: `results.tsv`는 git에 안 올림 → `git reset` 시 상태 보존
- NEVER STOP: 사람이 수동으로 멈출 때까지 무한 반복
- Simplicity 기준: 동등하면 단순한 게 낫다 / 코드 삭제로 동등 결과면 무조건 채택

### 실행 에이전트

문서가 상정하는 실행 환경: "spin up your Claude/Codex or whatever you want in this repo (and disable all permissions)." → [[claude-code]] / Codex / 기타 자율 코딩 에이전트 모두 후보.

## 관련 개념

- [[autonomous-research-loop]]: 이 저장소가 시연한 패턴 그 자체
- [[harness]]: program.md = 초경량 하네스. 4층 레이어(지식·도구·통제·패키지) 모두 최소화한 사례
- [[context-engineering]]: 로그 발췌 패턴 (`> run.log 2>&1` + `grep`)
- [[token-economy]]: 실험 간 컨텍스트 윈도우 보호 운영
- [[ml-ai]]: nanochat 단순화판으로 LLM 학습 코드 자체도 ML 학습 자료 가치

## 부모 저장소: [[nanochat]]

`train.py`는 [[nanochat]]의 단일-GPU 단순화판. nanochat이 풀 파이프라인(토큰화·사전학습·SFT·RL·평가·추론·웹 UI)이라면 autoresearch는 거기서 분산 학습/멀티 GPU/장치 추상화·SFT·RL·UI 등을 모두 걷어내고 **사전학습 + val_bpb 측정**만 남긴 베어본.

### 자기 강화 순환: autoresearch가 nanochat 리더보드를 갱신함

[[nanochat]] README의 Time-to-GPT-2 리더보드:

| # | 시간 | 설명 | 날짜 |
|---|-----|------|------|
| 4 | 2.02h | NVIDIA ClimbMix 데이터셋 (사람 손) | 2026-03-04 |
| **5** | **1.80h** | **autoresearch round 1** | **2026-03-09** |
| **6** | **1.65h** | **autoresearch round 2** | **2026-03-14** |

autoresearch가 발견한 개선이 nanochat master로 머지되는 구조 — **자율 루프 → 부모 저장소 갱신 → 다음 라운드 베이스라인**. 이게 [[autonomous-research-loop]] 패턴이 사변적이지 않다는 가장 강한 근거.

## 노출된 포크 (2026-04 기준)

- [miolini/autoresearch-macos](https://github.com/miolini/autoresearch-macos) — macOS
- [trevin-creator/autoresearch-mlx](https://github.com/trevin-creator/autoresearch-mlx) — Apple MLX
- [jsegov/autoresearch-win-rtx](https://github.com/jsegov/autoresearch-win-rtx) — Windows + RTX
- [andyluo7/autoresearch](https://github.com/andyluo7/autoresearch) — AMD

석근의 환경(회사 맥북, 집 윈도우)에 직접 매핑되는 포크가 양쪽에 있음.

## 출처

- [[karpathy-autoresearch]] — README + program.md 통합 요약

## 논쟁/모순

> [!warning] 논쟁/모순
> (현재 단일 소스 — 모순 없음)


## 메모

- 위키에 들여올 가치가 큰 디테일은 **"단일 메트릭 + 시간 예산 + 단일 파일 수정 + 무한 루프"** 4중 제약. 이 네 가지가 동시에 걸려야 자율 실험이 폭주하지 않고 수렴함.
- 석근 응용:
  - **BI 분석 자율 튜닝**: 메트릭=쿼리 latency or 대시보드 freshness, 5분 예산, train.py↔SQL/Python ETL 단일 파일.
  - **개인 비서 AI**: 메트릭=응답 만족도 점수(LLM-as-judge), 5분 예산, train.py↔prompt/skill 파일.
  - **위키 자체**: 메트릭 정의가 어려워 직접 적용은 어려움. 메트릭 후보 — "엔티티/개념 신규 생성률" or "고아 페이지 감소율".
- 후속 탐구: macOS / MLX 포크 중 하나를 실제 가동하여 1박 100실험 재현해볼 가치. 회사 맥북에서 야간 자가 실험으로 구현 가능.
