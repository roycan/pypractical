# PyPractical

**Open, classroom-tested Python programming assessments for teachers.**

PyPractical is an open educational resource that provides authentic programming practicals for introductory Python and Object-Oriented Programming courses.

Every assessment is designed to be:

* 📖 Easy for teachers to adopt
* 💻 Authentic and engaging for students
* ✅ Automatically graded using Python `unittest`
* 🏫 Suitable for real classrooms
* 🌱 Open for continuous improvement by the teaching community

Our goal is simple:

> **Help teachers spend less time grading and more time teaching.**
> **Help students spend less time memorizing and more time creating.**

---

# Why PyPractical?

Programming is learned by writing programs—not by memorizing syntax.

Unfortunately, creating high-quality practical assessments requires significant time and effort. Teachers often need to:

* write authentic programming problems
* prepare starter code
* create reliable unit tests
* manually verify expected outputs
* grade hundreds of student submissions
* create equivalent assessments for multiple class sections

PyPractical exists to reduce that workload while improving the learning experience for students.

Every practical is designed as a complete assessment package rather than a single programming question.

---

# What Every Problem Includes

Each assessment contains:

* 📄 Markdown problem statement
* 🐍 Python starter template
* ✅ Python `unittest` suite
* 👨‍🏫 Teacher reference solution
* 📝 Teacher notes
* 📋 Metadata describing learning objectives and difficulty

This allows teachers to adopt an assessment with minimal preparation.

---

# Design Philosophy

PyPractical is guided by a few simple principles.

* One primary learning objective per assessment
* Authentic programming stories
* Clear instructions
* Progressive difficulty
* Automatic, objective grading
* Classroom-tested improvements
* Respect for both student and teacher time

Assessment should measure understanding—not memorization.

Programming should feel purposeful, approachable, and enjoyable.

---

# Repository Structure

```text
PyPractical/
├── README.md
├── inceptions/context.md          # the project "second brain"
├── plans/                         # round plans + outcomes
├── 00-PROJECT_VISION.md ...       # philosophy, specs, and standards
├── examples/                      # legacy pre-spec snippets
│
├── Family-01-Minimum-Cost/              (functions reference)
├── Family-02-Intro-OOP/                 (SG 3 — Introduction to OOP)
├── Family-03-Classes-and-Objects/       (SG 4-5)
├── Family-04-Encapsulation/             (SG 8)
├── Family-05-Inheritance/               (SG 9)
├── Family-06-Method-Overriding/         (SG 10)
├── Family-07-Polymorphism/              (SG 11)
├── Family-08-Abstraction/               (SG 12)
├── Family-09-Relationships-Association/ (SG 6)
├── Family-10-Relationships-Composition/ (SG 7)
└── Family-13-SOLID-Single-Responsibility/ (SG 27)
```

Each family contains 3-4 equivalent practical assessments (same concept and
difficulty, different stories) for fairness across class sections. Every problem
ships six files: `problem.md`, `starter.py`, `solution.py`, `tests.py`,
`teacher_notes.md`, and `metadata.yml`.

---

# Current Roadmap

## Round 1 — Foundation (complete)

Two canonical, spec-compliant reference problems plus the class-based spec
(SPEC-005):

* **Family-01-Minimum-Cost/01-Parking-Garage** — the function-based reference
* **Family-03-Classes-and-Objects/01-TV-Recorder** — the class-based (OOP) reference

## Round 2 — OOP Families (complete)

A full, auto-gradable Object-Oriented Programming curriculum built in dependency
order (SG 3 -> 4-5 -> 8 -> 9 -> 10 -> 11 -> 12 -> 6 -> 7 -> 27).
**11 families, 40 problems, 473 tests — all passing.**

| Family | Topic |
|---|---|
| Family-02-Intro-OOP | Introduction to OOP |
| Family-03-Classes-and-Objects | Classes and Objects |
| Family-04-Encapsulation | Encapsulation |
| Family-05-Inheritance | Inheritance |
| Family-06-Method-Overriding | Method Overriding |
| Family-07-Polymorphism | Polymorphism |
| Family-08-Abstraction | Abstraction |
| Family-09-Relationships-Association | Relationships I |
| Family-10-Relationships-Composition | Relationships II |
| Family-13-SOLID-Single-Responsibility | SOLID: Single Responsibility |

Run any suite with `python3 -m unittest tests` from inside the problem folder.

## Round 3 — Data Handling (planned)

Reading and writing data (SG 18 text files -> 19 analysis -> 20 JSON).

---

# Who Is This For?

PyPractical is designed for:

* High school Computer Science teachers
* Introductory Python instructors
* Beginning Object-Oriented Programming courses
* Teachers who want automatic grading
* Schools teaching multiple class sections

---

# Contributing

PyPractical is an open educational project.

Teachers are encouraged to:

* improve existing assessments
* contribute new assessment families
* report issues
* suggest classroom improvements
* share teaching experiences

Real classroom feedback is one of the most valuable contributions to the project.

---

# Quality Standards

Every assessment published in PyPractical should:

* have a clearly defined learning objective
* include complete teacher resources
* contain verified expected outputs
* pass all published unit tests
* follow the project's design principles
* be suitable for immediate classroom use

We believe educational resources deserve the same care and quality as well-engineered software.

---

# Our Promise

> Every assessment in PyPractical should be good enough that its authors would be happy to use it in their own classroom tomorrow.

That promise guides every contribution to this project.

If an assessment is not ready for our own students, it is not yet ready for yours.

---

# License

PyPractical is intended to be an open educational resource that grows through collaboration among teachers.

We hope it becomes a community of educators who believe that authentic programming experiences can inspire the next generation of software creators.
