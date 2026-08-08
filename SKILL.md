---
name: make-xiaohongshu-ai-comics
description: Create accurate, entertaining multi-page Xiaohongshu AI explainer comics in a user-selected or user-referenced visual style, with original repeatable characters, structured storyboards, exact text, image-generation prompts, review, and packaging. Use when Codex needs to turn an AI term into a comic note, adapt to different visual directions, infer high-level style attributes from supplied images without copying protected elements, maintain character continuity across pages or episodes, or design and register new characters.
---

# Make Xiaohongshu AI Comics

Turn an AI concept into a swipeable educational comic while treating visual style and characters as project-specific inputs rather than built-in defaults.

## Required resources

Read only the references needed for the task:

- Always read [style-intake.md](references/style-intake.md), [character-bible-template.md](references/character-bible-template.md), [story-architecture.md](references/story-architecture.md), and [accuracy-and-copy.md](references/accuracy-and-copy.md).
- Read [image-prompts.md](references/image-prompts.md) before generating or editing images.
- Read [new-character-protocol.md](references/new-character-protocol.md) when creating or adding a character.

This Skill intentionally contains no bundled house style, fixed palette, reference art, or named recurring character.

For image generation or editing, also use the available `imagegen` skill and follow its instructions. Inspect every local image reference or edit target before using it. Use the built-in image generation path unless the user explicitly requests another path.

## Workflow

### 1. Establish the episode brief

Extract the topic, target reader, desired depth, page count, call to action, visual direction, provided reference images, and required or forbidden claims. If the topic and style are clear, proceed without asking. Default to eight 3:4 pages and general AI-curious readers.

Optionally scaffold the working folder:

```bash
python3 scripts/new_comic_project.py --topic "<topic>" --output "<output-directory>"
```

### 2. Create a project-specific style bible

Follow `style-intake.md`.

- If images are supplied, inspect them and record high-level attributes: medium, line, palette behavior, texture, shapes, layout, typography, mood, motifs, and exclusions.
- Treat images as references unless the user explicitly requests an edit.
- Do not copy characters, logos, signature marks, watermarks, text, or exact composition from a reference.
- If only a text direction is supplied, translate it into the same style-bible fields.
- If no visual direction is supplied, choose one coherent, original direction suitable for the audience and state the choice before generating.

Freeze the style bible for the episode. Do not let later pages drift into a different medium, palette, rendering depth, or typographic system.

### 3. Research before writing

Browse when the topic is current, niche, high stakes, externally referenced, or likely to have changed. Prefer official documentation, standards, original papers, and first-party technical sources.

Record a definition, boundaries, a relatable example, common misconceptions, limitations, and source URLs. Do not invent statistics, salaries, benchmarks, quotes, or guaranteed outcomes.

### 4. Write the complete copy before generating images

Use `story-architecture.md` unless the topic needs a shorter arc. Make each page teach one claim. Keep on-image copy concise and phone-readable.

Create:

- `brief.md`
- `research.md`
- `style-bible.md`
- `character-bible.md`
- `storyboard.md`
- `generation-prompts.md`
- `publish-caption.md`
- `qa-checklist.md`

Review the meaning before rendering. Preserve important qualifiers.

### 5. Design and freeze original characters

Use `character-bible-template.md`. Give each recurring character a teaching function, distinct silhouette, invariant colors and accessories, and a short personality definition.

Generate or approve a reference sheet before creating a multi-page episode. Never rely on character names alone for continuity. Repeat the invariant block and use the approved sheet as a reference on every relevant generation call.

When adding a character later, use `new-character-protocol.md`; do not silently redesign the existing cast.

### 6. Generate page by page

Build prompts from `image-prompts.md`.

1. Use the approved style and character references on the cover.
2. For later pages, include the reference sheet plus the most recent approved page needed for continuity.
3. Restate the exact style profile, character invariants, layout, and verbatim text on every call.
4. Generate one distinct page per call.
5. Save approved PNGs under `pages/` with numeric prefixes.
6. Preserve rejected versions under `drafts/`; do not overwrite silently.

### 7. Review every page

Inspect at full size and thumbnail size. Verify:

- exact Chinese, punctuation, numbers, and English terms;
- one clear teaching point and intact qualifiers;
- stable visual style across the episode;
- recurring character silhouette, proportions, colors, and accessories;
- readable information hierarchy and sufficient whitespace;
- no copied reference characters, logos, signatures, watermarks, or unrequested text.

Use a targeted edit for a localized error. Re-state all invariants and change only one thing. Update the storyboard whenever a semantic correction changes the image text.

### 8. Package the episode

Deliver ordered 3:4 PNGs, title/caption/hashtags, storyboard, exact prompt set, knowledge sources, style bible, character bible, and a ZIP containing approved assets only.

Report saved paths and state the image-generation path used.

## Non-negotiable rules

- Do not impose a bundled aesthetic; derive the style for each project.
- Do not equate visual similarity with copying. Abstract reference attributes and create original subjects, scenes, layouts, and characters.
- Do not distort AI terms for a joke or metaphor.
- Do not claim prompting alone can repair missing facts, unsuitable models, missing tools, or undefined goals.
- Do not finalize known text corruption.
- Do not use source citations inside the art unless requested; place them in source notes or the post caption.

