---
title: "활동 로그"
type: log
---

# 활동 로그

> 위키의 모든 활동(수집, 질의, 점검 등)을 시간순으로 기록합니다.
> 각 항목은 `## [날짜] 유형 | 제목` 형식을 따릅니다.

---

## [2026-04-27] ingest | anthropics/skills 수집 — Agent Skills 표준·마켓플레이스·skill-creator

- **소스 (raw 신규 보관)** — `raw/articles/anthropics-skills/` (8 파일):
  - `README.md` (5.5KB) — 마켓플레이스 등록·스킬 작성 가이드·document-skills 라이선스 안내
  - `marketplace.json` — 3개 플러그인(document-skills 4개, example-skills 12개, claude-api 1개) 정의
  - `template-skill.md` — 7줄 placeholder
  - `spec-redirect.md` — `spec/agent-skills-spec.md`가 agentskills.io/specification으로 리다이렉트되는 안내문
  - `skill-creator-skill.md` (33KB) — 가장 풍부한 메타-스킬, 5단계 루프·description 최적화·Claude.ai/Cowork specific 분기
  - `mcp-builder-skill.md` (9KB) — multi-domain reference 분리 패턴
  - `frontend-design-skill.md` (4.4KB) — 짧고 강한 단일 SKILL.md 패턴
  - `webapp-testing-skill.md` (3.9KB) — "scripts는 읽지 마라" 블랙박스 패턴
- **선택 근거**: 17개 스킬 전부를 raw에 두면 과적재 — 4가지 SKILL.md 패턴(메타-스킬·multi-domain·짧은 단일 파일·블랙박스) 대표 사례만 선별. 마켓플레이스 메타·README·spec 리다이렉트는 표준 진입점이라 보존 필수. 기존 `raw/articles/karpathy-*/` 관례와 일치.
- **생성된 파일 (2개)**
  - **소스 (1)**: `wiki/sources/anthropics-skills.md` — 리포 구조·17개 스킬 4갈래 분류·4개 SKILL.md 사례 분석·SKILL 작성 표준·spec 분리의 의미·document-skills source-available 라이선스의 비즈니스 신호·위키에 직접 응용 가능한 4가지 패턴
  - **개념 (1)**: `wiki/concepts/agent-skills.md` — Agent Skills 정의·3-Level Progressive Disclosure·14개 frontmatter 필드·호출 제어 매트릭스·Skill 저장 위치 우선순위·content lifecycle·description 작성 4룰·description 자동 최적화 루프·Slash Command vs Skill 비교·SKILL.md 패턴 4가지·석근 시나리오 4종(위키·BI·비서·templates/skill.md)·5가지 안티패턴
- **업데이트된 파일**
  - `wiki/entities/claude-code.md` — source_count 5→6, updated 2026-04-16→2026-04-27, tags에 agent-skills·plugin-marketplace 추가, Skills 항목 본문에 progressive disclosure 3-level 명시 + [[agent-skills]] 링크, **Plugin Marketplace 항목 신규** (anthropics-skills 등록 명령·플러그인 3종), 출처에 [[anthropics-skills]] 추가, 관련 개념에 [[agent-skills]] 추가
  - `wiki/index.md` — 통계 47→49 / 소스 18→19 / 개념 12→13. 소스 표·개념 표에 신규 행 추가
- **메모**: 핵심 발견 3가지.
  1. **spec 분리 = 표준 오너십 분리** — Anthropic이 SKILL.md 표준의 단일 운영자가 되는 걸 의도적으로 피한 흔적 (agentskills.io). [[mcp]]가 Anthropic 발이지만 modelcontextprotocol.io에서 운영되는 패턴과 동일.
  2. **document-skills "source-available, not open source"** — xlsx/docx/pptx/pdf는 Claude.ai 문서 생성 production 코드. 라이선스로 fork·재배포 통제. Anthropic의 비즈니스 라인이 어디서 시작되는지 노출.
  3. **skill-creator의 자기참조 구조** — 스킬 작성을 가르치는 스킬이 다시 SKILL.md 형식으로 쓰여 있고, 자기 자신을 평가·개선하는 검증 루프를 본문에서 주도. 이게 [[autonomous-research-loop]] (program.md)와 같은 자기 진화 패턴이지만 **코드가 아닌 지침서를 진화**시킨다는 차이.
