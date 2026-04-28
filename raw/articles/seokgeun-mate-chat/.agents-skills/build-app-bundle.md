---
name: build-app-bundle
description: Build versioned Android Flutter app bundles (.aab) for the mate-chat project using an explicit app version (build-name+build-number). Use when preparing Play Store uploads, reproducing release builds, or bumping/syncing the Flutter app version during release work.
---

# Build App Bundle

## Overview

Build `mate_chat_flutter` app bundles with a required explicit version string (for example `1.2.0+34`), similar to the release flow used in `travel-mate`.

Canonical project script:
- `mate_chat_flutter/scripts/build_appbundle.sh`

## Workflow

1. Confirm release version in `name+code` format (example: `1.3.0+27`).
2. Run the script with required `--version`.
3. Optionally update `pubspec.yaml` with `--update-pubspec`.
4. Verify generated bundle path from script output.

## Script Usage

```bash
# Dry run only (recommended first)
./mate_chat_flutter/scripts/build_appbundle.sh \
  --version 1.2.0+34 \
  --dry-run

# Release build
./mate_chat_flutter/scripts/build_appbundle.sh \
  --version 1.2.0+34

# Release build, sync pubspec.yaml, and update backend version policy
./mate_chat_flutter/scripts/build_appbundle.sh \
  --version 1.2.0+34 \
  --update-pubspec \
  --update-version-policy
```

## Options

- `--version <name+code>`: required (example `1.2.0+34`)
- `--mode release|profile|debug`: optional, default `release`
- `--env-file <path>`: optional, default `mate_chat_backend/.env`
- `--update-pubspec`: optional, update `mate_chat_flutter/pubspec.yaml` version line
- `--update-version-policy`: optional, set `ANDROID_LATEST_VERSION_CODE=<code>` in `.env`
- `--dry-run`: optional, print build command without executing

## Version Policy Integration

빌드 번호(build number)는 Android versionCode와 동일하며,
백엔드 `.env`의 `ANDROID_LATEST_VERSION_CODE`와 연동됩니다.

| `.env` 키 | 역할 | 업데이트 방법 |
|-----------|------|---------------|
| `ANDROID_LATEST_VERSION_CODE` | Play Store 최신 버전 코드 | `--update-version-policy` 로 자동 |
| `ANDROID_MIN_SUPPORTED_VERSION_CODE` | 강제 업데이트 기준 버전 코드 | 수동으로 설정 (의도적 결정 필요) |

`ANDROID_MIN_SUPPORTED_VERSION_CODE`는 하위호환성 파괴 시에만 올리는 값이므로
항상 수동으로 판단해서 변경합니다.

## Required Environment Keys

Read from `mate_chat_backend/.env` (or custom `--env-file`):
- `ADMIN_EMAIL`
- `ADMIN_PASSWORD`
- `API_BASE_URL` (fallback: `${BACKEND_URL}/v1`)
- `GOOGLE_PLAY_PACKAGE_NAME` (optional, default `com.mate.mate_chat_flutter`)

## Notes

- This skill is intentionally non-interactive for CI/repeatable release usage.
- It targets project root layout:
  - `mate_chat_flutter/`
  - `mate_chat_backend/.env`
