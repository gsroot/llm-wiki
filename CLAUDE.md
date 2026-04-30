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
│   └── index.md           # 전체 위키 카탈로그
└── templates/             # 페이지 템플릿
    ├── entity.md
    ├── concept.md
    ├── source.md
    ├── synthesis.md
    └── lesson.md          # Microsoft for-beginners 페다고지 6단 응용
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

### 태그 정책 (canonical + aliases 분리)

- **tags에는 canonical 1개만** 박는다. 표기 변종은 **frontmatter `aliases:`** (Obsidian 표준 alias)로 검색 변종을 흡수한다.
- canonical 결정 원칙: 현재 우세 표기를 채택한다 (정정 마찰 최소화).
- 회귀 차단: `wiki-lint.py`가 canonical-alias 매핑 위반을 자동 보고한다.

**6쌍 canonical 결정**:

| canonical | 강등(정정 대상) | 우세 비율 |
|---|---|---|
| `agent` | `에이전트` | 46:19 영어 우세 (LLM agent 기술 표준어) |
| `harness` | `하네스` | 64:6 영어 압도 |
| `백엔드` | `backend` | 9:5 한국어 우세 |
| `데이터분석` | `data-analysis` | 5:4 한국어 약간 우세 |
| `위키` | `wiki` | 13:1 한국어 압도 |
| `석근` | `owner` | 한국어 우선 (owner 정체성) — `owner`는 alias로 흡수 |

**적용 범위**:

- **개념·도메인 태그**: canonical 1개. (예: `백엔드`, `데이터분석`)
- **제품·라이브러리·도구·약어 태그**: 영어 단독 허용 (예: `fastapi`, `uv`, `zustand`, `BI`, `mcp`).
- **고유명사 태그**: 한국어 단독 허용 (예: `석근`, `컴투스플랫폼`).

**vocabulary 과밀 차단**:

- 새 태그 추가 시 **최소 3페이지 이상 사용 가능성** 검토 의무.
- 페이지 본문 키워드를 그대로 태그로 박지 말 것 (검색은 본문 텍스트로 충분히 잡힘). sub-keyword·fringe technical detail은 frontmatter `aliases:` 또는 본문 위임.
- 회귀 차단 임계: `wiki-lint.py`가 unique > 700 OR 저빈도(1-2회) > 60% 시 경고.

### 프론트매터 규칙

- 모든 위키 페이지는 YAML 프론트매터 필수
- **공통 필수 필드**: `title`, `type`, `tags`
- **타입별 필수 필드**:
  - `entity`: `entity_type`, `related`, `source_count`, `created`, `updated`
  - `concept`: `category`, `related`, `source_count`, `created`, `updated`
  - `source`: `source_type`, `source_url`, `raw_path`, `author`, `date_published`, `date_ingested`, `related`, `confidence` (※ source는 `date_ingested`로 시간 추적, `created`/`updated` 사용 안 함)
  - `synthesis`: `category`, `sources`, `created`, `updated`
- 자세한 형식은 `templates/{entity,concept,source,synthesis}.md` 참조

### 선택 필드

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

#### `aliases` (Obsidian 표준 alias)

- 표기 변종이 다수 존재하는 hub·고유명사 페이지에 적용. Obsidian의 `Cmd+O` 빠른 열기·자동완성·역링크 alias 그래프 활성화.
- 형식: `aliases: [표기1, 표기2, ...]` (YAML 리스트). 한국어·영어·약어 변종 모두 가능.
- 예: `matechat.md` → `aliases: [MateChat, 메이트챗, mate-chat, 메트챗]` / `c2spf-analytics.md` → `aliases: [c2spf-analytics, c2spf 게임 데이터 BI, 컴투스플랫폼 BI]` / `seokgeun-stack-guide.md` → `aliases: [석근 스택 가이드, 32 OSS 카탈로그]`.
- 적용 대상: 5축 hub 5개(`seokgeun-kim`·`portfolio`·`seokgeun-stack-guide`·`matechat`·`llm-infra-meta-cluster`) + 5축 sub-hub 4개(`agent-skills`·`harness`·`mcp`·`claude-code`) + 변동성 높은 entity(`c2spf-analytics`·`com2us-platform` 등).
- 운영 원칙: tags에 표기 변종을 박아 우회하던 패턴은 deprecated. tags는 검색 vocabulary, aliases는 표기 변종 — 역할 분리.
- redirect stub 페이지는 여전히 유지(canonical 병합 이력 보존). aliases는 redirect와 보완 관계, 대체 관계 아님.

