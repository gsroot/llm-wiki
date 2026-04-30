#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
fetch-codex-guide.py 결과물 후처리.

- html2text의 과도 이스케이프 제거 (\(, \), \[, \], \., \~, \!, \-, \+, \>)
- wikidocs `[[MARK]]…[[/MARK]]` 형광펜 어노테이션 → `**…**` 굵은체
- 다중 빈줄 정리 (3+ → 2)
- frontmatter 영역은 건드리지 않음 (--- 와 --- 사이)

사용법:
    ./scripts/clean-codex-guide.py

SKIP_VERBATIM에 들어있는 3개(Ch 1, Ch 4, 부록 D)는 메인 에이전트 결과라
이미 깨끗해서 정제 대상에서 제외.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DEST = Path(
    "/Users/sgkim/Projects/llm-wiki/raw/articles/openai-chatgpt-codex-guide"
)

# 메인 에이전트 WebFetch로 verbatim 수집된 3개 — 이미 깨끗
SKIP_VERBATIM_FILES: set[str] = {
    "ch-01-genai-openai-changes.md",
    "ch-04-effective-prompts.md",
    "appendix-d-codex-cheatsheet.md",
}


def clean_body(text: str) -> str:
    # 1) [[MARK]]…[[/MARK]] → **…**
    #    실제 본문에는 `\[\[MARK\]\]…\[\[/MARK\]\]` 형태로 들어옴
    text = re.sub(
        r"\\\[\\\[MARK\\\]\\\](.*?)\\\[\\\[/MARK\\\]\\\]",
        r"**\1**",
        text,
        flags=re.DOTALL,
    )
    # 혹시 비-이스케이프 형태도 처리
    text = re.sub(r"\[\[MARK\]\](.*?)\[\[/MARK\]\]", r"**\1**", text, flags=re.DOTALL)

    # 2) 백슬래시 이스케이프 제거 — 특정 문자에 한정
    #    `\(`, `\)`, `\[`, `\]`, `\.`, `\~`, `\!`, `\+`, `\>`, `\-`
    #    단, 줄 시작의 `\-` (리스트)와 `\#` (헤딩)은 건드리지 않음
    text = re.sub(r"\\([(\)\[\].~!+>])", r"\1", text)

    # 3) `1\.` 같은 numbered list는 마크다운에서 정상 표기로
    text = re.sub(r"(\d+)\\\.", r"\1.", text)

    # 4) `\-` (본문 중간) — 줄 시작이 아닌 경우만
    text = re.sub(r"(?<!^)(?<!\n)\\-", "-", text)

    # 5) 다중 빈줄 정리: 3+ 연속 빈줄 → 2 (단락 구분 보존)
    text = re.sub(r"\n{4,}", "\n\n\n", text)

    return text


def process_file(path: Path) -> tuple[bool, int, int]:
    raw = path.read_text(encoding="utf-8")

    # frontmatter 분리
    if raw.startswith("---\n"):
        end = raw.find("\n---\n", 4)
        if end == -1:
            return False, 0, 0
        frontmatter = raw[: end + 5]
        body = raw[end + 5 :]
    else:
        frontmatter = ""
        body = raw

    cleaned = clean_body(body)
    new = frontmatter + cleaned

    if new == raw:
        return False, len(raw), len(new)

    path.write_text(new, encoding="utf-8")
    return True, len(raw), len(new)


def main() -> int:
    if not DEST.exists():
        print(f"❌ 디렉토리 없음: {DEST}")
        return 1

    files = sorted(DEST.glob("*.md"))
    if not files:
        print(f"❌ {DEST} 안에 .md 파일 없음")
        return 1

    cleaned_count = 0
    skipped_count = 0
    total_before = 0
    total_after = 0

    for f in files:
        if f.name in SKIP_VERBATIM_FILES:
            print(f"  skip {f.name}  (verbatim 보존)")
            skipped_count += 1
            continue

        changed, before, after = process_file(f)
        total_before += before
        total_after += after
        delta = after - before
        marker = "✓" if changed else " "
        print(f"  {marker} {f.name}  ({before:,} → {after:,} bytes, Δ {delta:+,})")
        if changed:
            cleaned_count += 1

    print()
    print(f"✅ 정제 완료: cleaned={cleaned_count}, skipped={skipped_count}, 총 {len(files)}개")
    print(f"   바이트 합계: {total_before:,} → {total_after:,} (Δ {total_after - total_before:+,})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
