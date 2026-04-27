---
title: "컴투스플랫폼 NFT 마켓 (2022-05-nft-market.md)"
type: source
source_type: note
source_url: ""
author: "석근"
date_published: 2026-04-24
date_ingested: 2026-04-24
tags: [com2us-platform, c2spf, nft, blockchain, discord-bot, rust, smart-contract, 가스비절감]
related:
  - "[[com2us-platform]]"
  - "[[xpla-platform]]"
  - "[[seokgeun-kim]]"
  - "[[blockchain-xpla]]"
confidence: high
---

# 컴투스플랫폼 NFT 마켓 (2022-05-nft-market.md)

## 한줄 요약

> 2022-05 ~ 2024-03 기간 컴투스플랫폼 NFT 마켓의 지갑 관리 백엔드, Discord 홀더 인증 봇, Rust 투표 스마트 컨트랙트 최적화(**가스비 ~90% 절감**), Docker 배포 개선을 주도한 프로젝트 통합 문서.

## 핵심 내용

- **기간/역할**: 2022-05 ~ 2024-03. NFT 지갑 관리 백엔드 개발, Discord 봇 기능 통합, 투표 스마트 컨트랙트 개발.
- **기술 스택**: Node.js(NestJS, TypeORM), Python(Discord.py, FastAPI, Pytest), MySQL, Redis, Fluentd, Docker, Rust, TypeScript, ElasticSearch, Kibana.
- **핵심 성과**
  - **Rust 기반 투표 스마트 컨트랙트 최적화로 가스비 ~90% 절감** — 사용자 비용 감소 + 투명한 의사결정 구조 제공.
  - Discord 홀더 인증 봇 상용화 — 커뮤니티 인증 확장성 확보. 다양한 인증 방식으로 확장 가능한 아키텍처 설계.
  - GCPNFT 이슈 229/231 Done — 높은 완결성으로 프로젝트 종료.
  - 기존 컨테이너 관리 방식 개선으로 배포 효율성·생산성 향상.
- **증거 (portfolio 저장소 내 경로)**
  - `docs/20-projects/com2us-platform/2022-05-nft-market.md` — 프로젝트 통합 문서
  - `docs/40-stories/problem-solving-gas-fee-optimization.md` — 가스비 최적화 STAR 스토리
  - Jira: GCPNFT-1971, GCPNFT-1401, GCPNFT-1248, GCPNFT-983 등

## 주요 인사이트

- **가스비 90% 절감**은 블록체인 프로젝트에서 보기 드문 정량 지표. 단순 코드 최적화를 넘어 스마트 컨트랙트 설계 단계의 의사결정이 반영된 결과.
- NestJS(Node.js) + Discord.py(Python) + Rust가 공존 — 각 도메인의 특성에 맞춰 언어 선택. "Python 선호"라는 일반 프로필에도 불구하고 필요시 Rust 채택.
- 2년 가까이 운영된 장기 프로젝트. Discord 봇 → 투표 컨트랙트 → 지갑 관리까지 커뮤니티와 코어 시스템을 모두 건드림.

## 관련 엔티티/개념

- [[com2us-platform]] — 소속 조직
- [[xpla-platform]] — NFT 마켓 후속으로 확장된 블록체인 통합 플랫폼
- [[seokgeun-kim]] — 프로젝트 담당자
- [[blockchain-xpla]] — XPLA 생태계, 스마트 컨트랙트 개발 패턴

## 메모

- 원본 경로: `raw/notes/portfolio/docs/20-projects/com2us-platform/2022-05-nft-market.md`.
- 세부 Jira 티켓 본문은 `portfolio/private/jira/` (로컬 전용)에만 존재. llm-wiki에는 복사하지 않음.