### Redirect / RAG 제외 규칙

#### redirect alias 페이지

- canonical 병합 때문에 남기는 alias 페이지는 `entity_type: redirect`, `canonical: "[[대상]]"`, `rag_exclude: true`를 함께 둔다.
- `rag_exclude: true` 페이지는 Obsidian 링크 호환용으로만 유지한다. 질의 답변의 근거 페이지로 사용하지 말고 `canonical` 대상 페이지로 이동한다.
- lint에서 `source_count: 0`과 고아 페이지를 셀 때는 `rag_exclude: true` redirect 페이지를 별도 집계한다.

#### 메타 페이지 RAG 제외

- `wiki/index.md` (카탈로그·라우터)는 `rag_exclude: true` + `rag_exclude_reason:` 의무.
- 이유: 인덱스의 통계 숫자(페이지 수, 인바운드 합산)를 RAG 답변 근거로 사용하면 stale 정보가 노출된다. 사실 답변은 hub/concept/entity/synthesis 페이지를 직접 인용해야 한다.
- lint 검증: `type: index` 페이지에 `rag_exclude: true`가 없으면 결함.

## 워크플로우

### 세션 시작 시

1. 이 파일(`CLAUDE.md`)을 읽는다
2. `wiki/index.md`를 읽어서 현재 위키 상태를 파악한다

### 수집 (Ingest) 워크플로우

새로운 소스가 `raw/`에 추가되었을 때:

1. **읽기**: 소스를 완독한다. 이미지가 있으면 별도로 확인한다.
2. **논의**: 소유자와 핵심 시사점을 간단히 논의한다. 무엇을 강조할지 방향을 잡는다.
3. **소스 요약 작성**: `wiki/sources/`에 요약 페이지를 생성한다. 템플릿을 따른다.
4. **엔티티/개념 업데이트**: 소스에서 언급된 주요 엔티티와 개념을 확인한다.
   - 기존 페이지가 있으면 → 새 정보를 반영하여 업데이트
   - 기존 페이지가 없으면 → 새 페이지 생성
   - 기존 내용과 모순이 있으면 → `## 논쟁/모순` 섹션에 기록
5. **약자 풀이 의무**: hub 페이지의 첫 단락(요약 또는 정의 섹션)에서 위키 내 약자·고유명사가 처음 등장할 때 **한 번 이상 풀어쓰기**를 한다.
   - 적용 대상: `c2spf-analytics`, `c2spf`, `matechat`, `MateChat`, `seokgeun-stack-guide`, `llm-infra-meta-cluster` 등 owner 컨텍스트 약자.
   - 형식 예: "*c2spf-analytics(컴투스플랫폼 게임 데이터 BI 시스템, 2017~)*" 또는 "MateChat(석근의 사이드 프로젝트 AI 소셜 메시징 앱, v1.0.0 출시)".
   - 이유: RAG가 단일 페이지를 컨텍스트에 로드했을 때 약자만 보고 LLM이 "이게 무엇이고 왜 owner에게 중요한지"를 추론 가능해야 한다. 약자가 위키 다른 페이지에 링크돼 있어도 단일 청크 컨텍스트에서는 보이지 않는다.
   - 비적용: 산업 표준 약자(LLM, AI, RAG, MCP, OSS, BI, CI/CD 등)는 풀어쓰기 강제하지 않음.
