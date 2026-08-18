# PyPractical Website — Build Plan v2

> Supersedes v1. Reflects the expanded brief: **12 pages, component-driven, dark mode, print-friendly, Markdown-synced content**, positioned as **the first reference implementation of Open Assessment Engineering**.
> Imagery decision **locked**: SVG illustrations + curated warm stock photos.

---

## 0. How to read the scores

- **F = Feasibility** — can we build it to a good standard with current tools (file editing → code mode; vendored JS libs; GitHub Pages).
- **C = Confidence** — certainty in the approach/estimate; dips when a decision, craft quality, or a dependency is unresolved.
- ⚠ = **F ≤ 90 OR C ≤ 90** → flagged for review/simplification (Section 7).

---

## 1. Mission & message

Build a beautiful, fast, static documentation site introducing **PyPractical** as **the first reference implementation of Open Assessment Engineering**.

> *"Educational assessments deserve the same engineering discipline that we expect from great software."*

Primary audiences: **Teachers → Contributors → School leaders → Curious educators**.
Feel: **timeless, calm, trustworthy, welcoming.**

**Note on framing:** "Open Assessment Engineering" is a **new editorial frame** (seeded once in [`07-TESTING_GUIDE.md:259`](07-TESTING_GUIDE.md:259)). It is defensible because the repo already contains the engineering artifacts: specifications (`*-spec.md`), standards (`*-std.md`), a workflow ([`06-WORKFLOW.md`](06-WORKFLOW.md:1)), and a scoring model ([`66-assessment-scoring-std.md`](66-assessment-scoring-std.md:1)). The `/why`, `/assessment-engineering`, and `/pypractical` pages will **author** this frame (with your review); reference pages will **render** the existing docs.

---

## 2. Tech stack

HTML5 · Bulma CSS (vendored locally, not CDN — works offline) · custom CSS · vanilla JS · **no frameworks, no build tools** · GitHub Pages via a **GitHub Actions deploy**.

Key libraries (vendored, not CDN, to stay offline-capable & dependency-stable):
- **marked.js** (~30KB) — Markdown → HTML parser for the Markdown Viewer.
- **highlight.js** (optional, ~15KB core) — code-block syntax highlighting.

---

## 3. Proposed directory structure

```
website/
  index.html                    # /
  why/index.html
  philosophy/index.html
  manifesto/index.html
  assessment-engineering/index.html
  pypractical/index.html
  specifications/index.html
  standards/index.html
  workflow/index.html
  assessment-families/index.html
  contribute/index.html
  about/index.html
  assets/
    css/   tokens.css base.css components.css markdown.css print.css
    js/    theme.js components.js markdown-viewer.js explorer.js
    data/  curriculum-data.js
    vendor/marked.min.js (highlight.min.js)
    img/   logo.svg icons/ illustrations/ photos/
.github/workflows/pages.yml     # deploys website/ + bundles docs → Pages
```

Why `website/` (not repo root): keeps the project's existing root docs untouched. A Pages Action publishes `website/` and **bundles the referenced `.md` docs** into `website/_docs/` so the Markdown Viewer fetches local copies (works offline, no CORS, no hardcoded URLs). "Sync" = *synced at deploy time* — exactly right for a docs site.

---

## 4. Components (reusable, no framework)

Shared chrome injected by `components.js` into placeholder elements (so nav/footer are written once):
- **Navbar** (logo, links, theme toggle, responsive burger)
- **Footer**

CSS-class components (used via classes/structure on each page):
- **Hero**, **Section**, **Card Grid**, **Timeline**, **Specification Card**, **Standard Card**, **Call-to-Action**
- **Markdown Viewer** — `<div data-md="_docs/01-MANIFESTO.md" data-rewrite="md"></div>` → `markdown-viewer.js` fetches, parses (marked), rewrites internal `.md` links, applies `.prose` + code styling.

(No Web Components for v1 — keeps JS surface small and predictable. Can upgrade later.)

---

## 5. Design system — Warm & human (light + dark)

