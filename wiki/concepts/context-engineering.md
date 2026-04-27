---
title: "컨텍스트 엔지니어링 (Context Engineering)"
type: concept
category: ai
tags: [컨텍스트엔지니어링, context-engineering, 프롬프트엔지니어링, prompt-engineering, LLM, 자율연구, agent-memory, scratchpad, microsoft-for-beginners]
related: [[harness]], [[token-economy]], [[claude-code]], [[llm-wiki-pattern]], [[autonomous-research-loop]], [[mcp]], [[microsoft-ai-agents-for-beginners]]
source_count: 3
created: 2026-04-15
updated: 2026-04-27
---

# 컨텍스트 엔지니어링 (Context Engineering)

## 정의

LLM에게 **무엇을·언제·어떤 순서로 읽힐지**를 설계하는 기술. 프롬프트(한 번의 입력 문장)보다 한 층 위, 하네스(작업장 전체)보다 한 층 아래에 위치한다.

## 왜 중요한가

프롬프트 엔지니어링이 "어떻게 물을까"였다면, 컨텍스트 엔지니어링은 "무엇을 읽게 할까"다. 모델이 커지고 컨텍스트 윈도우가 넓어질수록 질문의 무게 중심이 이쪽으로 이동한다.

> "중요한 질문도 '어느 모델이 더 똑똑한가'보다 '어느 도구가 실제 일을 덜 끊기게 하는가'로 이동했다." — [[claude-code-master-guide]]

## 세 가지 엔지니어링 층

| 층 | 조작 대상 | 예시 |
|----|----------|------|
| **프롬프트 엔지니어링** | 한 번의 입력 문장 | "step by step으로 설명해줘", 역할 부여 |
| **컨텍스트 엔지니어링** | 컨텍스트 윈도우에 들어가는 자료 조합 | CLAUDE.md 구성, 참고 파일 선택, 순서, 양 |
| **[[harness]] 엔지니어링** | 작업장 전체 (컨텍스트 + 도구 + 권한 + 검증 + 저장) | Hooks, Worktree, approval gate |

## 핵심 내용

### 재사용 컨텍스트 (Memoized Context)

매 턴마다 처음부터 다시 설명하지 않도록 붙들어 두는 배경 컨텍스트.

- CLAUDE.md: 세션 시작 시 자동 로드되는 운영 계약서
- Projects의 배경 자료: 누적되는 프로젝트 컨텍스트
- Memory: 자동 축적되는 세션 간 기억

### 컨텍스트 조립 원칙

1. **짧고 강하게**: CLAUDE.md는 길수록 좋다는 말은 틀렸다. 항상 읽히는 문서라서 **짧고 강한 운영 계약서**일수록 낫다.
2. **역할 분리**: about-me.md(배경), working-rules.md(규칙), brand-voice.md(톤), glossary.md(용어)처럼 파일을 역할별로 쪼개면 재사용·수정·검토가 쉬워진다.
3. **출력 계약 (Output Contract)**: 결과가 어떤 형식과 위치로 나와야 하는지 미리 정한 약속. "잘 써달라"보다 강하다.
4. **필요 범위만**: [[token-economy]] 원칙 — 전체 파일 대신 필요한 조각만

### 파일 vs 프롬프트

파일 기반 컨텍스트가 강한 5가지 이유:
1. **기억을 바깥으로**: 세션이 바뀌어도 파일은 남는다
2. **사람·AI 공유**: Git 관리 가능, 다른 세션·모델도 읽을 수 있다
3. **반복 가능**: 매번 0부터 설명할 필요 없음
4. **검토·수정 쉬움**: 긴 채팅보다 파일 한 줄 수정이 강력
5. **운영 기본 단위**: 대화보다 파일이 오래 남는다

## 실전 적용

### CLAUDE.md 설계 원칙

- 한 페이지 이내 (스크롤 없이 읽힐 것)
- 반드시 지켜야 할 규칙만 (세세한 팁은 별도 파일로)
- 금지 사항과 허용 사항을 명시적으로
- 새 세션이 5초 안에 "이 프로젝트가 무엇인지·어떻게 작업해야 하는지"를 잡을 수 있어야 함

### 컨텍스트 조립 예: 주간 브리프
```
context/
├── about-me.md          (1회 로드)
├── investor-tone.md     (1회 로드)
projects/market-scan/
├── brief.md             (작업 요청)
└── sources.md           (참조 자료, 링크 포함)
templates/
└── weekly-founder-brief.md  (출력 계약)
```

### 컨텍스트 오염 방지

