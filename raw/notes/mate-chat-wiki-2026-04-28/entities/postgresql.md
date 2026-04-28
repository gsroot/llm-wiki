---
title: "PostgreSQL"
type: entity
source_count: 3
tags: [database, postgresql, rdbms, sqlalchemy, alembic]
related:
  - "../entities/fastapi-app.md"
  - "../entities/redis.md"
  - "../concepts/layered-architecture.md"
---

# PostgreSQL

## Overview

Mate Chat의 주 데이터 저장소이다. Firestore(NoSQL)에서 PostgreSQL 17(RDBMS)로 전환하여 데이터 무결성, 트랜잭션, 복잡한 쿼리(JOIN, 집계)를 지원한다. 24개 테이블 (23개 활성 + 1개 deprecated)로 구성된다.

## Architecture/Structure

### 테이블 그룹 (24개: 23개 활성 + 1개 deprecated)

- **인증 & 사용자** (5): users, user_sessions, email_verifications, password_resets, auth_methods
- **소셜** (5): follows, mates, mate_requests, blocks, follow_logs
- **채팅** (7): chat_rooms, chat_room_members, chat_messages, chat_room_invites, chat_room_bots, chat_room_bot_settings, chat_room_member_logs
- **AI** (2): chatbots, chatbot_mates
- **기타** (5): notifications, clover_transactions, device_tokens, user_reports, data_export_requests

### 연결 관리

- 비동기 연결 풀: asyncpg 드라이버
- SQLAlchemy 2.0 async 세션
- 최대 연결 수 제한 및 타임아웃 설정

## Key Details

- **버전**: PostgreSQL 17
- **ORM**: SQLAlchemy 2.0 (asyncio 모드)
- **마이그레이션**: Alembic (13개 마이그레이션 이력)
- **활용 기능**: JSONB (메타데이터), Array (언어 목록), Full-text Search (메시지 검색), UUID (기본 키)
- **ACID 보장**: 트랜잭션, 외래키, 제약조건으로 데이터 무결성 확보

## Dependencies

- asyncpg (비동기 드라이버)
- SQLAlchemy 2.0+ (ORM)
- Alembic (마이그레이션)

## Known Issues

- Firestore에서의 마이그레이션 시 NoSQL 서브컬렉션 -> 관계형 테이블 변환 복잡성 (이미 완료)
- WebSocket 연결이 DB 풀 슬롯 장기 점유 가능

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 애플리케이션 서버
- [Redis](../entities/redis.md) -- 캐시 계층
- [Layered Architecture](../concepts/layered-architecture.md) -- Repository 패턴으로 접근
