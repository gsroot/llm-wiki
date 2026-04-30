#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests",
#   "beautifulsoup4",
#   "html2text",
# ]
# ///
"""
wikidocs.net "ChatGPT & Codex 실무 활용 가이드" (송영옥, CC BY) 본문 verbatim 수집.

사용법:
    ./scripts/fetch-codex-guide.py

의존성: uv가 PEP 723 inline metadata로 자동 설치 (requests, beautifulsoup4, html2text).

이미 메인 에이전트 WebFetch로 verbatim 저장된 3개 페이지(Ch 1, Ch 4, 부록 D)는
SKIP_VERBATIM 집합에 들어있어 덮어쓰지 않습니다. 다시 받으려면 그 ID를 빼면 됩니다.

라이선스: 원본은 송영옥 저자의 CC BY 자료. 본 스크립트 결과는 CC BY attribution
요구사항을 충족하는 형태로 frontmatter에 출처·저자·라이선스를 명시합니다.
"""

from __future__ import annotations

import sys
import time
from datetime import date
from pathlib import Path

import html2text
import requests
from bs4 import BeautifulSoup

# ---- 설정 ----------------------------------------------------------------

DEST = Path(
    "/Users/sgkim/Projects/llm-wiki/raw/articles/openai-chatgpt-codex-guide"
)

# 42 페이지: ID → 파일 슬러그 (kebab-case)
PAGES: dict[int, str] = {
    340806: "part-1-intro",
    340807: "ch-01-genai-openai-changes",
    340808: "ch-02-chatgpt-vs-claude-vs-gemini",
    340809: "part-2-intro",
    340810: "ch-03-chatgpt-signup-interface",
    340811: "ch-04-effective-prompts",
    340812: "part-3-intro",
    340813: "ch-05-document-writing",
    340814: "ch-06-data-analysis",
    340815: "ch-07-image-dalle",
    340816: "ch-08-search-research",
    340817: "part-4-intro",
    340818: "ch-09-custom-gpts",
    340819: "ch-10-memory-personalization",
    340820: "ch-11-voice-multimodal",
    340821: "ch-12-operator",
    340822: "part-5-intro",
    340823: "ch-13-codex-intro",
    340824: "ch-14-codex-coding-refactor",
    340825: "ch-15-codex-bug-test",
    340826: "ch-16-codex-patterns",
    340827: "part-6-intro",
    340828: "ch-17-marketing-content",
    340829: "ch-18-finance-accounting",
    340830: "ch-19-education-research",
    340831: "ch-20-legal-compliance",
    340832: "ch-21-hr-personnel",
    340833: "ch-22-strategy-management",
    340834: "part-7-intro",
    340835: "ch-23-openai-api-getting-started",
    340836: "ch-24-assistants-api",
    340837: "ch-25-workflow-automation",
    340838: "part-8-intro",
    340839: "ch-26-team-enterprise-rollout",
    340840: "ch-27-security-privacy-ethics",
    340841: "ch-28-ai-productivity-culture",
    340842: "appendix-intro",
    340843: "appendix-a-prompt-templates",
    340844: "appendix-b-chatgpt-pricing",
    340845: "appendix-c-openai-api-reference",
    340846: "appendix-d-codex-cheatsheet",
    340847: "appendix-e-references-links",
}

# Path B 단계에서 메인 에이전트 WebFetch로 이미 verbatim 저장된 3개 — 덮어쓰지 않음
SKIP_VERBATIM: set[int] = {340807, 340811, 340846}

# 본문 컨테이너 후보 selectors (wikidocs 구조 변동에 대비한 fallback chain)
BODY_SELECTORS: tuple[str, ...] = (
    "div#pagecontent",
    "div.page-content",
    ".markdown-body",
    "article",
    "main",
)

# rate-limit 매너 (서버 부담 최소화)
SLEEP_BETWEEN = 0.7

USER_AGENT = (
    "Mozilla/5.0 (compatible; llm-wiki/1.0 personal RAG; "
    "CC-BY attribution preserved)"
)

# ---- 본체 ----------------------------------------------------------------


def make_converter() -> html2text.HTML2Text:
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_links = False
    h.ignore_images = False
    h.unicode_snob = True
    h.bypass_tables = False
    h.escape_snob = True
    return h


def extract_body(soup: BeautifulSoup) -> BeautifulSoup:
    for sel in BODY_SELECTORS:
        node = soup.select_one(sel)
        if node and len(node.get_text(strip=True)) > 200:
            return node
    return soup


def extract_last_edit(soup: BeautifulSoup) -> str | None:
    for text in soup.stripped_strings:
        if "마지막 편집" in text or "최종 편집" in text:
            return text.strip()
    return None


def fetch_page(page_id: int, converter: html2text.HTML2Text) -> tuple[str, str | None]:
    url = f"https://wikidocs.net/{page_id}"
    r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
    r.raise_for_status()

    soup = BeautifulSoup(r.text, "html.parser")
    body = extract_body(soup)
    last_edit = extract_last_edit(soup)

    md = converter.handle(str(body)).strip()
    return md, last_edit


def write_file(page_id: int, slug: str, md: str, last_edit: str | None) -> Path:
    today = date.today().isoformat()
    file = DEST / f"{slug}.md"

    frontmatter = (
        "---\n"
        f"source_url: https://wikidocs.net/{page_id}\n"
        "book: ChatGPT & Codex 실무 활용 가이드\n"
        "book_url: https://wikidocs.net/book/19558\n"
        "author: 송영옥\n"
        "license: CC-BY\n"
        'license_note: "wikidocs.net 페이지에 CC BY 아이콘(by.png) 표시. '
        '출처 표기 + URL 명시로 attribution 요구사항 충족."\n'
        f"fetched_at: {today}\n"
        "ingestion_mode: path-a-verbatim\n"
        "---\n\n"
    )

    footer = (
        "\n\n---\n\n"
        f"**원본**: https://wikidocs.net/{page_id}  \n"
        "**저자**: 송영옥 (CC BY)  \n"
        "**책 페이지**: https://wikidocs.net/book/19558  \n"
    )
    if last_edit:
        footer += f"**{last_edit}**\n"

    file.write_text(frontmatter + md + footer, encoding="utf-8")
    return file


def main() -> int:
    DEST.mkdir(parents=True, exist_ok=True)
    converter = make_converter()

    total = len(PAGES)
    success = 0
    skipped = 0
    failed: list[tuple[int, str, str]] = []

    pages_sorted = sorted(PAGES.items())
    for i, (page_id, slug) in enumerate(pages_sorted, 1):
        prefix = f"[{i:2d}/{total}] {page_id} → {slug}"

        if page_id in SKIP_VERBATIM:
            print(f"{prefix}  (이미 verbatim 저장됨, skip)")
            skipped += 1
            continue

        try:
            print(f"{prefix}", end="  ... ", flush=True)
            md, last_edit = fetch_page(page_id, converter)
            file = write_file(page_id, slug, md, last_edit)
            chars = len(md)
            lines = md.count("\n") + 1
            print(f"✓ {chars:,} chars / {lines} lines")
            success += 1
        except Exception as exc:  # noqa: BLE001
            print(f"✗ {exc}")
            failed.append((page_id, slug, str(exc)))

        time.sleep(SLEEP_BETWEEN)

    print()
    print("=" * 60)
    print(f"✅ 완료: success={success}, skipped={skipped}, failed={len(failed)}")
    print(f"   저장 경로: {DEST}")
    if failed:
        print("\n❌ 실패 목록:")
        for pid, slug, err in failed:
            print(f"   {pid} ({slug}): {err}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
