/* ──────────────────────────────────────────────────────────────────────────
   MOTEUR MOTION WIZDI — CŒUR (WZ). Tous formats : ?format=9x16 (1080x1920, défaut) · 4x5 (1080x1350) · 16x9 (1920x1080).
   Repris du moteur des films Wiz du 13/10/2026 et du kit du concours du 15/10, rendu indépendant de tout projet.

   Principe : UNE timeline GSAP en pause, calée au MOT de la narration (window.WIZ_WORDS : instants de chaque mot).
   window.__seek(t) pose l'image EXACTE de l'instant t ; rien ne dépend du temps réel (tout passe par `tl` ou par les
   fonctions `ambient` / `media` appelées avec t) : le rendu image par image (tools/render.py) est identique partout.

   Ce fichier ne dessine rien : il fournit au style (pop.js + style.js) les outils communs — séquences d'images des
   VRAIS médias (build/media), hibou 3D, logos officiels (assets/logos.js, généré depuis le kit par tools/brand.py),
   typographie des mots de l'écran (verbatim), panneau d'écran avec caméra + repère + morceau qui sort (règle d'Eyal),
   particules, lecture et rendu. Le style appelle WZ.run(build).

   Entrées (scripts chargés AVANT core.js) :
     window.WIZ_FILM   (film.js)   : { slug, mod, color, owl, voAt, endHold, dur?, format?, scenes, previewAudio, … }
     window.WIZ_WORDS  (words.js)  : { s1: [{ w, t, e, br?, x? }, …], s2: … }  — w VERBATIM ; x: true = mot interdit à l'écran
     window.WIZ_VO     (optionnel) : { dur, lines: { s1: { t, e } } } — sinon déduit des mots
     window.WIZ_MEDIA  (build/media/manifest.js, optionnel) : { nom: { n, w, h, fps, base?, dir? } }
     window.WIZ_OWLS   (optionnel) : séquences animées du hibou 3D { "<owl>-<pose>": { n, w, h, base?, dir? } }
     window.WIZ_LOGOS  (assets/logos.js, optionnel mais attendu) : { wizplay: "<svg…>", …, wizdi: "<svg…>" }
   ────────────────────────────────────────────────────────────────────────── */
