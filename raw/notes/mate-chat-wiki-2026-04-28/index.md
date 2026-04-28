# Mate Chat Wiki Index

> LLM이 유지관리하는 프로젝트 지식 베이스. 규칙: [SCHEMA.md](SCHEMA.md)

## Sources (19개)

- [리마스터 개요](sources/10-remaster-overview.md) — Firebase -> FastAPI 전면 전환 계획, 5단계 마이그레이션
- [기술 스택](sources/11-tech-stack-new.md) — 리마스터 후 전체 기술 스택 선택 근거
- [시스템 아키텍처](sources/12-system-architecture.md) — 4계층 시스템 아키텍처, 데이터 흐름, 보안/확장성
- [데이터베이스 스키마](sources/13-database-schema.md) — 16개(→20개) 테이블, Firestore 마이그레이션 매핑
- [API 설계](sources/14-api-design.md) — RESTful API 사양, 83개 엔드포인트, Rate Limiting
- [인증 시스템](sources/15-auth-system.md) — OAuth, JWT, 이메일 인증, 세션 관리
- [실시간 WebSocket](sources/16-realtime-websocket.md) — WebSocket 연결 관리, 메시지 프로토콜, Redis Pub/Sub
- [구현 현황](sources/19-implementation-status.md) — 전체 기능 구현 85% 완료, 83개 API, 31개 화면
- [푸시 알림 E2E 체크리스트](sources/20-push-notification-e2e-checklist.md) — 7회 세션 검증 로그
- [푸시/세션 운영 가이드](sources/21-push-session-operations-guide.md) — 배달 결정 매트릭스, 인시던트 대응
- [모바일 릴리스 체크리스트](sources/22-mobile-release-checklist.md) — 13개 게이트, 출시 금지 조건
- [Play Store 등록정보](sources/23-google-play-store-listing.md) — ASO 키워드, 다국어 현지화
- [Flutter i18n 준비](sources/24-flutter-i18n-preparation.md) — 9개 locale, 141개 키, 하드코딩 잔존
- [로컬라이제이션 용어집](sources/25-localization-glossary.md) — 제품 용어 고정 규칙, 번역 워크플로우
- [글로벌 출시 진단](sources/26-global-launch-readiness.md) — CRITICAL 3건, HIGH 2건, OK 5건
- [경쟁 앱 분석](sources/27-competitive-analysis.md) — 33개 경쟁 앱, 시장 포지셔닝
- [배포 가이드](sources/28-deployment-guide.md) — 3종 파이프라인, 인프라, GitHub Secrets
- [출시 준비 종합](sources/launch-prep.md) — 글로벌 전략, IAP 상품, Phase 0~4 로그
- [레거시 시스템 아카이브](sources/archive-legacy-system.md) — Firebase 레거시 8개 문서 통합, 마이그레이션 의사결정 맥락

## Entities (21개)

### Infrastructure
- [FastAPI App](entities/fastapi-app.md) — 백엔드 서버, 83개 API, 4계층 구조
- [PostgreSQL](entities/postgresql.md) — 주 데이터베이스, 24개 테이블, asyncpg
- [Redis](entities/redis.md) — 캐시, Rate Limiting, Pub/Sub
- [MinIO](entities/minio.md) — S3 호환 객체 스토리지
- [Docker Infrastructure](entities/docker-infrastructure.md) — Docker Compose 4서비스 + K8s
- [Docker Deployment](entities/docker-deployment.md) — 2개 Compose 프로젝트, Traefik, 롤백
- [Sentry](entities/sentry.md) — 에러 추적 및 APM
- [CI/CD Pipeline](entities/ci-cd-pipeline.md) — 4개 워크플로우, 브랜치 전략

### Application
- [Flutter App](entities/flutter-app.md) — 크로스 플랫폼 앱, 132파일/51,960줄
- [Auth System](entities/auth-system.md) — 인증 시스템 전체, 13개 API
- [JWT Tokens](entities/jwt-tokens.md) — Access/Refresh 토큰 구조, 검증 프로세스
- [OAuth Providers](entities/oauth-providers.md) — Google(완료), Apple(미구현)
- [Database Schema](entities/database-schema.md) — 24개 테이블, 5개 도메인 그룹
- [API Endpoints](entities/api-endpoints.md) — 83개 엔드포인트, 9개 도메인

