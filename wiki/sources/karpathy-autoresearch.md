---
title: "karpathy/autoresearch — 자율 LLM 실험 루프"
type: source
source_type: article
source_url: "https://github.com/karpathy/autoresearch"
raw_path: "raw/articles/karpathy-autoresearch/"
author: "Andrej Karpathy"
date_published: 2026-03-06
date_ingested: 2026-04-27
tags: [autoresearch, karpathy, LLM, 자율연구, agent, harness, nanochat, val-bpb, 실험루프, 에이전트]
related:
  - "[[karpathy]]"
  - "[[autoresearch]]"
  - "[[autonomous-research-loop]]"
  - "[[harness]]"
  - "[[context-engineering]]"
  - "[[claude-code]]"
confidence: high
cited_by:
  - "[[agent-stack-evolution]]"
  - "[[anthropics-claude-cookbooks]]"
  - "[[astral-sh-uv]]"
  - "[[autonomous-research-loop]]"
  - "[[autoresearch]]"
  - "[[claude-code]]"
  - "[[context-engineering]]"
  - "[[harness]]"
  - "[[karpathy]]"
  - "[[slash-commands-vs-agent-skills]]"
  - "[[uv]]"
---

# karpathy/autoresearch — 자율 LLM 실험 루프

## 한줄 요약

> 사람이 코드를 직접 안 만지고 **`program.md`(에이전트 지침서)만 다듬어서** 단일 GPU 위에서 5분 시간 예산의 LLM 학습 실험을 밤새 자율 반복하게 만드는, "AI 연구 조직의 코드"를 시제품화한 실험.

## 핵심 내용

### 구성 (저장소 4개 파일이 전부)

| 파일 | 역할 | 누가 수정하나 |
|------|------|--------------|
| `prepare.py` | 상수, 데이터/토크나이저 준비, 평가 함수 | **수정 금지** (실험 비교 가능성을 위한 고정 평가축) |
| `train.py` | GPT 모델, Muon+AdamW 옵티마이저, 학습 루프 — 전체가 한 파일 | **에이전트가** 매 실험마다 수정 |
| `program.md` | 에이전트 지시서 (셋업·실험·로깅 워크플로우) | **사람이** 시간을 들여 다듬는다 |
| `pyproject.toml` | 의존성 (새 패키지 추가 금지) | 고정 |

### 실험 루프 (program.md 본문)

`autoresearch/<tag>` 브랜치를 따로 만들고 무한 루프:

1. 현재 git 상태 확인
2. `train.py`를 실험 아이디어로 직접 수정
3. `git commit`
4. `uv run train.py > run.log 2>&1` (출력은 절대 stdout/tee로 흘리지 않음 — 컨텍스트 보호)
5. `grep "^val_bpb:\|^peak_vram_mb:" run.log`로 결과만 발췌
6. grep이 비면 크래시 — `tail -n 50 run.log`로 스택 확인 후 자체 수정 시도
7. `results.tsv`에 행 추가 (탭 구분, **commit 안 함** — 깃 미추적)
8. val_bpb 개선 시 → 브랜치 advance (커밋 유지)
9. 동일/악화 시 → `git reset`으로 출발점 복귀
10. **NEVER STOP** — 사람이 수동으로 멈출 때까지 무한 반복

### 핵심 설계 결정 5가지

1. **고정된 5분 시간 예산**: 컴퓨팅 플랫폼이 달라져도 시간이 같으니 실험들끼리 직접 비교 가능. 시간당 ~12회, 평균 수면 시간 동안 ~100회 실험.
2. **단일 메트릭 `val_bpb`** (validation bits per byte): vocab-size 독립이라 아키텍처 변경에도 공정. 낮을수록 좋음.
3. **단일 파일 수정**: `train.py`만 수정 — diff 리뷰 가능성 보존.
4. **외부 의존성 최소화**: PyTorch + 소수 패키지. 분산 학습/복잡한 config 없음.
5. **Simplicity 기준**: "동등하면 단순한 게 낫다." 0.001 val_bpb 개선을 위해 20줄 hack 추가? 보통 버림. 코드 삭제로 동등 결과? 무조건 채택.

### `program.md`의 작동 원리

> "The `program.md` file is essentially a super lightweight 'skill'."

- 에이전트(Claude/Codex 등)에게 `program.md` 읽으라고 지시하고 권한을 모두 풀어두면 알아서 셋업·실험·로깅·반복.
- 기본 `program.md`는 **의도적으로 베어본**으로 두고, 사람은 시간이 지나면서 이 파일을 다듬어가며 "가장 빠르게 연구를 진전시키는 research-org code"를 발견해 나간다.
- 즉 **실험 대상이 모델만이 아니라 program.md 자체**.

## 주요 인사이트

### 1. 이 프로젝트의 진짜 발명품은 `program.md`다

