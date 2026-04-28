---
name: migration-safety
description: >
  Alembic 마이그레이션을 생성하거나 수정할 때, 스키마를 변경하거나 Mate Chat의 PostgreSQL 데이터베이스 테이블을
  변경할 때 데이터베이스 마이그레이션의 안전성을 검증합니다. 다음 키워드 사용 시 활성화됩니다: "마이그레이션", "migration",
  "alembic", "데이터베이스 변경", "스키마 변경", "테이블", "컬럼 추가". 데이터 손실을 방지하고 롤백 계획을 보장합니다.
allowed-tools:
  - Read
  - Grep
  - Bash
---

# 마이그레이션 안전성 검증

Alembic 데이터베이스 마이그레이션의 안전성을 자동으로 검증하고 데이터 손실을 방지합니다.

## 개요

**Mate Chat 데이터베이스**: PostgreSQL, 20개 테이블, 13개 마이그레이션

**이 스킬은 다음을 보장합니다**:
- 파괴적 변경 감지 (DROP, ALTER)
- 롤백 계획 존재 확인
- 데이터 손실 방지
- 마이그레이션 테스트 가이드
- 프로덕션 배포 안전성

---

## 관련 시스템

**Slash Command:** `/migrate` (사용자 명시적 호출)
- 사용자가 `/migrate create add_user_preferences` 형식으로 마이그레이션 작업 시작
- Alembic 마이그레이션 생성, 적용, 롤백 작업을 명시적으로 시작

**Sub-Agent:** `data-schema-engineer` (자동 호출)
- 복잡한 데이터베이스 스키마 설계 및 마이그레이션 시 자동으로 호출되는 전문가
- 테이블 관계, 인덱스 최적화, 데이터 무결성 전문가
- 트리거 조건: 새 테이블 추가, 복잡한 스키마 변경, 데이터 마이그레이션

**Agent Skill:** `migration-safety` (이 스킬 - 자동 트리거)
- 트리거: Alembic 마이그레이션 파일 생성/수정 시 자동 실행
- 역할: 파괴적 변경 감지, 롤백 계획 확인, 데이터 손실 방지 자동 검증

**차이점:**
- **Slash Command (`/migrate`)**: 사용자가 명시적으로 입력하여 마이그레이션 시작
- **Sub-Agent (`data-schema-engineer`)**: 복잡한 스키마 설계 시 자동 호출
- **Agent Skill (`migration-safety`)**: 마이그레이션 작성 후 자동으로 안전성 검증

---

## 빠른 체크리스트

마이그레이션 생성/적용 전:

- [ ] ✅ 파괴적 변경 없음 (DROP TABLE, DROP COLUMN)
- [ ] ✅ NOT NULL 추가 시 기본값 존재
- [ ] ✅ 롤백 계획 문서화됨
- [ ] ✅ 마이그레이션 up/down 테스트됨
- [ ] ✅ 프로덕션 데이터 영향 평가됨
- [ ] ✅ 인덱스 생성 타이밍 고려됨
- [ ] ✅ 데이터 백업 계획 있음

전체 체크리스트는 [migration-checklist.md](./references/migration-checklist.md)를 참조하세요.

---

## 파괴적 변경 감지

### 자동 감지 스크립트

```bash
cd mate_chat_backend
python ../.Codex/skills/migration-safety/scripts/check-migration.py
```

**감지하는 위험한 작업**:
- `DROP TABLE` - 테이블 삭제
- `DROP COLUMN` - 컬럼 삭제
- `ALTER COLUMN ... DROP NOT NULL` - NULL 허용으로 변경
- `ALTER COLUMN TYPE` - 타입 변경 (데이터 손실 가능)

### 안전한 대안

**테이블/컬럼 제거**:
```python
# ❌ 위험: 즉시 삭제
op.drop_column('users', 'old_field')

# ✅ 안전: 2단계 프로세스
# Step 1: 컬럼을 nullable로 변경 (배포)
op.alter_column('users', 'old_field', nullable=True)

# Step 2: 나중에 컬럼 삭제 (다음 릴리스)
op.drop_column('users', 'old_field')
```

**NOT NULL 추가**:
```python
# ❌ 위험: 기존 NULL 데이터로 실패
op.alter_column('users', 'email', nullable=False)

# ✅ 안전: 기본값 먼저 설정
op.alter_column('users', 'email',
    server_default='unknown@example.com')
op.alter_column('users', 'email', nullable=False)
```

