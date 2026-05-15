#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""
Translate CS50 English content to Simplified Chinese using Gemini CLI.
Strategy:
  - Batch multiple small files (<3000 chars) into one Gemini call
  - For large files (notes), send as single call — code blocks preserved
  - Skip files that already exist in zh/ with --skip-existing
Run from repo root: uv run scripts/translate_zh.py --skip-existing
"""

import re
import subprocess
import sys
from pathlib import Path

SRC = Path(__file__).parent.parent / "content/en"
DST = Path(__file__).parent.parent / "content/zh"

BATCH_PROMPT = """Translate the following CS50 course Markdown files from English to Simplified Chinese (简体中文).

STRICT RULES:
1. Keep all YAML frontmatter KEYS unchanged — only translate VALUES of: title, topic, description
2. Keep ALL code blocks (```...```) EXACTLY unchanged — never translate code
3. Keep ALL Hugo shortcodes like {{< youtube ID >}} unchanged
4. Keep ALL URLs, image paths, and hyperlinks unchanged
5. Keep proper nouns unchanged: CS50, Harvard, David Malan, Scratch, C, Python, SQL, JavaScript, HTML, CSS, R
6. Write fluent, natural Simplified Chinese — as a skilled Chinese CS educator would write
7. Output ONLY the translated files separated by ---FILE-SEPARATOR--- markers, no extra commentary

"""

LARGE_FILE_PROMPT = """Translate this CS50 course Markdown file from English to Simplified Chinese (简体中文).

STRICT RULES:
1. Keep all YAML frontmatter KEYS unchanged — only translate VALUES of: title, topic, description
2. Keep ALL code blocks (```...```) EXACTLY unchanged — never translate code inside them
3. Keep ALL Hugo shortcodes like {{< youtube ID >}} unchanged
4. Keep ALL URLs, image paths, and hyperlinks unchanged
5. Keep proper nouns unchanged: CS50, Harvard, David Malan, Scratch, C, Python, SQL, JavaScript, HTML, CSS, R
6. Write fluent, natural Simplified Chinese — as a skilled Chinese CS educator would write
7. Output ONLY the translated markdown, nothing else

"""


def run_gemini(prompt: str) -> str:
    result = subprocess.run(
        ["gemini", "-p", prompt],
        capture_output=True,
        text=True,
        timeout=300,
    )
    out = result.stdout
    # Strip MCP warning lines wherever they appear (may or may not have trailing newline)
    out = re.sub(r'MCP issues detected[^\n]*\n?', '', out)
    out = out.strip()
    if not out:
        raise RuntimeError(f"Gemini returned empty output (stderr: {result.stderr[:200]})")
    return out


def ensure_frontmatter(text: str) -> str:
    """Ensure file starts with --- and fix quoted booleans."""
    text = text.strip()
    if not text.startswith('---'):
        text = '---\n' + text
    text = re.sub(r'^(draft):\s*"(true|false)"', lambda m: f'{m.group(1)}: {m.group(2)}', text, flags=re.MULTILINE)
    return text


def translate_large_file(raw: str) -> str:
    return run_gemini(LARGE_FILE_PROMPT + raw)


def batch_translate(batch: list[tuple[Path, Path]]) -> None:
    parts = []
    for src, _ in batch:
        parts.append(f"FILE: {src.name}\n{src.read_text(encoding='utf-8')}")

    combined = "\n\n---FILE-SEPARATOR---\n\n".join(parts)
    prompt = BATCH_PROMPT + "Translate each file. Separate outputs with ---FILE-SEPARATOR--- exactly.\n\n" + combined

    output = run_gemini(prompt)
    outputs = output.split('---FILE-SEPARATOR---')

    for i, (src, dst) in enumerate(batch):
        dst.parent.mkdir(parents=True, exist_ok=True)
        translated = outputs[i].strip() if i < len(outputs) else src.read_text()
        translated = re.sub(r'^FILE:\s*\S+\s*\n', '', translated)
        translated = ensure_frontmatter(translated)
        dst.write_text(translated + '\n', encoding='utf-8')


def process_large(src: Path, dst: Path) -> None:
    dst.parent.mkdir(parents=True, exist_ok=True)
    raw = src.read_text(encoding='utf-8')
    if len(raw.strip()) < 20:
        dst.write_text(raw, encoding='utf-8')
        return
    translated = ensure_frontmatter(translate_large_file(raw))
    dst.write_text(translated + '\n', encoding='utf-8')


def main():
    skip_existing = '--skip-existing' in sys.argv
    notes_only = '--notes-only' in sys.argv
    batch_size = 5

    all_files = sorted(SRC.rglob('*.md'))

    small_q: list[tuple[Path, Path]] = []
    large_q: list[tuple[Path, Path]] = []

    for src in all_files:
        rel = src.relative_to(SRC)
        dst = DST / rel
        if skip_existing and dst.exists():
            continue
        if notes_only and 'notes' not in str(rel):
            continue
        size = src.stat().st_size
        if size > 3500:
            large_q.append((src, dst))
        else:
            small_q.append((src, dst))

    total = len(small_q) + len(large_q)
    batch_calls = (len(small_q) + batch_size - 1) // batch_size
    print(f"Files: {len(small_q)} small (→{batch_calls} batched calls), {len(large_q)} large (one-shot)")
    print(f"Gemini calls estimate: ~{batch_calls + len(large_q)}\n")

    done = 0

    for i in range(0, len(small_q), batch_size):
        batch = small_q[i:i+batch_size]
        names = ', '.join(str(s.relative_to(SRC)) for s, _ in batch)
        print(f"[small {i//batch_size+1}/{batch_calls}] {names} ... ", end='', flush=True)
        try:
            batch_translate(batch)
            print("done")
        except Exception as e:
            print(f"FAILED: {e}")
            for src, dst in batch:
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_text(src.read_text(), encoding='utf-8')
        done += len(batch)

    for j, (src, dst) in enumerate(large_q):
        rel = src.relative_to(SRC)
        print(f"[large {j+1}/{len(large_q)}] {rel} ... ", end='', flush=True)
        try:
            process_large(src, dst)
            print("done")
        except Exception as e:
            print(f"FAILED: {e}")
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_text(src.read_text(), encoding='utf-8')
        done += 1

    print(f"\nCompleted {done}/{total} files.")


if __name__ == '__main__':
    main()
