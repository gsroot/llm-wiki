# Update Workflow — 주기적 업데이트 절차

포트폴리오는 **살아있는 문서**입니다. 수동 큐레이션이 필요한 자료 베이스이므로, 정기 업데이트 루틴을 정의합니다.

## 업데이트 주기

| 주기 | 트리거 | 작업 |
|------|--------|------|
| **실시간** | 새 프로젝트 시작 | `20-projects/` 스텁 추가, 기간·기술스택만 초기 기입 |
| **주간** | 매주 금요일 (또는 프로젝트 마일스톤) | 이번 주 Jira 티켓 중 중요한 것 `private/jira/`에 저장 |
| **월간** | 매월 말 | `10-sources/` 인덱스 새로 수집된 자료로 갱신 |
| **분기** | Q 종료 후 1주 | 완료된 프로젝트를 `20-projects/`에 상세 작성, STAR 1~3개 추출 |
| **반기** | 6개월마다 | `30-skills/`, `40-stories/` 재계산 |
| **연간** | 연말 또는 이직 준비 시작 시 | `50-portfolio/` 전면 개정 |

---

## 📅 업데이트 사이클 (Layer별)

```
 Raw         Synthesis      Output
  │            │              │
주간 ─────▶    │              │   (10-sources 인덱스 쌓기)
             월간 ─────▶      │   (20-projects 상세 작성)
                         분기 ─▶   (30-skills/40-stories 갱신)
                                  반기/연간 ─▶ (50-portfolio 재생성)
```

의존 방향은 단방향이다: **Raw → Synthesis → Output**. 역방향 수정 금지.

---

## 🔁 업데이트 체크리스트

### 주간 체크리스트 (금요일)
- [ ] 이번 주 완료/진행 중인 Jira 티켓 중 주목할 것 선별
- [ ] 주요 Confluence 페이지 변경 기록
- [ ] GitHub 주간 PR 활동 빠르게 스캔
- [ ] `private/jira/` 또는 `private/confluence/`에 필요시 저장
- [ ] (옵션) 주간 회고 1줄을 해당 프로젝트 문서에 추가

### 월간 체크리스트 (말일)
- [ ] `docs/10-sources/<company>/` 각 INDEX.md 새 항목 추가
- [ ] 프로젝트 종료된 것이 있다면 `20-projects/` 제목 상태 업데이트
- [ ] `period:` 필드 "현재" → 종료 월로 변경
- [ ] `docs/README.md` "현재 진행 상황" 표 상태 업데이트

### 분기 체크리스트
- [ ] 이번 분기 완료 프로젝트의 `20-projects/` 문서 **완성**:
  - [ ] frontmatter 전 필드 채움
  - [ ] STAR 섹션 본문 작성
  - [ ] `metrics:` 정량 지표 1개 이상
  - [ ] `sources:` 증거 링크 2개 이상
- [ ] 분기 내 언급된 새 스킬이 있다면 `30-skills/` 신규 문서
- [ ] 특별한 성취가 있다면 `40-stories/` 신규 스토리

### 반기 체크리스트
- [ ] `30-skills/*.md` 전체 review
  - [ ] 각 스킬의 프로젝트 테이블 최신화
  - [ ] `years_of_experience` 증가 반영
  - [ ] 숙련도(`proficiency`) 재평가
- [ ] `40-stories/` 전체 review
  - [ ] 중복 스토리 통합
  - [ ] 오래되어 가치 감소한 스토리는 보관(archive) 태그

### 연간/이직 준비 체크리스트
- [ ] `50-portfolio/resume-ko.md` 재작성 (최근 3년 기준)
- [ ] `50-portfolio/portfolio-ko.md` 대대적 리프레시
- [ ] `50-portfolio/portfolio-en.md` 번역 업데이트
- [ ] `50-portfolio/evaluation-kpt.md` 연간 성과로 재정렬
- [ ] `README.md` 저장소 소개 문구 최신화

---

## 🆕 새 회사 추가 플로우

퇴사·이직 시:

1. **이전 회사 아카이빙**
   - `20-projects/<prev-company>/` 는 그대로 유지 (과거 이력)
   - `README.md`에 "전 회사" 표기

2. **새 회사 디렉토리 생성**
   ```
   docs/10-sources/<new-company>/
     README.md, github-*/, jira/, confluence/, ...
   docs/20-projects/<new-company>/
     README.md
   ```

3. **collection-strategy.md 재사용**
   - 소스별 쿼리 템플릿 그대로 적용
   - 회사 고유의 도구(예: Notion, GitLab)가 있다면 `collection-strategy.md`에 섹션 추가

4. **Skills·Stories 연결**
   - `30-skills/`는 회사 가리지 않음. 새 프로젝트가 기존 스킬 테이블에 행 추가
   - `40-stories/`도 회사 무관. `primary_project` 필드만 새 회사 프로젝트로

---

## 🧹 정리·아카이빙

### 오래된 자료
- 5년 이상 된 Raw 자료 → 압축 후 `private/archive/<YYYY>/`로 이동
- `10-sources/` INDEX 에서는 링크는 유지하되 "(archived)" 표기

### 사용하지 않는 스킬
- 1년 이상 사용 안 한 스킬 → `30-skills/` 문서 유지하되 `proficiency: rusty` 또는 삭제
- `old-portfolio.md`와 달리 최신 이력서는 활성 스킬만 노출

---

## 🔧 도구/자동화 (향후)

현재는 전부 수동 큐레이션. 자동화 가능한 부분:

- `scripts/collect_github.py` — c2spf 레포 목록 + 내 기여도 자동 수집 → `INDEX.md` 재생성
- `scripts/collect_jira.py` — JQL 실행 + `private/jira/` 업데이트
- `scripts/validate_frontmatter.py` — 모든 `20-projects/*.md` 의 frontmatter 스키마 검증
- `scripts/build_skill_matrix.py` — `20-projects/` 전체 스캔 → `30-skills/`의 프로젝트 테이블 자동 재생성

이들 스크립트는 **필요해지기 전까지 작성하지 않음** (YAGNI). 수동 루틴에서 병목이 생기면 그때 자동화.
