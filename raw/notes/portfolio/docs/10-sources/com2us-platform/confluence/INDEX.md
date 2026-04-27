---
title: "컴투스플랫폼 Confluence 페이지 인덱스"
type: source-index
company: com2us-platform
source: confluence
collected_at: "2026-04-24"
---

# Confluence — 페이지 인덱스

컴투스플랫폼 Atlassian 워크스페이스에서 내가 생성한 Confluence 페이지의 **공개 인덱스**. 상세 페이지 본문은 `private/confluence/`에 저장.

## 수집 상태

- **수집일**: 2026-04-24
- **기간**: 2022-01-01 ~ 현재 (약 3년 3개월)
- **CQL**: `creator = currentUser() AND lastmodified >= "2022-01-01" ORDER BY lastmodified DESC`
- **총 페이지 수**: 52 (첨부/스페이스 overview 제외)
- **스페이스 수**: 4 (개인 스페이스 제외)
- **본문 수집 페이지 수**: 10 (private 저장)

## 스페이스별 요약

| 스페이스 키 | 스페이스명 | 내 페이지 수 | 주요 카테고리 |
|-----------|-----------|------------|-------------|
| GCPP2DTDW | 애널리틱스 개발 파트 | 30 | AI 가이드, 프론트엔드 가이드라인, 공통 API 명세/배포, Redis Sentinel/HA, 로깅 스택, 트러블슈팅 |
| GCPP2DT | AI개발2실 | 11 | Apache Superset 도입 R&D (개요/아키텍처/Embedding/통합 방안/활용 고도화) |
| GCPPD2 | GCP_PLATFORM DEPT.2 | 3 | CODE 트래블룰 회의록 (2022-04 ~ 2022-05 인수인계) |
| PNFTBD | Tech Business Division | 1 | NFT 디스코드 홀더 인증 봇 — DB 스키마 정리 |

## 카테고리 요약 (52페이지 기준)

- **설계/아키텍처 분석**: 애널리틱스 리포트 아키텍처 분석, Superset 통합 방안 비교 분석, Redis Sentinel vs Cluster 비교
- **R&D**: Apache Superset 도입 R&D (11건), SQL Templating R&D, ML 프로젝트 프로토타입
- **가이드**: AI 기반 개발 생산성 향상 가이드, 2025 프론트엔드 개발 가이드라인, 로깅 스택 구축 가이드, Redis Sentinel 도입 가이드, JetBrains IDE 설정 공유, Superset Embedding 가이드, Docker Compose 배포 가이드, Jenkins 멀티 브랜치 파이프라인 가이드, ag-grid Enterprise/Transpose 가이드
- **API 명세**: 지표 공통 API 명세 문서, 지표 공통 JavaScript 파일 사용 가이드
- **트러블슈팅**: "사용자 권한 게임 목록 조회" API 통합 트러블슈팅 (Redis 연결 끊김, MySQL 커넥션 풀, AWS idle 타임아웃)
- **회의록**: 2022-04~05 CODE 트래블룰 인수인계 3건

## 주요 페이지 (본문은 private)

본문 상세는 `pages-by-space.md` 참고. 본문 수집 10건은 `private/confluence/<page-id>.md`에 저장.

## 매핑

각 페이지는 `docs/20-projects/com2us-platform/` 프로젝트 문서의 `sources.confluence` 필드로 참조.

## 특이 발견

- **최근 집중 영역 (2025)**: 애널리틱스 개편 (프론트엔드 React 전환, 공통 API 구축, AI 도구 도입)
- **중기 집중 영역 (2025-Q2)**: Apache Superset 도입 R&D 집중 — 11편 문서로 완결적 R&D 수행
- **Redis 고가용성 구축 (2025-Q2)**: Redis Sentinel 도입부터 장애 시나리오, 인증 설정, Cluster vs Sentinel 비교까지 체계적 설계 문서 다수
- **초창기 (2022)**: CODE 트래블룰(가상자산 Travel Rule) 업무 인수인계 회의록
