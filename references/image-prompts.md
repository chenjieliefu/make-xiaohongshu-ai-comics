# Style-neutral image prompt system

## Shared generation scaffold

Replace every bracketed field from the project style and character bibles.

```text
Use case: scientific-educational or illustration-story
Asset type: Page [N] of a Chinese Xiaohongshu AI explainer comic, [aspect ratio].
Input images: [list each image and label it as style reference, character reference, edit target, or supporting insert].
Primary request: [one teaching purpose]
Scene: [one concrete original visual metaphor]
Characters: [paste invariant blocks from character-bible.md]
Style: [paste the compact continuity block from style-bible.md]
Composition: [headline area, information units, character placement, footer, reading order, whitespace].
Text (verbatim):
“[headline]”
“[body]”
“[labels]”
Typography: [project typography behavior], exact characters, high contrast, phone-readable.
Constraints: preserve the project bibles; original scene and composition; no copied reference subjects, logos, signatures, watermarks, extra words, gibberish, duplicated characters, or tiny dense text.
```

## Continuity strategy

- Cover: use the approved style references and all main character sheets.
- Later pages: use the character sheet plus the most relevant approved page when supported.
- Repeat style and character invariant blocks on every call.
- Generate one distinct asset per call.
- Keep the cast small on information-dense pages.

## Exact-text strategy

- Put each literal string in quotation marks on a separate line.
- Reduce the number of distinct strings before reducing font size.
- Spell uncommon English terms exactly and specify capitalization.
- Request no extra text, then inspect the output.

## Targeted correction scaffold

```text
Use case: text-localization or precise-object-edit
Input image: Image 1 is the edit target.
Change only: [one exact localized change].
Match: [existing typography, color, texture, spacing, alignment, lighting].
Invariants: preserve crop, layout, characters, expressions, every other text string, style, palette, borders, and background.
Constraints: no other changes; no extra words; no watermark.
```

Keep the original under `drafts/` and save the corrected page under the approved sequence.

