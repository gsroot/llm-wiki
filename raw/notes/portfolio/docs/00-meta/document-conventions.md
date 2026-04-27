# Document Conventions — 문서 작성 규칙

이 저장소의 **모든 Markdown 문서**가 따라야 할 네이밍·구조·링크 규칙입니다.

## 1. 파일 네이밍

### 디렉토리
- `NN-<kebab-case>/` — `00-meta/`, `10-sources/`, `20-projects/` 등 2자리 번호 접두사
- 회사명은 소문자 kebab-case: `com2us-platform/`, `zuminternet/`

### 문서 파일
- `README.md` — 디렉토리의 진입점. 필수. 하위 파일 인덱스 역할
- `INDEX.md` — `10-sources/`의 소스별 자료 인덱스 (테이블 + 메타만)
- `YYYY-MM-<slug>.md` — `20-projects/` 의 프로젝트 문서 (예: `2025-06-analytics-react-renewal.md`)
- `<skill-category>.md` — `30-skills/` (예: `backend-python.md`)
- `<category>-<slug>.md` — `40-stories/` (예: `leadership-react-adoption.md`)
- `<kebab-case>.md` — 기타

---

## 2. YAML Frontmatter Schema

### 필수 필드 (type별)

#### `type: project` (20-projects/)
```yaml
---
title: "애널리틱스 서비스 React 기반 리뉴얼"
type: project
company: com2us-platform
period: "2025-06 ~ 현재"                 # "YYYY-MM ~ YYYY-MM" 또는 "YYYY-MM ~ 현재"
role: "프론트엔드 리드, 풀스택 개발"     # 쉼표 구분
tech_stack:                              # YAML list
  - React
  - TypeScript
  - ag-grid
  - FastAPI
  - MySQL
  - Redis
  - BigQuery
  - Docker
  - Jenkins
sources:
  jira: ["private/jira/ANAP-1234.md", "private/jira/ANAP-1235.md"]
  confluence:
    - "https://<org>.atlassian.net/wiki/spaces/AN/pages/123"
  github:
    - "https://github.com/c2spf/<repo>"
  gdrive: ["private/google-drive/<file-id>.md"]
  gmail: ["private/gmail/<thread-id>.md"]
tags: [frontend, react, architecture, refactoring]
metrics:
  - "프론트엔드 개발 리드타임 30~40% 감소 기반 구축"
related_projects:
  - "2025-01-airbridge-api"
  - "2024-08-analytics-common-module"
star:
  situation: "한 문장 요약"
  task: "한 문장 요약"
  action: "한 문장 요약"
  result: "한 문장 요약"
---
```

#### `type: skill` (30-skills/)
```yaml
---
title: "Backend — Python"
type: skill
category: backend
slug: backend-python
years_of_experience: 9
proficiency: expert      # novice | advanced-beginner | competent | proficient | expert
related_stack:
  - FastAPI
  - Django
  - Flask
  - SQLAlchemy
  - Pytest
tags: [python, backend, async, api]
---
```

#### `type: story` (40-stories/)
```yaml
---
title: "팀 최초 React 도입을 주도한 경험"
type: story
category: leadership      # leadership | problem-solving | impact | learning
period: "2025-06 ~ 현재"
primary_project: "2025-06-analytics-react-renewal"
tags: [frontend, architecture, tech-leadership]
skills_demonstrated:
  - frontend-react
  - devops-container
---
```

#### `type: source-index` (10-sources/)
```yaml
---
title: "컴투스플랫폼 GitHub c2spf 조직 레포 인덱스"
type: source-index
company: com2us-platform
source: github
collected_at: "2026-04-24"      # ISO 8601 date
---
```

---

## 3. 링크 규칙

### 상대 경로 우선
같은 저장소 내부 링크는 **상대 경로**. GitHub 웹 뷰와 로컬 에디터 모두 동작.
```markdown
좋음: [Airbridge API](../20-projects/com2us-platform/2025-01-airbridge-api.md)
나쁨: [Airbridge API](/docs/20-projects/com2us-platform/2025-01-airbridge-api.md)
```

### 디렉토리 링크는 끝에 `/`
```markdown
좋음: [00-meta/](./00-meta/)
나쁨: [00-meta](./00-meta)
```

### 외부 링크는 꺽쇠 또는 inline
```markdown
<https://github.com/c2spf>      # URL 그대로 표시
[c2spf](https://github.com/c2spf) # 텍스트 링크
```

### Frontmatter `sources:` 필드는 **경로 또는 URL 문자열**
- 로컬 private 참조: `"private/jira/ANAP-1234.md"` (프로젝트 루트 기준)
- 외부 URL: `"https://..."`

---

## 4. 날짜·기간 표기

| 상황 | 포맷 | 예시 |
|------|------|------|
| 특정 월 | `YYYY-MM` | `2025-06` |
| 기간 | `"YYYY-MM ~ YYYY-MM"` | `"2024-04 ~ 2024-07"` |
| 진행 중 | `"YYYY-MM ~ 현재"` | `"2025-06 ~ 현재"` |
| 수집 시점 타임스탬프 | ISO 8601 | `"2026-04-24"` 또는 `"2026-04-24T10:30:00Z"` |

Output 문서(`50-portfolio/`)는 독자에 따라 `2025.06 ~ 현재` 같은 대시+닷 표기도 허용.

---

## 5. Markdown 스타일

- 헤딩 레벨: `#` 제목은 문서당 1개. 본문은 `##`부터
- 테이블: 3열 이상일 때 권장, 1~2열은 리스트
- 코드 블록: 언어 태그 필수 (` ```python `, ` ```bash `, ` ```yaml `)
- 이모지: 섹션 시각 구분용만 제한적 사용 (📚 🔒 🚧 ✅)
- 줄바꿈: 빈 줄 하나로 단락 구분. 강제 줄바꿈(`<br>`) 지양

---

## 6. `private/` 참조 규칙

- `private/`는 `.gitignore` 됨. 로컬에만 존재
- `sources:` 필드에서 경로로 참조 OK (로컬에서는 열림)
- Output(`50-portfolio/`)은 **`private/` 경로를 직접 인용하지 않음**. 필요하면 요약만 옮김
- 민감정보(PII, 급여, 비공개 전략) 인용 금지

---

## 7. 커밋 메시지 (선택)

일반 `feat/fix/docs/chore` 규약 따름. 특히:
- `docs(<layer>): <요약>` — 예: `docs(20-projects): add 2025-06 React renewal`
- `data(sources): collect jira 2022-2025 tickets`
- `meta: update collection strategy for confluence`
