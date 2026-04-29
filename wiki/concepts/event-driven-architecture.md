---
title: "Event-driven Architecture"
type: concept
category: system-architecture
tags: [event-driven-architecture, eda, event-sourcing, cqrs, kafka, pubsub, 25회차]
related:
  - "[[kafka]]"
  - "[[redis]]"
  - "[[append-only-log]]"
  - "[[matechat]]"
source_count: 4
created: 2026-04-28
updated: 2026-04-29
---

# Event-driven Architecture (EDA)

## 정의

**Event-driven Architecture** = 시스템 컴포넌트가 동기 호출(요청-응답)이 아닌 비동기 이벤트(메시지) 발행·구독으로 통신하는 아키텍처. 컴포넌트 간 시간·공간 결합 해체.

본 페이지는 **stub** — 16회차 [[kafka]] / 24회차 [[matechat]] WebSocket Pub/Sub 등에서 인용되므로 정합성 stub.

## 핵심 패턴 3가지

| 패턴 | 설명 | 본 위키 사례 |
|---|---|---|
| **Event Notification** | "X가 일어났다" 단순 알림 | [[matechat]] FCM 푸시 / Sentry 알림 |
| **Event-carried State Transfer** | 이벤트가 상태 데이터 포함 | [[kafka]] Topic message |
| **Event Sourcing** | 이벤트 로그 자체가 진실원, 상태는 derived | (미수집, [[append-only-log]] 기반) |

추가: **CQRS** (Command Query Responsibility Segregation) — 쓰기 모델(이벤트) ↔ 읽기 모델 분리.

## 본 위키 인용 맥락

- 16회차 [[kafka]]: EDA의 표준 메시지 브로커 (분산 + 영속 + replay 가능)
- 15회차 [[redis]] Pub/Sub: 경량 EDA 백본
- 24회차 [[matechat]]: WebSocket Pub/Sub (Redis 기반) — 실시간 채팅 메시지 브로드캐스트
- 19회차 [[observability-and-cicd-stack]]: Sentry 이벤트 수신 → 알림 발송도 EDA의 변종

## 회사 BI 응용

- 게임 이벤트 → Kafka → BigQuery 적재 = EDA + Lambda 아키텍처
- 실시간 BI 알림 (이상 탐지) = EDA + 임계치 trigger

## 관련 개념

- [[kafka]] — EDA 표준 백본
- [[append-only-log]] — Event Sourcing 자료구조
- [[redis]] Pub/Sub — 경량 EDA
- [[matechat]] — WebSocket EDA 실증

## 출처

- [[apache-kafka]] — 분산 이벤트 로그와 replay 가능한 메시징 백본
- [[redis-redis]] — Pub/Sub과 Streams 기반 경량 이벤트 처리
- [[seokgeun-mate-chat]] — MateChat WebSocket/Redis PubSub 실증
- [[getsentry-sentry]] — 이벤트 수집 → 이슈/알림으로 이어지는 운영 EDA 변종

## 메모

- 25회차 stub 사유: 23회차 점검에서 `[[event-driven-architecture]]` 깨진 링크 발견. 29회차에 Kafka/Redis/MateChat/Sentry source 기반으로 1차 보강.
- 후속: Event Sourcing + CQRS는 별도 종합 페이지 가치 — DDD 패턴과 결합.
