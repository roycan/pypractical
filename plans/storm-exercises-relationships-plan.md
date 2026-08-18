# Storm Exercises — Class Relationships Plan

> **Context:** Storm season — classes suspended or done asynchronously. Grade 9 students
> need simple, self-contained, auto-gradable exercises on class relationships.
>
> **Date:** 2026-08-18
> **Status:** Draft — awaiting user approval

---

## Scope Summary

8 problems across 5 topics. Each problem is a full package (6 deliverables):

- `problem.md` — SPEC-001 + SPEC-005 (class-based)
- `starter.py` — SPEC-002 + SPEC-005 (no type hints, no `pass`, placeholder returns)
- `solution.py` — STD-001 (readable, beginner-friendly)
- `tests.py` — SPEC-004 (behavior-based, equal weight, deterministic)
- `teacher_notes.md` — objectives, reinforced concepts, common mistakes, teaching strategy
- `metadata.yml` — SPEC-003 (title, family, difficulty, concepts, etc.)

---

## Association Progression (4 problems, Family-09)

The teacher can dose these out over successive sessions:

```
Basic has-a (2/5) → 1:1 (3/5) → N:M single-side (3/5) → N:M both-sides (4/5)
```

The existing Family-09 problems (01-Library, 02-Classroom, 03-Playlist, 04-Team-Roster)
already cover 1:N association, completing the full spectrum.

---

## Problem 1 — Basic Association (extends Family-09)

**Family:** Family-09-Relationships-Association
**Folder:** `05-Student-Locker/`
**Difficulty:** 2/5
**Time:** ~15 min

### Story

Every student is assigned one locker. A locker has a number and a combination.
The student stores their locker — the simplest form of association: one object
holds a reference to another.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Locker` | Provided | No — complete |
| `Student` | Container | **Yes** |

### What the student implements

`Locker` (provided) stores a number and combination, with `get_number()` and
`get_combination()`. `Student` stores a name and optionally a `Locker`. Methods:

- `Student.__init__(name)` — store name, set locker to `None`
- `Student.assign_locker(locker)` — store the given `Locker`
- `Student.get_locker_number()` — return the locker's number, or `"No locker"` if none
- `Student.has_locker()` — return `True` if a locker is assigned

### Key concept

Basic has-a: one object stores a reference to another. The student may or may not
have a locker — the code must handle both cases.

---

## Problem 2 — 1:1 Association (extends Family-09)

**Family:** Family-09-Relationships-Association
**Folder:** `06-Person-ID/`
**Difficulty:** 3/5
**Time:** ~20 min

### Story

A person carries exactly one ID card. A person and their ID card are linked
one-to-one — each person has one card, and each card belongs to one person.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `IDCard` | Provided | No — complete |
| `Person` | Container | **Yes** |

### What the student implements

`Person` stores a single `IDCard` object (initially `None`). Methods:

- `set_id_card(card)` — store the given `IDCard`
- `get_id_card()` — return the stored `IDCard` (or `None`)
- `get_id_number()` — return the card's number, or `"No ID"` if no card is set

### Key concept

One-to-one: one person holds exactly one card at a time. The card reference is a
single object, not a list. The card can be replaced.

---

## Problem 3a — N:M Association, Single-Side (extends Family-09)

**Family:** Family-09-Relationships-Association
**Folder:** `07-Student-Club/`
**Difficulty:** 3/5
**Time:** ~20 min
**Purpose:** Practice

### Story

A student can join several clubs — the chess club, the art club, the robotics
club. The student keeps track of which clubs they belong to. Many students can
join the same club, but the club itself does not track its members. That is a
many-to-many relationship from one side: the student manages their own list.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Club` | Provided | No — complete |
| `Student` | Manages own memberships | **Yes** |

### What the student implements

`Club` (provided) stores a name and description. `Student` stores a name and a
list of `Club` objects. Methods:

- `Student.__init__(name)` — name, empty clubs list
- `Student.join_club(club)` — append club to list; if already a member, do nothing
- `Student.leave_club(club_name)` — remove club by name; return True if removed,
  False if not found
- `Student.is_member(club_name)` — return True if that club name is in the list
- `Student.list_clubs()` — return list of club names

### Key concept

N:M from one side: the student manages their own list. The club does not track
members. This is the simpler N:M — only one side's list changes.

---

## Problem 3b — N:M Association, Both Sides (extends Family-09)

**Family:** Family-09-Relationships-Association
**Folder:** `08-Student-Subject/`
**Difficulty:** 4/5
**Time:** ~25 min
**Purpose:** Exam

### Story

