---
title: "인증 시스템 설계"
type: source
source_path: docs/15-auth-system.md
date_ingested: 2026-04-07
tags: [auth, jwt, oauth, security, session]
related:
  - ../entities/auth-system.md
  - ../entities/jwt-tokens.md
  - ../entities/oauth-providers.md
  - ../concepts/oauth-flow.md
  - ../concepts/jwt-token-lifecycle.md
---

# 인증 시스템 설계 - 소스 요약

## 문서 개요

Mate Chat의 인증 시스템 전체 설계를 다루는 문서. OAuth 2.0 소셜 로그인, JWT 토큰 관리, 세션 관리, 권한 관리까지 인증과 관련된 모든 계층을 포괄한다.

## 핵심 내용

### 인증 방식
- **OAuth 2.0**: Google(구현 완료), Apple(미구현) 소셜 로그인
- **JWT**: API 인증 토큰 (Access Token 15분, Refresh Token 7일)
- **이메일/비밀번호**: 전통적 인증 (별도 엔드포인트)

### 토큰 구조
- Access Token: `sub`(user_id), `exp`(15분), `iat`, `type`(access) / HS256 서명
- Refresh Token: `sub`(user_id), `exp`(7일), `jti`(token_id), `type`(refresh) / HS256 서명
- Access Token은 메모리 저장, Refresh Token은 Secure Storage 저장

### 세션 관리
- Redis 기반 세션 저장 (`session:{user_id}:{token_id}` 키 패턴)
- 단일 기기 로그아웃 및 전체 기기 로그아웃 지원
- 활성 세션 목록 조회 기능

### 보안 고려사항
- Flutter 클라이언트: `FlutterSecureStorage`로 토큰 저장
- Dio Interceptor로 자동 토큰 갱신 (401 응답 시)
- 갱신 실패 시 자동 로그아웃

### 권한 관리
- 채팅방 접근 권한 확인 (멤버십 기반)
- FastAPI Dependency Injection 패턴 활용

### API 엔드포인트
- `POST /auth/oauth` - OAuth 로그인
- `POST /auth/refresh` - 토큰 갱신
- `POST /auth/logout` - 로그아웃
- 총 13개 인증 관련 엔드포인트

## 관련 파일
- `app/api/v1/endpoints/auth.py`
- `app/core/security.py`
- `app/services/oauth_service.py`
- `app/services/email_auth_service.py`
- `lib/core/auth/` (Flutter)
- `lib/core/network/api_client.dart` (Flutter)
