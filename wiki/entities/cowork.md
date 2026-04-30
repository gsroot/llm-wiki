---
title: "Cowork"
type: entity
entity_type: tool
tags: [cowork, AI, anthropic, 지식업무, knowledge-work, 에이전트, 비개발자, agent]
related:
  - "[[claude-code]]"
  - "[[harness]]"
  - "[[llm-wiki-pattern]]"
source_count: 1
observed_source_refs: 4
inbound_count: 9
created: 2026-04-15
updated: 2026-04-15
cited_by_count: 3
---

# Cowork

## 개요

Anthropic이 Claude Code의 에이전트 기능을 **코딩 바깥 지식 업무**로 확장한 작업 경로. 폴더와 파일 기반으로 동작하며 비개발자도 쓸 수 있다. 리서치·문서 정리·경쟁사 분석·자료 정리·보고서 작성에 강하다.

Anthropic 공식 릴리스 노트는 Cowork를 "Claude Code의 에이전트 기능을 코딩 바깥 지식 업무로 가져온 표면"으로 설명한다.

## [[claude-code]]와의 관계

대체재가 아니라 **다른 작업층**:

| 구분 | Cowork | Claude Code |
|------|--------|-------------|
| 중심 | 문서·파일 결과물 | 코드 수정·검증 |
| 사용자 | 비개발자 친화 | 개발자 중심 |
| 기반 | 폴더·파일 | 터미널·Git |
| 강점 | 리서치, 문서, 보고서 | 파일 변경, 테스트, 재사용, 원격 이어받기 |

> **역할 분담**: 기획안과 브리프는 Cowork에서, 구현과 테스트는 Claude Code에서.

## Claude 생태계 4가지 작업 경로에서의 위치

1. **Chat**: 질문·요약·학습 (장기 상태 없음)
2. **Projects**: 배경 컨텍스트 유지 (파일 자동화 불가)
3. **Cowork**: 폴더·파일 기반 지식 업무
4. **Claude Code**: 코드·검증·배포

## 공유되는 운영 구조

Cowork는 Claude Code가 가진 다음 구조를 지식 업무로 확장한다:
- 컨텍스트 조립 (CLAUDE.md, 규칙 파일)
- 권한 판정 (allow/ask/deny)
- 도구 실행
- 세션 이어받기 (handoff)
- 검증 구조

즉 Cowork를 배우는 것은 별도 제품을 배우는 것이 아니라 **같은 [[harness]]를 다른 작업 모양에 붙이는 것**에 가깝다.

## 권장 사용 장면

- 주간 경쟁사 브리프 (경쟁사 메모·기사 링크·액션 아이템 폴더 → 이번주 변화/의미/액션 3개로 압축)
- 회의 이후 문서화 (메모·양식·미해결 질문 분리 → "무엇을 결정해야 하는가"로 정리)
- PRD 초안 (리서치 요약 → 비교표 → 미해결 질문 → 티켓 단위 실행 항목)
- 온보딩·교육 자료, 지원사업 제안서 (grant proposal)

## 출처

- [[claude-code-master-guide]] — CHOI의 실전 마스터 가이드. Cowork와 Claude Code를 상호 보완적 "작업 운영층"으로 배치

## 메모

- 석근님 관점: 회사 BI 업무에서 지표 해석·보고서 초안·회의록 정리는 Cowork가, 파이프라인 스크립트·대시보드 코드·쿼리 검증은 Claude Code가 맡는 조합이 자연스러울 것.
- 이 위키를 운영하는 도구로서는 Claude Code가 주력이지만, Cowork도 외출 시·비개발 업무 시 대체 가능 (Cowork 자체가 CLAUDE.md 계약을 읽으므로).
