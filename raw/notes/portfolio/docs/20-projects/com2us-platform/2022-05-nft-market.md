---
title: "NFT 마켓 (지갑 관리, Discord 홀더 인증, 투표 스마트 컨트랙트)"
type: project
company: com2us-platform
period: "2022-05 ~ 2024-03"
role: "NFT 지갑 백엔드, Discord 봇 통합, 스마트 컨트랙트, 배포 개선"
tech_stack:
  - Node.js
  - NestJS
  - TypeORM
  - Python
  - Discord.py
  - FastAPI
  - Pytest
  - Rust
  - TypeScript
  - MySQL
  - Redis
  - Docker
  - Fluentd
  - ElasticSearch
  - Kibana
sources:
  jira:
    - key: GCPNFT-983
      title: "C2X NFT 디스코드 (Epic)"
      url: "https://com2us.atlassian.net/browse/GCPNFT-983"
      path: "private/jira/GCPNFT-983.md"
    - key: GCPNFT-1401
      title: "[DISCORD] 서비스 유지보수 및 개선 (Epic)"
      url: "https://com2us.atlassian.net/browse/GCPNFT-1401"
      path: "private/jira/GCPNFT-1401.md"
    - key: GCPNFT-1248
      title: "C2XNFT 회계 데이터 시스템 구축 (Epic)"
      url: "https://com2us.atlassian.net/browse/GCPNFT-1248"
      path: "private/jira/GCPNFT-1248.md"
    - key: GCPNFT-1971
      title: "통합 로그인 시스템 개발 및 운영 (Epic)"
      url: "https://com2us.atlassian.net/browse/GCPNFT-1971"
      path: "private/jira/GCPNFT-1971.md"
    - key: CPBLOC-821
      title: "Mint (Sub-task, XPLA NFT Mint)"
      url: "https://com2us.atlassian.net/browse/CPBLOC-821"
      path: "private/jira/CPBLOC-821.md"
    - key: CPBLOC-861
      title: "코드 리팩토링 및 버그 수정 (Sub-task)"
      url: "https://com2us.atlassian.net/browse/CPBLOC-861"
      path: "private/jira/CPBLOC-861.md"
    - key: CPBLOC-862
      title: "다국어 적용 (Sub-task)"
      url: "https://com2us.atlassian.net/browse/CPBLOC-862"
      path: "private/jira/CPBLOC-862.md"
  confluence:
    - page_id: "51985462"
      space: PNFTBD
      title: "디스코드 홀더 인증 봇 수집 데이터 정리"
      updated: "2022-11-01"
      note: "인덱스 수록(본문 미수집) — NFT Discord 홀더 인증 봇 DB 스키마 정리"
  github: []
  gmail: []
tags: [blockchain, nft, discord, smart-contract, rust, nestjs, xpla, c2x]
metrics:
  - "NFT 홀더 인증 기능 단기 상용화 (Discord 봇 기반)"
  - "투표 스마트 컨트랙트 최적화로 가스비 약 90% 절감 (old-portfolio.md 기준)"
  - "컨테이너 배포 프로세스 개선으로 배포 효율성·생산성 향상"
  - "GCPNFT 프로젝트 누적 티켓 231건 중 Done 229건 (2022-05 ~ 2025-08)"
related_projects:
  - "2021-10-code-travel-rule-api"
  - "2024-04-xpla-platform"
