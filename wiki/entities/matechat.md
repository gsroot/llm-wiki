---
title: "MateChat"
type: entity
entity_type: project
tags: [matechat, 메이트챗, AI, social, social-ai, fastapi, flutter, openai, websocket, iap, clover, startup, side-project, project-wiki]
related:
  - "[[seokgeun-kim]]"
  - "[[seokgeun-kim-profile-2026]]"
  - "[[seokgeun-operating-profile-2026]]"
  - "[[mate-chat-project-wiki-2026]]"
  - "[[matechat-project-knowledge-map]]"
  - "[[backend-python-fastapi]]"
  - "[[ml-ai]]"
  - "[[flutter]]"
  - "[[fastapi]]"
  - "[[openai]]"
  - "[[postgresql]]"
  - "[[redis]]"
  - "[[sqlalchemy]]"
  - "[[alembic]]"
  - "[[token-economy]]"
source_count: 5
created: 2026-04-28
updated: 2026-04-28
---

# MateChat

## 개요

**MateChat**은 석근이 개발 중인 소셜+AI 하이브리드 모바일 서비스다. 제품 슬로건은 "대화의 시작은 AI, 끝은 사람." / "Start with AI. End with people."이며, 핵심 정체성은 **AI가 사람을 대체하는 앱이 아니라 사람과 사람의 연결을 돕는 앱**이다.

기존 AI 컴패니언 앱은 AI와의 관계 자체를 끝점으로 삼고, 기존 소셜/채팅 앱은 사용자가 어색함과 대화 시작의 부담을 직접 감당하게 만든다. MateChat은 그 사이에서 AI가 사회적 어색함을 완충하고, 최종적으로 실제 인간 대화를 만들도록 돕는 것을 목표로 한다.

## 주요 특징

### 제품 포지셔닝

- Character.AI/Replika의 더 좋은 버전이 아니다.
- Maum/Azar의 텍스트 버전도 아니다.
- Discord에 AI를 붙인 범용 채팅 앱도 아니다.
- 더 정확한 포지션은 **"AI 시대에 사람과 다시 연결되도록 돕는 앱"**이다.

### 핵심 페르소나

- 20대 후반~30대 대도시 거주자.
- ChatGPT, Character.AI, Replika 등과 긴 시간 대화하지만 실제 인간 친구를 만들고 싶은 사람.
- Tinder/Bumble은 부담스럽고, Discord 신규 그룹 진입은 어색하며, 직장 동료와는 거리감이 있는 사람.
- AI 대화 후 재미는 있지만 공허함을 느끼는 사람.

확장 페르소나는 외국 워홀러/이민자, 사회 불안이 있는 학생, 새 도시 이주자, 사람과 대화하고 싶지만 시작이 어려운 사람이다.

### 기술 스택

- **Backend**: [[fastapi]], Python 3.13, [[postgresql]] 15, [[redis]] 7, [[sqlalchemy]] 2.0 async, [[alembic]]
- **Mobile App**: [[flutter]]
- **AI**: [[openai]] GPT-4 계열 API
- **Storage/Infra**: MinIO, Redis, PostgreSQL
- **Tooling**: [[uv]]
- **주요 기능**: OAuth, JWT, WebSocket 실시간 채팅, AI 챗봇, 가상 화폐 클로버, IAP, FCM 푸시 알림

### 현재 상태

2026-04 기준 백엔드·Flutter 앱·인증·실시간 채팅·AI 챗봇·클로버·IAP·푸시 알림·다국어화 등 핵심 기능 대부분이 구현되어 있다. [[seokgeun-kim-profile-2026]]은 Android v1.0.0 출시 직전 수준이라고 기록하고, [[mate-chat-project-wiki-2026]]은 v1.0.0 Google Play Store 출시 완료 및 운영 모드라고 기록한다. 최신 출시 상태는 Play Console, 배포 태그, mate-chat 저장소의 최신 문서로 재확인해야 한다.

따라서 다음 단계는 기능 추가보다 **closed alpha 또는 내부 테스트**다. 우선 단위는 1개 공개 채팅방, 1개 Mate-Bot, 10명 이내 사용자로 잡는 것이 현실적이다.

### 프로젝트 위키 스냅샷

`mate-chat/wiki`는 MateChat 전용 LLM-maintained wiki이며, 2026-04-28 스냅샷 기준 68개 마크다운 파일을 가진다. 구조는 `sources/` 19개, `entities/` 22개, `concepts/` 22개, `synthesis/` 2개와 메타 파일 3개다.

