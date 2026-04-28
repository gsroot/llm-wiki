---
title: "OAuth Flow"
type: concept
source_count: 1
tags: [oauth, auth, google, apple, flow]
related:
  - ../entities/auth-system.md
  - ../entities/oauth-providers.md
  - ../concepts/jwt-token-lifecycle.md
  - ../sources/15-auth-system.md
---

# OAuth Flow

## Definition

OAuth 2.0 프로토콜을 이용한 외부 인증 제공자(Google, Apple)를 통한 사용자 인증 흐름. 클라이언트(Flutter)가 외부 SDK로 토큰을 획득하고, 서버(FastAPI)가 해당 토큰을 검증한 뒤 자체 JWT 토큰을 발급하는 방식이다.

## How It Works in Mate Chat

### Google OAuth 흐름 (7단계)

1. **Flutter**: Google Sign-In SDK 호출 → 사용자가 Google 계정 선택
2. **Google**: ID Token을 Flutter 앱에 반환
3. **Flutter**: `POST /auth/oauth` 요청 (`{ provider: "google", token: id_token }`)
4. **FastAPI**: `google.oauth2.id_token.verify_oauth2_token()`으로 ID Token 검증
5. **Google**: 검증 결과 + 사용자 정보(email, name, picture, sub) 반환
6. **FastAPI**: DB에서 사용자 조회 또는 신규 생성 (`get_or_create_user()`)
7. **FastAPI**: JWT Access Token + Refresh Token 발급 → Flutter에 반환

### Apple Sign In 흐름 (설계, 미구현)

1. **Flutter**: Sign in with Apple SDK 호출
2. **Apple**: Authorization Code + ID Token 반환
3. **FastAPI**: Apple JWKS 공개 키로 ID Token 검증
4. **FastAPI**: 사용자 조회/생성 → JWT 발급

### 통합 엔드포인트

`POST /auth/oauth`에서 `provider` 필드 값으로 분기 처리:
- `"google"` -> `verify_google_token()`
- `"apple"` -> `verify_apple_token()`
- 그 외 -> 400 Bad Request

### 신규 사용자 처리
- `created_at == updated_at` 비교로 신규 사용자 판별
- 응답에 `is_new_user` 플래그 포함
- 이메일 인증 시 Welcome 보너스 200 클로버 지급

## Trade-offs

| 장점 | 단점 |
|------|------|
| 사용자가 별도 비밀번호 없이 빠르게 가입 가능 | 외부 서비스(Google, Apple)에 의존 |
| 이메일 검증이 이미 완료된 상태 | Apple OAuth 미구현으로 iOS 출시 차단 |
| 보안이 외부 제공자에 의해 관리됨 | 제공자 장애 시 로그인 불가 |
| 클라이언트에서 토큰 획득, 서버에서 검증하는 분리 구조 | 각 제공자별 SDK 관리 비용 |

## Related

- [Auth System](../entities/auth-system.md) - 인증 시스템 전체 구조
- [OAuth Providers](../entities/oauth-providers.md) - Google, Apple 제공자 상세
- [JWT Token Lifecycle](../concepts/jwt-token-lifecycle.md) - OAuth 후 발급되는 JWT 생명주기
