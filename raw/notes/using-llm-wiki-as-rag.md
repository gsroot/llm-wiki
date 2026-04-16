# 이 LLM 위키를 Claude Code에서 RAG처럼 쓰는 법

> 2026-04-15 초안, 2026-04-16 방법 4 업데이트 (Slash Command → Agent Skill 승격).
> Claude Code(Opus 4.6) 세션에서 석근 질문에 답한 내용을 정리. 이 위키(`/Users/sgkim/llm-wiki`) 기준.
> 관련 조사 문서: `raw/notes/slash-commands-vs-agent-skills.md`

## 핵심 관점: 이 위키는 이미 RAG다

이 위키는 RAG의 "수작업 컴파일 버전"이다. 일반 RAG는 질문할 때마다 벡터 검색으로 청크를 뽑지만, 이 위키는 사전에 요약·링크·인덱스를 컴파일해둔 상태다. Claude Code의 Read/Grep/Glob 도구가 retrieval 역할을 한다.

| 항목 | 일반 RAG | 이 위키 |
|------|---------|--------|
| 지식 획득 | 벡터 검색으로 청크 회수 | 사전 컴파일된 요약·링크 |
| 라우팅 | 유사도 점수 | `index.md` (수동 큐레이션) |
| 축적 | 없음 (매번 재발견) | 복리 성장 |

즉 "RAG처럼 쓴다" = "Claude Code가 `index.md`를 라우터로 삼아 필요한 페이지만 Read하게 한다"가 본질.

## 방법 1: 위키 디렉토리에서 직접 실행 (지금 바로)

```bash
cd ~/llm-wiki
claude
```

이것만으로 완성. 이유:

- `CLAUDE.md`가 자동 로드 → 에이전트가 위키 규칙 이해
- CLAUDE.md에 "세션 시작 시 `wiki/index.md`와 `log.md`를 먼저 읽어라"가 명시되어 있음 → 에이전트가 지식 지도를 먼저 확보
- 이후 자연어 질문만 하면 됨

**질문 예시**:

```
"MCP가 뭐고 qmd와 어떻게 연결돼?"
"하네스 개념을 BI 쿼리 최적화에 적용하면?"
"지난주에 수집한 소스 요약해줘"
```

Claude Code가 자동으로 `index.md` → `wiki/concepts/mcp.md` → 관련 페이지 순으로 Read하며 답변.

## 방법 2: 다른 프로젝트에서 이 위키를 참조 (회사 업무 시)

회사 프로젝트에서 개인 위키 지식을 끌어오고 싶을 때. 그 프로젝트의 `CLAUDE.md`에 참조 지침 추가:

```md
## 참조 지식 베이스

개인 위키: `/Users/sgkim/llm-wiki/wiki/`

다음 경우 먼저 `wiki/index.md`를 Read하고 관련 페이지를 참고:
- AI/LLM 관련 개념 질문
- 지식 관리·문서 운영 방법
- Claude Code·Obsidian·MCP 사용법

위키는 **읽기 전용**. 수정하지 않는다.
```

회사 코드에 집중하되 필요할 때 개인 위키를 retrieval 소스로 활용.

## 방법 3: 세션 시작 시 명시적 로드 (일회성)

```bash
cd ~/work-project
claude
```

첫 메시지로:

```
먼저 /Users/sgkim/llm-wiki/wiki/index.md 읽고,
"토큰 경제학" 개념이 우리 BigQuery 비용 최적화와 어떻게 연결되는지 설명해줘.
```

한 번만 하면 세션 내내 그 컨텍스트가 유지됨. CLAUDE.md 수정 없이 가끔 쓸 때 편함.

## 방법 4: Agent Skill로 패키징 (반복 조회 시, 자동 호출 가능)

> **초안(2026-04-15)**에서는 Slash Command (`~/.claude/commands/wiki.md`)를 제안했으나,
> 조사 결과 Anthropic이 Custom Commands를 Skills에 통합했고 Skills를 권장.
> 자동 호출·supporting files·`context: fork`·`paths` 등 Skill 전용 기능이 위키 조회에
> 특히 유리하여 **Agent Skill로 승격** (2026-04-16).
> 상세 비교: `raw/notes/slash-commands-vs-agent-skills.md`

