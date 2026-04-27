---
title: "컴투스플랫폼 Gmail 스레드 인덱스"
type: source-index
company: com2us-platform
source: gmail
collected_at: "2026-04-24"
status: blocked-auth
---

# Gmail — 스레드 인덱스

컴투스플랫폼 재직 관련 주요 Gmail 스레드의 **메타 정보만**을 담은 공개 인덱스입니다.

🔒 **중요**: 본문 인용 금지. PII/사내 기밀 노출 방지를 위해 본문은 `private/gmail/`에만 저장하고 이 인덱스에는 **제목 + 날짜 + 관련 프로젝트 태그**만 기록.

## 수집 상태

- 📅 **마지막 시도**: 2026-04-24
- 🚫 **상태**: **BLOCKED — Gmail MCP 서버 토큰 만료 (re-authorization 필요)**
- ✅ **재수집 조건**: `mcp__claude_ai_Gmail__*` 도구 재인증 후 Phase E 재실행
- 🔑 **목적별 쿼리** (재시도 예정):
  - `(from:me OR to:me) (회고 OR 평가 OR 리뷰 OR 성과 OR KPT OR retrospective) after:2022/01/01`
  - `(from:me OR to:me) (프로젝트 완료 OR 릴리즈 OR 배포 OR launch OR release) after:2022/01/01`
  - `(from:me OR to:me) (피드백 OR 칭찬 OR 감사 OR 수고 OR feedback OR thanks) after:2022/01/01`
- 🔍 **수집 방법**: [`docs/00-meta/collection-strategy.md#️-gmail`](../../../00-meta/collection-strategy.md)

## 스레드 목록 (메타만)

> Phase E 수집은 인증 실패로 중단. 재인증 후 채움.

### 회고/평가/리뷰
| 제목 | 날짜 | 관련 프로젝트 | Thread ID |
|------|------|------------|-----------|
| _(수집 보류 — 인증 필요)_ | | | |

### 릴리즈/배포 공지
| 제목 | 날짜 | 관련 프로젝트 | Thread ID |
|------|------|------------|-----------|
| _(수집 보류 — 인증 필요)_ | | | |

### 피드백/감사
| 제목 | 날짜 | 관련 프로젝트 | Thread ID |
|------|------|------------|-----------|
| _(수집 보류 — 인증 필요)_ | | | |

## 매핑

`docs/20-projects/com2us-platform/` 프로젝트 문서의 `sources.gmail` 필드에 **private 경로**로 참조. Output 문서(`50-portfolio/`)에서는 절대 인용하지 않음.
