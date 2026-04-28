---
title: "API 버전 관리"
type: concept
source_count: 1
tags: [api, versioning, rest, backward-compatibility]
related:
  - ../entities/api-endpoints.md
  - ../sources/14-api-design.md
---

# API 버전 관리

## Definition

API 버전 관리는 기존 클라이언트와의 호환성을 유지하면서 API를 발전시키기 위한 전략이다. 버전을 명시적으로 구분하여, 새로운 변경 사항이 기존 클라이언트를 깨뜨리지 않도록 한다.

## How It Works in Mate Chat

### URL Path 기반 버전 관리 (채택)

Mate Chat은 URL 경로에 버전 번호를 포함하는 방식을 사용한다:

```
https://api.matechat.com/v1/users/me    # 현재 버전
https://api.matechat.com/v2/users/me    # 향후 버전
```

FastAPI 라우터 구조가 이를 반영한다:

```
app/api/v1/
├── router.py          # v1 라우터 등록
└── endpoints/         # v1 엔드포인트들
```

### 헤더 기반 버전 관리 (대안으로 설계)

설계 문서에서 헤더 기반 버전 관리도 대안으로 언급되어 있다:

```
GET /users/me
X-API-Version: 2024-01-01
```

현재는 사용하지 않으며, URL 기반이 주 전략이다.

### 현재 상태

- v1만 운영 중
- v2 계획은 아직 없음
- WebSocket도 `/v1/ws/` 경로 사용

## Trade-offs

### URL Path 방식의 장점

- **명확성**: URL만 보고 버전 식별 가능
- **라우팅 용이**: 웹 서버/로드밸런서에서 버전별 라우팅 쉬움
- **캐싱 친화적**: URL이 다르므로 CDN/프록시 캐싱 자연스러움
- **디버깅 용이**: 로그에서 버전 즉시 확인

### URL Path 방식의 단점

- **URL 변경 필요**: 버전 업그레이드 시 클라이언트가 모든 URL 변경 필요
- **리소스 중복**: 같은 리소스가 다른 URL에 존재
- **점진적 마이그레이션 어려움**: 엔드포인트별 개별 버전 관리 불가

### 헤더 방식 대비

헤더 기반은 URL 깔끔, 엔드포인트별 버전 관리 가능하지만, 브라우저 테스트 불편하고 캐싱이 복잡해진다. Mate Chat은 모바일 앱 중심이므로 URL 기반의 명확성이 더 적합하다.

## Related

- [API 엔드포인트](../entities/api-endpoints.md) -- 버전 관리가 적용되는 엔드포인트
- [소스: API 설계](../sources/14-api-design.md)
