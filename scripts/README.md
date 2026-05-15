# Scripts

Helper scripts for building and maintaining the CS50 i18n site.

## translate_vi.py

Translates English content to Vietnamese using the Gemini CLI.

**Setup**

Install [uv](https://github.com/astral-sh/uv) if you don't have it:

```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Make sure `gemini` CLI is installed and authenticated:

```sh
npm install -g @google/gemini-cli
gemini   # follow login prompt
```

**Usage**

```sh
# Translate all files (overwrites existing vi/ files)
uv run scripts/translate_vi.py

# Skip files that already have a Vietnamese version
uv run scripts/translate_vi.py --skip-existing

# Only retranslate notes pages
uv run scripts/translate_vi.py --notes-only
```

Run from the repo root. Output goes to `content/vi/`.

**How it works**

- Files under 3500 bytes are batched 5 at a time into a single Gemini call to save quota.
- Large files (lecture notes) are split by `##` section and each section's prose is translated independently, leaving code blocks untouched.
- Frontmatter keys are preserved; only `title`, `topic`, and `description` values are translated.
- Proper nouns (CS50, Harvard, C, Python, etc.) are kept in English.

After running, review the output in `content/vi/` before committing. Machine translation is a starting point; human review improves quality.
