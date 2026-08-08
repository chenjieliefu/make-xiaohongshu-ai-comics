# Contributing

Thank you for helping improve Make Xiaohongshu AI Comics.

## Good contributions

- Fix an inaccurate or ambiguous workflow instruction.
- Improve multilingual or in-image text QA.
- Add a style-neutral story structure or project template.
- Improve character-continuity guidance.
- Make the scaffolding script safer or easier to use.
- Improve accessibility and mobile readability.

Do not contribute copyrighted reference images, copied characters, logos, signatures, watermarks, or a mandatory house style.

## Before opening a pull request

1. Keep SKILL.md concise and move detailed guidance into references.
2. Update the relevant reference when changing behavior.
3. Keep all visual-style fields configurable.
4. Test the project scaffold:

~~~bash
python3 scripts/new_comic_project.py \
  --topic "RAG" \
  --series "Test Series" \
  --output "/tmp/xhs-ai-comic-test"
~~~

5. Confirm a second run against the same non-empty directory is rejected.
6. Check that no private artwork, credentials, caches, or generated episode files are included.

## Pull request checklist

- Explain what changed and why.
- Describe the creator or reader benefit.
- List the validation performed.
- Keep unrelated changes out of the pull request.
- Preserve factual qualifiers and the style-adaptive design.

By contributing, you agree that your contribution is licensed under the MIT License.

