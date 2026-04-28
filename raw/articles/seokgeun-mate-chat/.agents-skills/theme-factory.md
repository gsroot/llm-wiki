---
name: theme-factory
description: >
  웹과 모바일 아티팩트에 테마를 적용하여 스타일링하는 툴킷입니다.
  슬라이드, 문서, 보고서, HTML 랜딩 페이지, Flutter 앱 화면 등에 사용할 수 있습니다.
  색상/폰트가 포함된 10개의 사전 설정 테마를 제공하며, 즉석에서 새 테마를 생성할 수도 있습니다.
  웹과 모바일 모두에 적용 가능합니다.
---

# 테마 팩토리 스킬

전문적인 폰트 및 색상 테마의 큐레이션된 컬렉션을 제공합니다.
각 테마는 신중하게 선택된 색상 팔레트와 폰트 페어링을 포함합니다.
테마를 선택하면 웹 아티팩트와 모바일 앱 화면 모두에 적용할 수 있습니다.

## 목적

웹 아티팩트(프레젠테이션, 랜딩 페이지)와 모바일 앱 화면에 일관되고 전문적인 스타일링을 적용합니다. 각 테마는 다음을 포함합니다:
- Hex 코드가 있는 응집력 있는 색상 팔레트
- 헤더 및 본문 텍스트를 위한 보완적인 폰트 페어링
- 다양한 컨텍스트와 대상에 적합한 독특한 시각적 정체성

---

## 관련 시스템

**Slash Command:** `/ui` (테마 적용 시 연계)
- 사용자가 `/ui 프로필 화면 디자인 개선` 입력 시 테마 적용 가능
- UI/UX 작업의 일부로 테마 선택 및 적용

**Sub-Agent:** `flutter-ui-ux-expert` (테마 적용 작업)
- Flutter 앱에 테마 적용 시 자동으로 호출되는 UI 전문가
- ColorScheme, TextTheme 변환 및 적용 담당
- 트리거 조건: 테마 커스터마이징, 다크/라이트 모드 구현, 브랜딩 작업

**Agent Skill:** `theme-factory` (이 스킬)
- 역할: 10개 사전 설정 테마 제공 및 커스텀 테마 생성
- 웹(CSS variables)과 모바일(Flutter ColorScheme) 양쪽 가이드 제공

**차이점:**
- **Slash Command (`/ui`)**: 사용자가 명시적으로 UI 작업 시작
- **Sub-Agent (`flutter-ui-ux-expert`)**: 테마를 실제 코드로 구현
- **Agent Skill (`theme-factory`)**: 테마 선택 가이드 및 변환 방법 제공

**관련 스킬:**
- `frontend-design`: 전체 UI/UX 디자인 철학 및 미학 가이드
- `flutter-patterns`: Flutter에서 테마 적용 시 프로젝트 패턴 준수
- `flutter-artifacts-builder`, `web-artifacts-builder`: 프로젝트 초기화 시 기본 테마 설정

---

## 사용 지침

슬라이드 덱 또는 다른 아티팩트에 스타일링을 적용하려면:

1. **테마 쇼케이스 표시**: `theme-showcase.pdf` 파일을 표시하여 사용자가 모든 사용 가능한 테마를 시각적으로 볼 수 있도록 합니다. 수정하지 말고 보기용으로만 표시합니다.
2. **선택 요청**: 덱에 적용할 테마를 묻습니다
3. **선택 대기**: 선택한 테마에 대한 명시적 확인을 받습니다
4. **테마 적용**: 테마가 선택되면 선택한 테마의 색상과 폰트를 덱/아티팩트에 적용합니다

## 사용 가능한 테마

다음 10개 테마가 `theme-showcase.pdf`에 쇼케이스되어 있습니다:

1. **Ocean Depths** - 전문적이고 차분한 해양 테마
2. **Sunset Boulevard** - 따뜻하고 생동감 있는 일몰 색상
3. **Forest Canopy** - 자연스럽고 안정적인 대지 톤
4. **Modern Minimalist** - 깔끔하고 현대적인 그레이스케일
5. **Golden Hour** - 풍부하고 따뜻한 가을 팔레트
6. **Arctic Frost** - 시원하고 상쾌한 겨울 영감 테마
7. **Desert Rose** - 부드럽고 세련된 더스티 톤
8. **Tech Innovation** - 대담하고 현대적인 기술 미학
9. **Botanical Garden** - 신선하고 유기적인 정원 색상
10. **Midnight Galaxy** - 극적이고 우주적인 깊은 톤

## 테마 세부사항

각 테마는 `themes/` 디렉토리에 정의되어 있으며 다음을 포함합니다:
- Hex 코드가 있는 응집력 있는 색상 팔레트
- 헤더 및 본문 텍스트를 위한 보완적인 폰트 페어링
- 다양한 컨텍스트와 대상에 적합한 독특한 시각적 정체성

## 적용 프로세스

선호하는 테마가 선택된 후:
1. `themes/` 디렉토리에서 해당 테마 파일 읽기
2. 덱 전체에 지정된 색상과 폰트를 일관되게 적용
3. 적절한 대비와 가독성 보장
4. 모든 슬라이드에서 테마의 시각적 정체성 유지

## 커스텀 테마 생성
기존 테마 중 아티팩트에 적합한 것이 없는 경우 커스텀 테마를 생성합니다. 제공된 입력을 기반으로 위와 유사한 새 테마를 생성합니다. 폰트/색상 조합이 나타내는 것을 설명하는 유사한 이름을 지정합니다. 제공된 기본 설명을 사용하여 적절한 색상/폰트를 선택합니다. 테마를 생성한 후 검토 및 확인을 위해 표시합니다. 그런 다음 위에 설명된 대로 테마를 적용합니다.

## Flutter/모바일 앱 적용 가이드

모바일 앱에 테마를 적용할 때:

1. **색상 변환**:
   - Hex 코드를 Flutter Color로 변환: `Color(0xFF...)`
   - ColorScheme 생성: `ColorScheme.fromSeed()` 또는 커스텀 ColorScheme
   - 다크/라이트 모드 모두 정의

2. **폰트 적용**:
   - Google Fonts 패키지 사용: `GoogleFonts.{fontName}()`
   - 또는 pubspec.yaml에 커스텀 폰트 추가
   - TextTheme 정의 (headline, body, label 등)

3. **테마 구성**:
   ```dart
   ThemeData(
     colorScheme: ColorScheme(...),
     textTheme: TextTheme(
       headlineLarge: GoogleFonts.{displayFont}(...),
       bodyMedium: GoogleFonts.{bodyFont}(...),
     ),
     // 추가 스타일링
   )
   ```

4. **일관성 유지**:
   - 모든 화면에서 `Theme.of(context).colorScheme` 사용
   - 하드코딩된 색상 피하기
   - Material Design 3 컴포넌트 활용

**예시 변환**:
- Ocean Depths 테마 → 파란색 계열 ColorScheme + 세리프 폰트
- Modern Minimalist → 그레이스케일 ColorScheme + 산세리프 폰트
