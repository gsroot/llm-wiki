---
title: "커서 기반 vs 오프셋 기반 페이지네이션"
type: concept
source_count: 1
tags: [api, pagination, performance, ux]
related:
  - ../entities/api-endpoints.md
  - ../entities/database-schema.md
  - ../sources/14-api-design.md
---

# 커서 기반 vs 오프셋 기반 페이지네이션

## Definition

페이지네이션은 대량의 데이터를 여러 페이지로 나누어 전달하는 기법이다. 오프셋 기반은 `page`와 `per_page`로 건너뛸 행 수를 지정하고, 커서 기반은 마지막으로 본 항목의 식별자를 기준으로 다음 데이터를 조회한다.

## How It Works in Mate Chat

Mate Chat은 용도에 따라 두 가지 방식을 모두 사용한다.

### 커서 기반 페이지네이션

채팅 메시지 조회에 사용된다:

```
GET /chat-rooms/{room_id}/messages?before={message_uuid}&limit=50
```

응답:
```json
{
  "data": [...],
  "meta": {
    "has_more": true,
    "next_cursor": "uuid-of-last-message"
  }
}
```

- `before`: 해당 UUID 이전의 메시지를 조회
- `limit`: 최대 100, 기본 50
- 인덱스: `(room_id, created_at DESC)` 복합 인덱스 활용

### 오프셋 기반 페이지네이션

목록 조회(사용자 탐색, 채팅방 탐색, 알림 등)에 사용된다:

```
GET /users/explore?page=1&per_page=20&country_code=KR
```

응답:
```json
{
  "data": [...],
  "meta": {
    "page": 1,
    "per_page": 20,
    "total": 150
  }
}
```

- `per_page` 최대값: 100
- `total` 포함으로 전체 페이지 수 계산 가능

## Trade-offs

### 커서 기반

| 장점 | 단점 |
|------|------|
| 대량 데이터에서 일정한 성능 | 특정 페이지로 바로 이동 불가 |
| 실시간 데이터 삽입/삭제에 안정적 | total count 제공 어려움 |
| 채팅 메시지 같은 타임라인에 적합 | 구현 복잡도 높음 |

### 오프셋 기반

| 장점 | 단점 |
|------|------|
| 구현 단순 | 페이지가 깊어질수록 성능 저하 |
| 전체 개수(total) 제공 용이 | 데이터 삽입/삭제 시 페이지 누락/중복 |
| 특정 페이지 바로 접근 가능 | COUNT 쿼리 비용 |

### Mate Chat의 선택 근거

- **메시지**: 실시간 삽입이 빈번하고 역순(최신 먼저) 조회가 주 패턴이므로 커서 기반 적합
- **탐색/목록**: 사용자가 전체 수를 알고 싶어하고, 데이터 변경 빈도가 낮아 오프셋 기반 적합

## Related

- [API 엔드포인트](../entities/api-endpoints.md) -- 두 방식이 적용된 엔드포인트 상세
- [데이터베이스 스키마](../entities/database-schema.md) -- 페이지네이션을 지원하는 인덱스
