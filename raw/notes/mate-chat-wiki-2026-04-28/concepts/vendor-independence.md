---
title: "Vendor Independence"
type: concept
source_count: 2
tags: [architecture, vendor-lock-in, firebase, migration, self-hosted]
related:
  - "../sources/10-remaster-overview.md"
  - "../sources/archive-legacy-system.md"
  - "../entities/fastapi-app.md"
  - "../entities/minio.md"
---

# Vendor Independence

## Definition

특정 클라우드 벤더(Firebase, AWS 등)에 대한 종속성을 제거하고, 자체 호스팅 또는 벤더 교체가 가능한 인프라를 구축하는 설계 원칙이다.

## How It Works in Mate Chat

리마스터의 핵심 동기 중 하나가 Firebase 종속성 해소이다.

| 영역 | Firebase (종속) | 리마스터 (독립) |
|------|----------------|----------------|
| 백엔드 | Cloud Functions | FastAPI (자체 호스팅) |
| 데이터베이스 | Firestore | PostgreSQL (어디서든 운영 가능) |
| 인증 | Firebase Auth | 자체 JWT + OAuth 직접 연동 |
| 파일 저장소 | Firebase Storage | MinIO (S3 호환, AWS 이전 가능) |
| 실시간 통신 | Firestore 스트림 | WebSocket (표준 프로토콜) |
| 푸시 알림 | FCM (유일한 잔존 종속) | FCM 유지 (대안: OneSignal) |

### 이점 실현

- **비용 예측**: 고정 인프라 비용 vs Firebase 사용량 과금
- **완전한 제어**: 로직, 스케일링, 모니터링 자유도
- **이식성**: Docker 컨테이너로 어떤 환경에든 배포 가능
- **개발 경험**: 로컬에서 전체 스택 실행 가능

## Trade-offs

**장점**:
- 벤더 락인 해소, 비용 절감, 기술 자유도
- 로컬 개발/테스트 환경 완전 구축

**단점**:
- 인프라 관리 부담 증가 (DB, 캐시, 스토리지 직접 운영)
- 개발 기간 증가 (인증, 실시간 통신 등 직접 구현)
- Firebase의 자동 오프라인 동기화, 자동 스케일링 등 편의 기능 상실

## Historical Context

> **Historical note**: 레거시 시스템의 Firestore Security Rules가 `allow read, write: if true`로 방치되어 있었으며, 이것이 벤더 독립성 추구의 직접적 계기가 되었다. Firebase 에코시스템 내에서 보안을 강화하려면 Security Rules의 복잡도가 급증하는 구조적 한계가 있었다. 또한 Firebase 에뮬레이터의 복잡한 설정으로 인해 테스트 작성이 사실상 불가능했다 (레거시 테스트: 0개 → 리마스터 후 113개). 상세 내용은 [레거시 시스템 아카이브](../sources/archive-legacy-system.md) 참조.

## Related

- [레거시 시스템 아카이브](../sources/archive-legacy-system.md) -- Firebase 기반 레거시 시스템의 문제점과 전환 근거
- [리마스터 개요](../sources/10-remaster-overview.md) -- 전환 배경과 계획
- [MinIO](../entities/minio.md) -- S3 호환 자체 호스팅 스토리지
- [FastAPI Application](../entities/fastapi-app.md) -- 자체 호스팅 백엔드
