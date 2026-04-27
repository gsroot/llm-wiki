---
title: "NFT 마켓 스마트 컨트랙트 가스비 ~90% 절감"
type: story
category: problem-solving
period: "2022-05 ~ 2024-03"
primary_project: "2022-05-nft-market"
tags: [blockchain, smart-contract, optimization, gas-fee, rust, xpla]
skills_demonstrated:
  - blockchain
---

# NFT 마켓 스마트 컨트랙트 가스비 ~90% 절감

> C2X(Web3) 생태계의 온체인 거버넌스(투표) 스마트 컨트랙트를 Rust 기반으로 재설계해 **트랜잭션당 가스비를 약 90% 절감**, 사용자 비용 부담을 구조적으로 낮춘 최적화 사례.

## Situation

2022년 하반기 C2X(Web3) 생태계 확장 국면에서 NFT 지갑 관리·Discord 커뮤니티 인증·온체인 거버넌스(투표) 기능이 단기간에 요구되었고, 투표와 홀더 인증은 온체인에서 이루어져야 해 **트랜잭션당 가스비가 사용자 참여율과 운영 지속성의 직접 변수**가 되는 구조였다. 초기 구현 상태에서는 저장 구조와 이벤트 발행이 최적화되지 않아 투표·인증 컨트랙트의 가스비 부담이 운영 리스크로 누적되고 있었다.

## Task

XPLA 계열(Cosmos SDK 기반) **Rust 스마트 컨트랙트의 가스비 최적화**를 설계·적용해, NFT 홀더 인증·거버넌스 투표 같은 사용자 직접 참여 기능의 트랜잭션 비용을 대폭 낮추는 것. 동시에 CPBLOC(XPLA 웹뷰) NFT Mint 플로우에서 **중복 민팅·수수료 부족 처리·tx 서명/전송/결과 페이지**를 포함한 블록체인-프론트 E2E 연결 경험을 확보한다.

## Action

- **Rust 컨트랙트 저장 구조 재설계**: XPLA 계열(Cosmos SDK / CosmWasm 계열) Rust 컨트랙트 환경에서 투표·인증 상태의 저장 스키마를 재설계. 온체인 쓰기 비용이 지배적인 구조이므로, 핵심 엔티티의 스토리지 레이아웃과 접근 패턴을 최적화 (상세 기법은 `private/jira/` 및 내부 아카이브 참조).
- **이벤트 발행 최적화**: 트랜잭션 이벤트 발행 규모·필드 구성을 재정비해 불필요한 온체인 로그를 제거하고, 오프체인에서 재구성 가능한 정보는 이벤트에서 배제.
- **블록체인-프론트 E2E 검증**: CPBLOC Sub-task(CPBLOC-821 Mint, -861 리팩토링, -862 다국어)에서 XPLA 웹뷰 NFT Mint 플로우의 중복 민팅 가드, 수수료 부족 처리, Action/수수료 정보 노출, tx 서명·전송·결과 페이지 전환을 직접 구현하면서 가스 비용 특성을 실측·검증.
- **관측·배포 기반 정비**: Fluentd → ElasticSearch → Kibana 로그 파이프라인, Docker 컨테이너 빌드·배포 표준화로 컨트랙트 배포·회귀 주기를 단축해 최적화 이터레이션 속도를 확보.
- **Discord 봇·지갑 백엔드 병행 최적화**: NestJS/TypeORM 지갑 백엔드와 Python Discord.py + FastAPI 홀더 인증 봇(Pytest 회귀) 측에서 온체인 조회 호출을 캐싱(Redis)하여 컨트랙트 읽기 호출 자체를 줄이는 방식으로 가스 외 비용도 함께 절감.

## Result

### 정량

- **투표 스마트 컨트랙트 가스비 약 90% 절감** — 사용자 1인당 투표·인증 트랜잭션 비용을 자릿수 단위로 낮춤 (old-portfolio.md "NFT 마켓 개발" 성과 원문).
- **NFT 홀더 인증 기능 단기 상용화** — Discord 커뮤니티에서 NFT 보유 여부 기반 Role 부여가 즉시 운영 가능하도록 컨트랙트·봇 조합을 단기간에 완성 (old-portfolio.md).
- **GCPNFT 프로젝트 누적 티켓 231건 중 229건 Done** (2025-08 기준), 프로젝트 전반을 Done-대기 없이 종결.

### 정성

- 가스비 구조적 절감으로 **사용자 비용 부담 완화 → NFT 마켓 운영 지속성 확보**, 투표·인증 같은 커뮤니티 참여 기능의 확장 여지를 확보.
- 본 프로젝트의 Rust 컨트랙트·지갑 백엔드·Mint 플로우 경험이 이후 **XPLA 플랫폼(2024-04)**의 SDK 기반 블록체인 기능 공개로 자연스럽게 연결됨.
- 블록체인 도메인(지갑·컨트랙트·민팅·거버넌스)에 대한 end-to-end 소유권을 확보하고, 이후 블록체인 관련 의사결정에서 팀 내 레퍼런스 역할.

## 관련 증거

- **Jira** [GCPNFT-983](https://com2us.atlassian.net/browse/GCPNFT-983) — C2X NFT 디스코드 (Epic)
- **Jira** [GCPNFT-1401](https://com2us.atlassian.net/browse/GCPNFT-1401) — [DISCORD] 서비스 유지보수 및 개선 (Epic, 소유자)
- **Jira** [GCPNFT-1248](https://com2us.atlassian.net/browse/GCPNFT-1248) — C2XNFT 회계 데이터 시스템 구축 (Epic, 소유자)
- **Jira** [GCPNFT-1971](https://com2us.atlassian.net/browse/GCPNFT-1971) — 통합 로그인 시스템 개발 및 운영 (Epic, 소유자)
- **Jira** [CPBLOC-821](https://com2us.atlassian.net/browse/CPBLOC-821) / [CPBLOC-861](https://com2us.atlassian.net/browse/CPBLOC-861) / [CPBLOC-862](https://com2us.atlassian.net/browse/CPBLOC-862) — XPLA 웹뷰 NFT Mint / 리팩토링 / 다국어 (Sub-task)
- **Confluence** PNFTBD-51985462 — 디스코드 홀더 인증 봇 수집 데이터 정리 (2022-11-01)
- **프로젝트 문서**: [`../20-projects/com2us-platform/2022-05-nft-market.md`](../20-projects/com2us-platform/2022-05-nft-market.md)
- **원 시드**: `old-portfolio.md` "NFT 마켓 개발" 섹션 L176~183 ("스마트 컨트랙트 최적화를 통해 가스비를 90% 절감")
- **비고**: 가스비 90% 절감의 구체적 최적화 기법(저장 구조·이벤트 패킹 등)은 정성 서술 기반이며, 상세는 `private/jira/` 내부 아카이브 참조 (프로젝트 문서 §9 한계·메모).
