---
title: 컴투스플랫폼 (Com2usPlatform, c2spf)
type: entity
entity_type: organization
aliases:
- 컴투스플랫폼
- com2us-platform
- Com2us Platform
- c2spf
- com2us
tags:
- 컴투스플랫폼
- com2us-platform
- c2spf
- BI
related:
- '[[seokgeun-kim]]'
- '[[c2spf-analytics]]'
- '[[xpla-platform]]'
- '[[portfolio-seed]]'
- '[[portfolio-resume-ko]]'
- '[[portfolio-ko]]'
- '[[c2spf-nft-market]]'
- '[[c2spf-xpla-platform]]'
- '[[c2spf-analytics-common]]'
- '[[c2spf-analytics-renewal]]'
source_count: 6
observed_source_refs: 23
inbound_count: 42
created: 2026-04-24
updated: 2026-04-24
cited_by:
  - "[[c2spf-ai-agent-adoption-candidates]]"
  - "[[c2spf-analytics]]"
  - "[[c2spf-analytics-common]]"
  - "[[c2spf-analytics-renewal]]"
  - "[[c2spf-nft-market]]"
  - "[[c2spf-xpla-platform]]"
  - "[[matechat]]"
  - "[[portfolio-ko]]"
  - "[[portfolio-resume-ko]]"
  - "[[portfolio-seed]]"
  - "[[scikit-learn-scikit-learn]]"
  - "[[seokgeun-kim]]"
  - "[[seokgeun-stack-guide]]"
  - "[[xpla-platform]]"
cited_by_count: 14
---

# 컴투스플랫폼 (Com2usPlatform, c2spf)

## 개요

컴투스 그룹의 게임 플랫폼 자회사. 사내 GitHub 조직 핸들은 `c2spf`. 다수의 모바일/PC 게임에 공통 기능(인증, 결제, 데이터 분석, 블록체인, 광고 트래킹 등)을 SDK·플랫폼 형태로 제공한다. 김석근(석근)이 2017-05부터 현재까지 백엔드/풀스택으로 재직 중인 회사.

## 주요 특징

- **GitHub 조직**: [c2spf](https://github.com/c2spf) — 다수의 분석/플랫폼 레포 운영.
- **주요 서비스 라인**
  - **애널리틱스(BI)** — `c2spf/analytics-*` 레포 군. 게임 로그 수집·분석·시각화. → [[c2spf-analytics|c2spf 게임 데이터 BI]]
  - **블록체인 플랫폼 (XPLA)** — NFT 마켓·민팅·지갑·트랜잭션 SDK. → [[xpla-platform]]
  - **CODE 트래블룰 API** — 가상자산 거래소 트래블룰 공통 API.
- **사내 도구**
  - Jira: 프로젝트 키 `GCPPDT*`, `GCPNFT`, `GCPSRE`, `GCPHDBA`, `GCPPDTDW`, `CPBLOC` 등.
  - Confluence: 페이지 ID 35568xxx 등으로 공통 모듈/배포/운영 가이드 관리.
  - HIVE OAuth — 토큰·사용자·메뉴 권한·게임 권한을 8개 엔드포인트로 노출하는 사내 인증 시스템.

## 관련 개념

- [[c2spf-analytics|c2spf 게임 데이터 BI]] — 회사의 핵심 BI 서비스
- [[xpla-platform]] — 블록체인 통합 플랫폼
- [[seokgeun-kim|석근 (이 위키 owner)]] — 재직자, 위키 소유자
- [[backend-python-fastapi]] · [[devops-cicd]] · [[data-pipeline-bigquery]] · [[blockchain-xpla]] — 회사에서 활용되는 핵심 기술

## 출처

- [[portfolio-seed]] — 회사 재직 기간 동안의 프로젝트 전체 개요
- [[portfolio-resume-ko]] · [[portfolio-ko]] — 회사 프로젝트 정량 지표
- [[c2spf-nft-market]] — NFT 마켓 프로젝트
- [[c2spf-xpla-platform]] — XPLA 플랫폼 프로젝트
- [[c2spf-analytics-common]] — 애널리틱스 공통 모듈
- [[c2spf-analytics-renewal]] — Airbridge API + React 리뉴얼

## 논쟁/모순

(없음)

## 메모

- 사내 자료(Jira 티켓 본문, Confluence 페이지 원문, Google Drive 문서)는 민감도 때문에 portfolio 저장소의 `private/` 폴더에만 보존됨. llm-wiki에는 복사하지 않음.
- 본인의 회사 GitHub 활동은 `gsroot` 계정 기준 `c2spf` 조직 내 누적 1,111커밋 (2026-04 시점).
