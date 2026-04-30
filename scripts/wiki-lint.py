#!/usr/bin/env python3
"""wiki-lint.py — llm-wiki 정합성 검증 + source_count 자동 갱신.

CLAUDE.md "점검(Lint) 워크플로우" 자동화 도구. 32회차에 P1-7+P1-8 통합으로 신설.

USAGE:
    python3 scripts/wiki-lint.py [--check] [--update] [--report] [--quiet]

MODES (조합 가능):
    --check    (default) 모든 검증을 실행, 결함 리포트 출력, 결함 발견 시 exit 1
    --update   source_count 부정합을 frontmatter에서 자동 수정 (in-place)
    --report   인바운드 분포 / 5축 통계 / 빈약 페이지 상세 보고서 출력
    --quiet    문제만 출력, 통과한 검사는 침묵

CHECKS:
    1. 깨진 위키링크 (의도된 예시 화이트리스트 적용)
    2. 고아 페이지 (rag_exclude redirect 별도 집계)
    3. frontmatter YAML invalid (PyYAML 파싱 실패)
    4. source_count 부정합 (frontmatter source_count vs 실제 wiki/sources/ 인용 카운트)
       — 정보 보고. delta ±10 이상이면 운영자 의미 재검토 권장.
    5. 빈약 페이지 (source_count >= 3 인데 본문 < 30줄)
    6. source_scope 부재 결함 (33회차): source_url=="" 인데 source_scope 누락 시 결함
    7. last_verified 신선도 경고 (33회차): verification_required=true 페이지의 last_verified가
       90일 초과 시 경고 (결함 아닌 정보 보고)
    8. 태그 case-duplicate 회귀 검출 (36회차): 같은 태그의 대소문자 변형이 동시 존재
       (예: Anthropic + anthropic, llm + LLM). 34회차 정규화의 회귀 방지.
    9. 한영 병기 의무 위반 검출 (36회차): CLAUDE.md 31회차 4단계 규칙의 "개념·도메인 태그"
       카테고리(agent/에이전트 등) 한쪽만 있으면 경고.
    10. 메타 페이지 rag_exclude 누락 결함 (43회차): type=index 또는 type=log 페이지에
        rag_exclude:true가 없으면 결함. RAG 답변 근거로 메타 페이지가 혼입되는 위험 차단.
    11. 본문 정량 stale 경고 (49회차): 본문 [[페이지]](N) 패턴이 자동 측정 inbound와
        |delta| >= 5 이고 시점 라벨(28회차/스냅샷/당시 등)이 같은 줄에 없을 때 정보 보고.
    12. stub entity 결함 검출 (51회차 신설 — 평가 P0-5 채택): type=entity 인데 본문<25줄
        AND source_count==0 AND inbound>0 AND entity_type!=redirect 이면 결함.
        canonical 충돌 stub(예: 표기 변종) 회귀 차단. mate-chat 같은 redirect 후보가
        entity_type=tool 또는 project로 남아 있는 위험 검출.
    13. 인바운드 분포 보고 (5축 hub 합산 / 전체 인바운드 분포)

SCHEMA (43회차 — source_count 3분리):
    - source_count: 운영자 수동 정의 (정의 A, frontmatter)
    - observed_source_refs: source 페이지가 wikilink로 인용한 횟수 (정의 B, --update가 갱신)
    - inbound_count: 모든 페이지가 wikilink로 인용한 횟수 (정의 C, --update가 갱신)
    --update 모드는 자동 필드 두 개만 갱신하고 source_count는 절대 덮어쓰지 않는다.

EXIT CODES:
    0   결함 없음 (또는 --report 단독 모드)
    1   결함 발견
    2   사용 오류 (인자 / 환경 문제)

이 스크립트는 표준 라이브러리 + PyYAML만 의존한다. wiki/ 디렉토리 외부 파일은 수정하지 않는다.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import date, datetime
from pathlib import Path

import yaml


STALE_VERIFICATION_DAYS = 90  # last_verified 경고 임계
VALID_SOURCE_SCOPES = frozenset({"local", "private", "public"})

# 51회차 P0-3 신설: cited_by 비대화 완화 임계값
# cited_by 항목 수가 이 값 이상이면 frontmatter list 대신 본문 ## 인용한 페이지 섹션으로
# 이동하고 frontmatter에는 `cited_by_count: N`만 박는다. RAG 첫 청크의 의미 신호 손실 방지.
CITED_BY_FRONTMATTER_THRESHOLD = 40
CITED_BY_BODY_HEADER = "## 인용한 페이지 (cited_by — 51회차 자동 갱신)"

# 36회차 신설 → 59회차 deprecated: 한국어+영어 병기 의무 (옵션 A 정책 전환으로 폐기)
# CLAUDE.md 59회차 옵션 A: tags는 canonical 1개, 표기 변종은 aliases.
# 본 검증은 비활성화 (빈 튜플) — check #14가 canonical 회귀 차단을 대신 담당.
KO_EN_PAIRS: tuple[tuple[str, str], ...] = ()

# 36회차 신설: case-duplicate 검증에서 정상 케이스(영어 단독 약어)는 제외
# 이 화이트리스트의 태그는 대소문자 변형이 있어도 정상 (예: AI는 약어로 영어 단독)
CASE_DUPLICATE_WHITELIST: frozenset[str] = frozenset({
    # 현재는 비어있음. 회귀 발생 시 의도된 케이스만 등록.
})


WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"

WIKILINK_RE = re.compile(r"\[\[([^]|#]+?)(?:\||#|\])")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SOURCE_COUNT_LINE_RE = re.compile(r"^source_count:\s*\d+\s*$", re.MULTILINE)
OBSERVED_REFS_LINE_RE = re.compile(r"^observed_source_refs:\s*\d+\s*$", re.MULTILINE)
INBOUND_COUNT_LINE_RE = re.compile(r"^inbound_count:\s*\d+\s*$", re.MULTILINE)
CITED_BY_KEY_RE = re.compile(r"^cited_by:\s*$", re.MULTILINE)

# 의도된 예시 텍스트로 위키링크 형태를 사용한 케이스 (깨진 링크 false positive 제외)
EXAMPLE_TARGETS: frozenset[str] = frozenset(
    {
        "a",
        "b",
        "c",
        "kebab-case",
        "code-reviewer",
        "frontend-flutter-stack",
        "frontend-react-stack",
        "wikilink",
        "위키링크",
        "대상",
        "파일명",
        "프로젝트 허브",
        "프로젝트 - 결제 개선",
        # 코드 표현 안의 [[...]] false positive (Python 리스트, escape 잔재 등)
        '"user_id", "revenue"',
        '"revenue", "ma7"',
        "lazy-evaluation\\",
    }
)

# 5축 hub 페이지 분류 (인바운드 분포 측정용)
AXES: dict[str, list[str]] = {
    "1축 개인 프로필": [
        "seokgeun-kim",
        "seokgeun-operating-profile-2026",
        "career-timeline-seokgeun",
        "seokgeun-kim-profile-2026",
    ],
    "2축 포트폴리오": [
        "portfolio-seed",
        "portfolio-resume-ko",
        "portfolio-ko",
        "portfolio-method",
        "c2spf-analytics",
        "c2spf-nft-market",
        "c2spf-xpla-platform",
        "c2spf-analytics-common",
        "c2spf-analytics-renewal",
    ],
    "3축 스택 가이드": ["seokgeun-stack-guide"],
    "4축 MateChat": [
        "matechat",
        "seokgeun-mate-chat",
        "seokgeun-matechat-validation",
        "matechat-chat-analysis-module",
        "matechat-project-knowledge-map",
    ],
    "5축 LLM 인프라 메타": [
        "llm-infra-meta-cluster",
        "agent-skills",
        "harness",
        "mcp",
        "claude-code",
    ],
}

# 49회차 P0-5 신설: 본문 정량 stale 경고
# 본문에 박힌 `[[페이지명]](N)` 또는 `[[페이지명]](N, 1위)` 패턴이
# 자동 측정 inbound와 delta가 크면 stale 가능성. 결함 아닌 정보 보고.
BODY_STALE_INBOUND_RE = re.compile(
    r"\[\[([a-z0-9][a-z0-9-]*)(?:\|[^\]]+)?\]\]\((\d+)(?:,\s*\d+위)?\)"
)
# 시점 라벨이 있는 줄은 의도된 역사 기록 — 검사 제외.
SNAPSHOT_LABEL_KEYS: tuple[str, ...] = (
    "회차 시점",
    "회차 측정",
    "당시",
    "스냅샷",
    "역사 기록",
    "시점 인바운드",
    "시점 스냅샷",
)
# delta 임계 — 이 이상 차이나면 정보 보고.
BODY_STALE_DELTA_THRESHOLD: int = 5
# 인바운드 통계 추정 상한 — body_value가 이보다 크면 연도·금액 등으로 간주, 검사 제외.
# 위키 인바운드 현실적 최대값은 200대(agent-skills 등). 500 상한이면 충분한 안전 마진.
BODY_STALE_VALUE_CEILING: int = 500


@dataclass
class WikiPage:
    """위키 페이지의 파싱 결과."""

    path: Path
    stem: str
    raw: str
    frontmatter: dict | None
    body: str
    yaml_invalid: bool = False
    yaml_error: str | None = None

    @property
    def is_log_file(self) -> bool:
        return "logs/" in str(self.path)

    @property
    def is_redirect(self) -> bool:
        if not self.frontmatter:
            return False
        return self.frontmatter.get("entity_type") == "redirect"

    @property
    def is_rag_excluded(self) -> bool:
        if not self.frontmatter:
            return False
        return bool(self.frontmatter.get("rag_exclude", False))

    @property
    def page_type(self) -> str | None:
        if not self.frontmatter:
            return None
        return self.frontmatter.get("type")

    @property
    def declared_source_count(self) -> int | None:
        if not self.frontmatter:
            return None
        sc = self.frontmatter.get("source_count")
        return sc if isinstance(sc, int) else None

    @property
    def body_line_count(self) -> int:
        return self.body.count("\n") + 1


@dataclass
class LintResult:
    """검증 결과 누적."""

    pages: list[WikiPage] = field(default_factory=list)
    broken_links: list[tuple[str, str]] = field(default_factory=list)
    orphan_pages: list[str] = field(default_factory=list)
    redirect_pages: list[str] = field(default_factory=list)
    yaml_invalid: list[tuple[str, str]] = field(default_factory=list)
    source_count_mismatch: list[tuple[str, int, int]] = field(default_factory=list)
    thin_pages: list[tuple[str, int, int]] = field(default_factory=list)
    # 33회차 신설
    source_scope_missing: list[str] = field(default_factory=list)
    source_scope_invalid: list[tuple[str, str]] = field(default_factory=list)
    stale_verification: list[tuple[str, str, int]] = field(default_factory=list)
    verification_malformed: list[tuple[str, str]] = field(default_factory=list)
    # 36회차 신설
    tag_case_duplicates: list[tuple[str, str, int, int]] = field(default_factory=list)
    tag_pair_violations: list[tuple[str, str, list[str]]] = field(default_factory=list)
    inbound: dict[str, int] = field(default_factory=dict)
    # 43회차 신설: 메타 페이지 rag_exclude 누락 결함
    meta_rag_exclude_missing: list[tuple[str, str]] = field(default_factory=list)
    # 49회차 P0-5 신설: 본문 정량 stale 경고 (정보 보고, 결함 아님)
    # (page_stem, target_stem, body_value, observed_value, delta)
    body_stale_numbers: list[tuple[str, str, int, int, int]] = field(
        default_factory=list
    )
    # 51회차 P0-5 신설: stub entity 결함
    # (rel_path, body_lines, source_count, inbound)
    stub_entities: list[tuple[str, int, int, int]] = field(default_factory=list)
    # 57회차 P0-5 신설 (check #14): cited_by_count 누락 비-메타 페이지 (정보 보고)
    # 53회차 정책 정합화 — 비-메타 페이지에 정수 캐시 일관 적용 강제 안 하지만
    # 미적용은 정보 보고로 가시화하여 --update 실행을 권장.
    cited_by_count_missing: list[str] = field(default_factory=list)
    # 59회차 P0-2 신설 (check #14): 한·영 tag canonical 위반 (회귀 차단)
    # CLAUDE.md 59회차 옵션 A 정책 위반 자동 보고. 결함.
    # (rel_path, demoted_tag, canonical_tag)
    tag_canonical_violations: list[tuple[str, str, str]] = field(default_factory=list)

    def has_defect(self) -> bool:
        # source_count 부정합은 결함이 아닌 정보 보고로 격하 (32회차 발견):
        # 43회차에 source_count(정의 A, 수동) / observed_source_refs(정의 B, 자동) /
        # inbound_count(정의 C, 자동) 3분리로 의미 충돌 해소 (CLAUDE.md 참조).
        # last_verified 신선도(90일 초과)도 정보 보고. source_scope 부재/이상은 결함.
        # 36회차: tag_case_duplicates도 결함 (회귀 방지). tag_pair_violations는 경고(정보).
        # 43회차: meta_rag_exclude_missing 결함 (RAG 답변 근거 노이즈 차단).
        # 51회차: stub_entities 결함 (canonical 충돌 stub 회귀 차단).
        return bool(
            self.broken_links
            or self.yaml_invalid
            or self.source_scope_missing
            or self.source_scope_invalid
            or self.verification_malformed
            or self.tag_case_duplicates
            or self.meta_rag_exclude_missing
            or self.stub_entities
            or self.tag_canonical_violations
        )


def discover_pages() -> list[Path]:
    return sorted(WIKI_ROOT.rglob("*.md"))


def parse_page(path: Path) -> WikiPage:
    raw = path.read_text(encoding="utf-8")
    stem = path.stem
    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        return WikiPage(
            path=path,
            stem=stem,
            raw=raw,
            frontmatter=None,
            body=raw,
            yaml_invalid=True,
            yaml_error="frontmatter 부재",
        )
    fm_text = fm_match.group(1)
    body = raw[fm_match.end():]
    try:
        fm = yaml.safe_load(fm_text) or {}
        if not isinstance(fm, dict):
            return WikiPage(
                path=path,
                stem=stem,
                raw=raw,
                frontmatter=None,
                body=body,
                yaml_invalid=True,
                yaml_error=f"frontmatter가 dict 아님: {type(fm).__name__}",
            )
        return WikiPage(path=path, stem=stem, raw=raw, frontmatter=fm, body=body)
    except yaml.YAMLError as exc:
        return WikiPage(
            path=path,
            stem=stem,
            raw=raw,
            frontmatter=None,
            body=body,
            yaml_invalid=True,
            yaml_error=str(exc).split("\n", 1)[0],
        )


def collect_wikilinks(text: str) -> list[str]:
    return [m.group(1).strip() for m in WIKILINK_RE.finditer(text)]


def lint(update: bool = False) -> LintResult:
    paths = discover_pages()
    pages = [parse_page(p) for p in paths]
    stems = {p.stem for p in pages}

    result = LintResult(pages=pages)

    inbound: dict[str, int] = {p.stem: 0 for p in pages}
    source_count_observed: dict[str, int] = {p.stem: 0 for p in pages}
    # 47회차 신설: cited_by_map[source_stem] = sorted list of citing page stems
    sources_set = {p.stem for p in pages if p.page_type == "source"}
    # 48회차 P1-6: cited_by 자동 갱신 대상을 5축 hub 11개로 확장
    # entity/concept 전체에 박으면 frontmatter 폭증 → hub만 선별 적용
    HUB_CITED_BY_TARGETS = {
        "seokgeun-kim", "portfolio", "seokgeun-stack-guide", "matechat",
        "llm-infra-meta-cluster", "agent-skills", "harness", "mcp",
        "claude-code", "c2spf-analytics", "com2us-platform",
    }
    cited_by_targets = sources_set | (HUB_CITED_BY_TARGETS & {p.stem for p in pages})
    cited_by_map: dict[str, set[str]] = {s: set() for s in cited_by_targets}

    # 57회차 P0-3 신설 (56회차 4축 평가 합집합 Critical):
    # cited_by_count(정수)를 모든 비-메타 페이지(entity/concept/synthesis)에 일관 적용.
    # cited_by(전체 list)는 frontmatter 폭증 위험으로 sources + 11 hub 한정 유지.
    # 정수만 박는 cited_by_count는 RAG 답변 정책 §1 "수치 비교"의 신뢰도 가중치 캐시로,
    # 51회차 정책의 LLM 일관 적용을 위해 비-메타 194페이지 전체로 측정 갭 해소.
    cited_by_count_targets = {
        p.stem for p in pages
        if p.page_type in ("entity", "concept", "synthesis")
        and not p.is_redirect
        and not p.is_log_file
        and p.stem not in cited_by_targets  # 11 hub + sources는 _update_cited_by가 이미 처리
    }
    cited_by_count_map: dict[str, set[str]] = {s: set() for s in cited_by_count_targets}

    for page in pages:
        if page.yaml_invalid:
            result.yaml_invalid.append(
                (str(page.path.relative_to(WIKI_ROOT.parent)), page.yaml_error or "?")
            )
            continue

        if page.is_redirect:
            result.redirect_pages.append(page.stem)

        # log/index-history 회고 텍스트 안의 [[a]]/[[b]] 같은 예시 위키링크는 검증 제외
        is_history = page.stem in {"log", "index-history"}

        for target in collect_wikilinks(page.raw):
            if target == page.stem:
                continue
            if target in stems:
                inbound[target] = inbound.get(target, 0) + 1
                # source_count 측정: source 페이지가 entity/concept를 인용하는 경우만
                if page.page_type == "source":
                    source_count_observed[target] = (
                        source_count_observed.get(target, 0) + 1
                    )
                # 47회차 cited_by 측정 + 48회차 hub 11개 확장
                # log·history·redirect 페이지의 인용은 cited_by에 포함하지 않음
                # (메타 페이지가 답변 근거 출처 추적에 들어가면 안 됨)
                citing_is_meta = (
                    page.is_log_file
                    or page.stem in {"log", "index", "index-history", "by-session"}
                    or page.is_redirect
                )
                if target in cited_by_targets and not citing_is_meta:
                    cited_by_map[target].add(page.stem)
                # 57회차 P0-3: cited_by_count 정수 캐시를 모든 비-메타 페이지에 측정.
                # 동일 메타 격리 정책 적용.
                if target in cited_by_count_targets and not citing_is_meta:
                    cited_by_count_map[target].add(page.stem)
            else:
                if is_history:
                    continue
                if target in EXAMPLE_TARGETS:
                    continue
                result.broken_links.append(
                    (str(page.path.relative_to(WIKI_ROOT.parent)), target)
                )

    result.inbound = inbound

    # source_count 부정합 검출 (entity/concept만 — source/synthesis는 source_count 없음)
    # 43회차: --update는 source_count를 덮어쓰지 않고, observed_source_refs / inbound_count
    # 두 자동 필드만 갱신한다 (운영자 수동 의미 보존).
    # 57회차 P0-2 보강: --update의 자동 필드 갱신 대상을 synthesis까지 확장.
    # source_count_mismatch 검출은 entity/concept만 (정의 A 운영자 수동 필드를
    # 가지는 타입), 자동 필드 갱신은 비-메타 전체.
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        if page.page_type not in ("entity", "concept", "synthesis"):
            continue
        observed = source_count_observed.get(page.stem, 0)
        if page.page_type in ("entity", "concept"):
            declared = page.declared_source_count
            if declared is not None and declared != observed:
                result.source_count_mismatch.append(
                    (str(page.path.relative_to(WIKI_ROOT.parent)), declared, observed)
                )
        if update:
            _update_auto_fields(
                page,
                observed_source_refs=observed,
                inbound_count=inbound.get(page.stem, 0),
            )

    # 47회차 신설 + 48회차 hub 확장: cited_by 자동 갱신
    # source 페이지 전체 + 5축 hub 11개
    if update:
        for page in pages:
            if page.yaml_invalid or page.is_redirect or page.is_log_file:
                continue
            if page.stem not in cited_by_targets:
                continue
            citing_stems = sorted(cited_by_map.get(page.stem, set()))
            _update_cited_by(page, citing_stems)

    # 57회차 P0-3 신설: cited_by_count 정수 캐시를 모든 비-메타 페이지에 갱신.
    # cited_by 리스트는 박지 않음 (frontmatter 폭증 방지) — 정수만 일관 적용.
    # 56회차 4축 평가 합집합 Critical: 측정 갭 87페이지(cited_by_count=0) 해소.
    if update:
        for page in pages:
            if page.yaml_invalid or page.is_redirect or page.is_log_file:
                continue
            if page.stem not in cited_by_count_targets:
                continue
            count = len(cited_by_count_map.get(page.stem, set()))
            _update_cited_by_count_only(page, count)

    # 58회차 P0-2 신설: synthesis + source 페이지의 inbound_count 자동 갱신.
    # _update_auto_fields는 source_count 라인 의존 가드 때문에 entity/concept만 처리.
    # 57회차 사후 재평가 N2 회귀: synthesis 20개 + source 65/65 inbound_count 누락 →
    # RAG 답변 정책 §1 "수치 비교"의 일관성 갭. 본 패스로 해소.
    if update:
        for page in pages:
            if page.yaml_invalid or page.is_redirect or page.is_log_file:
                continue
            if page.page_type not in ("synthesis", "source"):
                continue
            _update_inbound_count_only(page, inbound.get(page.stem, 0))

    # 57회차 P0-5 신설 (check #13): cited_by_count 누락 비-메타 페이지 정보 보고
    # 53회차 정책에 따른 신뢰도 가중치 캐시 적용 가시화. --check 모드에서도 보고하여
    # --update 실행을 권장. 결함이 아닌 정보 보고.
    # 58회차 P0-3 (R1 패치): 검사 범위를 cited_by_targets(11 hub + sources)까지 확장.
    # 57회차 사후 재평가 회귀 R1 (B·D·A 3축 동시 발견): 11 hub 화이트홀 사각지대 해소.
    cited_by_count_check_targets = cited_by_count_targets | cited_by_targets
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        if page.stem not in cited_by_count_check_targets:
            continue
        if "cited_by_count:" not in page.raw:
            result.cited_by_count_missing.append(
                str(page.path.relative_to(WIKI_ROOT.parent))
            )

    # 59회차 P0-2 신설 (check #14): 한·영 tag canonical 위반 (회귀 차단)
    # CLAUDE.md 59회차 옵션 A 정책: tags는 canonical 1개만, 강등 표기는 사용 금지.
    # 6쌍 강등→canonical 매핑 검증.
    TAG_CANONICAL_MAP = {
        "에이전트": "agent",
        "하네스": "harness",
        "backend": "백엔드",
        "data-analysis": "데이터분석",
        "wiki": "위키",
        "owner": "석근",
    }
    for page in pages:
        if page.yaml_invalid or not page.frontmatter:
            continue
        page_tags = page.frontmatter.get("tags", []) or []
        if not isinstance(page_tags, list):
            continue
        page_tags_set = {str(t) for t in page_tags}
        for demoted, canonical in TAG_CANONICAL_MAP.items():
            if demoted in page_tags_set:
                result.tag_canonical_violations.append(
                    (str(page.path.relative_to(WIKI_ROOT.parent)), demoted, canonical)
                )

    # 고아 페이지: 인바운드 0 (단, redirect/index/log 제외)
    for stem, cnt in inbound.items():
        if cnt > 0:
            continue
        page = next((p for p in pages if p.stem == stem), None)
        if page is None:
            continue
        if page.is_redirect or page.is_log_file or stem == "index":
            continue
        result.orphan_pages.append(stem)

    # 빈약 페이지: source_count >= 3인데 본문 < 30줄 (frontmatter 제외)
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        sc = page.declared_source_count or 0
        if sc < 3:
            continue
        body_lines = page.body_line_count
        if body_lines < 30:
            result.thin_pages.append(
                (str(page.path.relative_to(WIKI_ROOT.parent)), sc, body_lines)
            )

    # 33회차 신설:
    # 6. source_scope 부재 결함 (source_url=="" 인데 source_scope 누락)
    # 7. last_verified 신선도 (verification_required=true 페이지의 last_verified 90일 초과)
    today = date.today()
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        fm = page.frontmatter or {}
        rel_path = str(page.path.relative_to(WIKI_ROOT.parent))

        # source 페이지의 source_scope 검증
        if page.page_type == "source":
            url = fm.get("source_url", None)
            scope = fm.get("source_scope", None)
            if url == "" or url is None:
                if scope is None:
                    result.source_scope_missing.append(rel_path)
                elif scope not in VALID_SOURCE_SCOPES:
                    result.source_scope_invalid.append((rel_path, str(scope)))
            elif scope is not None and scope not in VALID_SOURCE_SCOPES:
                result.source_scope_invalid.append((rel_path, str(scope)))

        # verification_required 페이지의 last_verified 신선도
        if fm.get("verification_required") is True:
            lv = fm.get("last_verified")
            if lv is None:
                result.verification_malformed.append(
                    (rel_path, "last_verified 누락")
                )
                continue
            if isinstance(lv, str):
                try:
                    lv_date = datetime.strptime(lv, "%Y-%m-%d").date()
                except ValueError:
                    result.verification_malformed.append(
                        (rel_path, f"last_verified 형식 오류: {lv!r}")
                    )
                    continue
            elif isinstance(lv, date):
                lv_date = lv
            else:
                result.verification_malformed.append(
                    (rel_path, f"last_verified 타입 오류: {type(lv).__name__}")
                )
                continue
            days_old = (today - lv_date).days
            if days_old > STALE_VERIFICATION_DAYS:
                result.stale_verification.append((rel_path, str(lv_date), days_old))

    # 36회차 신설:
    # 8. 태그 case-duplicate 회귀 검출 (전역 vocabulary 기준)
    # 9. 한영 병기 의무 위반 검출 (페이지별)
    from collections import Counter, defaultdict
    tag_count: Counter[str] = Counter()
    file_tags: dict[str, set[str]] = {}
    for page in pages:
        if page.yaml_invalid or page.is_log_file:
            continue
        fm = page.frontmatter or {}
        tags = fm.get("tags", [])
        if not isinstance(tags, list):
            continue
        page_tags = {t for t in tags if isinstance(t, str)}
        file_tags[str(page.path.relative_to(WIKI_ROOT.parent))] = page_tags
        tag_count.update(page_tags)

    # 검증 8: 같은 lowercase로 collapse 시 둘 이상의 변형이 동시 존재
    by_lower: dict[str, list[str]] = defaultdict(list)
    for tag in tag_count:
        if tag in CASE_DUPLICATE_WHITELIST:
            continue
        by_lower[tag.lower()].append(tag)
    for lower, variants in by_lower.items():
        if len(variants) <= 1:
            continue
        # 정렬: 사용 빈도 내림차순
        variants_sorted = sorted(variants, key=lambda t: -tag_count[t])
        canonical = variants_sorted[0]
        for variant in variants_sorted[1:]:
            result.tag_case_duplicates.append(
                (canonical, variant, tag_count[canonical], tag_count[variant])
            )

    # 검증 9: 한영 병기 의무 위반 (한쪽만 있으면 경고)
    for rel_path, page_tags in file_tags.items():
        missing: list[str] = []
        for en, ko in KO_EN_PAIRS:
            has_en = en in page_tags
            has_ko = ko in page_tags
            if has_en and not has_ko:
                missing.append(f"{ko} (짝: {en})")
            elif has_ko and not has_en:
                missing.append(f"{en} (짝: {ko})")
        if missing:
            result.tag_pair_violations.append((rel_path, "병기 누락", missing))

    # 43회차 신설:
    # 검증 10: 메타 페이지 rag_exclude 누락 결함
    # type: index 또는 type: log 페이지에 rag_exclude:true 가 없으면 결함.
    # RAG 답변 근거로 카탈로그(인덱스)나 메타 활동 로그가 혼입되면 stale 정보 노출.
    for page in pages:
        if page.yaml_invalid:
            continue
        ptype = page.page_type
        if ptype not in ("index", "log"):
            continue
        rel_path = str(page.path.relative_to(WIKI_ROOT.parent))
        fm = page.frontmatter or {}
        if not bool(fm.get("rag_exclude", False)):
            result.meta_rag_exclude_missing.append((rel_path, ptype))

    # 49회차 P0-5 신설:
    # 검증 11: 본문 정량 stale 경고
    # `[[페이지명]](N)` 또는 `[[페이지명]](N, 1위)` 패턴이 본문에 있고
    # 시점 라벨("28회차 시점", "당시", "스냅샷" 등)이 같은 줄에 없을 때
    # 그 페이지의 자동 측정 inbound와 |delta| >= 5 이면 stale 가능성 정보 보고.
    # 결함 아님 — has_defect()에 추가하지 않는다.
    for page in pages:
        if page.yaml_invalid or page.is_rag_excluded:
            continue
        for line in page.body.split("\n"):
            if any(label in line for label in SNAPSHOT_LABEL_KEYS):
                continue
            for match in BODY_STALE_INBOUND_RE.finditer(line):
                target_stem = match.group(1)
                try:
                    body_value = int(match.group(2))
                except ValueError:
                    continue
                # 인바운드 통계 범위 밖이면 연도·금액 등 다른 숫자로 간주, 검사 제외.
                if body_value > BODY_STALE_VALUE_CEILING:
                    continue
                observed = result.inbound.get(target_stem)
                if observed is None or observed > BODY_STALE_VALUE_CEILING:
                    continue
                delta = observed - body_value
                if abs(delta) >= BODY_STALE_DELTA_THRESHOLD:
                    result.body_stale_numbers.append(
                        (page.stem, target_stem, body_value, observed, delta)
                    )

    # 51회차 P0-5 신설:
    # 검증 12: stub entity 결함 검출
    # type=entity AND body<25 AND source_count==0 AND inbound>0 AND entity_type!=redirect.
    # canonical 충돌 stub (예: mate-chat이 redirect로 마이그레이션 안 된 채 entity로 남는 케이스)
    # 또는 stub 등록만 되고 콘텐츠가 없는 entity의 회귀 차단.
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        if page.page_type != "entity":
            continue
        fm = page.frontmatter or {}
        if str(fm.get("entity_type", "")) == "redirect":
            continue
        sc = page.declared_source_count or 0
        if sc != 0:
            continue
        body_lines = page.body_line_count
        if body_lines >= 25:
            continue
        inbound = result.inbound.get(page.stem, 0)
        if inbound <= 0:
            continue
        rel_path = str(page.path.relative_to(WIKI_ROOT.parent))
        result.stub_entities.append((rel_path, body_lines, sc, inbound))

    return result


def _update_auto_fields(
    page: WikiPage, *, observed_source_refs: int, inbound_count: int
) -> None:
    """frontmatter의 자동 필드(observed_source_refs, inbound_count)를 in-place 갱신.

    43회차 정책 (CLAUDE.md 참조):
    - source_count(정의 A, 수동)는 절대 덮어쓰지 않는다.
    - 두 자동 필드가 frontmatter에 없으면 source_count 라인 바로 다음에 삽입한다.
    - source_count 라인이 없으면 자동 필드도 삽입하지 않는다 (entity/concept만 대상).
    """
    raw = page.raw
    if not SOURCE_COUNT_LINE_RE.search(raw):
        return  # source_count가 없는 페이지는 자동 필드 삽입 대상 아님

    # observed_source_refs 갱신 또는 삽입
    if OBSERVED_REFS_LINE_RE.search(raw):
        raw = OBSERVED_REFS_LINE_RE.sub(
            f"observed_source_refs: {observed_source_refs}", raw, count=1
        )
    else:
        raw = SOURCE_COUNT_LINE_RE.sub(
            lambda m: m.group(0)
            + f"\nobserved_source_refs: {observed_source_refs}",
            raw,
            count=1,
        )

    # inbound_count 갱신 또는 삽입
    if INBOUND_COUNT_LINE_RE.search(raw):
        raw = INBOUND_COUNT_LINE_RE.sub(
            f"inbound_count: {inbound_count}", raw, count=1
        )
    else:
        raw = OBSERVED_REFS_LINE_RE.sub(
            lambda m: m.group(0) + f"\ninbound_count: {inbound_count}",
            raw,
            count=1,
        )

    if raw != page.raw:
        page.path.write_text(raw, encoding="utf-8")


def _update_inbound_count_only(page: WikiPage, inbound_count: int) -> None:
    """inbound_count(정수)만 in-place 갱신. observed_source_refs는 박지 않음.

    58회차 P0-2 신설 (57회차 사후 재평가 N2 회귀 대응):
    `_update_auto_fields`가 source_count 라인 의존 가드(line 678)를 가져
    synthesis 20개 + source 65/65에 inbound_count가 자동 갱신 안 되던 갭 해소.

    observed_source_refs는 정의 B(source 페이지가 wikilink로 인용한 횟수)라
    entity/concept만 의미가 있어 본 함수에서 제외.
    inbound_count는 모든 페이지에 의미 있는 그래프 중심성 지표 (정의 C).

    빈 카운트(0)도 명시적으로 박는다 — 51회차 RAG 답변 정책 §1 "수치 비교"에서
    synthesis·source 페이지의 신뢰도 가중치 가용성을 보장.
    """
    raw = page.raw
    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        return
    fm_text = fm_match.group(1)
    body_after = raw[fm_match.end():]
    fm_lines = fm_text.split("\n")

    # 기존 inbound_count 라인 위치 탐색
    cnt_idx = None
    for i, ln in enumerate(fm_lines):
        if ln.startswith("inbound_count:"):
            cnt_idx = i
            break

    new_line = f"inbound_count: {inbound_count}"
    if cnt_idx is not None:
        if fm_lines[cnt_idx] == new_line:
            return  # 변경 없음
        fm_lines[cnt_idx] = new_line
    else:
        # frontmatter 끝에 삽입 (trailing 빈 라인 제거 후)
        while fm_lines and fm_lines[-1] == "":
            fm_lines.pop()
        fm_lines.append(new_line)

    new_fm = "\n".join(fm_lines)
    new_raw = f"---\n{new_fm}\n---\n" + body_after
    if new_raw != raw:
        page.path.write_text(new_raw, encoding="utf-8")


def _update_cited_by(page: WikiPage, citing_stems: list[str]) -> None:
    """source 페이지 frontmatter의 cited_by 필드를 in-place 갱신.

    47회차 신설 (Codex 평가 P1 권고 — citation chain 양방향화).
    51회차 갱신 (평가 P0-3 채택): cited_by 항목이
    `CITED_BY_FRONTMATTER_THRESHOLD` 이상이면 frontmatter cited_by 리스트 대신
    `cited_by_count: N`만 박고 본문 섹션으로 이동. RAG 첫 청크 의미 신호 손실 방지.

    cited_by는 자동 측정 필드:
    - 페이지를 wikilink로 인용한 모든 비-메타 페이지 stem 리스트
    - 운영자 수동 입력 금지, --update가 갱신
    - 빈 list면 cited_by/cited_by_count 키 모두 제거 (orphan의 깔끔한 표시)

    구현: frontmatter 파싱 없이 정규식 + 라인 단위 안전 업서트.
    """
    raw = page.raw
    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        return
    fm_text = fm_match.group(1)
    body_after = raw[fm_match.end():]
    fm_lines = fm_text.split("\n")

    # 기존 cited_by 블록 위치 탐색
    cb_start = None
    cb_end = len(fm_lines)
    for i, ln in enumerate(fm_lines):
        if ln.strip() == "cited_by:":
            cb_start = i
            break
    if cb_start is not None:
        for j in range(cb_start + 1, len(fm_lines)):
            ln = fm_lines[j]
            if ln and not ln.startswith(" ") and not ln.startswith("\t") and not ln.startswith("-"):
                cb_end = j
                break
            if ln == "":
                cb_end = j
                break

    # 기존 cited_by_count 라인 위치 탐색
    cnt_idx = None
    for i, ln in enumerate(fm_lines):
        if ln.startswith("cited_by_count:"):
            cnt_idx = i
            break

    use_body = len(citing_stems) >= CITED_BY_FRONTMATTER_THRESHOLD
    new_lines = list(fm_lines)

    # 기존 cited_by 블록 제거
    if cb_start is not None:
        new_lines = new_lines[:cb_start] + new_lines[cb_end:]
        # 인덱스 갱신
        if cnt_idx is not None and cnt_idx >= cb_end:
            cnt_idx -= cb_end - cb_start
        elif cnt_idx is not None and cb_start <= cnt_idx < cb_end:
            cnt_idx = None  # cited_by_count가 cited_by 블록 안이었음 — 비정상이지만 안전 처리

    # 기존 cited_by_count 라인 제거 (재삽입 또는 조건부 삽입)
    if cnt_idx is not None:
        new_lines = new_lines[:cnt_idx] + new_lines[cnt_idx + 1:]

    if not citing_stems:
        # 빈 list — frontmatter에 cited_by/cited_by_count 모두 박지 않음.
        # 본문 섹션도 제거.
        new_body = _strip_cited_by_body_section(body_after)
    elif use_body:
        # 임계값 이상: frontmatter cited_by_count: N + 본문 섹션
        # frontmatter 끝의 빈 라인 제거 후 cited_by_count 삽입
        while new_lines and new_lines[-1] == "":
            new_lines.pop()
        new_lines.append(f"cited_by_count: {len(citing_stems)}")
        new_body = _replace_cited_by_body_section(body_after, citing_stems)
    else:
        # 임계값 미만: frontmatter cited_by list (47회차 기존 동작)
        # 58회차 P0-3 (R1 패치): cited_by_count 정수도 함께 박는다.
        # 57회차 사후 재평가 회귀 R1 (B·D·A 3축 동시 발견): portfolio·com2us-platform
        # 등 임계값 미만 hub가 cited_by_count 없이 cited_by list만 가지면
        # RAG 답변 정책 §1 "수치 비교" 시 정수 비교 불가. 일관성 회복.
        cb_block = ["cited_by:"] + [f'  - "[[{s}]]"' for s in citing_stems]
        while new_lines and new_lines[-1] == "":
            new_lines.pop()
        new_lines = new_lines + cb_block + [f"cited_by_count: {len(citing_stems)}"]
        new_body = _strip_cited_by_body_section(body_after)

    new_fm = "\n".join(new_lines)
    new_raw = f"---\n{new_fm}\n---\n" + new_body
    if new_raw != raw:
        page.path.write_text(new_raw, encoding="utf-8")


def _update_cited_by_count_only(page: WikiPage, count: int) -> None:
    """cited_by_count(정수)만 in-place 갱신. cited_by 리스트는 박지 않음.

    57회차 P0-3 신설 (56회차 4축 평가 합집합 Critical):
    51회차 RAG 답변 정책 §1 "수치 비교"의 신뢰도 가중치 캐시를 모든 비-메타
    페이지(entity·concept·synthesis)에 일관 적용. cited_by 리스트는 frontmatter
    폭증 위험으로 sources + 11 hub 한정 유지하되, 정수만 박는 cited_by_count는
    194 페이지 전체로 확장해 측정 갭 87페이지 해소.

    빈 카운트(0)도 명시적으로 박는다 — "측정됐고 0"과 "측정 안 됨" 구분.
    이는 53회차 정책의 "빈 cited_by인 경우 키 생략" 패턴과 다른 정책:
    cited_by 리스트는 양방향 추적이라 빈 list = 의미 없음(키 생략),
    cited_by_count는 신뢰도 가중치라 0도 의미 있음(키 박음).
    """
    raw = page.raw
    fm_match = FRONTMATTER_RE.match(raw)
    if not fm_match:
        return
    fm_text = fm_match.group(1)
    body_after = raw[fm_match.end():]
    fm_lines = fm_text.split("\n")

    # 기존 cited_by_count 라인 위치 탐색
    cnt_idx = None
    for i, ln in enumerate(fm_lines):
        if ln.startswith("cited_by_count:"):
            cnt_idx = i
            break

    new_line = f"cited_by_count: {count}"
    if cnt_idx is not None:
        if fm_lines[cnt_idx] == new_line:
            return  # 변경 없음
        fm_lines[cnt_idx] = new_line
    else:
        # frontmatter 끝에 삽입 (trailing 빈 라인 제거 후)
        while fm_lines and fm_lines[-1] == "":
            fm_lines.pop()
        fm_lines.append(new_line)

    new_fm = "\n".join(fm_lines)
    new_raw = f"---\n{new_fm}\n---\n" + body_after
    if new_raw != raw:
        page.path.write_text(new_raw, encoding="utf-8")


def _replace_cited_by_body_section(body: str, citing_stems: list[str]) -> str:
    """본문에서 ## 인용한 페이지 섹션을 새 리스트로 교체. 없으면 끝에 추가."""
    header = CITED_BY_BODY_HEADER
    block_lines = [header, ""] + [f"- [[{s}]]" for s in citing_stems] + [""]
    block_text = "\n".join(block_lines)

    lines = body.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == header:
            start = i
            break
    if start is None:
        # 끝에 추가. 본문이 줄바꿈으로 끝나는지 정규화
        body_clean = body.rstrip() + "\n\n"
        return body_clean + block_text + "\n"

    # 다음 H2(## ) 또는 파일 끝까지 블록 종료
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## ") or lines[j].startswith("# "):
            end = j
            break
    # 끝의 빈 라인 흡수
    while end < len(lines) and lines[end] == "":
        end += 1
    new_lines = lines[:start] + block_lines + lines[end:]
    return "\n".join(new_lines)


