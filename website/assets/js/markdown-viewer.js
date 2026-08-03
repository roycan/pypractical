/* =====================================================================
   markdown-viewer.js — fetch a bundled .md document, parse it (marked),
   tag code blocks, rewrite internal .md links, and render into a
   .md-viewer element. Usage on a page:

       <div class="md-viewer" data-md="_docs/66-assessment-scoring-std.md"></div>

   Requires the vendored marked.js (loaded before this script).
   ===================================================================== */
(function () {
  "use strict";

  var cfg = window.PYPRA || {};
  var docsBase = (document.body.getAttribute("data-root") || "") + (cfg.docsPath || "_docs");

  function status(el, msg, isError) {
    el.innerHTML = '<div class="md-viewer__status' + (isError ? " error" : "") + '">' + msg + "</div>";
  }

  // Tag each fenced code block with data-lang so CSS can show a label,
  // and wrap in a <pre> we control. marked gives <pre><code class="language-x">.
  function decorateCode(container) {
    container.querySelectorAll("pre > code[class*='language-']").forEach(function (code) {
      var m = code.className.match(/language-([\w-]+)/);
      var pre = code.parentElement;
      if (m) pre.setAttribute("data-lang", m[1]);
    });
  }

  // Rewrite links to other .md documents: if a GitHub repo is configured,
  // point them at the source; otherwise leave as-is (they resolve to bundled
  // copies only if present). Also rewrite raw image refs relative to repo root.
  function rewriteLinks(container) {
    var blob = cfg.ghBlob || "";
    container.querySelectorAll("a[href]").forEach(function (a) {
      var href = a.getAttribute("href");
      if (/\.md($|[?#])/i.test(href) && blob && !/^https?:/i.test(href)) {
        a.setAttribute("href", blob + href.replace(/^[./]+/, ""));
        a.setAttribute("target", "_blank"); a.setAttribute("rel", "noopener");
      }
    });
  }

  function render(el) {
    var src = el.getAttribute("data-md");
    if (!src) return;
    var url = /^[./]/.test(src) ? src : (docsBase + "/" + src);
    status(el, "Loading document…");

    fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error("HTTP " + r.status);
        return r.text();
      })
      .then(function (text) {
        var html;
        if (window.marked && typeof window.marked.parse === "function") {
          window.marked.setOptions && window.marked.setOptions({ gfm: true, breaks: false, headerIds: false });
          html = window.marked.parse(text);
        } else {
          // minimal fallback: escape + paragraphs (very rough) if marked missing
          html = "<p>" + text.replace(/&/g, "&").replace(/</g, "<").replace(/\n\n/g, "</p><p>") + "</p>";
        }
        el.innerHTML = '<div class="prose">' + html + "</div>";
        decorateCode(el);
        rewriteLinks(el);
        // print hint
        var hint = document.createElement("div");
        hint.className = "print-source"; hint.textContent = "Source: " + src;
        el.prepend(hint);
        el.dispatchEvent(new CustomEvent("md:ready", { bubbles: true }));
      })
      .catch(function (err) {
        status(el,
          "Could not load <code>" + src + "</code>. " +
          (location.protocol === "file:" ?
            "Open the site through a local server (e.g. <code>python3 -m http.server</code>) — browsers block file fetches." :
            "Check the path or run the doc-bundling step."),
          true);
        if (window.console) console.warn("[markdown-viewer]", err);
      });
  }

  // Expose render for on-page document switchers (spec/standard pages).
  window.PYPRA = window.PYPRA || {};
  window.PYPRA.renderMarkdown = render;

  function init() {
    var viewers = document.querySelectorAll(".md-viewer[data-md]");
    viewers.forEach(render);
    // if a page uses <div data-md> without the .md-viewer class, still render
    document.querySelectorAll("[data-md]:not(.md-viewer)").forEach(function (el) {
      el.classList.add("md-viewer"); render(el);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else { init(); }
})();
