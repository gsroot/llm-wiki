---
title: "mate-chat 프로젝트 위키 스냅샷 (2026-04-28)"
type: source
source_type: note
source_url: ""
source_scope: local
raw_path: "raw/notes/mate-chat-wiki-2026-04-28/"
author: "석근 + LLM-maintained Mate Chat wiki"
date_published: 2026-04-07
date_ingested: 2026-04-28
tags: [matechat, project-wiki, obsidian, fastapi, flutter, launch, architecture, iap, websocket, i18n, clover]
related:
  - "[[matechat]]"
  - "[[matechat-project-knowledge-map]]"
  - "[[seokgeun-kim-profile-2026]]"
  - "[[seokgeun-operating-profile-2026]]"
  - "[[backend-python-fastapi]]"
  - "[[ml-ai]]"
  - "[[flutter]]"
  - "[[token-economy]]"
confidence: high
---

# mate-chat 프로젝트 위키 스냅샷 (2026-04-28)

## 한줄 요약

> `mate-chat/wiki`는 MateChat 프로젝트 전용 Obsidian/LLM 위키로, 아키텍처·구현 현황·출시 준비·운영 지식 68개 마크다운 파일을 담은 프로젝트 단위 지식 베이스다.

## 핵심 내용

이 소스는 `/Users/sgkim/Projects/mate-chat/wiki`의 콘텐츠를 `llm-wiki` 원천 자료로 가져온 스냅샷이다. `.obsidian/` 설정은 제외하고, `SCHEMA.md`, `index.md`, `log.md`, `sources/`, `entities/`, `concepts/`, `synthesis/`의 마크다운 콘텐츠만 보존했다.

`mate-chat/wiki`는 현재 `llm-wiki`와 같은 LLM-maintained wiki 패턴을 MateChat 프로젝트 하나에 한정해 적용한 구조다. 원시 소스는 mate-chat 저장소의 `docs/`이고, 프로젝트 위키는 그 문서를 요약·연결·종합한 2차 지식 레이어다. `llm-wiki` 관점에서는 이 프로젝트 위키 전체가 **MateChat에 대한 원천 소스 묶음** 역할을 한다.

## 구조 스냅샷

| 구분 | 파일 수 | 역할 |
|------|--------:|------|
| Meta | 3 | `SCHEMA.md`, `index.md`, `log.md` |
| Sources | 19 | `docs/` 원문 18개+아카이브 요약 |
| Entities | 22 | FastAPI, Flutter, PostgreSQL, Redis, IAP, Clover 등 구성 요소 |
| Concepts | 22 | 아키텍처, 인증, WebSocket, 국제화, ASO, 배포 등 개념 |
| Synthesis | 2 | 구현 현황 종합, 글로벌 출시 준비 종합 |
| **합계** | **68** | 프로젝트 전용 지식 베이스 |

프로젝트 `index.md`는 엔티티를 21개로 표기하지만 스냅샷 파일 수 기준으로는 22개다. `clover-system.md`가 후속으로 추가되며 카운트만 완전히 갱신되지 않은 것으로 보인다.

## 주요 내용

### 1. 아키텍처와 스택

MateChat은 Firebase 레거시에서 FastAPI 기반 자체 백엔드로 리마스터된 프로젝트다. 핵심 스택은 [[fastapi]], Python 3.13, [[postgresql]], [[redis]], MinIO, Docker, [[flutter]], [[openai]] GPT-4 계열 API다.

프로젝트 위키는 FastAPI 앱을 4계층 구조(API, Service, Repository, Model/DB)로 설명하고, Flutter 앱은 feature-first 구조와 Riverpod, Dio, GoRouter, secure storage, WebSocket client를 중심으로 정리한다.

### 2. 제품 핵심: 하이브리드 AI 채팅

`hybrid-ai-chat.md`는 MateChat의 제품 차별점을 가장 잘 보여준다. 사람 간 채팅방에 AI 봇을 추가하고, 사용자가 트리거 프리픽스로 봇을 호출하면 최근 대화 컨텍스트를 기반으로 GPT 응답을 생성해 같은 방에 브로드캐스트하는 구조다.

이는 [[seokgeun-kim-profile-2026]]에서 정리된 "AI가 사람을 대체하는 앱이 아니라 사람과 사람의 연결을 돕는 앱"이라는 제품 비전과 직접 연결된다.

### 3. 수익화: 클로버와 IAP

`clover-system.md`와 `in-app-purchase.md`는 소모성 가상 화폐 모델을 설명한다. 클로버는 AI 채팅과 프리미엄 기능에 쓰이는 가상 화폐이며, Google Play/App Store IAP 검증 흐름과 거래 테이블로 추적된다.