6. **출처 정합화 의무**: entity/concept 페이지가 새 source를 반영할 때, **frontmatter `related` 와 본문 `## 출처` 섹션 양쪽 모두에 source 페이지 wikilink를 동시에** 추가해야 한다.
   - frontmatter `related`는 자동 추적의 source-of-truth, 본문 `## 출처`는 사람의 가독성을 위한 표시. 두 곳이 같은 source 페이지 목록을 가져야 한다.
   - 가능하면 entity 본문에도 raw에서 직접 가져온 인용 블록(quote) 1개 이상을 두어 "개념 ↔ raw" 추적을 명시화한다.
7. **종합 분석 업데이트**: 관련 종합 분석 페이지가 있으면 새 소스를 반영하여 업데이트한다.
8. **인덱스 업데이트**: `wiki/index.md`에 새 페이지를 등록하고, 변경된 페이지의 요약을 갱신한다.

### 질의 (Query) 워크플로우

소유자가 위키에 대해 질문했을 때:

1. `wiki/index.md`를 읽어서 관련 페이지를 찾는다.
2. 관련 페이지들을 읽고 정보를 종합한다.
3. 답변 시 출처 페이지를 `[[위키링크]]`로 인용한다.
4. 가치 있는 답변은 소유자의 동의 하에 `wiki/syntheses/`에 저장한다.

### RAG 답변 정책

LLM 에이전트가 위키를 RAG 컨텍스트로 사용해 답변할 때 따라야 할 신뢰도·랭킹 규칙.

#### 신뢰도·랭킹에 사용 금지 (자동 비교 불가 필드)

- **`source_count`** (정의 A, 운영자 수동): 페이지 사이의 "출처 풍부도"를 비교하는 데 사용 금지. 수동 의미 필드는 운영자의 시점·기준에 종속돼 페이지 간 일관 비교가 보장되지 않는다.

#### 신뢰도·랭킹에 사용 권장 (자동 측정 또는 시간 기반 필드)

- **`cited_by`** (source 페이지 전용, 자동 갱신): 이 source가 몇 페이지에서 인용됐는지로 영향력 측정. RAG 답변 시 인용 후보 source 페이지의 우선순위 결정에 사용.
- **`inbound_count`** (자동 갱신): 페이지의 그래프 중심성 지표. hub 페이지 라우팅·신뢰도 가중치에 사용 가능.
- **`observed_source_refs`** (자동 갱신): 정의 B. 자동 측정값이라 페이지 간 일관 비교 가능.
- **`last_verified` / `verification_required`**: 외부 상태 의존 페이지의 신선도 판정. 90일 초과 페이지는 답변 근거로 채택할 때 "최근 검증 필요" 경고 동반.
- **`sources` / 본문 `## 출처` 섹션**: 답변에 직접 인용할 raw 출처 추적.

#### 답변 작성 시 행동 규칙

1. **수치 비교 금지**: 두 페이지 간 "더 강한 출처를 가진 페이지"를 가릴 때 `source_count` 값을 비교하지 말 것. 비교가 필요하면 `inbound_count` 또는 `observed_source_refs`를 사용.
2. **인용 우선순위**: 답변에 wikilink 인용 시 hub 페이지(인바운드 100+) → entity/concept → source 순으로 검토. source 페이지 자체를 인용 근거로 쓸 때는 `last_verified` 신선도 확인.
3. **메타 페이지 인용 금지**: `rag_exclude: true` 페이지(`index.md`, redirect alias)는 답변 근거로 인용하지 말 것.
4. **약자 풀이 인용**: hub 페이지 첫 단락의 약자 풀이를 답변에서 한 번 이상 그대로 인용해 사용자가 약자만 보고 추론 부담을 갖지 않게 한다.
5. **출처 부재 답변 시 명시**: 위키 안에서 답변 근거 페이지를 못 찾았을 때는 "위키에 해당 정보 없음" 명시. 추측·모델 사전지식으로 채우지 말 것.

