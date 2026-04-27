# 40-stories — STAR 스토리 뱅크

**Synthesis Layer**: 면접·평가·자기소개에서 사용할 **재사용 가능한 서사 단위** 저장소입니다.

## STAR 포맷

| 축 | 의미 | 작성 가이드 |
|----|------|------------|
| **Situation** | 상황 | 1~2 문장. 왜 중요했는지 맥락 제공 |
| **Task** | 과제 | 당시 내 역할/목표. "무엇을 해야 했는가?" |
| **Action** | 행동 | 구체적 3~5 bullet. 동사 중심. 기술 결정·커뮤니케이션·도전 극복 |
| **Result** | 결과 | 정량 지표 우선. "비포/애프터" 또는 "예상/실제" |

## 카테고리 (파일 접두사)

| 접두사 | 주제 | 예시 |
|-------|------|------|
| `leadership-*` | 리더십/의사결정 | `leadership-react-adoption.md` (팀 최초 React 도입 주도) |
| `problem-solving-*` | 기술적 문제 해결 | `problem-solving-gas-fee-optimization.md` (가스비 90% 절감) |
| `impact-*` | 비즈니스 임팩트 | `impact-analytics-ux-improvement.md` (분석 플로우 단축) |
| `learning-*` | 학습·적응 | `learning-blockchain-domain.md` (블록체인 도메인 진입) |

## 스토리 문서 스키마

```yaml
---
title: "팀 최초 React 도입을 주도한 경험"
type: story
category: leadership
period: "2025-06 ~ 현재"
primary_project: "2025-06-analytics-react-renewal"
tags: [frontend, architecture, tech-leadership]
skills_demonstrated:
  - frontend-react
  - devops-container
---

## Situation
...

## Task
...

## Action
- ...
- ...

## Result
- 정량: ...
- 정성: ...
```

## 작성 원칙

1. **하나의 프로젝트에서 여러 스토리 추출 가능** — 동일 프로젝트에 대한 `leadership-*`, `problem-solving-*` 파일 가능
2. **스토리 당 1 페이지 이내** — 면접에서 2~3분 이내에 말할 수 있는 분량
3. **익명 처리** — 공동 작업자 이름 대신 역할로 표기 ("기획 담당자", "FE 동료")
4. **증거 링크** — `primary_project` frontmatter 필드로 `20-projects/` 문서 연결

## 스토리 후보 (초기 추출 대상)

[`../20-projects/com2us-platform/README.md`](../20-projects/com2us-platform/README.md)의 프로젝트 중 강한 서사가 있는 것:

- **React 리뉴얼** → 리더십(React 도입 주도), 임팩트(생산성 30~40%)
- **NFT 마켓** → 문제해결(가스비 90% 절감), 학습(블록체인 도메인)
- **Airbridge API** → 문제해결(새로운 데이터 소스 통합)
- **유저 예측 (AutoML)** → 학습(MLOps 구축), 임팩트(예측 정확도 85%+)
- **CODE 트래블룰** → 문제해결(규제 대응), 리더십(촉박한 일정 주도)