Light tokens: `--cream #FBF6EC`, `--paper #FFF`, `--ink #2A2622`, `--ink-soft #5B524A`, `--terracotta #C2562F`, `--amber #E0A24A`, `--sage #6E8B6A`, `--rule #E7DECF`.
Dark tokens (mirrored, lower saturation): `--cream #1B1714`, `--paper #24201C`, `--ink #F2EBDD`, `--ink-soft #C9BFAE`, `--terracotta #E07A55`, `--amber #E6B864`, `--sage #8FB38A`, `--rule #3A332C`.
Type: **Fraunces** (serif headings) + **Inter** (sans body), Google Fonts (or self-hosted). `1.125rem` base, `1.6` line-height.
Theme: `[data-theme="dark"]` on `<html>`; `theme.js` toggles + persists in `localStorage` + respects `prefers-color-scheme`.

---

## 6. Task breakdown with scores

### Phase A — Foundations & architecture
| # | Task | F% | C% |
|---|---|---|---|
| A1 | Scaffold `website/` tree + 12 page shells | 97 | 94 |
| A2 | Design tokens (light + dark) + Bulma overrides + fonts | 92 | 88 |
| A3 | Base CSS: reset, typography, layout, `.prose` | 95 | 92 |
| A4 | Component CSS (all 9 components) | 93 | 88 |
| A5 | `components.js` (inject navbar/footer, burger, theme toggle) + `theme.js` | 92 | 88 |
| ⚠A6 | **Markdown-sync architecture** (bundled-vs-raw-vs-hybrid) | 80 | 75 → recommend bundled-via-Action hybrid → 90 / 86 |

### Phase B — Imagery
| # | Task | F% | C% |
|---|---|---|---|
| ⚠B1 | SVG logo + icon set + illustrations | 90 | 86 |
| ⚠B2 | Curated warm stock photos (hero + accents) | 85 | 80 → small curated set → 90 / 86 |

### Phase C — Open Assessment Engineering framing (NEW)
| # | Task | F% | C% |
|---|---|---|---|
| ⚠C1 | Author the OAE concept (definition, why, principles) | 86 | 78 → draft + your review → 92 / 86 |
| C2 | Map existing artifacts as OAE evidence (specs/standards/workflow/scoring) | 92 | 86 |

### Phase D — Curriculum data
| # | Task | F% | C% |
|---|---|---|---|
| ⚠D1 | `curriculum-data.js` (stages→families→problems, default mapping) | 92 | 84 → confirm mapping → 95 / 88 |

### Phase E — Pages (12)
| # | Page | F% | C% |
|---|---|---|---|
| E1 | `/` Home | 93 | 88 |
| E2 | `/why` | 92 | 86 |
| E3 | `/manifesto` | 95 | 90 |
| E4 | `/philosophy` | 92 | 86 |
| ⚠E5 | `/assessment-engineering` (authored OAE concept) | 88 | 80 |
| E6 | `/pypractical` (the reference implementation) | 90 | 84 |
| ⚠E7 | `/specifications` (spec cards + md-viewer) | 90 | 84 |
| ⚠E8 | `/standards` (standard cards + md-viewer) | 90 | 84 |
| E9 | `/workflow` (timeline + md-viewer of 06-WORKFLOW) | 92 | 88 |
| ⚠E10 | `/assessment-families` (data-driven explorer) | 88 | 82 → drill-down v1 → 92 / 86 |
| E11 | `/contribute` | 94 | 90 |
| E12 | `/about` (origin story, AI partnership, living project) | 92 | 86 |

### Phase F — Cross-cutting
| # | Task | F% | C% |
|---|---|---|---|
| ⚠F1 | Dark mode across all components + persistence | 90 | 86 |
| ⚠F2 | Print CSS for spec/standard pages | 90 | 88 |
| ⚠F3 | Markdown Viewer fidelity (link rewrite, code blocks, tables) | 85 | 80 → vendor marked + rewriter → 92 / 86 |
| F4 | Accessibility pass (practical A-level) | 90 | 86 |
| F5 | Performance (small payloads, lazy images) | 92 | 88 |
| F6 | SEO + Open Graph + favicon per page | 92 | 88 |

