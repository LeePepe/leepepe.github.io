/* One theme owner for <html>: data-lp-theme (light|dark, resolved), data-strata-material (effective).
 * Preference key "lp-theme" = light | dark | system (default system). Prototype-only: ?material=solid. */
(function () {
  var root = document.documentElement, KEY = "lp-theme";
  var mqDark = window.matchMedia("(prefers-color-scheme: dark)");
  var mqClear = window.matchMedia("(prefers-reduced-transparency: reduce)");
  function pref() { try { var v = localStorage.getItem(KEY); return v === "light" || v === "dark" ? v : "system"; } catch (e) { return "system"; } }
  function material() {
    var forced = /[?&]material=solid\b/.test(location.search);
    var blur = window.CSS && (CSS.supports("backdrop-filter", "blur(1px)") || CSS.supports("-webkit-backdrop-filter", "blur(1px)"));
    return forced || mqClear.matches || !blur ? "solid" : "glass";
  }
  function apply() {
    var p = pref();
    root.setAttribute("data-lp-theme", p === "system" ? (mqDark.matches ? "dark" : "light") : p);
    root.setAttribute("data-strata-material", material());
    var btns = document.querySelectorAll("[data-theme-choice]");
    for (var i = 0; i < btns.length; i++) btns[i].setAttribute("aria-pressed", String(btns[i].getAttribute("data-theme-choice") === p));
  }
  apply();
  mqDark.addEventListener && mqDark.addEventListener("change", apply);
  mqClear.addEventListener && mqClear.addEventListener("change", apply);
  document.addEventListener("DOMContentLoaded", function () {
    apply();
    document.addEventListener("click", function (e) {
      var b = e.target.closest && e.target.closest("[data-theme-choice]");
      if (!b) return;
      try { localStorage.setItem(KEY, b.getAttribute("data-theme-choice")); } catch (err) {}
      apply();
    });
  });
})();
