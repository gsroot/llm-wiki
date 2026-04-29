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

### 선택 필드 (33회차 신설 — 외부 평가 합집합 P0)

#### `source_scope` (source 페이지 전용)
- `source_url: ""` 인 source 페이지는 `source_scope` 필드 의무.
- 값 도메인: `local` (석근 본인 작성 노트) / `private` (외부 자료지만 공식 URL 없음, 예: PDF 책) / `public` (URL 있는 공개 자료, 생략 가능 — 명시 시는 검증 강도 ↑).
- 목적: `source_url` 빈 문자열이 "공개 자료인데 URL 누락"인지 "본질적으로 비공개 로컬 자료"인지 구분.
- lint 검증: `source_url == ""` 인데 `source_scope` 부재면 결함.

#### `verification_required` / `last_verified` (변동성 높은 페이지 전용)
- 외부 상태가 변할 수 있는 주장(출시 상태, OSS 버전, 회사 시스템 상태 등)에 적용.
- `verification_required: true` 와 `last_verified: YYYY-MM-DD` 를 함께 둔다.
- `verification_notes:` 로 무엇을 어떻게 재검증해야 하는지 명시 (선택).
- lint 검증: `last_verified` 가 90일 초과 시 경고 (결함 아님, 정보 보고).
- 적용 대상 예시: `matechat` (Google Play 출시 상태), `seokgeun-stack-guide` (OSS 라이브러리 버전), `c2spf-analytics` (회사 시스템 운영 상태), `seokgeun-mate-chat` (39 SKILL 분류).

### Redirect / RAG 제외 규칙

#### redirect alias 페이지
- canonical 병합 때문에 남기는 alias 페이지는 `entity_type: redirect`, `canonical: "[[대상]]"`, `rag_exclude: true`를 함께 둔다.
- `rag_exclude: true` 페이지는 Obsidian 링크 호환용으로만 유지한다. 질의 답변의 근거 페이지로 사용하지 말고 `canonical` 대상 페이지로 이동한다.
- lint에서 `source_count: 0`과 고아 페이지를 셀 때는 `rag_exclude: true` redirect 페이지를 별도 집계한다.

#### 메타 페이지 RAG 제외 (43회차 신설 — Codex+자체 합집합 P0)
- `wiki/index.md` (카탈로그·라우터)와 `wiki/logs/*.md` (활동 로그·회차 회고)는 `rag_exclude: true` + `rag_exclude_reason:` 의무.
- 이유: 인덱스의 통계 숫자(페이지 수, 인바운드 합산)나 로그의 회차별 메타 기록을 RAG 답변 근거로 사용하면 stale 정보가 노출된다. 사실 답변은 hub/concept/entity/synthesis 페이지를 직접 인용해야 한다.
- lint 검증 (43회차 신설): `type: index` 또는 `type: log` 페이지에 `rag_exclude: true`가 없으면 결함.

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
5. **약자 풀이 의무 (43회차 명문화 — 자체 평가 P1)**: hub 페이지의 첫 단락(요약 또는 정의 섹션)에서 위키 내 약자·고유명사가 처음 등장할 때 **한 번 이상 풀어쓰기**를 한다.
   - 적용 대상: `c2spf-analytics`, `c2spf`, `matechat`, `MateChat`, `seokgeun-stack-guide`, `llm-infra-meta-cluster` 등 owner 컨텍스트 약자.
   - 형식 예: "*c2spf-analytics(컴투스플랫폼 게임 데이터 BI 시스템, 2017~)*" 또는 "MateChat(석근의 사이드 프로젝트 AI 소셜 메시징 앱, v1.0.0 출시)".
   - 이유: RAG가 단일 페이지를 컨텍스트에 로드했을 때 약자만 보고 LLM이 "이게 무엇이고 왜 owner에게 중요한지"를 추론 가능해야 한다. 약자가 위키 다른 페이지에 링크돼 있어도 단일 청크 컨텍스트에서는 보이지 않는다.
   - 비적용: 산업 표준 약자(LLM, AI, RAG, MCP, OSS, BI, CI/CD 등)는 풀어쓰기 강제하지 않음.
6. **출처 정합화 의무 (37회차 명문화)**: entity/concept 페이지가 새 source를 반영할 때, **frontmatter `related` 와 본문 `## 출처` 섹션 양쪽 모두에 source 페이지 wikilink를 동시에** 추가해야 한다.
   - 35·36회차에 두 번 발견된 결함 패턴: 본문 `## 출처`만 작성하고 frontmatter `related`에서 source 페이지를 누락하면 자동화 도구(wiki-lint.py·RAG)가 출처를 추적하지 못한다.
   - frontmatter `related`는 자동 추적의 source-of-truth, 본문 `## 출처`는 사람의 가독성을 위한 표시. 두 곳이 같은 source 페이지 목록을 가져야 한다.
   - 가능하면 entity 본문에도 raw에서 직접 가져온 인용 블록(quote) 1개 이상을 두어 "개념 ↔ raw" 추적을 명시화한다 (36·37회차 stack-guide 도구 보강에서 채택한 "## 의사결정 컨텍스트 (raw 인용)" 섹션 패턴).
