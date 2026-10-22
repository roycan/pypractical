# Plan — Family-055 Design B: `@property` + `@name.setter` for the Exam Variants

> Scope: exam problems `01-Library-Book`, `02-Video-Game-Edition`, `03-Streaming-Account`
> (and `04-Sports-Captain` if isomorphism is to be preserved — see Decision Points).
> `05-Race-Car` is out of scope (non-isomorphic practice extension).
>
> This plan reverses decision **D2** ("no setters") from
> [`plans/family-055-encapsulation-inheritance-plan.md`](plans/family-055-encapsulation-inheritance-plan.md:17).
> The old plan is a historical record and stays untouched; the reversal is recorded in
> the family README and [`inceptions/context.md`](inceptions/context.md).

## Goal

Replace the plain method getter (`get_number_of_pages()`) in the encapsulation half of
each exam problem with a `@property` getter plus a `@number_of_pages.setter`, and route
the constructor through the setter so the setter is exercised from the first line. Add
one post-construction test per problem that proves the setter validates. Update the
broken-solution matrix in [`tools/verify.py`](tools/verify.py:80) accordingly.

## Canonical solution shape (per problem)

```python
class Book(Publication):
    """Represents a book with a protected page count."""

    def __init__(self, title, author, number_of_pages):
        super().__init__(title, author)
        self.number_of_pages = number_of_pages   # routes through the setter

    @property
    def number_of_pages(self):
        """Return the protected page count."""
        return self._number_of_pages

    @number_of_pages.setter
    def number_of_pages(self, value):
        """Validate and store the page count."""
        if value <= 0:
            print("The number of pages must be positive")
            self._number_of_pages = 0
        else:
            self._number_of_pages = value
```

Substitutions per problem:

| Problem | Child | Property | Warning message |
|---|---|---|---|
| 01 | `Book` | `number_of_pages` | The number of pages must be positive |
| 02 | `DeluxeEdition` | `bonus_levels` | The number of bonus levels must be positive |
| 03 | `PremiumAccount` | `max_screens` | The number of screens must be positive |
| 04 | `Captain` | `trophies_won` | The number of trophies must be positive |

## Why this shape

- The constructor assigns `self.<prop> = ...`, so the setter runs during construction —
  the setter is live, not dead code.
- Matches SG 8's own `Student` pattern (default first, then delegate to the setter).
- No new story element: same domain, same validation, same observable output.

## Files changed per problem

| File | Change |
|---|---|
| `solution.py` | getter → `@property`; add `@<prop>.setter`; `__init__` routes through setter; demo uses `book.<prop>` |
| `starter.py` | TODOs restructured: inherit, `super()`, assign via property, `@property` getter, `@<prop>.setter` |
| `tests.py` | `get_<prop>()` → `.<prop>`; add `_assignment_output` helper; add `test_post_construction_update_validates` |
| `problem.md` | Required Methods rewritten; Example code uses `.<prop>`; Explanation + Hint mention the decorators |
| `teacher_notes.md` | Concepts, Common Mistakes, Strategy, test count |
| `metadata.yml` | add `@property`, `setters` to concepts |

## Test changes

- 12 → 13 tests (5 inheritance / 6 encapsulation / 1 integration / 1 hidden).
- New helper `_assignment_output(obj, attr, value)` captures stdout during assignment.
- New test:

```python
def test_post_construction_update_validates(self):
    book = Book("Clean Code", "R. Martin", 464)
    out = _assignment_output(book, "number_of_pages", -5)
    self.assertIn("positive", out.lower())
    self.assertEqual(book.number_of_pages, 0)
```

This test fails for a read-only property (`AttributeError`) and for a non-validating
setter — it is what makes `@name.setter` genuinely assessed.

## Broken-solution matrix changes ([`tools/verify.py`](tools/verify.py:80))

New mutations:

```python
def _mutate_no_property(text, spec):
    """Remove the '@property' decorator, turning the getter into a plain method."""
    new_text, count = re.subn(r"^[ \t]*@property[ \t]*\r?\n", "", text, flags=re.MULTILINE)
    return new_text if count else None


def _mutate_setter_no_validate(text, spec):
    """Force the setter's guard to never trigger, so it stores invalid values."""
    new_text, count = re.subn(r"if\s+\w+\s*<=\s*0\s*:", "if False:", text)
    return new_text if count else None
```

`DEFAULT_MUTATIONS` becomes:

```python
DEFAULT_MUTATIONS = ["drop_inheritance", "drop_super", "no_property",
                     "setter_no_validate", "boundary"]
```

`make_public` is removed from the default set (renaming the backing field to the property
name causes infinite recursion in the getter) but kept in `MUTATIONS` for `05-Race-Car`,
which still uses a plain getter.

Expected failures per exam variant:

| Mutation | Test that must fail |
|---|---|
| `drop_inheritance` | `test_<child>_is_subclass_of_<parent>` |
| `drop_super` | `test_<child>_inherits_<first_attr>_via_super` |
| `no_property` | `test_value_stored_in_protected_attribute` |
| `setter_no_validate` | `test_post_construction_update_validates` |
| `boundary` | `test_zero_<attr>_prints_warning` |

## Decision points

1. **04-Sports-Captain isomorphism.** 01–04 are documented as isomorphic exam variants.
   Updating only 01–03 makes 04 a Design A outlier. Recommend updating 04 too (keeps the
   family equivalent); otherwise 04 needs its own mutation list and a README note.
2. **05-Race-Car** stays Design A (plain getter) — it is the non-isomorphic practice
   extension, so divergence is intentional.
3. **SPEC-005 / STD-001.** STD-001 says avoid decorators "unless explicit objectives";
   SG 8 makes `@property` explicit, so add a one-line carve-out note to
   [`43-oop-class-spec.md`](43-oop-class-spec.md) and the style standard.
4. **Plan D2 reversal.** Record the reversal in the family README Revision History and
   [`inceptions/context.md`](inceptions/context.md).

## Verification

- `python3 tools/verify.py family Family-055-Encapsulation-Inheritance/01-Library-Book`
  (and 02, 03, 04) — tests + example lint + 5-mutation matrix.
- `python3 tools/verify.py all` — full repo green.
- Manually confirm each Example `text` block still matches `python3 solution.py`.
- Confirm test counts: 01–04 at 13 tests each.

## Risks

- **Recursion bug**: a student writing `self.number_of_pages = value` inside the setter
  gets `RecursionError`; document in teacher_notes.
- **Missing setter**: `AttributeError: can't set attribute` on the post-construction test.
- **Example gate**: the `text` block is unchanged, but the `python` block and the
  solution demo must both switch to `.<prop>`.
- **Test balance**: encapsulation tests go 5 → 6; update the README's balance note.