def _strip_cited_by_body_section(body: str) -> str:
    """본문에서 ## 인용한 페이지 섹션을 제거. 없으면 그대로."""
    header = CITED_BY_BODY_HEADER
    lines = body.split("\n")
    start = None
    for i, ln in enumerate(lines):
        if ln.strip() == header:
            start = i
            break
    if start is None:
        return body
    end = len(lines)
    for j in range(start + 1, len(lines)):
        if lines[j].startswith("## ") or lines[j].startswith("# "):
            end = j
            break
    while end < len(lines) and lines[end] == "":
        end += 1
    new_lines = lines[:start] + lines[end:]
    return "\n".join(new_lines)


def report(result: LintResult, *, quiet: bool = False) -> None:
    pages = result.pages
    real_pages = [p for p in pages if not p.is_log_file and p.stem != "index"]

    if not quiet:
        print("=" * 72)
        print("📊 llm-wiki 정합성 점검 보고")
        print("=" * 72)
        print(
            f"전체 페이지: {len(pages)} (log/index 제외 콘텐츠 페이지 = {len(real_pages)})"
        )
        print(f"redirect 페이지: {len(result.redirect_pages)} (별도 집계)")
        print()

    # 결함 보고
    print("--- 1. 깨진 위키링크 ---")
    if result.broken_links:
        print(f"❌ {len(result.broken_links)}건 발견:")
        for path, target in result.broken_links[:20]:
            print(f"    {path} -> [[{target}]]")
        if len(result.broken_links) > 20:
            print(f"    ...추가 {len(result.broken_links) - 20}건")
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 2. 고아 페이지 (인바운드 0, redirect/index/log 제외) ---")
    if result.orphan_pages:
        print(f"⚠ {len(result.orphan_pages)}건:")
        for stem in result.orphan_pages[:20]:
            print(f"    {stem}")
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 3. frontmatter YAML invalid ---")
    if result.yaml_invalid:
        print(f"❌ {len(result.yaml_invalid)}건:")
        for path, err in result.yaml_invalid[:10]:
            print(f"    {path}: {err}")
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 4. source_count 부정합 (declared vs observed, 정보 보고 — 결함 아님) ---")
    if result.source_count_mismatch:
        print(f"ℹ️ {len(result.source_count_mismatch)}건 (정의 A 운영자 의미 vs 정의 B 자동 측정 차이, 결함 아님):")
        for path, declared, observed in result.source_count_mismatch[:20]:
            print(
                f"    {path}: declared={declared} observed={observed} "
                f"(delta={observed - declared:+d})"
            )
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 5. 빈약 페이지 (source_count >= 3 + 본문 < 30줄) ---")
    if result.thin_pages:
        print(f"⚠ {len(result.thin_pages)}건:")
        for path, sc, body_lines in result.thin_pages[:20]:
            print(f"    {path}: source_count={sc} body_lines={body_lines}")
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 6. source_scope 부재/이상 (source_url 빈 페이지) ---")
    if result.source_scope_missing or result.source_scope_invalid:
        if result.source_scope_missing:
            print(f"❌ source_scope 누락 {len(result.source_scope_missing)}건:")
            for path in result.source_scope_missing[:10]:
                print(f"    {path}")
        if result.source_scope_invalid:
            print(f"❌ source_scope 값 이상 {len(result.source_scope_invalid)}건:")
            for path, scope in result.source_scope_invalid[:10]:
                print(f"    {path}: {scope!r}")
    else:
        if not quiet:
            print("✓ 0건")

    print("--- 7. last_verified 신선도 (verification_required 페이지) ---")
    if result.verification_malformed:
        print(f"❌ verification 형식 오류 {len(result.verification_malformed)}건:")
        for path, err in result.verification_malformed[:10]:
            print(f"    {path}: {err}")
    if result.stale_verification:
        print(
            f"⚠ {len(result.stale_verification)}건 신선도 경과 "
            f"(>{STALE_VERIFICATION_DAYS}일):"
        )
        for path, lv, days in result.stale_verification[:10]:
            print(f"    {path}: last_verified={lv} ({days}일 전)")
    if not result.verification_malformed and not result.stale_verification:
        if not quiet:
            print("✓ 0건 (모든 verification 페이지 신선)")

    print("--- 8. 태그 case-duplicate 회귀 (lowercase 통합 시 충돌) ---")
    if result.tag_case_duplicates:
        print(f"❌ {len(result.tag_case_duplicates)}쌍 동의어 분산:")
        for canon, variant, c_count, v_count in result.tag_case_duplicates[:15]:
            print(f"    canonical={canon!r}({c_count}) ↔ 회귀={variant!r}({v_count})")
    else:
        if not quiet:
            print("✓ 0건 (전체 태그 vocabulary 정규화 유지)")

    print("--- 9. 한영 병기 의무 위반 (개념·도메인 카테고리) ---")
    if result.tag_pair_violations:
        print(f"⚠ {len(result.tag_pair_violations)}건 병기 누락:")
        for path, _, missing in result.tag_pair_violations[:15]:
            print(f"    {path}")
            for m in missing:
                print(f"        + 추가 필요: {m}")
    else:
        if not quiet:
            print("✓ 0건 (4개 그룹 모두 100% 병기)")

    print("--- 10. 메타 페이지 rag_exclude 누락 (type=index/log, 43회차 신설) ---")
    if result.meta_rag_exclude_missing:
        print(f"❌ {len(result.meta_rag_exclude_missing)}건:")
        for path, ptype in result.meta_rag_exclude_missing[:10]:
            print(f"    {path} (type={ptype})")
    else:
        if not quiet:
            print("✓ 0건 (모든 메타 페이지 rag_exclude:true)")

    print(
        "--- 11. 본문 정량 stale 경고 "
        "(49회차 신설, 정보 보고 — 결함 아님) ---"
    )
    if result.body_stale_numbers:
        print(
            f"ℹ️ {len(result.body_stale_numbers)}건 "
            f"(|delta| >= {BODY_STALE_DELTA_THRESHOLD}, 시점 라벨 없는 줄):"
        )
        for page_stem, target_stem, body_value, observed, delta in result.body_stale_numbers[:20]:
            print(
                f"    {page_stem}.md: [[{target_stem}]]({body_value}) "
                f"— 자동 측정 {observed}, delta {delta:+d}"
            )
        if len(result.body_stale_numbers) > 20:
            remainder = len(result.body_stale_numbers) - 20
            print(f"    ... (생략 {remainder}건)")
    else:
        if not quiet:
            print(
                "✓ 0건 (본문 정량 단언이 자동 측정값과 정합 또는 시점 라벨 박힘)"
            )

    print(
        "--- 12. stub entity 결함 (51회차 신설 — type=entity AND body<25 "
        "AND source_count==0 AND inbound>0) ---"
    )
    if result.stub_entities:
        print(f"❌ {len(result.stub_entities)}건:")
        for rel_path, body_lines, sc, inbound in result.stub_entities[:10]:
            print(
                f"    {rel_path}: body={body_lines}줄, source_count={sc}, "
                f"inbound={inbound}"
            )
        if len(result.stub_entities) > 10:
            remainder = len(result.stub_entities) - 10
            print(f"    ... (생략 {remainder}건)")
    else:
        if not quiet:
            print("✓ 0건 (canonical 충돌 stub 또는 영양실조 entity 없음)")

    print(
        "--- 13. cited_by_count 누락 비-메타 페이지 (57회차 신설 — 53회차 정책 정합화, "
        "정보 보고 — 결함 아님) ---"
    )
    if result.cited_by_count_missing:
        print(
            f"ℹ️ {len(result.cited_by_count_missing)}건 (--update 실행 시 자동 채움):"
        )
        for rel_path in result.cited_by_count_missing[:10]:
            print(f"    {rel_path}")
        if len(result.cited_by_count_missing) > 10:
            remainder = len(result.cited_by_count_missing) - 10
            print(f"    ... (생략 {remainder}건)")
    else:
        if not quiet:
            print("✓ 0건 (모든 비-메타 페이지에 cited_by_count 정수 캐시 적용)")

    print(
        "--- 14. 한·영 tag canonical 위반 (59회차 신설 — 옵션 A 정책 회귀 차단) ---"
    )
    if result.tag_canonical_violations:
        print(f"❌ {len(result.tag_canonical_violations)}건:")
        for rel_path, demoted, canonical in result.tag_canonical_violations[:10]:
            print(f"    {rel_path}: '{demoted}' → '{canonical}'로 정정 필요")
        if len(result.tag_canonical_violations) > 10:
            remainder = len(result.tag_canonical_violations) - 10
            print(f"    ... (생략 {remainder}건)")
    else:
        if not quiet:
            print("✓ 0건 (한·영 6쌍 canonical 정합)")


