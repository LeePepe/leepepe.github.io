/* Theme owner for <html>: synchronizes data-theme ("light"|"dark" or unset for system)
 * and data-lp-theme ("light"|"dark", resolved), plus localStorage keys "profile-theme" and "lp-theme". */
(function () {
  var root = document.documentElement;
  var mqDark = window.matchMedia("(prefers-color-scheme: dark)");
  var mqClear = window.matchMedia("(prefers-reduced-transparency: reduce)");
  function pref() {
    try {
      var v = localStorage.getItem("profile-theme") || localStorage.getItem("lp-theme");
      return v === "light" || v === "dark" || v === "system" ? v : "system";
    } catch (e) {
      return "system";
    }
  }
  function material() {
    var forced = /[?&]material=solid\b/.test(location.search);
    var blur = window.CSS && (CSS.supports("backdrop-filter", "blur(1px)") || CSS.supports("-webkit-backdrop-filter", "blur(1px)"));
    return forced || mqClear.matches || !blur ? "solid" : "glass";
  }
  function setPref(value) {
    var v = value === "light" || value === "dark" || value === "system" ? value : "system";
    try {
      localStorage.setItem("profile-theme", v);
      localStorage.setItem("lp-theme", v);
    } catch (e) {}
    apply(v);
  }
  function apply(explicit) {
    var p = explicit || pref();
    var resolved = p === "system" ? (mqDark.matches ? "dark" : "light") : p;
    if (p === "system") {
      delete root.dataset.theme;
    } else {
      root.dataset.theme = p;
    }
    root.setAttribute("data-lp-theme", resolved);
    root.setAttribute("data-strata-material", material());
    var sel = document.getElementById("theme");
    if (sel && sel.value !== p) {
      sel.value = p;
    }
    var btns = document.querySelectorAll("[data-theme-choice]");
    for (var i = 0; i < btns.length; i++) {
      btns[i].setAttribute("aria-pressed", String(btns[i].getAttribute("data-theme-choice") === p));
    }
  }
  apply();
  mqDark.addEventListener && mqDark.addEventListener("change", function () { apply(); });
  mqClear.addEventListener && mqClear.addEventListener("change", function () { apply(); });
  window.addEventListener("storage", function (e) {
    if (!e.key || e.key === "profile-theme" || e.key === "lp-theme") apply();
  });
  document.addEventListener("DOMContentLoaded", function () {
    apply();
    var sel = document.getElementById("theme");
    if (sel) {
      sel.addEventListener("change", function (e) {
        setPref(e.target.value);
      });
    }
    document.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-theme-choice]");
      if (!b) return;
      setPref(b.getAttribute("data-theme-choice"));
    });

    /* Quiet scroll-spy for article TOC (aside.toc) */
    var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".toc a[href^='#']"));
    if (tocLinks.length > 0) {
      var targets = [];
      for (var j = 0; j < tocLinks.length; j++) {
        var id = tocLinks[j].getAttribute("href").slice(1);
        var el = document.getElementById(id);
        if (el) targets.push({ link: tocLinks[j], el: el });
      }
      var syncToc = function () {
        if (!targets.length) return;
        var active = targets[0];
        for (var k = 0; k < targets.length; k++) {
          if (targets[k].el.getBoundingClientRect().top <= 128) active = targets[k];
        }
        for (var m = 0; m < targets.length; m++) {
          if (targets[m] === active) targets[m].link.setAttribute("aria-current", "true");
          else targets[m].link.removeAttribute("aria-current");
        }
      };
      window.addEventListener("scroll", syncToc, { passive: true });
      syncToc();
    }
  });
})();

