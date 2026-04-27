---
title: "pandas-dev (GitHub 조직)"
type: entity
entity_type: organization
tags: [pandas-dev, github-org, numfocus, bdfl, pdep, governance, oss-governance, wes-mckinney]
related: [[pandas]], [[numfocus]], [[pdep]], [[bdfl]], [[karpathy]], [[anthropic]], [[microsoft]], [[github]]
source_count: 1
created: 2026-04-27
updated: 2026-04-27
---

# pandas-dev (GitHub 조직)

## 개요

**pandas-dev**는 [[pandas]] 라이브러리와 그 부속 저장소들을 운영하는 GitHub 조직이다. 2015년 [[numfocus]] sponsored project로 공식화. 11개 저장소 운영, 활성 메인테이너 15명 + pandas-stubs 메인테이너 3명 + 비활성 메인테이너 20명, 2,000+ 컨트리뷰터.

URL: https://github.com/pandas-dev

## 주요 특징

### 산하 저장소

| 저장소 | 역할 |
|--------|------|
| **pandas** | 메인 라이브러리 (★91k+) |
| pandas-stubs | 공식 타입 스텁 |
| pandas-governance | 거버넌스 문서 |
| pandas-release | 릴리스 인프라 |
| pandas-compat | 다운스트림 호환성 |
| pandas-msgpack | (deprecated) msgpack 직렬화 |
| pandas-dev-flaker | flake8 플러그인 |
| pandas-user-surveys | 사용자 설문 |
| pandas-benchmarks | asv 벤치마크 환경 |
| asv-runner | 자동 벤치마크 러너 (GitHub Actions) |
| project-management | 프로젝트 관리 |
| .github | 조직 공통 GitHub 설정 (CODE_OF_CONDUCT 포함) |

### 거버넌스 모델 — 3축

#### 1. [[bdfl|BDFL]] (Benevolent Dictator for Life)

- 현재: **Wes McKinney**
- 권한: 모든 최종 결정에 대한 override 권한 ("special vote")
- 실제로는 거의 행사하지 않음 — Core Team consensus에 위임
- 후계자 지명 권한 보유, 못 할 경우 Core Team 2/3 vote (80% 참여)

#### 2. Core Team (15명, 2026-04-27)

자격 조건:
- Project Contributor로서 1년 이상 substantial contribution
- 기존 Core 멤버에 의해 nomination + Core Team vote

역할:
- 일상 의사결정 (PR 머지, 기술 방향)
- 기술 비전과 직접 결정
- consensus 달성 안 되는 사안의 중재

이탈: 1년 비활동 시 Core Team vote로 제거 가능 (BDFL이 사전 면담)

명시적 메트릭 거부: "We are deliberately not setting arbitrary quantitative metrics (like '100 commits in this repo') to avoid encouraging behavior that plays to the metrics rather than the project's overall well-being."

활성 메인테이너 (config.yml 기준): jorisvandenbossche, TomAugspurger, jreback, WillAyd, mroeschke, jbrockmendel, datapythonista, simonjayhawkins, topper-123, alimcmaster1, Dr-Irv, rhshadrach, phofl, attack68, fangchenli

#### 3. NumFOCUS Subcommittee (5명+)

- 자금 관리만 (NumFOCUS를 통한 기부금)
- **기술 방향에 관여 불가** — 명시적 분리
- 권력 집중 방지: "no more than 2 Subcommittee Members can report to one person (either directly or indirectly) through employment or contracting work"

### 4개 워크그룹 (subcommittees)

| 워크그룹 | 책임 | 컨택 |
|---------|------|------|
| **Code of Conduct** | 위반 신고 처리, CoC 유지 | coc@pandas.pydata.org |
| **Finance** | 펀딩, 그랜트, 프로젝트 지출 | finance@pandas.pydata.org |
| **Infrastructure** | 서버, 벤치마크, CI 인프라 | infrastructure@pandas.pydata.org |
| **Communications** | 소셜 네트워크 + NumFOCUS와 코어팀 사이 연락 | communications@pandas.pydata.org |

