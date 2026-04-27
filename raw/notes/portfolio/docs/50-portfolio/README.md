# 50-portfolio — 최종 산출물 (Output Layer)

**Output Layer**: 용도별로 **렌더링된 최종 포트폴리오 문서**들. 여기 오는 내용은 모두 `10-sources/`, `20-projects/`, `30-skills/`, `40-stories/`에서 **파생된 것**이며, 원천이 없는 정보는 포함하지 않음.

## 산출물 목록

| 파일 | 용도 | 타겟 독자 | 분량 |
|------|------|----------|------|
| `resume-ko.md` | 이직용 이력서 | 한국 채용담당자/리크루터 | 2 페이지 |
| `portfolio-ko.md` | 상세 포트폴리오 | 한국 기술 면접관 | 무제한 (`old-portfolio.md` 진화판) |
| `portfolio-en.md` | 영문 포트폴리오 | 해외/외국계 채용담당자 | 2~4 페이지 |
| `evaluation-kpt.md` | 사내 성과 정리 | 팀장/상급자 (KPT/연말 평가) | 1~2 페이지 |

## 작성 원칙

1. **원천 참조**: 모든 주장은 `../20-projects/` 또는 `../40-stories/` 링크로 뒷받침
2. **정량 우선**: 정성 표현보다 정량 지표 우선
3. **독자 맞춤**:
   - `resume-ko.md` — 스캔하듯 훑기 좋은 구조, 굵은 글씨 3~5개
   - `portfolio-ko.md` — 기술적 깊이, 의사결정 이유, 트레이드오프 설명
   - `portfolio-en.md` — 간결, 문화 중립, 성과 중심
   - `evaluation-kpt.md` — KPT(Keep/Problem/Try) 구조 또는 성과/과제/성장
4. **개인정보**: 전화번호/주소/주민번호 금지. 이메일/GitHub/LinkedIn만
5. **업데이트**: 대규모 개정은 연 1~2회. 타이틀·기간만 자주 갱신
6. **`private/` 인용 절대 금지** — Output 레이어는 공개 가능한 자료 베이스

## 렌더링 워크플로우

```
20-projects/ + 30-skills/ + 40-stories/
              │
              ├─ 선별 (이직/사내/영문 등 용도별)
              │
              ▼
    50-portfolio/<target>.md
              │
              └─ 용도별 편집 (분량, 톤)
```

## 초안 작성 우선순위

1. `portfolio-ko.md` — `old-portfolio.md` 시드 기반, 최근 프로젝트 업데이트
2. `resume-ko.md` — `portfolio-ko.md` 축약
3. `evaluation-kpt.md` — 가장 최근 1년 성과 추출
4. `portfolio-en.md` — 완성도 있는 한국어 버전 번역

## 버전 관리 (선택)

대규모 개정 시 버전 태그:
```
resume-ko.md              # 현재
resume-ko-2026-spring.md  # 아카이브
```
