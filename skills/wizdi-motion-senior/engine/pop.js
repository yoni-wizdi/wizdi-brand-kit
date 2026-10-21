/* ──────────────────────────────────────────────────────────────────────────
   STYLE « POP CINÉTIQUE » WIZDI — la grammaire VALIDÉE des films du 13/10/2026 (WizPlan V2 → 5 films outils → concours
   du 15/10), rendue indépendante du projet et du format (9:16, 4:5, 16:9 : chaque format a SA mise en page, LAY).

   La grammaire : aplats saturés + trame de points changés par des VOLETS francs (iris, diagonale, montée, fente) sur le
   temps ; typographie GÉANTE qui claque au mot (le mot fort inversé sur une PLAQUE, comme un tampon) ; VRAIS écrans en
   STICKERS (liseré blanc 14 px, ombre franche décalée 18 px, ±2°) ; règle d'Eyal : l'écran entier, un CERCLE DE FEUTRE,
   puis le MORCEAU QUI SORT dans sa vraie forme ; vraies photos dans des BULLES qui ondulent ; HIBOU 3D à liseré blanc qui
   rebondit sur les mots ; stickers décoratifs (+ ★ ○ ×) qui flottent et pulsent sur le tempo ; CONFETTIS et éclats aux
   sommets ; plaque du logo fixe en haut qui pulse à chaque scène ; carte de fin (logo, slogan en pastille, hibou joyeux,
   signature Wizdi, wizdi.school, copyright).

   Deux usages :
     1) piloté par film.js : WIZ_FILM.scenes = { s1: { kind: "brand"|"generic"|"end", emph, media, portal, owl, count, chips, … } }
        puis, dans style.js : WZ.run(() => POP.build());
     2) à la main (senior) : WZ.run(() => { POP.wipe(…); POP.kl(…); POP.sticker(…); … }) — toutes les briques sont dans window.POP.
   Les champs d'une scène peuvent être surchargés PAR FORMAT : s3: { media: […], "16x9": { media: […] } }.
   ────────────────────────────────────────────────────────────────────────── */