(() => {
  "use strict";
  const F = window.WIZ_FILM = window.WIZ_FILM || {};
  const WD = window.WIZ_WORDS || {};
  const MED = window.WIZ_MEDIA || {}, OWLM = window.WIZ_OWLS || {}, LOGOS = window.WIZ_LOGOS || {};
  if (window.DrawSVGPlugin) gsap.registerPlugin(DrawSVGPlugin);

  const params = new URLSearchParams(location.search);
  const RENDER = params.has("render");
  /* ── format ─────────────────────────────────────────────────────────────── */
  const SIZES = { "9x16": [1080, 1920], "4x5": [1080, 1350], "16x9": [1920, 1080], "1x1": [1080, 1080] };
  const FMT = SIZES[params.get("format")] ? params.get("format") : (SIZES[F.format] ? F.format : "9x16");
  const [W, H] = SIZES[FMT];
  /* zones sûres (px) : Meta 15 % en haut / 22 % en bas en 9:16 ; télé ~5 % en 16:9 (WIZDI-PRODUCTION §4) */
  const SAFE = FMT === "9x16" ? { top: Math.round(H * 0.15), bottom: Math.round(H * 0.78), left: 54, right: W - 54 }
    : FMT === "16x9" ? { top: 70, bottom: 1010, left: 100, right: 1820 }
    : { top: Math.round(H * 0.06), bottom: Math.round(H * 0.94), left: 54, right: W - 54 };

  /* ── narration : instants des phrases, déduits des mots si WIZ_VO est absent ── */
  const VO = window.WIZ_VO || (() => {
    const lines = {};
    let end = 0;
    for (const k of Object.keys(WD)) {
      const a = WD[k];
      if (!a || !a.length) continue;
      lines[k] = { t: a[0].t, e: a[a.length - 1].e };
      end = Math.max(end, lines[k].e);
    }
    return { dur: end, lines };
  })();
  window.WIZ_VO = VO;
  const VO_AT = F.voAt != null ? F.voAt : 0.6;
  const END_HOLD = F.endHold != null ? F.endHold : 3.1;
  const DUR = F.dur != null ? F.dur : Math.ceil((VO_AT + VO.dur + END_HOLD) * 4) / 4;
  document.body.classList.add(RENDER ? "render" : "preview", "fmt-" + FMT);

  const KEYS = Object.keys(VO.lines).filter((k) => WD[k] && WD[k].length);
  const LS = (k) => VO_AT + VO.lines[k].t;
  const LE = (k) => VO_AT + VO.lines[k].e;
  const words = (k) => WD[k] || [];
  /* indices des mots AFFICHABLES d'une phrase (jamais un mot x: true) */
  const shown = (k) => words(k).map((w, i) => (w.x ? -1 : i)).filter((i) => i >= 0);
  const WT = (k, i) => { const a = WD[k]; return VO_AT + a[Math.max(0, Math.min(i, a.length - 1))].t; };
  const WE = (k, i) => { const a = WD[k]; return VO_AT + a[Math.max(0, Math.min(i, a.length - 1))].e; };
  /* fenêtre d'une scène = d'un peu avant sa phrase à un peu avant la suivante */
  const LEAD = 0.24;
  const T0 = (k) => { const i = KEYS.indexOf(k); return i <= 0 ? 0 : LS(k) - LEAD; };
  const T1 = (k) => { const i = KEYS.indexOf(k); return i >= KEYS.length - 1 ? DUR : LS(KEYS[i + 1]) - LEAD; };

  /* ── utilitaires ──────────────────────────────────────────────────────── */
  const $ = (tag, cls, parent, html) => {
    const e = document.createElement(tag);
    if (cls) e.className = cls;
    if (html != null) e.innerHTML = html;
    if (parent) parent.appendChild(e);
    return e;
  };
  const css = (e, o) => Object.assign(e.style, o);
  const box = (e, cx, cy, w, h) => css(e, { left: cx - w / 2 + "px", top: cy - h / 2 + "px", width: w + "px", height: h + "px" });
  const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
  const lerp = (a, b, k) => a + (b - a) * k;
  const prog = (t, a, b) => clamp((t - a) / (b - a));
  const EASES = {};
  const ease = (n) => EASES[n || "sine.inOut"] || (EASES[n || "sine.inOut"] = gsap.parseEase(n || "sine.inOut"));
  const rng = (seed) => () => { seed = (seed * 1664525 + 1013904223) >>> 0; return seed / 4294967296; };
  const TAU = Math.PI * 2, DEG = Math.PI / 180;
  const NS = "http://www.w3.org/2000/svg";
  /* images-clés génériques : rows = [t, v1..vn, ease?] */
  const kfEval = (kf, t, n) => {
    let v = kf[0].slice(1, 1 + n);
    for (let i = 0; i < kf.length - 1; i++) {
      const A = kf[i], B = kf[i + 1];
      if (t >= A[0] && t <= B[0]) { const e = ease(B[1 + n])(prog(t, A[0], B[0])); v = v.map((_, j) => lerp(A[1 + j], B[1 + j], e)); break; }
      if (t > B[0]) v = B.slice(1, 1 + n);
    }
    return v;
  };
  const hexRgb = (h) => { const n = parseInt(h.slice(1), 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
  const rgba = (h, a) => { const [r, g, b] = hexRgb(h); return `rgba(${r},${g},${b},${a})`; };
  const mix = (h1, h2, k) => { const a = hexRgb(h1), b = hexRgb(h2); return "#" + a.map((v, i) => Math.round(lerp(v, b[i], k)).toString(16).padStart(2, "0")).join(""); };

  const tl = gsap.timeline({ paused: true, defaults: { ease: "power3.out" } });
  /* garde-fou : un tween placé à un instant NÉGATIF fait décaler par GSAP TOUS les enfants de la timeline (le film
     entier perd sa synchro au mot). On ramène donc toute position négative à 0 (et on le signale une fois). */
  let negWarned = false;
  const POSARG = { to: 2, from: 2, set: 2, fromTo: 3, add: 1, call: 2 };
  for (const [m, i] of Object.entries(POSARG)) {
    const f = tl[m].bind(tl);
    tl[m] = (...a) => {
      if (typeof a[i] === "number" && a[i] < 0) {
        if (!negWarned) { console.warn(`tl.${m} à t=${a[i].toFixed(3)} s < 0 : ramené à 0 (avance l'élément dans le film)`); negWarned = true; }
        a[i] = 0;
      }
      return f(...a);
    };
  }
  const ambient = [], media = [], loads = [], SFX = [];
  /* repère sonore : (t, clé, gain 0..1, panoramique -1..1) -> out/timeline.json -> tools/mix.py */
  const sfx = (t, k, g = 1, p = 0) => { if (t >= 0 && t < DUR) SFX.push({ t: +t.toFixed(3), k, g, p }); };
  const settle = (i, ms = 8000) => Promise.race([
    new Promise((res) => { if (i.complete && i.naturalWidth) res(); else { i.addEventListener("load", res, { once: true }); i.addEventListener("error", res, { once: true }); } }),
    new Promise((r) => setTimeout(r, ms)),
  ]);
  const img = (parent, cls, src) => { const i = $("img", cls, parent); i.decoding = "sync"; i.src = src; loads.push(settle(i)); return i; };
  /* visible seulement dans [t0, t1] (évite de composer des calques cachés) */
  const window_ = (el, t0, t1) => ambient.push((t) => { el.style.display = t >= t0 - 0.05 && t <= t1 + 0.05 ? "" : "none"; });

  /* ── séquences d'images (vrais médias : build/media/<nom>/0001.jpg ; hibou : build/owl/<nom>/001.webp) ── */
  const frames = (name, base, ext = "jpg", pad = 4, n, dir) => ({ name, n: n || (MED[name] || {}).n || 1, base: base || (MED[name] || {}).base || "build/media/",
    dir: dir || (MED[name] || {}).dir || name, ext, pad, cache: new Map() });
  const getFrame = (S, f) => {
    let e = S.cache.get(f);
    if (e) { S.cache.delete(f); S.cache.set(f, e); return e; }
    const im = new Image(); im.decoding = "sync";
    const p = new Promise((res) => { im.onload = res; im.onerror = res; });
    im.src = `${S.base}${S.dir}/${String(f + 1).padStart(S.pad, "0")}.${S.ext}`;
    e = { im, p };
    S.cache.set(f, e);
    if (S.cache.size > 90) S.cache.delete(S.cache.keys().next().value);
    return e;
  };
  /* plan = [[t, image], …] interpolé ; play(nom, t0, vitesse, départ) = lecture à vitesse donnée depuis t0 */
  const play = (name, t0, speed = 1, start = 0, t1) => {
    const m = MED[name] || { n: 1, fps: 30 };
    const fps = m.fps || 30, n = m.n;
    const end = t1 != null ? t1 : t0 + (n - 1 - start) / (fps * speed);
    return [[t0, start], [end, Math.min(n - 1, start + (end - t0) * fps * speed)]];
  };
  const seqCanvas = (parent, cls, S, nw, nh, plan) => {
    const c = $("canvas", cls, parent);
    c.width = nw; c.height = nh;
    const g = c.getContext("2d");
    let last = -1;
    for (let f = 0; f < Math.min(S.n, 3); f++) loads.push(getFrame(S, Math.round(plan[0][1]) + f < S.n ? Math.round(plan[0][1]) + f : 0).p);
    media.push((t) => {
      let f = plan[0][1];
      for (let i = 0; i < plan.length - 1; i++) {
        const [t0, f0] = plan[i], [t1, f1] = plan[i + 1];
        if (t >= t0 && t <= t1) { f = f0 + (f1 - f0) * (t - t0) / (t1 - t0); break; }
        if (t > t1) f = f1;
      }
      f = Math.round(clamp(f, 0, S.n - 1));
      if (f === last || c.offsetParent === null) return null;
      const e = getFrame(S, f);
      const draw = () => { if (e.im.naturalWidth) { g.drawImage(e.im, 0, 0, nw, nh); last = f; } };
      if (e.im.complete) { draw(); return null; }
      return e.p.then(draw);
    });
    return c;
  };
  function mediaSrc(name, frame = 0) {
    const m = MED[name] || {};
    return `${m.base || "build/media/"}${m.dir || name}/${String(frame + 1).padStart(4, "0")}.jpg`;
  }
  /* un vrai média (vidéo ou image) dans un conteneur de sa taille native : renvoie l'élément */
  const mediaEl = (parent, name, plan, cls = "layer") => {
    const m = MED[name];
    if (!m) { console.warn("média inconnu (tools/media.py add …) :", name); return $("div", cls, parent); }
    if (m.n <= 1) { const i = img(parent, cls, mediaSrc(name)); css(i, { width: "100%", height: "100%", objectFit: "cover", objectPosition: "50% 0" }); return i; }
    const c = seqCanvas(parent, cls, frames(name), m.w, m.h, plan || [[0, 0], [m.n / (m.fps || 30), m.n - 1]]);
    css(c, { width: "100%", height: "100%" });
    return c;
  };
  /* plan d'un média de scène : m.still (image fixe), m.plan, sinon lecture depuis tIn */
  const planOf = (m, tIn) => m.still != null ? [[0, m.still], [1, m.still]] : (m.plan || play(m.name, tIn, m.speed || 1, m.start || 0, m.stopAt != null ? tIn + m.stopAt : undefined));
  /* suite d'écrans dans un même panneau : m.shots = [[mot, nom, image fixe?], …] */
  const shotsOf = (m, at) => m.shots ? [[0, m.name, planOf(m, at(m.at, -0.3))]].concat(m.shots.map(([w, name, still]) => {
    const t = at(w, -0.05);
    return [t, name, still != null ? [[0, still], [1, still]] : ((MED[name] || {}).n > 1 ? play(name, t) : null)];
  })) : undefined;
  const mediaSize = (name) => MED[name] ? [MED[name].w, MED[name].h] : [1600, 900];

  /* ── le hibou 3D (Wizi) ─────────────────────────────────────────────────
     1) séquence animée « <F.owl>-<pose> » dans WIZ_OWLS (WebP à alpha, 24 i/s, aller-retour) si le projet en a ;
     2) sinon image fixe détourée : F.owlImgs[pose] ou F.owlImg (défaut assets/owl-3d.webp, copié du kit par brand.py),
        le mouvement (rebond, flottement) est fait par le style. JAMAIS le hibou plat (il ne sert que dans le logo). */
  const owlSeq = {}, STATIC = {};
  const owlStaticSrc = (pose) => (F.owlImgs && F.owlImgs[pose]) || F.owlImg || "assets/owl-3d.webp";
  const owlCanvas = (parent, pose, tIn, tOut) => {
    const name = `${F.owl || F.slug}-${pose}`, m = OWLM[name];
    const cv = $("canvas", "", parent);
    css(cv, { width: "100%", height: "100%", display: "block" });
    const cx = cv.getContext("2d");
    if (!m) {
      const st = STATIC[owlStaticSrc(pose)];
      if (!st || !st.naturalWidth) { console.warn("hibou 3D introuvable :", owlStaticSrc(pose), "(python tools/brand.py)"); cv.width = 10; cv.height = 10; return { cv, w: 10, h: 10, missing: true }; }
      cv.width = st.naturalWidth; cv.height = st.naturalHeight;
      cx.drawImage(st, 0, 0);
      return { cv, w: cv.width, h: cv.height };
    }
    const S = owlSeq[name] || (owlSeq[name] = frames(name, m.base || "build/owl/", "webp", 3, m.n, m.dir));
    cv.width = m.w; cv.height = m.h;
    let last = -1;
    const end = tOut == null ? DUR : tOut + 0.8;
    for (let f = 0; f < Math.min(S.n, 10); f++) loads.push(getFrame(S, f).p);
    media.push((t) => {
      if (t < tIn - 0.05 || t > end) return null;
      const k = Math.max(0, Math.floor((t - tIn) * 24)), mm = 2 * (S.n - 1);
      const f = mm > 0 ? (k % mm < S.n ? k % mm : mm - (k % mm)) : 0;
      if (f === last) return null;
      const e = getFrame(S, f);
      const draw = () => { if (e.im.naturalWidth) { cx.clearRect(0, 0, m.w, m.h); cx.drawImage(e.im, 0, 0, m.w, m.h); last = f; } };
      if (e.im.complete) { draw(); return null; }
      return e.p.then(draw);
    });
    return { cv, w: m.w, h: m.h };
  };
  const preloadStatic = (src) => new Promise((res) => {
    const i = new Image(); i.decoding = "sync";
    i.onload = () => { STATIC[src] = i; res(); }; i.onerror = () => res();
    i.src = src;
  });

  /* ── logos officiels (kit de marque) : tracé puis remplissage ─────────── */
  const BRAND = window.WIZ_BRAND || {};
  const wordmark = (parent, key, sw = 6) => {
    const wrap = $("div", "wordmark abs", parent);
    if (!LOGOS[key]) {   // repli : texte bicolore en Baloo (WIZDI-BRAND §3) — à corriger avant livraison
      console.warn("logo absent de assets/logos.js :", key, "(python tools/brand.py)");
      const name = ((BRAND.modules || {})[key] || {}).name || key;
      const suf = /^wiz/i.test(name) ? name.slice(3) : "";
      wrap.innerHTML = suf ? `<span class="wiz-text"><b>Wiz</b><i style="color:${((BRAND.modules || {})[key] || {}).main || F.color || "#23A4D8"}">${suf}</i></span>`
        : `<span class="wiz-text"><b>${name}</b></span>`;
      return { wrap, svg: null, paths: [], strokes: [], ratio: 0.3, fallback: true };
    }
    wrap.innerHTML = LOGOS[key];
    const svg = wrap.querySelector("svg");
    const vb = svg.getAttribute("viewBox").split(/\s+/).map(Number);
    const paths = [...svg.querySelectorAll("path")];
    const strokes = paths.map((p) => {
      const s = p.cloneNode();
      s.setAttribute("fill", "none"); s.setAttribute("stroke", p.getAttribute("fill")); s.setAttribute("stroke-width", sw);
      s.setAttribute("stroke-linejoin", "round"); s.setAttribute("stroke-linecap", "round");
      svg.appendChild(s);
      return s;
    });
    return { wrap, svg, paths, strokes, ratio: vb[3] / vb[2] };
  };
  /* geste du site (WIZDI-BRAND §6), resserré pour la vidéo : contour qui se dessine, remplissage, trait qui s'efface */
  const drawLogo = (L, t, d = 0.5) => {
    if (!L.paths.length) { tl.fromTo(L.wrap, { opacity: 0 }, { opacity: 1, duration: 0.3, immediateRender: true }, t); return; }
    tl.set(L.paths, { fillOpacity: 0 }, 0);
    tl.set(L.strokes, { drawSVG: "0%", opacity: 1 }, 0);
    tl.to(L.strokes, { drawSVG: "100%", duration: d, ease: "power2.inOut", stagger: 0.08 }, t);
    tl.to(L.paths, { fillOpacity: 1, duration: 0.25, ease: "power2.out", stagger: 0.08 }, t + d * 0.7);
    tl.to(L.strokes, { opacity: 0, duration: 0.25 }, t + d + 0.1);
  };

  /* ── mots de l'écran (verbatim) : « WizPlay » en bleu Wiz + couleur du module, latin isolé ── */
  const fmtWord = (w) => {
    const m = w.match(/^([("“]*)(Wiz)([A-Z][a-z]+)([^A-Za-z]*)$/);
    if (m) return `${m[1]}<span class="lat brand"><span class="bw">${m[2]}</span><span class="bm">${m[3]}</span></span>${m[4]}`;
    const l = w.match(/^([("“]*)([A-Za-z0-9/.]+)([^A-Za-z0-9/.]*)$/);
    if (l) return `${l[1]}<span class="lat">${l[2]}</span>${l[3]}`;
    return w.replace(/</g, "&lt;");
  };
  /* découpe la phrase en groupes d'indices (sauts voulus = br), sans les mots x: true */
  const chunks = (k, max = 3) => {
    const ws = words(k), out = [];
    let cur = [];
    ws.forEach((w, i) => {
      if (!w.x) cur.push(i);
      if ((w.br && cur.length) || cur.length >= max) { out.push(cur); cur = []; }
    });
    if (cur.length) out.push(cur);
    return out;
  };

  /* ── panneau d'écran : un VRAI média, caméra en coordonnées de la source, pose en images-clés ──
     o = { name, plan, x, y, w, rot, cam:[[t, zoom, fx, fy, ease?]…], pose:[[t, x, y, s, rot, ease?]…], t0, t1, layer, cls } */
  const panel = (o) => {
    const [iw, ih] = o.iw ? [o.iw, o.ih] : mediaSize(o.name);
    const w = o.w || Math.min(960, W * 0.89), h = o.h || Math.round(w * ih / iw);
    const t0 = o.t0 == null ? 0 : o.t0, t1 = o.t1 == null ? DUR : o.t1;
    const el = $("div", "pnl " + (o.cls || ""), o.layer);
    css(el, { width: w + "px", height: h + "px", transformOrigin: `${w / 2}px ${h / 2}px`, display: "none" });
    const pop = $("div", "pop", el);
    const fr = $("div", "fr", pop);
    const inner = $("div", "layer", fr);
    css(inner, { width: iw + "px", height: ih + "px", right: "auto", bottom: "auto", transformOrigin: "0 0" });
    (o.shots || [[0, o.name, o.plan]]).forEach(([t, name, plan], k) => {
      const hold = $("div", "layer", inner);
      mediaEl(hold, name, plan);
      tl.set(hold, { opacity: k ? 0 : 1 }, 0);
      if (k) tl.to(hold, { opacity: 1, duration: 0.14, ease: "none" }, t - 0.07);
    });
    const ink = document.createElementNS(NS, "svg");
    ink.setAttribute("class", "ink"); ink.setAttribute("width", iw); ink.setAttribute("height", ih); ink.setAttribute("viewBox", `0 0 ${iw} ${ih}`);
    pop.appendChild(ink);
    const cam = o.cam || [[0, 1, iw / 2, ih / 2]];
    const at = (t) => {
      const [z, fx, fy] = kfEval(cam, t, 3);
      const S = z * w / iw;
      return { S, ox: clamp(w / 2 - fx * S, w - iw * S, 0), oy: clamp(h / 2 - fy * S, h - ih * S, 0) };
    };
    const pose = o.pose || [[0, o.x, o.y, 1, o.rot || 0]];
    const P_ = (t) => kfEval(pose, t, 4);
    ambient.push((t) => {
      const on = t >= t0 - 0.05 && t <= t1 + 0.05;
      el.style.display = on ? "block" : "none";
      if (!on) return;
      const a = at(t), tr = `translate(${a.ox.toFixed(2)}px,${a.oy.toFixed(2)}px) scale(${a.S.toFixed(5)})`;
      inner.style.transform = tr; ink.style.transform = tr;
      const [px, py, s, r] = P_(t);
      el.style.transform = `translate(${(px - w / 2).toFixed(2)}px,${(py - h / 2).toFixed(2)}px) rotate(${r.toFixed(3)}deg) scale(${s.toFixed(4)})`;
    });
    /* point de la source -> coordonnées de la scène (caméra + pose) */
    const pt = (t, x, y) => {
      const a = at(t), [px, py, s, r] = P_(t);
      const dx = a.ox + x * a.S - w / 2, dy = a.oy + y * a.S - h / 2, c = Math.cos(r * DEG), sn = Math.sin(r * DEG);
      return [px + s * (dx * c - dy * sn), py + s * (dx * sn + dy * c)];
    };
    const kAt = (t) => at(t).S * P_(t)[2];
    tl.set(pop, { opacity: 0, transformPerspective: 1600 }, 0);
    return { el, pop, fr, inner, ink, at, pt, kAt, pose: P_, iw, ih, w, h, name: o.name, t0, t1 };
  };

  /* chemin d'un trait « à main levée » autour d'une zone (repère au feutre) */
  const loopPath = (cx, cy, rx, ry, seed, tilt = -3, turns = 1.1, sq = 3.1) => {
    const r = rng(seed * 31 + 5), N = 30;
    const a0 = -Math.PI * (0.62 + r() * 0.12), ct = Math.cos(tilt * DEG), st = Math.sin(tilt * DEG), pts = [];
    for (let i = 0; i <= N; i++) {
      const k = i / N, a = a0 - k * turns * TAU;
      const j = 1 + (r() - 0.5) * 0.045 + (k > 0.8 ? (k - 0.8) * 0.4 : 0) - (k < 0.08 ? (0.08 - k) * 0.5 : 0);
      const ca = Math.cos(a), sa = Math.sin(a);
      const ex = Math.sign(ca) * Math.pow(Math.abs(ca), 2 / sq) * rx * j, ey = Math.sign(sa) * Math.pow(Math.abs(sa), 2 / sq) * ry * j;
      pts.push([cx + ex * ct - ey * st, cy + ex * st + ey * ct]);
    }
    const f = (v) => v.toFixed(1);
    let d = `M${f(pts[0][0])} ${f(pts[0][1])}`;
    for (let i = 0; i < pts.length - 1; i++) {
      const p0 = pts[Math.max(0, i - 1)], p1 = pts[i], p2 = pts[i + 1], p3 = pts[Math.min(pts.length - 1, i + 2)];
      d += ` C${f(p1[0] + (p2[0] - p0[0]) / 6)} ${f(p1[1] + (p2[1] - p0[1]) / 6)} ${f(p2[0] - (p3[0] - p1[0]) / 6)} ${f(p2[1] - (p3[1] - p1[1]) / 6)} ${f(p2[0])} ${f(p2[1])}`;
    }
    return d;
  };
  const roundRectPath = (x, y, w, h, r) => `M${x + r} ${y}H${x + w - r}A${r} ${r} 0 0 1 ${x + w} ${y + r}V${y + h - r}A${r} ${r} 0 0 1 ${x + w - r} ${y + h}H${x + r}A${r} ${r} 0 0 1 ${x} ${y + h - r}V${y + r}A${r} ${r} 0 0 1 ${x + r} ${y}Z`;

  /* le morceau sort EXACTEMENT de son emplacement dans l'écran entier, dans sa vraie forme (règle d'Eyal)
     s = panneau ; r = [x, y, w, h] dans la source ; to = { x, y, w, rot } ; o.back : il y retourne ;
     o.frame : image de la séquence à découper (défaut 0) ; o.cls / o.deco : habillage du style.
     ⚠ une découpe ne s'agrandit pas au-delà de ~1x de la source (sinon floue) : to.w <= r.w autant que possible. */
  const pieceOut = (s, r, t, tOut, to, o = {}) => {
    const [rx, ry, rw, rh] = r, w = to.w, h = w * rh / rw, k = w / rw;
    if (k > 1.25) console.warn(`pieceOut ${s.name} : découpe agrandie x${k.toFixed(2)} (floue) — réduire to.w`);
    const el = $("div", "abs piece " + (o.cls || ""), o.layer || s.el.parentNode);
    box(el, to.x, to.y, w, h);
    const bob = $("div", "layer", el);
    const fr = $("div", "pf", bob);
    css(fr, { backgroundImage: `url(${o.src || mediaSrc(s.name, o.frame || 0)})`, backgroundSize: `${s.iw * k}px ${s.ih * k}px`, backgroundPosition: `${-rx * k}px ${-ry * k}px` });
    const c0 = s.pt(t, rx + rw / 2, ry + rh / 2), home = { x: c0[0] - to.x, y: c0[1] - to.y, scale: rw * s.kAt(t) / w, rotation: s.pose(t)[3] };
    tl.set(el, { opacity: 0 }, 0);
    const din = Math.max(0.2, Math.min(o.din || 0.5, (o.back ? tOut - 0.28 : tOut - 0.2) - t - 0.01));
    tl.fromTo(el, { ...home, opacity: 1 }, { x: 0, y: 0, scale: 1, rotation: to.rot || 0, opacity: 1, duration: din, ease: o.ease || "back.out(1.5)", immediateRender: false }, t);
    if (o.deco) o.deco(fr, t, tOut);
    if (o.back) {
      const hb = s.pt(tOut - 0.26, rx + rw / 2, ry + rh / 2);
      tl.to(el, { x: hb[0] - to.x, y: hb[1] - to.y, scale: rw * s.kAt(tOut) / w, rotation: s.pose(tOut)[3], duration: 0.26, ease: "power3.in" }, tOut - 0.26);
      tl.set(el, { opacity: 0 }, tOut);
    } else if (tOut != null) tl.to(el, { scale: 0.3, rotation: (to.rot || 0) * -3, opacity: 0, duration: 0.2, ease: "back.in(2)" }, tOut - 0.2);
    const ph = (to.x + to.y) * 0.01;
    ambient.push((tt) => { bob.style.transform = `translateY(${(Math.sin(tt * 2.2 + ph) * 7).toFixed(2)}px) rotate(${(Math.sin(tt * 1.6 + ph) * 1.0).toFixed(2)}deg)`; });
    sfx(t, "whooshUp", 0.4); sfx(t + din * 0.6, "pop", 0.35);
    return { el, fr, bob };
  };

  /* ── particules (canvas, déterministe) : confettis, éclats ── */
  const CONF = [], POWS = [];
  let fxPal = ["#ffffff"];
  const confetti = (t0, x, y, o = {}) => CONF.push({ t0, x, y, n: o.n || 60, sp: o.sp || 1100, ang: o.ang != null ? o.ang : -90, spread: o.spread != null ? o.spread : 360,
    life: o.life || 1.9, seed: o.seed || CONF.length + 1, cols: o.cols || fxPal, shape: o.shape || "mix", g: o.g != null ? o.g : 900 });
  const pow = (t0, x, y, o = {}) => POWS.push({ t0, x, y, r0: o.r0 || 120, r1: o.r1 || 300, n: o.n || 14, col: o.col || "#fff", w: o.w || 12, life: o.life || 0.34, seed: o.seed || POWS.length + 3 });
  let fxCtx = null;
  const fxLayer = (parent) => { const c = $("canvas", "fx", parent); c.width = W; c.height = H; fxCtx = c.getContext("2d"); return c; };
  const drawFx = (t) => {
    if (!fxCtx) return;
    const ctx = fxCtx;
    ctx.clearRect(0, 0, W, H);
    for (const b of POWS) {
      const dt = t - b.t0;
      if (dt < 0 || dt > b.life) continue;
      const k = dt / b.life, r = rng(b.seed * 97 + 1);
      ctx.strokeStyle = b.col; ctx.lineCap = "round"; ctx.lineWidth = b.w * (1 - k * 0.6);
      for (let i = 0; i < b.n; i++) {
        const a = (i / b.n) * TAU + r() * 0.25, jr = 0.8 + r() * 0.4;
        const ra = lerp(b.r0, b.r1, Math.pow(k, 0.6)) * jr, rb = lerp(b.r0 + 40, b.r1 + 120, Math.pow(k, 0.45)) * jr;
        ctx.beginPath(); ctx.moveTo(b.x + Math.cos(a) * ra, b.y + Math.sin(a) * ra); ctx.lineTo(b.x + Math.cos(a) * rb, b.y + Math.sin(a) * rb); ctx.stroke();
      }
    }
    for (const c of CONF) {
      const dt = t - c.t0;
      if (dt < 0 || dt > c.life) continue;
      const r = rng(c.seed * 131 + 7);
      for (let i = 0; i < c.n; i++) {
        const a = (c.ang + (r() - 0.5) * c.spread) * DEG, v = c.sp * (0.35 + 0.65 * r());
        const kd = 2.4, e = (1 - Math.exp(-kd * dt)) / kd;
        const x = c.x + Math.cos(a) * v * e + Math.sin(dt * 3 + i) * 14;
        const y = c.y + Math.sin(a) * v * e + c.g * dt * dt * 0.5;
        const col = c.cols[Math.floor(r() * c.cols.length)], w = 14 + r() * 14, h = 8 + r() * 8, rot = r() * TAU + dt * (r() - 0.5) * 16;
        const flip = Math.cos(r() * TAU + dt * (6 + r() * 8)), shape = r();
        const al = dt > c.life * 0.75 ? 1 - (dt - c.life * 0.75) / (c.life * 0.25) : 1;
        ctx.save(); ctx.globalAlpha = al; ctx.translate(x, y); ctx.rotate(rot); ctx.fillStyle = col;
        ctx.scale(1, flip);
        if (shape < 0.6) ctx.fillRect(-w / 2, -h / 2, w, h);
        else { ctx.beginPath(); ctx.arc(0, 0, h * 0.75, 0, TAU); ctx.fill(); }
        ctx.restore();
      }
    }
  };

  /* ── lecture / rendu ──────────────────────────────────────────────────── */
  const stage = document.getElementById("stage");
  css(stage, { width: W + "px", height: H + "px" });
  const extraDraw = [];
  const seek = async (t) => {
    t = clamp(t, 0.001, DUR);
    tl.time(t, false);
    for (const fn of ambient) fn(t);
    drawFx(t);
    for (const fn of extraDraw) fn(t);
    const wait = media.map((fn) => fn(t)).filter(Boolean);
    if (wait.length) await Promise.all(wait);
  };
  window.__seek = seek;
  window.__dur = DUR;
  window.__fmt = FMT;
  /* texte visible à l'instant courant (contrôle verbatim : tools/render.py textscan) */
  window.__visibleText = () => {
    const out = [], sr = stage.getBoundingClientRect(), sc = sr.width / W;
    const vis = (el) => {
      for (let e = el; e && e !== document.body; e = e.parentElement) {
        const cs = getComputedStyle(e);
        if (cs.display === "none" || cs.visibility === "hidden" || +cs.opacity < 0.05) return false;
      }
      return true;
    };
    const walk = document.createTreeWalker(stage, NodeFilter.SHOW_TEXT);
    for (let n = walk.nextNode(); n; n = walk.nextNode()) {
      const s = n.nodeValue.trim();
      if (!s || !vis(n.parentElement)) continue;
      const r = n.parentElement.getBoundingClientRect();
      if (r.width < 2 || r.right < sr.left || r.left > sr.right || r.bottom < sr.top || r.top > sr.bottom) continue;
      out.push({ text: s, size: Math.round(parseFloat(getComputedStyle(n.parentElement).fontSize) * sc), y: Math.round((r.top - sr.top) / sc) });
    }
    return out;
  };
  const fit = () => { if (!RENDER) stage.style.transform = `scale(${Math.min(innerWidth / W, (innerHeight - 50) / H)})`; };
  addEventListener("resize", fit);
  fit();

  const run = (build) => {
    const owlSrcs = new Set([owlStaticSrc("wave"), ...Object.values(F.owlImgs || {})]);
    Promise.all([document.fonts.load('700 200px "Fredoka"', "אבגדהוזחטיכלמנסעפצקרשת"), document.fonts.load('600 200px "Fredoka"', "אבג"),
      document.fonts.load('500 60px "Fredoka"', "אבג"), document.fonts.load('700 200px "Baloo Latin"', "WizPlay Wizdi 0123456789"),
      ...[...owlSrcs].map(preloadStatic)]).catch(() => null).then(() => {
      build();
      tl.to({}, { duration: 0.01 }, DUR - 0.01);
      tl.time(DUR, true);
      tl.time(0, true);
      window.__timeline = Object.assign({ slug: F.slug || "film", fmt: FMT, w: W, h: H, dur: DUR, vo_at: VO_AT, sfx: SFX.sort((a, b) => a.t - b.t), keep: (window.KIT || {}).keep || null,
        lines: Object.fromEntries(KEYS.map((k) => [k, [LS(k), LE(k)]])) }, WZ.timelineExtra || {});
      return Promise.all([document.fonts.ready, ...loads]);
    }).then(async () => {
      await seek(params.has("t") ? +params.get("t") : 0);
      window.__ready = true;
      if (RENDER) return;
      const bar = $("div", "scrub", document.body, `<button>▶</button><input type="range" min="0" max="${DUR}" step="0.01" value="0"><span>0.00</span>`
        + `<select>${Object.keys(SIZES).map((f) => `<option${f === FMT ? " selected" : ""}>${f}</option>`).join("")}</select>`);
      const [btn, rg, lab, sel] = bar.children;
      sel.onchange = () => { params.set("format", sel.value); location.search = params.toString(); };
      let playing = false, t0 = 0, s0 = 0;
      const audio = new Audio(F.previewAudio || "out/mix.wav");
      const tick = (now) => {
        if (!playing) return;
        const t = s0 + (now - t0) / 1000;
        if (t >= DUR) { playing = false; btn.textContent = "▶"; audio.pause(); return; }
        seek(t); rg.value = t; lab.textContent = t.toFixed(2);
        requestAnimationFrame(tick);
      };
      btn.onclick = () => {
        playing = !playing; btn.textContent = playing ? "❚❚" : "▶";
        if (playing) { s0 = +rg.value; t0 = performance.now(); audio.currentTime = s0; audio.play().catch(() => {}); requestAnimationFrame(tick); } else audio.pause();
      };
      rg.oninput = () => { seek(+rg.value); lab.textContent = (+rg.value).toFixed(2); };
    });
  };

  const WZ = window.WZ = {
    F, VO, WD, MED, LOGOS, BRAND, FMT, W, H, SAFE, DUR, VO_AT, KEYS, LS, LE, WT, WE, T0, T1, words, shown, chunks, fmtWord,
    $, css, box, clamp, lerp, prog, ease, rng, kfEval, rgba, mix, hexRgb, TAU, DEG, NS,
    tl, ambient, media, loads, sfx, img, window: window_, extraDraw,
    frames, getFrame, play, planOf, shotsOf, seqCanvas, mediaEl, mediaSrc, mediaSize, owlCanvas, wordmark, drawLogo,
    panel, pieceOut, loopPath, roundRectPath, confetti, pow, fxLayer, setFxPal: (p) => { fxPal = p; },
    stage, run, seek,
  };
})();
