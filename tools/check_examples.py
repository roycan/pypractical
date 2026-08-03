#!/usr/bin/env python3
"""Best-effort worked-example linter for PyPractical.

Walks every problem folder (Family-*/0*/) that has both problem.md and
solution.py, extracts the expected output from the ```text fenced blocks in
the Example section of problem.md, runs solution.py, and compares the two.

Standard library only.
"""
import glob
import os
import subprocess
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def extract_example_section(text):
    """Lines between a '## Example' heading and the next '## ' heading."""
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if line.strip() == "## Example":
            start = i + 1
            break
    if start is None:
        return None
    end = len(lines)
    for j in range(start, len(lines)):
        if lines[j].startswith("## "):
            end = j
            break
    return lines[start:end]


def extract_expected(section):
    """Inner contents of all ```text fenced blocks, joined with '\\n'."""
    if section is None:
        return None
    blocks = []
    i = 0
    n = len(section)
    while i < n:
        if section[i].strip() == "```text":
            i += 1
            block_lines = []
            while i < n and section[i].strip() != "```":
                block_lines.append(section[i])
                i += 1
            blocks.append("\n".join(block_lines))
        i += 1
    if not blocks:
        return None
    return "\n".join(blocks)


def normalize(s):
    """Split into lines, rstrip each, drop trailing empty lines, rejoin."""
    lines = s.split("\n")
    lines = [line.rstrip() for line in lines]
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines)


def main():
    os.chdir(REPO_ROOT)
    print("=== PyPractical Worked-Example Linter ===")
    folders = sorted(
        d for d in glob.glob("Family-*/0*/")
        if os.path.isfile(os.path.join(d, "problem.md"))
        and os.path.isfile(os.path.join(d, "solution.py"))
    )

    p = m = u = 0
    for folder in folders:
        with open(os.path.join(folder, "problem.md"), encoding="utf-8") as f:
            text = f.read()

        section = extract_example_section(text)
        expected_raw = extract_expected(section)

        if expected_raw is None:
            u += 1
            print("%-55s UNPARSEABLE" % folder)
            continue

        result = subprocess.run(
            ["python3", "solution.py"],
            cwd=folder,
            capture_output=True,
            text=True,
        )
        actual_raw = result.stdout

        expected = normalize(expected_raw)
        actual = normalize(actual_raw)

        if expected == actual:
            p += 1
            print("%-55s PASS" % folder)
        else:
            m += 1
            print("%-55s MISMATCH" % folder)
            print("    --- expected (normalized) ---")
            print("    " + expected.replace("\n", "\n    "))
            print("    --- actual (normalized) ---")
            print("    " + actual.replace("\n", "\n    "))

    print("------------------------------------------------------------")
    print("%d PASS, %d MISMATCH, %d UNPARSEABLE" % (p, m, u))
    sys.exit(1 if m > 0 else 0)


if __name__ == "__main__":
    main()
