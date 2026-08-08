# Style intake and project style bible

Create `style-bible.md` for every new series or materially different visual direction.

## Inputs

Use one or both:

- User-provided images as visual references.
- A written direction such as “soft editorial collage,” “ink-and-watercolor field notes,” or “bright geometric vector comic.”

If a reference image is local, inspect it before describing or using it. Label its role as `style reference`, not `edit target`, unless the user explicitly requests an edit.

## Extraction grid

Record observable attributes without copying subject matter:

```markdown
# Style bible
Series name:
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
```

## Reference abstraction

Describe “uneven heavy ink outline, flat desaturated colors, paper grain, sticker-like scenes” instead of “copy Image 1.” Separate these layers:

1. **Rendering:** medium, edge behavior, fill, depth, texture.
2. **Composition:** density, panels, reading order, negative space.
3. **Typography:** weight, alignment, scale contrast, container shapes.
4. **Mood:** playful, clinical, calm, surreal, energetic, restrained.
5. **Original content:** new characters, new props, new scenes, new layout.

Never import a reference’s characters, branding, text, signature, watermark, or exact composition into the new work.

## No-reference default

If the user gives no style direction, choose a coherent original direction based on topic and audience. State it in one sentence, write the complete style bible, and keep it stable for the episode. Do not default to a style from another Skill or previous user unless the user requests continuity.

## Continuity block

At the end of `style-bible.md`, produce a compact 80–150 word block that can be pasted into every image-generation prompt. Include canvas, medium, line, palette, texture, shape, layout, typography, mood, and exclusions.

