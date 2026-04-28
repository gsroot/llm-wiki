---
name: flutter-artifacts-builder
description: >
  Flutter 앱 샘플과 프로토타입을 빠르게 생성하고 실행하는 툴킷입니다.
  사용자가 Flutter 앱, 모바일 UI, 위젯 프로토타입을 요청할 때 사용합니다.
  프로젝트 초기화부터 필수 패키지 설치, 기본 구조 설정까지 자동화하여
  즉시 개발을 시작할 수 있도록 합니다.
---

# Flutter Artifacts Builder

## 개요

Flutter 앱 샘플과 프로토타입을 빠르게 생성하고 실행할 수 있는 툴킷입니다.
프로젝트 초기화, 필수 패키지 설치, 기본 구조 설정을 자동화합니다.

**사용 시나리오:**
- Flutter 앱 프로토타입 요청
- 새로운 Flutter 기능 테스트
- 모바일 UI/UX 샘플 생성
- Flutter 위젯 데모 작성

---

## 관련 시스템

**Slash Command:** 없음 (독립적 도구)
- 사용자가 "Flutter 앱 프로토타입 만들어줘" 형식으로 요청하면 자동 사용
- 프로젝트 초기화 전용 툴킷

**Sub-Agent:** `flutter-app-expert`, `flutter-ui-ux-expert` (생성 후 연계)
- 프로젝트 초기화 후 기능 구현 시 자동으로 해당 에이전트들이 호출됨
- `flutter-app-expert`: 기능 로직, 상태 관리, API 통합
- `flutter-ui-ux-expert`: UI 디자인, 애니메이션, 스타일링

**Agent Skill:** `flutter-artifacts-builder` (이 스킬)
- 역할: Flutter 프로젝트 빠른 초기화 및 보일러플레이트 생성
- scripts/init-flutter-app.sh를 사용한 자동화된 프로젝트 설정

**차이점:**
- **이 스킬**: 프로젝트 초기화 및 기본 구조 생성
- **Sub-Agents**: 초기화 이후 실제 기능 개발 담당
- **flutter-patterns**: 생성된 코드가 프로젝트 패턴을 따르도록 검증

**관련 스킬:**
- `flutter-patterns`: 생성된 프로젝트가 따라야 할 코드 패턴
- `frontend-design`: UI/UX 디자인 가이드라인
- `theme-factory`: 프로젝트에 테마 적용 시

---

## 빠른 시작

### 1단계: 프로젝트 초기화

초기화 스크립트를 실행하여 새 Flutter 프로젝트를 생성합니다:

```bash
bash scripts/init-flutter-app.sh <project-name>
cd <project-name>
```

스크립트가 수행하는 작업:
- ✅ Flutter 프로젝트 생성 (`flutter create`)
- ✅ 필수 패키지 설치 (Riverpod, GoRouter, Dio, Hive 등)
- ✅ 기본 디렉토리 구조 생성 (`features/`, `core/`, `ui/components/`)
- ✅ Material Design 3 테마 설정
- ✅ main.dart, app.dart 보일러플레이트 생성
- ✅ flutter-patterns 스킬 패턴 적용

### 2단계: 앱 개발

생성된 프로젝트 구조:

```
<project-name>/
├── lib/
│   ├── main.dart              # 앱 엔트리 포인트
│   ├── app.dart               # 앱 설정 (테마, 라우팅)
│   ├── core/
│   │   ├── theme/            # AppColors, Typography
│   │   ├── routing/          # GoRouter 설정
│   │   └── utils/            # 유틸리티
│   ├── features/
│   │   └── home/             # 홈 화면 예시
│   └── ui/
│       └── components/       # 재사용 가능한 위젯
├── test/
├── android/
├── ios/
└── pubspec.yaml
```

**코딩 패턴:**
- `flutter-patterns` 스킬의 가이드라인 참조
- Feature-based 모듈 구조
- Riverpod을 사용한 상태 관리
- GoRouter를 사용한 라우팅
- Material Design 3 컴포넌트

### 3단계: 실행 및 테스트

**개발 서버 실행:**
```bash
flutter run
```

**Android 빌드:**
```bash
flutter build apk
```

**iOS 빌드:**
```bash
flutter build ios
```

**웹 빌드:**
```bash
flutter build web
```

**테스트 실행:**
```bash
flutter test
```

## 설치된 패키지

초기화 시 자동으로 설치되는 패키지:

| 패키지 | 용도 |
|--------|------|
| flutter_riverpod | 상태 관리 |
| go_router | 라우팅 |
| dio | HTTP 클라이언트 |
| hive, hive_flutter | 로컬 저장소 |
| flutter_secure_storage | 보안 저장소 |
| freezed, json_serializable | 데이터 클래스 |
| intl | 국제화 |
| cached_network_image | 이미지 캐싱 |

## 디자인 가이드라인

**중요:** `frontend-design` 스킬의 Flutter 가이드라인을 참조하세요.

핵심 원칙:
- 독특한 타이포그래피 (Pretendard, Noto Sans 등)
- 응집력 있는 색상 테마 (ColorScheme 사용)
- 플랫폼 적응형 디자인 (Material/Cupertino)
- 60fps 성능 유지
- SafeArea 고려

## 테마 적용

테마를 적용하려면 `theme-factory` 스킬을 사용하세요:

1. 테마 선택 (Ocean Depths, Sunset Boulevard 등)
2. Flutter ColorScheme으로 변환
3. TextTheme 정의
4. ThemeData 생성

예시:
```dart
ThemeData(
  colorScheme: ColorScheme.fromSeed(
    seedColor: Color(0xFF1E40AF), // Ocean Depths
  ),
  textTheme: TextTheme(
    headlineLarge: GoogleFonts.playfairDisplay(),
    bodyMedium: GoogleFonts.inter(),
  ),
)
```

## 참조

- **Flutter 패턴**: `flutter-patterns` 스킬 참조
- **디자인 가이드**: `frontend-design` 스킬 참조
- **테마 시스템**: `theme-factory` 스킬 참조