이 프로젝트 위키는 FastAPI 앱, Flutter 앱, WebSocket, Redis Pub/Sub, PostgreSQL, IAP, Clover, FCM, i18n, Google Play Store, 배포 파이프라인, 글로벌 출시 준비를 세부적으로 다룬다. `llm-wiki`에서는 이를 개별 페이지로 복제하지 않고, [[mate-chat-project-wiki-2026]] 원천 스냅샷과 [[matechat-project-knowledge-map]] 종합 분석으로 추적한다.

## 핵심 검증 질문

1. 외로운 AI 의존자 페르소나가 실제로 존재하는가?
2. 그들이 MateChat을 설치하고 계속 사용할 이유가 있는가?
3. AI가 사람 간 대화를 실제로 촉진하는가?
4. 첫 7일 안에 인간-인간 양방향 메시지 5회 이상이 발생하는가?
5. 사용자가 클로버에 돈을 낼 만큼 AI/소셜 경험에 가치를 느끼는가?

## KPI와 수익화

MateChat은 클로버라는 가상 화폐 기반 IAP 모델을 포함한다. AI 메시지 사용량, 클로버 소비, 유료 전환, 리텐션이 주요 수익 변수다.

현재 관점에서 수익은 후행 지표다. 먼저 확인해야 할 것은 제품이 실제로 유지율, 결제 사용자, 자연 확산을 만들어내는지 여부다.

중요 KPI:

- Paying user count 1,000명
- D30 retention 8%+
- Organic K-factor 0.3+
- 첫 7일 내 인간-인간 양방향 메시지 5회 이상 비율

## 리스크

- 기능 부족보다 사용자 검증 부족
- 출시 지연
- 마케팅/포지셔닝 미정
- 혼자 운영하면서 생길 수 있는 번아웃
- IAP 실제 검증, 개인정보처리방침/이용약관, 콘텐츠 모더레이션, 신고 처리, COPPA 13세 확인, 다국어 품질, 앱스토어 메타데이터 등 출시 전 최종 재확인 필요 항목
- 프로젝트 위키의 출시 완료 기록과 개인 프로필의 출시 직전 기록 사이의 시점/표현 차이

## 관련 개념

- [[ml-ai]]: OpenAI 기반 AI 챗봇과 AI→사람 연결 전략
- [[backend-python-fastapi]]: MateChat 백엔드의 기본 기술 축
- [[flutter]]: 모바일 앱 구현 스택
- [[token-economy]]: 클로버 기반 AI 사용량 과금과 LLM 비용 구조

## 출처

- [[seokgeun-kim-profile-2026]] — 제품 비전, 사업화 목표, KPI, 리스크, 육아휴직 기간 운영 계획의 1차 소스
- [[mate-chat-project-wiki-2026]] — 프로젝트 전용 위키 스냅샷. 구현, 아키텍처, 출시 준비, 운영 지식의 세부 소스
- [[portfolio-seed]] — 개인 프로젝트로서 Mate Chat 언급
- [[portfolio-resume-ko]] — 이력서의 Mate Chat 요약
- [[portfolio-ko]] — 상세 포트폴리오의 Mate Chat 기술 스택 요약

## 논쟁/모순

- 일부 출시 준비 문서는 IAP/푸시/법적 문서/모더레이션을 출시 차단 또는 고위험 이슈로 보지만, 이후 TODO 문서는 여러 항목을 v1.0.0 완료로 표시한다. 실제 출시 전에는 최신 구현 상태를 코드와 스토어 콘솔 기준으로 다시 확인해야 한다.
- [[mate-chat-project-wiki-2026]]은 v1.0.0 Google Play Store 출시 완료로 기록하지만, [[seokgeun-kim-profile-2026]]은 2026-04-28 기준 출시 직전 수준으로 기록한다. 최신 상태를 단정할 때는 mate-chat 저장소와 Play Console을 확인해야 한다.

## 메모

- 단기 최우선은 "더 많은 기능"이 아니라 실제 사람 간 대화가 만들어지는지 확인하는 것이다.
- 포지셔닝 문장은 "AI 친구 앱"보다 "AI가 사람 친구를 만들어주는 앱" 쪽이 핵심 가설과 더 잘 맞는다.
- 사업화가 가족 시간 확보 전략과 직접 연결되어 있으므로, 운영 계획에는 개발뿐 아니라 마케팅·QA·지표 분석·번아웃 방지 루틴이 함께 들어가야 한다.
