---
title: API Response Envelope (result_code · message · data 표준)
aliases:
- API Response Envelope
- api-response-envelope
- APIResponse
- result_code envelope
- response envelope
type: concept
category: 백엔드
tags:
- api-response-envelope
- api-design
- fastapi
- response-pattern
- error-handling
- 백엔드
related:
- '[[backend-python-fastapi]]'
- '[[annotated-pattern]]'
- '[[fastapi]]'
- '[[fastapi-fastapi]]'
- '[[c2spf-analytics]]'
- '[[c2spf-analytics-common]]'
- '[[c2spf-analytics-renewal]]'
- '[[portfolio-resume-ko]]'
- '[[data-pipeline-bigquery]]'
- '[[frontend-react]]'
- '[[matechat]]'
source_count: 4
created: 2026-04-30
updated: 2026-04-30
cited_by_count: 3
---

# API Response Envelope (result_code · message · data 표준)

## 정의

**API 응답을 항상 일관된 envelope으로 감싸는 패턴**. 데이터를 raw로 노출하지 않고 **`{result_code, message, data}` 같은 고정 구조**로 wrapping하여 (a) 성공/실패 분기가 명시적이고 (b) 에러 메시지가 표준화되며 (c) 클라이언트가 단일 처리 경로로 모든 응답을 다룰 수 있게 한다.

owner는 [[c2spf-analytics]]에서 **`{result_code, message, data}` 표준 + APICode 13종 + BigQuery 결과 코드 4종**으로 9년간 운영. 본 페이지가 그 운영 표준의 단일 진실원.

## 왜 중요한가

### 1. 클라이언트의 단일 처리 경로

```typescript
// envelope 없는 경우 — 클라이언트 분기 폭발
const data = await fetch('/users/123');
if (data.error) { ... }  // 어떤 에러? 어떻게 분류?
if (data.users) { ... }   // 다른 엔드포인트는 다른 모양
if (data.message) { ... } // HTTP 200인데 비즈니스 실패?

// envelope 있는 경우 — 단일 패턴
const { result_code, message, data } = await fetch('/users/123');
if (result_code !== 'OK') { showError(message); return; }
useData(data);  // 100% 안전
```

### 2. HTTP 상태 코드의 한계 보완

HTTP 상태 코드 (200/400/500)는 **전송 계층의 성공/실패만** 표현. **비즈니스 로직 결과**(예: "사용자는 있지만 권한 없음" / "데이터는 있지만 일부 BigQuery 쿼리 실패")는 별도 분류 필요.

owner의 c2spf 표준:
- HTTP 200 + `result_code: 'OK'` — 완전 성공
- HTTP 200 + `result_code: 'PARTIAL_FAILURE'` — 일부 실패 (BigQuery 4 결과 코드 활용)
- HTTP 200 + `result_code: 'PERMISSION_DENIED'` — 권한 거부 (HTTP 403 안 쓰는 이유: 클라이언트 캐시 정책)
- HTTP 5xx — 인프라 실패 (envelope 없이 raw error)

### 3. APICode + ProcessedData 이원 에러 정책

c2spf가 9년간 정착시킨 분기:
- **APICode** (13종): 전송·인증·권한·요청 검증 같은 **API 레이어 에러**
- **ProcessedData** (4 코드): BigQuery 결과 처리 단계의 **데이터 레이어 에러**

같은 envelope이지만 두 차원이 분리된 분류 — 운영자가 에러 위치를 즉시 파악 가능.

## 핵심 내용

### 표준 envelope 구조

```python
from typing import Annotated, Generic, TypeVar
from pydantic import BaseModel, Field

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    result_code: Annotated[str, Field(description="OK / PERMISSION_DENIED / PARTIAL_FAILURE / ...")]
    message: Annotated[str, Field(description="사람용 메시지")]
    data: T | None = None
    meta: dict | None = None  # pagination, request_id 등
```

[[annotated-pattern]] + Pydantic Generic으로 **타입 안전한 envelope** 표현. FastAPI 응답 모델로 박으면 OpenAPI 스키마에 자동 반영.

### 4가지 일반 패턴 비교

| 패턴 | 예시 | 장점 | 단점 |
|---|---|---|---|
| **단순 envelope** | `{ok, error, data}` (Rust Result 영향) | 간결, JSON 친화 | 에러 코드 분류 부재 |
| **owner의 c2spf 표준** | `{result_code, message, data}` | 코드 분류 명시, 메시지 표준화 | 클라이언트가 코드 enum 알아야 함 |
| **JSON:API spec** | `{data: {...}, errors: [...], meta: {...}}` | 산업 표준 | overhead 큼 (모든 필드 명시) |
| **GraphQL response** | `{data, errors, extensions}` | GraphQL 친화 | REST와 다른 메커니즘 |

### Pagination 메타 표준

```python
class APIResponse(BaseModel, Generic[T]):
    result_code: str
    message: str
    data: T | None = None
    meta: PaginationMeta | None = None

class PaginationMeta(BaseModel):
    total: int
    page: int
    limit: int
    has_next: bool
```

페이지네이션은 `meta` 하위로 분리 — `data` 자체는 항상 type T 보존. 클라이언트의 type narrowing이 자연스러움.

### 에러 응답 표준