- **후속 탐구**:
  1. `~/.claude/skills/wiki/SKILL.md` description을 "pushy" 원칙으로 재작성 + 20개 trigger 검증 쿼리로 trigger rate 측정
  2. 위키에 `templates/skill.md` 추가 검토 (entity/concept/source/synthesis 4종 + skill 1종)
  3. **컴투스플랫폼 BI 스킬** 후보: `bi-query-patterns/SKILL.md` — KPI 조회/코호트/retention 패턴, references에 BigQuery 슬롯 최적화·MMP 데이터 조인
  4. Partner Skills 첫 사례 Notion이 향후 확장 시그널 — 사내 도구 스킬 패키징 가능성

---

## [2026-04-27] ingest | karpathy/nanoGPT + karpathy/nanochat 수집

- **소스 (raw 신규 보관)**:
  - `raw/articles/karpathy-nanogpt/README.md` (13.8KB, 234줄) — `gh api repos/karpathy/nanoGPT/contents/README.md`로 base64 디코드 보관. 라이선스 MIT.
  - `raw/articles/karpathy-nanochat/README.md` (16.5KB, 222줄) — `gh api repos/karpathy/nanochat/contents/README.md`로 보관. 라이선스 MIT.
- **선택 근거**: 기존 `raw/articles/karpathy-autoresearch/` 관례와 일치. 두 저장소 모두 README가 운영 패턴의 본질 — 무거운 Python 코드(`train.py`, `model.py`, `prepare.py` 등) 및 `uv.lock`은 보관 제외.
- **생성된 파일 (4개)**
  - **소스 (2)**:
    - `wiki/sources/karpathy-nanogpt.md` — 2025-11 deprecated 명시, ~300줄 train.py + model.py 디자인, MPS 지원 디테일, 한계 4가지(사전학습만/구식 아키텍처/단일 다이얼 부재/평가 미내장) — 모두 nanochat에서 해결됨
    - `wiki/sources/karpathy-nanochat.md` — $100 GPT-2 풀 파이프라인, 단일 `--depth` 다이얼 디자인, **Time-to-GPT-2 리더보드** 표(행 #5, #6이 autoresearch 라운드 1, 2), AI Policy disclosure 정책
  - **엔티티 (2)**:
    - `wiki/entities/nanogpt.md` (project) — deprecated 상태 마킹, 자손 계보(minGPT → nanoGPT → nanochat → autoresearch), 위키 보존 사유 명시
    - `wiki/entities/nanochat.md` (project) — 활성 주력, 풀 파이프라인 모듈 매핑, 리더보드 표, 정밀도/하드웨어 가이드, AI Policy
- **업데이트된 파일 (3 + 1)**
  - `wiki/entities/karpathy.md` — source_count 1→3, 교육 자산 항목을 자손 계보로 구체화(minGPT → nanoGPT → nanochat → autoresearch), AI Policy 명문화 사실 추가, related에 [[nanogpt]]·[[nanochat]] 추가, 출처 2건 추가
  - `wiki/entities/autoresearch.md` — 부모 저장소 nanochat을 위키링크화([[nanochat]]), **"자기 강화 순환" 섹션 신규 추가** (autoresearch round 1·2가 nanochat 리더보드 #5·#6를 갱신했다는 사실)
  - `wiki/concepts/autonomous-research-loop.md` — source_count 1→2, **"실증: nanochat 리더보드 #5, #6" 섹션 신규** (자율 루프가 사람 SOTA를 갱신한 첫 공개 사례), 출처에 [[karpathy-nanochat]] 추가
  - `wiki/index.md` — 통계 43→47 / 소스 16→18 / 엔티티 12→14. 4개 카테고리 테이블 행 추가/갱신
- **메모**: 핵심 발견은 **autoresearch가 nanochat 리더보드 #4(사람) → #5(자율) → #6(자율)에서 사람 SOTA를 능가하고 그 결과가 부모 저장소로 머지되는 자기 강화 순환을 만든다는 점**. 이로써 [[autonomous-research-loop]] 패턴이 사변적이지 않고 실증된 운영 모델임이 위키에 박힘. 또한 nanoGPT의 deprecated 처리(2025-11)를 위키에 그대로 반영하여 사용자가 잘못된 출발점을 선택하지 않도록 함.
- **후속 탐구**:
  1. autoresearch round 3+ 결과를 정기 추적 → nanochat 페이지 리더보드 표 / autoresearch 페이지 / autonomous-research-loop 페이지 3곳 동기 갱신
  2. minGPT(전신) raw 보관은 보류 — 패턴 계보 시작점이지만 실용성이 nanoGPT보다 낮음
  3. micrograd, llm.c, Zero to Hero 등 Karpathy의 다른 교육 자산은 [[ml-ai]] 페이지 보강용으로 별도 수집 가치 있음
  4. **Karpathy의 두 작업(nanochat ↔ autoresearch)이 자기 강화 순환을 이루는 점**은 별도 종합 분석(`wiki/syntheses/`)으로 정리할 가치 있음 — "사람-자율 루프 협업의 첫 공개 사례"라는 큰 그림으로

---

## [2026-04-27] ingest | karpathy/autoresearch 수집

- **소스 (raw 신규 보관)**: `raw/articles/karpathy-autoresearch/README.md` (8.0KB) + `raw/articles/karpathy-autoresearch/program.md` (7.0KB) — `gh api repos/karpathy/autoresearch/contents/...` 로 base64 디코드해 그대로 복사. 라이선스 MIT.
- **선택 근거**: GitHub 프로젝트의 공식 문서라서 `raw/articles/`에 두는 게 기존 `raw/articles/claude-code/` 관례와 일치. 무거운 파이썬 코드(`prepare.py` 15KB, `train.py` 26KB, `uv.lock` 443KB)와 `progress.png`는 raw에 두지 않음 — 위키는 운영 패턴이 본질이므로 마크다운 2개로 충분.
- **생성된 파일 (4개)**
  - **소스 (1)**: `wiki/sources/karpathy-autoresearch.md` — 5분 시간 예산 / `val_bpb` 단일 메트릭 / `train.py` 단일 파일 수정 / `program.md` = "lightweight skill" / NEVER STOP 원칙 정리
  - **엔티티 (2)**: `wiki/entities/karpathy.md` (person — OpenAI 창립 멤버, Tesla AI 디렉터 출신, 교육 자산 nanoGPT/micrograd/llm.c/Zero to Hero 보유) · `wiki/entities/autoresearch.md` (project — 76,912 stars, MIT, 4개 포크 macos/mlx/win-rtx/amd 노출)
  - **개념 (1)**: `wiki/concepts/autonomous-research-loop.md` — 4중 제약(단일 메트릭·고정 시간 예산·단일 파일·무한 루프) / 5단계 루프 골격 / 컨텍스트 보호 3원칙 / 석근 응용 시나리오 3종(BI 쿼리 자율 튜닝, 비서 AI prompt 진화, 위키 운영 — 위키는 메트릭 부재로 직접 적용 불가)
- **업데이트된 파일**
  - `wiki/concepts/harness.md` — source_count 1→2, "극한 사례: autoresearch의 초경량 하네스" 섹션 추가, related에 [[autoresearch]]·[[autonomous-research-loop]] 추가
  - `wiki/concepts/context-engineering.md` — source_count 1→2, "자율 루프 컨텍스트 보호 3원칙" 섹션 추가 (`> run.log 2>&1` + `grep` 1줄 발췌 + 크래시 시에만 tail), 출처에 [[karpathy-autoresearch]] 추가
  - `wiki/index.md` — 통계 39→43 / 소스 15→16 / 엔티티 10→12 / 개념 11→12. 4개 카테고리 테이블에 행 추가, harness/context-engineering 행 갱신.
- **메모**: 이번 수집의 진짜 가치는 [[autonomous-research-loop]]를 위키의 새 지층으로 자리잡힌 것. **"단일 메트릭 + 시간 예산 + 단일 파일 + 무한 루프"** 4중 제약은 [[harness]] 개념을 극한으로 압축한 형태이며, 석근의 BI 자동화·개인 비서 AI 양쪽에 직접 이식 후보. 위키 자체는 메트릭 정의가 어려워 자율 루프 적용 전에 평가축을 먼저 정의해야 함을 본문에 명시.
- **후속 탐구**:
  1. macOS / MLX 포크 1종을 회사 맥북에서 실제 가동 → 1박 ~100실험 재현해보기
  2. nanochat 본 저장소 raw 보관 여부 결정 (별도 가치 검증 후)
  3. 위키 운영용 메트릭 후보(고정 질의 세트 정답률, 토큰/질의)를 3개월 운영하며 검증

---

## [2026-04-24] ingest | portfolio 커리어 자료 베이스 통합 수집

- **소스 (raw 신규 복사, 공개 자료만)**:
  - `raw/notes/portfolio/README.md` — portfolio 저장소 README
  - `raw/notes/portfolio/old-portfolio.md` — 시드 포트폴리오(22KB)
  - `raw/notes/portfolio/docs/**` — 3-Layer + Johnny.Decimal 구조 문서 미러 (총 47개 파일)
- **민감 자료 제외**: portfolio/private/ (Jira 22 + Confluence 10 + Google Drive 3)는 공개 GitHub 원격(`gsroot/llm-wiki`) 누출 방지를 위해 복사 제외. portfolio 저장소의 로컬 전용 폴더에만 보존.
- **수집 전략**: 계층적 — 개별 Jira/Confluence dump마다 source 페이지를 만들지 않고, 핵심 산출물(이력서·상세 포트폴리오·시드)과 프로젝트 통합 문서만 source 페이지로 요약. 세부 증거는 portfolio 내 `20-projects/*.md`의 `sources:` 필드에서 역추적 가능.
- **생성된 파일** (총 19개)
  - **소스 (8)**: `wiki/sources/portfolio-seed.md` · `portfolio-resume-ko.md` · `portfolio-ko.md` · `portfolio-method.md` · `c2spf-nft-market.md` · `c2spf-xpla-platform.md` · `c2spf-analytics-common.md` · `c2spf-analytics-renewal.md`
  - **엔티티 (4)**: `wiki/entities/seokgeun-kim.md` (위키 소유자) · `com2us-platform.md` (현 재직사) · `c2spf-analytics.md` (BI 서비스) · `xpla-platform.md` (블록체인 플랫폼)
  - **개념 (6)**: `wiki/concepts/backend-python-fastapi.md` · `frontend-react.md` · `data-pipeline-bigquery.md` · `devops-cicd.md` · `blockchain-xpla.md` · `ml-ai.md`
  - **종합 분석 (1)**: `wiki/syntheses/career-timeline-seokgeun.md` — 2016~2026 9년 커리어 타임라인, 4 패턴(역할 진화/스택 누적/정량 지표/회사+개인) 분석
- **업데이트된 파일**
  - `wiki/index.md` — 총 페이지 20→39, 소스 7→15, 엔티티 6→10, 개념 5→11, 종합 분석 1→2. 4개 카테고리 테이블에 19행 추가.
- **메모**: portfolio 저장소(3-Layer + Johnny.Decimal)와 llm-wiki(raw → sources → syntheses)는 같은 "원천 → 요약 → 종합" 패턴을 공유하므로 통합이 자연스러웠음. 향후 portfolio가 갱신되면 같은 source 페이지를 업데이트하는 방식으로 동기화 가능. 본 수집으로 LLM이 "내 커리어/프로젝트/스킬" 질의에 portfolio 저장소까지 가지 않고도 wiki 내에서 답변 생성 가능.

---

## [2026-04-16] ingest | Slash Commands vs Agent Skills 조사 수집 + RAG 가이드 재수집

- **소스 1 (신규)**: `raw/notes/slash-commands-vs-agent-skills.md` — 공식 문서(code.claude.com/docs/en/skills) 기반 조사·분석
- **소스 2 (업데이트)**: `raw/notes/using-llm-wiki-as-rag.md` — 방법 4를 "Slash Command"에서 "Agent Skill"로 승격, 새 소스 참조 추가
- **생성된 파일**:
  - `wiki/sources/slash-commands-vs-agent-skills.md` — 통합 경위, 기능 비교표, 위키 조회에 Skill이 유리한 4가지, frontmatter 핵심 필드, 호출 제어 매트릭스, 동적 context injection
- **업데이트된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 방법 4 전체 재작성(Agent Skill), 선택 매트릭스·인사이트·관련 링크 갱신
  - `wiki/entities/claude-code.md` — source_count 4→5, Skills 설명 보강(통합 경위·자동 호출·context:fork·paths·agentskills.io 표준), 출처 2건 추가
  - `wiki/index.md` — 총 페이지 19→20, 소스 6→7
- **raw/ 수정 참고**: `using-llm-wiki-as-rag.md`는 석근 본인+Claude 세션이 원저자인 메모이므로 업데이트를 허용. 외부 클리핑이었으면 불변 원칙 적용.
- **핵심 판단**: "어떤 도구든 Skills로 시작한다. 예외는 기존 commands 자산이 많아 이관 비용이 큰 경우뿐" — 이것이 이 조사의 결론이자 위키 전체의 새 운영 원칙

---

## [2026-04-16] setup | `wiki` Agent Skill 생성 (방법 4 구현)

- **작업**: [[using-llm-wiki-as-rag]]의 "방법 4"로 제안됐던 slash command를 **Agent Skill**로 승격하여 구현
- **생성된 파일**: `~/.claude/skills/wiki/SKILL.md` (Personal scope — 모든 프로젝트에서 자동 사용)
- **설계 결정**:
  - **Slash command가 아니라 Skill 선택**: 공식 문서 확인 결과 "Custom commands have been merged into skills"로 통합됐고 Skills가 권장됨. 자동 호출·supporting files·context:fork·paths 제한 등 Skill 전용 기능이 위키 조회에 특히 유용
  - **광범위한 description**: 초기 안은 "AI/LLM 질문"으로 좁혔으나, 개인 위키는 BI·업무·학습·독서·사이드 프로젝트 등 모든 주제로 확장될 예정이므로 description에 전 카테고리 열거
  - **"빈 조회" 방지 로직**: SKILL.md 1단계에서 `index.md` Read 후 관련 페이지 없으면 즉시 종료. Claude가 자동 호출해도 토큰 낭비 최소
  - **`context: fork` + `agent: Explore`**: 조회를 서브에이전트로 격리해 메인 세션 컨텍스트 오염 방지. [[harness]] 원칙 중 세션 분리 적용
  - **Personal scope 선택**: `~/.claude/skills/wiki/`에 두어 회사·개인 프로젝트 구분 없이 작동
- **업데이트된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 후속 과제 중 방법 4 완료 표시
- **의미**: 이 위키가 Claude Code의 네이티브 retrieval 경로로 **제품화**된 시점. 이제 어느 프로젝트에서든 `claude` 실행 후 관련 질문이 들어오면 자동으로 이 위키가 참조됨
- **후속 과제**:
  - 실사용하며 자동 호출의 정확도 관찰 → description 조정 여부 판정
  - 패턴이 쌓이면 `~/.claude/skills/wiki/query-patterns.md` supporting file 추가 검토
  - `context: fork` 비용이 과하다 싶으면 inline 모드로 전환 실험

---

## [2026-04-15] ingest | 이 위키를 Claude Code에서 RAG처럼 쓰는 법 (자기참조)

- **소스**: `raw/notes/using-llm-wiki-as-rag.md` (석근이 Claude Code 세션 대화 답변을 본인이 수집 대상으로 지정)
- **성격**: 자기참조적 수집 — 위키 운영 메타 문서. 이 위키의 활용법이 위키 자체의 한 페이지가 됨.
- **생성된 파일**:
  - `wiki/sources/using-llm-wiki-as-rag.md` — 5가지 통합 방법(디렉토리 실행 / 프로젝트 참조 / 명시적 로드 / slash command / MCP) + 선택 매트릭스
- **업데이트된 파일**:
  - `wiki/concepts/llm-wiki-pattern.md` — source_count 2→3, "RAG처럼 활용하기 (5단계)" 섹션 추가
  - `wiki/entities/claude-code.md` — source_count 3→4, 출처에 사용 가이드 추가
  - `wiki/concepts/mcp.md` — source_count 3→4, `.mcp.json` 예시 소스로 사용 가이드 추가
  - `wiki/index.md` — 총 페이지 18→19, 소스 5→6
- **후속 과제**:
  - 방법 4 구현: `~/.claude/commands/wiki.md` 실제 생성 (비용 대비 이득이 큼)
  - 방법 2 지원: 회사 프로젝트 CLAUDE.md 템플릿에 "참조 지식 베이스" 섹션 추가
  - qmd 도입 트리거 기준: 페이지 50개 또는 "index.md 읽는 데 5초 이상"
- **메모**: 수집하면서 확인된 것 — 이 위키는 이미 RAG 역할을 하고 있고, 18페이지 규모에서는 벡터 검색보다 index.md + Read가 오히려 빠르고 정확함. MCP 도입은 성급하지 않게.

---

## [2026-04-15] ingest | Obsidian 사용 가이드 수집

- **소스**: `raw/notes/OBSIDIAN_GUIDE.md` (석근 개인 정리, 21개 섹션)
- **작업**: Notion 사용자 관점 Obsidian 실무 입문 가이드 수집. 이 위키 자체가 Obsidian vault로 운영되고 있으므로 구조적으로 중요.
- **생성된 파일**:
  - `wiki/sources/obsidian-guide.md` — 21개 섹션 요약 (설치, 링크, Properties/Tags/Links 구분, 검색, 템플릿, Canvas/Bases, Sync, 실무 운영 규칙)
  - `wiki/entities/obsidian.md` — Obsidian 본체 엔티티 (그동안 누락됐던 핵심 엔티티)
- **업데이트된 파일**:
  - `wiki/entities/obsidian-web-clipper.md` — 관련 엔티티에 `[[obsidian]]` 추가 (확장이 본체 vault에 저장한다는 관계 명시)
  - `wiki/concepts/llm-wiki-pattern.md` — "Obsidian" 언급을 `[[obsidian]]` 위키링크로 승격
  - `wiki/index.md` — 총 페이지 16→18 (소스 4→5, 엔티티 5→6)
- **메모**: 이 가이드의 원칙("작고 일관된 규칙을 오래 지킨 사람"이 잘 쓴다, Properties/Tags/Links 역할 분리)이 이 위키 설계와 정확히 일치. 사실상 이 위키 설계의 개인적 배경 문서.
- **후속 탐구**: Bases 기능을 도입하면 `wiki/index.md`의 정적 테이블을 frontmatter 기반 동적 쿼리로 전환 가능. 현재 유지보수 비용 대비 이득이 크면 검토 가치 있음.

---

## [2026-04-15] ingest | 클로드 코드 중심 실전 마스터 가이드 수집

- **소스**: `raw/articles/claude-code/클로드코드_가이드북.pdf` (CHOI, 848페이지, 82.7MB)
- **변환 도구**: [opendataloader-pdf](https://github.com/opendataloader-project/opendataloader-pdf) (Python 래퍼, Java JAR 기반)
  - 명령: `opendataloader-pdf -f markdown --image-output off -q -o /tmp/claude-guidebook-md/ ...`
  - 출력: 15,148줄 / 934KB 마크다운 (이미지 제외)
  - 변환 출력물은 raw/ 원칙 준수를 위해 프로젝트 외부 `/tmp/`에 보관하고 위키에는 요약만 반영
- **생성된 파일**:
  - `wiki/sources/claude-code-master-guide.md` — 12장 구조 요약, 핵심 개념, 운영 인사이트
  - `wiki/entities/cowork.md` — Anthropic Cowork (비개발 지식 업무용 자매 작업 경로)
  - `wiki/concepts/harness.md` — 이 책의 중심 개념. AI 에이전트 작업장 전체 구조
  - `wiki/concepts/token-economy.md` — 토큰 경제학 (비용 단위 + 작업 범위 신호)
  - `wiki/concepts/context-engineering.md` — 프롬프트/컨텍스트/하네스 엔지니어링 3층 구분
- **업데이트된 파일**:
  - `wiki/entities/claude-code.md` — source_count 2→3, 운영 보강 섹션(허용/질문/차단, scope 우선순위, 세션 재개, Worktree) 추가, 관련 개념에 harness/cowork/token-economy/context-engineering 연결
  - `wiki/concepts/mcp.md` — source_count 2→3, "MCP → Skill → Plugin" 사용 순서와 managed 설정 추가
  - `wiki/concepts/llm-wiki-pattern.md` — source_count 1→2, 이 위키를 하네스 관점으로 재해석하는 섹션 추가
  - `wiki/index.md` — 총 페이지 11→16 (소스 3→4, 엔티티 4→5, 개념 2→5)
- **변환 품질 메모**: 한국어 단어가 줄바꿈에서 잘리는 경우 있음(예: "어받기(Channels)", "classier"). `--use-struct-tree` 옵션을 향후 시도해볼 가치 있음. 표 구조 일부 깨짐.
- **교차 참고**: 석근님이 별도로 만든 `/Users/sgkim/Downloads/클로드코드 가이드북.md` 요약(전반부 1~6장 중심)과 교차 확인. 본 수집은 opendataloader-pdf 변환본(15,148줄)을 1차 소스로 하여 후반부 7~11장까지 포함.
- **메모**: 이 위키가 이미 적용 중인 운영 원칙(CLAUDE.md·index.md·log.md·templates·handoff)이 가이드북의 "기본 파일 8종"과 "4층 하네스 레이어"에 정확히 대응함을 확인. 즉 이 위키는 [[harness]] 개념의 개인 지식 관리용 구현체.

---

## [2026-04-15] ingest | Claude Code 빠른 시작 수집

- **소스**: `raw/articles/claude-code/빠른 시작.md`
- **작업**: Anthropic 공식 빠른 시작 가이드 클리핑 수집
- **생성된 파일**:
  - `wiki/sources/claude-code-quickstart.md` — 소스 요약 (8단계 온보딩, CLI 명령표, 프롬프팅 팁)
- **업데이트된 파일**:
  - `wiki/entities/claude-code.md` — source_count 1→2, 필수 CLI 명령표·단축키·프롬프팅 원칙 섹션 추가, 출처 추가
  - `wiki/index.md` — 총 페이지 수 10→11, 소스 2→3, Claude Code 엔티티 소스 수·수정일 갱신
- **메모**: [[claude-code-overview]]와 주제는 겹치나, 이 문서는 실전 온보딩(설치→로그인→첫 세션→Git)과 CLI 플래그 레퍼런스(`-p`, `-c`, `-r`) 중심. 개요 페이지와 역할이 분명히 다르므로 별도 소스로 보존. 새 엔티티·개념 페이지는 생성하지 않고 기존 [[claude-code]] 엔티티를 보강.

---

## [2026-04-09] ingest | Claude Code 개요 수집

- **소스**: `raw/articles/Claude Code 개요.md`
- **작업**: Anthropic 공식 문서 클리핑 수집
- **생성된 파일**:
  - `wiki/sources/claude-code-overview.md` — 소스 요약
  - `wiki/entities/claude-code.md` — Claude Code 엔티티 페이지
- **업데이트된 파일**:
  - `wiki/concepts/mcp.md` — source_count 1→2, Claude Code의 MCP 활용 범위 추가, 출처 추가
  - `wiki/index.md` — 총 페이지 수 8→10, 새 페이지 2건 등록
- **메모**: 이 위키를 운영하는 도구 자체에 대한 문서. CLAUDE.md, MCP, Skills, Hooks 등 위키 운영과 직결되는 기능이 다수 포함됨.

---

## [2026-04-09] ingest | LLM 위키 아이디어 문서 수집

- **소스**: `raw/notes/llm_wiki.md`
- **작업**: 첫 번째 정식 수집(Ingest) 워크플로우 실행
- **생성된 파일**:
  - `wiki/sources/llm-wiki-idea-doc.md` — 소스 요약 페이지
  - `wiki/entities/memex.md` — 바네바 부시의 메멕스 (1945)
  - `wiki/entities/qmd.md` — 마크다운 검색 엔진
  - `wiki/entities/obsidian-web-clipper.md` — 웹 클리핑 도구
  - `wiki/concepts/mcp.md` — Model Context Protocol 개념
- **업데이트된 파일**:
  - `wiki/concepts/llm-wiki-pattern.md` — 역자 주석의 실전 팁 반영 (소스 수집 경로, RAG 보완 관계, 세션 간 컨텍스트, 관련 엔티티 링크 추가)
  - `wiki/syntheses/wiki-bootstrap-log.md` — 소스 참조 추가, 다음 단계 진행 상태 갱신
  - `wiki/index.md` — 총 페이지 수 2→8, 새 페이지 6건 등록
- **메모**: 원문(패턴 설명) + 역자 주석(실전 가이드 10개 항목) 구조. 이 문서가 현재 위키의 CLAUDE.md 설계의 직접적 기반이었으므로, 부트스트랩 시 이미 반영된 내용과 새로 추가된 실전 팁을 구분하여 수집.

---

## [2026-04-09] init | 위키 부트스트랩

- **작업**: LLM 위키 초기 구조 생성
- **생성된 파일**:
  - `CLAUDE.md` — 스키마 (운영 규칙 및 워크플로우)
  - `templates/` — 소스, 엔티티, 개념, 종합 분석 템플릿 4종
  - `wiki/index.md` — 위키 카탈로그
  - `wiki/logs/log.md` — 이 로그 파일
  - `wiki/concepts/llm-wiki-pattern.md` — 첫 번째 개념 페이지
  - `wiki/syntheses/wiki-bootstrap-log.md` — 부트스트랩 기록
- **메모**: "LLM 위키" 아이디어 문서를 기반으로 개인 종합 위키 초기 구축. Obsidian 볼트로 사용할 수 있도록 디렉토리 구조와 스키마를 설계함. Claude Code와 Cowork 양쪽에서 운영 가능하도록 설계.