- 여러 작업을 한 세션에서 섞지 않기 (plan / implement / review 분리)
- 긴 세션에서 `/compact`로 압축
- Worktree로 병렬 작업을 물리적으로 분리

### Microsoft가 정리한 5가지 Context Type · 6가지 Strategy · 4가지 Failure Mode

[[microsoft-ai-agents-for-beginners]] lesson 12가 컨텍스트 엔지니어링을 운영 수준에서 체계화. 위 [[claude-code-master-guide]]의 "운영 계약서" 발상보다 한 단계 구체적인 "전략·실패 모드" 카탈로그를 제공한다.

#### 5가지 Context Type — 무엇이 컨텍스트에 들어가는가

| 타입 | 내용 | 위키 매핑 |
|------|------|----------|
| **Instructions** | 시스템 프롬프트, few-shot, 도구 설명 | CLAUDE.md, working-rules.md |
| **Knowledge** | 사실, RAG 검색 결과, 장기 메모리 | 위키 페이지 본문 |
| **Tools** | 외부 함수·API·MCP 서버 정의 + 결과 | [[mcp]] 도구 호출 결과 |
| **Conversation History** | 진행중인 대화 | 세션 로그 |
| **User Preferences** | 학습된 사용자 취향 | Memory, profiles |

#### Planning 3단계

1. **Define Clear Results** — 완료 시 세계의 모습 정의
2. **Map the Context** — 필요 정보의 위치 매핑
3. **Create Context Pipelines** — 가져오는 방법 (RAG, [[mcp]] 서버, 도구 호출)

#### 6가지 Practical Strategy

1. **Agent Scratchpad** — 단일 세션 내 노트. 컨텍스트 윈도우 외부 파일/객체에 저장 후 필요 시 회수. (Karpathy의 `> run.log 2>&1`이 파일 격리 버전)
2. **Memories** — 다중 세션에 걸친 저장 (요약, 사용자 선호, 피드백)
3. **Compressing Context** — 요약·트리밍. 가장 관련 있는 정보만 유지
4. **Multi-Agent Systems** — 각 에이전트가 별도 컨텍스트 윈도우. 컨텍스트 분담이 곧 컨텍스트 엔지니어링
5. **Sandbox Environments** — 코드/대용량 처리는 외부에서 실행 후 결과만 회수
6. **Runtime State Objects** — 서브태스크별 상태 컨테이너. 복잡 태스크에서 단계별 결과만 컨텍스트에 유지

#### 4가지 Failure Mode + 처방

| 실패 | 증상 | 처방 |
|------|------|------|
| **Context Poisoning** | 할루시네이션이 컨텍스트에 박혀 반복 인용됨 → 불가능한 경로 추적 | **validation + quarantine**. 장기 메모리 추가 전 검증, 의심 시 새 컨텍스트 스레드 |
| **Context Distraction** | 누적 정보 양이 커지면서 모델이 학습 지식 대신 누적 히스토리에 과집중 | **summarization** — 주기적으로 요약 후 옛 내용 폐기 |
| **Context Confusion** | 도구가 너무 많아 LLM이 잘못된 호출. 작은 모델일수록 취약 | **RAG over tool descriptions** + 도구를 **30개 미만**으로 제한. 쿼리에 따라 동적 loadout |
| **Context Clash** | 모순 정보가 누적되어 일관성 깨짐 (예: "economy" → 나중에 "business class") | **pruning + offloading**. 새 지시가 옛 지시를 명시적으로 override 또는 scratchpad에서 정리 |

> "Research shows limiting tool selections to fewer than 30."
> — lesson 12

이 30개 한도는 [[claude-code]]가 **Skill의 Progressive Disclosure**(필요 시에만 로드)로 우회하는 발상과 같은 문제를 다른 해법으로 푼다.

#### Memories Strategy 심화 — 7가지 메모리 타입 (lesson 13)

lesson 13(Managing Agentic Memory)이 "Memories" strategy를 구현 수준으로 펼친다. 메모리를 **단일 카테고리가 아니라 7가지 타입**으로 분류하여 각각을 분리·관리.

