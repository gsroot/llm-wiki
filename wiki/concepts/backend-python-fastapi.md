---
title: "Python 백엔드 (FastAPI · Spring Boot 비교 맥락)"
type: concept
category: web-dev
tags: [backend, python, fastapi, flask, django, spring-boot, sqlalchemy, pytest, api, tiangolo, agent-skills, annotated, pydantic2, 백엔드]
related:
  - "[[seokgeun-kim]]"
  - "[[c2spf-analytics]]"
  - "[[devops-cicd]]"
  - "[[data-pipeline-bigquery]]"
  - "[[fastapi]]"
  - "[[tiangolo]]"
source_count: 6
observed_source_refs: 18
inbound_count: 47
created: 2026-04-24
updated: 2026-04-27
---

# Python 백엔드 (FastAPI · Spring Boot 비교 맥락)

## 정의

석근의 주력 백엔드 스택. Python 기반(FastAPI · Flask · Django · SQLAlchemy · Alembic · Pytest · Celery)이 핵심이고, Java 기반(Spring Boot · MyBatis · JPA · Gradle)은 c2spf 애널리틱스의 리포트 계층에서 병행 사용된다. 두 스택은 한 시스템 안에서 **하이브리드 파이프라인**으로 공존.

## 왜 중요한가

- 석근의 본인 정의: "Python 기반 백엔드 서비스와 데이터 파이프라인을 설계·개발하는 개발자". 가장 깊이 있는 영역.
- 9년 경력의 절반 이상이 이 스택 위에서 진행됨 — Flask(초기) → FastAPI(현재 주력)로 진화.
- c2spf 애널리틱스 공통 API(FastAPI)와 리포트 계층(Spring Boot)이 같은 시스템에서 공존, **APICode/ProcessedData 이원 에러 정책**으로 분기 가능.

## 핵심 내용

- **FastAPI** — 현재 주력. 비동기 처리, 자동 OpenAPI 스키마 생성, Pydantic 검증.
  - c2spf `analytics-common-api` (231/251 커밋, ~92%) — 단독 유지보수.
  - 트래블메이트 / Mate Chat 백엔드 (개인 프로젝트).
  - CODE 트래블룰 API (FastAPI + SQLAlchemy + Pytest + Locust).
- **Spring Boot** — c2spf 애널리틱스 리포트 계층, 줌인터넷 스윙 브라우저.
  - MyBatis + JPA 다중 소스 구성으로 BigQuery·MySQL을 같은 리포트 모듈에서 처리.
- **Flask** — 레거시 ML 예측 서비스(2020-2021), 통합 인증 모듈(2021-06~07), 대용량 다운로드 API(2019).
- **NestJS** (Node.js) — XPLA · NFT 마켓.
- **공통 패턴**
  - APIResponse `{result_code, message, data}` envelope (FastAPI 측 표준).
  - APICode 13종 + BigQuery 결과 코드 4종 정립.
  - Pydantic v1/v2 마이그레이션 경험.
  - SQLAlchemy + Alembic 스키마 마이그레이션, Pytest 단위 테스트.

## 실전 적용

- **하이브리드 파이프라인**: Spring Boot 리포트 → FastAPI 가공 → React 시각화.
- **Airbridge MMP 결합**: `/common/processed-data` 단일 엔드포인트에서 BigQuery + Airbridge 결합·피벗팅.
- **HIVE OAuth 8 엔드포인트 통합**: Redis 캐시 기반 게임 권한 조회, 패턴 매칭 무효화.
- **운영 디테일**: BigQuery Decimal 변환, OS별 TCP Keepalive, 슬레이브 DB 동기화 이슈 대응.

## 관련 개념

- [[data-pipeline-bigquery]] — 백엔드가 호출하는 데이터 레이어
- [[devops-cicd]] — Docker + Jenkins 멀티브랜치 배포로 운영
- [[frontend-react]] — APIResponse 계약을 소비

## 출처

- [[portfolio-seed]] — Flask → FastAPI 진화 타임라인
- [[portfolio-resume-ko]] — 정량 지표(커밋 수)
- [[portfolio-ko]] — Selected Work 5선
- [[c2spf-analytics-common]] — FastAPI 공통 API 표준화
- [[c2spf-analytics-renewal]] — Spring Boot + FastAPI 하이브리드 파이프라인
- [[fastapi-fastapi]] — fastapi/fastapi v0.136.1 공식 저장소 (README · docs · pyproject.toml · `.agents/skills/fastapi/SKILL.md`). 라이브러리가 직접 출하하는 코딩 컨벤션 — `Annotated` 강제, `def` 디폴트, `ORJSONResponse` deprecation, Asyncer/SQLModel/HTTPX 권장, 라우터 레벨 prefix/tags. c2spf `analytics-common-api` 점검 기준점.

## 공식 SKILL.md가 제시하는 코딩 컨벤션 (2026-04 갱신)

[[fastapi]] v0.136.1부터 `fastapi/.agents/skills/fastapi/SKILL.md`가 라이브러리 자체에 번들링되어 LLM 에이전트가 자동으로 따라야 할 권장사항이 명문화됐다:

- **`Annotated[T, Path/Query/Depends(...)]` 강제**: 디폴트 인자(`q: str = Query(...)`) 패턴 금지. 시그니처가 다른 컨텍스트(테스트, 문서)에서도 의미 보존 + 재사용성.
- **return type annotation 우선**: `response_model=`보다 함수 반환 타입을 권장. Pydantic 2 Rust 직렬화로 처리되므로 `ORJSONResponse`/`UJSONResponse`는 deprecated.
- **`def` 디폴트, async는 확실할 때만**: blocking I/O는 `def`(자동 threadpool)에서 안전. async 안에 blocking이 가장 큰 성능 함정.
- **라우터 레벨 prefix/tags/dependencies**: `include_router()`에 인자 전달하지 말고 `APIRouter(prefix=..., tags=...)`에 둔다.
- **함수 1개 = HTTP operation 1개**: `@app.api_route(methods=[...])` 다중 메서드 회피.
- **Pydantic `RootModel` 회피**: 대신 `Annotated[list[int], Field(min_length=1), Body()]`.
- **Tiangolo 추천 보조 스택**: Asyncer(>AnyIO/asyncio), SQLModel(>SQLAlchemy), HTTPX(>Requests), uv·Ruff·ty.

c2spf `analytics-common-api`가 이 권장과 어디서 일치/충돌하는지 점검하는 게 단기 후속 작업.

## 열린 질문

- Pydantic v2 마이그레이션 후 성능 변화는 측정되었는가?
- Spring Boot 부분을 FastAPI로 통합 일원화하는 시나리오의 비용/이득은?
- 기존 `result_code/message/data` envelope을 `Annotated` + 제네릭 응답 모델로 표현하면 자동 OpenAPI 스키마와 잘 맞는가?
- SQLAlchemy 자산을 SQLModel로 점진 마이그레이션하는 비용은? (Pydantic 모델과 통합되는 이득 vs 마이그레이션 부담)
