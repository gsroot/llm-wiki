---
title: "에이전트 스택의 3축 진화 — Microsoft · Anthropic · Karpathy 비교"
type: synthesis
category: comparison
tags: [agent-stack, 비교분석, microsoft, anthropic, karpathy, harness, agent-skills, agent-patterns, autonomous-research-loop, 운영표준, BI, 개인비서]
sources: [[microsoft-generative-ai-for-beginners]], [[microsoft-ai-agents-for-beginners]], [[microsoft-ml-for-beginners]], [[microsoft-web-dev-for-beginners]], [[microsoft-data-science-for-beginners]], [[anthropics-skills]], [[anthropics-claude-cookbooks]], [[karpathy-autoresearch]], [[karpathy-nanogpt]], [[karpathy-nanochat]]
created: 2026-04-27
updated: 2026-04-27
---

# 에이전트 스택의 3축 진화 — Microsoft · Anthropic · Karpathy 비교

## 요약

2026년 봄 시점, LLM 에이전트 시대의 운영 표준은 **세 가지 다른 추상화 레이어**로 결정화되고 있다. **Microsoft는 "단일 운영체계"**(co-op-translator GitHub Action·ff-quizzes·Foundry Discord 한 묶음으로 5 시리즈 통합 운영), **Anthropic은 "표준-구현 분리"**(`agentskills.io` 표준 ↔ `anthropics/skills` 구현 ↔ `anthropics/claude-cookbooks` 실습), **Karpathy는 "minimal harness"**(`program.md` 한 장 + 시간 예산 + `val_bpb` 단일 메트릭). 같은 시대의 같은 도구를 쓰면서도 **무엇을 표준으로 박고 무엇을 자유롭게 두는가**의 결정이 정반대다. 회사 BI/개인 비서를 만들 때 이 3축의 어느 위치를 잡느냐가 가장 큰 설계 결정이 된다.

## 배경

이 위키에 2026-04-15부터 4-27까지 약 2주간 LLM 에이전트 운영 표준을 다룬 거대 자료 3축이 동시에 들어왔다:

| 축 | 대표 자료 | 들어온 시점 |
|----|----------|------------|
| Microsoft | for-beginners 5종 통합 (`generative-ai`/`ai-agents`/`ml`/`web-dev`/`data-science`) | 2026-04-27 (4회차) |
| Anthropic | `anthropics/skills` + `anthropics/claude-cookbooks` 짝 | 2026-04-27 (3, 5회차) |
| Karpathy | `autoresearch` + `nanoGPT` + `nanochat` | 2026-04-27 (1, 2회차) |

각 자료의 **소스 페이지·엔티티·개념**은 이미 위키에 정리되어 있지만, **셋의 운영 철학을 한 자리에서 비교한 페이지가 없었다**. 본 분석의 출발점은 다음 질문:

> "같은 LLM·같은 시대인데 왜 운영 방식이 이렇게 다른가? 회사 BI에 도입할 때 어느 모델을 따라가야 하는가?"

## 분석

### 1. 표준-구현 관계의 3가지 모양

