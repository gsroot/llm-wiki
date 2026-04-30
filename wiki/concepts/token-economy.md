---
title: "토큰 경제학 (Token Economy)"
type: concept
category: ai
tags: [토큰경제학, token-economy, LLM, 비용, 컨텍스트, context, prompt-caching, claude-cookbooks, claude-agent-SDK]
related:
  - "[[harness]]"
  - "[[context-engineering]]"
  - "[[claude-code]]"
  - "[[claude-agent-sdk]]"
  - "[[anthropic]]"
  - "[[agent-patterns]]"
source_count: 2
observed_source_refs: 24
inbound_count: 52
created: 2026-04-15
updated: 2026-04-27
cited_by_count: 19
---

# 토큰 경제학 (Token Economy)

## 정의

LLM 운영에서 **토큰이 두 가지 의미를 동시에 갖는다**는 관점. 단순 비용 관리가 아니라, 컨텍스트 설계 철학이다.

1. **비용 계산 단위**: input token(읽는 것) + output token(생성하는 것)
2. **작업 범위 신호**: 좁고 집중된 작업(낮은 토큰) vs 넓고 산만한 작업(높은 토큰)

## 왜 중요한가

토큰 경제학의 핵심 전환은 **"인색하게 굴자"가 아니라 "꼭 필요한 컨텍스트만 읽도록 설계하자"**이다.

저장소 전체를 읽고 긴 대화로 계속 수정하는 것보다, **함수 하나와 에러 로그 20줄만 읽어서 빠르게 해결하는 것**이 훨씬 효율적이다. 토큰 많이 쓰는 것 = 작업 범위가 산만하다는 신호일 수 있다.

## 핵심 내용

### 토큰 = 작업 범위 진단 도구

토큰 사용량이 커지는 패턴:
- 파일 전체를 읽힐 때 (일부만 필요한데도)
- 같은 컨텍스트를 매 턴 다시 보낼 때 ([[prompt-cache]] 미활용)
- 대화가 길어지면서 과거 결과를 계속 들고 다닐 때
- 에이전트가 "혹시 필요할까" 식으로 여러 파일을 탐색할 때

이럴 때 토큰 절약 기법 이전에 **작업 범위 자체를 좁히는 게 먼저**다.

### Prompt Cache와의 관계

Anthropic의 prompt cache는 **같은 컨텍스트를 오래 유지할수록 재사용 이득이 커지는 구조**다. 하네스에 부모 컨텍스트와 도구 구성이 안정적으로 고정되어 있으면 병렬 세션도 cache를 공유하여 "거의 공짜"처럼 느껴진다.

커뮤니티에서 "병렬 세션은 공짜다"라는 바이럴 문장은 실제로는 "부모 컨텍스트와 도구 구성이 안정적일 때 prompt cache를 더 잘 공유한다"는 뜻에 가깝다.

### 긴 세션 관리 기법

긴 세션이 모든 것을 기억하지는 않는다. 실제로는 다음 장치가 함께 있어야 긴 작업이 산다:
- **Compaction** (`/compact`): 중간에 대화 요약 압축
- **Session Memory**: 핵심 상태를 다음 맥락까지 이어줌
- **Handoff 파일**: 세션 바깥 상태 기록

## 실전 적용

### 토큰 병목 (Token Hotspot) 지점 진단

컨텍스트가 갑자기 무거워져 비용과 품질이 흔들리기 쉬운 구간:
- 대용량 로그 파일 전체 로드
- 대화 수십 턴 누적
- 여러 MCP 도구가 각자 많은 데이터를 반환
- 긴 스키마·API 문서 통째로 로드

### 설계 원칙

1. **필요 범위만 로드**: 함수 하나 + 에러 로그 N줄 (전체 파일 ❌)
2. **상주 컨텍스트는 짧게**: CLAUDE.md를 운영 계약서 수준으로 유지
3. **장기 상태는 바깥 파일로**: handoff, decision-log를 세션 밖에 저장
4. **역할 분리**: plan / implement / review를 다른 세션으로 나누면 각자 토큰이 가볍다
5. **큰 전환점마다 handoff**: 다음 세션이 재로드 없이 이어받기

### BI 업무 적용 예

- ❌ 테이블 전체 DDL 500개 로드 → 좁은 작업 범위라도 비쌈
- ✅ 관련 테이블 3개 스키마 + 샘플 쿼리 2개 + 에러 메시지

## 관련 개념

- [[harness]]: 토큰 경제학을 자연스럽게 강제하는 구조
- [[context-engineering]]: 어떤 자료를 컨텍스트에 넣을지 선택하는 기술
- [[claude-code]]: `/compact`, `--resume`, CLAUDE.md 등 토큰 경제학 도구 제공

## Prompt Caching 운영 핸들 (claude-cookbooks 기준)

[[anthropics-claude-cookbooks]] `misc/prompt_caching.ipynb`에서 정리된 실제 운영 핸들:

| 항목 | 값 |
|------|-----|
| **TTL** | 5분 (기본) / 1시간 (확장) — 두 옵션 |
| **breakpoint 한도** | 메시지당 4개 |
| **최소 캐시 단위** | 1024 토큰 (이보다 작으면 캐시 안 됨) |
| **캐시 적중 시 입력 비용** | 정상가의 약 **0.1×** |
| **캐시 작성 비용** | 정상가의 약 1.25× (한 번 작성 후 재사용) |

운영 패턴:
- 시스템 프롬프트 + 자주 안 변하는 컨텍스트(예: CLAUDE.md)를 **캐시 대상**으로 두고 동적 부분만 뒤에 붙이기
- 멀티턴 세션에서 첫 N 메시지를 캐시 → 후속 턴에서 입력 비용 절감
- 5분 TTL은 "사용자가 활발히 대화 중"인 경우, 1시간 TTL은 "주기적으로 재호출되는 워크플로우"에 매핑

이 핸들이 [[harness]]의 "안정적 부모 컨텍스트가 prompt cache를 공유" 인용을 정량 수치로 풀어준다.

## 출처

- [[claude-code-master-guide]] — CHOI의 가이드북 2장 "핵심 개념" 및 9장 "커뮤니티 패턴"에서 prompt cache 해석
- [[anthropics-claude-cookbooks]] — `misc/prompt_caching.ipynb` 운영 핸들 (TTL 5분/1시간, 4 breakpoint, 1024 토큰 최소, 0.1× 적중 비용)

## 열린 질문

- Claude Opus 1M 컨텍스트를 쓸 때 토큰 경제학은 여전히 유효한가? (여전히 유효. 긴 컨텍스트가 가능해도 잘 쓰는 팀은 범위를 좁힌다)
- 회사 BI 쿼리 에이전트에서 토큰 hotspot은 어디인가? (대형 팩트 테이블 샘플링, 사용자 정의 함수 정의부 전체 로드)