상세 예시는 [migration-checklist.md](./references/migration-checklist.md#안전한-마이그레이션-패턴)을 참조하세요.

---

## 롤백 계획

### 롤백 템플릿

모든 마이그레이션에는 롤백 계획이 필요합니다:

```python
"""add new column to users table

Revision ID: abc123
Revises: def456
Create Date: 2025-01-16 10:00:00

Rollback Plan:
1. Run: alembic downgrade -1
2. Verify: SELECT * FROM users LIMIT 1 (컬럼 없어야 함)
3. If issues: [구체적 복구 절차]
"""

def upgrade():
    op.add_column('users', sa.Column('new_field', sa.String(100)))

def downgrade():
    op.drop_column('users', 'new_field')
```

롤백 템플릿 및 상세 가이드는 [rollback-template.md](./references/rollback-template.md)를 참조하세요.

---

## 마이그레이션 테스트 절차

### 로컬 테스트

```bash
cd mate_chat_backend

# 1. 현재 상태 확인
alembic current

# 2. 마이그레이션 적용
alembic upgrade head

# 3. 데이터 확인
psql postgresql://... -c "SELECT * FROM table_name LIMIT 5"

# 4. 롤백 테스트
alembic downgrade -1

# 5. 데이터 확인 (원복되었는지)
psql postgresql://... -c "SELECT * FROM table_name LIMIT 5"

# 6. 다시 적용
alembic upgrade head
```

### 스테이징 테스트

```bash
# 1. 스테이징 DB 백업
pg_dump staging_db > backup_$(date +%Y%m%d).sql

# 2. 마이그레이션 적용
alembic upgrade head

# 3. 애플리케이션 테스트

# 4. 문제 발생 시 롤백
alembic downgrade -1
# 또는 백업에서 복원
psql staging_db < backup_20250116.sql
```

---

## 인덱스 생성 고려사항

### CONCURRENTLY 옵션 사용

프로덕션에서 인덱스 생성 시:

```python
from alembic import op

def upgrade():
    # ❌ 위험: 테이블 잠금
    op.create_index('idx_users_email', 'users', ['email'])

    # ✅ 안전: 잠금 없이 생성
    op.create_index('idx_users_email', 'users', ['email'],
                   postgresql_concurrently=True)
```

**주의**: CONCURRENTLY는 트랜잭션 밖에서 실행되어야 합니다:

```python
from alembic import op
from sqlalchemy import text

def upgrade():
    conn = op.get_bind()
    conn.execute(text('COMMIT'))  # 트랜잭션 종료
    conn.execute(text(
        'CREATE INDEX CONCURRENTLY idx_users_email ON users (email)'
    ))
```

---

## 주요 주의사항

1. **항상 롤백 계획 작성** - downgrade() 함수 구현 필수
2. **테스트 환경에서 먼저** - 로컬 → 스테이징 → 프로덕션
3. **데이터 백업 필수** - 프로덕션 적용 전 반드시 백업
4. **NOT NULL 주의** - 기존 데이터 확인 후 적용
5. **인덱스는 CONCURRENTLY** - 프로덕션에서 잠금 방지
6. **스크립트 검증 사용** - check-migration.py로 자동 검증

---

## 일반적인 문제 및 해결

### 문제 1: "column contains null values"

```sql
-- 원인: NOT NULL 추가 시 기존 NULL 데이터 존재

-- 해결책 1: 기본값 설정
UPDATE users SET email = 'unknown@example.com' WHERE email IS NULL;
ALTER TABLE users ALTER COLUMN email SET NOT NULL;

-- 해결책 2: 마이그레이션에서 처리
op.execute("UPDATE users SET email = 'unknown@example.com' WHERE email IS NULL")
op.alter_column('users', 'email', nullable=False)
```

### 문제 2: "cannot drop table because other objects depend on it"

```sql
-- 원인: 외래 키 참조 존재

-- 해결책: 외래 키 먼저 삭제
op.drop_constraint('fk_posts_user_id', 'posts', type_='foreignkey')
op.drop_table('users')
```

### 문제 3: 마이그레이션 충돌

```bash
# 원인: 여러 브랜치에서 동시에 마이그레이션 생성

# 해결책: 마이그레이션 병합
alembic merge <rev1> <rev2> -m "merge migrations"
```

상세 트러블슈팅은 [migration-checklist.md](./references/migration-checklist.md#트러블슈팅)을 참조하세요.

---

## 참조 파일

### 상세 가이드
- **[migration-checklist.md](./references/migration-checklist.md)** - 완전한 체크리스트, 안전한 패턴, 트러블슈팅
- **[rollback-template.md](./references/rollback-template.md)** - 롤백 계획 템플릿 및 예시

### 자동화 도구
- **[scripts/check-migration.py](./scripts/check-migration.py)** - 파괴적 변경 자동 감지 스크립트

---

**기억하세요**: 데이터는 코드보다 중요합니다. 신중한 마이그레이션이 재앙을 예방합니다!
