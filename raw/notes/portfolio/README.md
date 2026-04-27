# Portfolio — 김석근 (gsroot)

커리어/포트폴리오 자료 베이스. 여러 시스템(Jira, Confluence, Google Drive, Gmail, GitHub)에 흩어진 업무 기록을 수집·분석·정리하여 **이직용 이력서, 공개 포트폴리오 사이트, 사내 성과 평가**에 활용 가능한 구조화된 자료로 관리하는 저장소입니다.

## 시작하기

문서의 진입점은 [`docs/README.md`](./docs/README.md)입니다 (🗺️ MOC — Map of Content).

## 저장소 구조 한눈에

```
portfolio/
├── docs/                # 공개 문서 (3-layer + Johnny.Decimal)
│   ├── 00-meta/         # 방법론 (수집/분석/컨벤션/업데이트)
│   ├── 10-sources/      # 원천 자료 인덱스 (Raw Layer)
│   ├── 20-projects/     # 프로젝트 통합 문서 (Synthesis Layer)
│   ├── 30-skills/       # 스킬 → 프로젝트 역매핑
│   ├── 40-stories/      # STAR 스토리 뱅크
│   └── 50-portfolio/    # 최종 산출물 (Output Layer)
├── private/             # 🔒 .gitignore — 로컬 전용 raw 덤프
├── scripts/             # (향후) 수집 자동화
└── old-portfolio.md     # 시드 자료 (참고용 보존)
```

## 핵심 원칙

- **3-Layer**: Raw(`10-sources/`) → Synthesis(`20-*`, `30-*`, `40-*`) → Output(`50-portfolio/`)
- **Public/Private 분리**: 공개 가능한 내용은 `docs/`에, 민감 자료는 `private/`에 (git-ignored)
- **증거 기반**: 모든 프로젝트 문서의 frontmatter `sources:`에 원천 자료 링크
- **업데이트 가능**: 각 Layer 독립적으로 갱신, 단방향 의존(Raw → Synthesis → Output)

## 연락처

- **Email**: gsr2732@gmail.com
- **GitHub**: <https://github.com/gsroot>
- **Blog**: <https://gsroot.tistory.com>
- **LinkedIn**: <https://www.linkedin.com/in/seokgeun-kim-839473285/>

---

상세 방법론은 [`docs/00-meta/`](./docs/00-meta/)를, 현재 진행 상황은 [`docs/README.md`](./docs/README.md)를 참고하세요.