7. **종합 분석 업데이트**: 관련 종합 분석 페이지가 있으면 새 소스를 반영하여 업데이트한다.
8. **인덱스 업데이트**: `wiki/index.md`에 새 페이지를 등록하고, 변경된 페이지의 요약을 갱신한다.
9. **로그 기록**: `wiki/logs/log.md`에 수집 기록을 추가한다.

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
python3 scripts/wiki-lint.py --update      # observed_source_refs / inbound_count 자동 갱신 (43회차: source_count는 자동 갱신 안 함)
```

자동 검증 항목 (스크립트가 처리):
1. **깨진 위키링크** — 의도된 예시는 `EXAMPLE_TARGETS` 화이트리스트에 등록
2. **고아 페이지** (인바운드 0) — `rag_exclude: true` redirect / `index` / `log` 별도 집계
3. **frontmatter YAML invalid** — PyYAML 파싱 실패 케이스
4. **source_count 부정합** — `정의 A` (수동 `source_count`) vs `정의 B` (자동 `observed_source_refs`) 차이 보고. **결함이 아닌 정보 보고** (delta ±10 이상이면 운영자 의미 재검토 권장)
5. **빈약 페이지** — `source_count` >= 3 인데 본문 < 30줄
6. **메타 페이지 rag_exclude 누락** (43회차 신설) — `type: index/log` 페이지에 `rag_exclude: true`가 없으면 결함
7. **인바운드 분포 / 5축 hub 합산** — `--report` 모드

#### `source_count` 세 가지 의미 분리 (43회차 명문화 — Codex 권고 채택)

32회차에 운영자 수동 정의(A)와 자동 측정값(B) 두 가지가 충돌한다는 것이 발견됐다. 43회차에 외부(Codex) 평가가 "필드명 분리가 LLM의 숫자 신뢰도 문제를 해소한다"고 권고했고, 이를 채택해 **세 가지 의미를 명시적으로 구분**한다.

| 필드 | 의미 | 입력 방식 | 보존 |
|---|---|---|---|
| `source_count` | **정의 A**: 이 페이지의 정보 출처가 된 source 페이지 수 (운영자 의미 판단). 본문에 위키링크가 박히지 않아도 정보 출처로 간주 가능. | 수동 (frontmatter) | **유지** |
| `observed_source_refs` | **정의 B**: 이 페이지를 `[[위키링크]]`로 인용한 source 페이지 수 (자동 측정값). | 자동 (`wiki-lint.py --update`가 갱신, 운영자는 수동 입력 안 함) | 도입 (43회차) |
| `inbound_count` | **정의 C**: 이 페이지를 인용한 모든 페이지 수 (entity·concept·synthesis·source 무관). 그래프 인바운드 총량. | 자동 (`--update`로 갱신) | 도입 (43회차) |

운영 원칙:
1. **운영자는 `source_count`만 수동 관리**한다. 빈약 페이지 검사는 이 값 기준.
2. `observed_source_refs`·`inbound_count`는 **자동 갱신 전용** — 수동 입력 금지.
3. lint check 4번(`source_count` 부정합)은 정의 A vs 정의 B 차이 보고 — **결함이 아닌 정보 보고**. delta가 큰 경우(±10 이상) 운영자가 의미 재검토.
4. `--update` 모드는 `observed_source_refs`·`inbound_count`·`cited_by` 자동 필드만 갱신한다. **`source_count`는 절대 자동 덮어쓰지 않는다**(32회차의 "의미 손실" 위험 제거).

#### `cited_by` (source 페이지 전용 — 47회차 신설, Codex P1 권고 채택)

source 페이지 frontmatter에 자동으로 박히는 역참조 리스트. RAG 답변 시 사용자가 "이 source가 위키 어디에서 인용됐는지"를 추적 가능하게 한다 (citation chain 양방향화).

```yaml
cited_by:
  - "[[matechat]]"
  - "[[matechat-chat-analysis-module]]"
  - "[[seokgeun-matechat-validation]]"
```

- **자동 갱신 전용**: `wiki-lint.py --update`가 측정·갱신. 운영자 수동 입력 금지.
- **포함 대상**: source 페이지를 wikilink로 인용한 모든 비-메타 페이지(entity/concept/synthesis/source). 메타 페이지(log, index, index-history, by-session, redirect)의 인용은 제외 — 메타 페이지가 답변 근거 출처로 추적되면 안 됨.
- **빈 list**: cited_by 키 자체를 frontmatter에서 제거 (orphan source의 깔끔한 표시).
- **정렬**: 알파벳순 (재현 가능한 갱신).

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