(() => {
  "use strict";
  const Z = window.WZ, F = Z.F;
  const { tl, $, css, box, rng, rgba, mix, sfx, TAU, NS, W, H, FMT, DUR, KEYS, LS, WT, WE, T0, T1 } = Z;
  const C = F.color || "#23A4D8", NAVY = "#1E1B4B", CREAM = "#FFF4E6", SKY = "#23A4D8", SUN = F.sun || "#FFD23F", WHITE = "#FFFFFF";
  const CD = mix(C, "#000000", 0.28);
  Z.setFxPal([C, SKY, SUN, WHITE, CREAM, NAVY]);
  const stage = Z.stage;
  stage.style.setProperty("--mod", C); stage.style.setProperty("--navy", NAVY);
  /* thèmes de fond : ink = mots ; plate/pInk = mot fort inversé ; tsh = ombre des mots ; csh = ombre des stickers */
  const TH = {
    mod: { bg: C, dot: rgba(CD, 0.45), ink: WHITE, plate: NAVY, pInk: C, tsh: NAVY, csh: NAVY, ang: "200deg" },
    navy: { bg: NAVY, dot: rgba(C, 0.42), ink: WHITE, plate: C, pInk: NAVY, tsh: C, csh: C, ang: "20deg" },
    cream: { bg: CREAM, dot: rgba(C, 0.3), ink: NAVY, plate: C, pInk: WHITE, tsh: C, csh: NAVY, ang: "340deg" },
    sky: { bg: SKY, dot: "rgba(10,120,170,.4)", ink: WHITE, plate: NAVY, pInk: SKY, tsh: NAVY, csh: NAVY, ang: "160deg" },
    sun: { bg: SUN, dot: rgba(mix(SUN, "#000000", 0.25), 0.4), ink: NAVY, plate: C, pInk: WHITE, tsh: WHITE, csh: NAVY, ang: "135deg" },
  };
  const ORDER = F.popThemes || ["mod", "navy", "cream", "sky", "mod", "sun", "navy", "cream"];

  /* ── mise en page par format (zones sûres respectées ; à affiner sur planche, surchargeable par F.layout[FMT]) ── */
  const LAYOUTS = {
    "9x16": {
      bug: { x: 540, y: 330, w: 280 }, wm: { x: 540, y: 760, w: 900 },
      wordsX: 540, words: [520, 740], size: [230, 190], maxW: 960,
      brandBefore: { y: 470, size: 220 }, brandAfter: { y: 1050, dy: 160, size: 150 },
      media: { x: 540, y: 1180, w: 980, wp: 540 }, piece: [{ x: 790, y: 1420, w: 380, rot: -3 }, { x: 290, y: 1420, w: 380, rot: 3 }],
      owl: { x: 850, y: 1320, h: 400 }, brandOwl: { x: 800, y: 1290, h: 440 }, portal: { x: 540, y: 1170, d: 640 },
      count: { x: 540, y: 1290, size: 260 }, chips: { x: 540, y: 980, dy: 170, size: 76 }, wizdi: { x: 540, y: 1300, w: 600 },
      deco: [[110, 560], [970, 600], [100, 1440], [980, 1450], [110, 1010], [970, 1030]],
      end: { logo: { x: 540, y: 420, w: 860 }, slog: { x: 540, y: 760, w: 980, h: 360, size: 150 }, owl: { x: 540, y: 1140, h: 300 },
        sig: { y: 1340, w: 300, h: 86 }, url: { y: 1420, size: 54 }, copy: { y: 1472, size: 22 } },
    },
    "4x5": {
      bug: { x: 540, y: 105, w: 240 }, wm: { x: 540, y: 560, w: 860 },
      wordsX: 540, words: [300, 490], size: [200, 170], maxW: 960,
      brandBefore: { y: 280, size: 190 }, brandAfter: { y: 840, dy: 140, size: 135 },
      media: { x: 540, y: 905, w: 960, wp: 430 }, piece: [{ x: 790, y: 1160, w: 340, rot: -3 }, { x: 290, y: 1160, w: 340, rot: 3 }],
      owl: { x: 880, y: 1080, h: 330 }, brandOwl: { x: 830, y: 1070, h: 360 }, portal: { x: 540, y: 900, d: 560 },
      count: { x: 540, y: 1000, size: 230 }, chips: { x: 540, y: 760, dy: 150, size: 68 }, wizdi: { x: 540, y: 1050, w: 540 },
      deco: [[80, 110], [1000, 110], [80, 1275], [1000, 1280]],
      end: { logo: { x: 540, y: 290, w: 800 }, slog: { x: 540, y: 610, w: 980, h: 300, size: 130 }, owl: { x: 540, y: 940, h: 260 },
        sig: { y: 1110, w: 280, h: 80 }, url: { y: 1190, size: 50 }, copy: { y: 1250, size: 22 } },
    },
    "16x9": {
      bug: { x: 1700, y: 128, w: 240 }, wm: { x: 960, y: 430, w: 1080 },
      wordsX: 1440, words: [380, 590], size: [150, 130], maxW: 720,
      brandBefore: { y: 200, size: 150 }, brandAfter: { y: 700, dy: 120, size: 110 },
      media: { x: 580, y: 560, w: 940, wp: 400 }, piece: [{ x: 1300, y: 840, w: 340, rot: -3 }, { x: 1300, y: 840, w: 340, rot: 3 }],
      owl: { x: 1720, y: 860, h: 300 }, brandOwl: { x: 1660, y: 800, h: 360 }, portal: { x: 580, y: 560, d: 600 },
      count: { x: 580, y: 580, size: 240 }, chips: { x: 1440, y: 760, dy: 120, size: 64 }, wizdi: { x: 1440, y: 820, w: 520 },
      deco: [[1840, 300], [80, 280], [1840, 960], [80, 980], [420, 1010], [1480, 1010]],
      end: { logo: { x: 960, y: 240, w: 700 }, slog: { x: 960, y: 520, w: 1400, h: 230, size: 115 }, owl: { x: 1700, y: 860, h: 270 },
        sig: { y: 780, w: 280, h: 80 }, url: { y: 880, size: 52 }, copy: { y: 950, size: 22 } },
    },
  };
  LAYOUTS["1x1"] = LAYOUTS["4x5"];
  const LAY = Object.assign({}, LAYOUTS[FMT] || LAYOUTS["9x16"], (F.layout || {})[FMT] || {});

  /* ── calques ──────────────────────────────────────────────────────────── */
  const bgL = $("div", "layer", stage);
  const raysL = $("div", "layer", stage);
  const stickL = $("div", "layer", stage);
  const bubL = $("div", "layer", stage);
  const panelL = $("div", "layer", stage);
  css(panelL, { perspective: "1800px", perspectiveOrigin: "50% 45%" });
  const owlL = $("div", "layer", stage);
  Z.fxLayer(stage);
  const typeL = $("div", "layer", stage);
  const hud = $("div", "layer", stage);

  /* ── volets de fond (aplat + trame de points), sur le temps ───────────── */
  const WIPES = [];
  const wipe = (t, th, kind = "iris", o = {}) => {
    const el = $("div", "bgw", bgL);
    el.style.background = th.bg;
    const ht = $("div", "ht", el);
    ht.style.setProperty("--dot", th.dot); ht.style.setProperty("--ang", o.ang || th.ang);
    const d = o.d || 0.42;
    let from = null, to = null;
    if (kind === "iris") {
      const [x, y] = o.at || [W / 2, H / 2];
      const R = Math.ceil(Math.hypot(Math.max(x, W - x), Math.max(y, H - y)) + 30);
      from = `circle(0px at ${x}px ${y}px)`; to = `circle(${R}px at ${x}px ${y}px)`;
    } else if (kind === "diag") {            // de droite à gauche (sens de lecture hébreu)
      from = "polygon(115% -5%, 115% -5%, 115% 105%, 150% 105%)"; to = "polygon(-40% -5%, 115% -5%, 115% 105%, -5% 105%)";
    } else if (kind === "rise") {
      from = "inset(100% 0% 0% 0%)"; to = "inset(0% 0% 0% 0%)";
    } else if (kind === "split") {
      from = "inset(50% 0% 50% 0%)"; to = "inset(0% 0% 0% 0%)";
    }
    const t0 = from ? t - d * 0.45 : -1, t1 = from ? t0 + d : -1;
    if (from) {
      tl.set(el, { clipPath: from }, 0);
      tl.to(el, { clipPath: to, duration: d, ease: o.ease || "power3.inOut" }, t0);
      if (!o.quiet) sfx(t0, "whoosh", 0.5);
    }
    WIPES.push({ el, t0, t1 });
    return el;
  };
  /* bande d'accent avant le nouveau fond (double volet) */
  const band = (t, th, accent, kind = "diag") => { wipe(t - 0.07, { ...th, bg: accent, dot: "rgba(0,0,0,0)" }, kind, { d: 0.38, quiet: true }); wipe(t + 0.05, th, kind, { d: 0.4 }); };
  Z.ambient.push((t) => {
    let top = 0;
    WIPES.forEach((w, i) => { if (w.t1 < 0 || t >= w.t1) top = i; });
    WIPES.forEach((w, i) => { w.el.style.display = i < top || (w.t0 >= 0 && t < w.t0 - 0.02) ? "none" : "block"; });
  });
  const rays = $("div", "rays", raysL);
  css(rays, { background: "repeating-conic-gradient(from 0deg, rgba(255,255,255,.5) 0deg 7.5deg, transparent 7.5deg 15deg)" });
  tl.set(rays, { opacity: 0 }, 0);
  let raysY = H / 2;
  Z.ambient.push((t) => { rays.style.transform = `translateY(${raysY - H / 2}px) rotate(${(t * 14).toFixed(2)}deg)`; });

  /* ── stickers décoratifs, qui flottent et rebondissent sur le tempo ──── */
  let BEAT = 0.53, BT0 = 0;
  const pulseAt = (t) => { const ph = (t - BT0) / BEAT; const f = ph - Math.floor(ph); return Math.exp(-f * 7); };
  const SHAPE = {
    "+": '<rect x="36" y="4" width="28" height="92" rx="14"/><rect x="4" y="36" width="92" height="28" rx="14"/>',
    "-": '<rect x="4" y="36" width="92" height="28" rx="14"/>',
    "x": '<g transform="rotate(45 50 50)"><rect x="36" y="4" width="28" height="92" rx="14"/><rect x="4" y="36" width="92" height="28" rx="14"/></g>',
    "=": '<rect x="4" y="20" width="92" height="24" rx="12"/><rect x="4" y="56" width="92" height="24" rx="12"/>',
    "*": '<polygon points="50,4 61,37 96,37 68,58 79,92 50,71 21,92 32,58 4,37 39,37"/>',
    "v": '<path d="M10 52 L38 80 L90 22" fill="none" stroke-width="20" stroke-linecap="round" stroke-linejoin="round"/>',
    ">": '<polygon points="22,8 90,50 22,92"/>',
    "o": '<circle cx="50" cy="50" r="40"/>',
    "c": '<path d="M14 18 H86 Q94 18 94 26 V62 Q94 70 86 70 H44 L24 88 L28 70 H14 Q6 70 6 62 V26 Q6 18 14 18 Z"/>',
  };
  let mstN = 0;
  const deco = (k, x, y, s, col, t0, t1, o = {}) => {
    const n = mstN++;
    const el = $("div", "mst", stickL);
    css(el, { width: s + "px", height: s + "px", display: "none" });
    const inner = $("div", "layer", el);
    const shp = SHAPE[k] || `<text x="50" y="88" font-size="118" text-anchor="middle">${k}</text>`;
    inner.innerHTML = k === "v"
      ? `<svg viewBox="0 0 100 100"><g stroke="#fff" fill="none">${shp.replace('stroke-width="20"', 'stroke-width="36"')}</g><g stroke="${col}" fill="none">${shp}</g></svg>`
      : `<svg viewBox="0 0 100 100"><g fill="#fff" stroke="#fff" stroke-width="15" stroke-linejoin="round">${shp}</g><g fill="${col}">${shp}</g></svg>`;
    const sd = Math.max(5, s * 0.055);
    css(inner, { filter: `drop-shadow(${sd}px ${sd}px 0 ${o.sh || NAVY})` });
    const r = rng(n * 7919 + 13);
    const glyph = !SHAPE[k];
    const ph = r() * TAU, w1 = 0.8 + r() * 0.7, rot0 = (r() - 0.5) * (glyph ? 24 : 50), spin = (r() - 0.5) * (glyph ? 6 : 36);
    Z.ambient.push((t) => {
      const on = t >= t0 - 0.05 && t <= t1 + 0.3;
      el.style.display = on ? "block" : "none";
      if (!on) return;
      const dy = Math.sin(t * w1 * 2.1 + ph) * 18, dx = Math.cos(t * w1 * 1.4 + ph) * 10;
      el.style.transform = `translate(${(x - s / 2 + dx).toFixed(1)}px,${(y - s / 2 + dy).toFixed(1)}px) rotate(${(rot0 + spin * (t - t0) + Math.sin(t * 1.7 + ph) * (glyph ? 6 : 9)).toFixed(2)}deg) scale(${(1 + pulseAt(t) * 0.12).toFixed(4)})`;
    });
    tl.set(inner, { scale: 0 }, 0);
    tl.to(inner, { scale: 1, duration: 0.65, ease: "elastic.out(1, 0.42)" }, t0);
    tl.to(inner, { scale: 0, duration: 0.2, ease: "back.in(2)" }, t1);
  };
  const DECO = F.popDeco || ["+", "*", "o", "x"];
  const decos = (t0, t1, th, n = 4, seed = 1) => {
    const r = rng(seed * 101 + 7), cols = [C, SKY, NAVY, WHITE, SUN, CREAM].filter((c) => c !== th.bg), SP = LAY.deco;
    for (let i = 0; i < Math.min(n, SP.length); i++) {   // jamais deux stickers au même endroit
      const [x, y] = SP[(i + seed) % SP.length];
      deco(DECO[(i + seed) % DECO.length], x, y, 100 + r() * 50, cols[(i + seed) % cols.length], t0 + 0.08 + i * 0.05, t1 - 0.04 * i, { sh: th.csh === WHITE ? NAVY : th.csh });
    }
  };

  /* étoile « BD » derrière un élément fort */
  const starB = (x, y, r, col, t, tOut, o = {}) => {
    const el = $("div", "burst2", o.layer || panelL);
    box(el, x, y, 2 * r, 2 * r);
    const n = o.n || 14, rr = rng(o.seed || Math.round(x + y));
    const pts = [];
    for (let i = 0; i < n * 2; i++) { const a = (i / (n * 2)) * TAU - Math.PI / 2, k = i % 2 ? 0.64 + rr() * 0.08 : 0.94 + rr() * 0.06; pts.push((50 + Math.cos(a) * 48 * k).toFixed(2) + "," + (50 + Math.sin(a) * 48 * k).toFixed(2)); }
    el.innerHTML = `<svg viewBox="0 0 100 100"><polygon points="${pts.join(" ")}" fill="${col}" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"/></svg>`;
    css(el.firstChild, { filter: `drop-shadow(${r * 0.035}px ${r * 0.035}px 0 ${o.sh || NAVY})` });
    tl.set(el, { scale: 0, rotation: -40 }, 0);
    tl.to(el, { scale: 1, rotation: 0, duration: tOut != null ? Math.min(0.6, tOut - t - 0.01) : 0.6, ease: "elastic.out(1, 0.5)" }, t);
    if (tOut != null) tl.to(el, { scale: 0, duration: 0.2, ease: "back.in(2)" }, tOut);
    Z.ambient.push((tt) => { el.style.rotate = `${((tt - t) * 16).toFixed(2)}deg`; });
    return el;
  };

  /* ── typographie géante : o.words = [[mot VERBATIM, instant, plaque?], …] ── */
  const shake = (el, t, a = 10) => {
    tl.to(el, { keyframes: [{ x: -a, y: a * 0.35, rotation: -0.6, duration: 0.035 }, { x: a * 0.8, y: -a * 0.3, rotation: 0.5, duration: 0.035 },
      { x: -a * 0.45, y: a * 0.15, rotation: -0.2, duration: 0.035 }, { x: a * 0.2, y: 0, rotation: 0, duration: 0.035 }, { x: 0, y: 0, duration: 0.04 }], ease: "none" }, t);
  };
  const kl = (o) => {
    const th = o.th, el = $("div", "kl", typeL);
    css(el, { width: W + "px" });
    const sh = $("div", "ksh", el);
    const items = o.words.map(([w, t, plate]) => {
      const brand = /^[("“]*Wiz[A-Z]/.test(w);
      const wd = $("span", "kw2" + (plate ? " hp" : ""), sh);
      let pl = null;
      if (plate) { pl = $("span", "pl", wd); css(pl, { background: brand ? WHITE : th.plate, boxShadow: `.05em .05em 0 ${th.plate === NAVY ? WHITE : NAVY}` }); }
      const m = $("span", "km", wd);
      const tx = $("span", "kt", m, Z.fmtWord(w));
      if (brand && !plate) { const b = tx.querySelector(".brand"); if (b) b.classList.add("brandBox"); }
      css(tx, { color: plate ? th.pInk : th.ink, textShadow: plate || brand ? "none" : `.045em .045em 0 ${th.tsh}` });
      return { wd, pl, tx, t, plate };
    });
    let fs = o.size;
    css(el, { fontSize: fs + "px" });
    const maxW = o.maxW || LAY.maxW, mw = sh.offsetWidth;
    if (mw > maxW) { fs = Math.floor(fs * maxW / mw); css(el, { fontSize: fs + "px" }); }
    css(el, { top: Math.round(o.y - sh.offsetHeight / 2) + "px", left: (o.x != null ? o.x : W / 2) - W / 2 + "px" });
    if (o.rot) tl.set(sh, { rotation: o.rot }, 0);
    items.forEach((it) => {
      const t = Math.max(0.02, it.t - 0.1);          // le mot claque 0,1 s avant d'être dit
      tl.set(it.wd, { opacity: 0 }, 0);
      tl.set(it.wd, { opacity: 1 }, t);
      if (it.plate) {                                 // mot fort : plaque-tampon
        tl.fromTo(it.wd, { scale: 1.75, rotation: -11 }, { scale: 1, rotation: -2.5, duration: 0.36, ease: "back.out(2.2)", immediateRender: false }, t);
        tl.fromTo(it.pl, { scaleX: 0.55 }, { scaleX: 1, duration: 0.12, ease: "power3.out", immediateRender: false }, t);
      } else {                                        // masque qui monte + rebond
        tl.fromTo(it.tx, { yPercent: 140 }, { yPercent: 0, duration: 0.18, ease: "power4.out", immediateRender: false }, t);
        tl.fromTo(it.wd, { scale: 0.5, rotation: 5 }, { scale: 1, rotation: 0, duration: 0.55, ease: "back.out(3.4)", immediateRender: false }, t);
      }
      shake(sh, t + 0.12, Math.max(6, fs / 20));
      sfx(t, it.plate ? "impact" : "pop", it.plate ? 0.3 : 0.32);
    });
    if (o.tOut != null) {
      if (o.out === "up") tl.to(el, { y: -150, opacity: 0, duration: 0.12, ease: "power2.in" }, o.tOut - 0.08);
      else tl.to(el, { scale: 1.12, opacity: 0, duration: 0.06, ease: "power2.in" }, o.tOut - 0.06);
    }
    return { el, sh, fs, items };
  };
  /* la phrase entière, par groupes (o.per mots, défaut 2), deux groupes à la fois (haut / bas) ; jamais un mot x: true */
  const sceneWords = (k, th, o = {}) => {
    const ws = Z.words(k), skip = new Set(o.skip || []), emph = new Set(o.emph || []);
    const groups = Z.chunks(k, o.per || 2).map((g) => g.filter((i) => !skip.has(i))).filter((g) => g.length);
    const ys = o.ys || LAY.words;
    const tEnd = o.tOut != null ? o.tOut : T1(k);
    for (let p = 0; p < groups.length; p += 2) {
      const pair = groups.slice(p, p + 2), next = groups[p + 2];
      const tOut = next ? WT(k, next[0]) - 0.06 : tEnd;
      pair.forEach((g, j) => {
        const big = g.length === 1;
        kl({ words: g.map((i) => [ws[i].w, WT(k, i), emph.has(i)]), x: o.x != null ? o.x : LAY.wordsX, y: ys[j], size: o.size || (big ? LAY.size[0] : LAY.size[1]), th, tOut, out: next ? "up" : null });
      });
    }
  };

  /* ── écran-sticker : un VRAI écran du produit (build/media) ───────────── */
  const sticker = (o) => {
    const p = Z.panel({ ...o, layer: o.layer || panelL, cls: "stk" });
    const lis = o.lis || 14, off = o.off || 18;
    css(p.fr, { boxShadow: `0 0 0 ${lis}px #fff, ${off}px ${off}px 0 ${lis}px ${o.sh || NAVY}` });
    return p;
  };
  const enter = (s, t, kind = "rise", d = 0.62) => {
    const Fr = { rise: { y: 520, rotation: 9, scale: 0.7 }, drop: { y: -520, rotation: -9, scale: 0.7 }, zoom: { scale: 0.15, rotation: 14 },
      left: { x: -900, rotation: -14 }, right: { x: 900, rotation: 14 }, flip: { rotationY: 90, scale: 0.9 } }[kind];
    tl.fromTo(s.pop, { ...Fr, opacity: 1 }, { x: 0, y: 0, scale: 1, rotation: 0, rotationY: 0, opacity: 1, duration: d,
      ease: kind === "zoom" ? "elastic.out(1, 0.62)" : kind === "flip" ? "back.out(1.6)" : "back.out(1.55)", immediateRender: false }, t);
    sfx(t, "whooshUp", 0.45); sfx(t + d * 0.45, "card", 0.45);
  };
  const leave = (s, t, kind = "punch", d = 0.2) => {
    const T = { punch: { scale: 1.12, opacity: 0 }, shrink: { scale: 0.2, rotation: -16, opacity: 0 }, up: { y: -1500, rotation: -8 }, down: { y: 1500, rotation: 8 },
      left: { x: -1000, rotation: -12 }, right: { x: 1000, rotation: 12 }, flip: { rotationY: -90, scale: 0.9, opacity: 0 } }[kind];
    tl.to(s.pop, { ...T, duration: d, ease: "power2.in" }, t);
    if (kind !== "punch") sfx(t, "swoosh", 0.35);
  };
  /* cercle de feutre dessiné à la main autour d'une zone de l'écran (r = [x, y, w, h] en px de la source) */
  let feltN = 0;
  const felt = (s, r, t, tOut, col, o = {}) => {
    const [x, y, w, h] = r, S = s.at(t).S;
    const sw = (o.sw || 12) / S, pad = (o.pad || 14) / S;
    const p = document.createElementNS(NS, "path");
    p.setAttribute("d", Z.loopPath(x + w / 2, y + h / 2, w / 2 * 1.06 + pad, h / 2 * 1.1 + pad, ++feltN, o.tilt != null ? o.tilt : -3));
    p.setAttribute("stroke", col); p.setAttribute("stroke-width", sw.toFixed(2));
    s.ink.appendChild(p);
    tl.set(p, { drawSVG: "0%", opacity: 1 }, 0);
    tl.to(p, { drawSVG: "100%", duration: o.d || 0.3, ease: "power1.inOut" }, t);
    if (tOut != null) tl.to(p, { opacity: 0, duration: 0.14 }, tOut);
    sfx(t, "scribble", 0.5);
    return p;
  };
  /* le morceau qui sort (règle d'Eyal), habillé en sticker */
  const piece = (s, r, t, tOut, to, o = {}) => Z.pieceOut(s, r, t, tOut, to, {
    ...o, layer: panelL,
    deco: (fr) => {
      const sh = o.sh || NAVY;
      tl.set(fr, { boxShadow: `0 0 0 0px #fff, 0px 0px 0 0px ${sh}` }, 0);
      tl.fromTo(fr, { boxShadow: `0 0 0 0px #fff, 0px 0px 0 0px ${sh}` }, { boxShadow: `0 0 0 12px #fff, 18px 18px 0 12px ${sh}`, duration: 0.3, ease: "power2.out", immediateRender: false }, t + 0.06);
    },
  });

  /* bulle : une vraie image (classe, enseignante) dans un cercle / blob à liseré blanc — jamais en fond plein écran */
  const bub = (o) => {
    const w = o.w, h = o.h || o.w;
    const el = $("div", "bub", bubL);
    css(el, { width: w + "px", height: h + "px", transformOrigin: `${w / 2}px ${h / 2}px` });
    box(el, o.x, o.y, w, h);
    const pop = $("div", "pop", el);
    const bf = $("div", "bf", pop);
    css(bf, { borderRadius: "50%", boxShadow: `0 0 0 14px #fff, 18px 18px 0 14px ${o.sh || NAVY}` });
    const inner = $("div", "layer", bf);
    const [iw, ih] = Z.mediaSize(o.name), s0 = Math.max(w / iw, h / ih) * (o.zoom || 1.08);
    css(inner, { width: iw + "px", height: ih + "px", right: "auto", bottom: "auto", transformOrigin: "0 0" });
    Z.mediaEl(inner, o.name, o.plan);
    const fx = o.fx != null ? o.fx : iw / 2, fy = o.fy != null ? o.fy : ih / 2;
    const r = rng(o.seed || 17), ph = r() * TAU;
    Z.window(el, o.tIn, o.tOut);
    Z.ambient.push((t) => {
      const z = s0 * (1 + 0.07 * Z.prog(t, o.tIn, o.tOut));
      inner.style.transform = `translate(${(w / 2 - fx * z).toFixed(2)}px,${(h / 2 - fy * z).toFixed(2)}px) scale(${z.toFixed(5)})`;
      if (o.blob) { const q = (i) => (50 + Math.sin(t * 1.9 + ph + i * 1.7) * 6).toFixed(1); bf.style.borderRadius = `${q(0)}% ${100 - q(1)}% ${q(2)}% ${100 - q(3)}% / ${q(4)}% ${q(5)}% ${100 - q(6)}% ${100 - q(7)}%`; }
    });
    tl.set(pop, { opacity: 0 }, 0);
    tl.fromTo(pop, { scale: 0, rotation: -18, opacity: 1 }, { scale: 1, rotation: 0, opacity: 1, duration: 0.7, ease: "elastic.out(1, 0.55)", immediateRender: false }, o.tIn);
    tl.to(pop, { scale: 0, rotation: 20, duration: 0.22, ease: "back.in(2)" }, o.tOut - 0.22);
    sfx(o.tIn, "bubble", 0.6); sfx(o.tIn + 0.1, "pop", 0.4); sfx(o.tOut - 0.22, "swoosh", 0.3);
    return el;
  };

  /* ── le hibou 3D : il entre en rebond, flotte, saute sur les mots forts, sort ── */
  const owl = (pose, x, y, h, tIn, tOut, from = "pop", o = {}) => {
    const pos = $("div", "owl2", owlL);
    const tmp = Z.owlCanvas(pos, pose, tIn, tOut);
    if (tmp.missing) { pos.remove(); return null; }
    const w = h * tmp.w / tmp.h;
    box(pos, x, y, w, h);
    if (tOut != null) tOut = Math.max(tOut, tIn + 0.66);
    if (o.sh) pos.style.setProperty("--osh", o.sh);
    if (o.mirror) css(tmp.cv, { transform: "scaleX(-1)" });
    const inner = tmp.cv;
    css(inner, { transformOrigin: "50% 92%" });
    tl.set(pos, { opacity: 0 }, 0);
    const fx_ = from === "left" ? -w * 1.1 : from === "right" ? w * 1.1 : 0, fy = from === "bottom" ? 700 : 0;
    tl.fromTo(pos, { x: fx_, y: fy + 40, scale: from === "pop" ? 0.15 : 0.85, rotate: from === "pop" ? -20 : from === "left" ? -18 : from === "right" ? 18 : 0, opacity: 1 },
      { x: 0, y: 0, scale: 1, rotate: 0, opacity: 1, duration: 0.62, ease: "back.out(2.1)", immediateRender: false }, tIn);
    (o.hops || []).forEach((th) => {
      tl.to(pos, { y: -70, duration: 0.16, ease: "power2.out" }, th);
      tl.to(pos, { y: 0, duration: 0.42, ease: "bounce.out" }, th + 0.16);
      sfx(th, "bubble", 0.35);
    });
    Z.pow(tIn + 0.3, x, y - h * 0.1, { r0: h * 0.42, r1: h * 0.62, col: o.powCol || WHITE, n: 12, w: 10 });
    sfx(tIn, "whooshUp", 0.5); sfx(tIn + 0.3, "twinkle", 0.45);
    if (tOut) {
      const ex = o.exit || "down";
      tl.to(pos, { y: -70, duration: 0.12, ease: "power2.out" }, tOut);
      if (ex === "down") tl.to(pos, { y: 1100, rotate: 14, duration: 0.3, ease: "power2.in" }, tOut + 0.12);
      else tl.to(pos, { x: ex === "left" ? -1100 : 1100, y: -200, rotate: ex === "left" ? -30 : 30, duration: 0.3, ease: "power2.in" }, tOut + 0.12);
      tl.set(pos, { opacity: 0 }, tOut + 0.44);
      sfx(tOut + 0.05, "swoosh", 0.35);
    }
    const n = rng(Math.round(x + y))() * TAU;
    Z.ambient.push((t) => { inner.style.translate = `0 ${(Math.sin(t * 2.4 + n) * 7).toFixed(2)}px`; inner.style.rotate = `${(Math.sin(t * 1.6 + n) * 2).toFixed(2)}deg`; });
    return pos;
  };

  /* ── chiffre géant sur une étoile (chiffre DIT dans la narration seulement) ── */
  const count = (to, t, x, y, size, tOut, th, o = {}) => {
    starB(x, y, size * 0.85, th.plate === NAVY ? NAVY : C, t - 0.04, tOut != null ? tOut - 0.2 : null, { n: 16, sh: WHITE, layer: typeL });
    const el = $("div", "pnum", typeL);
    css(el, { width: "600px", left: x - 300 + "px", top: y - size * 0.52 + "px", fontSize: size + "px", color: WHITE, textShadow: `.05em .05em 0 ${NAVY}` });
    const sp = $("span", "", el, "1");
    const steps = Math.min(to, 12), d = o.d || 0.45;
    tl.set(sp, { innerHTML: o.fmt ? o.fmt(1) : "1" }, 0);
    for (let i = 1; i <= steps; i++) { const v = Math.round(i * to / steps); tl.set(sp, { innerHTML: o.fmt ? o.fmt(v) : String(v) }, t + (i - 1) * d / steps); sfx(t + (i - 1) * d / steps, "tick", 0.35); }
    tl.fromTo(el, { scale: 0, rotation: -14 }, { scale: 1, rotation: -3, duration: 0.5, ease: "back.out(2.4)", immediateRender: true }, t);
    tl.fromTo(el, { scale: 1.3 }, { scale: 1, duration: 0.5, ease: "elastic.out(1, 0.45)", immediateRender: false }, t + d);
    Z.confetti(t + d, x, y, { n: 60, sp: 1200 });
    sfx(t + d, "impact", 0.55);
    if (tOut != null) tl.to(el, { scale: 0, duration: 0.2, ease: "back.in(2)" }, tOut - 0.2);
  };
  /* tuile : un élément d'une liste DITE (verbatim) */
  const tile = (html, x, y, size, t, tOut, th, o = {}) => {
    const el = $("div", "tile2", typeL, html);
    css(el, { fontSize: size + "px", padding: `${size * 0.22}px ${size * 0.55}px ${size * 0.3}px`, background: o.bg || CREAM, color: o.ink || NAVY,
      boxShadow: `0 0 0 10px #fff, 14px 14px 0 10px ${NAVY}` });
    const w = el.offsetWidth, h = el.offsetHeight, rot = o.rot != null ? o.rot : (rng(Math.round(y))() - 0.5) * 8;
    css(el, { left: x - w / 2 + "px", top: y - h / 2 + "px" });
    tl.fromTo(el, { opacity: 1, scale: 0, rotation: rot * 4, y: 80 }, { scale: 1, rotation: rot, y: 0, opacity: 1, duration: 0.42, ease: "back.out(2.6)", immediateRender: true }, t);
    if (tOut != null) tl.to(el, { scale: 0, rotation: -rot * 3, duration: 0.18, ease: "back.in(2)" }, tOut - 0.18);
    sfx(t, "pop", 0.5, (x - W / 2) / (W / 2));
    return el;
  };
  /* plaque Wizdi = le LOGO (hibou plat + mot Wizdi) : le seul endroit où le hibou plat est permis */
  const wizdiPlate = (x, y, w, t, tOut) => {
    starB(x, y, w * 0.52, C, t - 0.04, tOut != null ? tOut - 0.24 : null, { n: 16 });
    const el = $("div", "abs logoplate", panelL);
    const h = w * 0.34;
    box(el, x, y, w, h);
    css(el, { boxShadow: `0 0 0 12px #fff, 18px 18px 0 12px ${NAVY}` });
    const oi = Z.img(el, "abs", F.flatOwl || "assets/wizdi-owl.png");
    css(oi, { left: "auto", right: w * 0.08 + "px", top: h * 0.14 + "px", height: h * 0.72 + "px", width: "auto" });
    const L = Z.wordmark(el, "wizdi");
    css(L.wrap, { left: w * 0.08 + "px", top: (h - w * 0.6 * L.ratio) / 2 + "px", width: w * 0.6 + "px", fontSize: w * 0.6 * L.ratio + "px" });
    tl.set(el, { opacity: 0 }, 0);
    tl.fromTo(el, { opacity: 1, scale: 2, rotation: -12 }, { scale: 1, rotation: -3, opacity: 1, duration: 0.44, ease: "back.out(2.2)", immediateRender: false }, t);
    if (tOut != null) tl.to(el, { scale: 0, rotation: 16, duration: 0.18, ease: "back.in(2)" }, tOut - 0.24);
    Z.pow(t + 0.1, x, y, { r0: w * 0.55, r1: w * 0.75, col: WHITE, n: 16 });
    sfx(t + 0.04, "impact", 0.55); sfx(t + 0.08, "pillPop", 0.5);
  };

  /* ── logo du module : géant à l'ouverture, puis plaque fixe en haut qui pulse, puis géant au final ── */
  const BUG = LAY.bug, WM = LAY.wm;
  let logo = null, bug = null, LR = 0.3, logoShown = false;
  const ensureLogo = () => {
    if (logo) return logo;
    logo = Z.wordmark(hud, F.logo || F.slug, 6);
    LR = logo.ratio;
    bug = $("div", "abs bug2", hud);
    box(bug, BUG.x, BUG.y, BUG.w + 70, BUG.w * LR + 52);
    css(bug, { boxShadow: `0 0 0 5px ${NAVY}, 10px 10px 0 5px ${NAVY}` });
    hud.insertBefore(bug, logo.wrap);
    tl.set(bug, { opacity: 0, scale: 0.4, rotation: -2 }, 0);
    box(logo.wrap, WM.x, WM.y, WM.w, WM.w * LR);
    css(logo.wrap, { transformOrigin: "50% 50%", fontSize: WM.w * LR + "px" });
    tl.set(logo.wrap, { opacity: 0 }, 0);
    return logo;
  };
  const bugPulse = (t, k = 1.28) => {
    if (!logoShown) return;
    tl.fromTo(bug, { scale: k, rotation: -7 }, { scale: 1, rotation: -2, duration: 0.65, ease: "elastic.out(1.1, 0.42)", immediateRender: false }, t);
    tl.fromTo(logo.wrap, { scale: BUG.w / WM.w * k, rotation: -7 }, { scale: BUG.w / WM.w, rotation: -2, duration: 0.65, ease: "elastic.out(1.1, 0.42)", immediateRender: false }, t);
    sfx(t, "pillPop", 0.35);
  };

  /* ═══ scènes ═══ */
  const SC = F.scenes || {};
  const sb = (sc) => Object.assign({}, sc, sc[FMT] || {});
  const themeOf = (k, i, sc) => TH[sc.theme || ORDER[i % ORDER.length]];

  /* OUVERTURE DE MARQUE : le logo officiel se trace au mot qui le dit (brandAt = indice du mot « WizPlay »),
     le reste de la phrase en géant autour, le hibou salue, puis le logo file dans la plaque du haut. */
  const brand = (k, sc, i) => {
    ensureLogo();
    const t0 = T0(k), t1 = T1(k), bt = sc.brandAt || 0, th = themeOf(k, i, sc);
    if (i === 0) wipe(0, th, "base"); else wipe(t0 + 0.2, th, "iris");
    decos(t0 + 0.15, t1 - 0.1, th, 4, 1);
    const tWM = sc.logoAt != null ? sc.logoAt : Math.max(0.05, WT(k, bt) - 0.1);
    wipe(Math.max(0.2, tWM - 0.12), TH.cream, "iris", { at: [WM.x, WM.y], d: 0.36 });
    raysY = WM.y;
    css(rays, { background: `repeating-conic-gradient(from 0deg, ${rgba(C, 0.18)} 0deg 7.5deg, transparent 7.5deg 15deg)` });
    tl.to(rays, { opacity: 1, duration: 0.3 }, tWM);
    tl.to(rays, { opacity: 0, duration: 0.25 }, t1 - 0.3);
    tl.set(logo.wrap, { opacity: 1 }, tWM);
    if (logo.paths.length) {
      tl.set(logo.paths, { fillOpacity: 0 }, 0);
      tl.set(logo.strokes, { drawSVG: "0%", opacity: 1 }, 0);
      tl.to(logo.strokes, { drawSVG: "100%", duration: 0.4, ease: "power2.inOut", stagger: 0.06 }, tWM);
      tl.to(logo.paths, { fillOpacity: 1, duration: 0.2, ease: "power2.out" }, tWM + 0.3);
      tl.to(logo.strokes, { opacity: 0, duration: 0.2 }, tWM + 0.45);
    }
    tl.fromTo(logo.wrap, { scale: 0.55, rotation: -6 }, { scale: 1, rotation: -2, duration: 0.85, ease: "elastic.out(1, 0.5)", immediateRender: false }, tWM);
    tl.set(logo.wrap, { filter: `drop-shadow(10px 10px 0 ${NAVY})` }, tWM);
    tl.set(logo.wrap, { filter: "none" }, t1 - 0.45);
    Z.pow(tWM + 0.32, WM.x, WM.y, { r0: WM.w * 0.55, r1: WM.w * 0.68, col: C, n: 18, w: 14 });
    Z.confetti(tWM + 0.35, WM.x, WM.y, { n: 70, sp: 1300 });
    sfx(tWM + 0.3, "impact", 0.7); sfx(tWM + 0.34, "shimmer", 0.55);
    logoShown = true;
    /* le reste de la phrase, géant, autour du logo (verbatim, sans les mots x: true) */
    const ws = Z.words(k), rest = Z.shown(k).filter((j) => j !== bt);
    const emph = new Set(sc.emph || []);
    const before = rest.filter((j) => j < bt), after = rest.filter((j) => j > bt);
    const BB = LAY.brandBefore, BA = LAY.brandAfter;
    if (before.length) kl({ words: before.map((j) => [ws[j].w, WT(k, j), emph.has(j)]), x: WM.x, y: BB.y, size: BB.size, th: TH.cream, tOut: t1 - 0.4 });
    if (after.length) {
      const rows = after.length > 3 ? [after.slice(0, Math.ceil(after.length / 2)), after.slice(Math.ceil(after.length / 2))] : [after];
      rows.forEach((r, j) => kl({ words: r.map((q) => [ws[q].w, WT(k, q), emph.has(q)]), x: WM.x, y: BA.y + j * BA.dy, size: BA.size, th: TH.cream, tOut: t1 - 0.05, maxW: Math.min(W - 100, LAY.maxW + 40) }));
    }
    if (sc.wizdi) wizdiPlate(LAY.wizdi.x, LAY.wizdi.y, LAY.wizdi.w, WT(k, sc.wizdi.at) - 0.1, t1 - 0.3);
    if (sc.owl !== false) {
      const ow = Object.assign({ pose: "wave" }, LAY.brandOwl, sc.owl || {});
      const tOw = Math.max(0.1, sc.owlAt != null ? sc.owlAt : (ws.length > bt + 1 ? WT(k, bt + 1) - 0.2 : tWM + 0.45));
      owl(ow.pose, ow.x, ow.y, ow.h, tOw, Math.min(Math.max(t1 - 0.5, tOw + 1.2), t1 + 0.2), "right", { hops: [tOw + 0.6], exit: "right" });
    }
    /* le logo file dans la plaque fixe du haut */
    tl.to(logo.wrap, { x: BUG.x - WM.x, y: BUG.y - WM.y, scale: BUG.w / WM.w, duration: 0.42, ease: "power3.inOut" }, t1 - 0.34);
    tl.to(bug, { opacity: 1, scale: 1, duration: 0.5, ease: "back.out(2.4)" }, t1 - 0.1);
    sfx(t1 - 0.6, "riser", 0.6);
  };

  /* CARTE DE FIN : volets en cascade, logo géant, slogan (verbatim) en pastille mot à mot, hibou joyeux, confettis,
     signature Wizdi (logo), wizdi.school, Copyright © 2026 Wizdi. All rights reserved */
  const end = (k, sc) => {
    ensureLogo();
    const t0 = T0(k), E = LAY.end;
    [[TH.mod, 0], [TH.sky, 0.06], [TH.navy, 0.12], [TH.cream, 0.19]].forEach(([tt, dt]) => wipe(t0 + 0.1 + dt, tt, "iris", { at: [E.logo.x, E.logo.y + H * 0.15], d: 0.5, ease: "power3.out", quiet: true }));
    sfx(t0 - 0.2, "riser", 0.8);
    raysY = E.logo.y;
    css(rays, { background: `repeating-conic-gradient(from 0deg, ${rgba(C, 0.2)} 0deg 7.5deg, transparent 7.5deg 15deg)` });
    tl.to(rays, { opacity: 1, duration: 0.4 }, t0 + 0.3);
    tl.to(bug, { opacity: 0, scale: 0.4, duration: 0.2, ease: "back.in(2)" }, t0);
    const END = E.logo;
    if (!logoShown) {   // pas d'ouverture de marque : le logo se trace ici
      tl.set(logo.wrap, { x: END.x - WM.x, y: END.y - WM.y, scale: END.w / WM.w, rotation: -2 }, 0);
      tl.set(logo.wrap, { opacity: 1 }, t0 + 0.3);
      Z.drawLogo(logo, t0 + 0.3, 0.45);
      logoShown = true;
    } else tl.to(logo.wrap, { x: END.x - WM.x, y: END.y - WM.y, scale: END.w / WM.w, rotation: -2, duration: 0.46, ease: "power3.inOut" }, t0 - 0.1);
    tl.set(logo.wrap, { filter: `drop-shadow(12px 12px 0 ${NAVY})` }, t0 + 0.1);
    tl.fromTo(logo.wrap, { scale: END.w / WM.w * 1.22 }, { scale: END.w / WM.w, duration: 0.8, ease: "elastic.out(1.1, 0.4)", immediateRender: false }, t0 + 0.36);
    if (logo.paths.length) tl.to(logo.paths, { y: -30, duration: 0.18, ease: "sine.out", stagger: 0.06, yoyo: true, repeat: 1 }, t0 + 0.9);
    Z.pow(t0 + 0.38, END.x, END.y, { r0: END.w * 0.58, r1: END.w * 0.78, col: WHITE, n: 22, w: 16 });
    Z.confetti(t0 + 0.4, 60, H - 20, { n: 110, sp: H * 1.2, ang: -62, spread: 34, life: 2.6 });
    Z.confetti(t0 + 0.4, W - 60, H - 20, { n: 110, sp: H * 1.2, ang: -118, spread: 34, life: 2.6 });
    sfx(t0 + 0.36, "impact", 0.7); sfx(t0 + 0.38, "finalChord", 0.7);
    decos(t0 + 0.6, DUR + 1, TH.cream, 6, 3);
    /* la pastille du slogan, mot à mot en géant (verbatim) */
    const SL = E.slog;
    const slog = $("div", "slog", typeL);
    box(slog, SL.x, SL.y, SL.w, SL.h);
    css(slog, { background: C, boxShadow: `0 0 0 14px #fff, 22px 22px 0 14px ${NAVY}` });
    const ws = Z.words(k), idx = Z.shown(k), emph = new Set(sc.emph || []), half = Math.ceil(idx.length / 2);
    tl.set(slog, { scale: 0, rotation: 10 }, 0);
    tl.to(slog, { scale: 1, rotation: -2, duration: 0.6, ease: "elastic.out(1, 0.55)" }, WT(k, idx[0] || 0) - 0.25);
    sfx(WT(k, idx[0] || 0) - 0.25, "pillPop", 0.7);
    const thS = { ...TH.mod, plate: NAVY, pInk: C };
    const rows = idx.length > 2 ? [idx.slice(0, half), idx.slice(half)] : [idx];
    rows.forEach((r, j) => {
      const dy = rows.length === 1 ? 0 : (j ? 1 : -1) * SL.h * 0.25;
      const l = kl({ words: r.map((q) => [ws[q].w, WT(k, q), emph.has(q)]), x: SL.x, y: SL.y + dy, size: SL.size, th: thS, maxW: SL.w - 80, rot: -2 });
      css(l.el, { zIndex: 2 });
    });
    const tLast = WT(k, idx[idx.length - 1] || 0);
    Z.confetti(tLast + 0.2, SL.x, SL.y, { n: 90, sp: 1600 });
    if (sc.owl !== false) {
      const ow = Object.assign({ pose: "joy" }, E.owl, sc.owl || {});
      owl(ow.pose, ow.x, ow.y, ow.h, WT(k, idx[0] || 0) + 0.3, null, "bottom", { hops: [tLast + 0.05, tLast + 0.9] });
    }
    /* signature Wizdi + wizdi.school + copyright exact */
    const tSig = Math.min(WE(k, idx[idx.length - 1] || 0) + 0.25, DUR - 0.6);
    const sig = $("div", "abs", hud);
    css(sig, { left: SL.x - E.sig.w / 2 + "px", top: E.sig.y - E.sig.h / 2 + "px", width: E.sig.w + "px", height: E.sig.h + "px" });
    const so = Z.img(sig, "abs", F.flatOwl || "assets/wizdi-owl.png");
    css(so, { left: "auto", right: "0", top: "0", height: E.sig.h * 0.98 + "px", width: "auto" });
    const sw = Z.wordmark(sig, "wizdi");
    css(sw.wrap, { left: "0", top: E.sig.h * 0.16 + "px", width: E.sig.w * 0.68 + "px", fontSize: E.sig.w * 0.68 * sw.ratio + "px" });
    const url = $("div", "sig2 url2", hud, "wizdi.school");
    css(url, { width: W + "px", top: E.url.y - E.url.size / 2 + "px", fontSize: E.url.size + "px", color: NAVY });
    const copy = $("div", "sig2 copy2", hud, "Copyright © 2026 Wizdi. All rights reserved");
    css(copy, { width: W + "px", top: E.copy.y - E.copy.size / 2 + "px", fontSize: E.copy.size + "px", color: rgba(NAVY, 0.7) });
    tl.set([sig, url, copy], { opacity: 0, y: 30 }, 0);
    tl.to([sig, url, copy], { opacity: 1, y: 0, duration: 0.45, stagger: 0.1, ease: "back.out(2)" }, tSig);
    tl.fromTo(sig, { scale: 0.5 }, { scale: 1, duration: 0.6, ease: "elastic.out(1, 0.5)", immediateRender: false }, tSig);
    sfx(tSig, "twinkle", 0.45);
  };

  /* SCÈNE COURANTE : volet + mots géants + vrais écrans (stickers, feutre, morceau qui sort) + bulle + hibou… */
  const KINDS = ["rise", "zoom", "flip", "right", "left", "drop"];
  const generic = (k, sc, i) => {
    const t0 = T0(k), t1 = T1(k), th = themeOf(k, i, sc);
    const wk = sc.wipe || ["diag", "iris", "diag", "rise", "iris", "split"][i % 6];
    if (i === 0) wipe(0, th, "base");
    else if (sc.band) band(t0 + 0.2, th, sc.band); else wipe(t0 + 0.2, th, wk, wk === "iris" ? { at: [W / 2, H * 0.62] } : {});
    bugPulse(t0 + 0.32);
    decos(t0 + 0.1, t1, th, 4, i + 2);
    if (sc.words !== false) sceneWords(k, th, { emph: sc.emph || [], ys: sc.ys, per: sc.per, size: sc.wordSize, x: sc.wordsX });
    const at = (v, d = 0) => (v == null ? t0 + 0.1 + d : typeof v === "number" ? WT(k, v) + d : t0 + parseFloat(v));
    const until = (v, d = 0) => (v == null ? t1 : typeof v === "number" ? WT(k, v) + d : t0 + parseFloat(v));
    const felts = [C === th.bg ? NAVY : C, th.bg === SKY ? SUN : SKY];
    const M = LAY.media;
    (sc.media || []).forEach((m, j) => {
      if (!Z.MED[m.name]) { console.warn("média absent de build/media (scène " + k + ") :", m.name); return; }
      const [iw, ih] = Z.mediaSize(m.name), portrait = ih > iw;
      const tIn = at(m.at, -0.25), tOut = until(m.until, -0.08);
      const w = m.w || (portrait ? M.wp : M.w), x = m.x || M.x, y = m.y || M.y;
      const s = sticker({ name: m.name, plan: Z.planOf(m, tIn), shots: Z.shotsOf(m, at),
        x, y, w, rot: m.rot != null ? m.rot : (j % 2 ? 2 : -2), t0: tIn, t1: tOut + 0.25, cam: m.cam, sh: th.csh === WHITE ? NAVY : th.csh });
      enter(s, tIn, m.enter || KINDS[(i + j) % KINDS.length], 0.6);
      leave(s, tOut, m.leave || (j % 2 ? "down" : "punch"), 0.2);
      (m.marks || []).forEach((mk, q) => {
        const tm = at(mk.at, -0.05), tmo = mk.until != null ? until(mk.until, -0.1) : tOut - 0.12;
        felt(s, mk.r, tm, tmo, felts[q % 2], { d: 0.26, tilt: q % 2 ? 2 : -3 });
        if (mk.piece) {
          const P = Object.assign({}, LAY.piece[q % LAY.piece.length], mk.piece === true ? {} : mk.piece);
          if (mk.piece === true) P.w = Math.min(P.w, mk.r[2]);   // jamais une découpe agrandie
          piece(s, mk.r, tm + 0.26, tmo, P, { back: mk.back, frame: mk.frame, sh: th.csh === WHITE ? NAVY : th.csh });
        }
      });
    });
    if (sc.portal && Z.MED[sc.portal.name]) {
      const Pp = Object.assign({}, LAY.portal, sc.portal), tIn = at(Pp.at, -0.25);
      bub({ name: Pp.name, plan: Pp.plan || (Z.MED[Pp.name].n > 1 ? Z.play(Pp.name, tIn, Pp.speed || 1, Pp.start || 0) : null),
        x: Pp.x, y: Pp.y, w: Pp.d, h: Pp.h, tIn, tOut: until(Pp.until, -0.05), fx: Pp.fx, fy: Pp.fy, zoom: Pp.zoom, blob: true, seed: i + 3,
        sh: th.csh === WHITE ? NAVY : th.csh });
    }
    if (sc.count) { const c = Object.assign({}, LAY.count, sc.count); count(c.to, at(c.at, -0.05), c.x, c.y, c.size, until(c.until), th, c); }
    (sc.chips || []).forEach((c, q) => { const L = LAY.chips; tile(c.html, c.x || L.x, c.y || (L.y + q * L.dy), c.size || L.size, at(c.at, -0.08), until(c.until), th, c); });
    if (sc.wizdi) wizdiPlate(LAY.wizdi.x, LAY.wizdi.y, LAY.wizdi.w, at(sc.wizdi.at, -0.1), until(sc.wizdi.until));
    if (sc.owl) {
      const o = Object.assign({}, LAY.owl, sc.owl);
      owl(o.pose || "point", o.x, o.y, o.h, at(o.at, -0.2), o.until === "keep" ? null : until(o.until, -0.5), o.from || "pop",
        { hops: o.hops ? o.hops.map((v) => at(v)) : [], exit: o.exit, powCol: C, mirror: o.mirror });
    }
    (sc.burst || []).forEach((b) => { const t = at(b, 0); Z.confetti(t, W / 2, H * 0.47, { n: 70, sp: 1300 }); Z.pow(t, W / 2, H * 0.47, { r0: 420, r1: 560, col: WHITE, n: 18 }); sfx(t, "shimmer", 0.5); });
    if (sc.extra) sc.extra({ Z, POP, k, t0, t1, at, until, th, LAY });
  };

  /* construit le film depuis F.scenes ; la grille de tempo (BEAT) va de la 2e phrase au final (nombre entier de mesures) */
  const build = () => {
    if (!KEYS.length) { console.warn("aucun mot (words.js) : rien à construire"); return; }
    const tDive = KEYS.length > 1 ? LS(KEYS[1]) - 0.02 : 0.5, tFinal = T0(KEYS[KEYS.length - 1]) + 0.4;
    const bpm = F.bpm || 116, span = tFinal - tDive, barLen = 240 / bpm;
    /* nombre ENTIER de mesures entre la 2e phrase et le final : les deux grands impacts tombent sur un premier temps */
    BEAT = span >= barLen * 0.6 ? span / (Math.max(1, Math.round(span / barLen)) * 4) : 60 / bpm;
    BT0 = tDive;
    KEYS.forEach((k, i) => {
      const sc = sb(SC[k] || {});
      const kind = sc.kind || (i === KEYS.length - 1 && KEYS.length > 1 ? "end" : "generic");
      if (kind === "brand") brand(k, sc, i);
      else if (kind === "end") end(k, sc);
      else generic(k, sc, i);
    });
    Z.timelineExtra = Object.assign({ marks: { dive: tDive, final: tFinal }, style: "pop", bpm: 60 / BEAT }, Z.timelineExtra || {});
  };

  const POP = window.POP = {
    TH, LAY, LAYOUTS, C, NAVY, CREAM, SKY, SUN, WHITE, layers: { bgL, raysL, stickL, bubL, panelL, owlL, typeL, hud },
    wipe, band, deco, decos, starB, shake, kl, sceneWords, sticker, enter, leave, felt, piece, bub, owl, count, tile, wizdiPlate,
    ensureLogo, bugPulse, brand, end, generic, build, rays: () => rays, setRaysY: (y) => { raysY = y; },
    setBeat: (beat, t0) => { BEAT = beat; BT0 = t0; },
  };
})();
