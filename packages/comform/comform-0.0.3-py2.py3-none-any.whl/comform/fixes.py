"""Identify and apply fixes."""

from __future__ import annotations

import re
from typing import List, TextIO, Tuple

from comform.cli import Options
from comform.comments import Chunk, Comment, get_comments, to_chunks
from comform.text import format_as_md

Fixes = List[Tuple[Chunk, Chunk]]


def _get_fixes(chunks: list[Chunk], options: Options) -> Fixes:
    fixes = []
    for chunk in chunks:
        if chunk.inline and not options.align:
            fixes.append((chunk, chunk))
            continue

        if chunk.inline and options.align:
            col_max = max(comment.hash_col for comment in chunk)
            new_chunk = Chunk(Comment(c.text, c.lineno, col_max, True) for c in chunk)
            fixes.append((chunk, new_chunk))
            continue

        if len(chunk) == 1 and not chunk.inline and options.dividers:
            comment = chunk[0]
            match = re.match(r"^ *-*(.+?)-+ *#?$", comment.text)
            if match:
                text = format_as_md(match.group(1), wrap="no").strip()
                text = f" -- {text} ".ljust(options.wrap - len("# #"), "-") + " #"
                new_comment = Comment(text, comment.lineno, comment.hash_col, False)
                fixes.append((chunk, Chunk([new_comment])))
                continue

        text = format_as_md(
            text="\n".join(comment.text for comment in chunk),
            number=True,
            wrap=options.wrap - chunk.hash_col - len("# "),
        ).strip()

        new_chunk = Chunk(
            Comment(f" {line}".rstrip(), chunk.start_lineno + j, chunk.hash_col, False)
            for j, line in enumerate(text.split("\n"))
        )

        fixes.append((chunk, new_chunk))
    return fixes


def _apply_fixes(fixes: Fixes, old_lines: list[str]) -> list[str]:
    new_lines = []

    prev_end_lineno = 0
    for fix in fixes:
        old_chunk, new_chunk = fix
        end_lineno = old_chunk[-1].lineno

        new_lines.extend(old_lines[prev_end_lineno : old_chunk.start_lineno - 1])
        if not old_chunk.inline:
            new_lines.extend(f"#{comment.text}\n" for comment in new_chunk)
        else:
            chunk_code_lines = old_lines[old_chunk.start_lineno - 1 : end_lineno]
            new_lines.extend(
                line[: old_c.hash_col].ljust(new_c.hash_col) + f"#{new_c.text}\n"
                for line, old_c, new_c in zip(chunk_code_lines, old_chunk, new_chunk)
            )

        prev_end_lineno = end_lineno
    return new_lines


def fix_text(stream: TextIO, options: Options) -> tuple[list[str], list[str]]:
    old_comments = list(get_comments(stream))
    stream.seek(0)
    old_lines = stream.readlines()

    chunks = to_chunks(old_comments)
    fixes = _get_fixes(chunks, options)
    new_lines = _apply_fixes(fixes, old_lines)
    return new_lines, old_lines
