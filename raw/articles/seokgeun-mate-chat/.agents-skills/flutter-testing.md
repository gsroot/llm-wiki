---
name: flutter-testing
description: >
  Flutter 앱 테스팅 가이드와 예시를 제공합니다.
  Unit, Widget, Integration 테스트 작성 패턴과 모범 사례를 제공하여
  Flutter 앱의 품질을 보장합니다. 사용자가 Flutter 앱 테스트를 작성하거나
  기능 검증이 필요할 때 사용합니다.
---

# Flutter Testing

## 개요

Flutter 앱의 단위 테스트, 위젯 테스트, 통합 테스트를 작성하기 위한 가이드입니다.
각 테스트 유형별 작성 패턴, 모범 사례, 실행 방법을 제공합니다.

**사용 시나리오:**
- Flutter 위젯 테스트 작성
- Flutter 통합 테스트 작성
- 앱 기능 검증
- 회귀 테스트 자동화

---

## 관련 시스템

**Slash Command:** `/test-gen` (사용자 명시적 호출)
- 사용자가 `/test-gen lib/features/chat/` 형식으로 테스트 생성 요청
- 백엔드/프론트엔드 로직 분석하여 정확한 테스트 케이스 생성

**Sub-Agent:** `fullstack-qa-engineer` (자동 호출)
- 복잡한 테스트 케이스 설계 및 커버리지 분석 시 자동으로 호출되는 전문가
- 단위/통합/e2e 테스트 작성, 엣지 케이스 식별, 품질 보증 전문가
- 트리거 조건: 새 기능 테스트 작성, 테스트 실패 디버깅, 커버리지 분석

**Agent Skill:** `flutter-testing` (이 스킬)
- 역할: Flutter 테스트 작성 패턴 및 모범 사례 가이드 제공
- Unit, Widget, Integration 테스트 예시 및 실행 방법 제공

**차이점:**
- **Slash Command (`/test-gen`)**: 사용자가 명시적으로 입력하여 테스트 생성 시작
- **Sub-Agent (`fullstack-qa-engineer`)**: 복잡한 테스트 전략 수립 및 구현
- **Agent Skill (`flutter-testing`)**: 테스트 작성 가이드 및 패턴 참조 자료

**관련 스킬:**
- `flutter-patterns`: Flutter 코드 구조 및 패턴 (테스트 대상 코드)
- `flutter-artifacts-builder`: 프로젝트 초기화 시 테스트 구조 포함

---

## 테스트 유형

Flutter에서 제공하는 세 가지 테스트 유형:

### 1. Unit Testing (단위 테스트)

**목적:** 개별 함수, 메서드, 클래스를 테스트

**특징:**
- 가장 빠름
- 외부 의존성 없음
- 비즈니스 로직 검증

**예시:**
```dart
// test/services/calculator_test.dart
import 'package:flutter_test/flutter_test.dart';
import 'package:my_app/services/calculator.dart';

void main() {
  group('Calculator', () {
    late Calculator calculator;

    setUp(() {
      calculator = Calculator();
    });

    test('adds two numbers', () {
      expect(calculator.add(2, 3), 5);
    });

    test('subtracts two numbers', () {
      expect(calculator.subtract(5, 3), 2);
    });
  });
}
```

**실행:**
```bash
flutter test test/services/calculator_test.dart
```

### 2. Widget Testing (위젯 테스트)

**목적:** 개별 위젯의 UI와 상호작용 테스트

**특징:**
- UI 렌더링 검증
- 사용자 인터랙션 시뮬레이션
- 빠른 실행 속도

**예시:**
```dart
// test/widgets/counter_button_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:my_app/widgets/counter_button.dart';

void main() {
  testWidgets('CounterButton increments counter', (tester) async {
    int counter = 0;

    await tester.pumpWidget(
      MaterialApp(
        home: Scaffold(
          body: CounterButton(
            onPressed: () => counter++,
          ),
        ),
      ),
    );

    // 초기 상태 확인
    expect(find.text('0'), findsOneWidget);

    // 버튼 탭
    await tester.tap(find.byType(ElevatedButton));
    await tester.pump();

    // 업데이트된 상태 확인
    expect(counter, 1);
  });

  testWidgets('CounterButton displays correct text', (tester) async {
    await tester.pumpWidget(
      const MaterialApp(
        home: Scaffold(
          body: CounterButton(label: 'Click Me'),
        ),
      ),
    );

    expect(find.text('Click Me'), findsOneWidget);
  });
}
```

**주요 메서드:**
- `tester.pumpWidget()`: 위젯 트리 생성
- `tester.pump()`: 프레임 렌더링 (애니메이션 중간 상태)
- `tester.pumpAndSettle()`: 애니메이션 완료까지 대기
- `tester.tap()`: 탭 제스처
- `tester.enterText()`: 텍스트 입력
- `find.byType()`, `find.text()`: 위젯 찾기

**실행:**
```bash
flutter test test/widgets/
```

### 3. Integration Testing (통합 테스트)

**목적:** 전체 앱 또는 대규모 플로우 테스트

**특징:**
- 실제 기기/에뮬레이터에서 실행
- 전체 사용자 플로우 검증
- 가장 느림

**설정:**

