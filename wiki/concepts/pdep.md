---
title: "PDEP (Pandas Enhancement Proposal)"
type: concept
category: dev-tools
tags: [pdep, pandas, governance, decision-record, proposal, open-source, roadmap]
related:
  - "[[pandas]]"
  - "[[pandas-dev]]"
  - "[[copy-on-write]]"
  - "[[bdfl]]"
  - "[[spec-driven-development]]"
  - "[[github-spec-kit]]"
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# PDEP (Pandas Enhancement Proposal)

## 정의

**PDEP(Pandas Enhancement Proposal)**는 [[pandas]] 프로젝트의 중요한 변경을 제안·토론·투표·기록하는 공식 의사결정 문서 시스템이다. Python의 PEP와 비슷하지만, pandas 프로젝트 범위에 맞춘 거버넌스 산출물이다.

## 왜 중요한가

PDEP는 오픈소스 프로젝트가 커졌을 때 "누가 결정하는가"와 "왜 그렇게 결정했는가"를 기록으로 남긴다. 단순 이슈나 PR보다 무겁고, 사소한 버그 수정이나 파라미터 추가는 PDEP 대상이 아니다. 커뮤니티 전체가 알아야 하는 비즉시적·비자명한 변화가 PDEP 대상이다.

## 핵심 내용

### pandas의 PDEP 워크플로우

1. Draft 작성
2. Under discussion 60일
3. Vote 15일
4. Accepted / Rejected / Withdrawn 결정

투표는 quorum과 supermajority를 요구한다. 위키에 수집된 [[pandas-dev-pandas]] 기준으로 quorum은 11명 또는 voting 구성원 50% 중 작은 값, majority는 non-abstaining 표의 70% 찬성이다.

### 대표 사례

| PDEP | 주제 | 의미 |
|---|---|---|
| PDEP-1 | Purpose and guidelines | PDEP 자체의 운영 규칙 |
| PDEP-7 | Copy-on-Write | pandas 2.0~3.0 메모리 모델 전환 |
| PDEP-10 | Required pyarrow dependency | pandas의 미래 데이터 모델 논의 |
| PDEP-17 | Backwards compatibility and deprecation policy | 안정성·호환성 정책 |

### 다른 문서 체계와의 비교

- [[spec-driven-development]]: 구현 전 "무엇을 만들지"를 사양으로 고정한다.
- [[github-spec-kit]]: Constitution/Spec/Plan/Tasks를 도구화한다.
- PDEP: 프로젝트 차원의 비가역적·광범위한 의사결정을 공개 기록으로 남긴다.

## 실전 적용

LLM 위키 운영에도 PDEP식 패턴을 차용할 수 있다. 예를 들어 `CLAUDE.md`의 필수 필드를 바꾸거나, `source` 페이지 스키마를 바꾸거나, `raw_path`를 모든 source에 강제하는 결정은 단순 수정이 아니라 "운영 규칙 변경"이다. 이런 결정은 `wiki/syntheses/` 또는 별도 `wiki/decisions/`에 남기는 방식이 맞다.

## 관련 개념

- [[pandas-dev]]: PDEP를 운영하는 GitHub 조직.
- [[copy-on-write]]: PDEP-7의 대표 구현 결과.
- [[bdfl]]: pandas가 BDFL 중심에서 Core Team + PDEP 기반 거버넌스로 확장된 맥락.
- [[spec-driven-development]]: 사양·결정·구현을 분리한다는 점에서 같은 가족.

## 출처

- [[pandas-dev-pandas]] — PDEP-1, 거버넌스 규칙, Copy-on-Write PDEP-7 수집 내용.

## 열린 질문

- llm-wiki 자체도 `LDEP` 같은 결정 기록 체계를 둘 필요가 있는가?
- 개인 위키에서는 어느 정도 변경부터 PDEP식 기록이 필요한가?