### 점검 (Lint) 워크플로우

소유자가 "점검해줘" 또는 "lint"라고 요청했을 때:

#### 자동 도구

```bash
python3 scripts/wiki-lint.py --check       # 결함 발견 시 exit 1
python3 scripts/wiki-lint.py --report      # 인바운드 분포 + 5축 통계
python3 scripts/wiki-lint.py --update      # observed_source_refs / inbound_count / cited_by / cited_by_count 자동 갱신
```

자동 검증 항목 (스크립트가 처리):

1. **깨진 위키링크** — 의도된 예시는 `EXAMPLE_TARGETS` 화이트리스트에 등록
2. **고아 페이지** (인바운드 0) — `rag_exclude: true` redirect / `index` 별도 집계
3. **frontmatter YAML invalid** — PyYAML 파싱 실패 케이스
4. **source_count 부정합** — `정의 A` (수동 `source_count`) vs `정의 B` (자동 `observed_source_refs`) 차이 보고. **결함이 아닌 정보 보고** (delta ±50까지 정상 범위로 간주)
5. **빈약 페이지** — `source_count` >= 3 인데 본문 < 30줄
6. **메타 페이지 rag_exclude 누락** — `type: index` 페이지에 `rag_exclude: true`가 없으면 결함
7. **인바운드 분포 / 5축 hub 합산** — `--report` 모드
8. **태그 case-duplicate 검출** — 같은 태그의 대소문자 변형 동시 존재 검출 (회귀 방지)
9. **canonical-alias 위반** — tags 안 강등 표기(예: `에이전트`)가 박힌 경우 결함
10. **태그 vocabulary 과밀 경고** — unique > 700 OR 저빈도(1-2회) > 60% 시 정보 보고
11. **citation chain 양방향 정합** — source의 `cited_by` 와 인용한 페이지의 `[[source]]` wikilink 양방향 일치 검증

#### `source_count` 세 가지 의미 분리

운영자 수동 정의(A)와 자동 측정값(B/C) 충돌을 명시적으로 분리한다.

| 필드 | 의미 | 입력 방식 | 보존 |
|---|---|---|---|
| `source_count` | **정의 A**: 이 페이지의 정보 출처가 된 source 페이지 수 (운영자 의미 판단). 본문에 위키링크가 박히지 않아도 정보 출처로 간주 가능. | 수동 (frontmatter) | 유지 |
| `observed_source_refs` | **정의 B**: 이 페이지를 `[[위키링크]]`로 인용한 source 페이지 수 (자동 측정값). | 자동 (`wiki-lint.py --update`가 갱신, 운영자는 수동 입력 안 함) | 도입 |
| `inbound_count` | **정의 C**: 이 페이지를 인용한 모든 페이지 수 (entity·concept·synthesis·source 무관). 그래프 인바운드 총량. | 자동 (`--update`로 갱신) | 도입 |

운영 원칙:

1. **운영자는 `source_count`만 수동 관리**한다. 빈약 페이지 검사는 이 값 기준.
2. `observed_source_refs`·`inbound_count`는 **자동 갱신 전용** — 수동 입력 금지.
3. lint check 4번(`source_count` 부정합)은 정의 A vs 정의 B 차이 보고 — **결함이 아닌 정보 보고**. 정의 A는 "운영자가 핵심으로 보는 source 페이지 수"이며, hub 페이지 본문에 인용된 source 중 운영자 기준 핵심 출처만 카운트한다. 본문 wikilink로 박힌 모든 source가 자동으로 가산되지 않으므로 정의 A < 정의 B는 정상이다 (delta ±50까지 정상 범위).
4. RAG·평가 시 신뢰도·출처 풍부도 비교는 **반드시 정의 B(`observed_source_refs`) 또는 `inbound_count`·`cited_by_count`** 사용. 정의 A는 LLM의 비교 입력에서 제외.
5. `--update` 모드는 `observed_source_refs`·`inbound_count`·`cited_by` 자동 필드만 갱신한다. **`source_count`는 절대 자동 덮어쓰지 않는다**.

