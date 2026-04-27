---
title: "컴투스플랫폼 Jira 주요 티켓 (프로젝트별)"
type: source-tickets
company: com2us-platform
source: jira
collected_at: "2026-04-24"
---

# Jira — 프로젝트별 주요 티켓

Phase B에서 선정한 대표 티켓 목록. 전체 636건 중 Epic/Story 우선으로 22건을 선정해 상세 본문은 `/private/jira/<KEY>.md`로 저장함. 이 문서에는 공개해도 무방한 메타(키/제목/타입/상태/최신 업데이트)만 담음.

## 정렬/표기 기준

- 각 프로젝트 섹션 내에서 `updated desc`
- `타입` 열: 원문 한국어 타입 그대로 (에픽, 스토리, 부작업, 설치, 설정)
- `상태` 열: Done = 완료, In Progress = 진행 중, QA = QA, To Do = 해야 할 일

## <a id="gcpnft"></a>GCPNFT — GCP_Web3 (Web3 / NFT / Discord)

총 231건 · Done 229 · In Progress 1 · To Do 1

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPNFT-1971](https://com2us.atlassian.net/browse/GCPNFT-1971) | 통합 로그인 시스템 개발 및 운영       | 에픽 | Done | 2025-08-20 |
| [GCPNFT-1401](https://com2us.atlassian.net/browse/GCPNFT-1401) | [DISCORD] 서비스 유지보수 및 개선     | 에픽 | Done | 2025-08-20 |
| [GCPNFT-1248](https://com2us.atlassian.net/browse/GCPNFT-1248) | C2XNFT 회계 데이터 시스템 구축        | 에픽 | Done | 2025-08-20 |
| [GCPNFT-983](https://com2us.atlassian.net/browse/GCPNFT-983)   | C2X NFT 디스코드                      | 에픽 | Done | 2022-11-25 |

## <a id="gcpsre"></a>GCPSRE — CP_IEP (SRE 인프라)

총 170건 · Done 169 · To Do 1

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPSRE-16239](https://com2us.atlassian.net/browse/GCPSRE-16239) | [애널리틱스] 애널리틱스 공통 api 서버 nginx 설정 변경 요청 | 설정 | Done | 2025-07-08 |
| [GCPSRE-15853](https://com2us.atlassian.net/browse/GCPSRE-15853) | [애널리틱스] v2 서버 패키지 설치 요청                      | 설치 | Done | 2025-05-09 |

SRE 티켓은 대부분 nginx/docker/패키지 설치 요청으로 작업 패턴이 반복됨 (요청자=본인).

## <a id="gcppdtdw"></a>GCPPDTDW — 애널리틱스 개발 파트

총 128건 · Done 125 · In Progress 1 · To Do 2

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPPDTDW-2386](https://com2us.atlassian.net/browse/GCPPDTDW-2386) | 공통 API - 2025                          | 스토리 | Done        | 2026-04-15 |
| [GCPPDTDW-2114](https://com2us.atlassian.net/browse/GCPPDTDW-2114) | 유저 활동 추적 - 2025                    | 스토리 | Done        | 2025-12-02 |
| [GCPPDTDW-2365](https://com2us.atlassian.net/browse/GCPPDTDW-2365) | 애널리틱스 프런트 엔드 개선              | 스토리 | In Progress | 2025-11-17 |
| [GCPPDTDW-412](https://com2us.atlassian.net/browse/GCPPDTDW-412)   | 세그먼트 생성 API View 개발              | 스토리 | Done        | 2023-02-02 |
| [GCPPDTDW-260](https://com2us.atlassian.net/browse/GCPPDTDW-260)   | 세그먼트 생성 API 기능 개발              | 스토리 | Done        | 2023-02-02 |

## <a id="gcppdt"></a>GCPPDT — AI개발2실 (이벤트 애널리틱스 · CODE 트래블룰)

총 66건 · Done 30 · In Progress 36

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPPDT-742](https://com2us.atlassian.net/browse/GCPPDT-742) | [이벤트 애널리틱스] 차트 테이블 가독성 개선             | 스토리 | In Progress | 2026-04-23 |
| [GCPPDT-741](https://com2us.atlassian.net/browse/GCPPDT-741) | [이벤트 애널리틱스] 차트 시각화 및 측정값 편집 UX 개선 | 스토리 | In Progress | 2026-04-23 |
| [GCPPDT-638](https://com2us.atlassian.net/browse/GCPPDT-638) | 지표 템플릿 기능 적용                                  | 스토리 | QA          | 2026-03-30 |
| [GCPPDT-639](https://com2us.atlassian.net/browse/GCPPDT-639) | 대시보드 기능 개선                                     | 스토리 | QA          | 2026-03-25 |
| [GCPPDT-167](https://com2us.atlassian.net/browse/GCPPDT-167) | [CODE 트래블룰] 모니터링할 장애 케이스 목록 정리       | 스토리 | Done        | 2025-08-20 |

이 프로젝트는 현재 진행 중인 Story 비중이 가장 높음 (AG-Grid 컬럼 UX, 파이 차트 다중 측정값, 측정값 연산식 검증 등).

## <a id="cpbloc"></a>CPBLOC — CP_Blockchain (XPLA 웹 지갑 / NFT Mint)

총 19건 · Done 19

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [CPBLOC-862](https://com2us.atlassian.net/browse/CPBLOC-862) | 다국어 적용                        | 부작업 | Done | 2024-08-27 |
| [CPBLOC-861](https://com2us.atlassian.net/browse/CPBLOC-861) | 코드 리팩토링 및 버그 수정         | 부작업 | Done | 2024-08-02 |
| [CPBLOC-821](https://com2us.atlassian.net/browse/CPBLOC-821) | Mint                               | 부작업 | Done | 2024-07-30 |

프로젝트가 Epic/Story 없이 부작업(Sub-task) 기반으로 관리됨 — XPLA 웹 지갑 FE/NFT Mint 플로우 구현 작업들.

## <a id="gcphdba"></a>GCPHDBA — CP_IEP_DBA (DB 서버 요청)

총 16건 · Done 16

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPHDBA-2820](https://com2us.atlassian.net/browse/GCPHDBA-2820) | [GCP_HIVE_DBA] 애널리틱스 권한 관리 시스템 DB 서버신청 | 스토리 | Done | 2024-11-15 |
| [GCPHDBA-1245](https://com2us.atlassian.net/browse/GCPHDBA-1245) | [GCP_HIVE_DBA] 블록체인 웹 지갑 상용 DB 서버신청       | 스토리 | Done | 2022-07-28 |

DBA 신청 티켓은 본인이 요청자(reporter)로서 신규 서비스 런칭 전에 작성. MySQL 8 MASTER-SLAVE 구성이 일반적 패턴.

## <a id="gcppde"></a>GCPPDE — 데이터 아키텍트 파트

총 3건 · Done 3

| 키 | 제목 | 타입 | 상태 | 최신 업데이트 |
|----|-----|------|------|--------------|
| [GCPPDE-1820](https://com2us.atlassian.net/browse/GCPPDE-1820) | [애널리틱스 예측] 타겟팅시 스냅샷 자동 선택 적용 구현 | 스토리 | Done | 2022-01-03 |
