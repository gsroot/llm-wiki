---
title: "하네스 (Harness)"
type: concept
category: ai
tags: [하네스, harness, claude-code, 에이전트, agent, 작업운영, ops]
related: [[claude-code]], [[context-engineering]], [[token-economy]], [[llm-wiki-pattern]]
source_count: 1
created: 2026-04-15
updated: 2026-04-15
---

# 하네스 (Harness)

## 정의

AI 에이전트가 일하는 **작업장 전체 구조**. 프롬프트 한 줄이 아니라, 에이전트가 무엇을 읽고 어떤 도구를 쓰고 어디서 멈춰야 하는지를 묶어 놓은 운영 환경이다.

> 비유: "동료에게 일을 맡길 때 책상 위에 참고 자료를 놓고, 출입 가능한 서랍을 정하고, 끝나기 전에 체크할 항목을 붙여 두는 것."

## 왜 중요한가

**모델 이름보다 작업 구조·하네스·검증 습관에서 차이가 벌어진다.** 같은 Claude를 쓰더라도 하네스가 있는 팀과 없는 팀의 산출물 품질은 크게 달라진다.

AI 성능 경쟁이 "어느 모델이 더 똑똑한가"에서 "어느 도구가 실제 일을 덜 끊기게 하는가"로 이동했고, 이 질문의 답이 하네스 설계다.

## 핵심 구성 요소

| 요소 | 역할 |
|------|------|
| **권한 모드 (Permission Modes)** | 무엇을 자동 허용, 질문, 차단할지 |
| **자동 개입 규칙 (Hooks)** | 세션 중간에 자동으로 끼어드는 검사·후처리 |
| **폴더 구조 (File Organization)** | 어떤 파일이 어디에 놓이고 언제 읽히는가 |
| **테스트와 검증 (Testing & Verification)** | 출력이 의도대로인지 확인하는 루프 |
| **저장 위치 지정 (Save Locations)** | 결과물·로그·handoff가 어디에 남는가 |

## 4층 레이어로 본 하네스

[[claude-code-master-guide]]의 분류:

1. **지식 레이어**: CLAUDE.md, 규칙 파일, 메모리, 예시, 스킬 지침
2. **도구 레이어**: Bash, Read/Edit/Write, MCP, Connector, 브라우저 제어, 예약 실행
3. **패키지 레이어**: Skills, Plugins
4. **통제 레이어**: Permissions, Hooks, 승인 단계, Plan Mode, Worktree, 테스트, 검토 에이전트

## 하네스 엔지니어링 vs 프롬프트/컨텍스트 엔지니어링

| 엔지니어링 종류 | 조작 대상 |
|----------------|----------|
| 프롬프트 엔지니어링 | 한 번의 입력 문장 |
| [[context-engineering]] | 컨텍스트 윈도우에 들어가는 자료 구성 |
| **하네스 엔지니어링** | 에이전트가 일하는 작업장 전체 (컨텍스트·도구·권한·검증·저장) |

가이드북 5장의 핵심 주장: **프롬프트 → 컨텍스트 → 하네스** 순으로 추상화 수준이 올라가고, 하네스 수준의 설계가 장기적 효용을 만든다.

## 실전 적용

### 최소 하네스 (개인 사용자용)
```
project/
├── CLAUDE.md          # 프로젝트 계약서 (짧게)
├── about-me.md        # 배경 맥락
├── working-rules.md   # 작업 규칙
├── plan.md            # 현재 작업 상태
├── handoff.md         # 다음 세션용 인수인계
└── templates/*.md     # 출력 형식
```

### 팀 하네스 추가 요소
- `decision-log.md`, `approval-log.md`, `review-findings.md` — 사후 흔적
- `.claude/settings.json`의 managed scope — 관리자 강제 설정
- Hooks로 포맷팅·린트·승인 자동 삽입
- Worktree로 역할별 병렬 세션 분리

### 하네스 품질 체크리스트
- CLAUDE.md가 짧고 강한 운영 계약서인가
- plan / implement / review가 분리되어 있는가
- 긴 세션에 compaction·session memory·handoff 파일이 함께 있는가
- 고위험 작업에 approval gate가 앞단에 있는가
- 세션이 끊겨도 바깥 파일로 상태 복원이 가능한가

## 관련 개념

- [[context-engineering]]: 하네스의 지식 레이어를 설계하는 방법
- [[token-economy]]: 하네스가 컨텍스트를 낭비 없이 쓰도록 만드는 원리
- [[claude-code]]: 하네스 개념을 제일 선명하게 구현한 제품
- [[llm-wiki-pattern]]: 이 위키 자체가 개인 지식 관리용 하네스

## 출처

- [[claude-code-master-guide]] — CHOI의 가이드북에서 가장 중심적인 개념. 5장 "시스템 설계: 문맥, 하네스, 검증"

## 열린 질문

- BI 업무에서 쿼리 에이전트용 최소 하네스는 어떤 모양인가? (SQL 스키마·샘플 쿼리·검증 SELECT·승인 규칙)
- Cowork와 Claude Code 사이 하네스를 공유할 때의 경계는? (CLAUDE.md는 공유, 권한은 분리?)