star:
  situation: "2022년 하반기 C2X(Web3) 생태계 확장 국면에서 NFT 지갑 관리·커뮤니티 인증·거버넌스(투표)·회계 데이터 수집·통합 로그인까지 블록체인 도메인 전반을 커버하는 플랫폼이 필요했다. 특히 Discord 커뮤니티 내 NFT 홀더 인증과 투표(거버넌스)의 온체인 구현이 단기간에 요구되었다."
  task: "(1) NFT 지갑 관리 백엔드(NestJS/TypeORM), (2) Discord 봇 기반 NFT 홀더 인증(Python Discord.py + FastAPI), (3) Rust 기반 투표 스마트 컨트랙트와 가스비 최적화, (4) Docker 기반 배포 프로세스 개선, (5) C2XNFT 회계 데이터 시스템 및 통합 로그인 시스템 유지보수를 순차·병행 담당."
  action: "NestJS/TypeORM으로 지갑·NFT 메타데이터 도메인을 모델링하고 Redis 캐시와 Fluentd→ElasticSearch→Kibana 로깅 파이프라인을 연결. Discord 봇은 Python Discord.py + FastAPI로 인증 엔드포인트를 분리하고 Pytest로 회귀를 보장. 투표 컨트랙트는 Rust/TypeScript 환경(XPLA 계열)에서 저장 구조·이벤트 발행을 재설계해 가스비를 대폭 절감. 배포는 Docker 컨테이너 구성·이미지 빌드·릴리스 절차를 표준화했고, GCPNFT-1248(C2XNFT 회계 데이터 시스템)과 GCPNFT-1971(통합 로그인 시스템) Epic을 소유자로 운영했다. CPBLOC Sub-task(Mint/리팩토링/다국어)에서는 XPLA 웹뷰 NFT Mint 플로우(중복 민팅·수수료 부족 처리·tx 서명/전송/결과 페이지)를 직접 구현하며 블록체인-프론트 연결을 다졌다."
  result: "짧은 기간에 NFT 홀더 인증 기능을 상용화해 다양한 인증 방식 확장 가능성을 제시했고, 투표 스마트 컨트랙트 최적화로 가스비 ~90% 절감(old-portfolio.md 기준)하여 사용자 비용을 낮췄다. 컨테이너 기반 배포 개선으로 배포 효율성·생산성이 향상되었고, GCP_Web3 프로젝트(GCPNFT) 231건 중 229건이 Done 상태로 완료되었다(2025-08 기준). 본 프로젝트의 Discord/지갑/민팅 경험이 이후 XPLA 플랫폼(2024-04)으로 자연스럽게 이어졌다."
---

# NFT 마켓 (지갑 관리, Discord 홀더 인증, 투표 스마트 컨트랙트)

> 컴투스플랫폼 Web3/블록체인 시리즈 중 가장 장기(22개월) 프로젝트. Jira `GCPNFT` 프로젝트(GCP_Web3, 231건)와 `CPBLOC` 프로젝트(CP_Blockchain, 19건)에 걸쳐 진행됨.

## 1. 개요

- **기간**: 2022-05 ~ 2024-03 (22개월)
- **팀/소속**: GCP_Web3 (NFT/Discord/블록체인)
- **역할 요약**
  - NFT 지갑 관리 백엔드 개발 (NestJS, TypeORM)
  - Discord 봇 기능 통합 — NFT 홀더 인증 등 (Python Discord.py, FastAPI, Pytest)
  - 투표 스마트 컨트랙트 개발 (Rust / TypeScript)
  - 컨테이너 기반 배포 프로세스 개선 (Docker)
  - C2XNFT 회계 데이터 시스템 / 통합 로그인 시스템 Epic 소유·운영
- **도메인**: Web3, NFT, 커뮤니티 인증(Discord), 온체인 거버넌스(투표), 지갑·민팅

## 2. 핵심 성과 (Metrics)

| 지표 | 값 | 출처 |
|------|-----|------|
| NFT 홀더 인증 기능 상용화 | 단기 상용화 | `old-portfolio.md` "NFT 마켓 개발" |
| 투표 스마트 컨트랙트 가스비 절감 | **약 90%** | `old-portfolio.md` "NFT 마켓 개발" |
| 배포 효율성·생산성 | 컨테이너 관리 방식 개선으로 향상 | `old-portfolio.md` |
| GCPNFT 티켓 처리 (누적) | 231건 / Done 229 | `docs/10-sources/com2us-platform/jira/INDEX.md` |
| Epic 소유 | 3건 (GCPNFT-1401, GCPNFT-1248, GCPNFT-1971) | Jira |

## 3. 시스템 구성

### 3.1 구성 요소

- **NFT 지갑 관리 백엔드 (NestJS + TypeORM + MySQL)**
  - 지갑/NFT 메타데이터 도메인 모델
  - Redis 캐시로 조회 경로 최적화
  - Fluentd 로그 수집 → ElasticSearch → Kibana 대시보드