`~/.claude/skills/wiki/SKILL.md` 파일 생성:

```yaml
---
name: wiki
description: >
  석근의 개인 LLM 위키(/Users/sgkim/llm-wiki) 조회.
  AI·LLM·Claude Code·MCP·지식관리 주제는 물론, 게임 데이터 BI,
  업무 노하우, 학습 기록, 독서 메모, 사이드 프로젝트 아이디어,
  개인 경험 등 어떤 주제든 위키에 축적된 지식이 있을 수 있으므로
  답변 전 먼저 조회한다. 위키에 관련 항목이 없으면 바로 일반 지식으로 답한다.
context: fork
agent: Explore
argument-hint: "[주제]"
---
```

**Slash Command와의 차이 (Agent Skill이 유리한 이유)**:

1. **자동 호출**: description 기반으로 Claude가 판단하여 자동 발동. `/wiki`로 수동 호출도 가능
2. **`context: fork`**: 위키 조회를 서브에이전트로 격리해 메인 세션 컨텍스트 오염 방지
3. **Supporting files**: `query-patterns.md`, `scripts/wiki-stats.sh` 등을 디렉토리에 묶을 수 있음
4. **Personal scope**: `~/.claude/skills/wiki/`에 두면 회사·개인 프로젝트 구분 없이 모든 곳에서 작동

이제 어느 프로젝트에서든 수동 호출:

```
/wiki 하네스
/wiki BI 업무에 LLM 위키 적용
```

또는 자동 호출 — 그냥 관련 질문을 하면 Claude가 알아서 위키를 참조:

```
"하네스 개념으로 내 BI 파이프라인을 리뷰해줘"
→ Claude가 wiki skill 자동 발동 → index.md → [[harness]] Read → 답변
```

## 방법 5: MCP 서버로 노출 (위키가 50+ 페이지 되면)

현재 18페이지라 아직 불필요. 나중에 필요해지면:

1. qmd 설치 + 위키 인덱싱

```bash
qmd index ~/llm-wiki/wiki/
```

2. 프로젝트 루트에 `.mcp.json`:

```json
{
  "mcpServers": {
    "personal-wiki": {
      "command": "qmd",
      "args": ["serve", "/Users/sgkim/llm-wiki/wiki"]
    }
  }
}
```

3. Claude Code에서 위키 검색이 **네이티브 도구**가 됨 (Read보다 빠르고 정확). BM25 + 벡터 하이브리드.

## 방법 선택 매트릭스

| 상황 | 추천 방법 |
|------|----------|
| 위키 자체를 관리할 때 | 방법 1 (`cd ~/llm-wiki && claude`) |
| 회사 프로젝트에서 참조 | 방법 2 (프로젝트 CLAUDE.md에 참조 경로 추가) |
| 가끔 한 번씩 | 방법 3 (세션 첫 메시지로 index.md 로드) |
| 자주 반복 조회 + 자동 호출 | 방법 4 (`/wiki` Agent Skill — 자동·수동 모두) |
| 50+ 페이지 되면 | 방법 5 (qmd MCP) |

## 사용을 잘하기 위한 2가지 팁

### 1. 위키를 자주 키워라

RAG는 데이터 베이스에 비례해 정확도가 오른다. 이 위키는 더 나아가, 수집할 때마다 기존 페이지가 **업데이트·연결**되어 복리로 강해진다 (예: `claude-code` 엔티티가 현재 `source_count: 3`).

### 2. 질문을 "위키에 물어본다"는 감각으로

단순 지식 검색보다 **위키 페이지를 근거로 한 합성**이 가장 강력:

- ❌ "하네스가 뭐야?" (일반 지식)
- ✅ "`wiki/concepts/harness.md` 기준으로, 내 BI 업무 하네스를 설계한다면 어떤 파일 세트부터 시작해야 할까?" (합성)

## 추천 시작점

오늘 당장은 방법 1로 시작하고, 회사 프로젝트에서 끌어다 쓰고 싶어지면 방법 2를 추가하면 된다. 방법 5(MCP)는 위키가 50페이지를 넘은 후.
