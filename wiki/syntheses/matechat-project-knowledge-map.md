---
title: MateChat 프로젝트 지식 지도
type: synthesis
category: analysis
tags:
- matechat
- architecture
- launch
- project-wiki
sources:
- '[[mate-chat-project-wiki-2026]]'
- '[[matechat]]'
- '[[seokgeun-kim-profile-2026]]'
- '[[seokgeun-operating-profile-2026]]'
created: 2026-04-28
updated: 2026-04-28
cited_by_count: 6
inbound_count: 15
---

# MateChat 프로젝트 지식 지도

## 요약

MateChat 지식은 두 축으로 관리하는 것이 맞다. `mate-chat/wiki`는 구현·아키텍처·출시·운영의 세부 지식이고, `llm-wiki`는 석근의 삶/사업/AI 협업 맥락 속에서 MateChat이 어떤 의미를 갖는지 정리하는 상위 지식이다.

따라서 `llm-wiki`는 프로젝트 위키를 통째로 복제하지 않고, 스냅샷을 원천 데이터로 보존한 뒤 핵심 해석만 유지한다. 실제 코드·운영·릴리스 상태가 필요하면 `raw/notes/mate-chat-wiki-2026-04-28/` 아래 개별 페이지로 내려간다.

## 배경

석근은 `llm-wiki`를 개인 전체 지식 베이스로, `mate-chat/wiki`를 MateChat 프로젝트 전용 지식 베이스로 운영한다. 두 위키는 같은 LLM-maintained wiki 패턴을 쓰지만 범위가 다르다.

- `llm-wiki`: 석근 개인, 커리어, 기술, 가족, 사업, AI 협업, 여러 프로젝트를 아우르는 상위 위키
- `mate-chat/wiki`: MateChat 프로젝트의 구현/문서/운영만 다루는 하위 프로젝트 위키

## 분석

### 1. 프로젝트 위키가 담는 지식

`mate-chat/wiki`는 68개 마크다운 파일로 구성된다.

- `sources/`: 리마스터 개요, 기술 스택, 아키텍처, DB 스키마, API 설계, 인증, WebSocket, 구현 현황, 푸시, 릴리스, Play Store, i18n, 경쟁 분석, 배포 가이드
- `entities/`: FastAPI 앱, Flutter 앱, PostgreSQL, Redis, MinIO, Docker, Sentry, CI/CD, 인증, JWT, WebSocket, FCM, IAP, Clover, Google Play Store
- `concepts/`: layered architecture, async-first, repository pattern, soft delete, cursor pagination, OAuth, JWT lifecycle, WebSocket realtime, hybrid AI chat, release process, ASO
- `synthesis/`: 구현 현황 종합, 글로벌 출시 준비 종합

이 범위는 MateChat을 다시 온보딩하거나, 특정 시스템 변경의 영향 범위를 추적하거나, 출시 전 체크리스트를 재검토할 때 유용하다.

### 2. llm-wiki가 맡아야 할 해석

`llm-wiki`가 맡을 영역은 프로젝트 위키보다 한 단계 위다.

- MateChat이 석근의 2026년 육아휴직과 어떤 관계인지
- 제품 비전이 "AI 친구"가 아니라 "AI가 사람 친구를 만들어주는 앱"이라는 점
- 기능 완성도보다 사용자 검증이 병목이라는 판단
- 수익화 목표가 가족 시간 확보와 퇴사 판단 기준에 어떻게 연결되는지
- AI가 석근을 도울 때 코드 구현보다 검증·마케팅·운영 루틴을 어떻게 잡아줘야 하는지

### 3. 현재 상태 해석: 기술 완료와 시장 검증의 분리 (44회차 정합)

MateChat은 **출시 직전 QA 단계**다. 한때 프로젝트 위키 일부 raw 문서가 "출시 완료/운영 모드"로 잘못 기록했으나, 44회차에 owner 자기보고로 정정. 두 source([[mate-chat-project-wiki-2026]], [[seokgeun-kim-profile-2026]]) 모두 이제 동일 표현(출시 직전 QA 단계)으로 일치한다.

