---
title: 석근 커리어 타임라인 (2016-2026)
type: synthesis
category: timeline
tags:
- career
- seokgeun-kim
- com2us-platform
- portfolio
related:
- '[[seokgeun-kim]]'
- '[[portfolio]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-stack-guide]]'
- '[[matechat]]'
sources:
- '[[portfolio-seed]]'
- '[[portfolio-resume-ko]]'
- '[[portfolio-ko]]'
- '[[portfolio-method]]'
- '[[c2spf-nft-market]]'
- '[[c2spf-xpla-platform]]'
- '[[c2spf-analytics-common]]'
- '[[c2spf-analytics-renewal]]'
created: 2026-04-24
updated: 2026-04-29
cited_by_count: 15
inbound_count: 23
---

# 석근 커리어 타임라인 (2016-2026)

## 요약

석근은 2016년 줌인터넷에서 백엔드 개발을 시작해, 2017년 컴투스플랫폼으로 옮긴 뒤 9년간 게임 데이터 BI(`c2spf` 애널리틱스) · 블록체인 플랫폼 · ML/AI 서비스를 풀스택으로 구축해 왔다. 시간이 지날수록 **기능 구현자에서 표준 정립자로** 역할이 진화했고, 2025-06 React 리뉴얼로 이 변화가 정점에 달했다. 같은 시기 LangGraph 기반 개인 앱을 Google Play에 출시하며 LLM/Agent 시대로 활동 영역을 확장.

## 배경

이 분석은 portfolio 저장소의 자료(이력서·상세 포트폴리오·프로젝트 통합 문서·시드 문서)를 통합 수집한 결과를 기반으로, **9년간의 기술적·역할적 진화 패턴**을 한 페이지에 응축하기 위해 작성됨. LLM이 면접/이력 질의에 답할 때 한 번의 페이지 조회로 시간순 맥락을 잡을 수 있도록 만든 종합 분석이다.

## 분석

### 시간축 정리

| 시기 | 회사/프로젝트 | 핵심 영역 | 역할의 진화 |
|------|--------------|----------|-------------|
| 2016-01 ~ 2016-07 | 줌인터넷 — 스윙 브라우저 / 줌닷컴 분석 | Spring Boot · HiveQL | 기능 구현자 |
| 2017-05 ~ 2018-08 | c2spf 애널리틱스 본체 + 스케줄러 | Spring Boot + jQuery, Digdag, BigQuery | 풀스택 구현자 |
| 2019-03 ~ 2019-06 | 대용량 다운로드 REST API · Celery 워커 | Flask + Celery + Pandas | 비동기 워커 패턴 도입 |
| 2020-08 ~ 2021-09 | ML 유저 예측 + AutoML MLOps | GCP AutoML + AI Platform Pipeline | **MLOps 체계 구축자** |
| 2021-06 ~ 2021-07 | 통합 인증 & 비동기 통신 모듈 | Flask | 모듈 표준화 |
| 2021-10 ~ 2022-04 | CODE 트래블룰 API | FastAPI + SQLAlchemy + Locust | 규제 대응 시스템 주도 |
| 2022-05 ~ 2024-03 | NFT 마켓 + Discord 봇 + Rust 컨트랙트 | NestJS + Discord.py + Rust | **블록체인 + 가스비 ~90% 절감** |
| 2024-04 ~ 2024-07 | XPLA 플랫폼 SDK | NestJS + TypeORM + React | 시스템 설계 리드 |
| 2024-08 ~ 2024-12+ | 애널리틱스 공통 모듈 + 배포 표준화 | FastAPI + Docker + Jenkins + Loki | **표준 정립자** (가이드 4종 발행) |
| 2025-01 ~ 2025-02 | Airbridge MMP API | Spring Boot + FastAPI 하이브리드 | 데이터 계약 확장 |
| 2025-06 ~ 현재 | 애널리틱스 React 리뉴얼 | Vite + React + TS + TanStack + Zustand + ag-grid | **팀 최초 React 도입 리드** |
| 2025-08 ~ 현재 | Mate Chat (개인) | FastAPI + WebSocket + OpenAI | LLM 시대 합류 |
| 2025-10 ~ 2025-11 | 트래블메이트 — Google Play 출시 (개인) | Flutter + LangGraph + FastAPI | **에이전트 프로덕션 배포자** |

### 패턴 1 — 역할의 진화

기능 구현자(2016-2018) → 모듈 표준화(2019-2021) → 시스템 설계 리드(2022-2024) → **표준 정립자**(2024-2025) → **에이전트 프로덕션 배포자**(2025+).

### 패턴 2 — 기술 스택의 누적

레거시 스택을 지우지 않고 **공존**시키는 능력. 2024-2025 기준 한 시스템 안에 Spring Boot + FastAPI + jQuery/Mobx + React + TS + ag-grid가 같이 살아 있고, 각자 자기 역할을 한다.

### 패턴 3 — 정량 지표의 누적

가스비 ~90% 절감(2022-2024), ML 정확도 85%+(2020-2021), 공통 API 92% 단독 유지보수(2024+), 프론트엔드 생산성 30~40% 향상 기반(2025+) — **각 시기마다 정량 지표를 하나씩 남긴다**.

### 패턴 4 — 회사 + 개인의 동시 진행

회사에서 React 리뉴얼을 주도하면서 개인적으로 LangGraph 앱을 출시(2025). 회사 활동과 개인 학습이 시간적으로 겹치며 서로 양방향 강화 — 회사에서 표준화·관측성 학습이 개인 프로젝트의 인앱결제·영수증 검증 시스템 구축에 적용됨.

## 결론

- **9년 풀스택 + 4영역(백엔드 / BI / ML/AI / 블록체인) 동시 운영자**라는 정체성이 시간순으로 일관되게 강화됨.
- 2024-2025년이 **변곡점** — 표준화 가이드 4종 발행 + React 팀 최초 도입 + LangGraph Google Play 출시로 "구현자에서 정립자로" 역할이 변화.
- 다음 자연스러운 발전 방향: (a) 사내 AI 도구 활용 가이드 정립자 역할 (이미 2025 React 리뉴얼에서 시작), (b) 개인 LLM/Agent 프로젝트의 수익화 안정화 (트래블메이트 ARPU 등).

## 열린 질문

- "표준 정립자" 역할이 다음 단계(예: 다른 팀까지 확산, 공식 강의·기고)로 어떻게 확장될 것인가?
- ML/AI의 두 시대(AutoML / LangGraph) 사이의 간극(2022-2024) 동안 ML 활동이 어떻게 유지되었는가?
- 4 영역 동시 운영의 한계는 어디에 있는가? 어떤 영역이 다음에 깊이 강화될 후보인가?

## 출처

- [[portfolio-seed]] — 시드 문서 (전체 시간축의 기반)
- [[portfolio-resume-ko]] — 정량 지표 5선의 출처
- [[portfolio-ko]] — Selected Work 5선과 Impact 표
- [[portfolio-method]] — 이 통합 분석의 메타 방법론
- [[c2spf-nft-market]] — 블록체인 시대 (가스비 절감)
- [[c2spf-xpla-platform]] — XPLA 시스템 설계 리드
- [[c2spf-analytics-common]] — 표준 정립자 변곡점 (가이드 4종)
- [[c2spf-analytics-renewal]] — 팀 최초 React 도입
- [[seokgeun-kim|석근 (이 위키 owner)]] — 본인 엔티티
