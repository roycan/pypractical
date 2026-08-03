/* =====================================================================
   components.js — shared chrome (navbar + footer), injected per page.
   Pattern: each page has <div data-include="nav"></div> and
   <footer data-include="footer"></footer>; this file fills them in.
   Also wires: mobile burger, theme toggle, active-link highlight, year.
   Relative-path aware via <body data-root="../"> (set per page).
   ===================================================================== */
(function () {
  "use strict";

  // ---- Site config (edit here when forking) -------------------------
  window.PYPRA = Object.assign({
    name: "PyPractical",
    repo: "",                 // e.g. "yourname/pypractical" — enables GitHub links
    branch: "main",
    docsPath: "_docs",        // where bundled .md files live (relative to site root)
    year: new Date().getFullYear()
  }, window.PYPRA || {});

  var root = document.body.getAttribute("data-root") || "";
  var repo = window.PYPRA.repo;
  var ghBlob = repo ? "https://github.com/" + repo + "/blob/" + window.PYPRA.branch + "/" : "";
  var ghHome = repo ? "https://github.com/" + repo + "/" : "#";

  // ---- Inline SVG logo (reused in nav + footer) ---------------------
  var LOGO = ''
    + '<svg class="logo" viewBox="0 0 48 48" role="img" aria-label="PyPractical logo">'
    +   '<defs><linearGradient id="ppLogo" x1="0" y1="0" x2="1" y2="1">'
    +     '<stop offset="0" stop-color="#E07A55"/><stop offset="1" stop-color="#E0A24A"/>'
    +   '</linearGradient></defs>'
    +   '<rect x="2" y="2" width="44" height="44" rx="13" fill="url(#ppLogo)"/>'
    +   '<path d="M14 25.5l5 5.5 11-14.5" fill="none" stroke="#fff" stroke-width="3.4" '
    +         'stroke-linecap="round" stroke-linejoin="round"/>'
    +   '<path d="M31 16l4 3-4 3" fill="none" stroke="#fff" stroke-opacity=".75" stroke-width="2.2" '
    +         'stroke-linecap="round" stroke-linejoin="round"/>'
    + '</svg>';

  // ---- Primary nav items (label, folder-key) ------------------------
  var NAV = [
    { key: "why",                  href: "why/",                  label: "Why" },
    { key: "philosophy",           href: "philosophy/",           label: "Philosophy" },
    { key: "assessment-engineering", href: "assessment-engineering/", label: "Engineering" },
    { key: "assessment-families",  href: "assessment-families/",  label: "Explore" },
    { key: "contribute",           href: "contribute/",           label: "Contribute" }
  ];

  function navItemsHTML() {
    return NAV.map(function (n) {
      return '<a href="' + root + n.href + '" data-nav="' + n.key + '">' + n.label + "</a>";
    }).join("");
  }

  var NAV_HTML = ''
    + '<a class="skip-link" href="#main">Skip to content</a>'
    + '<nav class="nav" aria-label="Primary">'
    +   '<div class="nav__inner">'
    +     '<a class="nav__brand" href="' + root + 'index.html" aria-label="PyPractical home">'
    +       LOGO + '<span>Py<b>Practical</b></span>'
    +     "</a>"
    +     '<div class="nav__links" id="navLinks">' + navItemsHTML() + "</div>"
    +     '<div class="nav__actions">'
    +       '<button class="theme-toggle" type="button" aria-label="Toggle dark mode" title="Toggle dark mode">'
    +         sunSVG() + moonSVG()
    +       "</button>"
    +       '<a class="btn btn--ghost" href="' + ghHome + '" rel="noopener" ' + (repo ? "" : 'hidden') + '>'
    +         ghIcon() + "<span>GitHub</span></a>"
    +       '<button class="nav__burger" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="navLinks"><span></span></button>'
    +     "</div>"
    +   "</div>"
    + "</nav>";

  function sunSVG() {
    return '<svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
      + 'stroke-linecap="round"><circle cx="12" cy="12" r="4.2"/>'
      + '<path d="M12 2v2M12 20v2M2 12h2M20 12h2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M19.1 4.9l-1.4 1.4M6.3 17.7l-1.4 1.4"/></svg>';
  }
  function moonSVG() {
    return '<svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" '
      + 'stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  }
  function ghIcon() {
    return '<svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor" aria-hidden="true">'
      + '<path d="M12 2C6.48 2 2 6.58 2 12.25c0 4.53 2.87 8.37 6.84 9.73.5.1.68-.22.68-.49 0-.24-.01-.88-.01-1.73-2.78.62-3.37-1.37-3.37-1.37-.45-1.18-1.11-1.5-1.11-1.5-.91-.64.07-.62.07-.62 1 .07 1.53 1.06 1.53 1.06.89 1.56 2.34 1.11 2.91.85.09-.66.35-1.11.63-1.36-2.22-.26-4.56-1.14-4.56-5.06 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.71 0 0 .84-.27 2.75 1.05A9.36 9.36 0 0 1 12 6.84c.85 0 1.71.12 2.51.34 1.91-1.32 2.75-1.05 2.75-1.05.55 1.41.2 2.45.1 2.71.64.72 1.03 1.63 1.03 2.75 0 3.93-2.34 4.79-4.57 5.05.36.32.68.94.68 1.9 0 1.37-.01 2.48-.01 2.82 0 .27.18.6.69.49A10.02 10.02 0 0 0 22 12.25C22 6.58 17.52 2 12 2z"/></svg>';
  }

  // ---- Footer -------------------------------------------------------
  function footerCol(title, links) {
    var items = links.map(function (l) {
      var href = /^\w+:\/\//.test(l.href) ? l.href : root + l.href;
      return '<li><a href="' + href + '"' + (l.ext ? ' rel="noopener"' : "") + ">" + l.label + "</a></li>";
    }).join("");
    return "<div><h4>" + title + "</h4><ul>" + items + "</ul></div>";
  }

  var FOOTER_HTML = (function () {
    var explore = footerCol("Explore", [
      { href: "assessment-families/", label: "Assessment Families" },
      { href: "why/", label: "Why It Matters" },
      { href: "philosophy/", label: "Philosophy" },
      { href: "manifesto/", label: "Manifesto" }
    ]);
    var reference = footerCol("Reference", [
      { href: "specifications/", label: "Specifications" },
      { href: "standards/", label: "Standards" },
      { href: "workflow/", label: "Workflow" },
      { href: "assessment-engineering/", label: "Assessment Engineering" }
    ]);
    var project = footerCol("Project", [
      { href: "pypractical/", label: "About PyPractical" },
      { href: "about/", label: "About the Project" },
      { href: "contribute/", label: "Contribute" },
      { href: ghHome, label: "GitHub", ext: true }
    ]);
    return ''
      + '<footer class="footer">'
      +   '<div class="container footer__grid">'
      +     '<div class="footer__col">'
      +       '<div class="footer__brand">' + LOGO + "<span>Py<b>Practical</b></span></div>"
      +       '<p class="footer__about">Open Assessment Engineering — classroom-tested, '
      +         'automatically-gradable Python assessments, openly shared and continuously improved.</p>'
      +     "</div>"
      +     explore + reference + project
      +   "</div>"
      +   '<div class="container footer__bottom">'
      +     "<span>© " + window.PYPRA.year + " PyPractical contributors. "
      +       'Docs under <a href="https://creativecommons.org/licenses/by-sa/4.0/" rel="noopener">CC&nbsp;BY-SA&nbsp;4.0</a>; '
      +       'code under <a href="https://opensource.org/license/mit" rel="noopener">MIT</a>.</span>'
      +     "<span>Made for teachers, by teachers and their tools.</span>"
      +   "</div>"
      + "</footer>";
  })();

  // ---- Inject -------------------------------------------------------
  function inject() {
    var navSlot = document.querySelector('[data-include="nav"]');
    if (navSlot) navSlot.outerHTML = NAV_HTML;
    var footSlot = document.querySelector('[data-include="footer"]');
    if (footSlot) footSlot.outerHTML = FOOTER_HTML;
  }

  // ---- Active link + interactions -----------------------------------
  function currentPageKey() {
    var p = location.pathname.replace(/\/+$/, "");
    var seg = p.split("/").filter(Boolean).pop() || "index.html";
    if (seg === "index.html" || seg === "") {
      // home if nothing meaningful above it
      var parts = p.split("/").filter(Boolean);
      if (parts.length === 0 || (parts.length === 1 && /index\.html$/i.test(parts[0]))) return "home";
      return parts[parts.length - 1].replace(/\.html?$/, "");
    }
    return seg.replace(/\.html?$/, "");
  }

  function wire() {
    // active nav link
    var key = currentPageKey();
    if (key === "home") {
      var brand = document.querySelector(".nav__brand");
      if (brand) brand.setAttribute("aria-current", "page");
    }
    document.querySelectorAll(".nav__links a").forEach(function (a) {
      if (a.getAttribute("data-nav") === key) {
        a.classList.add("is-active");
        a.setAttribute("aria-current", "page");
      }
    });

    // mobile burger
    var burger = document.querySelector(".nav__burger");
    if (burger) {
      burger.addEventListener("click", function () {
        var open = document.body.classList.toggle("nav-open");
        burger.setAttribute("aria-expanded", String(open));
        burger.setAttribute("aria-label", open ? "Close menu" : "Open menu");
      });
    }
    // close menu on link click (mobile)
    document.querySelectorAll(".nav__links a").forEach(function (a) {
      a.addEventListener("click", function () { document.body.classList.remove("nav-open"); });
    });

    // theme toggle (no-flash bootstrap lives inline in each page <head>)
    document.querySelectorAll(".theme-toggle").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var html = document.documentElement;
        var next = (html.getAttribute("data-theme") === "dark") ? "light" : "dark";
        html.setAttribute("data-theme", next);
        try { localStorage.setItem("pypra-theme", next); } catch (e) {}
      });
    });
  }

  // run on DOM ready
  function init() { inject(); wire(); }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }

  // expose github helpers for other scripts
  window.PYPRA.ghBlob = ghBlob;
  window.PYPRA.ghHome = ghHome;
})();