A student can enroll in several subjects. A subject can have several students
enrolled. That is a many-to-many relationship — both sides hold lists of the
other. When a student enrolls, both sides must be updated.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Subject` | Provided | No — complete |
| `Student` | Both sides of N:M | **Yes** |

### What the student implements

`Student` stores a name and a list of `Subject` objects. `Subject` (provided) stores
a code, a title, and a list of enrolled student names. Methods:

- `Student.__init__(name)` — name, empty subjects list
- `Student.enroll(subject)` — append subject to student's list AND call
  `subject.add_student(self.name)`
- `Student.drop(subject_code)` — remove subject from list AND call
  `subject.remove_student(self.name)`
- `Student.is_enrolled(subject_code)` — return True if any subject in list has that code
- `Student.list_subjects()` — return list of subject titles

### Key concept

Many-to-many both sides: both lists must be updated. When a student enrolls, both
the student's list and the subject's list change. This is the authentic N:M
pattern.

---

## Problem 4 — Dependency (new family)

**Family:** Family-11-Relationships-Dependency *(new)*
**Folder:** `Family-11-Relationships-Dependency/01-Grade-Checker/`
**Difficulty:** 2/5
**Time:** ~15 min

### Story

A grade checker looks at an answer and decides whether it passes. The checker
uses the answer but does not own it — it receives it, reads it, and returns a
result. That is a dependency: one class uses another without storing it.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Answer` | Provided | No — complete |
| `GradeChecker` | Uses Answer as parameter | **Yes** |

### What the student implements

`Answer` (provided) stores a student name and score. `GradeChecker` has no state
— it is a "utility" class whose methods receive an `Answer` and return a result.

- `GradeChecker.check_pass(answer, passing_score)` — return True if answer's
  score >= passing_score
- `GradeChecker.get_grade(answer)` — return "A" (≥90), "B" (≥80), "C" (≥70),
  "D" (≥60), "F" (<60)
- `GradeChecker.compare(answer1, answer2)` — return the name of the student with
  the higher score; if equal, return "Tie"

### Key concept

Dependency: `GradeChecker` never stores an `Answer`. It receives one as a
parameter, uses its getters, and returns a result. The `Answer` exists
independently.

---

## Problem 5 — Aggregation (new family)

**Family:** Family-12-Relationships-Aggregation *(new)*
**Folder:** `Family-12-Relationships-Aggregation/01-Computer-Peripherals/`
**Difficulty:** 3/5
**Time:** ~20 min

### Story

A computer has peripherals — a keyboard and a mouse. The peripherals are
manufactured separately and can exist without the computer. The computer stores
them but does not create them. That is aggregation: the whole holds the parts,
but the parts can live on their own.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Peripheral` | Provided | No — complete |
| `Computer` | Whole that holds parts | **Yes** |

### What the student implements

`Peripheral` (provided) stores a name and type. `Computer` stores a name and a
list of `Peripheral` objects. Methods:

- `Computer.__init__(name)` — name, empty peripherals list
- `Computer.add_peripheral(peripheral)` — add to list
- `Computer.remove_peripheral(name)` — remove by name; return True if removed,
  False if not found
- `Computer.count_peripherals()` — return count
- `Computer.list_peripheral_names()` — return list of names
- `Computer.has_type(type_name)` — return True if any peripheral has that type

### Key concept

Aggregation: parts are created outside and passed in. The whole stores them but
does not create them. Contrast with composition (Problem 7).

---

## Problem 6 — Inheritance (fresh variant for Family-05)

**Family:** Family-05-Inheritance
**Folder:** `05-Animal-Bird/`
**Difficulty:** 2/5
**Time:** ~15 min

### Story

Every bird is an animal. The `Animal` class stores a name and species. A bird
inherits everything an animal has and adds a wingspan — the distance from
wingtip to wingtip.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Animal` | Parent — provided | No — complete |
| `Bird` | Child — inherits from Animal | **Yes** |

### What the student implements

`Animal` (provided) stores name and species, with `get_name()` and `get_species()`.
`Bird` inherits from `Animal` and adds `wingspan`. Methods:

- `Bird.__init__(name, species, wingspan)` — call
  `super().__init__(name, species)`, store wingspan
- `Bird.get_wingspan()` — return wingspan
- `Bird.describe()` — return `"name is a species with a wingspan cm wingspan"`
  (e.g., `"Tweety is a canary with a 25 cm wingspan"`)

### Key concept

Inheritance: the child reuses the parent's constructor and getters via
`super().__init__()`, then adds its own attribute and method.

---

## Problem 7 — Composition (fresh variant for Family-10)

**Family:** Family-10-Relationships-Composition
**Folder:** `05-House-Rooms/`
**Difficulty:** 4/5
**Time:** ~25 min

### Story

A house is built with its own rooms. The rooms do not exist before the house is
built and they do not exist after the house is demolished. The house creates the
rooms itself. That is composition: the whole creates and owns its parts.

### Classes

| Class | Role | Student writes? |
|-------|------|-----------------|
| `Room` | Part — provided | No — complete |
| `House` | Whole — creates parts | **Yes** |

### What the student implements

