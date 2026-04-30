---
title: "RAG (Retrieval-Augmented Generation)"
type: concept
category: ai
aliases: [RAG, Retrieval-Augmented Generation, 검색 증강 생성, 검색-증강-생성, retrieval-augmented-generation]
tags: [검색증강생성, retrieval-augmented-generation, LLM, 검색, retrieval, 생성, generation, 컨텍스트, context, 임베딩, embeddings, 벡터DB, vector-database, agent-skills, harness, mcp, llm-wiki, 53회차]
related:
  - "[[llm-wiki-pattern]]"
  - "[[context-engineering]]"
  - "[[agent-skills]]"
  - "[[harness]]"
  - "[[mcp]]"
  - "[[prompt-cache]]"
  - "[[ml-ai]]"
  - "[[anthropic]]"
  - "[[anthropics-claude-cookbooks]]"
  - "[[claude-code]]"
source_count: 4
observed_source_refs: 4
inbound_count: 12
created: 2026-04-29
updated: 2026-04-29
cited_by_count: 11
---

# RAG (Retrieval-Augmented Generation)

> [!info] 검색 + 생성을 결합한 LLM 컨텍스트 주입 패턴
> *RAG(Retrieval-Augmented Generation, 검색 증강 생성)*. LLM이 답변을 생성하기 전에 외부 지식 베이스에서 관련 문서를 **검색**(retrieval)해서 컨텍스트로 주입하는 패턴. 모델이 학습 시점 이후의 사실, 도메인 전용 지식, 개인 데이터를 답변에 반영할 수 있게 하는 가장 보편적 기법.
> 
> 한국어 표기: **검색 증강 생성**.

## 언제 읽어야 하는가

- "LLM이 최신 정보나 내 데이터를 답변에 활용하게 하려면?" — 정의·핵심 흐름.
- "RAG vs Fine-tuning vs Long Context 어느 것을 골라야 하는가?" — 의사결정 트리.
- "RAG 시스템을 처음 만들려는데 무엇이 필요한가?" — 5계층 컴포넌트.
- "이 위키(llm-wiki) 자체가 RAG와 어떤 관계인가?" — [[llm-wiki-pattern]]과의 비교.
- "agent-skills·harness·mcp와는 어떻게 다른가?" — LLM 컨텍스트 주입 4가지 패턴 비교.

## 정의

RAG는 두 단계로 작동한다:

1. **Retrieval (검색)**: 사용자 질의와 관련된 문서·문단·청크를 외부 지식 베이스에서 찾아온다. 임베딩 기반 의미 검색 또는 BM25 같은 키워드 검색을 쓴다.
2. **Augmentation + Generation (증강 + 생성)**: 검색된 문서를 LLM 프롬프트의 컨텍스트로 추가하고, LLM이 그 컨텍스트를 근거로 답변을 생성한다.

핵심은 **모델 가중치를 건드리지 않고 답변 내용을 바꾸는 것**. fine-tuning(가중치 업데이트)이나 long-context(전체 코퍼스를 매 호출에 박기)와 다른 접근.

## 왜 중요한가

- **사실 신선도**: 모델 학습 시점 이후 정보(2026년 출시 제품, 어제 발생한 사건 등)를 답변에 반영 가능.
- **도메인 적응**: 회사 내부 문서·개인 노트·특수 도메인 지식을 LLM이 활용 가능.
- **할루시네이션 완화**: "근거 문서에서 답하라" 제약을 걸면 모델이 추측 대신 검색된 사실을 인용한다.
- **출처 추적**: 답변에 인용된 청크 ID를 추적해 검증 가능 — 본 위키의 wikilink 인용 정책과 같은 사상.
- **비용 효율**: 매 호출에 전체 코퍼스를 컨텍스트로 박지 않고 관련 부분만 검색해서 토큰 절약.

## 핵심 컴포넌트 (5계층)

| 계층 | 역할 | 표준 도구 |
|---|---|---|
| **인제스트 파이프라인** | 원본 문서를 청크로 분할 → 임베딩 생성 → 벡터 DB 적재 | LangChain, LlamaIndex |
| **임베딩 모델** | 텍스트 → 고차원 벡터 변환 | OpenAI text-embedding-3, sentence-transformers |
| **벡터 저장소** | 의미 검색 가능한 벡터 인덱스 | pgvector, Pinecone, Weaviate, Chroma |
| **검색 엔진** | 질의 임베딩과 가장 가까운 K개 청크 회수 | cosine/dot-product 유사도, hybrid (BM25+vector) |
| **생성 LLM** | 검색 결과 + 시스템 프롬프트 + 사용자 질의로 답변 생성 | Claude, GPT, Gemini |

## RAG vs 다른 컨텍스트 주입 패턴

LLM에 외부 지식을 주입하는 4가지 패턴이 있고, RAG는 그중 하나다:

| 패턴 | 작동 시점 | 위키 페이지 |
|---|---|---|
| **RAG** | 매 질의마다 검색 → 컨텍스트 주입 | 본 페이지 |
| **Agent Skills (SKILL.md)** | 질의 분류 후 관련 스킬만 로드 (progressive disclosure) | [[agent-skills]] |
| **MCP (Model Context Protocol)** | LLM이 도구처럼 호출해 외부 시스템에서 데이터·기능 동적 호출 | [[mcp]] |
| **Context Engineering** | 컨텍스트 윈도우 자체를 설계 — 위 3개의 상위 메타 | [[context-engineering]] |

