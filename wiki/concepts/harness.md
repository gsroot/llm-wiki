---
title: 하네스 (Harness)
type: concept
category: ai
aliases:
- Agent Harness
- harness
- 에이전트 하네스
- claude harness
- AI 하네스
tags:
- harness
- claude-code
- agent
- 자율연구
- agent-skills
- 패키지레이어
- claude-agent-SDK
- agent-patterns
- bare-metal-harness
- spec-kit
- sdd
- scikit-learn
- slep
- openai
- openai-cookbook
- openai-agents-python
- plans-md
- exec-plans
- 9-sop-skills
- skill-chaining
related:
- '[[claude-code]]'
- '[[claude-agent-sdk]]'
- '[[anthropic]]'
- '[[agent-patterns]]'
- '[[context-engineering]]'
- '[[token-economy]]'
- '[[llm-wiki-pattern]]'
- '[[autonomous-research-loop]]'
- '[[autoresearch]]'
- '[[agent-skills]]'
- '[[spec-kit]]'
- '[[spec-driven-development]]'
- '[[github]]'
- '[[scikit-learn]]'
- '[[openai]]'
- '[[openai-cookbook]]'
- '[[openai-agents-python]]'
- '[[mcp]]'
- '[[seokgeun-kim]]'
- '[[portfolio]]'
- '[[c2spf-analytics]]'
- '[[seokgeun-stack-guide]]'
- '[[matechat]]'
- '[[llm-infra-meta-cluster]]'
- '[[claude-code-master-guide]]'
- '[[karpathy-autoresearch]]'
- '[[anthropics-skills]]'
- '[[anthropics-claude-cookbooks]]'
- '[[github-spec-kit]]'
- '[[openai-openai-cookbook]]'
- '[[flutter-flutter]]'
- '[[openai-openai-agents-python]]'
source_count: 8
observed_source_refs: 58
inbound_count: 187
created: 2026-04-15
updated: 2026-04-29
cited_by_count: 67
---

# 하네스 (Harness)

> 한국어 표기: **에이전트 하네스** 또는 **AI 하네스**(Agent Harness).

> [!tldr]
> **Harness** = LLM 모델 위에 얹어 컨텍스트·도구·검증·작업 흐름을 관리하는 **운영 외피층**. 모델은 능력을, 하네스는 능력을 작업으로 변환하는 거버넌스.
> - **판단**: 살아있는 운영 노트(OpenAI Cookbook 패턴) vs 정적 가이드(Anthropic Skills 패턴) / meta-harness vs library-as-harness
> - **근거**: Claude Code·Cursor·Codex의 harness 비교 / 7-hour task 벤치마크 / 석근 운영 사례 (39 SKILL · MateChat 자작)
> - **히스토리**: 2024 Custom Commands → 2026 Skills+MCP+Subagents 메타 운영 표준화
> - **이 위키 맥락**: 5축(LLM 인프라 메타) sub-hub 2위 (inbound 178). 본문 4단 표는 TL;DR 섹션 참조.

## TL;DR (요약·판단·근거·히스토리 4단)

| 단 | 내용 | 본문 위치 |
|---|---|---|
| **요약** | AI 에이전트 작업장 전체 구조. 프롬프트 한 줄이 아니라 읽을 자료·도구·중지 조건을 묶어둔 운영 환경. | 정의 / 왜 중요한가 |
| **판단** | 4층 레이어 (모델 / 프롬프트+컨텍스트 / 하네스 / 검증) / 양극 스펙트럼 (autoresearch 초경량 vs spec-kit 풀패키지) / 회사·사이드 적용 분기 | 4층 레이어 / 하네스 스펙트럼 / 실전 적용 |
| **근거** | 하네스 vs 프롬프트/컨텍스트 엔지니어링 차이 / autoresearch·spec-kit·scikit-learn·flutter·PLANS.md 5축 거버넌스 비교 / Anthropic 자기 정의 (claude-cookbooks 인용) | 하네스 vs 프롬프트... / 극한 사례 1 / Anthropic의 자기 정의 |
| **히스토리** | 모델 경쟁 → 작업 구조·하네스·검증 습관 경쟁으로 이동 / 하네스 엔지니어링이 새 직무로 부상 / MateChat 39 SKILL이 하네스 사례 | 관련 개념 / 출처 / 열린 질문 |

