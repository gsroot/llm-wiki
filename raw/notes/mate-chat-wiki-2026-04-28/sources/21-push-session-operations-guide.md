---
title: "Push/Session Operations Guide"
type: source
source_path: docs/21-push-session-operations-guide.md
date_ingested: 2026-04-07
tags: [push-notification, session, operations, fcm, firebase, sentry]
related:
  - ../entities/push-notification-system.md
  - ../entities/fcm-integration.md
  - ../concepts/push-notification-flow.md
  - ./20-push-notification-e2e-checklist.md
---

## 요약

Mate Chat의 푸시 알림 및 세션 처리에 대한 운영 정책 문서이다. E2E 체크리스트(docs/20)에서 검증된 결과를 기반으로 런타임 정책, 배달 결정 기준, 인시던트 대응 절차를 정의한다.

## 핵심 내용

### Delivery Policy Matrix
| 수신자 상태 | 동작 |
|------------|------|
| Foreground, 다른 화면 | 로컬 알림 표시 |
| Foreground, 같은 채팅방 | 로컬 알림 억제 |
| Foreground, 카테고리 비활성 | 로컬 알림 억제 |
| Background | 시스템 푸시 발송 |
| Terminated | 시스템 푸시 발송 |
| Online (WebSocket 활성) | 시스템 푸시 억제 |
| Offline | 시스템 푸시 발송 |

### Best-Practice Rules
- `notifications` 테이블이 알림 히스토리의 source of truth
- Redis 공유 presence로 온라인/오프라인 판단 (in-process 메모리 X)
- Cold-start 시 auth bootstrap 완료 전 네비게이션 금지
- 토큰 등록은 인증 세션 존재 후에만 수행
- 네트워크 장애 시 세션 유지 (transient failure에 로그아웃 금지)

### 인시던트 대응 체크리스트
- "알림 레코드 있으나 푸시 미수신" 시: 8단계 트리아지
- "푸시 탭 시 잘못된 화면" 시: 5단계 트리아지

### 환경 설정
- Firebase: ADC 모드 선호, `FIREBASE_CREDENTIALS_PATH` 비워두기
- Sentry: `staging`/`production` 환경에서만 초기화
