---
title: "블록체인 (XPLA · Rust 스마트 컨트랙트 · NFT)"
type: concept
category: web-dev
tags: [blockchain, xpla, nft, smart-contract, rust, cosmos-SDK, web3, nestjs, discord-bot, gas-fee]
related:
  - "[[seokgeun-kim]]"
  - "[[xpla-platform]]"
  - "[[backend-python-fastapi]]"
source_count: 3
observed_source_refs: 7
inbound_count: 13
created: 2026-04-24
updated: 2026-04-24
---

# 블록체인 (XPLA · Rust 스마트 컨트랙트 · NFT)

## 정의

c2spf의 블록체인 통합 영역. XPLA(Cosmos SDK 계열) 체인 기반의 NFT 마켓·민팅·지갑·트랜잭션 SDK가 핵심. 스마트 컨트랙트는 Rust로, 백엔드는 NestJS(TypeORM)로, 봇/API는 Python(Discord.py + FastAPI)로 도메인별 적합 도구를 골라 구성.

## 왜 중요한가

- **블록체인 프로젝트 3건 주도** — CODE 트래블룰 API · NFT 마켓 · XPLA 플랫폼.
- **Rust 투표 스마트 컨트랙트 가스비 ~90% 절감** — 사용자 비용 직접 감소, 의사결정 투명성 확보. 정량 지표가 뚜렷한 보기 드문 성과.
- 2021-10부터 2024-07까지 약 3년간의 블록체인 서비스 운영 경험 — 가상자산 트래블룰 규제 대응부터 다중 게임 SDK까지.

## 핵심 내용

- **CODE 트래블룰 API** (2021-10 ~ 2022-04)
  - 가상자산 거래소들의 트래블룰 이행을 위한 공통 API.
  - 웹·블록체인 버전 API 구현, Sample VASP API, VerifyVasp 솔루션 연동.
  - FastAPI + SQLAlchemy + Pytest + Locust + MariaDB + Nats + Docker + AWS.
- **NFT 마켓** (2022-05 ~ 2024-03)
  - NFT 지갑 관리 백엔드 (NestJS + TypeORM).
  - Discord 홀더 인증 봇 (Discord.py + FastAPI + Pytest).
  - Rust 투표 스마트 컨트랙트 (가스비 ~90% 절감).
  - GCPNFT 229/231 Done.
- **XPLA 플랫폼** (2024-04 ~ 2024-07)
  - 다중 게임 SDK 통합 — 한 번의 SDK 호출로 블록체인 기능 사용.
  - NFT 민팅 E2E 플로우 (Action 조회 → 서명 → 전송 → 결과).
  - 엣지 케이스 선제 처리 (중복 민팅, 수수료 부족 등).
  - NestJS + TypeORM + React 웹뷰 + MySQL 8 Master-Slave + Docker.
  - CPBLOC 19건 전수 완료.

## 실전 적용

- **가스비 최적화 패턴** — 컨트랙트 설계 단계에서부터 storage 비용 줄이기, batch 처리, on-chain 데이터 최소화.
- **엣지 케이스 선제 처리** — 블록체인 트랜잭션은 재시도 비용(가스비)이 크므로 프론트/백 양쪽에서 유효성을 보장.
- **다중 언어 구성**: Rust(컨트랙트) + NestJS(코어 백엔드) + Python(봇/API) — 각 도메인 적합도 우선.

## 관련 개념

- [[backend-python-fastapi]] — 트래블룰 API와 Discord 봇 백엔드
- [[xpla-platform]] — 이 개념을 구체화한 서비스 엔티티

## 출처

- [[portfolio-seed]] — 블록체인 3 프로젝트 라인
- [[c2spf-nft-market]] — NFT 마켓 상세
- [[c2spf-xpla-platform]] — XPLA 플랫폼 상세

## 열린 질문

- Rust 컨트랙트의 가스비 최적화는 어떤 패턴을 적용했는가? (예: storage layout, batch operations)
- XPLA(Cosmos SDK 계열)와 EVM 계열의 SDK 통합 비교 — 어떤 차이가 운영에 영향을 주었는가?
