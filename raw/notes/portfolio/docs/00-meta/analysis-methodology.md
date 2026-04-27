# Analysis Methodology — 분석 방법론

수집된 Raw 자료를 **Synthesis Layer**(프로젝트/스킬/스토리) 문서로 가공하기 위한 분석 방법을 정의합니다.

## 분석의 5가지 축

```
Raw 자료
   │
   ├──▶ ① Chronological      (시간)  → Timeline
   ├──▶ ② Project Clustering (공간)  → 프로젝트 그룹
   ├──▶ ③ Skill Mapping      (역량)  → 스킬 증거
   ├──▶ ④ STAR Extraction    (서사)  → 스토리 뱅크
   └──▶ ⑤ Quantitative       (지표)  → 정량 메트릭
```

---

## ① Chronological Timeline — 시간 축 분석

### 목적
커리어 연대기 구성. 이직·승진·평가 시 "언제 무엇을" 빠르게 답변.

### 방법
1. 모든 프로젝트를 `YYYY-MM` 시작월로 정렬
2. `docs/20-projects/<company>/README.md`에 타임라인 표 작성
3. Mermaid Gantt 추가 (선택):

```
gantt
    title 컴투스플랫폼 프로젝트 타임라인 (2022~)
    dateFormat  YYYY-MM
    section Analytics
    NFT 마켓             :2022-05, 22M
    XPLA 플랫폼          :2024-04, 4M
    공통모듈·배포 개선    :2024-08, 5M
    Airbridge API        :2025-01, 2M
    React 리뉴얼         :2025-06, 11M
```

### 산출물
- `docs/20-projects/<company>/README.md`의 타임라인 섹션

---

## ② Project Clustering — 프로젝트 그룹화

### 목적
유사 프로젝트 묶어 **도메인 전문성**을 드러내기. "8개 프로젝트"보다 "4개 도메인 × 각 2개"가 강하다.

### 김석근 작업 기반 초기 클러스터 (from `old-portfolio.md`)
| 클러스터 | 프로젝트 예 | 핵심 도메인 |
|---------|-----------|-----------|
| **Analytics 시리즈** | 애널리틱스 본체, 공통모듈, Airbridge API, React 리뉴얼 | 게임 데이터 분석, BI |
| **Blockchain 시리즈** | CODE 트래블룰, NFT 마켓, XPLA 플랫폼 | 블록체인, 규제, 스마트컨트랙트 |
| **ML/AI 시리즈** | 유저 예측, AutoML 파이프라인 | ML 서비스 배포 |
| **Infrastructure** | 통합 인증, 비동기 통신 모듈 | 플랫폼화 |

### 방법
1. 프로젝트별 기술 스택과 비즈니스 도메인 추출
2. 2개 이상 공유하는 프로젝트를 묶음
3. 클러스터별 1줄 요약 작성 → `docs/50-portfolio/portfolio-ko.md`에 섹션 헤더로

---

## ③ Skill Evidence Mapping — 스킬 역매핑

### 목적
"Python 경험 있나요?" 질문에 **프로젝트 3개 + 구체적 역할**으로 즉답.

### 방법
1. `docs/30-skills/<skill>.md` 문서 하나당 스킬 하나
2. frontmatter에 스킬 카테고리, 숙련도, 연차
3. 본문에 해당 스킬을 사용한 프로젝트 **테이블**:

```markdown
| 프로젝트 | 기간 | 역할 | 링크 |
|---------|------|------|------|
| React 리뉴얼 | 2025-06~ | FE 설계 주도 | [→](../20-projects/com2us-platform/2025-06-analytics-react-renewal.md) |
| Airbridge API | 2025-01~02 | 풀스택 | [→](../20-projects/com2us-platform/2025-01-airbridge-api.md) |
```

4. 본문 하단에 해당 스킬 관련 STAR 스토리 링크