이 구조는 [[token-economy]]의 LLM 비용 관리와 연결된다. 단순 결제 기능이 아니라 OpenAI API 사용량, 유료 전환, AI 대화 가치 인식이 맞물리는 수익화 레이어다.

### 4. 구현과 출시 상태

프로젝트 위키의 `synthesis/implementation-status.md`와 `synthesis/launch-readiness.md`는 MateChat v1.0.0을 Google Play Store 출시 완료 및 운영 모드로 기록한다. 백엔드 83개 API, Flutter 132개 Dart 파일, 9개 언어, FCM 푸시, IAP 검증, Sentry/Grafana/Loki, 보안 감사와 QA 결과가 요약되어 있다.

다만 [[seokgeun-kim-profile-2026]]은 2026-04-28 기준 "Android v1.0.0 출시 직전 수준"이라고 표현한다. 두 소스 사이에 시점 또는 표현 차이가 있으므로, 최신 출시 상태를 말할 때는 Play Console, 배포 태그, 현재 mate-chat 저장소 문서를 직접 확인해야 한다.

### 5. 남은 과제

프로젝트 위키 기준 남은 과제는 iOS App Store 배포, Apple OAuth, 콘텐츠 모더레이션 강화, UI 번역 완성도 개선, Redis Pub/Sub 분산 배포, WebSocket DB 풀 최적화, Flutter E2E 테스트 확충 등이다.

사업 관점에서는 기능 완성보다 사용자 검증이 더 중요하다는 [[seokgeun-operating-profile-2026]]의 판단과 결합해야 한다. 기술 위키가 "무엇을 만들었는가"를 말한다면, 개인 운영 프로필은 "무엇을 검증해야 하는가"를 말한다.

## 주요 인사이트

1. **프로젝트 위키는 복제 대상이 아니라 원천 스냅샷 대상이다.** 68개 페이지를 `llm-wiki`에 개별 페이지로 다시 만들면 중복 관리가 생긴다. `llm-wiki`에는 요약·종합만 두고 세부는 `raw_path`로 추적하는 편이 낫다.
2. **MateChat 지식은 두 레이어로 나뉜다.** 프로젝트 위키는 구현/출시/운영 지식, 개인 프로필은 사업화/가족/사용자 검증/AI 협업 지식이다.
3. **출시 상태는 반드시 최신 확인이 필요하다.** 프로젝트 위키는 출시 완료로 쓰고, 개인 프로필은 출시 직전으로 쓴다. 이 모순은 나쁜 데이터라기보다 문서 작성 시점과 관점 차이로 보인다.
4. **Clover는 제품 수익화와 LLM 비용을 연결하는 핵심 노드다.** 가상 화폐, IAP, AI 사용량, 결제 전환, 유지율이 한 지점에서 만난다.
5. **가장 중요한 후속 지식은 사용자 검증 로그다.** 프로젝트 위키가 구현 지식은 충분히 담고 있으므로, 다음 수집 대상은 closed alpha 결과, 인터뷰, 이벤트 지표, D1/D7/D30 리텐션, 인간-인간 메시지 발생률이다.

## 관련 엔티티/개념

- [[matechat]]: 이 프로젝트 위키의 대상
- [[matechat-project-knowledge-map]]: 이 스냅샷과 개인 프로필을 함께 해석한 종합 분석
- [[backend-python-fastapi]]: MateChat 백엔드 스택과 연결
- [[flutter]]: MateChat 모바일 앱 스택
- [[ml-ai]]: OpenAI GPT 기반 AI 대화 기능
- [[token-economy]]: 클로버/IAP/AI 사용량 수익화 구조

## 인용할 만한 구절

> "LLM이 작성하고 유지관리하며, `docs/`의 원시 문서를 종합하여 구조화된 지식으로 변환합니다."
> — `mate-chat/wiki/SCHEMA.md`

> "Mate Chat은 2026-04-07 기준 v1.0.0 Google Play Store 출시 완료 상태이다."
> — `synthesis/implementation-status.md`

## 메모

- 이 스냅샷은 `mate-chat/wiki`를 그대로 복사한 것이므로, 이후 프로젝트 위키가 바뀌면 새 날짜의 raw 스냅샷을 별도로 만들어 수집하는 편이 안전하다.
- `llm-wiki`에서 MateChat 관련 질문에 답할 때, 세부 구현 근거는 이 source의 `raw_path` 아래 개별 파일을 확인한다.
- `.obsidian/` 설정은 기계/뷰 상태라 원천 지식으로 보존하지 않았다.