`Room` (provided) stores a name and area (in sqm). `House` stores a name and a
list of `Room` objects it creates in `__init__`. Methods:

- `House.__init__(name, room_specs)` — `room_specs` is a list of
  `(room_name, area)` tuples; loop and create a `Room` for each, append to list
- `House.count_rooms()` — return count
- `House.total_area()` — sum all room areas
- `House.get_largest_room()` — return the name of the room with the largest area;
  if tie, return first
- `House.list_room_names()` — return list of room names

### Key concept

Composition: the whole creates the parts in `__init__`. The rooms do not exist
independently. Contrast with aggregation (Problem 5) where peripherals are
passed in.

---

## Family Structure

```
Family-05-Inheritance/
├── 05-Animal-Bird/          ← NEW (fresh variant)
│   └── (6 deliverables)

Family-09-Relationships-Association/
├── 05-Student-Locker/       ← NEW (basic has-a)
│   └── (6 deliverables)
├── 06-Person-ID/            ← NEW (1:1 multiplicity)
│   └── (6 deliverables)
├── 07-Student-Club/         ← NEW (N:M single-side, practice)
│   └── (6 deliverables)
├── 08-Student-Subject/      ← NEW (N:M both-sides, exam)
│   └── (6 deliverables)

Family-10-Relationships-Composition/
├── 05-House-Rooms/          ← NEW (fresh variant)
│   └── (6 deliverables)

Family-11-Relationships-Dependency/    ← NEW family
├── README.md
├── 01-Grade-Checker/
│   └── (6 deliverables)

Family-12-Relationships-Aggregation/   ← NEW family
├── README.md
├── 01-Computer-Peripherals/
│   └── (6 deliverables)
```

---

## Spec Compliance Checklist

Every problem must satisfy:

- [ ] SPEC-001: problem.md section order (Story → Task → Class Specification →
  Required Methods → Constraints → Example → Explanation → Hint)
- [ ] SPEC-005: class-based extensions (Class Specification with ### per class,
  Required Methods with ### per method)
- [ ] SPEC-002: starter.py — no type hints, no `pass`, placeholder returns per
  the placeholder table
- [ ] SPEC-004: tests.py — behavior-based, equal weight, deterministic,
  commented-out main guard
- [ ] SPEC-003: metadata.yml — all required fields, difficulty as N/5
- [ ] STD-001: Python style — descriptive names, ≤100 char lines, 4-space indent
- [ ] STD-002: Markdown style — ATX headings, fenced code blocks with language tag
- [ ] Scoring: 6 rules from 66-assessment-scoring-std.md
- [ ] Design Principle 1: One New Idea per problem
- [ ] Design Principle 2: Authentic Stories
- [ ] Design Principle 4: Early Success (student understands goal in first minute)

---

## Implementation Order

1. **Problem 6** (Inheritance) — simplest, extends existing family, good warm-up
2. **Problem 1** (Basic Association) — simplest association, extends existing family
3. **Problem 4** (Dependency) — new family, simple concept
4. **Problem 2** (1:1 Association) — extends existing family
5. **Problem 5** (Aggregation) — new family, moderate complexity
6. **Problem 3a** (N:M Single-Side) — moderate complexity
7. **Problem 7** (Composition) — extends existing family, moderate complexity
8. **Problem 3b** (N:M Both-Sides) — most complex, save for last

---

## Suggested Teaching Sequence

| Week | Problem | Topic | Difficulty | Purpose |
|------|---------|-------|-----------|---------|
| Week 1 | Problem 1 | Basic Association | 2/5 | Practice |
| Week 1 | Problem 4 | Dependency | 2/5 | Practice |
| Week 2 | Problem 6 | Inheritance | 2/5 | Practice |
| Week 2 | Problem 2 | 1:1 Association | 3/5 | Practice |
| Week 2 | Problem 5 | Aggregation | 3/5 | Practice |
| Week 3 | Problem 3a | N:M Single-Side | 3/5 | Practice |
| Week 3 | Problem 7 | Composition | 4/5 | Practice |
| Week 3 | Problem 3b | N:M Both-Sides | 4/5 | **Exam** |

---

## Open Questions

1. **Family numbering:** ✅ Resolved. New families are Family-11 (Dependency) and
   Family-12 (Aggregation). The existing Family-11 (SOLID SR) will be renamed to
   Family-13 as a separate task.

2. **N:M split:** ✅ Resolved. Problem 3a (Student-Club, single-side) for practice
   and Problem 3b (Student-Subject, both-sides) for exam.

3. **README updates:** Should the plan include updating the README.md files for
   Family-05, Family-09, and Family-10 to list the new problems?

4. **Difficulty ratings:** Proposed: 2/5 for Basic Association, Inheritance,
   Dependency; 3/5 for 1:1 Association, N:M Single-Side, Aggregation; 4/5 for
   N:M Both-Sides, Composition. Do these feel right for Grade 9?