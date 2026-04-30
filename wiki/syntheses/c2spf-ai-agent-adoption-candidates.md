---
title: c2spf AI Agent 도입 후보 — MateChat 자작 SKILL 9건 + 차용 매트릭스
type: synthesis
category: guide
aliases:
- c2spf AI agent 도입
- c2spf-ai-agent-adoption-candidates
- MateChat SKILL 차용 후보
- c2spf 차용 매트릭스
tags:
- c2spf
- matechat
- agent-skills
sources:
- '[[seokgeun-mate-chat]]'
- '[[c2spf-analytics-renewal]]'
- '[[c2spf-analytics-common]]'
related:
- '[[c2spf-analytics]]'
- '[[matechat]]'
- '[[com2us-platform]]'
- '[[seokgeun-kim]]'
- '[[agent-skills]]'
- '[[parental-leave-2026-operating-plan]]'
created: 2026-04-29
updated: 2026-04-29
verification_required: true
last_verified: 2026-04-29
verification_notes: 분기별 PoC 진행 상태 갱신 (검토/진행/완료/포기). 2026-Q4까지 최소 1건 도입 목표.
cited_by_count: 12
inbound_count: 17
---

# c2spf AI Agent 도입 후보 — MateChat 자작 SKILL 9건 + 차용 매트릭스

> [!important] 실행형 hub — MateChat → c2spf 단방향 펌프의 실행 SOP
> 신설 (Codex 권고 P1). [[matechat|MateChat 사이드 프로젝트]]에서 검증된 자작 11개 SKILL 중 mate-chat 도메인 특화 2개를 제외한 **9개의 c2spf 차용 후보**를 우선순위·도입 비용·기대 효과로 정량화. 박힌 가설을 PoC로 회수하는 게 본 페이지의 핵심.
> 
> 한국어 표기: **c2spf AI Agent 도입 후보** 또는 **MateChat 차용 매트릭스**.

## 언제 읽어야 하는가

- "MateChat 자작 SKILL 중 회사로 차용 가능한 게 무엇인가?" — 9건 매트릭스 직행.
- "어느 SKILL부터 PoC를 시작해야 하나?" — 우선순위 점수 표.
- "PoC를 어떻게 진행하나?" — PoC SOP 섹션.
- "이미 진행된 PoC 결과는?" — 진행 추적 표 (verification_required: true로 분기 갱신).

## 1. MateChat 자작 11개 → c2spf 차용 9개 분류

[[seokgeun-mate-chat]] 검증 결과:

| SKILL | 도메인 | c2spf 차용 가능 | 비고 |
|---|---|---|---|
| `api-consistency` | API 표준 | ✅ Yes | FastAPI 응답 envelope·에러 코드 표준 |
| `fastapi-testing` | 백엔드 테스트 | ✅ Yes | pytest async + httpx 클라이언트 패턴 |
| `websocket-pattern` | 실시간 통신 | ✅ Yes | 사내 BI 실시간 알림에 적용 가능 |
| `security-review` | 보안 감사 | ✅ Yes | OWASP·인증/인가 체크리스트 |
| `migration-safety` | DB 마이그레이션 | ✅ Yes | Alembic 안전 패턴 |
| `pre-deployment` | 배포 전 검증 | ✅ Yes | CI에서 자동 트리거 |
| `feature-workflow` | 기능 개발 SOP | ✅ Yes | spec → impl → test → review |
| `doc-management` | 문서 관리 | ✅ Yes | API/README 자동 갱신 |
| `skill-creator` | SKILL 신설 메타 | ✅ Yes | c2spf 자체 SKILL 생성 부트스트랩 |
| `build-app-bundle` | Android Flutter 전용 | ❌ No | mate-chat 도메인 특화 |
| `flutter-qa-audit` | Flutter QA 전용 | ❌ No | mate-chat 도메인 특화 |

**차용 가능 9개**.

## 2. 우선순위 점수 (Effort × Impact × Risk)

스코어 = (Impact 1~5) × (Risk 역수 1~5) ÷ (Effort 1~5). 높을수록 우선.

