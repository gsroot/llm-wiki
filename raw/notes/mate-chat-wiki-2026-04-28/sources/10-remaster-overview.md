---
title: "리마스터 개요"
type: source
source_path: docs/10-remaster-overview.md
date_ingested: 2026-04-07
tags: [remaster, migration, architecture, firebase, fastapi]
related:
  - "../sources/11-tech-stack-new.md"
  - "../sources/12-system-architecture.md"
  - "../entities/fastapi-app.md"
  - "../entities/postgresql.md"
  - "../concepts/vendor-independence.md"
---

# 리마스터 개요

## 핵심 요약

Mate Chat 리마스터는 Firebase 기반 인프라를 자체 호스팅 인프라로 전면 전환하는 프로젝트이다. 핵심 목표는 인프라 독립성, 확장성, 개발 효율성, 보안 강화 네 가지이다.

## 주요 변경 결정

| 영역 | 기존 | 리마스터 | 전환 이유 |
|------|------|----------|-----------|
| 백엔드 | Firebase Cloud Functions | FastAPI | 완전한 제어권, 로컬 개발, 비용 예측 |
| 데이터베이스 | Firestore (NoSQL) | PostgreSQL (RDBMS) | 데이터 무결성, JOIN/트랜잭션, 명확한 스키마 |
| 인증 | Firebase Auth | 자체 JWT + OAuth | 인증 로직 제어, 커스텀 필드, 비용 절감 |
| 실시간 통신 | Firestore 스트림 + FCM | WebSocket | 양방향 통신, 낮은 지연, 이벤트 타입 다양성 |
| 파일 저장소 | Firebase Storage | MinIO (S3 호환) | 자체 호스팅, 클라우드 이전 용이 |

## 유지 요소

- Flutter 프레임워크 + Riverpod 상태 관리
- 핵심 기능: 프로필, 채팅, AI Mate, 소셜 관계, 클로버 경제
- 외부 연동: OpenAI API, Google/Apple OAuth, 인앱 결제
- 다국어 지원 (9개 언어)

## 리마스터 5단계

1. **기반 구축**: FastAPI 셋업, PostgreSQL 스키마, 인증, 기본 CRUD
2. **핵심 기능**: 사용자/채팅/WebSocket/AI 챗봇 API
3. **부가 기능**: 소셜, 알림, 클로버, 파일 업로드
4. **Flutter 연동**: API/WebSocket 클라이언트, 상태 관리 리팩토링
5. **배포 및 운영**: 인프라, CI/CD, 모니터링, 데이터 마이그레이션

## 주요 리스크

- Firestore -> PostgreSQL 마이그레이션: NoSQL 서브컬렉션을 관계형 테이블로 변환하는 복잡성
- 실시간 통신: Firestore 자동 동기화를 WebSocket으로 대체 시 오프라인 지원/연결 안정성 확보 필요
- 인증 전환: Firebase Auth 토큰에서 자체 JWT로의 전환, 세션 관리 필요
