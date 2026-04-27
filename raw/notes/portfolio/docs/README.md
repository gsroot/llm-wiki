# 📚 Docs — 포트폴리오 오케스트레이션 루트 (MOC)

이 문서는 포트폴리오 자료 베이스의 **네비게이션 허브**(Map of Content)입니다. 각 섹션으로의 진입점과 문서 간 의존 관계를 한눈에 파악할 수 있습니다.

---

## 🗺️ 3-Layer 구조 개요

```
 Raw Layer (수집)           Synthesis Layer (가공)           Output Layer (산출)
┌─────────────────────┐    ┌─────────────────────────┐    ┌─────────────────────┐
│ 10-sources/         │───▶│ 20-projects/            │───▶│ 50-portfolio/       │
│   ├ github-c2spf/   │    │   프로젝트 통합 문서   │    │   ├ resume-ko.md    │
│   ├ jira/           │    │                         │    │   ├ portfolio-ko.md │
│   ├ confluence/     │    │ 30-skills/              │    │   ├ portfolio-en.md │
│   ├ google-drive/   │───▶│   스킬 → 프로젝트 매핑 │───▶│   └ evaluation-kpt  │
│   └ gmail/          │    │                         │    │                     │
│                     │    │ 40-stories/             │    │                     │
│ + private/ (🔒 local)│    │   STAR 스토리 뱅크    │    │                     │
└─────────────────────┘    └─────────────────────────┘    └─────────────────────┘
         ▲
         │
┌────────┴────────────┐
│ 00-meta/            │  방법론 문서 (수집/분석/컨벤션/업데이트)
└─────────────────────┘
```

---

## 📋 섹션 인덱스

### [00-meta/](./00-meta/) — 방법론
문서 체계를 운영하기 위한 메타 문서들입니다. 어떻게 수집하고 분석하고 유지보수할지를 정의합니다.

| 문서 | 설명 |
|------|------|
| [collection-strategy.md](./00-meta/collection-strategy.md) | 소스별 수집 전략 (JQL/CQL/검색쿼리) |
| [analysis-methodology.md](./00-meta/analysis-methodology.md) | 분석 방법론 (STAR, skill mapping, metric 추출) |
| [document-conventions.md](./00-meta/document-conventions.md) | 파일 네이밍, YAML frontmatter 스키마, Markdown 스타일 |
| [update-workflow.md](./00-meta/update-workflow.md) | 주기적 업데이트 절차 (어떻게 최신 상태를 유지할지) |

### [10-sources/](./10-sources/) — 원천 자료 (Raw Layer)
외부 시스템에서 수집한 원천 자료의 **인덱스**. 실제 원본 데이터 중 민감한 것은 `private/`에만 존재.

- [com2us-platform/](./10-sources/com2us-platform/) — 컴투스플랫폼 (현 재직)
  - [github-c2spf/INDEX.md](./10-sources/com2us-platform/github-c2spf/INDEX.md)
  - [jira/INDEX.md](./10-sources/com2us-platform/jira/INDEX.md)
  - [confluence/INDEX.md](./10-sources/com2us-platform/confluence/INDEX.md)
  - [google-drive/INDEX.md](./10-sources/com2us-platform/google-drive/INDEX.md)
  - [gmail/INDEX.md](./10-sources/com2us-platform/gmail/INDEX.md)

### [20-projects/](./20-projects/) — 프로젝트 통합 (Synthesis Layer)
프로젝트 단위로 여러 소스의 증거를 통합한 문서. 각 문서는 frontmatter `sources:`에 원천 링크.

- [com2us-platform/](./20-projects/com2us-platform/) — 타임라인 및 프로젝트별 상세

### [30-skills/](./30-skills/) — 스킬 매핑
스킬 → 이를 증명하는 프로젝트로의 역링크 테이블. 면접/채용 프로세스에서 "이 스킬 경험이 있나요?"에 바로 답할 수 있도록.

### [40-stories/](./40-stories/) — STAR 스토리 뱅크
면접·평가용 STAR(Situation/Task/Action/Result) 포맷 스토리. 리더십/문제해결/임팩트 카테고리별.

### [50-portfolio/](./50-portfolio/) — 최종 산출물 (Output Layer)
용도별 렌더링된 최종 문서.

| 문서 | 용도 |
|------|------|
| [resume-ko.md](./50-portfolio/resume-ko.md) | 이직용 이력서 (한국어, 2 페이지 분량) |
| [portfolio-ko.md](./50-portfolio/portfolio-ko.md) | 상세 포트폴리오 (한국어, `old-portfolio.md` 진화판) |
| [portfolio-en.md](./50-portfolio/portfolio-en.md) | 영문 포트폴리오 (선택 프로젝트) |
| [evaluation-kpt.md](./50-portfolio/evaluation-kpt.md) | 사내 성과/KPT 평가용 |

---

## 🧭 사용 가이드 (역할별)

### 👔 이직 준비 중
1. [50-portfolio/resume-ko.md](./50-portfolio/resume-ko.md) → 이력서 본문
2. [40-stories/](./40-stories/) → 면접 답변 재료
3. [30-skills/](./30-skills/) → "이 스킬 경험?" 질문 대응

### 📝 사내 성과/KPT 작성
1. [50-portfolio/evaluation-kpt.md](./50-portfolio/evaluation-kpt.md)
2. [20-projects/](./20-projects/) → 구체 증거

### 🔄 정기 업데이트
1. [00-meta/update-workflow.md](./00-meta/update-workflow.md) 절차 따라
2. 새 수집 → `10-sources/` 업데이트
3. 새 프로젝트 → `20-projects/` 추가
4. 영향받은 `30-skills/`, `40-stories/` 재생성
5. 마지막으로 `50-portfolio/` 반영

### 🆕 새 회사 추가 시
1. [00-meta/collection-strategy.md](./00-meta/collection-strategy.md) 재사용
2. `10-sources/<company-name>/` 생성
3. `20-projects/<company-name>/` 생성

---

## 📅 현재 진행 상황

| Phase | 상태 | 내용 |
|-------|------|------|
| 0. Foundation | 🚧 진행 중 | 디렉토리 구조, 방법론 문서, 섹션 README |
| A. GitHub c2spf 수집 | ⏳ 대기 | c2spf 조직 레포 목록 및 기여도 |
| B. Jira 수집 | ⏳ 대기 | 최근 3년 JQL 수집 |
| C. Confluence 수집 | ⏳ 대기 | 최근 3년 CQL 수집 |
| D. Google Drive | ⏳ 대기 | 문서/시트 목록 |
| E. Gmail | ⏳ 대기 | 주요 스레드 (민감도 높음) |
| F. Synthesis | ⏳ 대기 | 프로젝트 통합 문서 |
| G. Skills & Stories | ⏳ 대기 | 역매핑 및 스토리 뱅크 |
| H. Final Output | ⏳ 대기 | 렌더링 산출물 |

---

## 🔗 외부 링크

- **사용자 GitHub**: <https://github.com/gsroot>
- **컴투스플랫폼 조직 GitHub**: <https://github.com/c2spf>
- **Blog**: <https://gsroot.tistory.com>
- **LinkedIn**: <https://www.linkedin.com/in/seokgeun-kim-839473285/>

## 📎 시드 자료

[`../old-portfolio.md`](../old-portfolio.md) — 기존 작성된 포트폴리오 문서. 프로젝트 목록/기술 스택의 초기 시드로 사용되며 참고용으로 보존됩니다.
