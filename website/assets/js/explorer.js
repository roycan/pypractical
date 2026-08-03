/* =====================================================================
   explorer.js — renders the curriculum explorer on /assessment-families/.
   Reads window.PYPRA_CURRICULUM (curriculum-data.js).
   Governance: shows a METADATA catalog of all families. Reference families
   (PYPRA_CURRICULUM.referenceFamilies) deep-link to the public repo; all
   other "pack" families are shown as Educator packs with no deep link.
   ===================================================================== */
(function () {
  "use strict";

  var D = window.PYPRA_CURRICULUM;
  if (!D) return;
  var cfg = window.PYPRA || {};
  var blob = cfg.ghBlob || "";
  var ref = D.referenceFamilies || [];

  var stagesEl = document.getElementById("expStages");
  var barEl = document.getElementById("expBar");
  var resultsEl = document.getElementById("expResults");
  if (!stagesEl || !resultsEl) return;

  var state = { stage: "all", diff: 0 };

  // ---- helpers -----------------------------------------------------
  function problemCount(stageId) {
    return (D.stages.find(function (s) { return s.id === stageId; }).families || [])
      .reduce(function (sum, fid) { return sum + (D.families[fid].problems.length); }, 0);
  }
  function diffHTML(n) {
    var filled = "", empty = "";
    for (var i = 1; i <= 5; i++) { if (i <= n) filled += "●"; else empty += "○"; }
    return '<span class="diff">' + filled + '<span class="dot-empty">' + empty + "</span></span>";
  }
  function esc(s) {
    return String(s)
      .replace(/&/g, "&")
      .replace(/</g, "<")
      .replace(/>/g, ">");
  }
  function tag(s) { return '<span class="problem__tag">' + esc(s) + "</span>"; }

  // ---- stage rail --------------------------------------------------
  function renderStages() {
    var html = "";
    html += '<button class="stage-chip" type="button" data-stage="all" aria-pressed="' + (state.stage === "all") + '">' +
            '<span class="stage-chip__num">★</span>All stages</button>';
    D.stages.forEach(function (s) {
      var cnt = problemCount(s.id);
      var empty = cnt === 0;
      html += '<button class="stage-chip" type="button" data-stage="' + s.id + '" ' + (empty ? "disabled" : "") +
              ' aria-pressed="' + (state.stage === s.id) + '" title="' + esc(s.title) + '">' +
              '<span class="stage-chip__num">' + s.num + "</span>" + esc(s.title) +
              '<span class="stage-chip__count">' + (empty ? "soon" : cnt) + "</span></button>";
    });
    stagesEl.innerHTML = html;
    stagesEl.querySelectorAll(".stage-chip[data-stage]").forEach(function (b) {
      b.addEventListener("click", function () {
        if (b.disabled) return;
        state.stage = b.getAttribute("data-stage");
        renderStages(); renderResults();
      });
    });
  }

  // ---- difficulty filter ------------------------------------------
  function renderBar() {
    if (!barEl) return;
    var html = '<div class="explorer__filters"><span class="lbl">Difficulty</span>';
    [0, 1, 2, 3, 4].forEach(function (d) {
      html += '<button class="filter-chip" type="button" data-diff="' + d + '" aria-pressed="' + (state.diff === d) + '">' +
              (d === 0 ? "Any" : diffHTML(d)) + "</button>";
    });
    html += "</div>";
    html += '<div class="explorer__summary" id="expSummary"></div>';
    barEl.innerHTML = html;
    barEl.querySelectorAll(".filter-chip[data-diff]").forEach(function (b) {
      b.addEventListener("click", function () {
        state.diff = parseInt(b.getAttribute("data-diff"), 10);
        renderBar(); renderResults();
      });
    });
  }

  // ---- results -----------------------------------------------------
  function visibleFamilies() {
    if (state.stage === "all") {
      return D.stages.reduce(function (a, s) { return a.concat(s.families); }, []);
    }
    return D.stages.find(function (s) { return s.id === state.stage; }).families;
  }

  function renderResults() {
    var fids = visibleFamilies();
    var totalShown = 0;
    var html = "";

    if (state.stage !== "all") {
      var stg = D.stages.find(function (s) { return s.id === state.stage; });
      html += '<div class="family__blurb" style="margin-bottom:var(--s-6)"><strong>Stage ' + stg.num + " · " + esc(stg.title) +
              ".</strong> " + esc(stg.blurb) + '<div class="family__meta">' +
              stg.concepts.map(function (c) { return '<span class="tag">' + esc(c) + "</span>"; }).join("") + "</div></div>";
    }

    fids.forEach(function (fid) {
      var f = D.families[fid];
      if (!f) return;
      var problems = f.problems.filter(function (p) { return state.diff === 0 || p.difficulty === state.diff; });
      if (problems.length === 0) return;
      totalShown += problems.length;
      var isRef = ref.indexOf(fid) >= 0;

      html += '<section class="family' + (isRef ? "" : " family--pack") + '">';
      html += '<div class="family__head"><span class="family__num">F' + String(f.num).padStart(2, "0") + "</span>" +
              '<span class="family__title">' + esc(f.title) + "</span>" +
              (isRef ? '<span class="tag tag--sage">Reference</span>' : '<span class="tag">Educator pack</span>') + "</div>";
      html += '<p class="family__blurb">' + esc(f.blurb) + "</p>";
      html += '<div class="family__meta">' + diffHTML(f.difficulty) + '<span class="diff__label">family level</span>' +
              '<span class="tag">' + problems.length + " problem" + (problems.length === 1 ? "" : "s") + "</span></div>";
      html += '<div class="problems">';

      problems.forEach(function (p) {
        var openTag = isRef
          ? '<a class="problem" href="' + (blob ? (blob + f.folder + "/" + p.slug + "/problem.md") : "../contribute/") + '"' + (blob ? ' target="_blank" rel="noopener"' : "") + ">"
          : '<div class="problem problem--pack" role="listitem">';
        html += openTag;
        html += '<div class="problem__main"><div class="problem__title">' + esc(p.title);
        if (p.tested) html += ' <span class="tag tag--sage">classroom-tested</span>';
        html += "</div>";
        html += '<div class="problem__tags">' + p.concepts.slice(0, 4).map(tag).join("") + "</div></div>";
        html += '<div class="problem__side">' + diffHTML(p.difficulty) + '<span class="muted" style="font-size:var(--fs-xs)">' + esc(p.time) + "</span>";
        if (isRef) {
          html += blob ? '<span class="text-accent" style="font-size:var(--fs-xs)">View problem ↗</span>'
                       : '<span class="tag tag--sage" style="font-size:var(--fs-xs)">Reference</span>';
        } else {
          html += '<span class="tag" style="font-size:var(--fs-xs)">Educator pack</span>';
        }
        html += "</div>" + (isRef ? "</a>" : "</div>");
      });

      html += "</div></section>";
    });

    if (totalShown === 0) {
      html += '<div class="family"><p class="muted">No problems match this filter yet. Stages 5 and 6 are part of the roadmap.</p></div>';
    }

    resultsEl.innerHTML = html;
    var sum = document.getElementById("expSummary");
    if (sum) sum.textContent = totalShown + " problem" + (totalShown === 1 ? "" : "s") + " shown";
  }

  renderStages();
  renderBar();
  renderResults();
})();