→ 4개 패턴은 배타적이지 않다. 실제 시스템은 RAG + SKILL + MCP를 조합 (예: [[claude-code]]).

## 의사결정 트리: RAG vs Fine-tuning vs Long Context

```
질문 1: 답변에 필요한 지식이 정적인가, 자주 바뀌는가?
├─ 정적 + 좁은 도메인 (예: 의료 용어 사전) → Fine-tuning 고려
└─ 자주 바뀜 또는 광범위 → RAG 또는 Long Context

질문 2: 코퍼스 크기는?
├─ 100K 토큰 미만 → Long Context (Claude 200K, Gemini 2M)에 통째로 박기
├─ 100K~10M 토큰 → RAG 강력 추천
└─ 10M+ → RAG + 계층적 인덱스 (경계마다 요약 청크)

질문 3: 답변에 출처 인용이 필요한가?
├─ Y → RAG (검색된 청크 ID를 답변에 박을 수 있음)
└─ N → Long Context도 가능하나 RAG가 여전히 효율적

질문 4: 호출당 비용이 중요한가?
├─ 비용 민감 → RAG (관련 청크만 컨텍스트에 박음)
└─ 비용 무관 → Long Context도 OK
```

## 이 위키(llm-wiki)의 RAG 적용 ([[llm-wiki-pattern]]과의 관계)

이 위키 자체가 RAG의 한 사례다. 다만 표준 RAG와 다른 점:

- **검색 단계 부재**: LLM이 질의에 대해 임베딩 검색을 하지 않고, hub 페이지([[llm-infra-meta-cluster]] 등) → 세부 페이지로 직접 wikilink를 따라간다.
- **인덱스가 사람 큐레이션**: [[index]]·[[seokgeun-stack-guide]]·5축 hub 표가 운영자가 직접 만든 라우팅. 자동 임베딩이 아닌 의도된 카탈로그.
- **청크 단위가 페이지**: 표준 RAG는 256~1024 토큰 청크지만, 이 위키는 페이지 단위(평균 142줄, RAG 권장 100~300줄과 정합).
- **메타 페이지 격리**: `rag_exclude: true`로 stale 통계 카탈로그를 답변 근거에서 제외 (43회차 정책).

→ 즉 본 위키는 **"수동 인덱스 + 페이지 청킹 + LLM 추론"** 형태의 변형 RAG. [[llm-wiki-pattern]] 페이지가 본 위키를 다른 RAG 패턴과 비교한다.

## 실전 적용

`uv` + Python으로 최소 RAG 시스템 부트스트랩:

```python
# 1. 의존성
# uv add anthropic chromadb sentence-transformers

from chromadb import Client
from sentence_transformers import SentenceTransformer
from anthropic import Anthropic

# 2. 인제스트 (한 번만)
embedder = SentenceTransformer("all-MiniLM-L6-v2")
client = Client()
collection = client.create_collection("docs")
chunks = ["문서1 청크1", "문서1 청크2", ...]  # 256~1024 토큰
collection.add(
    ids=[f"chunk-{i}" for i in range(len(chunks))],
    embeddings=embedder.encode(chunks).tolist(),
    documents=chunks,
)

# 3. 질의 시
def rag_answer(query: str) -> str:
    q_emb = embedder.encode([query]).tolist()
    results = collection.query(query_embeddings=q_emb, n_results=4)
    context = "\n\n".join(results["documents"][0])
    anthropic = Anthropic()
    msg = anthropic.messages.create(
        model="claude-opus-4-7",
        max_tokens=1024,
        messages=[{
            "role": "user",
            "content": f"다음 컨텍스트로만 답하라:\n{context}\n\n질문: {query}",
        }],
    )
    return msg.content[0].text
```

→ production 시스템은 [[anthropics-claude-cookbooks]]의 memory cookbook · prompt caching · RAG 패턴을 참조.

## 관련 개념

- [[llm-wiki-pattern]] — 이 위키의 변형 RAG 패턴 (수동 인덱스 + 페이지 청킹).
- [[context-engineering]] — RAG의 상위 메타 (컨텍스트 윈도우 설계 자체).
- [[agent-skills]] — progressive disclosure 패턴, RAG의 SKILL.md 변종.
- [[harness]] — RAG는 보통 harness 한 컴포넌트로 들어감.
- [[mcp]] — RAG가 정적 검색이라면 MCP는 동적 도구 호출 (보완 관계).
- [[prompt-cache]] — RAG 컨텍스트 재사용 시 비용 절감.
- [[ml-ai]] — 상위 카테고리.

## 출처

- [[claude-code-master-guide]] — RAG·하네스·거버넌스 실무 운영 관점.
- [[using-llm-wiki-as-rag]] — 본 위키를 Claude Code에서 RAG처럼 쓰는 운영 가이드.
- [[llm-wiki-idea-doc]] — LLM 위키 아이디어 (RAG와의 차이 포함).
- [[anthropics-claude-cookbooks]] — RAG·memory cookbook·prompt caching 패턴 모음.

## 열린 질문

- 본 위키의 "수동 인덱스 + 페이지 청킹" 패턴이 어떤 코퍼스 크기까지 확장 가능한가? 1000+ 페이지에서 수동 인덱스가 한계인가?
- hybrid retrieval (BM25 + vector)이 임베딩 단독보다 얼마나 회수율을 올리는가?
- agentic RAG (LLM이 검색을 도구로 호출 — MCP 기반)는 표준 RAG와 어떻게 다른가? [[mcp]] 페이지와 통합 가능성.