이 4단 분리는 Codex 평가 P1 권고("장문 hub의 히스토리 노이즈 분리")에 따른 navigation aid.

## 정의

AI 에이전트가 일하는 **작업장 전체 구조**. 프롬프트 한 줄이 아니라, 에이전트가 무엇을 읽고 어떤 도구를 쓰고 어디서 멈춰야 하는지를 묶어 놓은 운영 환경이다.

> 비유: "동료에게 일을 맡길 때 책상 위에 참고 자료를 놓고, 출입 가능한 서랍을 정하고, 끝나기 전에 체크할 항목을 붙여 두는 것."

## 왜 중요한가

**모델 이름보다 작업 구조·하네스·검증 습관에서 차이가 벌어진다.** 같은 Claude를 쓰더라도 하네스가 있는 팀과 없는 팀의 산출물 품질은 크게 달라진다.

AI 성능 경쟁이 "어느 모델이 더 똑똑한가"에서 "어느 도구가 실제 일을 덜 끊기게 하는가"로 이동했고, 이 질문의 답이 하네스 설계다.

본 위키에서 하네스는 [[agent-skills]], [[mcp]], [[claude-code]]와 함께 LLM 협업 운영의 메타 클러스터를 만든다. 네 축의 관계와 OSS 거버넌스 모델은 [[llm-infra-meta-cluster|LLM 인프라 메타 5축]]에서 종합한다.

## 핵심 구성 요소

| 요소 | 역할 |
|------|------|
| **권한 모드 (Permission Modes)** | 무엇을 자동 허용, 질문, 차단할지 |
| **자동 개입 규칙 (Hooks)** | 세션 중간에 자동으로 끼어드는 검사·후처리 |
| **폴더 구조 (File Organization)** | 어떤 파일이 어디에 놓이고 언제 읽히는가 |
| **테스트와 검증 (Testing & Verification)** | 출력이 의도대로인지 확인하는 루프 |
| **저장 위치 지정 (Save Locations)** | 결과물·로그·handoff가 어디에 남는가 |

## 4층 레이어로 본 하네스

[[claude-code-master-guide]]의 분류:

1. **지식 레이어**: CLAUDE.md, 규칙 파일, 메모리, 예시, 스킬 지침
2. **도구 레이어**: Bash, Read/Edit/Write, MCP, Connector, 브라우저 제어, 예약 실행
3. **패키지 레이어**: Skills, Plugins → 단일 표준 구현은 [[agent-skills]] 참조 (SKILL.md + scripts·references·assets)
4. **통제 레이어**: Permissions, Hooks, 승인 단계, Plan Mode, Worktree, 테스트, 검토 에이전트

### 패키지 레이어 상세 (Anthropic anthropics/skills 사례 기준)

[[anthropics-skills]] 마켓플레이스가 패키지 레이어의 운영 사례를 노출:

- **3-Level Progressive Disclosure**: Metadata 100w 상시 / SKILL.md body <500lines / scripts·references·assets 필요 시만
- **자동 호출**: description 기반으로 LLM이 스스로 트리거 결정 → 패키지 레이어가 사용자 호출에 의존하지 않게 됨
- **`context: fork`**: 서브에이전트 격리 → 패키지가 메인 컨텍스트를 오염시키지 않음
- **`paths`**: 자동 호출 조건을 glob으로 제한 → 패키지가 다른 작업을 방해하지 않음

이 4가지 메커니즘이 패키지 레이어를 "단순 명령 묶음"에서 "지능형 작업장 모듈"로 격상시킴.

