# Collection Strategy — 자료 수집 전략

각 외부 시스템에서 자료를 수집하기 위한 **쿼리 템플릿**과 **절차**를 정의합니다. 새로운 회사/기간 수집 시 이 문서를 복사해서 재사용합니다.

## 수집 원칙

- **Time window**: 기본 최근 3년 (현재 기준 `2022-01-01`~). 필요 시 확장
- **접근성 순서**: 접근성 좋은 것부터 (GitHub → Jira/Confluence → GDrive → Gmail)
- **민감도 역순**: 민감도 낮은 것부터 (공개 레포 → 업무 티켓 → 이메일)
- **증거 링크 병행**: 수집하면서 `docs/20-projects/<company>/` 의 `sources:` 필드에 링크 기록

---

## 🐙 GitHub (c2spf 조직)

### 수집 도구
- `gh` CLI (인증 필요)
- `mcp__plugin_everything-claude-code_github__*` MCP tools

### 수집 절차

**Step 1 — 조직 레포 목록**
```bash
gh repo list c2spf --limit 200 \
  --json name,description,visibility,isPrivate,primaryLanguage,pushedAt,updatedAt
```

**Step 2 — 내 기여가 있는 레포 식별**
각 레포에 대해:
```bash
gh search commits --author=gsroot --repo=c2spf/<name> \
  --json sha,commit,repository --limit 50
```
커밋 개수 ≥ 1이면 기여 레포로 분류.

**Step 3 — 각 기여 레포 상세**
```bash
# README 스냅샷
gh api repos/c2spf/<name>/readme --jq '.content' | base64 -d > private/github/<name>-README.md

# 내 PR 목록
gh search prs --author=gsroot --repo=c2spf/<name> \
  --json number,title,state,createdAt,closedAt,url
```

**Step 4 — 문서 작성**
- `docs/10-sources/com2us-platform/github-c2spf/INDEX.md` — 전체 레포 테이블
- `docs/10-sources/com2us-platform/github-c2spf/repos/<name>.md` — 주요 레포 상세

### 수집 필드
| 필드 | 예시 | 출처 |
|------|------|------|
| repo_name | `c2spf/analytics-web` | `gh repo list` |
| primary_language | `Python` | `gh repo list` |
| visibility | `private` | `gh repo list` |
| pushedAt | `2026-04-24T10:30:00Z` | `gh repo list` |
| my_commit_count | `42` | `gh search commits --author` |
| my_pr_count | `15` | `gh search prs --author` |
| readme_snapshot | (private) | `gh api repos/.../readme` |

---

## 🎫 Jira (Atlassian)

### 수집 도구
- `mcp__plugin_atlassian_atlassian__*` MCP tools

### 수집 절차

**Step 1 — cloudId 획득**
```
getAccessibleAtlassianResources()
→ response의 id 필드를 cloudId로 사용
```

**Step 2 — 프로젝트 목록 파악**
```
getVisibleJiraProjects(cloudId=..., searchBy="name")
```

**Step 3 — 내 관련 티켓 JQL 검색**
```jql
(assignee = currentUser() OR reporter = currentUser())
AND updated >= "2022-01-01"
ORDER BY updated DESC
```
MCP 호출:
```
searchJiraIssuesUsingJql(cloudId=..., jql="...", nextPageToken=null)
```
페이지네이션 루프 — `nextPageToken` 끝날 때까지.

**Step 4 — 주요 티켓 상세**
Epic/Story 타입 티켓만:
```
getJiraIssue(cloudId=..., issueIdOrKey="ANAP-1234")
```
결과를 `private/jira/<KEY>.md`에 저장.

**Step 5 — 문서 작성**
- `docs/10-sources/com2us-platform/jira/INDEX.md` — 프로젝트별 요약 통계
- `docs/10-sources/com2us-platform/jira/tickets-by-project.md` — 프로젝트별 주요 티켓 테이블

### 수집 필드
| 필드 | 예시 |
|------|------|
| issue_key | `ANAP-1234` |
| summary | "Airbridge 지표 API 설계" |
| issue_type | `Story`, `Task`, `Epic`, `Bug` |
| status | `Done`, `In Progress`, `To Do` |
| project | `ANAP` |
| created | `2025-01-10` |
| updated | `2025-02-28` |
| labels | `["backend", "adtech"]` |

---

## 📖 Confluence (Atlassian)

### 수집 도구
- `mcp__plugin_atlassian_atlassian__*` MCP tools

### 수집 절차

**Step 1 — 스페이스 목록**
```
getConfluenceSpaces(cloudId=..., limit=100)
```