| 타입 | 지속 범위 | 무엇을 저장 | 예시 |
|------|----------|------------|------|
| **Working Memory** | 단일 task / 한 단계 | 즉시 계산용 핵심 정보 (대화 전체가 아닌 요구사항·결정·액션만) | "I want to book a trip to Paris" — 현재 turn 동안만 |
| **Short-term Memory** | 단일 세션 / 대화 | 대화 컨텍스트 (지시어 해석에 필요) | "How much to Paris?" → "What about accommodation **there**?" |
| **Long-term Memory** | 다중 세션 / 영구 | 사용자 선호, 역사적 상호작용, 일반 지식 | "Ben enjoys skiing, likes coffee with mountain view, avoids advanced slopes due to past injury" |
| **Persona Memory** | 에이전트 자체 | 에이전트의 "성격·역할" 일관성 | "expert ski planner" 톤·전문성 유지 |
| **Episodic / Workflow Memory** | 복잡 task의 시퀀스 | 단계별 성공·실패 기록 | "이 항공편 예약 시도가 매진으로 실패" → 다음에 대안 시도 |
| **Entity Memory** | 명명 객체 | 사람·장소·사물·이벤트 추출 | "Paris", "Eiffel Tower", "Le Chat Noir restaurant" |
| **Structured RAG** | 비정형 → 구조화 | 이메일·이미지·대화에서 dense structured info 추출 | flight: {dest: Paris, date: Tue, airline: AF} |

**구현 도구**:
- **Mem0** — 2단계 파이프라인: ① extraction(LLM이 대화 요약→메모리 추출) → ② update(LLM이 add/modify/delete 결정). hybrid 데이터 스토어 (vector + graph + key-value)
- **Cognee** — 오픈소스 semantic memory. **dual-store**(vector 유사도 + graph 관계). hybrid 검색(vector + graph + LLM reasoning). "living memory"가 진화하면서도 한 그래프로 쿼리 가능
- **Azure AI Search** — Structured RAG 백엔드. "superhuman precision and recall" 클레임

**Self-Improving Agent 패턴 — Knowledge Agent**:

별도 에이전트(Knowledge Agent)가 주 대화를 관찰하며 4단계 수행:
1. **Identify** — 저장 가치 있는 정보인지 판별
2. **Extract & Summarize** — 학습/선호 본질 추출
3. **Store** — 벡터 DB에 영속화
4. **Augment** — 다음 사용자 쿼리에 자동으로 컨텍스트 주입

최적화:
- **Latency**: 1차 필터에 cheaper/faster 모델, 가치 있을 때만 본격 추출/검색 호출
- **Knowledge Base Maintenance**: 자주 안 쓰이는 정보는 "cold storage"로 이동 — 비용 관리

이 패턴은 [[harness]]에서의 "다단계 검증 게이트"와 같은 발상의 메모리 버전 — **별도 에이전트가 메인 에이전트의 출력을 관찰하며 보강**한다.

### 자율 루프 컨텍스트 보호 3원칙 ([[autoresearch]] 사례)

자율 실험 루프가 12회/시간으로 돌면 학습 로그가 즉시 컨텍스트를 폭파시킨다. autoresearch의 `program.md`가 보여준 회피책:

1. **stdout 격리**: `uv run train.py > run.log 2>&1` — `tee` 금지. 출력은 파일로만.
2. **메트릭 1줄 발췌**: `grep "^val_bpb:" run.log` — 결과 1줄만 본문에 노출.
3. **크래시 시에만 tail**: 정상 시 로그 자체를 안 봄. 비정상 시에도 `tail -n 50` 한도.

이 3줄 패턴은 위키 운영에도 그대로 이식 가능하다 — 큰 PDF 변환물이나 외부 데이터를 직접 컨텍스트에 끌어들이지 말고, `grep`/`head`/`tail` 발췌 1~2줄만.

## 관련 개념

- [[harness]]: 컨텍스트 엔지니어링을 지속적으로 작동시키는 상위 구조
- [[token-economy]]: 컨텍스트 분량·조합의 품질 지표
- [[llm-wiki-pattern]]: 이 위키 자체가 컨텍스트 엔지니어링의 개인용 적용
- [[mcp]]: 컨텍스트를 동적으로 조립해주는 외부 도구 프로토콜

## 출처

- [[claude-code-master-guide]] — CHOI의 가이드북 5장 "프롬프트 엔지니어링, 컨텍스트 엔지니어링, 하네스 엔지니어링"
- [[karpathy-autoresearch]] — 자율 실험 루프 운영의 컨텍스트 보호 패턴(`> run.log 2>&1` + `grep` 1줄 발췌)
- [[microsoft-ai-agents-for-beginners]] — lesson 12 "Context Engineering for AI Agents"가 5 type / 6 strategy / 4 failure mode 카탈로그화 (Microsoft Cloud Advocates 운영판)

## 열린 질문

- 회사 BI 프로젝트용 CLAUDE.md에는 무엇을 담아야 한가? (팀 지표 정의 링크? 데이터웨어하우스 ERD? 파이프라인 명명 규칙?)
- 이 위키의 `templates/` 디렉토리에 `handoff.md`, `working-rules.md` 템플릿을 추가할 필요가 있는가?
