---
title: "Mate Chat"
type: entity
entity_type: project
tags: [mate-chat, side-project, personal, flutter, riverpod, fastapi, ai-companion, 23회차]
related: [[flutter]], [[riverpod]], [[fastapi]], [[backend-fastapi-stack]], [[flutter-nextjs-fullstack-pattern]]
source_count: 0
created: 2026-04-28
updated: 2026-04-28
---

# Mate Chat

## 개요

**Mate Chat**은 석근의 **개인 사이드 프로젝트** — AI 동반자 채팅 앱. 17~18회차 메모리 컨텍스트에 등장했고, 22회차 [[flutter-nextjs-fullstack-pattern]]에서 Flutter+Riverpod 단일 통합의 실증 사례로 인용됨.

본 페이지는 **stub** — Mate Chat 저장소가 위키 raw에 수집되지 않은 상태에서 외부 참조([[riverpod]], [[flutter]], [[backend-fastapi-stack]])들이 가리킬 수 있도록 등록된 placeholder.

## 추정 스택 (참조 페이지 종합)

| 영역 | 도구 |
|---|---|
| 모바일 | [[flutter]] + [[riverpod]] |
| 백엔드 | [[fastapi]] + [[postgresql]] + [[redis]] |
| 분석 | (가설) BigQuery 파이프라인, ML 분석 레이어 |
| 통신 | HTTP + WebSocket |

## 위치

- 저장소 URL: 미수집 (private 또는 별도 GitHub 조직 가능성)
- raw 디렉토리: 없음 → 추후 수집 시 `raw/articles/seokgeun-mate-chat/` 등 위치 후보

## 관련 개념

- [[flutter]] — 모바일 클라이언트 프레임워크
- [[riverpod]] — Flutter 단일 통합 상태관리
- [[fastapi]] — 백엔드 코어
- [[backend-fastapi-stack]] — 백엔드 6단 스택 종합
- [[flutter-nextjs-fullstack-pattern]] — 22회차 듀얼 클라이언트 종합 (Mate Chat = Flutter 진영 단일 통합 실증)

## 메모

- **23회차 stub 생성 사유**: 22회차까지 4개 페이지([[riverpod]], [[flutter]], [[flutter-nextjs-fullstack-pattern]], [[backend-fastapi-stack]])가 `[[mate-chat]]`을 참조했으나 페이지 부재로 깨진 링크였음. 마무리 점검에서 위키 정합성을 위해 stub 등록.
- **추후 수집 트리거**: Mate Chat 저장소가 공개되거나 README/AGENTS.md를 노출하면 raw 수집 → 본 페이지 1차 출처 등록 → 채팅 분석 모듈 설계(7가지 분석 축, BigQuery 파이프라인)를 별도 종합 페이지로 분리 가능.
- 채팅 분석 모듈 설계 메모(2026-04-27)에서 7가지 분석 축 + BigQuery 파이프라인 아키텍처가 논의됨. 추후 종합 페이지 [[matechat-project-knowledge-map]]와 연결 검토.
