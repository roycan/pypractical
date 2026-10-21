#!/usr/bin/env python3
"""Verification gates for PyPractical.

Usage:
    python3 tools/verify.py renumber      Gate R: structure + stale-reference audit after
                                          the x10 family renumbering.
    python3 tools/verify.py family DIR    Gate P: one problem folder -- unit tests, worked
                                          example lint, and (for Family-055 problems) the
                                          broken-solution matrix.
    python3 tools/verify.py all           Gate ALL: Gate P for every problem folder in the
                                          repo, then a summary.

Every gate exits 0 only when all checks pass. The broken-solution matrix copies a
problem folder under temp/verify-work/ (git-ignored) and never touches the real
files; the copy is deleted afterwards.

Family numbering convention checked by Gate R:
    folder style   Family-050-Inheritance        (3 digits, zero padded)
    prose style    Family 050                    (3 digits, zero padded)
Any other Family number width (e.g. "Family 5", "Family 05", "Family 50") is
reported as a stale or unpadded reference.
"""

import glob
import os
import re
import shutil
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_examples import extract_example_section, extract_expected, normalize

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMP_WORK = os.path.join(REPO_ROOT, "temp", "verify-work")

VALID_FAMILY_NUMBERS = {10, 20, 30, 40, 50, 55, 60, 70, 80, 90, 100, 110, 120, 130}

EXPECTED_FOLDERS = [
    "Family-010-Minimum-Cost",
    "Family-020-Intro-OOP",
    "Family-030-Classes-and-Objects",
    "Family-040-Encapsulation",
    "Family-050-Inheritance",
    "Family-060-Method-Overriding",
    "Family-070-Polymorphism",
    "Family-080-Abstraction",
    "Family-090-Relationships-Association",
    "Family-100-Relationships-Composition",
    "Family-110-Relationships-Dependency",
    "Family-120-Relationships-Aggregation",
    "Family-130-SOLID-Single-Responsibility",
]

OLD_FOLDERS = [
    "Family-01-Minimum-Cost",
    "Family-02-Intro-OOP",
    "Family-03-Classes-and-Objects",
    "Family-04-Encapsulation",
    "Family-05-Inheritance",
    "Family-06-Method-Overriding",
    "Family-07-Polymorphism",
    "Family-08-Abstraction",
    "Family-09-Relationships-Association",
    "Family-10-Relationships-Composition",
    "Family-11-Relationships-Dependency",
    "Family-12-Relationships-Aggregation",
    "Family-13-SOLID-Single-Responsibility",
]

SCAN_SKIP_DIRS = {"plans", ".git", "temp", "__pycache__", "pics"}
# Files skipped by the stale-reference scan because they intentionally encode
# old family names: CHANGELOG history, and the tools that carry the mapping.
SCAN_SKIP_FILES = {"08-CHANGELOG.md", "verify.py", "renumber_refs.py"}

DELIVERABLES = ["problem.md", "starter.py", "solution.py", "tests.py",
                "teacher_notes.md", "metadata.yml"]


# --- Broken-solution matrix (Family-055 integration family) -------------------
# Each mutation simulates one classic student mistake in solution.py. The gate
# asserts that the named test then FAILS -- proving that test really guards
# its concept. "expected_fails" maps mutation name -> test method name.

def _mutate_drop_inheritance(text, spec):
    """Remove the '(Parent)' part of the child class statement."""
    pattern = r"class\s+%s\s*\(\s*%s\s*\)\s*:" % (re.escape(spec["child"]),
                                                  re.escape(spec["parent"]))
    new_text, count = re.subn(pattern, "class %s():" % spec["child"], text)
    return new_text if count else None


def _mutate_drop_super(text, spec):
    """Delete the super().__init__(...) call."""
    pattern = r"^[ \t]*super\(\)\.__init__\([^\n]*\)[ \t]*\r?\n"
    new_text, count = re.subn(pattern, "", text, flags=re.MULTILINE)
    return new_text if count else None


def _mutate_make_public(text, spec):
    """Turn the protected _attr into a public attr everywhere."""
    attr = "_" + spec["int_attr"]
    pattern = r"(?<![A-Za-z0-9])" + re.escape(attr)
    new_text, count = re.subn(pattern, spec["int_attr"], text)
    return new_text if count else None


