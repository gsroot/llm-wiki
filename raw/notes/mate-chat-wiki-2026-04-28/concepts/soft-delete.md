---
title: "Soft Delete 패턴"
type: concept
source_count: 1
tags: [database, pattern, deletion, postgresql]
related:
  - ../entities/database-schema.md
  - ../concepts/repository-pattern.md
---

# Soft Delete 패턴

## Definition

Soft Delete는 데이터를 물리적으로 삭제(DELETE)하지 않고, `deleted_at` 타임스탬프 컬럼을 설정하여 논리적으로 삭제 상태를 표시하는 패턴이다. 삭제된 데이터는 일반 쿼리에서 제외되지만, 데이터베이스에는 보존된다.

## How It Works in Mate Chat

### Soft Delete 적용 테이블

4개 테이블에 `deleted_at TIMESTAMPTZ` 컬럼이 존재한다:

| 테이블 | 용도 |
|--------|------|
| users | 계정 탈퇴 (개인정보 보존 기간 필요) |
| chat_rooms | 채팅방 삭제 (메시지 히스토리 보존) |
| chat_messages | 메시지 삭제 (신고 증거 보존) |
| chatbots | 챗봇 삭제 (사용 통계 보존) |

### Partial 인덱스 활용

Soft Delete와 함께 partial 인덱스를 사용하여, 활성 데이터만 인덱싱한다:

```sql
-- 활성 사용자만 국가별 인덱스
CREATE INDEX idx_users_country ON users(country_code) WHERE deleted_at IS NULL;

-- 활성 사용자의 언어 인덱스
CREATE INDEX idx_users_languages ON users USING GIN(languages) WHERE deleted_at IS NULL;

-- 공개 챗봇만 인덱스
CREATE INDEX idx_chatbots_public ON chatbots(is_public, created_at DESC) WHERE deleted_at IS NULL;
```

### Hard Delete 사용 테이블

일부 테이블은 FK의 `ON DELETE CASCADE`로 물리적 삭제를 수행한다:

- user_sessions, follows, mates, mate_requests, blocks, chat_room_members, notifications, device_tokens

### left_at 패턴 (유사 Soft Delete)

`chat_room_members` 테이블은 `left_at` 컬럼으로 멤버 탈퇴를 표시한다. `left_at IS NULL`이면 활성 멤버이며, partial 인덱스가 적용된다.

## Trade-offs

### 장점

- **데이터 복구 가능**: 실수로 삭제된 데이터 복원 가능
- **감사 추적**: 삭제 시점 기록 보존
- **규정 준수**: 개인정보 보존 기간 요구사항 충족
- **참조 무결성 유지**: 다른 테이블에서 참조하는 데이터의 FK 위반 방지

### 단점

- **쿼리 복잡성**: 모든 쿼리에 `WHERE deleted_at IS NULL` 조건 필요
- **저장 공간 증가**: 삭제된 데이터가 계속 저장됨
- **인덱스 비효율**: Partial 인덱스로 완화하지만, 완전하지 않음
- **UNIQUE 제약 충돌**: 삭제된 레코드의 유니크 값이 재사용 불가 (예: email)

### Mate Chat에서의 완화 전략

- Partial 인덱스로 활성 데이터만 인덱싱하여 성능 유지
- Repository 계층에서 `deleted_at IS NULL` 조건을 기본 적용하여 쿼리 누락 방지

## Related

- [데이터베이스 스키마](../entities/database-schema.md) -- Soft Delete가 적용된 테이블 상세
- [Repository 패턴](../concepts/repository-pattern.md) -- Soft Delete 조건이 적용되는 계층
