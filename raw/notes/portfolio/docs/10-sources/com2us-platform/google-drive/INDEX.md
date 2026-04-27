---
title: "컴투스플랫폼 Google Drive 문서 인덱스"
type: source-index
company: com2us-platform
source: google-drive
collected_at: "2026-04-24"
---

# Google Drive — 문서 인덱스

컴투스플랫폼 재직 관련 Google Drive 문서의 **공개 인덱스**. 상세 본문은 `private/google-drive/`에 저장.

## 수집 상태

- 수집일: **2026-04-24**
- 수집 범위: 최근 3년 (`modifiedTime > '2022-01-01T00:00:00Z'`)
- 문서 타입 필터: Docs, Sheets, Slides, DOCX/XLSX/PPTX (Google Apps + MS Office)
- 검색 계정: 개인 Google 계정 (gsr2732@gmail.com) — 사내 Google Workspace 계정(sgkim@com2us.com)은 별도 접근 경로 필요
- 총 관련 문서: **3건**

## 수집 참고 사항

- MCP 도구는 개인 Google 계정에 연결됨. 사내 계정의 공식 설계 문서·RFC·회고·기획서는 주로 Confluence/Jira에 보관됨 (Phase A/B 참조)
- 3년 내 개인 Drive에는 **컴투스 관련 기술 리서치 문서 3건**이 확인됨
- HIVE/컴투스 직접 키워드로는 2017-2018년 초기 자료가 있으나 **수집 범위 외 (>3년)** 로 제외
- 제외된 문서: 이력서, 지원서, 개인 프로젝트(mate-chat), 개인 파일, 백업 이미지 등

## 문서 목록 (카테고리별)

### 분석/리서치

| 제목 | 타입 | 수정일 | 관련 프로젝트/기술 | Private Link |
|------|------|--------|--------------------|--------------|
| RedisInsight 설정 및 사용법 | Google Docs | 2025-04-14 | Redis 운영/모니터링 도구 검토 | `private/google-drive/1gDdgA3aFmfIi2b1_gnwfOVBKwZ89WzH7bVD5GFBH7aA.md` |
| 최신 LLM 비교 및 활용 조사 | Google Docs | 2025-04-14 | LLM/Agent/MCP 도입 리서치 | `private/google-drive/1RkW2M47hZSHX4O3buedub5JiXETPs9ZhsfOolNvyhVo.md` |

### 가이드/기술문서

| 제목 | 타입 | 수정일 | 관련 프로젝트/기술 | Private Link |
|------|------|--------|--------------------|--------------|
| Databricks IDE Plugin Guide | DOCX | 2026-01-08 | 데이터 플랫폼/IDE 연동/Asset Bundles 배포 | `private/google-drive/1gVqXpodxayay48lWE3N2f4WQVgaeLVmB.md` |

### 설계/RFC

_해당 없음 (개인 Drive 범위 내 수집되지 않음)_

### 회고/리포트

_해당 없음 (개인 Drive 범위 내 수집되지 않음)_

### 기획서

_해당 없음 (개인 Drive 범위 내 수집되지 않음)_

## 매핑

`docs/20-projects/com2us-platform/` 프로젝트 문서의 `sources.gdrive` 필드로 참조.

## 향후 확장

- 사내 Google Workspace 계정(sgkim@com2us.com)에 MCP 접근이 가능해지면 재수집
- HIVE SDK / 빌링 / 인증 관련 초기(2016-2018) 문서는 **프로젝트 히스토리** 용도로 별도 수집 검토 가능 (수집 범위 3년 제약 해제 시)