## 하네스 엔지니어링 vs 프롬프트/컨텍스트 엔지니어링

| 엔지니어링 종류 | 조작 대상 |
|----------------|----------|
| 프롬프트 엔지니어링 | 한 번의 입력 문장 |
| [[context-engineering]] | 컨텍스트 윈도우에 들어가는 자료 구성 |
| **하네스 엔지니어링** | 에이전트가 일하는 작업장 전체 (컨텍스트·도구·권한·검증·저장) |

가이드북 5장의 핵심 주장: **프롬프트 → 컨텍스트 → 하네스** 순으로 추상화 수준이 올라가고, 하네스 수준의 설계가 장기적 효용을 만든다.

## 실전 적용

### 최소 하네스 (개인 사용자용)
```
project/
├── CLAUDE.md          # 프로젝트 계약서 (짧게)
├── about-me.md        # 배경 맥락
├── working-rules.md   # 작업 규칙
├── plan.md            # 현재 작업 상태
├── handoff.md         # 다음 세션용 인수인계
└── templates/*.md     # 출력 형식
```

### 팀 하네스 추가 요소
- `decision-log.md`, `approval-log.md`, `review-findings.md` — 사후 흔적
- `.claude/settings.json`의 managed scope — 관리자 강제 설정
- Hooks로 포맷팅·린트·승인 자동 삽입
- Worktree로 역할별 병렬 세션 분리

### 하네스 품질 체크리스트
- CLAUDE.md가 짧고 강한 운영 계약서인가
- plan / implement / review가 분리되어 있는가
- 긴 세션에 compaction·session memory·handoff 파일이 함께 있는가
- 고위험 작업에 approval gate가 앞단에 있는가
- 세션이 끊겨도 바깥 파일로 상태 복원이 가능한가

## 하네스 스펙트럼 — 양극 사례

[[harness]]는 "최소화 ↔ 완전 표준화"의 스펙트럼 위에 놓인다. 위키에 등록된 두 극단:

| 축 | 최소 극단 | 표준화 극단 |
|----|---------|------------|
| **사례** | [[autoresearch]] (Karpathy) | [[spec-kit]] (GitHub) |
| **지식** | `program.md` 한 장 (~7KB) | `constitution.md` (9 Articles) + `spec.md` + `plan.md` + 5 템플릿 |
| **도구** | bash, python, git만 | bash, git, GitHub CLI, MCP, 30+ 에이전트 통합 |
| **패키지** | 없음 | 9 슬래시 명령 (또는 Codex SKILL.md 9 패키지) |
| **통제** | "5분 시간 예산 + `val_bpb` 단일 메트릭 + Simplicity" 세 줄 | Phase -1 Gates, `[NEEDS CLARIFICATION]` 마커, Constitutional Compliance, TDD Red 단계 강제 |
| **세계관** | **메트릭 객관성**이 자유도를 견딘다 | **메소드론 강제**가 산출물 품질을 보장한다 |
| **장점** | 빠른 0→1, 창의적 탐색, 적은 오버헤드 | 일관성, 추적성, 다중 spec 누적 가능 |
| **단점** | 도메인 외에서 재현 어려움, 메트릭 의존 | 5분 prototype에는 과잉, 학습 곡선 |

[[spec-driven-development]]는 spec-kit가 강제하는 메소드론 자체의 페이지. 양극 사이의 "어떤 작업에 어느 쪽이 ROI인가"는 [[spec-driven-development]]의 열린 질문.

### 제3의 축 — "라이브러리 자체가 하네스"

위 양극은 **에이전트의 작업 환경**을 최소화하거나 표준화한다. [[scikit-learn]]은 다른 차원의 사례 — **라이브러리 디자인 자체가 작업 운영 패턴**:

| 축 | scikit-learn (library-as-harness) |
|----|----------------------------------|
| **지식** | 5가지 API 컨트랙트(`fit`/`predict`/`transform`/`Pipeline`/Meta-estimator) — 19년간 변하지 않은 추상화가 곧 "작업 모양" |
| **도구** | NumPy + SciPy + joblib + threadpoolctl 5개 의존성 — 최소 도구 셋이 학습/예측 모든 작업에 충분 |
| **패키지** | scikit-learn-contrib + skops + sklearn-onnx + auto-sklearn + MLFlow + yellowbrick 등 30+ 호환 라이브러리 — sklearn 컨트랙트 따르면 자동 호환 |
| **통제** | **SLEP** (Scikit-Learn Enhancement Proposal) — API 변경에 1주+ 토론 + 2/3 다수결 강제, `pytest sklearn` 공통 테스트 헬퍼가 컨트랙트 위반 자동 검출 |
| **세계관** | **API 컨트랙트가 곧 협업 표준**, 라이브러리 자체가 외부 컴포넌트의 협업 하네스 |

→ [[autoresearch]]가 "에이전트의 자유도", [[spec-kit]]가 "메소드론 강제", [[scikit-learn]]은 "API 컨트랙트의 영구성"으로 각자 다른 강제 메커니즘. 회사 BI 모델 운영에는 sklearn 모델이 곧 작은 하네스 — `model_persistence.rst` 5단 의사결정 트리가 그대로 운영 SOP가 됨.

### 제4의 축 — "vendor-neutral 자산 + 토큰 예산 다층화"

[[flutter]] (Google, ★176K 11년차 OSS)가 박은 또 다른 변종:

| 축 | flutter/flutter (vendor-neutral asset) |
|----|---------------------------------------|
| **지식** | `.agents/rules/dart-editing.md` (always_on trigger) + `.agents/skills/README.md` (5개 채택 요건 + agentskills.io 표준 인용) + `docs/about/Values.md` (5 가치) |
| **도구** | `dart_skills_lint` 자체 검증 도구, dart format/analyze, MCP 서버, `dart_format` MCP |
| **패키지** | `.agents/skills/{find-release, rebuilding-flutter-tool, upgrade-browser}/SKILL.md` 3종 + scripts/ ([[agent-skills]] 표준) |
| **통제** | (1) **vendor-neutral 위치**(`.agents/`)를 단일 원천, `.claude/skills` → `../.agents/skills` 심볼릭 링크로 멀티 벤더 forwarding, (2) **토큰 예산 4계층** rules.md(30K) → 10k → 4k → 1k 동일 룰을 도구 한계별로 자동 매칭, (3) `agent-artifacts/` 별도 디렉토리 + .gitignore로 AI 산출물 격리 |
| **세계관** | **표준은 채택하되 위치 컨벤션은 자체 결정** — agent-skills 표준의 형식을 따르면서 위치는 vendor-neutral, 토큰 예산은 도구별 대응 |

→ [[anthropics-skills]] 진영의 `.claude/skills/` (자기 도구 중심)와 정면 다른 모델. **표준 채택자가 표준 정의자의 위치 컨벤션을 누르고 자체 결정**. [[github-spec-kit]] Codex 모드의 `.codex/skills/` (벤더별 분산 설치)와도 다름.

특히 `docs/rules/` 4계층(rules_1k 799B → 4k 3.5K → 10k 9.4K → full 30K)이 **AI 도구 시장 매트릭스** (Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K)에 자동 매칭하는 패턴은 [[anthropics-skills]] [[progressive-disclosure|progressive disclosure]] 3계층의 도구별 변종. 거대 OSS가 다중 AI 도구 환경에서 운영하는 첫 사례.

### 제5의 축 — "PLANS.md / ExecPlans = 7시간+ 단일 작업 living document"

[[openai-cookbook]] (★73K 4년차)이 박은 또 다른 거버넌스 변종:

| 축 | openai-cookbook (PLANS.md / ExecPlans) |
|----|----------------------------------------|
| **지식** | `articles/codex_exec_plans.md` (16KB)에서 메타-규칙 정의 + `.agent/PLANS.md` 본체 (각 프로젝트 자체) |
| **도구** | Codex CLI / `gpt-5.2-codex` 모델 + `python .github/scripts/check_notebooks.py` |
| **패키지** | `AGENTS.md` 한 줄 (`When writing complex features, use an ExecPlan from .agent/PLANS.md`)이 자동 호출 트리거 |
| **통제** | NON-NEGOTIABLE 5 요건: ① 자기완결 ② **살아있는 문서** ③ 초보자 구현 가능 ④ **관찰 가능한 동작** 결과물 ⑤ 모든 용어 본문 정의. 단일 fenced code block 강제, 산문 우선 |
| **세계관** | **단일 LLM 작업 7시간+** 가능성이 차별 지표 — "기존 LLM이 완료 못 하던 규모"의 직접적 답 |

→ [[github-spec-kit]] Constitution은 명세 → 구현 분리, [[anthropics-skills]] SKILL.md는 자동 호출 트리거 분리, [[scikit-learn]] SLEP는 표준 변경 분리, [[flutter]] `docs/rules/`는 토큰 예산 분리. **PLANS.md는 명세 + 진행 + 학습을 단일 파일에 합쳐 living document로 운영**.

추가로 [[openai-cookbook]] `AGENTS.md` (5.5KB)의 `Recent Learnings` 섹션은 운영 중 발견된 함정·솔루션을 누적하는 **살아있는 운영 노트** — 다른 OSS의 정적 가이드(astral-sh/uv, scikit-learn, fastapi 등)와 본질적으로 다름. 6개 항목 형식: "현상 → 대응 → 이유". `agent-skills` 외부 채택 7단계 진화의 7번째이자 첫 살아있는 사례 (자세한 도식은 [[agent-skills]] 출처 섹션).

5축 비교 요약:

| 축 | 거버넌스 단위 | 시간 단위 | 산출물 | 변경 비용 |
|---|---|---|---|---|
| autoresearch (Karpathy) | 자율 메트릭 게임 | 분~시간 | `program.md` 단일 파일 | 즉시 |
| spec-kit (GitHub) | 다중 에이전트 표준화 | 시간~일 | Constitution + 9 슬래시 명령 | 중간 |
| scikit-learn (커뮤니티) | API 컨트랙트 영구성 | 19년 | SLEP 공식 문서 | 매우 높음 |
| flutter (Google) | 다중 도구 토큰 매트릭스 | 11년 | rules-1k/4k/10k/full 4계층 | 높음 |
| **openai-cookbook PLANS.md** | **단일 LLM 7시간+ 작업** | **시간~하루** | **자기완결 living document + AGENTS.md Recent Learnings** | **즉시 (살아있는 문서)** |

회사 BI 적용 가설: c2spf-analytics의 분기/연간 대형 분석 작업(예: 게임 출시 전후 코호트 분석)에 PLANS.md ExecPlan 패턴을 적용하면, 단일 분석가가 LLM 협업으로 7시간+ 작업을 수행 가능. NON-NEGOTIABLE 5 요건의 "관찰 가능한 동작"은 BI 대시보드/보고서 산출물로 매핑 자연스러움.

## 극한 사례 1: autoresearch의 초경량 하네스

[[autoresearch]] (Karpathy, 2026-03)는 **하네스를 어디까지 줄일 수 있는가**의 한 답변이다. 4층 레이어가 모두 최소화돼 있다:

| 레이어 | autoresearch에서의 모양 |
|--------|------------------------|
| 지식 | `program.md` 한 장 (~7KB) |
| 도구 | `bash`, `python`, `git`만 |
| 패키지 | 없음 (Skills/Plugins 미사용, `pyproject.toml` 추가 금지) |
| 통제 | "5분 시간 예산 + `val_bpb` 단일 메트릭 + Simplicity 기준" 세 줄 |