### Real-time & Messaging
- [WebSocket Manager](entities/websocket-manager.md) — 연결 관리자, 메시지 핸들링
- [Redis Pub/Sub](entities/redis-pubsub.md) — 분산 WebSocket, 채널 패턴
- [Push Notification System](entities/push-notification-system.md) — 7가지 알림 타입, delivery policy
- [FCM Integration](entities/fcm-integration.md) — Firebase Cloud Messaging 연동

### Distribution
- [Google Play Store](entities/google-play-store.md) — 배포 채널, Staged Rollout
- [In-App Purchase](entities/in-app-purchase.md) — 클로버 5개 번들, 검증 흐름
- [Clover System](entities/clover-system.md) — 가상 화폐, Welcome 보너스, IAP 검증
- [i18n System](entities/i18n-system.md) — Flutter ARB + 백엔드 푸시 i18n

## Concepts (22개)

### Architecture
- [Layered Architecture](concepts/layered-architecture.md) — 4계층 시스템 + 3계층 앱 분리
- [Async-First](concepts/async-first.md) — 모든 I/O를 async/await로 처리
- [Vendor Independence](concepts/vendor-independence.md) — Firebase 종속성 제거, 자체 호스팅
- [Repository Pattern](concepts/repository-pattern.md) — 백엔드 6개 + Flutter 7개 Repository

### Data & API
- [Pydantic Schema Design](concepts/pydantic-schema-design.md) — Create/Update/Response 분리
- [API Versioning](concepts/api-versioning.md) — URL path 기반 /v1/ 전략
- [Soft Delete](concepts/soft-delete.md) — deleted_at 패턴, Partial 인덱스
- [Cursor vs Offset Pagination](concepts/cursor-vs-offset-pagination.md) — 메시지(커서)/목록(오프셋) 이원화

### Auth
- [OAuth Flow](concepts/oauth-flow.md) — Google 7단계, Apple 4단계
- [JWT Token Lifecycle](concepts/jwt-token-lifecycle.md) — 발급→사용→갱신→무효화→만료

### Real-time
- [WebSocket Realtime](concepts/websocket-realtime.md) — 양방향 실시간 통신, Pub/Sub 분산
- [WebSocket Connection Management](concepts/websocket-connection-management.md) — 하트비트, 지수 백오프
- [Real-time Messaging](concepts/real-time-messaging.md) — 메시지 전송 흐름, 상태 동기화
- [Typing Indicators](concepts/typing-indicators.md) — 비저장형, 브로드캐스트 전용
- [Read Receipts](concepts/read-receipts.md) — last_read_at 기반, DB 영구 저장
- [Hybrid AI Chat](concepts/hybrid-ai-chat.md) — 사람+AI 혼합, 트리거 멘션, 컨텍스트 윈도우

### Operations
- [Deployment Pipeline](concepts/deployment-pipeline.md) — 백엔드/Flutter 배포 흐름, 환경 분리
- [Push Notification Flow](concepts/push-notification-flow.md) — 발생→배달 결정→수신
- [Release Process](concepts/release-process.md) — 13개 게이트, 출시 금지 조건

### Launch
- [Internationalization Strategy](concepts/internationalization-strategy.md) — 한국어 SOT, 단계적 확장
- [Competitive Landscape](concepts/competitive-landscape.md) — 시장 4분면, 하이브리드 AI 공백
- [App Store Optimization](concepts/app-store-optimization.md) — 키워드 클러스터, 다국어 ASO

## Synthesis (2개)

- [구현 현황 종합](synthesis/implementation-status.md) — 완료/진행 중/미완료, 기술 부채, 핵심 수치
- [글로벌 출시 준비 종합](synthesis/launch-readiness.md) — 완료 항목, 남은 블로커, 전략, 경쟁 포지셔닝
