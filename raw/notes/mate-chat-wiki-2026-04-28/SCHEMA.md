# Mate Chat Wiki Schema

## Overview

이 위키는 Mate Chat 프로젝트의 지식 베이스입니다.
LLM이 작성하고 유지관리하며, `docs/`의 원시 문서를 종합하여 구조화된 지식으로 변환합니다.

## Architecture

```
docs/          ← Raw Sources (불변, LLM은 읽기만)
wiki/          ← Wiki (LLM이 소유, 작성/수정)
  ├── SCHEMA.md       ← 이 파일 (위키 운영 규칙)
  ├── index.md        ← 콘텐츠 카탈로그
  ├── log.md          ← 시간순 활동 기록
  ├── entities/       ← 시스템 구성 요소 (서비스, 모델, API 등)
  ├── concepts/       ← 아키텍처 개념/패턴/의사결정
  ├── sources/        ← 원시 문서 요약
  └── synthesis/      ← 종합 분석, 비교, 로드맵
```

## Page Types

### Source (`sources/`)
원시 문서(`docs/`)의 요약 페이지. 핵심 시사점을 추출.

```yaml
---
title: "문서 제목"
type: source
source_path: docs/XX-filename.md
date_ingested: YYYY-MM-DD
tags: []
related: []
---
```

### Entity (`entities/`)
시스템의 구체적 구성 요소. 서비스, 모델, 엔드포인트 그룹, 인프라 등.

```yaml
---
title: "엔티티 이름"
type: entity
source_count: N
tags: []
related: []
---
```

필수 섹션: Overview, Architecture/Structure, Key Details, Dependencies, Known Issues, Related

### Concept (`concepts/`)
아키텍처 패턴, 의사결정, 기술적 개념.

```yaml
---
title: "개념 이름"
type: concept
source_count: N
tags: []
related: []
---
```

필수 섹션: Definition, How It Works in Mate Chat, Trade-offs, Related

### Synthesis (`synthesis/`)
여러 소스/엔티티/개념을 종합한 분석. 로드맵, 비교, 아키텍처 개관 등.

```yaml
---
title: "종합 분석 제목"
type: synthesis
source_count: N
tags: []
related: []
---
```

## Rules

### Naming
- 파일명: `kebab-case.md` (영어)
- 제목(H1): 한국어 또는 영어 (내용에 맞게)
- 내부 링크: `[표시텍스트](../category/filename.md)` 상대 경로

### Content
- 원시 소스(`docs/`)는 절대 수정하지 않는다
- 원문을 통째로 복붙하지 않는다 — 핵심만 추출하고 출처를 명시한다
- 모순이 발견되면 명시적으로 기록한다 (`> **모순**: ...`)
- 코드 예시는 최소한으로, 패턴과 의도에 집중한다

### Ingest Workflow
새 소스 수집 시:
1. 소스 문서를 읽는다
2. `sources/`에 요약 페이지를 작성한다
3. 관련 `entities/` 페이지를 생성하거나 업데이트한다
4. 관련 `concepts/` 페이지를 생성하거나 업데이트한다
5. 필요시 `synthesis/` 페이지를 업데이트한다
6. `index.md`를 업데이트한다
7. `log.md`에 항목을 추가한다

### Lint Checklist
점검 시 확인 항목:
- [ ] index.md에 등록되었지만 실제 파일이 없는 항목
- [ ] 파일은 있지만 index.md에 누락된 페이지
- [ ] 인바운드 링크가 없는 고아 페이지
- [ ] 페이지 간 모순되는 주장
- [ ] 언급되었지만 자체 페이지가 없는 주요 개념
- [ ] source_count 대비 내용이 빈약한 페이지

### Session Start
새 세션 시작 시 위키 작업 전에:
1. `wiki/index.md`를 읽어 전체 구조 파악
2. `wiki/log.md`의 최근 항목을 읽어 마지막 활동 확인