```python
# 비즈니스 에러 (HTTP 200)
{
    "result_code": "PERMISSION_DENIED",
    "message": "이 게임의 데이터를 볼 권한이 없습니다",
    "data": None,
    "meta": {"required_role": "game_admin"}
}

# 인프라 에러 (HTTP 5xx, envelope 없음)
{
    "detail": "Internal Server Error"
}
```

비즈니스 에러는 envelope 안, 인프라 에러는 envelope 밖. 이 분리가 **클라이언트의 retry 전략 결정**의 입력.

## 안티패턴

| 안티패턴 | 문제 | 회피 |
|---|---|---|
| 모든 응답에 HTTP 200 + envelope 사용 | 모니터링 도구가 "200=성공"으로 알람 못 침 | 인프라 에러는 5xx, 비즈니스 분기만 envelope |
| `data` 안에 또 envelope 중첩 | 클라이언트 처리 복잡 | data는 항상 단일 type T |
| `message`에 PII (사용자 이메일·내부 ID) 노출 | 에러 메시지로 정보 누출 | 일반화된 메시지 + meta로 디버깅 정보 분리 |
| envelope을 모든 엔드포인트에 강제 (binary 응답까지) | 파일 다운로드·스트리밍에 부적합 | binary/stream 응답은 envelope 외 |
| `result_code` 값을 자유 문자열로 두기 | 클라이언트 분기에 magic string | enum으로 타입화 (Pydantic Literal) |

## owner 활용 시나리오

### [[c2spf-analytics]] 표준 (9년 운영)

```python
# common/responses.py
from typing import Annotated, Generic, Literal, TypeVar
from pydantic import BaseModel, Field

ResultCode = Literal[
    "OK",
    "PERMISSION_DENIED",
    "PARTIAL_FAILURE",
    "INVALID_REQUEST",
    "NOT_FOUND",
    "BIGQUERY_TIMEOUT",
    "BIGQUERY_QUOTA_EXCEEDED",
    # ... APICode 13종
]

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    result_code: ResultCode
    message: str
    data: T | None = None
    meta: dict | None = None
```

`analytics-common-api` 92% (231/251 커밋)이 이 표준 위에 빌드. `analytics-react-renewal`이 클라이언트 측에서 같은 envelope을 type-safe하게 소비.

### [[matechat]] API 응답 모델 적용

Flutter 클라이언트가 받는 모든 응답을 envelope으로 통일:
- `result_code`: `OK | RATE_LIMITED | UNAUTHORIZED | INVALID_INPUT`
- 클라이언트는 `result_code !== 'OK'` 시 message를 표시, 그 외에는 data 사용
- ag-grid·차트·리스트 모두 단일 처리 경로

### BigQuery PARTIAL_FAILURE 패턴

c2spf의 게임 데이터 분석 API가 100개 게임 동시 조회 시 일부 BigQuery 쿼리만 실패할 수 있음. envelope으로 처리:

```python
{
    "result_code": "PARTIAL_FAILURE",
    "message": "100개 게임 중 5개 데이터 조회 실패",
    "data": {
        "games": [...],  # 95개 게임 데이터
        "failed_game_ids": [...]  # 5개 실패 ID
    },
    "meta": {"bigquery_partial_codes": ["TIMEOUT", "QUOTA"]}
}
```

`PARTIAL_FAILURE`가 가능하도록 envelope 설계가 필수. raw 노출 시 클라이언트가 95개를 보여줘야 할지 0개를 보여줘야 할지 결정 못 함.

## 관련 개념

- [[backend-python-fastapi]] — FastAPI 기반 envelope의 모범 구현. 본 패턴이 백엔드 스택의 1차 출력 표준.
- [[annotated-pattern]] — `Annotated[T, Field(...)]` 로 envelope 필드를 타입 안전하게 표현.
- [[frontend-react]] — 클라이언트 측 single-path consumption. TanStack Query가 envelope 패턴 친화적.
- [[data-pipeline-bigquery]] — `BIGQUERY_*` result_code가 BI 데이터 레이어 에러를 envelope에 통합.

## 출처

- [[c2spf-analytics-common]] — APIResponse `{result_code, message, data}` envelope 9년 운영 (2017~). FastAPI 공통 API 표준.
- [[c2spf-analytics-renewal]] — Airbridge MMP × BigQuery 결합에서 envelope 활용 (PARTIAL_FAILURE 코드 활용 사례).
- [[fastapi-fastapi]] — `.agents/skills/fastapi/SKILL.md`가 [[annotated-pattern|`Annotated`]] + return type annotation 권장. Pydantic Generic 직렬화로 envelope 자동 OpenAPI.
- [[portfolio-resume-ko]] — owner의 9년 운영 정량 지표.

## 열린 질문

- **GraphQL 도입 시 envelope 패턴 호환성**: GraphQL의 `{data, errors}` 와 c2spf의 `{result_code, message, data}` 가 어떻게 결합?
- **gRPC 도입 시**: gRPC는 자체 status code가 있어 envelope이 중복. REST envelope과 gRPC status를 어떻게 매핑?
- **streaming 응답에 envelope 적용**: Server-Sent Events / WebSocket 응답에 envelope을 어떻게 박을지.
- **envelope 자체의 버저닝**: `result_code` 코드 추가가 빈번할 때 클라이언트 호환성 보장 정책 (cf. [[openai-openai-agents-python]] Public API Positional Compatibility).