### Institutional Partners 시스템

기준: 조직이 직원으로서 적극적으로 contribute해야 함. 기부만으로는 Partner 자격 없음.

**Tier 1**: 1명 이상의 Institutional Core Team Member 보유 → 웹사이트/talks/T-shirt에 노출 + 자체 펀딩 출처 인지 + Core Team Member를 통한 영향력
**Tier 2**: 1명 이상의 Institutional Contributor 보유

활성 sponsors (2026-04-27): NumFOCUS (모회사) + Nvidia (Matthew Roeschke 풀타임 고용) + Tidelift (subscription) + Bodo (병렬 컴퓨팅 플랫폼)

In-kind: OVH (호스팅), Indeed (로고 디자인)

과거 institutional partners (10): Paris-Saclay, Anaconda, RStudio, Ursa Labs, Gousto, d-fine GmbH, Two Sigma, Voltron Data, Intel, Coiled

### [[pdep|PDEP]] (Pandas Enhancement Proposal) 시스템

PDEP-1이 메소드론 자체. Python의 PEP, NumPy의 NEP와 같은 가족.

**워크플로우**: Draft → Under discussion (60일) → Vote (15일) → Accepted/Rejected/Withdrawn → Implemented

**Quorum**: 11명 또는 voting 구성원의 50% 중 작은 값. **Majority**: non-abstaining의 70% 찬성.

**제출 절차**: PR로 `web/pandas/pdeps/` 디렉터리에 마크다운 추가.

**가버넌스 변경 자체도 PDEP**: 80% Core Team 참여 + 2/3 찬성 필요. BDFL은 단독 override 가능.

수집 시점 PDEP 11개: PDEP-1 (메타) / 4 / 5 / 6 / 7 (Copy-on-Write Implemented) / 8 / 9 / 10 (Required pyarrow) / 12 / 14 / 17.

### Copyright 모델

PyData shared copyright:
- 2008-2011: AQR Capital Management
- 2011-2012: Lambda Foundry (Wes의 두번째 직장)
- 2011-: PyData Development Team (집단 저자)
- "the PyData source code, in its entirety, is not the copyright of any single person or institution"

## 관련 개념

- [[pandas]]: 운영하는 라이브러리
- [[numfocus]]: 501(c)(3) 모회사 (PyData 생태계 비영리 후원)
- [[pdep]]: 거버넌스 산출물 시스템 (PEP의 pandas판)
- [[bdfl]]: 오픈소스 거버넌스 패턴 — pandas는 BDFL 단계에서 코어 팀 + PDEP 단계로 진화한 사례
- [[github]]: 인프라 호스트
- [[anthropic]] / [[microsoft]] / [[karpathy]]와의 비교: 거버넌스 모델이 본질적으로 다름

## 출처

- [[pandas-dev-pandas]] — pandas-dev/pandas + governance.md + about/, web/pandas/community/, web/pandas/pdeps/, config.yml, AUTHORS.md, AGENTS.md 통합 수집

## 메모

- pandas-dev의 거버넌스는 LLM 위키 운영 패턴의 후보 — [[bdfl|BDFL]](석근님) + Core Team(LLM) + [[numfocus|NumFOCUS]] Subcommittee(외부 도구 정책 위원회) 3축으로 매핑 가능.
- "BDFL ≠ 일상 메인테이너" 원칙: Wes McKinney도 일상 메인테이너 리스트에서는 inactive — 정치적 권위와 일상 운영 권한이 분리되는 패턴.
- 메트릭 게이밍 명시적 거부 — "100 commits" 같은 자의적 임계치를 두지 않음. 이는 [[autonomous-research-loop]]의 "메트릭 잠금"과 정반대 철학.