| SKILL | Impact | Risk | Effort | Score | 우선순위 |
|---|---|---|---|---|---|
| `migration-safety` | 5 | 1 (낮음) | 1 | **25.0** | 🔴 P0 |
| `pre-deployment` | 5 | 1 | 1 | **25.0** | 🔴 P0 |
| `api-consistency` | 4 | 2 | 1 | **8.0** | 🟡 P1 |
| `fastapi-testing` | 4 | 1 | 2 | **8.0** | 🟡 P1 |
| `security-review` | 5 | 2 | 2 | **6.25** | 🟡 P1 |
| `doc-management` | 3 | 1 | 2 | **6.0** | 🟡 P1 |
| `feature-workflow` | 4 | 3 | 2 | **2.67** | 🟢 P2 |
| `skill-creator` | 5 | 4 | 2 | **1.56** | 🟢 P2 |
| `websocket-pattern` | 3 | 4 | 3 | **0.25** | 🟢 P2 |

**순위 해석**:
- **P0 2건** (migration-safety / pre-deployment): 안전 강화 + 회사 영향 큼 + 도입 비용 낮음. 첫 PoC 후보.
- **P1 4건** (api-consistency / fastapi-testing / security-review / doc-management): 표준화 가치 큼.
- **P2 3건**: 기존 회사 SOP와 충돌 가능, 신중 검토.

## 3. PoC SOP

### 단계
1. **검토** (1주): SKILL 본문 + 회사 환경 매핑 문서 1장 작성
2. **소규모 적용** (1주): 1개 팀·1개 프로젝트에 한정 적용
3. **회고** (1주): KPI 측정 (적용 전후 차이) + 팀 피드백 수집
4. **확장 결정** (1주): Go (전사 표준화) / Iterate (개선 후 재시도) / Drop (적합도 낮음)

### 측정 KPI (각 SKILL별 정의)
- `migration-safety`: 마이그레이션 롤백 횟수 / 다운타임 분 단위
- `pre-deployment`: 배포 후 핫픽스 횟수 / 평균 발견 시간
- `api-consistency`: API 응답 포맷 일관성 점수 (linter 기반)
- `fastapi-testing`: 백엔드 테스트 커버리지 % / 신규 테스트 작성 시간

### 비용
- PoC 1건당 owner 시간 약 4주 × 5h/주 = 20h
- [[parental-leave-2026-operating-plan]] Q2~Q3에 1건씩 배치

## 4. 진행 추적 (verification_required: true)

분기별 갱신:

| SKILL | 상태 | 시작일 | 완료일 | 회고 링크 |
|---|---|---|---|---|
| migration-safety | 검토 전 | - | - | - |
| pre-deployment | 검토 전 | - | - | - |
| api-consistency | 검토 전 | - | - | - |
| fastapi-testing | 검토 전 | - | - | - |
| security-review | 검토 전 | - | - | - |
| doc-management | 검토 전 | - | - | - |
| feature-workflow | 검토 전 | - | - | - |
| skill-creator | 검토 전 | - | - | - |
| websocket-pattern | 검토 전 | - | - | - |

## 5. 회사 컨텍스트 제약

- c2spf는 **보수적 운영** — AI Agent 도입 자체에 사내 합의 필요
- 회사 보안 정책상 **claude-code 사용 가능 여부**가 차용 전제
- mcp 서버를 사내 BigQuery·Loki 등에 연결하려면 **별도 보안 검토**
- **owner 단독 도입 vs 팀 표준화** 분기 — 단독 도입은 빠르나 확산은 팀 합의 필요

## 출처

- [[seokgeun-mate-chat]] — 자작 11개 SKILL 분포 + 외부 28개 통합 운영
- [[c2spf-analytics-renewal]] — 2025 React 리뉴얼 시 사용된 SOP 참고
- [[c2spf-analytics-common]] — 공통 모듈에 차용 시 영향 범위

## 열린 질문

- 회사 보안 정책상 외부 SKILL repo 직접 클론이 가능한가? (대안: 사내 fork)
- PoC 결과를 portfolio 저장소에 STAR 스토리로 박을 수 있나? (회사 IP 이슈)
- 첫 PoC가 실패하면 다음 SKILL로 빠르게 전환할지, 또는 1년 종료 후 회고로 연기할지?
