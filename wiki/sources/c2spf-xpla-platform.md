---
title: "컴투스플랫폼 XPLA 플랫폼 (2024-04-xpla-platform.md)"
type: source
source_type: note
source_url: ""
source_scope: local
raw_path: "raw/notes/portfolio/docs/20-projects/com2us-platform/2024-04-xpla-platform.md"
author: "석근"
date_published: 2026-04-24
date_ingested: 2026-04-24
tags: [com2us-platform, c2spf, xpla, blockchain, nestjs, typeorm, webview, SDK]
related:
  - "[[com2us-platform]]"
  - "[[xpla-platform]]"
  - "[[seokgeun-kim]]"
  - "[[blockchain-xpla]]"
confidence: high
---

# 컴투스플랫폼 XPLA 플랫폼 (2024-04-xpla-platform.md)

## 한줄 요약

> 2024-04 ~ 2024-07, 여러 게임이 SDK로 블록체인 기능(지갑·NFT 민팅·트랜잭션 서명/전송)을 쉽게 쓸 수 있게 해 주는 공통 서비스 플랫폼. 시스템 설계·API 정의·백엔드·웹뷰를 풀스택으로 담당, NFT 민팅 E2E와 엣지 케이스(중복 민팅·수수료 부족) 선제 처리.

## 핵심 내용

- **기간/역할**: 2024-04 ~ 2024-07. 시스템 설계, API 정의, 백엔드 + 프론트엔드(웹뷰) 풀스택, 테스트 및 리팩토링.
- **기술 스택**: Node.js(NestJS, TypeORM), React, TypeScript, Docker, MySQL 8 (Master-Slave).
- **핵심 성과**
  - 여러 게임이 SDK로 블록체인 기능을 통합 호출할 수 있는 공통 플랫폼 구축.
  - NFT 민팅 E2E 플로우(Action 조회 → 서명 → 전송 → 결과) 구현.
  - 중복 민팅·수수료 부족 등 엣지 케이스 **선제 처리**.
  - CPBLOC Jira 19건 전수 완료로 일정 준수.
  - 개발·테스트·유지보수 단계의 리팩토링을 통해 코드 품질 향상.
- **증거**
  - `docs/20-projects/com2us-platform/2024-04-xpla-platform.md` — 통합 문서
  - Jira: CPBLOC-821(Mint), CPBLOC-861, CPBLOC-862 등 19건

## 주요 인사이트

- **엣지 케이스 선제 처리**가 핵심 가치 — 블록체인 트랜잭션은 재시도 비용(가스비)이 크므로 프론트/백 양쪽에서 유효성을 보장해야 UX 붕괴를 막을 수 있음.
- NestJS + TypeORM 선택은 컴투스플랫폼 내 기존 블록체인 스택(NFT 마켓, CODE 트래블룰)과 정합. 새 언어/프레임워크 도입보다 팀 내 지식 재활용 우선.
- MySQL Master-Slave로 서빙 DB 스케일 고려 — 플랫폼형 서비스의 읽기 트래픽 증가 대비.

## 관련 엔티티/개념

- [[com2us-platform]] — 소속 조직
- [[xpla-platform]] — 이 프로젝트로 구축된 플랫폼 엔티티
- [[seokgeun-kim]] — 담당자 (시스템 설계 리드)
- [[blockchain-xpla]] — XPLA 생태계 개념

## 메모

- 원본 경로: `raw/notes/portfolio/docs/20-projects/com2us-platform/2024-04-xpla-platform.md`.
- NFT 마켓(2022~2024) → XPLA 플랫폼(2024.04~07)으로 이어지는 연속적 블록체인 프로젝트 라인.
