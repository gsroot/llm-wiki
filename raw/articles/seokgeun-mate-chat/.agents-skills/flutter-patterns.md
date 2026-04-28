---
name: flutter-patterns
description: >
  Mate Chat 앱에서 위젯, 화면, 기능을 생성할 때 Flutter 코드 패턴을 강제합니다.
  기능 기반 아키텍처, Riverpod 상태 관리, GoRouter 통합, Material Design 3 사용을 보장합니다.
  Flutter 코드 생성 또는 수정 시 자동으로 트리거됩니다.
allowed-tools:
  - Read
  - Grep
  - Glob
---

# Flutter 코드 패턴

Mate Chat 앱에서 일관된 Flutter 코드 패턴을 강제합니다.

## 개요

**Mate Chat Flutter 앱** (132개 Dart 파일, 51,960줄):
- 상태 관리: Riverpod 2.5.0
- 라우팅: GoRouter 17.0.0
- HTTP: Dio 5.4.0
- WebSocket: web_socket_channel 2.4.0
- 테마: Material Design 3 + shadcn/ui 패턴
- 폰트: Pretendard (한국어 최적화)

**이 스킬은 모든 Flutter 코드가 프로젝트 표준을 따르도록 보장합니다.**

---

## 관련 시스템

**Slash Command:** `/flutter` (사용자 명시적 호출)
- 사용자가 `/flutter 채팅방 설정 화면 만들기` 형식으로 Flutter 작업 시작
- Flutter 위젯, 기능, 버그 수정 작업을 명시적으로 시작

**Sub-Agent:** `flutter-app-expert` (자동 호출)
- 복잡한 Flutter 기능 구현 시 자동으로 호출되는 전문가 에이전트
- Feature-based 아키텍처, Riverpod 상태관리, WebSocket 통합 전문가
- 트리거 조건: 새 화면 생성, 상태 관리 구현, API 연동, 성능 최적화

**Sub-Agent:** `flutter-ui-ux-expert` (디자인 작업 시)
- UI 디자인, 애니메이션, 스타일링 전문가
- `flutter-app-expert`는 기능/로직, `flutter-ui-ux-expert`는 디자인/UX에 집중

**Agent Skill:** `flutter-patterns` (이 스킬 - 자동 트리거)
- 트리거: Flutter 코드 작성 완료 시 자동 실행
- 역할: Feature-based 구조, Riverpod 패턴, GoRouter, Material Design 3 준수 자동 검증

**차이점:**
- **Slash Command (`/flutter`)**: 사용자가 명시적으로 입력하여 작업 시작
- **Sub-Agent (`flutter-app-expert`)**: 복잡한 기능 구현 시 자동 호출되는 전문가
- **Sub-Agent (`flutter-ui-ux-expert`)**: UI/UX 디자인 작업 시 자동 호출
- **Agent Skill (`flutter-patterns`)**: 코드 작성 후 자동으로 프로젝트 패턴 검증

---

## 아키텍처 패턴

전체 아키텍처 가이드는 [flutter-architecture.md](./references/flutter-architecture.md)를 참조하세요.

### 기능 기반 구조

```
lib/features/{feature_name}/
├── presentation/        # UI 레이어
│   ├── {feature}_page.dart
│   └── widgets/
│       └── {widget}_widget.dart
├── application/         # 비즈니스 로직 + 상태
│   └── {feature}_notifier.dart
└── data/               # 데이터 레이어 (선택적)
    └── {feature}_repository.dart
```

**예시**: Chat 기능
```
lib/features/chat/
├── presentation/
│   ├── chat_page.dart
│   └── widgets/message_bubble.dart
├── application/
│   └── chat_notifier.dart
└── (repositories는 lib/repositories/에 위치)
```

상세 구조 및 예시는 [flutter-architecture.md](./references/flutter-architecture.md)를 참조하세요.

---

## 네이밍 규칙

| 타입 | 규칙 | 예시 |
|------|------|------|
| 파일 | snake_case | `chat_page.dart` |
| 클래스 | PascalCase | `ChatPage`, `MessageBubble` |
| 변수 | camelCase | `chatRooms`, `isLoading` |
| 상수 | lowerCamelCase | `defaultPadding`, `apiBaseUrl` |
| Private | _ 접두사 | `_controller`, `_buildHeader()` |

---

## Riverpod 상태 관리

자세한 패턴 및 예시는 [riverpod-patterns.md](./references/riverpod-patterns.md)를 참조하세요.

### Provider 타입

**1. Provider** - 단순 불변 값 (서비스, 클라이언트)
```dart
final apiClientProvider = Provider((ref) => ApiClient(...));
```

**2. StateNotifierProvider** - 복잡한 가변 상태 (리스트, 폼)
```dart
final chatListProvider = StateNotifierProvider<ChatListNotifier, ChatListState>((ref) {
  return ChatListNotifier(ref.watch(chatRepositoryProvider));
});
```