#### `cited_by` (source 페이지 전용)

source 페이지 frontmatter에 자동으로 박히는 역참조 리스트. RAG 답변 시 사용자가 "이 source가 위키 어디에서 인용됐는지"를 추적 가능하게 한다 (citation chain 양방향화).

```yaml
cited_by:
  - "[[matechat]]"
  - "[[matechat-chat-analysis-module]]"
  - "[[seokgeun-matechat-validation]]"
```

- **자동 갱신 전용**: `wiki-lint.py --update`가 측정·갱신. 운영자 수동 입력 금지.
- **포함 대상**: source 페이지를 wikilink로 인용한 모든 비-메타 페이지(entity/concept/synthesis/source). 메타 페이지(index, redirect)의 인용은 제외.
- **빈 list**: cited_by 키 자체를 frontmatter에서 제거 (orphan source의 깔끔한 표시).
- **정렬**: 알파벳순 (재현 가능한 갱신).

#### `cited_by_count` (모든 비-메타 페이지)

`cited_by` 리스트의 길이를 단일 정수로 캐싱한 보조 자동 필드. hub 페이지·entity·concept·synthesis 모두 적용 가능. RAG 답변 시 인바운드 강도를 정수 한 번 읽기로 비교 가능하게 한다.

```yaml
cited_by_count: 67
```

- **자동 갱신 전용**: `wiki-lint.py --update`가 함께 캐싱. 운영자 수동 입력 금지 (수동값은 `--update` 시 덮어씀).
- **`cited_by` 리스트 vs `cited_by_count`**: `cited_by`는 source 페이지 전용(자동 양방향 추적), `cited_by_count`는 모든 비-메타 페이지에서 가능(정수 캐시).
- **사용 처**: RAG 답변 정책 §1 "수치 비교" 시 `inbound_count`·`observed_source_refs`·`cited_by_count` 셋 중 가장 적합한 것을 선택. 일반적으로 hub 라우팅 신뢰도 가중치는 `inbound_count`·`cited_by_count` 사용.
- **`source_count`와의 관계**: `source_count`(정의 A 운영자 의미)와 무관한 자동 필드. delta가 누적돼도 결함이 아니다.

#### 수동 점검 (소유자와 논의 필요)

1. 2개 이상의 페이지에서 서로 모순되는 주장
2. 언급은 되지만 자체 페이지가 없는 주요 개념
3. 최근 수집된 소스가 기존 주장을 업데이트했어야 하는데 반영 안 된 곳
4. 웹 검색으로 보완할 수 있는 데이터 공백
5. 탐색할 새로운 질문이나 찾아볼 새로운 소스 제안
6. raw 측정 vs 위키 본문 자동 대조 — 정량 주장이 raw 데이터와 일치하는지 사용자 의심 발생 시 검증

결과를 보고하고, 소유자와 논의 후 수정한다.

### 패턴 결함 grep 전수 검사 SOP

평가·점검·작업 중 frontmatter 키 typo·태그 중복·중복 단락 등 **패턴 결함**을 발견한 경우, 정정 직후 grep으로 동일 패턴이 다른 파일에 잔존하는지 **전수 검사 의무**.

**적용 트리거**:

- frontmatter 키 단복수 혼용·오타 발견 (예: `sources_count` vs `source_count`)
- 본문 단락 중복 발견 (예: 같은 unique 문자열이 한 페이지에 2번)
- 태그·alias 표기 변종 발견 (예: `agent` vs `에이전트` 분기)
- redirect·rag_exclude·cited_by_count 등 정책 필드 누락 패턴 발견

