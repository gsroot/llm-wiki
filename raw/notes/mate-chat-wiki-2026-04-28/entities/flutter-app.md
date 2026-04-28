---
title: "Flutter Application"
type: entity
source_count: 3
tags: [frontend, flutter, dart, riverpod, mobile]
related:
  - "../entities/fastapi-app.md"
  - "../concepts/websocket-realtime.md"
---

# Flutter Application

## Overview

Mate Chat의 크로스 플랫폼 프론트엔드 애플리케이션이다. iOS, Android, Web을 단일 코드베이스로 지원한다. 리마스터에서 Flutter 프레임워크 자체는 유지하되, API 연동과 상태 관리 구조를 개선했다.

## Architecture/Structure

```
mate_chat_flutter/lib/
├── core/
│   ├── auth/          # 토큰 저장 및 관리
│   ├── network/       # Dio API 클라이언트, JWT 인터셉터
│   ├── websocket/     # WsClient, 자동 재연결
│   ├── theme/         # Material Design 3 + 다크/라이트
│   ├── routing/       # GoRouter, 30+ 라우트
│   └── utils/
├── features/          # 기능별 모듈 (auth, chat, chatbot, social, profile, home, settings, purchase)
├── repositories/      # 7개 API 연동 Repository
├── models/            # 데이터 모델
└── ui/components/     # 50+ 재사용 컴포넌트
```

총 132개 Dart 파일, 51,960줄 코드

## Key Details

- **상태 관리**: Riverpod 2.5.0 + riverpod_generator
- **HTTP**: Dio 5.4.0 (인터셉터로 JWT 자동 갱신)
- **WebSocket**: web_socket_channel, 자동 재연결 (지수 백오프 1s-30s), 하트비트 30초, 오프라인 큐잉
- **로컬 저장소**: FlutterSecureStorage (JWT), Hive (캐시)
- **라우팅**: GoRouter 17.0.0 (딥링크 지원)
- **국제화**: 9개 언어 ARB
- **테마**: Material Design 3, Pretendard 폰트

## Dependencies

- Flutter SDK (stable)
- Dart 3.10.1+
- Riverpod, Dio, GoRouter, Hive, google_sign_in, sign_in_with_apple

## Known Issues

- iOS 앱 빌드 및 App Store 배포 대기 중
- Apple Sign-in 미구현 (iOS 출시 시 필요)

## Related

- [FastAPI Application](../entities/fastapi-app.md) -- 백엔드 API 연동
- [WebSocket Realtime](../concepts/websocket-realtime.md) -- 실시간 채팅