핵심 판단은 변함없다: **기술적으로는 많이 만들었고, 다음 병목은 QA 마무리와 사용자 검증이다.** 출시 후 물어야 할 질문은 "앱이 실제 사람 간 대화를 만들어내는가"다.

### 4. 핵심 시스템 노드

| 노드 | 프로젝트 위키의 의미 | 사업/검증 관점 |
|------|---------------------|----------------|
| Hybrid AI Chat | 사람 채팅방에 AI 봇이 함께 참여 | AI가 인간-인간 대화를 촉진하는지 검증하는 핵심 기능 |
| Clover System | IAP 기반 가상 화폐와 AI 사용량 추적 | 사용자가 AI/소셜 경험에 돈을 내는지 보는 수익화 실험 |
| Push Notification | 재방문과 메시지 알림 | D1/D7 리텐션과 대화 지속성에 직접 연결 |
| i18n System | 9개 언어 ARB와 푸시 i18n | 글로벌 포지셔닝의 전제, 하지만 초기 검증은 작게 가능 |
| Moderation | 신고/필터/스팸 처리 | 소셜 앱 운영 리스크의 핵심 |
| WebSocket | 실시간 채팅 기반 | 인간-인간 메시지 빈도 측정의 데이터 경로 |

### 5. 다음 수집 우선순위

프로젝트 위키를 가져온 뒤 더 중요한 것은 "구현 문서 추가"가 아니라 실제 사용 기록이다.

1. closed alpha 운영 로그
2. 사용자 인터뷰 원문
3. 첫 7일 인간-인간 메시지 5회 이상 발생률
4. AI 개입 전후 인간-인간 메시지 빈도 변화
5. D1/D7/D30 리텐션
6. 클로버 지급/소비/구매 전환
7. 앱스토어/플레이스토어 실제 심사·출시·리뷰 로그

## 결론

MateChat 프로젝트 위키는 이미 프로젝트 내부 실행 지식으로 충분히 크고 세부적이다. `llm-wiki`는 이를 원천 스냅샷으로 보존하고, MateChat이 석근의 사업화·가족 시간·AI 협업 전략에서 어떤 결정을 요구하는지 정리하는 상위 레이어로 남기는 것이 맞다.

앞으로 MateChat 관련 질문을 받을 때는 먼저 [[matechat|MateChat 사이드 프로젝트]]과 이 지도를 보고, 세부 구현이 필요하면 [[mate-chat-project-wiki-2026]]의 `raw_path` 아래 프로젝트 위키 스냅샷으로 내려간다.

## 열린 질문

- (해소됨, 44회차) ~~프로젝트 위키의 "v1.0.0 출시 완료"와 개인 프로필의 "출시 직전" 중 최신 운영 상태는 무엇인가?~~ → owner 자기보고로 "출시 직전 QA 단계"로 정합 완료.
- closed alpha 또는 실제 출시 후 사용자 검증 로그는 어디에 저장할 것인가?
- MateChat 위키와 llm-wiki 사이의 주기적 동기화는 수동 스냅샷으로 충분한가, 아니면 스크립트화할 필요가 있는가?
- 프로젝트 위키의 index 카운트 불일치(엔티티 21 표기 vs 파일 22개)는 mate-chat 쪽에서 별도로 정리할 것인가?

## 출처

- [[mate-chat-project-wiki-2026]] — mate-chat 프로젝트 위키 스냅샷
- [[matechat|MateChat 사이드 프로젝트]] — llm-wiki의 MateChat 프로젝트 엔티티
- [[seokgeun-kim-profile-2026]] — MateChat 비전, 사업화, 육아휴직 맥락
- [[seokgeun-operating-profile-2026]] — 2026년 개인 운영 전략