### 스킬 카테고리 (초기)
- `backend-python` (FastAPI, Django, Flask)
- `backend-java-spring` (Spring Boot)
- `backend-nodejs` (NestJS)
- `frontend-react`
- `frontend-vanilla-js`
- `ml-ai` (AutoML, LLM/LangGraph)
- `data-pipeline` (Airflow, BigQuery, Digdag)
- `devops-container` (Docker, Jenkins)
- `database` (MySQL, PostgreSQL, Redis)
- `blockchain` (Smart Contract, NFT)

---

## ④ STAR Story Extraction — 스토리 뱅크

### 목적
면접·평가·자기소개에서 사용할 **재사용 가능한 서사 단위** 구축.

### 방법
각 프로젝트에서 최소 1개, 최대 3개의 STAR 스토리 추출:

```markdown
## Situation (상황)
문제 상황 1~2문장. 왜 중요했는지.

## Task (과제)
당시 내 역할과 목표. "무엇을 해야 했는가?"

## Action (행동)
구체적 행동. 기술적 결정, 커뮤니케이션, 도전 극복.
동사 중심 3~5 bullet.

## Result (결과)
정량 지표 우선, 정성 평가 보조. "비포/애프터" 또는 "예상/실제".
```

### 카테고리 (40-stories 디렉토리 네이밍)
- `leadership-*` : 리더십/의사결정 (팀 React 도입 주도 등)
- `problem-solving-*` : 기술적 문제 해결 (가스비 90% 절감 등)
- `impact-*` : 비즈니스 임팩트 (사용자 경험 개선, 리드타임 단축)
- `learning-*` : 학습·적응 (새 기술 도입)

---

## ⑤ Quantitative Metrics — 정량 지표 추출

### 목적
"생산성 향상"보다 "**리드타임 30~40% 감소**"가 10배 강하다. 모호한 문장에서 **숫자**를 뽑아낸다.

### 방법
1. 프로젝트 문서에 `metrics:` frontmatter 필드 (YAML list)
2. 각 지표 형식:
   - `"<Before → After> 단위 (<측정 방법>)"`
   - 예: `"가스비 ~90% 절감 (트랜잭션 당 기존 X → Y)"`
   - 예: `"예측 정확도 평균 85%+ (이탈 예측 모델)"`
3. `docs/50-portfolio/` 렌더링 시 상위 3~5개 메트릭을 첫 화면에

### 지표 유형
| 유형 | 예시 |
|------|------|
| **성능** | 응답속도, 처리량, 가스비 |
| **비즈니스** | 활성사용자, 전환율, 리텐션 |
| **생산성** | 리드타임, 배포 빈도, 온콜 횟수 |
| **품질** | 버그 밀도, 테스트 커버리지, MTTR |
| **규모** | 데이터량, 레코드 수, 쿼리 수 |

---

## 가공 파이프라인 (전체)

```
docs/10-sources/              (raw 인덱스)
        │
        ├─ 수동 큐레이션
        ▼
docs/20-projects/<co>/*.md    (프로젝트별 통합 + STAR + metrics)
        │
        ├─ ③ Skill Mapping
        ▼
docs/30-skills/*.md           (스킬 → 프로젝트 역링크)
        │
        ├─ ④ STAR Extraction
        ▼
docs/40-stories/*.md          (재사용 가능 서사)
        │
        ├─ ② Clustering + ⑤ Metrics top
        ▼
docs/50-portfolio/*.md        (렌더링 산출물)
```

## 분석 체크리스트 (프로젝트당)

- [ ] frontmatter에 `period`, `role`, `tech_stack` 채워짐
- [ ] `sources:`에 최소 2개 이상 증거 링크
- [ ] STAR 섹션 본문 작성
- [ ] `metrics:` 최소 1개 정량 지표
- [ ] 관련 `30-skills/*.md` 3개 이상에 역링크 추가됨
- [ ] `docs/20-projects/<co>/README.md` 타임라인 업데이트
