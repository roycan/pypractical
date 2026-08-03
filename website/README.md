# PyPractical Website

A static, component-driven documentation site that presents PyPractical as the
first reference implementation of **Open Assessment Engineering**.

Built with **HTML5 + Bulma CSS + custom CSS + vanilla JavaScript**. No build
tools, no frameworks. Deploys straight to **GitHub Pages**.

---

## Run locally

The Markdown-Viewer pages fetch documents over HTTP, so preview with a tiny
static server (not by opening the file directly):

```bash
cd website
python3 -m http.server 8000
# open http://localhost:8000
```

---

## Structure

```
website/
  index.html              # Home
  why/                    # The problem & vision
  philosophy/             # 10 principles + curriculum/assessment philosophy
  manifesto/              # The 7 declarations
  assessment-engineering/ # The Open Assessment Engineering concept (signature)
  pypractical/            # The reference implementation (deliverables + curriculum)
  specifications/         # Spec docs (interactive Markdown Viewer)
  standards/              # Standards + scoring model (Markdown Viewer)
  workflow/               # 10-step workflow (timeline + Markdown Viewer)
  assessment-families/    # Interactive curriculum explorer (41 assessments)
  contribute/             # Use, license, the Educators' Pledge
  about/                  # The story + full Project Vision doc
  _docs/                  # bundled .md documents (synced on deploy)
  assets/
    css/      tokens base components markdown explorer print
    js/       components markdown-viewer explorer
    data/     curriculum-data.js
    vendor/   bulma.min.css  marked.min.js
    img/      photos/ (WebP)   icons/   illustrations/
  favicon.svg
```

---

## Configure

Edit `assets/js/components.js` → `window.PYPRA.repo` (e.g. `"yourname/pypractical"`)
to enable the GitHub nav button, problem "View" links, and internal `.md` link
rewriting in the Markdown Viewer.

---

## How content stays in sync

- **Marketing pages** (Home, Why, Engineering, PyPractical, About, Philosophy,
  Manifesto, Contribute) are hand-authored HTML — best for SEO and no-JS.
- **Reference pages** (Specifications, Standards, Workflow, About's vision)
  fetch the real `.md` documents from `_docs/` via the Markdown Viewer, so the
  site and the source always agree.
- The **GitHub Actions** workflow (`.github/workflows/pages.yml`) re-copies the
  root `.md` files into `website/_docs/` on every deploy, keeping production
  synchronized automatically.

## Imagery

Editorial illustrations are served as optimized **WebP** from
`assets/img/photos/` (sourced from `pics/`). To re-optimize after changing the
source PNGs, run a Pillow resize+WebP pass at ≤1280px, quality ~82.

## Distribution tiers (governance)

PyPractical separates the open **framework** from **operational** assessments:

- **Core (public):** philosophy, specs, standards, workflow, scoring — openly licensed and indexed.
- **Reference (public):** a canonical example family (set via `referenceFamilies` in
  `assets/data/curriculum-data.js`) that demonstrates the format — never used for graded work.
- **Assessment Packs (educator):** the operational bank — distributed to educators and **not**
  publicly indexed, to protect classroom validity.

The public website shows a **metadata catalog** (topics, concepts, difficulty) for transparency,
but deep-links resolve only for Reference examples. To avoid exposing live quiz content, **commit
operational families only to a private repository** (or keep them local) — never `git add Family-*`
to the public repository.

## Visual identity

Designed against `visual_identity_guide.md` (VIS-001): warm paper palette,
terracotta accent, Cormorant Garamond + Source Sans 3 + JetBrains Mono,
~920px reading width, 12px cards / 8px buttons, subtle paper grain, outline
icons, plus a warm "lamplight" dark theme.
