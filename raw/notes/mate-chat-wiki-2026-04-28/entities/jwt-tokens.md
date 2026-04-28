---
title: "JWT Tokens"
type: entity
source_count: 1
tags: [jwt, auth, security, token]
related:
  - ../entities/auth-system.md
  - ../concepts/jwt-token-lifecycle.md
  - ../sources/15-auth-system.md
---

# JWT Tokens

## Overview

Mate Chat에서 API 인증에 사용하는 JSON Web Token 시스템. Access Token과 Refresh Token 두 종류로 구성되며, HS256 알고리즘으로 서명한다. 서버에서 발급하고 클라이언트에서 저장/관리한다.

## Structure

### Access Token
```
Header:  { alg: HS256, typ: JWT }
Payload: { sub: user_id, exp: 환경별 설정, iat: 발급시각, type: "access" }
Signature: HS256(header + payload, SECRET_KEY)
```
- **용도**: API 요청 인증
- **저장 위치**: 메모리 (Flutter)
- **만료**: 코드 기본값 1시간 (환경별 상이)

### Refresh Token
```
Header:  { alg: HS256, typ: JWT }
Payload: { sub: user_id, exp: 환경별 설정, jti: token_id, type: "refresh" }
Signature: HS256(header + payload, SECRET_KEY)
```
- **용도**: Access Token 갱신
- **저장 위치**: FlutterSecureStorage (암호화)
- **만료**: 코드 기본값 6개월 (환경별 상이)

> **설정 주의**: 토큰 만료 시간은 환경별로 다르게 설정됨. 코드 기본값: Access 1시간 / Refresh 6개월. Docker Compose prod: Access 30분 / Refresh 7일. 프로덕션 환경의 실제 .env 설정을 확인할 것.

## Key Details

- **서명 알고리즘**: HS256 (HMAC + SHA-256, 대칭키)
- **키 관리**: 환경 변수 또는 Secret Manager에 저장
- **토큰 검증**: `python-jose` 라이브러리 사용
- **세션 연동**: Refresh Token의 `jti`(token_id)로 Redis 세션과 매핑
- **갱신 흐름**: Refresh Token으로 새 Access Token 발급 (Refresh Token은 유지)
- **무효화**: Redis에서 세션 삭제로 Refresh Token 무효화

### 검증 프로세스
1. `Authorization: Bearer {access_token}` 헤더에서 토큰 추출
2. HS256 서명 검증 및 만료 시간 확인
3. `type` 필드가 `"access"`인지 확인
4. `sub` 필드로 사용자 조회
5. 사용자 존재 및 삭제 여부 확인

## Dependencies

- **python-jose**: 서버측 JWT 인코딩/디코딩
- **Redis**: Refresh Token 세션 저장
- **FlutterSecureStorage**: 클라이언트측 토큰 암호화 저장
- **Dio Interceptor**: 자동 토큰 갱신

## Known Issues

- **만료 시간 환경별 차이**: 코드 기본값(1시간/6개월), Docker Compose prod(30분/7일), .env.example(15분/7일)로 환경마다 다름. 프로덕션 실제 .env 확인 필요
- **HS256 한계**: 대칭키 방식으로 모든 서비스가 동일한 비밀키를 공유해야 함. 마이크로서비스 확장 시 RS256(비대칭키) 전환 권장

## Related

- [Auth System](../entities/auth-system.md) - 인증 시스템 전체
- [JWT Token Lifecycle](../concepts/jwt-token-lifecycle.md) - 토큰 생명주기 상세
