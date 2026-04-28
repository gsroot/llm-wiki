# mate_chat_flutter

Flutter client for Mate Chat.

## Local Run

```bash
flutter pub get
./scripts/run_android.sh --api-base-url http://10.0.2.2:8000/v1
```

For a real device, replace the API URL with the host machine IP:

```bash
./scripts/run_android.sh --api-base-url http://192.168.x.x:8000/v1
```

### Faster emulator dev via `adb reverse`

The default `10.0.2.2` path routes through QEMU's software NAT (SLIRP), which
adds ~400 ms per TCP connect and can hang for several seconds after idle.
`adb reverse` tunnels the emulator's `localhost:PORT` directly to the host's
`127.0.0.1:PORT`, bypassing SLIRP.

```bash
./scripts/run_android.sh --adb-reverse --api-base-url http://10.0.2.2:8000/v1
```

With `--adb-reverse` the script:

1. Runs `adb -s <device> reverse tcp:<port> tcp:<port>` (port parsed from
   `API_BASE_URL`).
2. Rewrites `API_BASE_URL` host to `localhost` so the app goes through the
   fast adb tunnel.

Note: `adb reverse` rules are cleared when the emulator disconnects — re-run
the script after each emulator restart. Physical devices should keep using
the LAN IP path (do not pass `--adb-reverse`).

## Sentry

- Sentry is disabled by default.
- Enable it only by passing `--sentry-dsn` to the script or `--dart-define=SENTRY_DSN=...` directly.
- Recommended release usage:

```bash
./scripts/run_android.sh \
  --mode release \
  --api-base-url https://api.example.com/v1 \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment staging
```

## Android App Bundle

```bash
./scripts/build_appbundle.sh \
  --version 1.0.0+10 \
  --update-pubspec \
  --sentry-dsn https://examplePublicKey@o000.ingest.sentry.io/000 \
  --sentry-environment production
```

## Related Docs

- `../docs/20-push-notification-e2e-checklist.md`
- `../docs/21-push-session-operations-guide.md`
- `../docs/22-mobile-release-checklist.md`