def report_full(result: LintResult) -> None:
    """--report 모드: 인바운드 분포 + 5축 통계."""
    print()
    print("=" * 72)
    print("📈 인바운드 분포 (상위 20)")
    print("=" * 72)
    top = sorted(result.inbound.items(), key=lambda kv: -kv[1])[:20]
    for stem, cnt in top:
        print(f"    {cnt:4d}  {stem}")

    print()
    print("=" * 72)
    print("🎯 5축 hub 인바운드 합산")
    print("=" * 72)
    total_axis = 0
    axis_totals: list[tuple[str, int]] = []
    for axis, hubs in AXES.items():
        subtotal = sum(result.inbound.get(h, 0) for h in hubs)
        total_axis += subtotal
        axis_totals.append((axis, subtotal))
        print(f"\n  {axis}: 합산 {subtotal}")
        for h in hubs:
            cnt = result.inbound.get(h)
            marker = "    " if cnt is not None else " ✗  "
            print(f"  {marker}{cnt or 0:4d}  {h}")
    if total_axis:
        print(f"\n  5축 합산 총: {total_axis}")
        for axis, subtotal in axis_totals:
            pct = subtotal * 100 / total_axis
            print(f"    {axis}: {subtotal} ({pct:4.1f}%)")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="llm-wiki 정합성 검증 + source_count 자동 갱신",
    )
    parser.add_argument("--check", action="store_true", help="검증 실행 (default)")
    parser.add_argument(
        "--update", action="store_true", help="source_count 부정합 자동 수정"
    )
    parser.add_argument(
        "--report", action="store_true", help="인바운드 분포 / 5축 통계 추가 출력"
    )
    parser.add_argument("--quiet", action="store_true", help="문제만 출력")
    args = parser.parse_args(argv)

    if not WIKI_ROOT.exists():
        print(f"ERROR: wiki/ 디렉토리 부재: {WIKI_ROOT}", file=sys.stderr)
        return 2

    result = lint(update=args.update)

    do_check = args.check or not (args.update or args.report)
    if do_check or args.update:
        report(result, quiet=args.quiet)

    if args.report:
        report_full(result)

    if args.update:
        print()
        print(
            "✓ 자동 필드 갱신 완료: observed_source_refs / inbound_count "
            "(entity/concept), cited_by (source). "
            "source_count(수동)는 보존됨."
        )
        if result.source_count_mismatch:
            print(
                f"  ※ source_count vs observed_source_refs 부정합 "
                f"{len(result.source_count_mismatch)}건은 정의 차이 정보 보고 "
                f"(결함 아님, CLAUDE.md schema 3분리 참조)"
            )

    if (do_check or args.update) and result.has_defect() and not args.update:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