### Phase G — Deploy
| # | Task | F% | C% |
|---|---|---|---|
| ⚠G1 | GitHub Actions Pages workflow + `.md` bundling step + instructions | 88 | 82 |

### Net
~33 tasks. Most sit ≥ 90/86. The genuinely soft spots are **A6 (markdown sync)** and **F3 (viewer fidelity)** — the technical heart — plus **C1/E5 (new framing)** — the editorial heart.

---

## 7. Flagged items — review & simplifications

1. **A6 / F3 — Markdown sync (the crux).** Three options:
   - **(a) Bundled-via-Action (RECOMMENDED):** Pages Action copies referenced `.md` into `website/_docs/`; viewer fetches local copies. ✅ offline, ✅ no CORS, ✅ no hardcoded URLs, ✅ stable. "Sync at deploy time."
   - **(b) Live `raw.githubusercontent` fetch:** viewer reads source directly. ✅ always-current, ❌ hardcodes repo URL, ❌ needs internet, ❌ no offline.
   - **(c) No live md — hand-author all pages:** safest, ❌ loses the "stay synchronized" goal.
   - **Recommendation:** (a), with marketing pages hand-authored anyway (so they're SEO/no-JS-safe), and the Markdown Viewer used only on **reference** pages (specs, standards, workflow, manifesto full-text) where sync matters most. → F 90 / C 86.

2. **C1 / E5 — new OAE framing.** I draft the concept page grounded in your real artifacts; you review wording. De-risks brand positioning. → F 92 / C 86.

3. **D1 — stage↔family mapping.** Proposed default (from v1, still stands):
   - S1 → Family-01-Minimum-Cost
   - S2 → Family-02-Intro-OOP, Family-03-Classes-and-Objects, Family-04-Encapsulation
   - S3 → Family-09-Relationships-Association
   - S4 → Family-05-Inheritance, Family-06-Method-Overriding, Family-07-Polymorphism, Family-08-Abstraction, Family-10-Relationships-Composition, Family-13-SOLID-Single-Responsibility
   - S5/S6 → *(none yet)*

4. **E10 — explorer v1.** Drill-down (Stage → Family → Problem) + difficulty chips; defer free-text search.

5. **F1 — dark mode.** Token-driven; check every component + ensure photos/SVG read in dark.

6. **F2 — print.** `@media print` on spec/standard pages (hide nav/theme toggle/CTAs; expand md content).

7. **G1 — deploy.** I deliver the Action workflow + doc-bundling step + enable instructions; you push & enable Pages.

8. **B2 — photos.** Curate ~6–8 warm/human shots; use gradients + SVG elsewhere to limit licensing surface.

---

## 8. Build order (proposed)

1. Foundations: scaffold, tokens (light+dark), base + component CSS, `components.js`/`theme.js` (A1–A5).
2. Imagery: SVG set + curated photos (B1–B2).
3. Resolve markdown-sync (A6) + Markdown Viewer (F3).
4. Curriculum data (D1).
5. Author OAE frame (C1) → build `/`, `/why`, `/assessment-engineering`, `/pypractical`, `/about` (E1,E2,E5,E6,E12).
6. Reference pages w/ Markdown Viewer: `/manifesto`, `/philosophy`, `/specifications`, `/standards`, `/workflow` (E3,E4,E7,E8,E9).
7. `/assessment-families` explorer (E10) + `/contribute` (E11).
8. Cross-cutting: dark/print/accessibility/perf/SEO (F1–F6).
9. Deploy workflow + docs (G1).

---

## 9. Decisions to confirm before coding

1. **Markdown sync strategy** — confirm bundled-via-Action hybrid (Section 7.1a)? *(This is the main one.)*
2. **Author the Open Assessment Engineering frame** — go ahead, with your review?
3. **Stage↔family default mapping** (Section 7.3) — accept?
4. **Bulma vendored locally** (offline-capable) — OK?
5. **GitHub repo remote** — is this repo on GitHub (so the deploy workflow + raw-fetch fallback are usable)?
