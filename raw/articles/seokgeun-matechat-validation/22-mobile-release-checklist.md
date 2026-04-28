# Mobile Release Checklist

> Last updated: 2026-03-12

This checklist is the release handoff for the Flutter app.
Use it together with:

- [Push/Session Operations Guide](./21-push-session-operations-guide.md)
- [Push Notification E2E Checklist](./20-push-notification-e2e-checklist.md)

## 1. Release Inputs

- [ ] target version fixed (`x.y.z+build`)
- [ ] target backend environment fixed (`staging` or `production`)
- [ ] backend URL confirmed
- [ ] Firebase project confirmed
- [ ] Sentry DSN confirmed for target environment
- [ ] Google Play package name confirmed

## 2. Backend Release Preconditions

- [ ] `ENVIRONMENT=staging` or `ENVIRONMENT=production`
- [ ] `SENTRY_DSN` set for the target environment
- [ ] `FIREBASE_CREDENTIALS_PATH` empty when using ADC, or valid if key-based mode is intentionally used
- [ ] `FIREBASE_PROJECT_ID` matches the Firebase project used by the app
- [ ] `gcloud auth application-default print-access-token` succeeds on the machine that runs push tests
- [ ] backend startup log confirms Firebase Admin initialization
- [ ] backend startup log confirms Sentry initialization only in staging/production

## 3. Flutter Release Preconditions

- [ ] `google-services.json` matches the Firebase project for the target app
- [ ] Flutter Sentry is enabled only by explicit `--dart-define=SENTRY_DSN=...`
- [ ] admin test credentials are available if release smoke tests need them
- [ ] release command is executed through repo script, not copied manually from memory

## 4. Build Commands

### 4.1 Android Run Smoke Test

Example:

```bash
cd mate_chat_flutter
./scripts/run_android.sh \
  --mode release \
  --api-base-url https://api.example.com/v1 \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment staging
```

### 4.2 Android App Bundle

Example:

```bash
cd mate_chat_flutter
./scripts/build_appbundle.sh \
  --version 1.0.0+10 \
  --update-pubspec \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment production
```

## 5. Push/Session Smoke Checks

These are the minimum release gates for push behavior.

- [ ] login registers device token
- [ ] logout unregisters device token
- [ ] global notification OFF unregisters token and syncs backend flag
- [ ] global notification ON re-registers token and syncs backend flag
- [ ] foreground notification shows on non-chat screen
- [ ] same-room foreground notification is suppressed
- [ ] background push arrives and tap deep-links correctly
- [ ] terminated push arrives and cold-start deep-links correctly
- [ ] online receiver with active WebSocket presence does not get duplicated push
- [ ] offline receiver resumes getting push
- [ ] invalid FCM token is cleaned up automatically
- [ ] Android `POST_NOTIFICATIONS` denial does not crash the app
- [ ] offline relaunch preserves signed-in session UX

If any item fails, use the incident sequence in [21-push-session-operations-guide.md](./21-push-session-operations-guide.md).

## 6. Release Validation Evidence

- [ ] final app bundle path recorded
- [ ] release command captured in PR/release notes
- [ ] backend commit SHA recorded
- [ ] Flutter commit SHA recorded
- [ ] push/session smoke test result recorded
- [ ] known limitations or waived checks recorded explicitly

## 7. Do Not Ship If

- [ ] Sentry is still enabled in `development` by default
- [ ] Flutter release build was produced without explicit backend URL
- [ ] Firebase project does not match the installed app config
- [ ] push deep-link opens home instead of the target route
- [ ] app force-logs out on transient network loss during startup