**Step 2 — 내가 생성한 페이지 CQL 검색**
```cql
creator = currentUser() AND lastmodified >= "2022-01-01"
ORDER BY lastmodified DESC
```
MCP:
```
searchConfluenceUsingCql(cloudId=..., cql="...", limit=100)
```

**Step 3 — 주요 페이지 본문 수집**
설계/회고/RFC 문서만 우선:
```
getConfluencePage(cloudId=..., pageId="...")
```
결과를 `private/confluence/<page-id>.md`에 저장.

**Step 4 — 문서 작성**
- `docs/10-sources/com2us-platform/confluence/INDEX.md`
- `docs/10-sources/com2us-platform/confluence/pages-by-space.md`

### 수집 필드
| 필드 | 예시 |
|------|------|
| page_id | `123456789` |
| title | "Airbridge API 설계 RFC" |
| space_key | `AN` |
| space_name | "Analytics" |
| created | `2025-01-15` |
| lastmodified | `2025-02-10` |
| version | `7` |

---

## 💾 Google Drive

### 수집 도구
- `mcp__claude_ai_Google_Drive__*` MCP tools

### 수집 절차

**Step 1 — 최근 파일 목록**
```
list_recent_files(pageSize=100)
```
또는:
```
search_files(
  query="owner:'me' and modifiedTime > '2022-01-01T00:00:00'",
  pageSize=100
)
```

**Step 2 — 문서 타입 필터**
MimeType 필터:
- `application/vnd.google-apps.document` (Docs)
- `application/vnd.google-apps.spreadsheet` (Sheets)
- `application/vnd.google-apps.presentation` (Slides)

**Step 3 — 관련성 판단 후 본문 수집**
```
read_file_content(fileId="...")
```
또는 Markdown으로 export 가능하면:
```
download_file_content(fileId="...", mimeType="text/markdown")
```
결과를 `private/google-drive/<file-id>.md`에 저장.

**Step 4 — 문서 작성**
- `docs/10-sources/com2us-platform/google-drive/INDEX.md`

### 수집 필드
| 필드 | 예시 |
|------|------|
| file_id | `1AbC...XyZ` |
| name | "2024 Q4 회고" |
| mimeType | `application/vnd.google-apps.document` |
| createdTime | `2024-10-05T02:30:00Z` |
| modifiedTime | `2024-12-28T08:15:00Z` |
| webViewLink | `https://docs.google.com/document/d/...` |

---

## ✉️ Gmail

### 수집 도구
- `mcp__claude_ai_Gmail__*` MCP tools

### 수집 절차

🔒 **민감도 최상**: 이메일은 PII와 사내 기밀 포함 가능. 요약 외 원본 저장은 `private/`만.

**Step 1 — 목적별 쿼리**
```
search_threads(q="from:me OR to:me (회고 OR 평가 OR 리뷰 OR 성과) after:2022/01/01", maxResults=50)
search_threads(q="(프로젝트 완료 OR 릴리즈 OR 배포 공지) after:2022/01/01", maxResults=50)
search_threads(q="(피드백 OR 칭찬 OR 감사) after:2022/01/01", maxResults=30)
```

**Step 2 — 주요 스레드 본문**
```
get_thread(threadId="...")
```
결과를 `private/gmail/<thread-id>.md`에 저장.

**Step 3 — 요약만 공개 인덱스에**
`docs/10-sources/com2us-platform/gmail/INDEX.md`에는 **제목, 날짜, 관련 프로젝트 태그, 스레드 ID**만. 본문 인용 금지.

### 수집 필드 (공개 인덱스)
| 필드 | 예시 |
|------|------|
| thread_id | `1815a7...` (링크만) |
| subject | "Airbridge API 릴리즈 공지" |
| date | `2025-02-28` |
| related_project | `2025-01-airbridge-api` |
| tags | `["release", "retrospective"]` |

---

## 수집 체크리스트 (신규 회사/기간 추가 시)

- [ ] `docs/10-sources/<company>/` 디렉토리 생성 + README
- [ ] GitHub: 조직명 확인 → 레포 목록 수집
- [ ] Jira: cloudId 확인 → JQL 실행
- [ ] Confluence: 스페이스 목록 확인 → CQL 실행
- [ ] Google Drive: 날짜 필터 검색 실행
- [ ] Gmail: 목적별 쿼리 3종 실행
- [ ] 각 소스 INDEX.md 작성
- [ ] 주요 자료 `private/`에 저장
- [ ] `docs/20-projects/<company>/README.md`에 타임라인 반영