| 축 | 표준의 위치 | 구현의 위치 | 분리 방식 |
|----|----------|----------|----------|
| **Microsoft** | README 안에 통합 (lesson별로 분산) | 같은 리포 (Jupyter notebook + 코드) | **분리 안 함** — 표준이 곧 구현물 |
| **Anthropic** | 외부 사이트 [agentskills.io](https://agentskills.io) | [[anthropics-skills]] (마켓플레이스) + [[anthropics-claude-cookbooks]] (실습) | **명확히 분리** — 표준 중립성 확보 |
| **Karpathy** | 표준 자체가 없음 (`program.md` 한 장으로 자기 정의) | [[autoresearch]] / [[nanogpt]] / [[nanochat]] 단일 파일 | **표준 = 구현** — 한 파일 안에 모든 것 |

이 3가지가 사실상 **에이전트 표준화의 3가지 길**이다.

### 2. 최소 단위(unit of distribution)의 차이

| 축 | 최소 단위 | 단위당 크기 | 단위 수 |
|----|----------|----------|--------|
| **Microsoft** | `lesson.md` (페다고지 6단 구조: pre-quiz / 본문 / knowledge checks / challenge / supplemental reading / assignment / post-quiz) | 200~500 lines | 107개 (5 시리즈 합산) |
| **Anthropic** | `SKILL.md` 패키지 (frontmatter + body + scripts/references/assets) 또는 `notebook.ipynb` | SKILL.md <500lines / notebook 평균 ~30KB | 17 SKILL + ~100 노트북 |
| **Karpathy** | 단일 파일 (`autoresearch.py`, `train.py`, `program.md`) | 수백~수천 line, 한 파일 | 1~3개 |

**해석**: Microsoft는 "교육 단위", Anthropic은 "재사용 작업 단위", Karpathy는 "운영 단위"를 표준화. 같은 LLM 시대의 사용 시나리오가 셋 다 다르다는 것을 의식적으로 분리.

### 3. 페다고지(가르치는 방식)의 위계

| 축 | 학습자 가정 | 학습 흐름 | 평가 |
|----|----------|----------|------|
| **Microsoft** | 입문자 (배경 지식 없음) | sketchnote → pre-quiz → 본문 → knowledge check → challenge → assignment → post-quiz | quiz 정답률 + assignment 제출 |
| **Anthropic** | API 개발자 (개발 경험 있음) | README → 노트북 top-to-bottom 실행 → 결과 확인 | "노트북이 에러 없이 끝까지 실행되는가" |
| **Karpathy** | 연구자/실험가 (LLM 내부 구조 익숙) | "Read the source. Run it. Modify it." | `val_bpb` 같은 정량 메트릭 |

Karpathy의 [nanoGPT의 deprecated note](https://github.com/karpathy/nanoGPT)("for educational purposes, no further development")가 상징적: **자기 자료를 "교육용"이라 명시하면서도 페다고지 자체는 의도적으로 만들지 않음**. 학습자가 코드를 직접 깎으며 배우는 게 페다고지.

### 4. CI-로컬 통합 채널

각 축에서 "로컬에서 작동 = CI에서 작동"을 보장하는 단일 채널이 다음과 같이 다르게 구현됨:

| 축 | 단일 채널 | 어디 정의되나 | 호출 주체 |
|----|----------|----------|----------|
| **Microsoft** | `co-op-translator` GitHub Action (50+ 언어 자동 번역) | `.github/workflows/co-op-translator.yml` | GitHub Actions (자동) |
| **Anthropic** | 슬래시 커맨드 `/notebook-review`, `/model-check`, `/link-review` | `.claude/commands/*.md` | Claude Code(로컬) + GitHub Actions(CI) 양쪽 |
| **Karpathy** | 평가 스크립트 (`prepare.py` + `val_bpb`) | 단일 .py 파일 | 사람이 직접 실행 |

핵심 관찰: **Microsoft는 "infra-driven"(CI가 표준 강제), Anthropic은 "command-driven"(슬래시 커맨드가 표준), Karpathy는 "metric-driven"(메트릭이 표준)**. 셋 다 다른 메커니즘으로 같은 효과(standard enforcement)를 달성.

### 5. 다국어/접근성 정책

| 축 | 다국어 전략 | 접근성 정책 |
|----|----------|-----------|
| **Microsoft** | **50+ 언어 자동 번역 (`co-op-translator` GitHub Action)** | Web Dev lesson 03 = Accessibility, Data Science lesson 02 = Ethics — **본문 02·03번에 가치 박기** |
| **Anthropic** | 영어 only (cookbook) / 영어 only (skills 마켓플레이스) | 비공식, "재무 도메인 사례"(skills cookbook 02번)에 한정 |
| **Karpathy** | 영어 only | 명시적 비고려 (코드 자체가 universal) |

Microsoft의 "**다국어 + 접근성 + 윤리를 입문 단계에서 명시**"는 다른 둘이 안 가진 강점. **회사 BI에 도입할 때 가장 차용 가치가 높은 부분이 여기**.

### 6. 메트릭과 객관성

각 축이 "에이전트가 잘 작동하는가"를 어떻게 판정하는가:

| 축 | 메트릭 | 객관성의 원천 |
|----|-------|-----------|
| **Microsoft** | quiz 정답률, assignment 제출 (사람 평가) | 페다고지 6단 + 다관점 검토 |
| **Anthropic** | "노트북이 에러 없이 실행되는가" + skill description trigger rate (skill-creator 자동 평가) | 자동 평가 루프 (`run_loop.py`) |
| **Karpathy** | `val_bpb` (validation bits per byte) — 단일 정량 메트릭 | 메트릭이 `prepare.py`에 잠겨 LLM이 만질 수 없음 |

[[autonomous-research-loop]] 페이지에서 추출했던 "**메트릭의 객관성이 자율 루프의 신뢰를 만든다**"는 명제가 3축에 다 적용되되, 객관성을 만드는 방식이 다르다. Karpathy식이 가장 엄격(메트릭이 코드로 잠김), Microsoft식이 가장 인간 중심(quiz/assignment), Anthropic식이 그 중간(자동 + 인간 검토 혼합).

### 7. [[harness]] 4층 레이어로 본 3축

[[harness]]에 정리된 4층(지식·도구·패키지·통제) 레이어가 3축에서 어떻게 다른지:

| 레이어 | Microsoft | Anthropic | Karpathy (autoresearch) |
|--------|-----------|-----------|-------------------------|
| **지식** | 107 lesson md + 50+ 언어 번역 | CLAUDE.md + 노트북 markdown 셀 | `program.md` 한 장 (~7KB) |
| **도구** | 다양 (Streamlit·BigQuery·Azure·OpenAI·...) | Bash·Read·Write·MCP 통합 | bash·python·git만 |
| **패키지** | lesson 단위 (재사용 안 함, 1회 학습) | SKILL.md 패키지 17개 (재사용 표준) | 패키지 없음 (Skills/Plugins 미사용 명시) |
| **통제** | quiz·assignment·co-op-translator | Permissions·Hooks·Plan Mode·`paths`·`context: fork` | "5분 시간 예산 + `val_bpb` + Simplicity" 세 줄 |

**3축의 추상화 레이어가 다른 부분**: Microsoft는 지식 레이어가 가장 두껍고, Anthropic은 패키지 레이어가 가장 두껍고, Karpathy는 통제 레이어가 가장 가볍다. 셋 다 자기 도메인에서 합리적인 균형.

### 8. 자기 정의 인용 비교

각 축이 자기 자신을 어떻게 부르는가의 한 문장:

| 축 | 자기 정의 (출처) |
|----|--------------|
| **Microsoft** | "The whole world has access to it free of charge!" — `microsoft-for-beginners` 시리즈 README |
| **Anthropic** | "Claude Code the closest thing to a 'bare metal' harness for Claude's raw agentic power" — `claude_agent_sdk/README.md` |
| **Karpathy** | "for educational purposes" + "Read the source." — `nanoGPT` README |

세 자기 정의가 각자의 운영 철학을 한 줄로 요약: Microsoft = **접근성·무료**, Anthropic = **bare-metal harness**, Karpathy = **read the source**. 위키에서 가장 빈번히 인용되는 문장 후보들.

## 결론

### 핵심 인사이트 5가지

1. **3축은 보완 관계, 경쟁 관계가 아니다** — Microsoft가 입문자를 가르치고, Anthropic이 production을 표준화하고, Karpathy가 연구·minimal 패턴을 보여준다. **사용자가 어느 단계에 있느냐에 따라 다른 축을 따라야 한다**.
2. **표준-구현 분리의 깊이가 운영 철학의 가장 큰 차이** — Microsoft는 통합(빠른 입문), Anthropic은 분리(표준 중립성), Karpathy는 단일 파일(자기 결정성). 회사 BI에 어느 쪽을 따를지가 의사결정의 1차 갈래.
3. **CI-로컬 통합 채널은 모든 축이 갖고 있다** — 메커니즘만 다를 뿐(Action / 슬래시 커맨드 / 메트릭). **위키 운영에 차용할 때 가장 빨리 베낄 수 있는 부분**.
4. **다국어·접근성·윤리는 Microsoft만 본문에 박았다** — Anthropic·Karpathy는 비고려. **회사 BI에 도입할 때 Microsoft 패턴을 의식적으로 차용해야** 한국 사용자·일본 사용자·내부 비전공자도 쓸 수 있는 BI가 됨.
5. **객관성을 만드는 방식의 위계** — Karpathy식 메트릭 잠금 > Anthropic식 자동 평가 > Microsoft식 인간 평가. **자율 루프를 만들수록 Karpathy 방식**, 사람이 검토하는 워크플로우라면 Microsoft 방식.

### 회사 BI에 도입할 때의 의사결정 가이드

석근의 게임 데이터 BI에 에이전트를 도입한다고 할 때, 3축 중 어느 패턴을 따라야 하는지:

| BI 시나리오 | 권장 축 | 이유 |
|------------|--------|------|
| **사내 비전공자가 SQL을 자연어로 조회** | Microsoft 패턴 | quiz/assignment 페다고지 + 다국어/접근성 |
| **자주 쓰는 BI 쿼리 패턴을 표준화** | Anthropic 패턴 | SKILL.md로 재사용 + 슬래시 커맨드로 호출 |
| **새로운 지표 정의·실험을 자동화** | Karpathy 패턴 | minimal harness + 정량 메트릭 잠금 |
| **세 시나리오가 동시에 필요** | **3축 합성** | 페다고지(MS) + 패키지(Anthropic) + 메트릭(Karpathy) |

**가장 흔한 함정**: 한 축만 따라가면 다른 축의 강점을 놓침. 예: Anthropic만 따라가면 SKILL.md 패키지는 잘 만들지만 다국어·접근성 부재. Karpathy만 따라가면 메트릭은 잘 잠그지만 사용자 페다고지 없음.

### 개인 비서 AI에 도입할 때

석근의 "개인 비서 AI 서비스 개발" 관심사에는:

- **Anthropic의 [[claude-agent-sdk]] `01_The_chief_of_staff_agent`가 가장 가까운 reference** — Output styles · Plan mode · Hooks · Subagent를 한 노트북에 압축
- **Karpathy의 minimal harness는 "1인용 도구"의 단순성 모델** — `program.md` 한 장 + 시간 예산이 개인 비서 자기 진화 루프와 직접 매핑
- **Microsoft 패턴은 "사용자 = 자기 자신"이므로 부분 차용** (다국어 X, 접근성 X, 페다고지 X)

따라서 **개인 비서는 "Anthropic 70% + Karpathy 30%"의 비율**, 회사 BI는 **"Microsoft 50% + Anthropic 30% + Karpathy 20%"의 비율**이 일차 가설.

### 위키 운영 자체에의 차용

이 위키 자신을 운영할 때:

- **Microsoft**에서 차용: 한국어/영어 병기 (제목 한국어 + tag 한영 병기), 접근성/윤리를 본문에 박는 페다고지
- **Anthropic**에서 차용: 슬래시 커맨드 `/wiki-lint`(향후), `registry.yaml` 같은 단일 카탈로그(현재 `index.md`가 그 역할), SKILL.md로 위키 조회 패키지화
- **Karpathy**에서 차용: `program.md` 한 장 같은 단일 운영 계약서 (현재 `CLAUDE.md`가 그 역할), 메트릭 잠금 (위키에 적용 가능한 메트릭은 무엇인가?)

위키가 이미 셋을 부분 차용 중이며, 의식적으로 비율을 조정할 수 있다.

## 스냅샷 이후 — 4축·5축 확장 노트 (2026-04-27 후속 추가)

본 페이지는 원래 Microsoft·Anthropic·Karpathy 3축 비교로 작성됐다. 같은 날 후속 수집된 [[github-spec-kit]]와 [[flutter-flutter]]가 각자 새로운 축을 박아 **5축 진화**로 확장:

| 축 | 핵심 명제 | 결과물 | 표준-구현 관계 |
|----|---------|--------|--------------|
| Microsoft | 단일 운영체계로 학습 콘텐츠 정렬 | for-beginners 5종 + co-op-translator | 통합 (표준 = 구현물) |
| Anthropic | 표준은 분리·구현은 cookbook + marketplace | anthropics/skills + claude-cookbooks | 명확 분리 (agentskills.io ↔ 마켓플레이스 ↔ 노트북) |
| Karpathy | 최소 하네스로 자율 진화 | autoresearch + nanochat | 표준 = 구현 (단일 파일) |
| **GitHub spec-kit** | **메소드론 도구화 + 30+ 에이전트 동일 설치** | spec-kit (CLI + 9 슬래시 명령 + 5 템플릿) | **메소드론 → 다중 에이전트 어댑터** (`SkillsIntegration` base class) |
| **Google (Flutter)** | **자산 vendor-neutral화 + 토큰 예산 4계층** | flutter/flutter `.agents/` + `docs/rules/` (1k/4k/10k/full) | **표준 채택, 위치는 자체 결정** (`.agents/skills` + `.claude/skills` 심볼릭 링크) |

### 4·5축 추가의 의미

- **GitHub spec-kit (4번째 축)**: Anthropic 표준의 **첫 외부 채택**. Codex CLI 통합이 `--integration-options="--skills"`로 `.codex/skills/speckit-*/SKILL.md` 9개 패키지를 배포. "agent-skills = Anthropic-only" 가설을 깸. 그러나 메소드론 자체(SDD)는 spec-kit가 정의 — 메소드론 → 도구 → 다중 에이전트 어댑터의 흐름.
- **Google Flutter (5번째 축)**: Anthropic 표준의 **두 번째 외부 채택, 그러나 다른 모델**. `.agents/skills/`에 자기 자산을 두고 `.claude/skills` 심볼릭 링크로 forwarding — **표준 채택자가 정의자의 위치 컨벤션을 누른** 첫 사례. 또한 `docs/rules/` 4계층(rules_1k 799B → 4k 3.5K → 10k 9.4K → full 30K)이 **AI 도구 시장 매트릭스**(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K)에 자동 매칭하는 패턴을 박음 — Anthropic의 progressive disclosure 3-level을 도구별 토큰 단위로 더 세분화.

### 결론 갱신

- 원래 3축 결론(보완 관계, 표준-구현 분리 깊이, CI-로컬 채널, 다국어·접근성, 객관성 위계)은 5축에서도 유효
- 추가 인사이트: **표준 정의자 ≠ 표준 채택자**의 모델은 GitHub·Flutter 두 사례에서 다르게 나타남. spec-kit는 "메소드론 표준화", Flutter는 "위치 컨벤션 재정의" — agent-skills 표준이 도메인별로 다르게 흡수되는 첫 신호.
- **회사 BI 도입 가이드 보강**: Flutter의 `docs/rules/` 4계층 패턴은 BI 도메인의 `CLAUDE_1k.md/4k.md/10k.md` 분할에 직접 차용 가능. 다중 AI 도구를 BI에 통합할 때 (Cursor + Copilot + Claude Code + ChatGPT) 룰 파일을 자동 매칭.

## 스냅샷 이후 — 4축·5축 확장 노트 (2026-04-27 후속 추가)

본 페이지는 원래 Microsoft·Anthropic·Karpathy 3축 비교로 작성됐다. 같은 날 후속 수집된 [[github-spec-kit]]와 [[flutter-flutter]]가 각자 새로운 축을 박아 **5축 진화**로 확장:

| 축 | 핵심 명제 | 결과물 | 표준-구현 관계 |
|----|---------|--------|--------------|
| Microsoft | 단일 운영체계로 학습 콘텐츠 정렬 | for-beginners 5종 + co-op-translator | 통합 (표준 = 구현물) |
| Anthropic | 표준은 분리·구현은 cookbook + marketplace | anthropics/skills + claude-cookbooks | 명확 분리 (agentskills.io ↔ 마켓플레이스 ↔ 노트북) |
| Karpathy | 최소 하네스로 자율 진화 | autoresearch + nanochat | 표준 = 구현 (단일 파일) |
| **GitHub spec-kit** | **메소드론 도구화 + 30+ 에이전트 동일 설치** | spec-kit (CLI + 9 슬래시 명령 + 5 템플릿) | **메소드론 → 다중 에이전트 어댑터** (`SkillsIntegration` base class) |
| **Google (Flutter)** | **자산 vendor-neutral화 + 토큰 예산 4계층** | flutter/flutter `.agents/` + `docs/rules/` (1k/4k/10k/full) | **표준 채택, 위치는 자체 결정** (`.agents/skills` + `.claude/skills` 심볼릭 링크) |

### 4·5축 추가의 의미

- **GitHub spec-kit (4번째 축)**: Anthropic 표준의 **첫 외부 채택**. Codex CLI 통합이 `--integration-options="--skills"`로 `.codex/skills/speckit-*/SKILL.md` 9개 패키지를 배포. "agent-skills = Anthropic-only" 가설을 깸. 그러나 메소드론 자체(SDD)는 spec-kit가 정의 — 메소드론 → 도구 → 다중 에이전트 어댑터의 흐름.
- **Google Flutter (5번째 축)**: Anthropic 표준의 **두 번째 외부 채택, 그러나 다른 모델**. `.agents/skills/`에 자기 자산을 두고 `.claude/skills` 심볼릭 링크로 forwarding — **표준 채택자가 정의자의 위치 컨벤션을 누른** 첫 사례. 또한 `docs/rules/` 4계층(rules_1k 799B → 4k 3.5K → 10k 9.4K → full 30K)이 **AI 도구 시장 매트릭스**(Antigravity 12K, OpenAI 1.5K, CodeRabbit 1K, Copilot 4K)에 자동 매칭하는 패턴을 박음 — Anthropic의 progressive disclosure 3-level을 도구별 토큰 단위로 더 세분화.

### 결론 갱신

- 원래 3축 결론(보완 관계, 표준-구현 분리 깊이, CI-로컬 채널, 다국어·접근성, 객관성 위계)은 5축에서도 유효
- 추가 인사이트: **표준 정의자 ≠ 표준 채택자**의 모델은 GitHub·Flutter 두 사례에서 다르게 나타남. spec-kit는 "메소드론 표준화", Flutter는 "위치 컨벤션 재정의" — agent-skills 표준이 도메인별로 다르게 흡수되는 첫 신호.
- **회사 BI 도입 가이드 보강**: Flutter의 `docs/rules/` 4계층 패턴은 BI 도메인의 `CLAUDE_1k.md/4k.md/10k.md` 분할에 직접 차용 가능. 다중 AI 도구를 BI에 통합할 때 (Cursor + Copilot + Claude Code + ChatGPT) 룰 파일을 자동 매칭.

## 열린 질문

- **3축 외에 다른 축이 있는가?** OpenAI(GPT Store + Custom GPTs + AssistantsAPI)는 어디에 위치하는가? Cursor·Cline 같은 IDE-에이전트는?
- **시간이 지나면 3축이 수렴할까, 분기할까?** 가설: Anthropic-Microsoft가 수렴(Anthropic이 다국어 도입 가능성), Karpathy는 분기 유지(연구자용 minimal 노선).
- **회사 BI 도입 시 "한 축 70% + 다른 축 30%"의 비율 가설**이 실제로 맞나? 한 축 100% 또는 다른 비율이 더 효과적일 수 있음.
- **위키 운영 메트릭은 무엇인가?** Karpathy식 메트릭 잠금을 위키에 적용한다면 "방문 빈도 × 위키링크 차수 × source_count"의 가중치 같은 것?
- **이 3축 비교 자체를 SKILL.md로 패키지화 가능한가?** "에이전트 운영 모델 선택" 의사결정 SKILL — Anthropic 패턴이긴 하지만 Microsoft 페다고지를 빌려서.

## 출처

이 종합 분석에 사용된 위키 페이지 (소스 + 개념 + 엔티티):

### 소스 (10)
- [[microsoft-generative-ai-for-beginners]] — 21 Lesson GenAI 입문, 다중 백엔드(Azure/GitHub Models/OpenAI)
- [[microsoft-ai-agents-for-beginners]] — 12+ Lesson, lesson 11(Agentic Protocols MCP/A2A/NLWeb) + lesson 12(Context Engineering 5 type/6 strategy/4 failure)
- [[microsoft-ml-for-beginners]] — 26 Lesson 클래식 ML, 의도적 딥러닝 회피
- [[microsoft-web-dev-for-beginners]] — 24 Lesson, 의도적 프레임워크 회피, 9-chat-project = AI Assistant
- [[microsoft-data-science-for-beginners]] — 20 Lesson, 02=Data Ethics 본문 두 번째, 4-Lifecycle 3단계
- [[anthropics-skills]] — Skills 마켓플레이스 (17개 스킬, 3개 플러그인, skill-creator)
- [[anthropics-claude-cookbooks]] — 14 디렉토리 ~100 노트북 카탈로그, Building Effective Agents 5 패턴, claude_agent_sdk 6단계
- [[karpathy-autoresearch]] — `program.md` 자율 진화 + `val_bpb` 단일 메트릭 + 시간 예산
- [[karpathy-nanogpt]] — "for educational purposes" deprecated 노트, 단일 파일 GPT
- [[karpathy-nanochat]] — $100짜리 ChatGPT 풀 파이프라인, gpt2-speedrun 리더보드 #5/#6 등재(자율 루프 실증)

### 개념 (5)
- [[harness]] — 4층 레이어 분류로 3축 비교의 골격
- [[agent-skills]] — Anthropic 축의 패키지 레이어 표준
- [[agent-patterns]] — Building Effective Agents 5 패턴, Anthropic 축의 워크플로우 분류
- [[autonomous-research-loop]] — Karpathy 축의 자율 루프 추상화
- [[context-engineering]] — Microsoft lesson 12로 카탈로그화된 5 type/6 strategy/4 failure

### 엔티티 (7)
- [[anthropic]] — Anthropic 축의 운영 주체
- [[microsoft]] — Microsoft 축의 운영 주체
- [[karpathy]] — Karpathy 축의 운영 주체
- [[claude-code]] — Anthropic 축의 사람용 진입점
- [[claude-agent-sdk]] — Anthropic 축의 코드용 진입점
- [[microsoft-for-beginners]] — Microsoft 축의 통합 운영체계
- [[autoresearch]] — Karpathy 축의 reference 구현

## 메모

- 이 페이지는 **2026년 4월 시점의 스냅샷**. 6개월 후 다시 보면 위치가 달라질 가능성 높음 — 분기/수렴 판단을 위한 기준선으로 보존.
- 3축 비교는 **반드시 짝(pair) 비교가 더 정확**할 때가 있음 (Microsoft ↔ Anthropic 비교는 [[anthropic]]·[[microsoft]] 엔티티 페이지에 이미 표 있음). 본 페이지는 3자 동시 비교의 가치만 담음.
- 후속 합성 후보: (a) `synthesis/llm-eval-objectivity.md` — 메트릭 객관성의 3축 비교를 더 깊이, (b) `synthesis/wiki-operating-model.md` — 이 위키 자체가 어떤 비율로 3축을 차용 중인지 자기 분석.