- **Discord 홀더 인증 봇 (Python: Discord.py + FastAPI + Pytest)**
  - NFT 보유 여부 확인 → Discord 역할(Role) 부여
  - 인증 수집 데이터는 별도 스키마로 정리 (Confluence PNFTBD-51985462 "디스코드 홀더 인증 봇 수집 데이터 정리")
- **투표 스마트 컨트랙트 (Rust + TypeScript)**
  - XPLA 계열 Rust 컨트랙트로 거버넌스/투표 구현
  - 저장 구조·이벤트 설계 최적화로 가스비 대폭 절감
- **XPLA NFT Mint 플로우 (CPBLOC)**
  - 중복 민팅 처리, 수수료 부족 처리, Action/수수료 정보 노출
  - tx 생성·서명·전송·결과 페이지까지 E2E 흐름 구현 (CPBLOC-821 Mint)
- **C2XNFT 회계 데이터 시스템 (GCPNFT-1248 Epic)**
  - 블록체인 온체인 트랜잭션 → 회계 시스템 데이터 파이프라인
- **통합 로그인 시스템 (GCPNFT-1971 Epic)**
  - C2X/Web3 서비스 전반 공통 인증

### 3.2 배포 / 관측

- **Docker** 컨테이너 빌드·배포 표준화 (배포 프로세스 개선의 핵심)
- **Fluentd / ElasticSearch / Kibana** 로그 파이프라인
- **MySQL / Redis** — 메인 DB + 캐시
- `GCPHDBA-1245` "블록체인 웹 지갑 상용 DB 서버신청" (2022-07-28)을 통해 MySQL 8 MASTER-SLAVE 구성 도입

## 4. 주요 작업 타임라인

| 시점 | 이벤트 | 근거 |
|------|--------|------|
| 2022-05 | NFT 마켓 프로젝트 착수 | old-portfolio.md |
| 2022-07 | 블록체인 웹 지갑 상용 DB 서버 신청 (MySQL 8 M-S) | GCPHDBA-1245 |
| 2022-09~10 | C2X NFT 디스코드 설정 및 오픈 (붕어빵 10/11 12시 KST) | GCPNFT-983 |
| 2022-11 | Discord 홀더 인증 봇 수집 데이터 스키마 정리 | Confluence PNFTBD-51985462 |
| 2023 | Discord 서비스 유지보수·개선 지속 (Epic) | GCPNFT-1401 |
| 2024-03 | NFT 마켓 프로젝트 종료 (XPLA 플랫폼으로 전환) | old-portfolio.md |
| 2024-07~08 | XPLA 웹 지갑 Mint/리팩토링/다국어 (후속) | CPBLOC-821/861/862 |
| 2025-08 | GCPNFT 관련 Epic 최종 Done | GCPNFT-1401/1248/1971 |

## 5. 근거 자료 (Evidence)

### 5.1 Jira — GCPNFT (GCP_Web3)

