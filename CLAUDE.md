# LLM Wiki Schema

> 이 파일은 LLM 에이전트(Claude Code, Cowork 등)가 위키를 운영할 때 따라야 할 규칙과 워크플로우를 정의합니다.
> 세션을 시작할 때 반드시 이 파일을 먼저 읽으세요.

## 소유자 정보

- 이름: 석근
- 직업: 컴투스플랫폼 게임 데이터 BI 서비스 개발자
- 관심 분야: 파이썬, AI, 데이터 분석, 개인 비서 AI 서비스 개발
- 개발 환경: 회사 맥북 / 집 윈도우, IDE는 Antigravity와 Claude Code
- 선호 스택: Python, FastAPI, 바이브 코딩

## 디렉토리 구조

```
llm-wiki/
├── CLAUDE.md              # 이 파일 (스키마)
├── raw/                   # 원시 소스 (불변, 절대 수정 금지)
│   ├── articles/          # 웹 기사, 블로그 포스트
│   ├── papers/            # 논문, 기술 보고서
│   ├── notes/             # 개인 메모, 회의록, 일기
│   └── assets/            # 이미지, PDF 등 첨부 파일
├── wiki/                  # LLM이 관리하는 위키 (LLM만 쓰기)
│   ├── entities/          # 사람, 조직, 도구, 서비스 등 고유 대상
│   ├── concepts/          # 개념, 기술, 방법론, 이론
│   ├── sources/           # 원시 소스별 요약 페이지
│   ├── syntheses/         # 여러 소스를 종합한 분석, 비교, 에세이
│   ├── logs/              # 로그 파일
│   │   └── log.md         # 시간순 활동 기록
│   └── index.md           # 전체 위키 카탈로그
└── templates/             # 페이지 템플릿
    ├── entity.md
    ├── concept.md
    ├── source.md
    ├── synthesis.md
    └── lesson.md           # Microsoft for-beginners 페다고지 6단 응용
```

## 핵심 규칙

### 불변 원칙
1. `raw/` 디렉토리의 파일은 **절대 수정하지 않는다**. 읽기 전용.
2. `wiki/` 디렉토리는 **LLM만 작성/수정**한다. 소유자는 읽기만 한다.
3. 원문을 위키 페이지에 통째로 복사하지 않는다. 핵심만 추출하고 원본을 참조한다.

### 네이밍 규칙
- 파일명: `kebab-case.md` (영어, 소문자, 하이픈)
- 페이지 제목(H1): 한국어 우선 (예: `# 트랜스포머 아키텍처`). 단, 한국어 표기가 어색하거나 영어 식별자가 표준 호칭인 경우(`Microsoft`, `DevOps & CI/CD`) 영어 우선 허용.
- 내부 링크: Obsidian 위키링크 `[[파일명]]` 사용
- 태그 (적용 범위 4단계 — 31회차 명확화):
  - **개념·도메인 태그**: 한국어 + 영어 병기 의무. (예: `[인공지능, artificial-intelligence]`, `[백엔드, backend]`, `[데이터분석, data-analysis]`)
  - **제품·라이브러리·도구·약어 태그**: 영어 단독 허용. 영어 식별자 자체가 표준 호칭인 경우 한국어 번역 강제 안 함. (예: `fastapi`, `uv`, `zustand`, `BI`, `mcp`)
  - **고유명사 태그**: 한국어 단독 허용. 한국 인물·조직 등 한국어가 일차 표기인 경우. 검색 편의를 위해 영어 라틴 표기 동시 추가 권장. (예: `[석근, owner]`, `[컴투스플랫폼, com2us-platform]`)
  - **회차 / 메타 태그**: `22회차`, `30회차`, `agents-md` 등 추적용 태그 자유 사용.

### 프론트매터 규칙
- 모든 위키 페이지는 YAML 프론트매터 필수
- **공통 필수 필드**: `title`, `type`, `tags`
- **타입별 필수 필드**:
  - `entity`: `entity_type`, `related`, `source_count`, `created`, `updated`
  - `concept`: `category`, `related`, `source_count`, `created`, `updated`
  - `source`: `source_type`, `source_url`, `raw_path`, `author`, `date_published`, `date_ingested`, `related`, `confidence` (※ source는 `date_ingested`로 시간 추적, `created`/`updated` 사용 안 함)
  - `synthesis`: `category`, `sources`, `created`, `updated`
- 자세한 형식은 `templates/{entity,concept,source,synthesis}.md` 참조

### Redirect / RAG 제외 규칙
- canonical 병합 때문에 남기는 alias 페이지는 `entity_type: redirect`, `canonical: "[[대상]]"`, `rag_exclude: true`를 함께 둔다.
- `rag_exclude: true` 페이지는 Obsidian 링크 호환용으로만 유지한다. 질의 답변의 근거 페이지로 사용하지 말고 `canonical` 대상 페이지로 이동한다.
- lint에서 `source_count: 0`과 고아 페이지를 셀 때는 `rag_exclude: true` redirect 페이지를 별도 집계한다.

## 워크플로우

### 세션 시작 시
1. 이 파일(`CLAUDE.md`)을 읽는다
2. `wiki/index.md`를 읽어서 현재 위키 상태를 파악한다
3. `wiki/logs/log.md`의 최근 5개 항목을 읽어서 최근 활동을 파악한다