가벼운데도 작동한다는 점이 핵심. 하네스가 작을수록 에이전트의 자유도가 커지고, 그 자유도를 견디는 건 **평가 메트릭의 객관성**이다 (autoresearch는 이걸 `prepare.py`에 잠궈둠).

[[autonomous-research-loop]] 페이지에서 이 패턴을 일반화한 모양으로 정리.

## 관련 개념

- [[context-engineering]]: 하네스의 지식 레이어를 설계하는 방법
- [[token-economy]]: 하네스가 컨텍스트를 낭비 없이 쓰도록 만드는 원리
- [[claude-code]]: 하네스 개념을 제일 선명하게 구현한 제품
- [[llm-wiki-pattern]]: 이 위키 자체가 개인 지식 관리용 하네스
- [[autonomous-research-loop]]: 하네스를 극한으로 압축한 자율 운영 패턴
- [[autoresearch]]: 그 패턴의 표준 시제품

## Anthropic의 자기 정의 (claude-cookbooks)

[[anthropic]]이 직접 박은 하네스 정의 (`claude_agent_sdk/README.md`):

> "Claude Code the closest thing to a 'bare metal' harness for Claude's raw agentic power: a minimal yet complete and sophisticated interface that lets the model's capabilities shine with the least possible overhead."

이 한 문장이 [[claude-code]]를 "코딩 도구"에서 "Claude의 raw agentic power를 위한 bare-metal harness"로 자리매김함. [[claude-agent-sdk]]는 같은 하네스를 코드로 노출해 SW 외 도메인(연구 에이전트·개인 비서·SRE)에 raw power를 푸는 통로. 따라서 위키에서 하네스 = "Claude Code/Agent SDK 인터페이스 + 사용자 정의 4층 레이어 합성".

## 출처

