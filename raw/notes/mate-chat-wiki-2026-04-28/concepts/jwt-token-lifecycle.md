---
title: "JWT Token Lifecycle"
type: concept
source_count: 1
tags: [jwt, token, auth, lifecycle, refresh]
related:
  - ../entities/jwt-tokens.md
  - ../entities/auth-system.md
  - ../concepts/oauth-flow.md
  - ../sources/15-auth-system.md
---

# JWT Token Lifecycle

## Definition

JWT(JSON Web Token)의 발급, 사용, 갱신, 무효화까지의 전체 생명주기. Mate Chat에서는 단기 Access Token과 장기 Refresh Token의 이중 토큰 전략을 사용하여 보안과 사용자 편의성을 동시에 확보한다.

## How It Works in Mate Chat

### 1. 발급 (Issuance)

로그인(OAuth 또는 이메일) 성공 시 두 토큰 동시 발급:
- **Access Token**: `create_access_token(user_id)` - 코드 기본값 1시간 만료 (환경별 상이)
- **Refresh Token**: `create_refresh_token(user_id)` - 코드 기본값 6개월 만료 (환경별 상이), 고유 `jti` 포함

> **설정 주의**: 토큰 만료 시간은 환경별로 다르게 설정됨. 코드 기본값: Access 1시간 / Refresh 6개월. Docker Compose prod: Access 30분 / Refresh 7일. 프로덕션 환경의 실제 .env 설정을 확인할 것.

Refresh Token 발급 시 Redis에 세션 저장:
- 키: `session:{user_id}:{token_id}`
- TTL: Refresh Token 만료 기간과 동일
- 값: 기기 정보, 생성 시각

### 2. 사용 (Usage)

모든 API 요청에 Access Token 포함:
- 헤더: `Authorization: Bearer {access_token}`
- 서버에서 `get_current_user()` dependency로 검증
- 검증 실패 시 401 Unauthorized

### 3. 갱신 (Renewal)

Access Token 만료 시:
1. Dio Interceptor가 401 응답 감지
2. 저장된 Refresh Token으로 `POST /auth/refresh` 호출
3. 서버에서 Refresh Token 검증 + Redis 세션 확인
4. 새 Access Token 발급 (Refresh Token은 유지)
5. 원래 요청 자동 재시도

### 4. 무효화 (Revocation)

로그아웃 시:
- **단일 기기**: `redis.delete(f"session:{user_id}:{token_id}")`
- **전체 기기**: `redis.keys(f"session:{user_id}:*")`로 모든 세션 삭제
- Refresh Token이 Redis에서 제거되면 갱신 불가 -> 실질적 무효화

### 5. 만료 (Expiration)

- Access Token: 설정된 만료 시간 후 자동 만료 (서버에서 `ExpiredSignatureError`)
- Refresh Token: 설정된 만료 시간 후 자동 만료 + Redis TTL에 의한 세션 만료
- 클라이언트: 갱신 실패 시 `TokenStorage.clearTokens()` -> 로그아웃

### 흐름도

```
로그인 → [Access + Refresh 발급] → API 요청 (Access Token)
                                        │
                                   만료? ──No──→ 정상 응답
                                        │
                                       Yes
                                        │
                                   401 응답 → Refresh Token으로 갱신
                                                    │
                                              성공? ──Yes──→ 새 Access Token → 재시도
                                                    │
                                                   No
                                                    │
                                               로그아웃 (토큰 삭제)
```

## Trade-offs

| 장점 | 단점 |
|------|------|
| 짧은 Access Token으로 토큰 탈취 피해 최소화 | 이중 토큰 관리의 복잡성 |
| Refresh Token으로 빈번한 재로그인 방지 | Redis 의존성 (세션 저장) |
| 서버 측 세션 무효화 가능 (순수 JWT보다 유연) | Stateless JWT의 장점 일부 상실 |
| Dio Interceptor로 사용자 경험 투명 | 갱신 실패 시 전체 재로그인 필요 |

## Related

- [JWT Tokens](../entities/jwt-tokens.md) - 토큰 구조 상세
- [Auth System](../entities/auth-system.md) - 인증 시스템 전체
- [OAuth Flow](../concepts/oauth-flow.md) - 토큰 발급의 시작점
