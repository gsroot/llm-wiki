---
name: flutter-qa-audit
description: >
  Flutter 앱의 현재 구현 상태를 코드 레벨에서 조사하고 리포트를 생성/업데이트합니다.
  미구현/미완성/stub 기능을 식별하고, 이전 리포트가 있으면 미완료 항목만 재조사합니다.
  트리거 키워드: QA 감사, 구현 상태 확인, 미구현 체크, 앱 감사, flutter audit, qa-audit
---

# Flutter QA Audit

## 리포트 파일

- **경로**: `docs/flutter-qa-report.md` (프로젝트 루트 기준)
- **단일 파일로만 관리** - 절대 다른 경로나 파일명으로 생성하지 않음
- **포맷**: [references/report-template.md](references/report-template.md) 참조 - 이 포맷을 반드시 준수

## 워크플로우

### 0단계: MCP 연결 우선 사용 규칙

- **Dart MCP 연결됨**: 코드 조사/정적 분석/테스트는 가능하면 Dart MCP 도구(`analyze_files`, `resolve_workspace_symbol`, `run_tests` 등)를 우선 사용.
- **Maestro MCP 연결됨**: 설정 화면/토글/네비게이션 같은 실제 UI 동작 확인이 필요하면 Maestro MCP로 화면 탐색 및 상호작용 검증을 우선 수행.
- **둘 다 미연결**: 기존 Grep/파일 스캔 기반 워크플로우(1~5단계)를 그대로 수행.
- **원칙**: 동일 목적을 달성할 수 있다면 MCP 도구를 우선, 불가하거나 부족하면 CLI Grep/파일 리딩으로 보완.

### 1단계: 기존 리포트 확인

`docs/flutter-qa-report.md` 파일이 존재하는지 확인.

- **존재하면**: 파일을 읽고, `상태` 컬럼이 `✅ 완료`가 아닌 항목만 추출하여 재조사 대상 목록 생성
- **존재하지 않으면**: 전체 조사 수행 (2단계의 모든 검사 항목 실행)

### 2단계: 코드 레벨 조사

Flutter 소스 디렉토리: `mate_chat_flutter/lib/`

**2-1. TODO/FIXME 스캔**

```
Grep pattern="(TODO|FIXME|HACK|XXX)" path="mate_chat_flutter/lib/" glob="*.dart"
```

각 TODO의 파일, 라인, 내용을 기록. 이미 리포트에 있는 TODO 중 제거된 것은 `✅ 완료`로 업데이트.

**2-2. Stub/미구현 메서드 검사**

```
Grep pattern="(throw UnimplementedError|NotImplementedError|// TODO)" path="mate_chat_flutter/lib/" glob="*.dart"
```

**2-3. 에러 핸들링 검사**

```
Grep pattern="e\.toString\(\)|error\.toString\(\)" path="mate_chat_flutter/lib/" glob="*.dart"
```

DioException 등의 raw 에러가 사용자에게 노출되는 곳 식별.

**2-4. 핵심 기능 구현 여부 체크**

각 항목에 대해 특정 패턴을 Grep으로 검색:

| 기능 | 검색 패턴 | 대상 경로 |
|------|-----------|----------|
| Apple OAuth | `apple\|AppleSignIn\|sign_in_with_apple` | `lib/features/auth/` |
| 푸시 알림 | `firebase_messaging\|FCM\|fcm\|APNs` | `lib/` 전체 + `pubspec.yaml` |
| 다크모드 | `ThemeMode\|themeMode\|darkMode` | `lib/core/theme/` + `lib/features/settings/` |
| i18n | `Localizations\|AppLocalizations\|intl` | `lib/` 전체 + `pubspec.yaml` |

**2-5. Settings 하위 페이지 실제 구현 여부**

```
Grep pattern="// TODO" path="mate_chat_flutter/lib/features/settings/" glob="*.dart" output_mode="content"
```

**2-6. Repository stub 검사**

```
Grep pattern="(TODO|Wire up|stub|placeholder)" path="mate_chat_flutter/lib/repositories/" glob="*.dart"
```

**2-7. 라우팅 동작 점검 (GoRouter/Router 앱 필수)**

- `MaterialApp.router` + `go_router`를 사용하는 앱에서는 `Navigator.pushNamed(...)` 사용 시 실제 라우팅이 실패할 수 있으므로 반드시 점검:

```
Grep pattern="Navigator\.pushNamed\(" path="mate_chat_flutter/lib/features/settings/" glob="*.dart"
Grep pattern="MaterialApp\.router|GoRouter" path="mate_chat_flutter/lib/" glob="*.dart"
```

- 위 패턴이 동시에 검출되면 **설정/지원 메뉴 미동작 가능성 HIGH**로 분류하고, `context.push(...)` 또는 `context.go(...)` 사용 여부를 `app_router.dart` 경로와 대조 확인.

### 3단계: 심각도 분류

| 심각도 | 기준 |
|--------|------|
| CRITICAL | 앱스토어 출시에 필수 (Apple OAuth, 법적 요구사항) 또는 핵심 UX 결함 |
| HIGH | 사용자 경험에 직접적 영향 (설정 미동작, 에러 메시지 raw 노출) |
| MEDIUM | 부가 기능 미구현 (도움말, 다국어) |
| LOW | 선택적 기능 (사진 공유, 갤러리 저장) |

### 4단계: 리포트 동기화

조사 완료 후 반드시 `docs/flutter-qa-report.md`를 업데이트:

1. 기존 항목 중 해결된 것 → `상태`를 `✅ 완료`로 변경, `확인일` 업데이트
2. 새로 발견된 이슈 → 다음 번호로 추가
3. 상단 `최종 업데이트` 타임스탬프 갱신
4. `요약` 섹션의 카운트 재계산
5. 리포트 포맷은 [references/report-template.md](references/report-template.md)를 엄격히 준수

**중요**: 리포트의 테이블 포맷, 컬럼 순서, 섹션 구조를 절대 변경하지 않음. 내용만 업데이트.

### 5단계: 사용자에게 요약 보고

리포트 업데이트 후, 변경 사항을 간결하게 보고:
- 새로 발견된 이슈 수
- 해결 확인된 이슈 수
- 남은 이슈 심각도별 카운트
