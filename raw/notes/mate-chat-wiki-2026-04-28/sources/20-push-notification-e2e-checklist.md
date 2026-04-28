---
title: "Push Notification E2E Checklist"
type: source
source_path: docs/20-push-notification-e2e-checklist.md
date_ingested: 2026-04-07
tags: [push-notification, fcm, e2e-testing, mobile, qa]
related:
  - ../entities/push-notification-system.md
  - ../entities/fcm-integration.md
  - ../concepts/push-notification-flow.md
  - ./21-push-session-operations-guide.md
---

## 요약

푸시 알림 시스템의 E2E(End-to-End) 검증 체크리스트 및 실제 테스트 세션 로그를 기록한 문서이다. 2026-03-04부터 2026-03-11까지 총 7회의 세션을 통해 전체 항목을 검증 완료하였다.

## 핵심 내용

### 테스트 범위
- Token lifecycle: 로그인 등록, 로그아웃 해제, 전체 알림 ON/OFF 토큰 동기화
- Feature flow: 7가지 알림 타입별 알림 레코드 생성 검증 (follow, mate_request, mate, invite, force_exit, manager_transfer, chat)
- Foreground handling: 로컬 알림 표시, 같은 채팅방 내 중복 억제, 카테고리 필터
- Background/Terminated handling: 시스템 푸시 수신 및 딥링크 라우팅
- Online/Offline push gating: Redis 기반 공유 presence를 통한 중복 방지
- Failure/Recovery: 잘못된 토큰 정리, 권한 거부 안정성, 네트워크 장애 복구

### 검증 과정에서 발견 및 수정한 버그
1. 백그라운드 WebSocket 재연결 버그 - 백그라운드 사용자를 온라인으로 잘못 판단
2. 알림 탭 시 토큰 리프레시 경쟁 조건 - 동시 API 요청으로 인한 강제 로그아웃
3. `ChatPage.dispose()` Riverpod 접근 버그
4. 인증 전 device-token 등록 시도 문제
5. Cold-start 알림 탭 시 딥링크 목적지 유실
6. 오프라인 재시작 시 로그인 화면 회귀 문제

### 세션 로그
- Session 11 (2026-03-04): 초기 스모크 체크
- Session 12 (2026-03-04): API/DB 크로스체크로 토큰 및 기능 플로우 검증
- Session 13 (2026-03-11): Firebase ADC 기반 실제 푸시 E2E
- Session 14 (2026-03-11): 온라인 게이팅 및 terminated cold-start 재검증
- Session 15 (2026-03-11): 오프라인 복구 및 실패 케이스
- Session 16 (2026-03-11): 네트워크 장애 중 토큰 등록 검증
- Session 17 (2026-03-11): 오프라인 시작 시 세션 UX 수정
