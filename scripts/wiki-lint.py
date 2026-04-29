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
    5. 빈약 페이지 (source_count >= 3 인데 본문 < 30줄)
    6. 인바운드 분포 보고 (5축 hub 합산 / 전체 인바운드 분포)

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
from pathlib import Path

import yaml


WIKI_ROOT = Path(__file__).resolve().parent.parent / "wiki"

WIKILINK_RE = re.compile(r"\[\[([^]|#]+?)(?:\||#|\])")
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)
SOURCE_COUNT_LINE_RE = re.compile(r"^source_count:\s*\d+\s*$", re.MULTILINE)

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
    inbound: dict[str, int] = field(default_factory=dict)

    def has_defect(self) -> bool:
        # source_count 부정합은 결함이 아닌 정보 보고로 격하 (32회차 발견):
        # frontmatter source_count의 운영 정의는 "이 페이지 정보의 출처 source 수"
        # (정의 A, 수동 입력)인데, 자동 측정 가능한 건 "이 페이지를 인용한 source 페이지 수"
        # (정의 B, 객관 측정). 두 정의가 다르므로 부정합을 결함으로 판정하지 않는다.
        # --update 모드는 정의 B로 일괄 갱신하므로 사용 시 주의 (CLAUDE.md 참조).
        return bool(self.broken_links or self.yaml_invalid)


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
    for page in pages:
        if page.yaml_invalid or page.is_redirect or page.is_log_file:
            continue
        if page.page_type not in ("entity", "concept"):
            continue
        declared = page.declared_source_count
        if declared is None:
            continue
        observed = source_count_observed.get(page.stem, 0)
        if declared != observed:
            result.source_count_mismatch.append(
                (str(page.path.relative_to(WIKI_ROOT.parent)), declared, observed)
            )
            if update:
                _update_source_count(page, observed)

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

    return result


def _update_source_count(page: WikiPage, observed: int) -> None:
    """frontmatter의 source_count 필드를 in-place로 갱신."""
    new_text = SOURCE_COUNT_LINE_RE.sub(
        f"source_count: {observed}", page.raw, count=1
    )
    if new_text != page.raw:
        page.path.write_text(new_text, encoding="utf-8")


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

    print("--- 4. source_count 부정합 (declared vs observed) ---")
    if result.source_count_mismatch:
        print(f"❌ {len(result.source_count_mismatch)}건:")
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
        if result.source_count_mismatch:
            print()
            print(
                f"✓ source_count 부정합 {len(result.source_count_mismatch)}건 자동 수정 완료"
            )
        else:
            print()
            print("✓ source_count 부정합 없음 (수정 사항 없음)")

    if (do_check or args.update) and result.has_defect() and not args.update:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
