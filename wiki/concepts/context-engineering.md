---
title: "컨텍스트 엔지니어링 (Context Engineering)"
type: concept
category: ai
tags: [컨텍스트엔지니어링, context-engineering, 프롬프트엔지니어링, prompt-engineering, LLM, 자율연구]
related: [[harness]], [[token-economy]], [[claude-code]], [[llm-wiki-pattern]], [[autonomous-research-loop]]
source_count: 2
created: 2026-04-15
updated: 2026-04-27
---

# 컨텍스트 엔지니어링 (Context Engineering)

## 정의

LLM에게 **무엇을·언제·어떤 순서로 읽힐지**를 설계하는 기술. 프롬프트(한 번의 입력 문장)보다 한 층 위, 하네스(작업장 전체)보다 한 층 아래에 위치한다.

## 왜 중요한가

프롬프트 엔지니어링이 "어떻게 물을까"였다면, 컨텍스트 엔지니어링은 "무엇을 읽게 할까"다. 모델이 커지고 컨텍스트 윈도우가 넓어질수록 질문의 무게 중심이 이쪽으로 이동한다.

> "중요한 질문도 '어느 모델이 더 똑똑한가'보다 '어느 도구가 실제 일을 덜 끊기게 하는가'로 이동했다." — [[claude-code-master-guide]]

## 세 가지 엔지니어링 층

| 층 | 조작 대상 | 예시 |
|----|----------|------|
| **프롬프트 엔지니어링** | 한 번의 입력 문장 | "step by step으로 설명해줘", 역할 부여 |
| **컨텍스트 엔지니어링** | 컨텍스트 윈도우에 들어가는 자료 조합 | CLAUDE.md 구성, 참고 파일 선택, 순서, 양 |
| **[[harness]] 엔지니어링** | 작업장 전체 (컨텍스트 + 도구 + 권한 + 검증 + 저장) | Hooks, Worktree, approval gate |

## 핵심 내용

### 재사용 컨텍스트 (Memoized Context)

매 턴마다 처음부터 다시 설명하지 않도록 붙들어 두는 배경 컨텍스트.

- CLAUDE.md: 세션 시작 시 자동 로드되는 운영 계약서
- Projects의 배경 자료: 누적되는 프로젝트 컨텍스트
- Memory: 자동 축적되는 세션 간 기억

### 컨텍스트 조립 원칙

1. **짧고 강하게**: CLAUDE.md는 길수록 좋다는 말은 틀렸다. 항상 읽히는 문서라서 **짧고 강한 운영 계약서**일수록 낫다.
2. **역할 분리**: about-me.md(배경), working-rules.md(규칙), brand-voice.md(톤), glossary.md(용어)처럼 파일을 역할별로 쪼개면 재사용·수정·검토가 쉬워진다.
3. **출력 계약 (Output Contract)**: 결과가 어떤 형식과 위치로 나와야 하는지 미리 정한 약속. "잘 써달라"보다 강하다.
4. **필요 범위만**: [[token-economy]] 원칙 — 전체 파일 대신 필요한 조각만

### 파일 vs 프롬프트

파일 기반 컨텍스트가 강한 5가지 이유:
1. **기억을 바깥으로**: 세션이 바뀌어도 파일은 남는다
2. **사람·AI 공유**: Git 관리 가능, 다른 세션·모델도 읽을 수 있다
3. **반복 가능**: 매번 0부터 설명할 필요 없음
4. **검토·수정 쉬움**: 긴 채팅보다 파일 한 줄 수정이 강력
5. **운영 기본 단위**: 대화보다 파일이 오래 남는다

## 실전 적용

### CLAUDE.md 설계 원칙

- 한 페이지 이내 (스크롤 없이 읽힐 것)
- 반드시 지켜야 할 규칙만 (세세한 팁은 별도 파일로)
- 금지 사항과 허용 사항을 명시적으로
- 새 세션이 5초 안에 "이 프로젝트가 무엇인지·어떻게 작업해야 하는지"를 잡을 수 있어야 함

### 컨텍스트 조립 예: 주간 브리프
```
context/
├── about-me.md          (1회 로드)
├── investor-tone.md     (1회 로드)
projects/market-scan/
├── brief.md             (작업 요청)
└── sources.md           (참조 자료, 링크 포함)
templates/
└── weekly-founder-brief.md  (출력 계약)
```

### 컨텍스트 오염 방지

- 여러 작업을 한 세션에서 섞지 않기 (plan / implement / review 분리)
- 긴 세션에서 `/compact`로 압축
- Worktree로 병렬 작업을 물리적으로 분리

### 자율 루프 컨텍스트 보호 3원칙 ([[autoresearch]] 사례)

자율 실험 루프가 12회/시간으로 돌면 학습 로그가 즉시 컨텍스트를 폭파시킨다. autoresearch의 `program.md`가 보여준 회피책:

1. **stdout 격리**: `uv run train.py > run.log 2>&1` — `tee` 금지. 출력은 파일로만.
2. **메트릭 1줄 발췌**: `grep "^val_bpb:" run.log` — 결과 1줄만 본문에 노출.
3. **크래시 시에만 tail**: 정상 시 로그 자체를 안 봄. 비정상 시에도 `tail -n 50` 한도.

이 3줄 패턴은 위키 운영에도 그대로 이식 가능하다 — 큰 PDF 변환물이나 외부 데이터를 직접 컨텍스트에 끌어들이지 말고, `grep`/`head`/`tail` 발췌 1~2줄만.

## 관련 개념

- [[harness]]: 컨텍스트 엔지니어링을 지속적으로 작동시키는 상위 구조
- [[token-economy]]: 컨텍스트 분량·조합의 품질 지표
- [[llm-wiki-pattern]]: 이 위키 자체가 컨텍스트 엔지니어링의 개인용 적용
- [[mcp]]: 컨텍스트를 동적으로 조립해주는 외부 도구 프로토콜

## 출처

- [[claude-code-master-guide]] — CHOI의 가이드북 5장 "프롬프트 엔지니어링, 컨텍스트 엔지니어링, 하네스 엔지니어링"
- [[karpathy-autoresearch]] — 자율 실험 루프 운영의 컨텍스트 보호 패턴(`> run.log 2>&1` + `grep` 1줄 발췌)

## 열린 질문

- 회사 BI 프로젝트용 CLAUDE.md에는 무엇을 담아야 한가? (팀 지표 정의 링크? 데이터웨어하우스 ERD? 파이프라인 명명 규칙?)
- 이 위키의 `templates/` 디렉토리에 `handoff.md`, `working-rules.md` 템플릿을 추가할 필요가 있는가?