`train.py`는 [nanochat](https://github.com/karpathy/nanochat)의 단일-GPU 단순화판. 새로운 게 아니다. **새로운 건 "사람은 이제 파이썬이 아니라 자연어 지침서를 프로그래밍한다"는 운영 모델**이다.

이건 [[harness]] 개념의 극단적 사례다:
- 지식 레이어 = `program.md` 한 장
- 도구 레이어 = `bash`, `python`, `git`만
- 통제 레이어 = "5분 시간 예산 + val_bpb 단일 메트릭 + simplicity 기준"
- 패키지 레이어 = 없음

가벼운데도 작동한다는 점이 핵심. **하네스가 작을수록 에이전트의 자유도가 커지고, 그 자유도를 견디는 건 평가 메트릭의 객관성이다.**

### 2. "코드"라는 말의 의미가 변한다

> "The agents claim that we are now in the 10,205th generation of the code base, in any case no one could tell if that's right or wrong as the 'code' is now a self-modifying binary that has grown beyond human comprehension."
> — @karpathy, March 2026

README의 풍자적 도입부지만, 진심도 섞여 있다. autoresearch는 **"사람이 자연어로 만든 program.md를 진짜 코드, 파이썬은 부산물"** 로 보는 시각의 작은 시연.

### 3. 컨텍스트 보호의 디테일

- `uv run train.py > run.log 2>&1` — `tee` 금지. 학습 로그가 에이전트 컨텍스트 윈도우를 침범하면 즉시 토큰 낭비.
- `grep "^val_bpb:" run.log` — 결과 1줄만 본문으로 끌어들임.
- 크래시 시에만 `tail -n 50` — 절대 전체 로그를 읽지 않음.

이 3줄 패턴이 곧 [[token-economy]]의 정수. 위키의 `index.md` 우선 읽기 → 관련 페이지만 Read와 동일한 사상.

### 4. results.tsv를 commit 안 함

각 실험은 **모델 코드만** commit. 결과 기록 `results.tsv`는 untracked. 이렇게 하면 `git reset`이 상태를 깨끗이 복구해도 누적 실험 기록은 남는다. 단순한 트릭이지만 자율 루프의 안정성에 직결.

### 5. NEVER STOP 원칙 — 자율성의 끝까지 가본 사례

> "The human might be asleep, or gone from a computer and expects you to continue working **indefinitely** until you are manually stopped."

기존 Claude Code/Cowork도 자율 작업을 강조하지만, autoresearch는 "끝나는 조건"을 의도적으로 제거. **연구 진척이 시간 단조 함수가 아니라는 점을 받아들이고, 시간만 늘리면 어떤 결과가 나오는지 보는 실험.**

## 관련 엔티티/개념

- [[karpathy]]: 저자 — OpenAI 공동 창립자, Tesla AI 디렉터 출신, 교육 콘텐츠 제작자
- [[autoresearch]]: 이 저장소 자체 (project entity)
- [[autonomous-research-loop]]: 이 소스로 정의된 새 개념 페이지
- [[harness]]: program.md = 초경량 하네스. 이 위키의 4층 레이어 분류로 매핑됨
- [[context-engineering]]: 로그 발췌 패턴이 컨텍스트 엔지니어링의 모범
- [[token-economy]]: `> run.log 2>&1` + `grep` = 토큰 절약 운영 원칙
- [[claude-code]]: 실행 에이전트 후보 중 하나로 명시됨 ("spin up your Claude/Codex…")
- [[slash-commands-vs-agent-skills]]: program.md를 Karpathy가 "lightweight skill"로 호명한 점에서 직접 연결

## 인용할 만한 구절

> "The default `program.md` in this repo is intentionally kept as a bare bones baseline, though it's obvious how one would iterate on it over time to find the 'research org code' that achieves the fastest research progress."
> — README

> "If each experiment takes you ~5 minutes then you can run approx 12/hour, for a total of about 100 over the duration of the average human sleep. The user then wakes up to experimental results, all completed by you while they slept!"
> — program.md

> "Conversely, removing something and getting equal or better results is a great outcome — that's a simplification win."
> — program.md (Simplicity criterion)

## 메모

- 라이선스 MIT — 패턴을 그대로 차용해도 무방.
- 76,912 stars (수집 시점) — Karpathy 영향력으로 보정 필요하지만 이 패턴이 빠르게 표준이 될 신호로 읽힘.
- 노출된 포크: macos / mlx / win-rtx / amd 4종. **프로젝트 차원의 실험 인프라가 곧 GPU 종류만큼 분기됨**.
- 석근의 응용 가능성:
  - **BI 분석 자동화**: `train.py` ↔ `analytics_query.py`, `val_bpb` ↔ `query latency` or `dashboard freshness`. 5분 예산으로 쿼리 최적화 자율 실험.
  - **개인 비서 AI 서비스**: program.md 패턴을 그대로 차용. 단일 메트릭(예: 응답 만족도 점수)을 정하고 prompt/skill을 자율 튜닝하게 만드는 구조 가능.
  - 이 위키 자체에 적용: `program.md` ↔ `CLAUDE.md`, `train.py` ↔ `wiki/`. 단 LLM 위키는 "메트릭이 없는" 영역이라 자율 루프 적용 전에 평가축을 먼저 정의해야 함.
- 후속 탐구:
  1. nanochat 본 저장소를 raw에 넣을지 결정 (autoresearch가 단순화판이므로 본판은 다른 맥락에서 가치 있을 가능성).
  2. 4개 포크(macos/mlx/win-rtx/amd) 중 macOS·MLX 포크는 석근의 집 환경/맥북에서 실제 시도 가능 — 후일 별도 source로 수집 검토.
  3. "메트릭 + 시간예산 + program.md" 3종을 BI나 개인 프로젝트에 어떻게 이식할지 설계 노트 작성.
