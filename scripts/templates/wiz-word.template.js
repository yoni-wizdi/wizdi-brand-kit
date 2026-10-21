/* ═══════════════════════════════════════════════════════════════════════════
   wiz-word.js — le wordmark d'un module Wiz (WizPlay, WizBook…) ou « Wizdi »,
   rendu avec les VRAIS tracés Baloo et animé comme sur studio-wizdi.com :
   le contour se dessine, le remplissage monte, le trait s'efface.
   Sans dépendance (Web Animations API). Version React + GSAP : WizWord.tsx.

   Usage :
     <script src="wiz-word.js"></script>
     <span data-wiz-word="WizPlay" data-accent="#FF5FA2" style="font-size:48px"></span>
     <span data-wiz-word="Wizdi" style="font-size:40px"></span>
     <script>WizWord.init();</script>                 // ou WizWord.init(root)

   Règles encodées ici (ne pas changer sans Yoni) :
     - « Wiz » en bleu #23A4D8, le suffixe dans la couleur du module (data-accent
       ou la variable CSS --mc du parent) ; « Wizdi » entièrement bleu.
     - hauteur = 1em du parent → se règle avec font-size.
     - animation à l'entrée dans l'écran (seuil 35 %), UNE fois, délai 1,1 s,
       contour 2,4 s (ease in-out), remplissage 1 s (−0,5 s), trait 0,7 s (−0,6 s).
       data-fast="1" = variante en-tête : sans délai, contour 1,6 s, remplissage 0,7 s (−0,3 s),
       trait 0,45 s (−0,45 s), stroke-width 1,6 (valeurs de TopBar.tsx).
     - prefers-reduced-motion : aucun mouvement, wordmark plein immédiatement.
   ═══════════════════════════════════════════════════════════════════════════ */
(function (global) {
  var WIZ_BLUE = "#23A4D8";
  var PATHS = /*__PATHS__*/{}/*__END__*/;

  var EASE_INOUT = "cubic-bezier(.45,0,.55,1)";   // ≈ power2.inOut
  var EASE_OUT = "cubic-bezier(.33,1,.68,1)";     // ≈ power2.out
  var reduce = global.matchMedia && global.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function accentOf(el) {
    return el.getAttribute("data-accent") || getComputedStyle(el).getPropertyValue("--mc").trim() || "#7B6CF6";
  }

  function build(el) {
    var name = el.getAttribute("data-wiz-word");
    var d = PATHS[name];
    var accent = accentOf(el);
    if (!d) { // repli texte bicolore — jamais d'uppercase
      var suffix = name.replace(/^Wiz/i, "");
      el.innerHTML = '<span style="font-family:\'Baloo Latin\',sans-serif;font-weight:700;direction:ltr;display:inline-block"><b style="color:' + WIZ_BLUE + ';font-weight:inherit">Wiz</b><i style="font-style:normal;color:' + accent + '">' + suffix + '</i></span>';
      return null;
    }
    var ns = "http://www.w3.org/2000/svg";
    var svg = document.createElementNS(ns, "svg");
    svg.setAttribute("viewBox", d.vb);
    svg.setAttribute("role", "img");
    svg.setAttribute("aria-label", name);
    svg.setAttribute("preserveAspectRatio", "xMidYMid meet");
    svg.style.height = "1em"; svg.style.width = "auto"; svg.style.display = "inline-block"; svg.style.verticalAlign = "-.12em"; svg.style.overflow = "visible";
    var parts = d.suffix ? [[d.wiz, WIZ_BLUE], [d.suffix, accent]] : [[d.wiz, WIZ_BLUE]];
    parts.forEach(function (p) {
      var path = document.createElementNS(ns, "path");
      path.setAttribute("d", p[0]); path.setAttribute("fill", p[1]); path.setAttribute("stroke", p[1]);
      path.setAttribute("stroke-width", "0"); path.setAttribute("stroke-linejoin", "round");
      svg.appendChild(path);
    });
    el.innerHTML = ""; el.appendChild(svg);
    return svg;
  }

  /* les deux timelines du site : module (WizWord.tsx) et logo d'en-tête (TopBar.tsx) */
  var T_MODULE = { delay: 1100, draw: 2400, fill: 1000, fillOff: 500, fade: 700, fadeOff: 600, sw: 3 };
  var T_HEADER = { delay: 0, draw: 1600, fill: 700, fillOff: 300, fade: 450, fadeOff: 450, sw: 1.6 };
  function play(svg, fast) {
    var T = fast ? T_HEADER : T_MODULE;
    var paths = svg.querySelectorAll("path");
    Array.prototype.forEach.call(paths, function (path) {
      var len = path.getTotalLength();
      path.style.strokeDasharray = len; path.style.strokeDashoffset = len;
      path.style.fillOpacity = 0; path.style.strokeOpacity = 1; path.setAttribute("stroke-width", String(T.sw));
      path.animate([{ strokeDashoffset: len }, { strokeDashoffset: 0 }], { duration: T.draw, delay: T.delay, easing: EASE_INOUT, fill: "forwards" });
      path.animate([{ fillOpacity: 0 }, { fillOpacity: 1 }], { duration: T.fill, delay: T.delay + T.draw - T.fillOff, easing: EASE_OUT, fill: "forwards" });
      path.animate([{ strokeOpacity: 1 }, { strokeOpacity: 0 }], { duration: T.fade, delay: T.delay + T.draw - T.fillOff + T.fill - T.fadeOff, easing: EASE_OUT, fill: "forwards" });
    });
  }

  function observe(svg, fast) {
    if (reduce || !("IntersectionObserver" in global)) return;
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { io.disconnect(); play(svg, fast); } });
    }, { threshold: 0.35 });
    io.observe(svg);
  }

  var api = {
    paths: PATHS,
    init: function (root) {
      var els = (root || document).querySelectorAll("[data-wiz-word]");
      Array.prototype.forEach.call(els, function (el) {
        if (el.getAttribute("data-wiz-ready")) return;
        el.setAttribute("data-wiz-ready", "1");
        var svg = build(el);
        if (svg) observe(svg, el.getAttribute("data-fast") === "1");
      });
    },
    /* rejouer à la demande (planche de marque, démo) */
    replay: function (el) {
      var svg = el.querySelector("svg"); if (!svg || reduce) return;
      Array.prototype.forEach.call(svg.querySelectorAll("path"), function (p) { p.getAnimations().forEach(function (a) { a.cancel(); }); });
      play(svg, el.getAttribute("data-fast") === "1");
    }
  };
  global.WizWord = api;
  if (document.readyState !== "loading") api.init(); else document.addEventListener("DOMContentLoaded", function () { api.init(); });
})(window);
