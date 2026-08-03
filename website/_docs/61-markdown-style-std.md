# Markdown Style Standard

**Document ID:** STD-002

**Status:** Draft

**Applies To:** All Markdown documents in PyPractical

---

# Purpose

This standard defines the preferred Markdown style used throughout PyPractical.

A consistent Markdown style improves readability for:

* students
* teachers
* contributors
* AI assistants

Every document should feel like it belongs to the same project.

---

# Guiding Principles

Good Markdown should be:

* readable in plain text
* easy to edit
* easy to review
* easy to render
* consistent

Markdown is source code for documentation.

It deserves the same care as Python code.

---

# Headings

Use ATX headings.

Preferred

```markdown
# Title

## Section

### Subsection
```

Do not skip heading levels.

Example

```text
# Family

## Overview

### Learning Objective
```

Avoid

```text
# Family

### Overview
```

---

# Document Title

Every document begins with exactly one level-one heading.

Example

```markdown
# Assessment Philosophy
```

There should only be one `#` heading in each document.

---

# Blank Lines

Leave one blank line:

* after headings
* before headings
* between paragraphs
* around code blocks
* around lists

Whitespace improves readability.

---

# Paragraphs

Prefer short paragraphs.

Recommended

3–5 lines.

Large blocks of text are more difficult to review.

---

# Lists

Use unordered lists for collections.

Example

```markdown
- students
- teachers
- contributors
```

Use numbered lists only when sequence matters.

Example

```markdown
1. Read the problem.
2. Plan the solution.
3. Write the code.
4. Test the program.
```

---

# Emphasis

Use emphasis sparingly.

Preferred

```markdown
**Important**
```

Avoid excessive formatting.

Too much emphasis reduces its effectiveness.

---

# Block Quotes

Use block quotes for:

* educational principles
* memorable statements
* guiding questions
* classroom philosophy

Example

```markdown
> Programming is learned by programming.
```

---

# Code Blocks

Always use fenced code blocks.

Specify the language whenever possible.

Example

````markdown
```python
for customer in customers:
    total += customer
```
````

Language identifiers improve rendering and editor support.

---

# Inline Code

Use backticks for:

* filenames
* commands
* function names
* variable names
* class names

Examples

```markdown
`Recorder`

`calculate_total()`

`README.md`
```

Do not use inline code for emphasis alone.

---

# Tables

Use tables only when they improve clarity.

Good uses

* assessment metadata
* version history
* curriculum progression
* feature comparison

Avoid using tables for long explanations.

---

# Horizontal Rules

Use horizontal rules to separate major sections only when they improve readability.

Avoid excessive separators.

---

# Links

Prefer descriptive links.

Example

```markdown
See `workflow.md` for the complete assessment lifecycle.
```

Avoid raw URLs unless necessary.

Internal documentation should reference repository files by name.

---

# Images

Images are optional.

When included:

* provide meaningful filenames
* include alt text when supported
* ensure the image contributes to understanding

Documentation should remain useful even without images.

---

# Line Length

Recommended maximum:

100 characters.

Long lines are more difficult to review in Git.

---

# Tone

Write professionally.

Use active voice whenever practical.

Examples

Preferred

> Contributors should verify every expected output.

Less preferred

> Every expected output should be verified by contributors.

The active voice is usually clearer.

---

# Cross References

When referring to another project document, use its filename.

Example

```markdown
See `workflow.md`.
```

Avoid references such as

> "the previous document"

Explicit filenames remain correct as the repository grows.

---

# Examples

Examples should be complete enough to teach.

Avoid placeholders like

```python
...
```

unless the omitted code is irrelevant to the lesson.

---

# Notes

When adding notes, use a consistent format.

Example

```markdown
> **Note**
>
> Hidden tests must never introduce new requirements.
```

Use notes sparingly to highlight genuinely important information.

---

# File Naming

Preferred

```text
assessment-philosophy.md
workflow.md
problem-template.md
python-style-std.md
```

Use:

* lowercase
* hyphens
* descriptive names

Avoid spaces.

---

# Document Evolution

Documentation is expected to evolve.

When improving a document:

* preserve clarity
* preserve consistency
* improve examples where appropriate
* remove outdated guidance

Revision is a normal part of maintaining educational resources.

---

# Validation Checklist

Before publishing, verify:

* □ One level-one heading
* □ Correct heading hierarchy
* □ Blank lines between sections
* □ Consistent list formatting
* □ Fenced code blocks with language identifiers
* □ Appropriate use of emphasis
* □ Descriptive filenames and references
* □ Professional tone
* □ Readable line lengths
* □ Markdown renders correctly

---

# Compliance

A document is **STD-002 compliant** when it follows the conventions defined in this standard.

The objective of this standard is not stylistic perfection.

Its objective is to make every PyPractical document clear, approachable, and pleasant to read—for both humans and AI.
