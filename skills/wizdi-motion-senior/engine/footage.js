/* ──────────────────────────────────────────────────────────────────────────
   OPTIONNEL — une PERSONNE FILMÉE (ou toute vidéo tournée) comme calque. Se charge APRÈS core.js (et cut.js si montage).
   Images : WIZ_FILM.footage.dir (défaut build/footage/) 0001.jpg … (tools/media.py footage <clip>) ;
   détourage facultatif : WIZ_FILM.footage.matte (défaut build/matte/) 0001.png … (alpha = la personne ; à la taille
   footage.matteScale de l'image, défaut 0.5 ; à produire avec un outil de matting de ton choix, non fourni).
   La personne reste le cœur de l'image : ne jamais cacher son visage pendant qu'elle parle.

   FOOT.layer(o) -> { el, cv }  ·  o = {
     parent,                       // calque parent (défaut : WZ.stage)
     t0, t1,                       // fenêtre de visibilité (temps du film), exacte à l'image près
     w, h,                         // taille du canvas (défaut : le format du film, plein cadre)
     cam: [[t, zoom, fx, fy, ease?]…],   // recadrage DANS l'image source : zoom 1 = image entière, fx/fy = centre en px source
     pose: [[t, x, y, s, rot, ease?]…],  // position du canvas dans la scène (centre, échelle, rotation en degrés)
     cutout: true,                 // détouré (fond transparent) : sur un aplat, avec un liseré…
     hold: 12.4,                   // image figée à cet instant du film
     timeMap: (t) => t,            // temps de lecture personnalisé (ralenti…)
     cls,                          // classe CSS du conteneur
   }
   FOOT.frameAt(t) : image à l'instant t du film ; FOOT.noVideo(t) : vrai si voix sans image (noir à COUVRIR).
   ────────────────────────────────────────────────────────────────────────── */
(() => {
  "use strict";
  const Z = window.WZ, F = Z.F, K = window.KIT || null, FO = F.footage || {};
  const { clamp, kfEval, css, $ } = Z;
  const SW = FO.w || (K && K.w) || 1080, SH = FO.h || (K && K.h) || 1920;
  const FPS = FO.fps || (K && K.fps) || 30;
  const NF = FO.n || (K && K.frames) || Math.round(Z.DUR * FPS);
  const MS = FO.matteScale || 0.5;
  const SF = Z.frames("footage", FO.dir || "build/footage/", "jpg", 4, NF, ".");
  const SM = Z.frames("matte", FO.matte || "build/matte/", "png", 4, NF, ".");
  SF.dir = SF.base.replace(/\/$/, ""); SF.base = ""; SM.dir = SM.base.replace(/\/$/, ""); SM.base = "";
  const toCut = K ? K.toCut : (t) => t;
  const frameAt = (t) => clamp(Math.round(toCut(clamp(t, 0, Z.DUR)) * FPS), 0, NF - 1);
  const noVideo = (t) => !!K && K.novideo.some(([a, b]) => t >= a && t < b);

  const layer = (o = {}) => {
    const w = o.w || Z.W, h = o.h || Z.H;
    const t0 = o.t0 == null ? 0 : o.t0, t1 = o.t1 == null ? Z.DUR : o.t1;
    const el = $("div", "act " + (o.cls || ""), o.parent || Z.stage);
    css(el, { position: "absolute", left: 0, top: 0, width: w + "px", height: h + "px", transformOrigin: `${w / 2}px ${h / 2}px`, display: "none" });
    const cv = $("canvas", "", el);
    cv.width = w; cv.height = h;
    css(cv, { width: "100%", height: "100%", display: "block" });
    const g = cv.getContext("2d");
    const cam = o.cam || [[0, 1, SW / 2, SH / 2]];
    const pose = o.pose || [[0, w / 2, h / 2, 1, 0]];
    /* rectangle source au ratio du canvas, zoom >= 1 */
    const srcRect = (t) => {
      const [z, fx, fy] = kfEval(cam, t, 3);
      let sw = SW / Math.max(1, z), sh = sw * h / w;
      if (sh > SH) { sh = SH / Math.max(1, z); sw = sh * w / h; }
      return [clamp(fx - sw / 2, 0, SW - sw), clamp(fy - sh / 2, 0, SH - sh), sw, sh];
    };
    for (let f = 0; f < 3; f++) Z.loads.push(Z.getFrame(SF, frameAt(t0) + f < NF ? frameAt(t0) + f : 0).p);
    let lastKey = "";
    Z.ambient.push((t) => {
      const on = t >= t0 - 1e-4 && (t < t1 - 1e-4 || t1 >= Z.DUR);
      el.style.display = on ? "block" : "none";
      if (!on) return;
      const [x, y, s, r] = kfEval(pose, t, 4);
      el.style.transform = `translate(${(x - w / 2).toFixed(2)}px,${(y - h / 2).toFixed(2)}px) rotate(${r.toFixed(3)}deg) scale(${s.toFixed(4)})`;
    });
    Z.media.push((t) => {
      if (t < t0 - 1e-4 || (t >= t1 - 1e-4 && t1 < Z.DUR)) return null;
      const f = o.hold != null ? frameAt(o.hold) : frameAt(o.timeMap ? o.timeMap(t) : t);
      const R = srcRect(t), key = f + ":" + R.map((v) => v.toFixed(1)).join(",");
      if (key === lastKey) return null;
      const e = Z.getFrame(SF, f), m = o.cutout ? Z.getFrame(SM, f) : null;
      const draw = () => {
        if (!e.im.naturalWidth) return;
        g.globalCompositeOperation = "source-over";
        g.clearRect(0, 0, w, h);
        g.drawImage(e.im, R[0], R[1], R[2], R[3], 0, 0, w, h);
        if (m && m.im.naturalWidth) {
          g.globalCompositeOperation = "destination-in";
          g.drawImage(m.im, R[0] * MS, R[1] * MS, R[2] * MS, R[3] * MS, 0, 0, w, h);
          g.globalCompositeOperation = "source-over";
        }
        lastKey = key;
      };
      if (e.im.complete && (!m || m.im.complete)) { draw(); return null; }
      return Promise.all([e.p, m ? m.p : null]).then(draw);
    });
    return { el, cv };
  };
  window.FOOT = window.ACT = { layer, frameAt, noVideo, NF, footDur: K ? K.footDur : Z.DUR };
})();
