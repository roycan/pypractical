# SPEC-005 — Class-Based (OOP) Problem Specification

> Addendum to SPEC-001 ([`40-problem-markdown-spec.md`](40-problem-markdown-spec.md))
> and SPEC-002 ([`41-python-template-spec.md`](41-python-template-spec.md)).
> Applies when the assessment's unit of work is a **class** (or a small set of
> related classes) instead of a single function.

## When this spec applies

Use SPEC-005 for any OOP assessment: classes, attributes, methods, encapsulation,
inheritance, polymorphism, abstraction, and object relationships. For
single-function assessments, use SPEC-001 / SPEC-002 unchanged.

## 1. Problem markdown — class-based section order

```text
# Title
## Story
## Task
## Class Specification
### ClassName            (one ### per class: purpose + attributes)
## Required Methods
### ClassName.method(...)  (signature, parameters, return, behavior)
## Constraints
## Example
## Explanation
## Hint
```

Differences from SPEC-001:

- `## Function Specification` becomes `## Class Specification`, with one `###`
  subsection per class stating its purpose and the instance variables it stores.
- A new `## Required Methods` section lists every method the student must write.
  Each method is a `###` heading showing its signature, then its parameters,
  return value, and required behavior.

Everything else (Story, Task, Constraints **before** Example, Example,
Explanation, Hint) follows SPEC-001 exactly.

## 2. Starter code — class-based rules

All SPEC-002 rules apply unless overridden here:

- The **unit of work** is the class (or related classes) defined in the problem,
  not "exactly one public function."
- A **module docstring** identifies the Family and Assessment.
- A **class docstring** gives a one-line purpose for each class.
- A **method docstring** gives purpose, parameters, and return for each method.
- **No type hints.**
- **No `pass`.** Use the placeholder table below.
- A **provided helper function** (when used) is included verbatim with a
  `DO NOT MODIFY` docstring; students never change it.

### Placeholder table (replaces SPEC-002's single return rule)

| Method kind | Placeholder |
|---|---|
| `__init__` | bare `return` |
| returns `bool` | `return False` |
| returns `int` | `return 0` |
| returns `list` | `return []` |
| returns `str` | `return ""` |
| returns an object / `None` | `return None` |
| void / mutator (no return value) | bare `return` |

Rationale: a bare `return` is a valid body that lets the object or method be
constructed without leaking the required logic, so tests fail cleanly until the
student solves it instead of raising a `SyntaxError`.

## 3. Unit tests — class-based rules

SPEC-004 ([`42-unittest-spec.md`](42-unittest-spec.md)) applies fully. Add only:

- Build objects (`recorder = Recorder()`), call methods, and assert **observable
  behavior**: attribute values, return values, and list contents.
- A provided helper function enables integration-level tests (for example, a
  scheduler returning the correct count). These still test documented behavior
  only and introduce no new requirements.

## 4. Reference example

The upgraded TV Recorder problem (`Family-02-Intro-OOP/01-TV-Recorder/`) is the
canonical class-based reference built to this spec.

## Revision history

| Version | Summary |
|---|---|
| 1.0 | Initial class-based addendum (Round 1 foundation). |