| 키 | 제목 | 타입 | 상태 | 업데이트 |
|----|------|------|------|----------|
| [GCPNFT-983](https://com2us.atlassian.net/browse/GCPNFT-983) | C2X NFT 디스코드 | 에픽 | Done | 2022-11-25 |
| [GCPNFT-1401](https://com2us.atlassian.net/browse/GCPNFT-1401) | [DISCORD] 서비스 유지보수 및 개선 | 에픽 | Done | 2025-08-20 |
| [GCPNFT-1248](https://com2us.atlassian.net/browse/GCPNFT-1248) | C2XNFT 회계 데이터 시스템 구축 | 에픽 | Done | 2025-08-20 |
| [GCPNFT-1971](https://com2us.atlassian.net/browse/GCPNFT-1971) | 통합 로그인 시스템 개발 및 운영 | 에픽 | Done | 2025-08-20 |

### 5.2 Jira — CPBLOC (CP_Blockchain, XPLA 웹뷰 연동 작업)

| 키 | 제목 | 타입 | 상태 | 업데이트 |
|----|------|------|------|----------|
| [CPBLOC-821](https://com2us.atlassian.net/browse/CPBLOC-821) | Mint (NFT 민팅 E2E 플로우) | 부작업 | Done | 2024-07-30 |
| [CPBLOC-861](https://com2us.atlassian.net/browse/CPBLOC-861) | 코드 리팩토링 및 버그 수정 | 부작업 | Done | 2024-08-02 |
| [CPBLOC-862](https://com2us.atlassian.net/browse/CPBLOC-862) | 다국어 적용 (요청자) | 부작업 | Done | 2024-08-27 |

> CPBLOC은 Epic/Story 없이 Sub-task 기반으로 관리된 XPLA 웹 지갑 FE/NFT Mint 플로우 작업(총 19건, 전부 Done). 본 프로젝트 말기(2024-03) 이후 XPLA 플랫폼(2024-04-xpla-platform.md)으로 연결되는 가교 역할.

### 5.3 Confluence — PNFTBD (Tech Business Division)

- **디스코드 홀더 인증 봇 수집 데이터 정리** (page id `51985462`, 2022-11-01)
  - NFT Discord 홀더 인증 봇의 **DB 스키마/수집 데이터** 정리 문서
  - 위치: `docs/10-sources/com2us-platform/confluence/pages-by-space.md` PNFTBD 섹션
  - 본문은 수집 대상 외(인덱스 수록)

### 5.4 GitHub / Gmail

- GitHub: `c2spf` 조직에 직접 매칭되는 리포 없음(블록체인 전용 조직 가능성). 추가 조사 보류.
- Gmail: 없음.

## 6. STAR 요약

- **S (Situation)**: C2X Web3 생태계 확장으로 NFT 지갑 관리·Discord 커뮤니티 인증·온체인 거버넌스(투표)·회계 데이터 수집·통합 로그인까지 블록체인 도메인 전반이 단기간에 요구됨.
- **T (Task)**: 지갑 백엔드(NestJS), Discord 봇(Python), 투표 컨트랙트(Rust), 컨테이너 배포 개선, C2XNFT 회계/통합 로그인 시스템 운영을 동시에 담당.
- **A (Action)**: NestJS/TypeORM 도메인 모델링 + Redis 캐시 + Fluentd→ES→Kibana 관측. Discord 홀더 인증 봇(Discord.py + FastAPI, Pytest 회귀)과 DB 스키마 정리. Rust 컨트랙트 저장 구조·이벤트 최적화로 가스비 절감. Docker 컨테이너 빌드·배포 표준화. CPBLOC Sub-task에서 XPLA NFT Mint E2E 플로우(민팅 중복·수수료 부족 처리·tx 서명/전송/결과) 구현.
- **R (Result)**: **NFT 홀더 인증 단기 상용화**, **가스비 ~90% 절감**(old-portfolio.md 인용), **배포 효율성·생산성 향상**, GCP_Web3 티켓 229/231건 Done, XPLA 플랫폼(2024-04)으로 연결되는 토대 마련.

## 7. 연관 프로젝트

- **이전**: [2021-10 CODE 트래블룰 API](../2021-10-code-travel-rule-api.md) — Web3 규제/인프라 경험의 선행 프로젝트
- **이후**: [2024-04 XPLA 플랫폼](./2024-04-xpla-platform.md) — 본 프로젝트의 지갑/Mint 경험이 XPLA 웹 지갑으로 이어짐 (CPBLOC 후반 Sub-task가 이 전환의 증거)

## 8. 기술 스택 (정규화)

- **Backend**: Node.js, NestJS, TypeORM, Python (Discord.py, FastAPI, Pytest)
- **Smart Contract**: Rust, TypeScript (XPLA 계열 Cosmos SDK / Web3 환경)
- **Data**: MySQL (8, MASTER-SLAVE), Redis
- **Observability**: Fluentd, ElasticSearch, Kibana
- **DevOps**: Docker (컨테이너 배포 개선)

## 9. 한계·메모

- Confluence PNFTBD-51985462 본문은 미수집 상태(인덱스만 존재). DB 스키마 세부는 원문 확인 필요.
- 스마트 컨트랙트 가스비 90% 절감의 구체적 최적화 기법(저장 구조·이벤트 패킹 등)은 `old-portfolio.md`에 서술된 정성 지표로, 원시 측정 자료는 별도 아카이브 대상.
- GitHub c2spf 조직 직속 리포가 확인되지 않아, 이후 블록체인 전용 조직(c2x/xpla 등) 존재 가능성에 대한 추가 조사 필요.
