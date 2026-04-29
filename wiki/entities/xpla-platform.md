---
title: "XPLA 플랫폼 (c2spf 블록체인 통합 서비스)"
type: entity
entity_type: service
tags: [xpla, blockchain, nft, smart-contract, com2us-platform, c2spf, nestjs, rust]
related:
  - "[[com2us-platform]]"
  - "[[seokgeun-kim]]"
  - "[[blockchain-xpla]]"
source_count: 3
observed_source_refs: 11
inbound_count: 19
created: 2026-04-24
updated: 2026-04-24
---

# XPLA 플랫폼 (c2spf 블록체인 통합 서비스)

## 개요

컴투스플랫폼이 게임에 블록체인 기능(지갑 연동·NFT 민팅·트랜잭션 서명/전송·홀더 인증·투표 등)을 SDK로 통합 제공하는 서비스 플랫폼. 2022~2024년 NFT 마켓 프로젝트로 시작해 2024-04 XPLA 플랫폼으로 통합·확장되었다. 김석근이 시스템 설계·API 정의·풀스택 개발을 주도.

## 주요 특징

- **모듈 구성**
  - **NFT 마켓 백엔드** (2022-05 ~ 2024-03) — NFT 지갑 관리, 민팅, 거래.
  - **Discord 홀더 인증 봇** — Discord.py + FastAPI + Pytest. NFT 홀더만 접근 가능한 채널/역할 부여.
  - **Rust 투표 스마트 컨트랙트** — 가스비 ~90% 절감 최적화 적용. 의사결정 투명성 확보.
  - **XPLA 플랫폼 SDK** (2024-04 ~ 2024-07) — 게임이 SDK 호출 한 번으로 블록체인 기능 통합.
  - **CODE 트래블룰 API** (2021-10 ~ 2022-04) — 가상자산 거래소 트래블룰 공통 API (FastAPI).
- **핵심 플로우**
  - NFT 민팅 E2E: Action 조회 → 서명 → 전송 → 결과 노출.
  - 엣지 케이스 선제 처리: 중복 민팅, 수수료 부족 (XPLA 잔액 < 총 수수료) 등.
- **기술 스택**
  - Backend: Node.js (NestJS, TypeORM, TypeScript), Python (FastAPI, Discord.py)
  - Frontend: React + TypeScript (XPLA 웹뷰)
  - Smart Contract: Rust
  - Data: MySQL 8 (Master-Slave), MariaDB, Redis
  - Infra: Docker, AWS, ElasticSearch/Kibana, Fluentd
- **Jira 추적**: `GCPNFT` (NFT 마켓, 229/231 Done), `CPBLOC` (XPLA 플랫폼, 19건 전수 완료).

## 관련 개념

- [[com2us-platform|컴투스플랫폼 c2spf]] — 운영 회사
- [[seokgeun-kim|석근 (이 위키 owner)]] — 주축 개발자
- [[blockchain-xpla]] — XPLA 생태계·스마트 컨트랙트 개발 패턴

## 출처

- [[portfolio-seed]] — XPLA, NFT 마켓, 트래블룰 다년 프로젝트 라인
- [[c2spf-nft-market]] — NFT 마켓 상세
- [[c2spf-xpla-platform]] — XPLA 플랫폼 상세

## 논쟁/모순

(없음)

## 메모

- "NFT 마켓에서 XPLA 플랫폼으로"의 전이는 단순 명명 변경이 아니라 단일 프로덕트에서 다중 게임 SDK 플랫폼으로의 추상화 격상.
- Rust + NestJS + Python(Discord.py) 다언어 구성은 도메인별 도구 적합성에 따라 결정 — 가스 비용에 민감한 컨트랙트는 Rust, 봇/API는 Python, 코어 백엔드는 NestJS.