def _mutate_boundary(text, spec):
    """Use '< 0' instead of '<= 0', letting zero slip past validation."""
    new_text, count = re.subn(r"<=\s*0", "< 0", text)
    return new_text if count else None


def _mutate_relational_boundary(text, spec):
    """Rewrite the relational bound '<=' against the parent field to '<'.

    Applies to non-isomorphic practice extensions whose validation compares a
    proposed value with inherited parent state (e.g. '<= self.max_speed');
    moving the boundary to '<' wrongly rejects the equal-to-maximum case.
    """
    new_text, count = re.subn(r"<=\s*self\.", "< self.", text)
    return new_text if count else None


MUTATIONS = {
    "drop_inheritance": _mutate_drop_inheritance,
    "drop_super": _mutate_drop_super,
    "make_public": _mutate_make_public,
    "boundary": _mutate_boundary,
    "relational_boundary": _mutate_relational_boundary,
}

# The four classic mutations shared by the isomorphic exam variants (01-04).
# Specs without a "mutations" key run exactly this set, so adding a new mutation
# to MUTATIONS never changes what existing specs are checked against.
DEFAULT_MUTATIONS = ["drop_inheritance", "drop_super", "make_public", "boundary"]

MATRIX_SPECS = {
    "01-Library-Book": {
        "child": "Book", "parent": "Publication", "int_attr": "number_of_pages",
        "expected_fails": {
            "drop_inheritance": "test_book_is_subclass_of_publication",
            "drop_super": "test_book_inherits_title_via_super",
            "make_public": "test_value_stored_in_protected_attribute",
            "boundary": "test_zero_pages_prints_warning",
        },
    },
    "02-Video-Game-Edition": {
        "child": "DeluxeEdition", "parent": "Game", "int_attr": "bonus_levels",
        "expected_fails": {
            "drop_inheritance": "test_deluxe_edition_is_subclass_of_game",
            "drop_super": "test_deluxe_edition_inherits_title_via_super",
            "make_public": "test_value_stored_in_protected_attribute",
            "boundary": "test_zero_bonus_levels_prints_warning",
        },
    },
    "03-Streaming-Account": {
        "child": "PremiumAccount", "parent": "Account", "int_attr": "max_screens",
        "expected_fails": {
            "drop_inheritance": "test_premium_account_is_subclass_of_account",
            "drop_super": "test_premium_account_inherits_email_via_super",
            "make_public": "test_value_stored_in_protected_attribute",
            "boundary": "test_zero_screens_prints_warning",
        },
    },
    "04-Sports-Captain": {
        "child": "Captain", "parent": "Member", "int_attr": "trophies_won",
        "expected_fails": {
            "drop_inheritance": "test_captain_is_subclass_of_member",
            "drop_super": "test_captain_inherits_name_via_super",
            "make_public": "test_value_stored_in_protected_attribute",
            "boundary": "test_zero_trophies_prints_warning",
        },
    },
    "05-Race-Car": {
        "child": "Racer", "parent": "Vehicle", "int_attr": "top_speed",
        "mutations": ["drop_inheritance", "drop_super", "make_public",
                      "relational_boundary"],
        "expected_fails": {
            "drop_inheritance": "test_racer_is_subclass_of_vehicle",
            "drop_super": "test_racer_inherits_name_via_super",
            "make_public": "test_value_stored_in_protected_attribute",
            "relational_boundary": "test_top_speed_equal_to_max_is_valid",
        },
    },
}


# --- Helpers -----------------------------------------------------------------

def _read_text(path):
    """Return the file's text, or None when it is not UTF-8 text."""
    try:
        with open(path, encoding="utf-8") as handle:
            return handle.read()
    except (UnicodeDecodeError, OSError):
        return None


def _iter_scan_files():
    """Yield living text files that are scanned for stale references."""
    for dirpath, dirnames, filenames in os.walk(REPO_ROOT):
        dirnames[:] = [d for d in dirnames if d not in SCAN_SKIP_DIRS]
        for name in sorted(filenames):
            if name in SCAN_SKIP_FILES:
                continue
            path = os.path.join(dirpath, name)
            if _read_text(path) is not None:
                yield os.path.relpath(path, REPO_ROOT)


