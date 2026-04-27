---
title: "컴투스플랫폼 Jira 티켓 인덱스"
type: source-index
company: com2us-platform
source: jira
collected_at: "2026-04-24"
---

# Jira — 티켓 인덱스

컴투스플랫폼 Atlassian 워크스페이스(`com2us.atlassian.net`)에서 수집한 내 Jira 티켓의 **공개 인덱스**. 개별 티켓 본문(민감 정보 포함 가능)은 `/private/jira/`에만 저장되며 Git에는 포함되지 않음.

## 수집 상태

- 수집일: **2026-04-24**
- 조회 범위: `assignee = currentUser() OR reporter = currentUser()`
- 기간: `2022-01-01` ~ 현재 (약 4.3년)
- 총 티켓 수: **636건**
- 수집 방식: `mcp__plugin_atlassian_atlassian__searchJiraIssuesUsingJql` (7페이지 커서 페이지네이션)

## 프로젝트별 요약

| 키 | 프로젝트명 | 총 | Done | In Progress | To Do | 상세 |
|----|-----------|---:|-----:|-----------:|------:|------|
| `GCPNFT`   | GCP_Web3 (Web3/NFT/Discord)                  | 231 | 229 | 1 | 1 | [주요 티켓](./tickets-by-project.md#gcpnft) |
| `GCPSRE`   | CP_IEP (SRE / 인프라 요청)                   | 170 | 169 | 0 | 1 | [주요 티켓](./tickets-by-project.md#gcpsre) |
| `GCPPDTDW` | 애널리틱스 개발 파트                         | 128 | 125 | 1 | 2 | [주요 티켓](./tickets-by-project.md#gcppdtdw) |
| `GCPPDT`   | AI개발2실 (이벤트 애널리틱스 / CODE 트래블룰) |  66 |  30 | 36 | 0 | [주요 티켓](./tickets-by-project.md#gcppdt) |
| `CPBLOC`   | CP_Blockchain (XPLA 웹 지갑/NFT)             |  19 |  19 | 0 | 0 | [주요 티켓](./tickets-by-project.md#cpbloc) |
| `GCPHDBA`  | CP_IEP_DBA (DB 서버 요청)                    |  16 |  16 | 0 | 0 | [주요 티켓](./tickets-by-project.md#gcphdba) |
| `GCPPDE`   | 데이터 아키텍트 파트                         |   3 |   3 | 0 | 0 | [주요 티켓](./tickets-by-project.md#gcppde) |
| `GCPPDG`   | CP_Developers_Guide                          |   1 |   1 | 0 | 0 | — |
| `GCPPDTET` | ETL파트                                      |   1 |   1 | 0 | 0 | — |
| `PTFTCQ`   | CP_TFT QA                                    |   1 |   1 | 0 | 0 | — |

- **총합**: 636건 (Done 593 / In Progress 38 / To Do 4 / Backlog 2 그 외 Hold·Deploy·QA 포함)
- In Progress가 특히 많은 프로젝트: `GCPPDT` (이벤트 애널리틱스 현재 진행 중인 Story 다수)

## 이슈 타입 분포

| 타입 | 건수 |
|------|---:|
| 부작업 (Sub-task) | 207 |
| 하위 작업 | 134 |
| 설정 | 132 |
| 작업 (Task) | 96 |
| 설치 | 31 |
| 스토리 (Story) | 23 |
| 에픽 (Epic) | 5 |
| 버그 | 3 |
| 기타/설치/계정/기술지원 | 5 |

## 프로젝트 클러스터 매핑

프로젝트 키별로 대응되는 상위 포트폴리오 프로젝트 클러스터:

- **애널리틱스 (Hive Analytics / 이벤트 애널리틱스)**
  - `GCPPDTDW` · `GCPPDT` · `GCPPDE` · `GCPPDTET`
  - 포트폴리오: `/docs/20-projects/com2us-platform/hive-analytics*.md`, `/docs/20-projects/com2us-platform/event-analytics*.md`
- **Web3 / 블록체인 (XPLA · C2X · 트래블룰)**
  - `GCPNFT` · `CPBLOC`
  - 포트폴리오: `/docs/20-projects/com2us-platform/xpla-wallet*.md`, `/docs/20-projects/com2us-platform/c2x-nft*.md`, `/docs/20-projects/com2us-platform/code-travelrule*.md`
- **인프라 / DB 요청 (SRE · DBA)**
  - `GCPSRE` · `GCPHDBA`
  - 참고: 서비스 릴리스 시 인프라 요청 티켓. 위 애널리틱스/블록체인 프로젝트에 종속.
- **QA / 기타**
  - `GCPPDG` · `PTFTCQ`

## 수집 방법

1. cloudId: `02dc5221-53cc-4881-b640-73ee791a453d` (`com2us.atlassian.net`) 획득
2. JQL (각 페이지마다 `updated < "<이전 페이지 마지막 updated>"`로 커서 이동):
   ```
   (assignee = currentUser() OR reporter = currentUser())
   AND updated >= "2022-01-01"
   AND updated < "<cursor>"
   ORDER BY updated DESC
   ```
3. 7페이지 × 100건 (마지막 36건) = 총 636건 수집, 키로 중복 제거
4. Epic/Story 우선 + 프로젝트 대표성 기준으로 22개 티켓을 선정하여 `getJiraIssue`로 상세 수집
5. 상세는 `/private/jira/<KEY>.md` 에 YAML frontmatter + 본문 저장 (Git 제외)

## 주요 티켓

프로젝트별 대표 티켓(Epic/Story 우선)은 [`tickets-by-project.md`](./tickets-by-project.md) 참조.