**3. FutureProvider** - 비동기 데이터 (일회성 fetch)
```dart
final userProfileProvider = FutureProvider.family<User, int>((ref, userId) async {
  return ref.watch(userRepositoryProvider).getUser(userId);
});
```

### 위젯에서 사용

```dart
class ChatListPage extends ConsumerWidget {
  @override
  Widget build(BuildContext context, WidgetRef ref) {
    final chatState = ref.watch(chatListProvider);  // 상태 감시

    // 액션 트리거
    ref.read(chatListProvider.notifier).loadRooms();  // 재빌드 안 함

    return ...;
  }
}
```

**상세 패턴**: [riverpod-patterns.md](./references/riverpod-patterns.md)에서 State 클래스 정의, copyWith, 에러 처리, family modifier 등 확인

---

## Material Design 3 테마

### AppColors 사용

```dart
// ❌ 나쁨: 하드코딩
Container(color: Color(0xFF6750A4))

// ✅ 좋음: AppColors 사용
Container(color: AppColors.primary)
```

**사용 가능한 색상**:
- `AppColors.primary` / `.onPrimary`
- `AppColors.secondary` / `.onSecondary`
- `AppColors.surface` / `.onSurface`
- `AppColors.background` / `.onBackground`
- `AppColors.error` / `.onError`

### AppSpacing 사용

```dart
Padding(
  padding: EdgeInsets.all(AppSpacing.md),  // 16.0
  child: Column(
    spacing: AppSpacing.sm,  // 자식 간 8.0
    children: [...]
  ),
)
```

**간격 상수**: `xs` (4.0), `sm` (8.0), `md` (16.0), `lg` (24.0), `xl` (32.0)

---

## GoRouter 라우팅

```dart
// 페이지로 이동
context.go('/chat/$roomId');

// 파라미터와 함께 이동
context.goNamed('chatRoom', pathParameters: {'roomId': roomId.toString()});

// Push/Pop/Replace
context.push('/settings');
context.pop();
context.replace('/login');
```

**라우트 추가**:
```dart
// lib/core/routing/app_router.dart
GoRoute(
  path: '/chat/:roomId',
  name: 'chatRoom',
  builder: (context, state) => ChatPage(
    roomId: int.parse(state.pathParameters['roomId']!)
  ),
),
```

---

## API 연동 - Repository 패턴

```dart
// lib/repositories/chat_repository.dart
class ChatRepository {
  final ApiClient _apiClient;
  ChatRepository(this._apiClient);

  Future<List<ChatRoom>> getRooms() async {
    try {
      final response = await _apiClient.get('/chats');
      return (response.data as List)
          .map((json) => ChatRoom.fromJson(json))
          .toList();
    } on DioException catch (e) {
      throw _handleError(e);
    }
  }
}

// Provider
final chatRepositoryProvider = Provider((ref) {
  return ChatRepository(ref.watch(apiClientProvider));
});
```

---

## 새 Flutter 코드 체크리스트

- [ ] 기능 기반 디렉토리 구조 (`lib/features/{feature}/`)
- [ ] `ConsumerWidget` 또는 `ConsumerStatefulWidget` 사용
- [ ] Riverpod provider로 상태 관리
- [ ] AppColors 사용 (하드코딩된 색상 금지)
- [ ] AppSpacing 사용 (매직 넘버 금지)
- [ ] 적절한 에러 처리 (try-catch, 에러 상태)
- [ ] 로딩 상태 표시
- [ ] 비동기 작업 후 `context.mounted` 확인
- [ ] 컨트롤러 적절히 dispose
- [ ] GoRouter로 라우팅
- [ ] Repository 패턴으로 API 호출
- [ ] Material Design 3 컴포넌트
- [ ] 접근성 고려 (semantics, labels)

---

## 주요 주의사항

1. **StatefulWidget 최소화** - Riverpod으로 상태 관리
2. **위젯에 비즈니스 로직 금지** - Provider/Notifier에 로직 위치
3. **context.mounted 확인 필수** - 비동기 후 navigation/snackbar
4. **컨트롤러 dispose 필수** - TextEditingController, ScrollController 등
5. **하드코딩 금지** - AppColors, AppSpacing 사용
6. **ListView.builder 사용** - 동적 리스트는 builder로 성능 최적화

---

## 참조 파일

### 상세 가이드
- **[flutter-architecture.md](./references/flutter-architecture.md)** - 전체 프로젝트 구조, 디렉토리 예시, 모범 사례
- **[riverpod-patterns.md](./references/riverpod-patterns.md)** - State 클래스, Notifier 패턴, 에러 처리, 테스팅

---

**기억하세요**: 일관성 = 유지보수성. 모든 Flutter 파일에서 이 패턴을 따르세요!