def _run_unittest(workdir, verbose=False):
    """Run 'python3 -m unittest tests' inside workdir; return the CompletedProcess."""
    args = [sys.executable, "-m", "unittest", "tests"]
    if verbose:
        args.append("-v")
    return subprocess.run(args, cwd=workdir, capture_output=True, text=True)


def _unittest_summary(result):
    """Return (ran_count_or_None, passed_bool, failed_test_names)."""
    output = result.stdout + result.stderr
    match = re.search(r"Ran (\d+) tests?", output)
    ran = int(match.group(1)) if match else None
    passed = result.returncode == 0 and re.search(r"^OK", output, re.MULTILINE) is not None
    failed_names = re.findall(r"^(?:FAIL|ERROR): (\S+)", output, re.MULTILINE)
    return ran, passed, failed_names


# --- Gate R: renumber --------------------------------------------------------

def gate_renumber():
    """Structure + stale-reference audit. Returns True when everything passes."""
    problems = []

    for folder in EXPECTED_FOLDERS:
        if not os.path.isdir(os.path.join(REPO_ROOT, folder)):
            problems.append("missing expected folder: %s" % folder)
    for folder in OLD_FOLDERS:
        if os.path.isdir(os.path.join(REPO_ROOT, folder)):
            problems.append("old folder still present: %s" % folder)

    re_ok = re.compile(r"Family[-\s]+\d{3}(?![0-9])")
    re_short = re.compile(r"Family[-\s]+\d{1,2}(?![0-9])")
    re_long = re.compile(r"Family[-\s]+\d{4,}")
    re_number = re.compile(r"Family[-\s]+(\d{3})(?![0-9])")

    for rel_path in _iter_scan_files():
        text = _read_text(os.path.join(REPO_ROOT, rel_path))
        if text is None:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            where = "%s:%d" % (rel_path, lineno)
            for match in re_short.finditer(line):
                problems.append("%s stale/unpadded family reference %r -- "
                                "use 3 digits, e.g. 'Family 050'" % (where, match.group(0)))
            for match in re_long.finditer(line):
                problems.append("%s oversized family reference %r" % (where, match.group(0)))
            for match in re_number.finditer(line):
                if int(match.group(1)) not in VALID_FAMILY_NUMBERS:
                    problems.append("%s unknown family number %r" % (where, match.group(0)))

    for problem in problems:
        print("  FAIL  %s" % problem)
    print("Gate R (renumber): %s" % ("PASS" if not problems else "FAIL"))
    return not problems


# --- Gate P: one problem folder ----------------------------------------------

def _check_deliverables(problem_dir):
    missing = [name for name in DELIVERABLES
               if not os.path.isfile(os.path.join(problem_dir, name))]
    return missing


def _check_example(problem_dir):
    """Compare the problem.md Example text block with solution.py's output."""
    text = _read_text(os.path.join(problem_dir, "problem.md"))
    expected_raw = extract_expected(extract_example_section(text))
    if expected_raw is None:
        return False, "no parseable ```text block in the Example section"
    result = subprocess.run([sys.executable, "solution.py"], cwd=problem_dir,
                            capture_output=True, text=True)
    if normalize(expected_raw) == normalize(result.stdout):
        return True, "example output matches solution.py"
    return False, ("example output differs from solution.py\n"
                   "    --- expected ---\n%s\n    --- actual ---\n%s"
                   % (normalize(expected_raw), normalize(result.stdout)))


def _check_matrix(problem_dir, spec):
    """Run every mutation on a temp copy; each must fail its expected test."""
    all_ok = True
    with open(os.path.join(problem_dir, "solution.py"), encoding="utf-8") as handle:
        original = handle.read()

    for name in spec.get("mutations", DEFAULT_MUTATIONS):
        mutate = MUTATIONS.get(name)
        if mutate is None:
            print("  FAIL  matrix.%s: unknown mutation name" % name)
            all_ok = False
            continue

        expected_test = spec["expected_fails"].get(name)
        if expected_test is None:
            print("  FAIL  matrix.%s: no expected test in the spec" % name)
            all_ok = False
            continue

        mutated = mutate(original, spec)
        if mutated is None:
            print("  FAIL  matrix.%s: mutation did not apply -- solution.py drifted "
                  "from the canonical form" % name)
            all_ok = False
            continue

        work = os.path.join(TEMP_WORK, "%s--%s" % (os.path.basename(problem_dir), name))
        if os.path.isdir(work):
            shutil.rmtree(work)
        shutil.copytree(problem_dir, work, ignore=shutil.ignore_patterns("__pycache__"))
        with open(os.path.join(work, "solution.py"), "w", encoding="utf-8") as handle:
            handle.write(mutated)

        result = _run_unittest(work, verbose=True)
        _, _, failed_names = _unittest_summary(result)
        shutil.rmtree(work)

        if expected_test in failed_names:
            print("  ok    matrix.%s: '%s' fails as intended" % (name, expected_test))
        else:
            all_ok = False
            print("  FAIL  matrix.%s: expected '%s' to fail, but failing tests were: %s"
                  % (name, expected_test, failed_names or "none"))
    return all_ok


