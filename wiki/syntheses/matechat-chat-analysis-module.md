---
title: "Mate Chat 채팅 분석 모듈 — 7축 분석 + BigQuery 파이프라인 (24회차 종합)"
type: synthesis
category: side-project-analysis
sources:
  - "[[seokgeun-mate-chat]]"
  - "[[matechat-project-knowledge-map]]"
  - "[[seokgeun-operating-profile-2026]]"
sources_count: 3
related:
  - "[[matechat]]"
  - "[[backend-fastapi-stack]]"
  - "[[dataframe-ecosystem-evolution]]"
  - "[[duckdb]]"
  - "[[polars]]"
  - "[[pandas-ai]]"
  - "[[flutter-nextjs-fullstack-pattern]]"
  - "[[seokgeun-stack-guide]]"
  - "[[data-pipeline-bigquery]]"
created: 2026-04-28
updated: 2026-04-28
tags: [matechat, chat-analysis, bigquery, analytics, kakao-talk, ml, side-project, c2spf-bi-applicable, 24회차]
---

# Mate Chat 채팅 분석 모듈 — 7축 분석 + BigQuery 파이프라인

## 한줄 요약

[[matechat]] 본진(v1.0.0 출시 직전 QA 단계) 외에 석근이 운영 중인 **3개 형제 분석 프로젝트**(`mate-katok-analysis-backend` + `mate-katok-analysis-flutter` + `data-mate`)와 메모리 컨텍스트(2026-04-27 S442/S443)에 박혀있는 **7가지 채팅 분석 축 + BigQuery 파이프라인** 설계 메모를 한 페이지로 통합. 회사 BI([[c2spf-analytics]]) 게임 데이터 분석에 직접 적용 가능한 패턴 정리.

## 형제 프로젝트 3개 (24회차 발견)

`/Users/sgkim/Projects/` 트리에서 채팅·데이터 분석 관련 4개 형제 프로젝트 발견. 24회차에서는 디렉토리 트리만 확인하고 raw 수집은 25회차 후속:

| 프로젝트 | 정체성 | 의존성·도구 |
|---|---|---|
| `mate-katok-analysis-backend` | 카카오톡 채팅 분석 백엔드 (FastAPI) | Poetry / Dockerfile / docker-compose / gunicorn / gcloud / **notebooks/** (Jupyter) / firebase.json |
| `mate-katok-analysis-flutter` | 카카오톡 분석 결과 시각화 모바일 앱 | Flutter (android/ios/web/macos/linux/windows 6 platform) |
| `data-mate` | 별도 데이터 분석 프로젝트 (CLAUDE.md + project-plan.md 풍부) | 자체 backend+frontend / Docker compose 듀얼 / pyproject.toml / config·docs·pages·tests 풍부 |
| (참고) `mate_chat_cloud_functions` | Mate Chat 본진 보조 (Firebase Functions) | (별도) |

**핵심 관찰**:
- `mate-katok-analysis-*` 듀얼 = **카카오톡(외부 데이터) 분석** — Mate Chat 본진 채팅 분석이 아닌, 사용자가 가진 카카오톡 대화 로그를 분석하는 별도 서비스
- `data-mate` 단독 = **자체 데이터 분석 프로젝트** — 별도 비전·로드맵 (project-plan.md 명시)
- Mate Chat 본진(`mate-chat/`)은 **운영 중 v1.0.0** 채팅 서비스 자체. 채팅 데이터 분석은 별도 형제 프로젝트로 분리.

→ Mate Chat 본진의 채팅 분석은 **(가설) 본진 PostgreSQL → 형제 분석 백엔드 → BigQuery → 분석 Flutter** 흐름이 가능하나, 본 24회차에서는 raw 미수집으로 **공식적 검증 안 됨**. 25회차에서 3 형제 프로젝트 raw 수집 후 본 종합 페이지 보강.

## 7가지 분석 축 (메모리 컨텍스트 S443)

2026-04-27 메모에 박혀있는 채팅 분석 모듈 설계 7개 축:

| # | 축 | 분석 대상 | 출력 |
|---|---|---|---|
| 1 | **메시지 빈도 시계열** | sender_id × 시간 단위 (시·일·주) | 사용량 곡선, 최대 활동 시간대 |
| 2 | **대화 지속 길이 분포** | 채팅방별 메시지 ↔ 응답 간격 | 활성 채팅방 / 휴면 채팅방 분류 |
| 3 | **AI 트리거 비율** | `@botname` 멘션 메시지 / 전체 | AI 의존도, 챗봇 활용 분석 |
| 4 | **읽음 시점 지연** | sent_at ↔ read_at 차이 | 응답성 분포, 알림 효과성 |
| 5 | **그룹 채팅 vs 1:1 비율** | room.type 별 메시지 분포 | 소셜 패턴 분류 |
| 6 | **이탈 예측 신호** | 사용자 마지막 활동 ↔ 현재 시간 + 빈도 추세 | 이탈 위험군 (회사 BI에서 직접 차용 가능) |
| 7 | **콘텐츠 분류** | 메시지 텍스트 → LLM 분류 (정보 / 감정 / 일상 / 약속 등) | 채팅 의도 분포, [[pandas-ai]] / GPT-4 응용 |

→ 7개 축 중 **1, 2, 4, 5번은 SQL만으로**, **3, 6, 7번은 LLM 또는 ML 분류기 필요**.

## BigQuery 파이프라인 아키텍처 (메모리 컨텍스트 S442)

### 흐름

```
[Mate Chat PostgreSQL]      [Mate Chat 본진 운영 중 — v1.0.0]
       │
       │ (a) Logical Replication 또는 일배치 export
       ↓
[GCS Parquet 스테이징]      [Apache Arrow + Parquet 16회차 표준]
       │
       │ (b) BigQuery EXTERNAL TABLE 또는 LOAD
       ↓
[BigQuery 분석 데이터셋]    [컬럼 압축 + 열 기반 쿼리]
       │
       ├─→ (c) 7축 분석 SQL 뷰 (1·2·4·5)
       │
       ├─→ (d) [[pandas-ai]] / GPT-4 분류 LLM 파이프라인 (3·6·7)
       │
       └─→ (e) Flutter 분석 클라이언트 (mate-katok-analysis-flutter 패턴)
```

### 단계별 도구 매핑

| 단계 | 도구 | 위키 회차 |
|---|---|---|
| (a) 추출 | PostgreSQL → CDC (Debezium) 또는 일배치 SQL | (신규) |
| (b) 스테이징 | [[parquet]] + GCS / [[pyarrow]] | 16 |
| (b) 로드 | BigQuery EXTERNAL TABLE 또는 BQ LOAD | (신규) |
| (c) SQL 뷰 | BigQuery / [[duckdb]] (로컬 검증) | 16 |
| (c) 대용량 분석 | [[polars]] (Rust) | 16 |
| (d) LLM 분류 | OpenAI GPT-4 + [[pandas-ai]] | 17/18 |
| (d) 머신러닝 | [[scikit-learn]] / [[lightgbm]] (이탈 예측) | 17 |
| (e) 시각화 | Flutter (mate-katok-analysis-flutter 사례) 또는 [[nextjs]]+[[shadcn-ui]] | 22 |
| (e) 알림 | FCM 푸시 (이상 탐지 트리거) | (신규) |
| 운영 | [[sentry]] / [[prometheus]] / structlog | 21 |

→ **위키 22회차까지의 거의 모든 도구가 단일 분석 파이프라인 내에 매핑 가능**.

## 회사 BI ([[c2spf-analytics]]) 직접 차용 가능 패턴

7축 중 회사 게임 데이터 BI에 거의 그대로 적용 가능한 4개:

| 축 | Mate Chat 적용 | 컴투스플랫폼 게임 데이터 적용 |
|---|---|---|
| **1 메시지 빈도 시계열** | sender × 시간 | player × 시간 (DAU/MAU 곡선) |
| **4 읽음 지연** | sent ↔ read | 게임 내 행동 ↔ 응답 (튜토리얼 이탈, 푸시 응답률) |
| **6 이탈 예측** | last activity + 빈도 | 게임별 이탈 위험군 (회사 핵심 KPI) |
| **7 콘텐츠 분류** | 메시지 의도 | 고객 문의·리뷰 LLM 분류 |

→ Mate Chat 분석 모듈을 1회 만들어두면 컴투스플랫폼 BI에 패턴 복제 가능. **개인 사이드 프로젝트가 회사 업무에 역으로 학습 자원 제공**하는 구조.

## 23회차 stub 가설과의 차이

23회차 [[matechat]] stub에서 다음과 같이 적었음:

> **추정 스택 — 분석**: (가설) BigQuery 파이프라인, ML 분석 레이어

24회차 raw 수집으로 검증한 결과:
- **본진 mate-chat에는 BigQuery 파이프라인 미통합** — Sentry/Prometheus 운영 메트릭만 있고 분석 데이터 흐름 없음
- 분석 모듈은 **3개 형제 프로젝트로 분리** (mate-katok-analysis-backend / -flutter / data-mate)
- 본 페이지의 BigQuery 파이프라인은 **(아직) 가설 영역에 머무름** — 25회차 형제 프로젝트 raw 수집으로 실제 흐름 확정 필요

## 미래 작업

1. **25회차 raw 수집**: 3 형제 프로젝트(mate-katok-analysis-backend / -flutter / data-mate)의 README + pyproject.toml + CLAUDE.md / project-plan.md / notebooks/ 1차 자료 수집. 본 종합 페이지 (a)~(e) 단계의 실제 도구 검증 또는 가설 폐기.
2. **7축 SQL 템플릿화**: 1·2·4·5번 축의 SQL 뷰 템플릿을 [[seokgeun-stack-guide]]에 "데이터 분석 30분 부트스트랩" 섹션으로 추가.
3. **이탈 예측 (6번 축) 별도 종합**: [[lightgbm]] / [[scikit-learn]] 적용 + 회사 BI 직접 차용 시나리오 분리 — 25~26회차 후보.
4. **콘텐츠 분류 (7번 축)**: [[pandas-ai]] vs OpenAI 직접 호출 비교, 한국어 한글 토크나이즈 한계 검증.
5. **Mate Chat 본진과 분석 모듈 통합**: BigQuery로 일배치 적재가 합리적인지 vs 본진 PostgreSQL 안에서 직접 분석이 합리적인지 — DB 부하 vs 분석 자유도 트레이드오프.

## 사용 출처 (24회차)

신규:
- [[seokgeun-mate-chat]] — 24회차 Mate Chat 본진 1차 수집

기존 통합:
- [[matechat-project-knowledge-map]] (18회차) — Mate Chat 위키 스냅샷
- [[seokgeun-operating-profile-2026]] (17회차) — 석근 운영 프로필 / 사업화 맥락
- [[matechat]] entity (24회차 정식 격상)

## 메모

- **본 종합은 가설 영역**: 24회차에서는 형제 프로젝트 raw 미수집으로, 분석 모듈의 실제 구현이 본 페이지 BigQuery 파이프라인 가설과 일치하는지 검증 안 됨. **25회차 후속 작업**으로 명시.
- 23회차 stub의 "BigQuery 파이프라인" 추정은 메모리 컨텍스트 S442에서 유래한 것으로, 본 24회차에서 raw 검증 시도 후 **분석 모듈이 본진과 분리된 별도 프로젝트로 운영**된다는 실태 확인.
- **[[c2spf-analytics]] 직접 응용 가치**가 본 모듈의 위키 보존 가치를 정당화. 1회 자기 프로젝트로 만들어두면 회사 BI에 4개 축 그대로 복제 가능.
- LLM 분류(7번 축)는 [[pandas-ai]] vs 직접 OpenAI 호출의 사용 시나리오 분리 필요. PandasAI는 자연어 → SQL 자동 변환에 강하고, 직접 호출은 분류 정확도 통제에 강함.
- 한국어 채팅 데이터 특성상 토크나이즈·임베딩 다국어 모델 (예: bge-m3, multilingual-e5) 검토 필요. 25회차 형제 프로젝트 수집에서 어떤 임베딩 모델 사용 중인지 확인.