### 수집 (Ingest) 워크플로우
새로운 소스가 `raw/`에 추가되었을 때:

1. **읽기**: 소스를 완독한다. 이미지가 있으면 별도로 확인한다.
2. **논의**: 소유자와 핵심 시사점을 간단히 논의한다. 무엇을 강조할지 방향을 잡는다.
3. **소스 요약 작성**: `wiki/sources/`에 요약 페이지를 생성한다. 템플릿을 따른다.
4. **엔티티/개념 업데이트**: 소스에서 언급된 주요 엔티티와 개념을 확인한다.
   - 기존 페이지가 있으면 → 새 정보를 반영하여 업데이트
   - 기존 페이지가 없으면 → 새 페이지 생성
   - 기존 내용과 모순이 있으면 → `## 논쟁/모순` 섹션에 기록
5. **종합 분석 업데이트**: 관련 종합 분석 페이지가 있으면 새 소스를 반영하여 업데이트한다.
6. **인덱스 업데이트**: `wiki/index.md`에 새 페이지를 등록하고, 변경된 페이지의 요약을 갱신한다.
7. **로그 기록**: `wiki/logs/log.md`에 수집 기록을 추가한다.

### 질의 (Query) 워크플로우
소유자가 위키에 대해 질문했을 때:

1. `wiki/index.md`를 읽어서 관련 페이지를 찾는다.
2. 관련 페이지들을 읽고 정보를 종합한다.
3. 답변 시 출처 페이지를 `[[위키링크]]`로 인용한다.
4. 가치 있는 답변은 소유자의 동의 하에 `wiki/syntheses/`에 저장한다.

### 점검 (Lint) 워크플로우
소유자가 "점검해줘" 또는 "lint"라고 요청했을 때:

#### 자동 도구 (32회차 신설)

```bash
python3 scripts/wiki-lint.py --check       # 결함 발견 시 exit 1
python3 scripts/wiki-lint.py --report      # 인바운드 분포 + 5축 통계
python3 scripts/wiki-lint.py --update      # source_count 자동 갱신 (정의 B 기준)
```

자동 검증 항목 (스크립트가 처리):
1. **깨진 위키링크** — 의도된 예시는 `EXAMPLE_TARGETS` 화이트리스트에 등록
2. **고아 페이지** (인바운드 0) — `rag_exclude: true` redirect / `index` / `log` 별도 집계
3. **frontmatter YAML invalid** — PyYAML 파싱 실패 케이스
4. **source_count 부정합** — `정의 A` (수동) vs `정의 B` (객관) 차이 보고. **결함이 아닌 정보 보고**
5. **빈약 페이지** — `source_count` >= 3 인데 본문 < 30줄
6. **인바운드 분포 / 5축 hub 합산** — `--report` 모드

#### `source_count` 두 가지 정의 (32회차 명문화)

- **정의 A (운영 컨벤션, 수동 입력)**: 이 페이지의 정보 출처가 된 source 페이지 수. frontmatter 작성 시 운영자가 수동 결정. 본문에 위키링크가 박히지 않아도 정보 출처로 간주 가능.
- **정의 B (객관 측정, 자동 갱신 가능)**: 이 페이지를 `[[위키링크]]`로 인용한 source 페이지 수. lint가 측정하는 값.

기본 운영은 **정의 A**를 따른다. `--update`는 정의 B로 일괄 갱신하므로 의미 손실이 발생할 수 있어 신중히 사용한다.

#### 수동 점검 (소유자와 논의 필요)

7. 2개 이상의 페이지에서 서로 모순되는 주장
8. 언급은 되지만 자체 페이지가 없는 주요 개념
9. 최근 수집된 소스가 기존 주장을 업데이트했어야 하는데 반영 안 된 곳
10. 웹 검색으로 보완할 수 있는 데이터 공백
11. 탐색할 새로운 질문이나 찾아볼 새로운 소스 제안
12. 28회차-2 `raw 측정 vs 위키 본문 자동 대조` SOP — 정량 주장이 raw 데이터와 일치하는지 사용자 의심 발생 시 검증

결과를 보고하고, 소유자와 논의 후 수정한다.

## 금지 사항

- `.obsidian/` 디렉토리 수정 금지
- `raw/` 디렉토리 수정 금지
- 위키 페이지에 원문 전체를 복사하지 않는다
- 프론트매터 없는 위키 페이지를 만들지 않는다
- `index.md` 업데이트 없이 새 페이지를 만들지 않는다
- `log.md` 기록 없이 수집을 완료하지 않는다

## 카테고리 가이드 (개인 종합 위키)

석근님의 관심 영역에 맞춘 주요 카테고리:

### 기술/개발
- AI/ML (LLM, 프롬프트 엔지니어링, RAG, 에이전트 등)
- 데이터 분석 (파이썬, pandas, SQL, 시각화 등)
- 웹 개발 (FastAPI, 프론트엔드, 인프라 등)
- 개발 도구 (IDE, CLI, Git, 바이브 코딩 등)

### 업무
- 게임 데이터 BI (지표, 대시보드, 분석 패턴 등)
- 컴투스플랫폼 관련 내부 지식

### 개인
- 자기 개발 / 학습 기록
- 가족 / 생활
- 독서 / 콘텐츠 소비 기록
- 사이드 프로젝트 아이디어

이 카테고리는 고정이 아니며, 위키가 성장하면서 자연스럽게 확장/변경될 수 있다.
