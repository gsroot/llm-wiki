# 00-meta — 방법론

이 섹션은 포트폴리오 자료 베이스를 **어떻게 수집/분석/유지보수**할지를 정의합니다. 다른 섹션의 문서들은 여기 정의된 규칙을 따릅니다.

## 문서 구성

| 문서 | 언제 참조 |
|------|-----------|
| [collection-strategy.md](./collection-strategy.md) | 새로운 소스에서 자료를 수집할 때. Jira/Confluence/GDrive/Gmail/GitHub 각 소스별 쿼리 템플릿과 절차. |
| [analysis-methodology.md](./analysis-methodology.md) | 수집된 raw 자료를 synthesized 문서로 가공할 때. STAR 스토리 추출, 스킬 매핑, 정량 지표 추출 방법. |
| [document-conventions.md](./document-conventions.md) | 새 문서를 작성할 때. 파일 네이밍, YAML frontmatter 스키마, 링크 규칙, 날짜/기간 표기. |
| [update-workflow.md](./update-workflow.md) | 주기적 업데이트·재생성 시. 각 Layer별 갱신 트리거와 체크리스트. |

## 원칙

1. **Raw is Raw, Synthesis is Synthesis**: Raw Layer(`10-sources/`)에 가공 내용을 쓰지 않는다. 요약이나 분석이 필요하면 Synthesis Layer에.
2. **Single Source of Truth per Fact**: 하나의 사실은 하나의 문서에만. 다른 문서는 링크로만 참조.
3. **Progressive Disclosure**: 상위 문서(README/INDEX)는 개요와 링크만, 세부는 하위 문서에.
4. **Update in Dependency Order**: Raw → Synthesis → Output. 역방향 수정 금지.
5. **Privacy by Default**: 민감도 판단이 애매하면 `private/`에.
