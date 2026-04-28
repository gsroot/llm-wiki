# Wiki Activity Log

## [2026-04-07] lint+fix | 위키 품질 점검 및 수정

Lint 감사 + 코드 대조 검증 후 10개 이슈 수정.

### CRITICAL 수정
- 출시 상태 모순 해소: synthesis 2개 페이지 → v1.0.0 출시 완료로 통일
- PostgreSQL 버전: 15 → **17**로 4개 파일 수정

### HIGH 수정
- JWT 만료 시간: 환경별 설정 차이를 3개 페이지에 정확히 기술
- 테이블 수: 20 → **24개 (23 active + 1 deprecated)**로 수정
- 다중 기기 WebSocket: `Set[WebSocket]` 다중 지원으로 수정
- index.md Entity 카운트: 20 → 21

### MEDIUM 수정
- Clover 엔티티 페이지 신규 생성 (`entities/clover-system.md`)
- `websocket-realtime.md` 크로스 레퍼런스 4개 추가
- `fastapi-app.md` → `sentry.md` 링크 추가

### 통계
- 수정 파일: 14개
- 신규 파일: 1개 (clover-system.md)
- 총 위키 페이지: **65개** (+ 메타 3개 = 68)

---

## [2026-04-07] ingest | 레거시 아카이브 수집 (docs/_archive/ 8개 문서)

`docs/_archive/`의 Firebase 레거시 문서 8개(01~06, 17, 18)를 통합 수집.

### 생성
- Sources 1개: `archive-legacy-system.md` (8개 레거시 문서 통합 요약)

### 수정 (Historical Context 추가)
- `concepts/vendor-independence.md` — Security Rules 방치 이슈, 테스트 불가 문제 추가
- `entities/database-schema.md` — Firestore 서브컬렉션 → PostgreSQL 정규화 배경 추가
- `entities/auth-system.md` — Firebase Auth → JWT 전환 이유 (세션 제어 한계) 추가
- `index.md` — Sources 카운트 18→19, 아카이브 항목 추가

### 주요 발견
- Firestore Security Rules가 `allow: true`로 방치 → 리마스터 보안 강화의 직접적 계기
- 레거시 테스트 0개 → Firebase 에뮬레이터 복잡성이 원인
- Facebook OAuth 레거시에 존재 → 리마스터에서 제거 (Google + Apple로 전환)
- 클로버 경제 구조(생성 -10, 채팅 -5, 수익 +1)는 레거시부터 동일
- Strangler Fig 마이그레이션 계획 수립했으나, 실제로는 클린 스타트로 진행

---

## [2026-04-07] ingest | 전체 일괄 수집 (5개 그룹 병렬)

18개 원시 문서(`docs/`)를 5개 병렬 에이전트로 수집. 총 **62개 위키 페이지** 생성.

### Group 1: Core Architecture (docs/10, 11, 12)
- Sources 3개: remaster-overview, tech-stack, system-architecture
- Entities 7개: fastapi-app, postgresql, redis, minio, docker-infrastructure, sentry, flutter-app
- Concepts 5개: layered-architecture, async-first, vendor-independence, websocket-realtime, hybrid-ai-chat

### Group 2: Data & API (docs/13, 14)
- Sources 2개: database-schema, api-design
- Entities 2개: database-schema, api-endpoints
- Concepts 5개: repository-pattern, pydantic-schema-design, api-versioning, soft-delete, cursor-vs-offset-pagination

### Group 3: Features (docs/15, 16)
- Sources 2개: auth-system, realtime-websocket
- Entities 5개: auth-system, jwt-tokens, oauth-providers, websocket-manager, redis-pubsub
- Concepts 5개: oauth-flow, jwt-token-lifecycle, websocket-connection-management, real-time-messaging, typing-indicators, read-receipts
- **발견된 모순**: 토큰 만료 시간 (설계 문서 15분/7일 vs CLAUDE.md 7일/6개월)
- **발견된 오류**: Apple OAuth 알고리즘 (문서 HS256 → 실제 RS256/ES256)
- **알려진 한계**: ConnectionManager user_id당 단일 WebSocket 매핑

### Group 4: Operations (docs/19, 20, 21, 22, 28 + QA 문서)
- Sources 5개: implementation-status, push-notification-e2e, push-session-ops, mobile-release, deployment-guide
- Entities 4개: push-notification-system, fcm-integration, docker-deployment, ci-cd-pipeline
- Concepts 3개: deployment-pipeline, push-notification-flow, release-process
- Synthesis 1개: implementation-status

### Group 5: Global Launch (docs/23~27 + _launch-prep/)
- Sources 6개: play-store-listing, flutter-i18n, localization-glossary, global-launch-readiness, competitive-analysis, launch-prep
- Entities 3개: google-play-store, in-app-purchase, i18n-system
- Concepts 3개: internationalization-strategy, competitive-landscape, app-store-optimization
- Synthesis 1개: launch-readiness

### 통계
| 카테고리 | 파일 수 |
|----------|---------|
| Sources | 18 |
| Entities | 21 |
| Concepts | 21 |
| Synthesis | 2 |
| **합계** | **62** |

---

## [2026-04-07] init | Wiki 초기화
- 디렉토리 구조 생성: `entities/`, `concepts/`, `sources/`, `synthesis/`
- SCHEMA.md 작성 (운영 규칙, 페이지 타입, 워크플로우)
- index.md, log.md 생성
- 원시 소스: `docs/` 18개+ 문서 식별 완료
