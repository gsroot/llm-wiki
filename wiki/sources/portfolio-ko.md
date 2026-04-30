---
title: 포트폴리오 — 상세 포트폴리오(한국어, portfolio-ko.md)
type: source
source_type: note
source_url: ''
source_scope: local
raw_path: raw/notes/portfolio/docs/50-portfolio/portfolio-ko.md
author: 석근
date_published: 2026-04-24
date_ingested: 2026-04-24
tags:
- 포트폴리오
related:
- '[[seokgeun-kim]]'
- '[[com2us-platform]]'
- '[[c2spf-analytics]]'
- '[[portfolio-resume-ko]]'
confidence: high
inbound_count: 35
aliases:
- Portfolio Ko
- portfolio ko
- 포트폴리오 — 상세 포트폴리오(한국어, portfolio-ko.md)
cited_by:
  - "[[backend-python-fastapi]]"
  - "[[c2spf-analytics]]"
  - "[[career-timeline-seokgeun]]"
  - "[[com2us-platform]]"
  - "[[data-pipeline-bigquery]]"
  - "[[devops-cicd]]"
  - "[[frontend-react]]"
  - "[[matechat]]"
  - "[[ml-ai]]"
  - "[[portfolio]]"
  - "[[portfolio-resume-ko]]"
  - "[[seokgeun-kim]]"
  - "[[seokgeun-stack-guide]]"
cited_by_count: 13
---

# 포트폴리오 — 상세 포트폴리오(한국어, portfolio-ko.md)

## 한줄 요약

> "로그를 결정으로 바꾸는 시스템을 만듭니다." — 컴투스플랫폼 9년차 풀스택 엔지니어의 Selected Work 5선 + 정량 Impact 표 + 기술 스택 심화 설명을 엮은 상세 포트폴리오. 이력서보다 서사와 근거가 두텁다.

## 핵심 내용

- **캐치프레이즈** — 로그를 결정으로 바꾸는 시스템.
- **Impact 표** — 개발 경력 9년, c2spf 기여 1,111커밋, 공통 API 92% ownership, 프론트엔드 생산성 30~40% 향상 기반, 블록체인 프로젝트 5건(가스비 ~90% 절감 포함). 모든 수치는 `10-sources/*/INDEX.md`로 역링크.
- **Selected Work 5선**
 1. 애널리틱스 React 리뉴얼 (2025.06–) — `analytics-frontend` 476커밋, Vite/TS/TanStack/Zustand/ag-grid 스택 표준화, 2025 FE 가이드라인 문서화, GCPPDT-741/742 Story MR, 회귀 테스트 32/32·22/22 통과, 측정값 에러 8종 × 5개 로케일 i18n.
 2. Airbridge 데이터 가공 API (2025.01–02) — `/common/processed-data`에 MMP 결합·피벗팅, Spring Boot + FastAPI 하이브리드 파이프라인, APICode/ProcessedData 이원 에러 정책.
 3. 애널리틱스 공통 모듈 & 배포 (2024.08–) — `analytics-common-api` 231/251(92%), HIVE OAuth 8엔드포인트, Docker Compose + Jenkins 멀티브랜치, Promtail/Loki/Grafana 4환경, 배포/운영 가이드 4종 2024-10 집중 발행.
 4. XPLA 플랫폼 (2024.04–07) — NestJS + TypeORM + React 웹뷰, NFT 민팅 E2E, 중복 민팅·수수료 부족 엣지 케이스, CPBLOC 19건 완료.
 5. NFT 마켓 (2022.05–2024.03) — NFT 지갑 백엔드, Discord 홀더 인증 봇, Rust 투표 스마트 컨트랙트 가스비 ~90% 절감, Docker 배포 개선.
- **기술 스택 심화** — 8개 카테고리별 도구와 실무 맥락 설명 (Backend·Frontend·Data/ML·DevOps·Observability·Data Store·Blockchain·Mobile).

## 주요 인사이트

- Impact 표는 **재귀적 증거 구조**를 가짐: 각 수치 옆에 "[상세 ↗](...)" 링크로 즉시 근거 확인 가능. 외부 독자가 "진짜인가?"라는 의심을 바로 해소할 수 있도록 설계.
- Selected Work는 최근 5개 프로젝트로 한정해 **recency bias**를 의도적으로 활용 — 면접·채용 시 최신 기술(React/TS/ag-grid, Airbridge, Jenkins 멀티브랜치)에 대한 신뢰성 부여.
- 9년 경력이지만 "새로움" 메시지가 강함: 팀 최초 React 리뉴얼, LangGraph 앱 출시, AI 기반 개발 생산성 가이드 등.

## 관련 엔티티/개념

- [[seokgeun-kim|석근 (이 위키 owner)]] · [[com2us-platform|컴투스플랫폼 c2spf]] · [[c2spf-analytics|c2spf 게임 데이터 BI]] · [[xpla-platform]]
- [[backend-python-fastapi]] · [[frontend-react]] · [[data-pipeline-bigquery]] · [[devops-cicd]] · [[blockchain-xpla]] · [[ml-ai]]
- [[portfolio-resume-ko]] — 동일 내용 이력서 형태(2페이지)
- [[seokgeun-stack-guide|석근 32 OSS 스택 카탈로그]] — Selected Work 5선의 기술 스택(Vite·TanStack·Zustand·ag-grid·FastAPI·Spring Boot·Jenkins·Grafana 등)이 32 OSS 카탈로그의 6분류 의사결정 트리와 직접 매핑됨 (3축↔이 source 교차 인용)
- [[matechat]] — 회사 BI(c2spf-analytics)와 사이드 사업화(MateChat)의 쌍 검증 모델은 [[portfolio]] hub의 핵심 메시지이며, 본 source에 나열된 5개 프로젝트가 그 검증 환경 (4축↔이 source 교차 인용)

## 메모

- 원본 경로: `raw/notes/portfolio/docs/50-portfolio/portfolio-ko.md`.
- portfolio 저장소의 `portfolio-en.md`는 선택 프로젝트만 영어로 추려내므로 별도 수집하지 않음 (중복 방지).
