---
title: "Auth System"
type: entity
source_count: 1
tags: [auth, security, backend, flutter]
related:
  - ../entities/jwt-tokens.md
  - ../entities/oauth-providers.md
  - ../concepts/oauth-flow.md
  - ../concepts/jwt-token-lifecycle.md
  - ../sources/15-auth-system.md
  - ../sources/archive-legacy-system.md
---

# Auth System

## Overview

Mate Chat의 인증 시스템은 OAuth 2.0 소셜 로그인과 이메일/비밀번호 인증을 지원하며, JWT 토큰 기반으로 API 접근을 관리한다. 백엔드(FastAPI)에서 토큰 발급/검증/갱신을 처리하고, Flutter 클라이언트에서 토큰 저장 및 자동 갱신을 담당한다.

> **Historical note**: 레거시 시스템에서는 Firebase Auth를 사용했으며, Google + Facebook + Email/Password + SMS(MFA) 인증을 지원했다. 자동 토큰 갱신(1시간 만료)이 편리했으나, 강제 로그아웃/다중 디바이스 세션 관리가 불가능했다. 리마스터에서 Facebook을 제거하고, 자체 JWT + OAuth 직접 연동으로 전환하여 세션 제어 유연성을 확보했다. [레거시 아카이브](../sources/archive-legacy-system.md) 참조.

## Architecture

```
Flutter App                    FastAPI Backend                External
┌──────────────┐              ┌──────────────────┐          ┌──────────┐
│ TokenStorage │              │ auth.py (13 API) │          │ Google   │
│ AuthInterceptor│◄──────────►│ security.py      │◄────────►│ Apple    │
│ (Dio)        │   JWT        │ oauth_service.py │  OAuth   │          │
└──────────────┘              │ email_auth_svc.py│          └──────────┘
                              └────────┬─────────┘
                                       │
                              ┌────────▼─────────┐
                              │ Redis (Sessions)  │
                              │ PostgreSQL (Users) │
                              └──────────────────┘
```

### 계층 구조
- **엔드포인트 계층**: `app/api/v1/endpoints/auth.py` (13개 API)
- **서비스 계층**: `oauth_service.py`, `email_auth_service.py`, `email_service.py`
- **보안 계층**: `app/core/security.py` (토큰 생성/검증)
- **세션 계층**: Redis 기반 세션 저장
- **클라이언트 계층**: `FlutterSecureStorage`, Dio Interceptor

## Key Details

- **인증 방식**: OAuth 2.0 (Google, Apple), 이메일/비밀번호, JWT
- **Access Token 만료**: 코드 기본값 1시간 (환경별 상이)
- **Refresh Token 만료**: 코드 기본값 6개월 (환경별 상이)

> **설정 주의**: 토큰 만료 시간은 환경별로 다르게 설정됨. 코드 기본값: Access 1시간 / Refresh 6개월. Docker Compose prod: Access 30분 / Refresh 7일. 프로덕션 환경의 실제 .env 설정을 확인할 것.
- **서명 알고리즘**: HS256
- **세션 저장**: Redis (`session:{user_id}:{token_id}`)
- **클라이언트 토큰 저장**: `FlutterSecureStorage` (암호화된 로컬 저장소)
- **자동 갱신**: Dio Interceptor가 401 응답 시 자동으로 토큰 갱신
- **권한 관리**: FastAPI Dependency Injection을 통한 리소스 접근 제어

### 주요 API 엔드포인트
| 엔드포인트 | 설명 |
|-----------|------|
| `POST /auth/oauth` | OAuth 소셜 로그인 |
| `POST /auth/refresh` | Access Token 갱신 |
| `POST /auth/logout` | 로그아웃 (세션 삭제) |

## Dependencies

- **FastAPI**: 엔드포인트 및 Dependency Injection
- **python-jose**: JWT 토큰 생성/검증
- **Redis**: 세션 저장 및 관리
- **PostgreSQL**: 사용자 데이터, 이메일 인증, 비밀번호 재설정 저장
- **google-auth**: Google OAuth 토큰 검증
- **PyJWT / PyJWKClient**: Apple Sign In 토큰 검증
- **flutter_secure_storage**: Flutter 클라이언트 토큰 암호화 저장
- **Dio**: HTTP 클라이언트 및 인터셉터

## Known Issues

- **Apple OAuth 미구현**: iOS App Store 출시에 필수적이나 아직 구현되지 않음
- **토큰 만료 시간 환경별 차이**: 코드 기본값(1시간/6개월), Docker Compose prod(30분/7일), .env.example(15분/7일)로 환경마다 다름. 프로덕션 실제 .env 확인 필요
- **HS256 사용**: 대칭키 알고리즘으로, 마이크로서비스 확장 시 RS256 전환 검토 필요

## Related

- [JWT Tokens](../entities/jwt-tokens.md) - 토큰 구조 및 생명주기
- [OAuth Providers](../entities/oauth-providers.md) - 외부 인증 제공자
- [OAuth Flow](../concepts/oauth-flow.md) - OAuth 인증 흐름
- [JWT Token Lifecycle](../concepts/jwt-token-lifecycle.md) - 토큰 생명주기