pubspec.yaml에 추가:
```yaml
dev_dependencies:
  integration_test:
    sdk: flutter
  flutter_test:
    sdk: flutter
```

**예시:**
```dart
// integration_test/app_test.dart
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:integration_test/integration_test.dart';
import 'package:my_app/main.dart' as app;

void main() {
  IntegrationTestWidgetsFlutterBinding.ensureInitialized();

  group('end-to-end test', () {
    testWidgets('complete login flow', (tester) async {
      // 앱 시작
      app.main();
      await tester.pumpAndSettle();

      // 로그인 페이지로 이동
      final loginButton = find.text('Login');
      expect(loginButton, findsOneWidget);
      await tester.tap(loginButton);
      await tester.pumpAndSettle();

      // 이메일 입력
      final emailField = find.byKey(const Key('email_field'));
      await tester.enterText(emailField, 'test@example.com');
      await tester.pumpAndSettle();

      // 비밀번호 입력
      final passwordField = find.byKey(const Key('password_field'));
      await tester.enterText(passwordField, 'password123');
      await tester.pumpAndSettle();

      // 로그인 버튼 탭
      final submitButton = find.text('Submit');
      await tester.tap(submitButton);
      await tester.pumpAndSettle();

      // 홈 화면 확인
      expect(find.text('Welcome'), findsOneWidget);
    });

    testWidgets('navigate through app screens', (tester) async {
      app.main();
      await tester.pumpAndSettle();

      // 홈 → 프로필
      await tester.tap(find.byIcon(Icons.person));
      await tester.pumpAndSettle();
      expect(find.text('Profile'), findsOneWidget);

      // 프로필 → 설정
      await tester.tap(find.text('Settings'));
      await tester.pumpAndSettle();
      expect(find.text('Settings'), findsOneWidget);
    });
  });
}
```

**실행:**
```bash
# Android 에뮬레이터/기기
flutter test integration_test/app_test.dart

# 또는 flutter drive 사용
flutter drive \
  --driver=test_driver/integration_test.dart \
  --target=integration_test/app_test.dart
```

## 모범 사례

### 1. 테스트 구조화

```dart
void main() {
  group('UserService', () {
    late UserService userService;
    late MockUserRepository mockRepo;

    setUp(() {
      mockRepo = MockUserRepository();
      userService = UserService(mockRepo);
    });

    tearDown(() {
      // 정리 작업
    });

    group('login', () {
      test('succeeds with valid credentials', () {
        // Arrange
        when(mockRepo.login(any, any))
            .thenAnswer((_) async => User(id: 1));

        // Act
        final result = await userService.login('email', 'password');

        // Assert
        expect(result, isA<User>());
        verify(mockRepo.login('email', 'password')).called(1);
      });

      test('fails with invalid credentials', () async {
        // Arrange
        when(mockRepo.login(any, any))
            .thenThrow(LoginException('Invalid credentials'));

        // Act & Assert
        expect(
          () => userService.login('wrong', 'wrong'),
          throwsA(isA<LoginException>()),
        );
      });
    });
  });
}
```

### 2. Mock 사용 (mockito)

```dart
// test/mocks.dart
import 'package:mockito/annotations.dart';
import 'package:my_app/repositories/user_repository.dart';

@GenerateMocks([UserRepository])
void main() {}
```

Mock 생성:
```bash
flutter pub run build_runner build
```

### 3. Golden Testing (스크린샷 비교)

```dart
testWidgets('ProfileCard matches golden', (tester) async {
  await tester.pumpWidget(
    const MaterialApp(
      home: Scaffold(
        body: ProfileCard(name: 'John Doe'),
      ),
    ),
  );

  await expectLater(
    find.byType(ProfileCard),
    matchesGoldenFile('goldens/profile_card.png'),
  );
});
```

Golden 파일 생성:
```bash
flutter test --update-goldens
```

### 4. 비동기 테스트

```dart
test('fetches user data', () async {
  final userService = UserService();

  final user = await userService.fetchUser(1);

  expect(user.id, 1);
  expect(user.name, isNotEmpty);
});
```

### 5. Riverpod 상태 관리 테스트

```dart
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  test('counterProvider increments', () {
    final container = ProviderContainer();
    final counter = container.read(counterProvider.notifier);

    expect(container.read(counterProvider), 0);

    counter.increment();
    expect(container.read(counterProvider), 1);

    container.dispose();
  });
}
```

## 테스트 실행

### 모든 테스트 실행
```bash
flutter test
```

### 특정 파일 실행
```bash
flutter test test/services/user_service_test.dart
```

### 커버리지 리포트
```bash
flutter test --coverage
genhtml coverage/lcov.info -o coverage/html
open coverage/html/index.html
```

### 통합 테스트 실행
```bash
flutter test integration_test/
```

## 예시 파일

`examples/` 디렉토리에 다음 예시가 포함되어 있습니다:

- `widget_test_example.dart`: 위젯 테스트 패턴
- `integration_test_example.dart`: 통합 테스트 전체 플로우
- `riverpod_test_example.dart`: Riverpod 상태 관리 테스트

## 참조

- **Flutter Testing 공식 문서**: https://docs.flutter.dev/testing
- **mockito 패키지**: https://pub.dev/packages/mockito
- **integration_test 패키지**: https://pub.dev/packages/integration_test
