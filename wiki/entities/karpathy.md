---
title: "Andrej Karpathy"
type: entity
entity_type: person
tags: [karpathy, AI, LLM, openai, tesla, 교육콘텐츠, nanogpt, nanochat, autoresearch, mingpt, zero-to-hero]
related:
  - "[[autoresearch]]"
  - "[[autonomous-research-loop]]"
  - "[[nanogpt]]"
  - "[[nanochat]]"
source_count: 3
observed_source_refs: 15
inbound_count: 32
created: 2026-04-27
updated: 2026-04-27
cited_by_count: 17
---

# Andrej Karpathy

## 개요

AI 연구자·교육자. 슬로바키아계 캐나다인으로 OpenAI 창립 멤버 → Tesla AI 디렉터 → OpenAI 복귀 후 독립. 현재(2026년 기준)는 개인 연구·교육 콘텐츠 제작과 오픈소스 프로젝트로 활동.

이 위키 맥락에서 중요한 이유: **자율 AI 에이전트가 코드 대신 "지침서(`program.md`)"를 다뤄 LLM 학습을 자율 반복하게 만드는** [[autoresearch]] 패턴을 시연한 인물. 위키의 [[harness]]·[[context-engineering]] 개념과 직접 연결된다.

## 주요 특징

- **교육 자산 계보**: minGPT(교육 우선) → [[nanogpt]] (이빨 우선, ~300줄 train.py + ~300줄 model.py로 GPT-2 재현, 2025-11 deprecated) → [[nanochat]] ($100 GPT-2 풀 파이프라인, 활성) → [[autoresearch]] (단일-GPU 자율 실험). 각 단계마다 **"단일 파일 + 최소 의존성 + 해킹 가능"** 원칙이 누적 진화.
- **개별 교육 콘텐츠**: micrograd, llm.c, [Zero to Hero](https://karpathy.ai/zero-to-hero.html) 강의 시리즈, [GPT 비디오](https://www.youtube.com/watch?v=kCc8FmEb1nY)로 LLM 내부 구조의 표준 학습 경로를 만든 인물.
- **단순화 미학**: "복잡한 시스템을 단일 파일·최소 의존성으로 환원"하는 일관된 스타일. nanochat의 `--depth` 단일 다이얼이 정수 — 사용자에게 N×M 결정점을 떠넘기는 "프레임워크"가 아닌 **"강한 baseline"** 코드베이스를 추구.
- **2026년 화법**: autoresearch README의 "10,205세대 자기수정 바이너리" 풍자처럼, AI 연구의 자동화·자율화 미래를 도발적으로 가시화하는 글쓰기 스타일.
- **AI Policy 명문화**: nanochat README — "PR에서 LLM이 substantial 기여한 부분과 본인이 이해 못 한 부분을 disclosure". LLM 시대 오픈소스 협업 정책의 표준 사례.

## 관련 개념

- [[autonomous-research-loop]]: Karpathy가 autoresearch로 시연한 패턴
- [[harness]]: program.md를 "lightweight skill"로 호명 — 하네스 개념의 극단적 사례
- [[context-engineering]]: `> run.log 2>&1` + `grep` 한 줄 발췌 같은 컨텍스트 절약 디테일이 그의 코드 곳곳에 묻어남

## 출처

- [[karpathy-autoresearch]] — 2026-03 공개한 autoresearch 저장소 README & program.md
- [[karpathy-nanogpt]] — 2022-12 공개, 2025-11 deprecated. 단순화 미학의 출발점.
- [[karpathy-nanochat]] — 2025-10 공개. $100 GPT-2 풀 파이프라인. AI policy / 단일 다이얼 / 리더보드 모두 명문화.

## 메모

- nanoGPT/nanochat 별도 엔티티로 분리 완료 (2026-04-27 수집). karpathy 본인 페이지에서는 계보와 미학 연결만 담당.
- 교육 자료 중 micrograd, llm.c, Zero to Hero는 별도 소스로 수집할 가치 있음. 특히 [[ml-ai]] 개념 페이지 보강에 직접적.
- **autoresearch가 nanochat 리더보드를 실제 갱신**(round 1, 2)했다는 사실은 Karpathy의 두 작업이 단순한 시리즈가 아니라 **자기 강화 순환**임을 시사. 후일 별도 종합 분석 페이지(`wiki/syntheses/`)에 정리할 가치 있음.