**검사 명령 패턴**:

```bash
# 정확한 typo·키 잔존
grep -rn "^typo_pattern" /Users/sgkim/Projects/llm-wiki/wiki/

# 본문 단락 중복 (단락 첫 30자 unique signature)
grep -c "unique signature" /Users/sgkim/Projects/llm-wiki/wiki/path/file.md  # 2 이상이면 중복
```

**commit message 의무 항목**: P0/P1 commit message에 "**grep 전수 검증 결과: N건 잔존 / N건 정정**" 명시. 단 1건 정정으로 끝낸 작업은 SOP 미적용으로 간주, 사후 평가에서 회귀 결함으로 적발 가능.

## 금지 사항

- `.obsidian/` 디렉토리 수정 금지
- `raw/` 디렉토리 수정 금지
- 위키 페이지에 원문 전체를 복사하지 않는다
- 프론트매터 없는 위키 페이지를 만들지 않는다
- `index.md` 업데이트 없이 새 페이지를 만들지 않는다

## 추출 거버넌스 (Extraction Governance)

원천 자료(source)에서 wiki layer(concept/entity/synthesis) 신설 여부를 판단할 때 따르는 일관 기준. 목적은 **over-extract(과도한 신설로 위키 비대화) 와 under-extract(자료가 위키에 흐르지 않아 그래프 빈약화) 양극단을 동시에 방어**하는 것.

### 4-layer 결정 트리

source 1개에서 후보를 식별할 때 순차 적용:

1. **이미 위키에 존재?** → 기존 페이지 frontmatter `related` + 본문 `## 출처`에 source 추가, 끝.
2. **어느 layer 후보?**
   - 고유명사(사람/조직/도구/시스템) → entity 후보
   - 추상 개념·패턴·방법론 → concept 후보
   - 2+ source를 가로지르는 비교/타임라인/hub → synthesis 후보
   - 위 어느 것도 아님 → source 페이지 본문에만 남기고 끝
3. **layer별 5-test 중 3개 이상 통과** (다음 표) → Pass면 신설, Fail이면 source에만 둠.
4. **inbound 기대 점검**: 6개월 내 2+ 페이지에서 인용될까? Yes → 신설 확정. No → 보류, 두 번째 source 등장 시 재평가.

### Concept 5-test

| 테스트 | 질문 |
|---|---|
| **Recurrence** | 2+ source에 등장하나? |
| **Generalizability** | 단일 source 맥락 밖에서도 적용되나? |
| **Owner relevance** | owner가 이 개념을 도구로 쓸 가능성? |
| **Stable name** | 인용 가능한 안정 명칭? |
| **Body weight** | 본문 30+줄 쓸 거리 있나? |

### Entity 5-test

| 테스트 | 질문 |
|---|---|
| **Uniqueness** | 세상에 하나뿐인 고유명사? |
| **Centrality** | 1+ source의 주요 주제? (지나가는 언급 ✗) |
| **Inbound potential** | 2+ 다른 페이지에서 참조될 가능성? |
| **Stability** | 6+ 개월 지속 존재할 대상? |
| **Owner relevance** | owner stack/관심에 연결? |

### Synthesis 5-test

| 테스트 | 질문 |
|---|---|
| **Multi-source** | 진짜 2+ source를 합쳐 만든 것인가? (4+ 권장: §Synthesis 분류 정책) |
| **New insight** | 단일 source엔 없던 새 그림(비교/타임라인/hub)? |
| **Owner-actionable** | owner의 의사결정·라우팅에 도움? |
| **Sustained relevance** | 6+ 개월 후에도 가치 있나? |
| **Can't-fit-elsewhere** | 기존 concept/entity/synthesis에 흡수 안 되나? |

### Volume sanity check (편차 최소화)

