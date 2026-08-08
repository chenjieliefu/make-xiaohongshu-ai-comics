#!/usr/bin/env python3
"""Scaffold a style-adaptive Xiaohongshu AI comic project safely."""

import argparse
from pathlib import Path
from textwrap import dedent


def write(path: Path, content: str) -> None:
    path.write_text(dedent(content).lstrip(), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--topic", required=True, help="AI concept or episode topic")
    parser.add_argument("--output", required=True, help="New or empty project directory")
    parser.add_argument("--pages", type=int, default=8, help="Storyboard page count")
    parser.add_argument("--audience", default="对 AI 好奇的普通读者")
    parser.add_argument("--series", default="未命名 AI 漫画系列")
    args = parser.parse_args()

    if args.pages < 3 or args.pages > 12:
        parser.error("--pages must be between 3 and 12")

    root = Path(args.output).expanduser().resolve()
    if root.exists() and any(root.iterdir()):
        parser.error(f"refusing to write into non-empty directory: {root}")

    root.mkdir(parents=True, exist_ok=True)
    for name in ("pages", "drafts", "sources", "style-references", "character-references"):
        (root / name).mkdir(exist_ok=True)

    write(
        root / "brief.md",
        f"""
        # Project brief

        Series: {args.series}
        Topic: {args.topic}
        Audience: {args.audience}
        Page count: {args.pages}
        Intended platform: Xiaohongshu
        Format: 3:4 portrait PNG unless the user specifies another supported ratio
        Learning objective:
        Curiosity hook:
        Required claims:
        Forbidden claims:
        Visual direction or reference roles:
        Call to action:
        """,
    )

    write(
        root / "research.md",
        f"""
        # Research — {args.topic}

        One-sentence definition:
        What it does:
        What it does not mean:
        Relatable example:
        Common misconceptions:
        Limits and prerequisites:

        ## Sources

        | Claim | Primary source URL | Access date | Notes |
        |---|---|---|---|
        """,
    )

    write(
        root / "style-bible.md",
        f"""
        # Style bible — {args.series}

        Reference roles:
        Canvas and aspect ratio:
        Medium:
        Line quality:
        Shape language:
        Palette behavior:
        Surface and texture:
        Lighting and depth:
        Character proportions:
        Facial language:
        Layout and panel system:
        Typography behavior:
        Recurring motifs:
        Emotional tone:
        Must preserve:
        Must avoid:

        ## Compact continuity block

        Write an 80–150 word block for every image-generation prompt.
        """,
    )

    write(
        root / "character-bible.md",
        f"""
        # Character bible — {args.series}

        Shared shape language:
        Shared outline/rendering:
        Shared eye and facial system:
        Scale relationships:
        World interaction rules:

        ## Character 1

        Teaching function:
        Species or object basis:
        Silhouette:
        Head-to-body proportion:
        Dominant and accent colors:
        Eyes and face:
        Invariant accessory:
        Signature prop:
        Personality in three adjectives:
        Typical actions:
        Must always preserve:
        Must never add:
        Approved reference sheet:
        """,
    )

    page_sections = []
    for number in range(1, args.pages + 1):
        page_sections.append(
            dedent(
                f"""
                ### Page {number:02d}

                Purpose:
                Claim:
                Headline:
                Body:
                Labels:
                Visual metaphor:
                Characters:
                Style application:
                Accuracy note:
                """
            ).strip()
        )
    write(root / "storyboard.md", "# Storyboard\n\n" + "\n\n".join(page_sections) + "\n")

    write(
        root / "generation-prompts.md",
        """
        # Generation prompts

        Paste the exact final prompt for every page here before generation.

        ## Shared continuity blocks

        Style:

        Characters:
        """,
    )

    write(
        root / "publish-caption.md",
        f"""
        # Title

        {args.topic}

        # Caption

        Hook:

        Plain-language explanation:

        Immediately useful takeaway:

        Question for readers:

        # Hashtags

        #AI科普 #人工智能 #漫画科普 #小红书知识笔记
        """,
    )

    write(
        root / "qa-checklist.md",
        """
        # QA checklist

        - [ ] Every claim matches research.md and preserves qualifiers.
        - [ ] Every rendered string matches storyboard.md exactly.
        - [ ] Technical English, punctuation, and numbers are correct.
        - [ ] Style matches style-bible.md across all pages.
        - [ ] Character silhouettes, proportions, colors, and accessories match character-bible.md.
        - [ ] Each page teaches one clear point at thumbnail size.
        - [ ] No copied reference subject, logo, signature, watermark, or unrequested text appears.
        - [ ] Rejected variants are in drafts/ and approved pages are numerically ordered.
        - [ ] Caption, sources, bibles, prompt set, and approved pages are ready to package.
        """,
    )

    print(root)


if __name__ == "__main__":
    main()