def gate_problem(problem_dir, label):
    """Gate P for one problem folder. Returns True when everything passes."""
    print("-- %s" % label)
    ok = True

    missing = _check_deliverables(problem_dir)
    if missing:
        print("  FAIL  missing deliverables: %s" % ", ".join(missing))
        ok = False
    else:
        print("  ok    deliverables complete")

    result = _run_unittest(problem_dir)
    ran, passed, failed_names = _unittest_summary(result)
    if passed:
        print("  ok    unit tests (%s tests)" % ran)
    else:
        ok = False
        print("  FAIL  unit tests: ran=%s failed=%s" % (ran, failed_names or "see output"))
        tail = (result.stdout + result.stderr).strip().splitlines()[-15:]
        for line in tail:
            print("        %s" % line)

    example_ok, example_msg = _check_example(problem_dir)
    if example_ok:
        print("  ok    worked example: %s" % example_msg)
    else:
        ok = False
        print("  FAIL  worked example: %s" % example_msg)

    spec = MATRIX_SPECS.get(os.path.basename(problem_dir))
    is_family_055 = "Family-055" in problem_dir
    if spec is not None:
        if _check_matrix(problem_dir, spec):
            mutation_count = len(spec.get("mutations", DEFAULT_MUTATIONS))
            print("  ok    broken-solution matrix (%d mutations)" % mutation_count)
        else:
            ok = False
    elif is_family_055:
        ok = False
        print("  FAIL  broken-solution matrix: no MATRIX_SPECS entry for %s"
              % os.path.basename(problem_dir))
    else:
        print("  --    broken-solution matrix: not applicable (pre-Family-055 problem)")

    return ok


# --- Gate ALL ----------------------------------------------------------------

def _problem_dirs():
    dirs = sorted(glob.glob(os.path.join(REPO_ROOT, "Family-*", "0*")))
    return [d for d in dirs if all(
        os.path.isfile(os.path.join(d, name)) for name in ("problem.md", "solution.py", "tests.py"))]


def gate_all():
    """Gate P for every problem folder; returns True when all pass."""
    if os.path.isdir(TEMP_WORK):
        shutil.rmtree(TEMP_WORK)
    os.makedirs(TEMP_WORK, exist_ok=True)

    dirs = _problem_dirs()
    passed = failed = 0
    for problem_dir in dirs:
        label = os.path.relpath(problem_dir, REPO_ROOT)
        if gate_problem(problem_dir, label):
            passed += 1
        else:
            failed += 1
    shutil.rmtree(TEMP_WORK, ignore_errors=True)

    print("=" * 60)
    print("Gate ALL: %d problem folders | %d PASS | %d FAIL" % (len(dirs), passed, failed))
    return failed == 0


# --- Entry point -------------------------------------------------------------

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        return 2
    command = sys.argv[1]

    if command == "renumber":
        return 0 if gate_renumber() else 1

    if command == "family":
        if len(sys.argv) < 3:
            print("usage: python3 tools/verify.py family <problem-dir>")
            return 2
        problem_dir = sys.argv[2]
        if not os.path.isabs(problem_dir):
            problem_dir = os.path.join(REPO_ROOT, problem_dir)
        if not os.path.isdir(problem_dir):
            print("no such problem folder: %s" % problem_dir)
            return 2
        os.makedirs(TEMP_WORK, exist_ok=True)
        try:
            ok = gate_problem(problem_dir, os.path.relpath(problem_dir, REPO_ROOT))
        finally:
            shutil.rmtree(TEMP_WORK, ignore_errors=True)
        return 0 if ok else 1

    if command == "all":
        return 0 if gate_all() else 1

    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main())