source type별 **예상 추출량 대역**. 적색 신호 발생 시 5-test 재실행.

| Source 타입 | 신규 concept | 신규 entity | 신규 synthesis | 기존 페이지 보강 |
|---|---|---|---|---|
| 두꺼운 입문서·교재 | 3~6개 | 0~2개 | 0~1개 | 5~10개 |
| 단일 OSS 레포 | 1~3개 | 1개(레포 자체) | 0개 | 3~5개 |
| 짧은 블로그·기사 | 0~1개 | 0~1개 | 0개 | 1~3개 |
| owner 본인 노트 | 0개 | 0~2개 | 0~1개 | 2~5개 |

**적색 신호**:
- 1개 source에서 concept **10+개** 신설 시도 → over-extract, Recurrence 재검
- 두꺼운 입문서인데 concept **0개** 신설 → under-extract, 5-test 재실행
- synthesis 신설 시 sources < 2 → multi-source 위반, source 페이지로 격하

### Under-extract 자동 탐지 (lint 신호)

`wiki-lint.py`가 보고하는 신호로 사후 audit:

| 신호 | 의미 | 조치 |
|---|---|---|
| source 페이지 `inbound_count == 1` (index만 인용) | 자료가 위키 어디에도 안 흘러감 | 5-test 재실행, 누락 추출 발굴 |
| concept 페이지 `cited_by_count == 1` | 1 source에만 묶임 → 진짜 concept 아닐 수 있음 | Recurrence 재검, source로 흡수 검토 |
| synthesis `sources` 길이 < 2 | multi-source 위반 | source로 격하 또는 흡수 |

자세한 lint 항목은 `## 점검 (Lint) 워크플로우` 섹션 참조. 본 신호는 결함이 아닌 **정보 보고**.

### 적용 의무

- **새 source 수집 시**: 본 거버넌스를 명시적으로 따라 신설/보강 후보를 식별. commit message에 "추출 결과: concept N개 신설 + entity M개 보강 + synthesis K개 신설/흡수" 명시.
- **재평가 트리거**: 분기 1회 audit 또는 lint under-extract 신호 발생 시 5-test 재실행.
- **Synthesis 분류 정책과의 관계**: 본 5-test 통과 후 synthesis로 신설된 페이지는 다음 §Synthesis 분류 정책의 category(`hub`/`comparison`/`operating-log` 등) 분류 의무를 추가로 받는다.

## Synthesis 분류 정책

`wiki/syntheses/` 페이지는 두 가지 성격이 혼재한다. RAG·평가·인용 우선순위에서 두 성격을 구분하기 위해 `category:` 필드로 명시 분리한다.

### 진정한 synthesis (응집 메시지)

- **요건**: 최소 4개 source 인용 + 다중 source를 종합한 새 통찰·비교·해석 틀 제시.
- **category 예시**: `hub`, `comparison`, `analysis`, `architect`, `data`, `dev-tools`, `timeline`, `ai`, `frontend-architect`.
- **RAG 답변 정책**: hub 라우팅 / 답변 근거로 우선 인용.

### 운영 기록 (operating-log)

- **요건**: 단일 프로젝트의 운영 기록·검증 루프·정책 audit.
- **category**: `operating-log`.
- **RAG 답변 정책**: 답변 근거로 인용 가능하나, hub 라우팅에서는 후순위. 시점 라벨(`date`) 신선도 확인 필수.
- **현재 분류 대상**: `kpi-recovery-loop`, `matechat-30day-validation-loop`, `matechat-launch-metrics-ledger`, `parental-leave-2026-operating-plan` (4개).

### 신설·갱신 시 의무

- 새 synthesis 페이지는 source 4개 미만이면 `category: operating-log` 또는 다른 source/concept 페이지로 흡수 검토.
- 운영 기록은 `category: operating-log` 명시 의무. RAG 답변 시 LLM이 hub 인용과 분리해 인지하도록 함.

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
