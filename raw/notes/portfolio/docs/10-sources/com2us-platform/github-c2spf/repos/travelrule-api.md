---
title: "c2spf/travelrule-api"
type: source-index
company: com2us-platform
source: github
repo: c2spf/travelrule-api
visibility: private
primary_language: Python
collected_at: "2026-04-24"
---

# c2spf/travelrule-api

가상자산 거래소용 트래블룰 이행 공통 API ("라이트닝" 서비스) — ✅ 완료

## 기본 정보

| 항목 | 값 |
|------|----|
| URL | <https://github.com/c2spf/travelrule-api> (private) |
| Visibility | private |
| Default Branch | `master` |
| 주 언어 | Python (~670KB), JavaScript (~312KB), CSS, Dockerfile, Shell, Mako |
| 크기 | 3.7 MB |

## 내 기여

- **내 커밋**: **135** / 전체 507 (~27%)
- **기여 기간**: 2021-11-09 ~ 2022-06-17
- **역할**: 프로젝트 전담 리더 — 웹/블록체인 API 설계·구현, Sample VASP API 개발, 버전 관리

## 디렉토리 구조 (README 기반)

```
travelrule-api/
├── documents/       # reStructuredText + Sphinx 기반 공식 문서 (HTML/PDF 생성)
├── examples/        # 각 거래소가 구현해야 할 WebSocket 샘플 (NodeJS + Java Spring)
├── lightning-api/   # 라이트닝 메인 서비스
├── loadtest/        # Locust 기반 로드 테스트
└── management/      # 거래소용 관리 대시보드 (Python backend + React frontend)
```

## 기술 스택

- **백엔드 메인**: Python (FastAPI 추정)
- **데이터베이스**: MariaDB (기존 포트폴리오 참고)
- **캐시/메시징**: Redis, NATS
- **로드 테스트**: Locust (`loadtest/`)
- **문서**: Sphinx + reStructuredText (`documents/`)
- **샘플 SDK**: NodeJS, Java Spring (거래소 연동용)
- **관리 대시보드**: Python backend + React frontend
- **컨테이너·배포**: Docker
- **클라우드**: AWS

## 관련 프로젝트 문서

- [`docs/20-projects/com2us-platform/2021-10-code-travel-rule-api.md`](../../../../20-projects/com2us-platform/) (작성 예정, 2022년 이전 프로젝트이므로 필요시)

## 관련 스킬

- `backend-python` (FastAPI, Locust)
- `database` (MariaDB, Redis)
- `blockchain` (트래블룰 규제 대응)
- `devops-container` (Docker)
- `frontend-react` (관리 대시보드)
