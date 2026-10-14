#!/usr/bin/env python3
"""One-shot reference sweep for the x10 family renumbering.

Rewrites every family reference in living documents from the old numbering
(Family-01 / Family 01 / Family 1) to the zero-padded x10 scheme
(Family-010 / Family 010). Folder-style and prose-style references are both
handled by one rule that preserves the separator.

Skipped on purpose (they encode old names as data or history):
    plans/                 historical round records
    08-CHANGELOG.md        history entries keep the names as they were
    tools/verify.py        OLD_FOLDERS lists old names as must-not-exist data
    tools/renumber_refs.py this script's mapping table

Special fixes applied before the general sweep:
    * stale TV-Recorder path Family-02-Intro-OOP/01-TV-Recorder is corrected
      to its real home Family-030-Classes-and-Objects/01-TV-Recorder
    * website/assets/data/curriculum-data.js 'num: N' fields are renumbered

Usage:
    python3 tools/renumber_refs.py             apply (prints every change)
    python3 tools/renumber_refs.py --dry-run   show what would change

One-shot guard: refuses to run when zero-padded family folders already exist.
"""

import glob
import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SKIP_DIRS = {"plans", ".git", "temp", "__pycache__", "pics"}
SKIP_FILES = {"08-CHANGELOG.md", "verify.py", "renumber_refs.py"}

OLD_TO_NEW = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70,
              8: 80, 9: 90, 10: 100, 11: 110, 12: 120, 13: 130}

SPECIAL_FIXES = [
    ("Family-02-Intro-OOP/01-TV-Recorder",
     "Family-030-Classes-and-Objects/01-TV-Recorder"),
]

# Matches "Family-05-..." / "Family 05" / "Family 5" but never 3-digit numbers.
FAMILY_RE = re.compile(r"Family([-\s]+)(\d{1,2})(?![0-9])")
# Family entries only ('id: "f01", num: 1'); stage entries ('id: "s1", num: 1')
# must NOT be renumbered -- their numbering is the stage order, not the family.
NUM_FIELD_RE = re.compile(r'(\bid: "f\d+", num: )(\d+)')
CURRICULUM_DATA = os.path.join("website", "assets", "data", "curriculum-data.js")


def _replace_family(match):
    sep, digits = match.group(1), match.group(2)
    number = int(digits)
    if number in OLD_TO_NEW:
        return "Family%s%03d" % (sep, OLD_TO_NEW[number])
    return match.group(0)


def _replace_num_field(match):
    number = int(match.group(2))
    if number in OLD_TO_NEW:
        return "%s%d" % (match.group(1), OLD_TO_NEW[number])
    return match.group(0)


def _iter_text_files():
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in sorted(filenames):
            if name in SKIP_FILES:
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8", newline="") as handle:
                    handle.read()
            except (UnicodeDecodeError, OSError):
                continue
            yield path


def main():
    dry_run = "--dry-run" in sys.argv

    # Content-based one-shot guard: the sweep may run only while old-style
    # references still exist. (Folder names cannot be used: the folders may
    # already be moved by 'git mv' before the sweep runs.)
    old_refs = 0
    for path in _iter_text_files():
        with open(path, encoding="utf-8", newline="") as handle:
            text = handle.read()
        for match in FAMILY_RE.finditer(text):
            if int(match.group(2)) in OLD_TO_NEW:
                old_refs += 1
    if old_refs == 0:
        print("refusing to run: no old-style family references found -- "
              "the sweep has already been applied (this script is one-shot).")
        return 1

    changed_files = 0
    total_replacements = 0

    for path in _iter_text_files():
        with open(path, encoding="utf-8", newline="") as handle:
            text = handle.read()
        original = text

        for old, new in SPECIAL_FIXES:
            if old in text:
                text = text.replace(old, new)

        text = FAMILY_RE.sub(_replace_family, text)

        if os.path.relpath(path, REPO_ROOT).replace(os.sep, "/") == CURRICULUM_DATA:
            text = NUM_FIELD_RE.sub(_replace_num_field, text)

        if text == original:
            continue

        changes = sum(1 for a, b in zip(original.splitlines(), text.splitlines()) if a != b)
        changed_files += 1
        total_replacements += changes
        rel = os.path.relpath(path, REPO_ROOT)
        print("%-60s %d line(s) changed" % (rel, changes))

        if not dry_run:
            with open(path, "w", encoding="utf-8", newline="") as handle:
                handle.write(text)

    print("-" * 60)
    mode = "would change" if dry_run else "changed"
    print("%d file(s) %s, %d line(s) total" % (changed_files, mode, total_replacements))
    return 0


if __name__ == "__main__":
    sys.exit(main())