- [[claude-code-master-guide]] — CHOI의 가이드북에서 가장 중심적인 개념. 5장 "시스템 설계: 문맥, 하네스, 검증"
- [[karpathy-autoresearch]] — 하네스 최소화의 극단 사례. `program.md` 한 장으로 LLM 학습 자율 실험 운영
- [[anthropics-skills]] — 패키지 레이어의 표준 구현 (SKILL.md + scripts·references·assets, 3-Level Progressive Disclosure)
- [[anthropics-claude-cookbooks]] — Anthropic 자기 정의 "bare-metal harness" 문장 출처 + claude_agent_sdk 6단계 튜토리얼이 하네스를 SW 외 도메인으로 푸는 reference
- [[github-spec-kit]] — 하네스 스펙트럼의 **표준화 극단**. SDD 메소드론을 9개 슬래시 명령 + 5 템플릿 + 9 Articles 헌법으로 코드화. autoresearch의 최소 하네스와 정확히 반대 극단을 박음 → harness 개념의 양극 완성
- [[scikit-learn]] — 하네스의 **제3축 "library-as-harness"** 사례. 19년 변하지 않은 5가지 API 컨트랙트(`fit`/`predict`/`transform`/`Pipeline`/Meta-estimator)가 곧 작업 운영 패턴. SLEP(Scikit-Learn Enhancement Proposal)이 [[github-spec-kit]] SDD나 [[anthropics-skills]] SKILL.md의 19년 선배 — "표준화 → 구현" 분리 패턴의 원형. 30+ 호환 라이브러리 생태계가 컨트랙트 영구성의 결과
- [[openai-openai-cookbook]] — 하네스의 **제5축 "PLANS.md / ExecPlans + 살아있는 AGENTS.md"** 사례. [[openai]] cookbook(★73K 4년차)이 박은 두 가지 거버넌스 패턴: (1) **PLANS.md / ExecPlans** — Codex `gpt-5.2-codex`가 단일 프롬프트로 7시간+ 작업하도록 만드는 living document. NON-NEGOTIABLE 5 요건(자기완결 / 살아있는 문서 / 초보자 구현 / 관찰 가능한 동작 / 본문 용어 정의) + 단일 fenced code block 형식 강제. `articles/codex_exec_plans.md` (16KB)에서 정의. (2) **AGENTS.md (5.5KB)의 "Recent Learnings" 섹션** — 운영 중 발견된 함정·솔루션 6개를 "현상 → 대응 → 이유" 형식으로 누적하는 살아있는 운영 노트. 다른 OSS의 정적 가이드(astral-sh/uv, scikit-learn, fastapi, flutter 등)와 본질적으로 다른 첫 메인스트림 사례. → 1~4축이 모두 정적 가이드라면 본 5축은 시간 기반 검증(7시간+) + 실시간 학습 누적의 살아있는 모드. [[agent-skills]] 외부 채택 7단계 진화의 7번째 단계와 동일 시점 반영
- [[flutter-flutter]] — 하네스의 **제4축 "vendor-neutral asset + 토큰 예산 다층화"** 사례. `.agents/skills/` 표준 채택 + `.claude/skills` 심볼릭 링크 forwarding + `docs/rules/` 4계층(1k/4k/10k/full) 도구별 대응 + `agent-artifacts/` 격리. 11년차 거대 OSS가 다중 AI 도구 환경에서 거버넌스를 운영하는 첫 사례. [[anthropics-skills]] 표준의 두 번째 외부 채택([[github-spec-kit]] Codex 모드 첫 번째)이지만, **위치 컨벤션은 자체 결정**으로 표준 채택자가 정의자를 누른 모델
- [[openai-openai-agents-python]] — 하네스의 **제5축 "PLANS.md / ExecPlans"의 본체 단 풀스택 적용** 사례. [[openai]]의 1년차 멀티 에이전트 SDK(★25K, v0.14.6)가 cookbook 정의된 ExecPlan 메소드론을 **자기 핵심 SDK 운영에 풀스택 채택**: (1) `PLANS.md`(5,485B) — cookbook의 `articles/codex_exec_plans.md`(16KB)를 응축, NON-NEGOTIABLE 4 + Living Sections 4(Progress / Surprises & Discoveries / Decision Log / Outcomes & Retrospective) + 단일 fenced code block 강제. (2) `AGENTS.md` "ExecPlans" 섹션이 `Use an ExecPlan when work is multi-step, spans several files, involves new features or refactors, or is likely to take more than about an hour` 한 줄로 PLANS.md 자동 호출. (3) `.codex/hooks.json` Stop 훅 → `uv run python stop_repo_tidy.py` 자동 정리. (4) **9개 운영 SOP 스킬 (`.agents/skills/`)** — `$code-change-verification`/`$implementation-strategy`/`$pr-draft-summary`/`$runtime-behavior-probe`(13.4KB ★)/`$docs-sync`/`$examples-auto-run`/`$final-release-review`/`$openai-knowledge`/`$test-coverage-improver` — 각자 trigger·skip·workflow 정책 명시 + **스킬 간 호출 (skill chaining)** 명시. 5축은 "표준 정의 (autoresearch 최소 / spec-kit 중간 / scikit-learn library-as-harness / flutter vendor-neutral asset / cookbook PLANS.md)"의 메소드론 단이라면, 본 사례는 **메소드론 정의자가 자기 본체에 동일 패턴을 풀스택 적용**한 **거버넌스 자기 채택 (self-adoption)** 직접 증거. 회사 BI 적용 가설 보강 — 9개 스킬 중 4개(`code-change-verification`/`docs-sync`/`runtime-behavior-probe`/`pr-draft-summary`)가 c2spf-analytics SOP에 직접 매핑

## 열린 질문

- BI 업무에서 쿼리 에이전트용 최소 하네스는 어떤 모양인가? (SQL 스키마·샘플 쿼리·검증 SELECT·승인 규칙)
- Cowork와 Claude Code 사이 하네스를 공유할 때의 경계는? (CLAUDE.md는 공유, 권한은 분리?)

## 인용한 페이지 (cited_by)

