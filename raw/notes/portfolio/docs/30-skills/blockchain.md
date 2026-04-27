---
title: "Blockchain / Web3"
type: skill
category: blockchain
slug: blockchain
years_of_experience: 3
proficiency: proficient
related_stack: [Smart Contract, NFT, Rust, Discord.py, Web3, Travel Rule, XPLA, C2X]
tags: [blockchain, web3, nft, smart-contract, rust]
---

# Blockchain / Web3

## 개요

CODE 트래블룰 API(가상자산 규제 대응 업계 초기 구현), NFT 마켓(Discord 홀더 인증 상용화 + 투표 스마트 컨트랙트 가스비 ~90% 절감), XPLA 플랫폼(게임 SDK용 지갑·NFT 민팅 공통 서비스) 등 **3개 블록체인/Web3 프로젝트에 걸쳐 약 3년** 경험을 보유. 규제 대응, 온체인 거버넌스, 지갑·민팅 E2E 플로우를 관통하는 풀스택 범위를 소화했다.

## 프로젝트 증거

| 프로젝트 | 기간 | 역할 | 링크 |
|---------|------|------|------|
| CODE 트래블룰 API (라이트닝) | 2021-10 ~ 2022-06 | 프로젝트 **전담 리더** — 웹/블록체인 API 설계·구현, Sample VASP API, 관리 대시보드 | [→](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) |
| NFT 마켓 (지갑·Discord 홀더 인증·투표 컨트랙트) | 2022-05 ~ 2024-03 | NFT 지갑 백엔드, Discord 봇 통합, Rust 스마트 컨트랙트, 배포 개선 | [→](../20-projects/com2us-platform/2022-05-nft-market.md) |
| XPLA 플랫폼 | 2024-04 ~ 2024-07 | 시스템 설계·API 정의·풀스택, 게임 SDK용 지갑/민팅 기능 제공 | [→](../20-projects/com2us-platform/2024-04-xpla-platform.md) |

## 서브 스택 숙련도

| 스택 | 숙련도 | 근거 |
|------|--------|------|
| Smart Contract (Rust/XPLA·Cosmos 계열) | proficient | 투표 컨트랙트 저장 구조·이벤트 설계 최적화로 **가스비 ~90% 절감** (old-portfolio.md 인용) |
| NFT | proficient | 지갑·메타데이터 도메인 모델링 + Mint E2E 플로우(CPBLOC-821) 구현 |
| Rust | competent | NFT 투표 스마트 컨트랙트(XPLA 계열) 개발 |
| Discord.py + FastAPI | proficient | NFT 홀더 인증 봇 — 역할 부여 로직, Pytest 회귀 (Confluence PNFTBD-51985462) |
| Travel Rule 규제 대응 | proficient | 가상자산 트래블룰 공통 API **업계 초기 구현**, WebSocket 기반 거래소 간 통신 샘플 SDK(NodeJS/Java Spring) 제공 |
| XPLA / C2X 생태계 | proficient | 지갑 DB 인프라(GCPHDBA-1245) 요청자부터 SDK 레이어까지 연속 경험 |
| Web3 주변 (지갑 관리, 온체인 tx 서명/전송, 수수료 처리) | proficient | XPLA 웹뷰 Mint 플로우에서 중복 민팅·수수료 부족 가드 직접 구현 |

## 대표 성과

- **투표 스마트 컨트랙트 가스비 ~90% 절감** — Rust 저장 구조·이벤트 발행 재설계 (old-portfolio.md 인용, 2022~2024 NFT 마켓)
- **NFT 홀더 인증 기능 단기 상용화** — Discord.py 봇 기반, 다양한 인증 방식 확장 가능성 제시 (old-portfolio.md 인용)
- **CODE 트래블룰 API 전담 리드** — 가상자산 규제 대응 업계 초기 구현, travelrule-api 레포 **135커밋**(전체 507의 ~27%), Sphinx/reStructuredText 공식 문서 + Locust 로드 테스트 + NodeJS/Java Spring 샘플 SDK 설계
- **XPLA 플랫폼 CPBLOC 19건 전수 Done** — NFT 민팅 tx 조회·서명·전송·결과 E2E 플로우 단일 담당자로 주도 (CPBLOC-821)
- **GCP_Web3 누적 229/231건 Done** — Epic 3건(GCPNFT-1401 Discord 유지보수, GCPNFT-1248 C2XNFT 회계 데이터 시스템, GCPNFT-1971 통합 로그인) 소유

## 관련 인용 출처

- [old-portfolio.md](../../old-portfolio.md) — 가스비 90% 절감, NFT 홀더 인증 상용화 원문
- GitHub: [`c2spf/travelrule-api`](../10-sources/com2us-platform/github-c2spf/repos/travelrule-api.md) (135커밋 / 507, 2021-11 ~ 2022-06)
- Confluence PNFTBD-51985462 (디스코드 홀더 인증 봇 수집 데이터 정리)
- Jira: GCPNFT-983/1401/1248/1971 (Epic), CPBLOC-821/861/862 (XPLA Mint·리팩토링·다국어), GCPHDBA-1245 (블록체인 웹 지갑 상용 DB)
