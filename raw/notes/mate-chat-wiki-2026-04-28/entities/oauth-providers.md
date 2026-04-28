---
title: "OAuth Providers"
type: entity
source_count: 1
tags: [oauth, google, apple, auth]
related:
  - ../entities/auth-system.md
  - ../concepts/oauth-flow.md
  - ../sources/15-auth-system.md
---

# OAuth Providers

## Overview

Mate Chat이 지원하는 외부 OAuth 2.0 인증 제공자. 현재 Google OAuth가 구현 완료되어 있으며, Apple Sign In은 iOS 출시를 위해 설계만 완료된 상태이다.

## Structure

| Provider | 상태 | 토큰 검증 방식 | 반환 정보 |
|----------|------|---------------|----------|
| Google | 구현 완료 | `google.oauth2.id_token.verify_oauth2_token()` | email, name, picture, provider_id(sub) |
| Apple | 미구현 | Apple JWKS 공개 키로 JWT 검증 | email, provider_id(sub) |

### Google OAuth
- **SDK**: Flutter `google_sign_in` (클라이언트), `google-auth` (서버)
- **검증**: Google의 공개 키로 ID Token 검증
- **Client ID**: 환경 변수 `GOOGLE_CLIENT_ID`로 관리
- **반환 데이터**: 이메일, 이름, 프로필 사진, provider_id

### Apple Sign In
- **SDK**: Flutter `sign_in_with_apple` (클라이언트, 예정)
- **검증**: Apple JWKS URL (`https://appleid.apple.com/auth/keys`)에서 공개 키 획득 후 JWT 검증
- **설정**: `APPLE_TEAM_ID`, `APPLE_KEY_ID` 환경 변수 필요
- **주의**: 설계 문서의 알고리즘이 HS256으로 기술되어 있으나, Apple은 실제로 RS256/ES256 사용

## Key Details

- **통합 엔드포인트**: `POST /auth/oauth`에서 `provider` 필드로 분기
- **사용자 생성/조회**: `get_or_create_user()` 함수로 첫 로그인 시 자동 계정 생성
- **신규 사용자 판별**: `created_at == updated_at` 비교로 판단
- **DB 저장**: `users` 테이블의 `provider`, `provider_id` 컬럼에 OAuth 정보 저장

## Dependencies

- **google-auth**: Google ID Token 검증
- **PyJWT + PyJWKClient**: Apple ID Token 검증 (예정)
- **PostgreSQL**: 사용자 및 OAuth 정보 저장

## Known Issues

- **Apple OAuth 미구현**: iOS App Store 출시의 필수 요구사항
- **Apple 검증 알고리즘 오류**: 설계 문서에서 HS256으로 기술되어 있으나, Apple은 RS256 또는 ES256 사용. 구현 시 수정 필요

## Related

- [Auth System](../entities/auth-system.md) - 인증 시스템 전체
- [OAuth Flow](../concepts/oauth-flow.md) - OAuth 인증 흐름 상세