- [[agent-patterns]]
- [[agent-skills]]
- [[agent-stack-evolution]]
- [[anthropic]]
- [[anthropics-claude-cookbooks]]
- [[anthropics-skills]]
- [[astral]]
- [[astral-sh-ruff]]
- [[astral-sh-uv]]
- [[autonomous-research-loop]]
- [[autoresearch]]
- [[backend-fastapi-stack]]
- [[c2spf-analytics]]
- [[claude-agent-sdk]]
- [[claude-code]]
- [[claude-code-master-guide]]
- [[claude-managed-agents]]
- [[context-engineering]]
- [[cowork]]
- [[crewai]]
- [[deepagents]]
- [[fastapi]]
- [[flutter]]
- [[flutter-flutter]]
- [[github-spec-kit]]
- [[karpathy]]
- [[karpathy-autoresearch]]
- [[karpathy-nanochat]]
- [[karpathy-nanogpt]]
- [[langgraph]]
- [[llm-infra-meta-cluster]]
- [[llm-wiki-pattern]]
- [[matechat]]
- [[mcp]]
- [[microsoft-ai-agents-for-beginners]]
- [[nanochat]]
- [[nanogpt]]
- [[openai]]
- [[openai-agents-python]]
- [[openai-cookbook]]
- [[openai-openai-agents-python]]
- [[openai-openai-cookbook]]
- [[pandas-dev-pandas]]
- [[portfolio]]
- [[python-packaging]]
- [[rag]]
- [[ruff]]
- [[scikit-learn]]
- [[scikit-learn-scikit-learn]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-mate-chat]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[slash-commands-vs-agent-skills]]
- [[spec-driven-development]]
- [[spec-kit]]
- [[token-economy]]
- [[using-llm-wiki-as-rag]]
- [[uv]]

## 인용한 페이지

- [[agent-patterns]]
- [[agent-sdk-comparison]]
- [[agent-skills]]
- [[agent-stack-evolution]]
- [[annotated-pattern]]
- [[anthropic]]
- [[anthropics-claude-cookbooks]]
- [[anthropics-skills]]
- [[astral]]
- [[astral-sh-ruff]]
- [[astral-sh-uv]]
- [[autonomous-research-loop]]
- [[autoresearch]]
- [[backend-fastapi-stack]]
- [[c2spf-analytics]]
- [[chain-of-thought-prompting]]
- [[claude-agent-sdk]]
- [[claude-code]]
- [[claude-code-master-guide]]
- [[claude-managed-agents]]
- [[codex]]
- [[context-engineering]]
- [[cowork]]
- [[crewai]]
- [[deepagents]]
- [[fastapi]]
- [[flutter]]
- [[flutter-flutter]]
- [[github-spec-kit]]
- [[governance-axis-comparison]]
- [[karpathy]]
- [[karpathy-autoresearch]]
- [[karpathy-nanochat]]
- [[karpathy-nanogpt]]
- [[langgraph]]
- [[llm-infra-meta-cluster]]
- [[llm-wiki-pattern]]
- [[matechat]]
- [[mcp]]
- [[microsoft-ai-agents-for-beginners]]
- [[nanochat]]
- [[nanogpt]]
- [[openai]]
- [[openai-agents-python]]
- [[openai-cookbook]]
- [[openai-openai-agents-python]]
- [[openai-openai-cookbook]]
- [[pandas-dev-pandas]]
- [[portfolio]]
- [[progressive-disclosure]]
- [[python-packaging]]
- [[rag]]
- [[ruff]]
- [[scikit-learn]]
- [[scikit-learn-scikit-learn]]
- [[sentry]]
- [[seokgeun-kim]]
- [[seokgeun-mate-chat]]
- [[seokgeun-operating-profile-2026]]
- [[seokgeun-stack-guide]]
- [[slash-commands-vs-agent-skills]]
- [[spec-driven-development]]
- [[spec-kit]]
- [[token-economy]]
- [[using-llm-wiki-as-rag]]
- [[uv]]
- [[vendor-neutral]]
