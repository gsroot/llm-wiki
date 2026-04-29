---
title: "BDFL (Benevolent Dictator For Life)"
type: concept
category: dev-tools
tags: [bdfl, governance, open-source, decision-making, pandas, python]
related:
  - "[[pandas-dev]]"
  - "[[pandas]]"
  - "[[pdep]]"
  - "[[numfocus]]"
  - "[[github]]"
  - "[[pandas-dev-pandas]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# BDFL (Benevolent Dictator For Life)

## 정의

**BDFL(Benevolent Dictator For Life)**은 오픈소스 프로젝트에서 창시자나 핵심 리더가 최종 의사결정권을 갖는 거버넌스 모델이다. "자비로운 독재자"라는 표현처럼, 일상 결정은 커뮤니티와 메인테이너에게 맡기되 교착 상태나 큰 방향성 충돌에서 최종 결정을 내리는 역할이다.

## 왜 중요한가

오픈소스 프로젝트는 완전한 합의제로 운영되기 어렵다. 특히 API 안정성, 대규모 breaking change, 로드맵 우선순위처럼 모두가 영향을 받는 결정에는 최종 조정자가 필요할 수 있다. BDFL 모델은 빠른 결정과 일관성을 주지만, 프로젝트가 커질수록 개인 의존성과 권력 집중이 문제가 된다.

## 핵심 내용

### pandas 사례

[[pandas-dev-pandas]]에서 수집한 pandas 거버넌스는 BDFL + Core Team + NumFOCUS Subcommittee 3축으로 정리된다.

| 축 | 역할 |
|---|---|
| BDFL | Wes McKinney. 최종 결정권자이나 거의 행사하지 않음 |
| Core Team | 일상 기술 의사결정과 유지보수 |
| NumFOCUS Subcommittee | 자금 관리. 기술 방향에는 관여하지 않음 |

pandas의 중요한 변화는 BDFL 개인 판단에만 의존하지 않고 [[pdep]] 시스템으로 결정 절차를 문서화했다는 점이다. 즉, BDFL은 사라진 것이 아니라 **공개 절차와 병행되는 최후 조정자**에 가깝다.

### 장단점

| 장점 | 단점 |
|---|---|
| 결정 교착 해소 | 개인 의존성 |
| 제품 철학 일관성 | 후계 구조 불명확 |
| 초기 성장 속도 | 커뮤니티 신뢰가 깨지면 취약 |
| 책임 소재 명확 | 규모가 커질수록 단독 판단 부담 증가 |

## 실전 적용

llm-wiki는 사실상 석근이 BDFL이고, LLM 에이전트가 Core Team 역할을 일부 수행하는 구조다. 이 관점은 운영 규칙을 명확히 만든다.

- 최종 판단: 석근
- 운영 실행: Claude Code / Codex / Cowork
- 결정 기록: `CLAUDE.md`, `wiki/logs/log.md`, 필요 시 synthesis/decision 문서
- 원천 불변성: `raw/`는 수정 금지

## 관련 개념

- [[pdep]]: BDFL 판단을 공개 절차와 결합하는 문서 시스템.
- [[numfocus]]: 자금·법무 운영 층. 기술 결정권과 분리된다.
- [[pandas-dev]]: BDFL + Core Team + NumFOCUS 분리 사례.

## 출처

- [[pandas-dev-pandas]] — pandas의 BDFL + Core Team + NumFOCUS Subcommittee 거버넌스 정리.

## 열린 질문

- 개인 위키의 BDFL 모델은 어디까지 명시해야 하는가?
- LLM 에이전트가 Core Team처럼 제안·검토·실행을 맡는다면, 어떤 변경은 반드시 사용자 승인 후 진행해야 하는가?
