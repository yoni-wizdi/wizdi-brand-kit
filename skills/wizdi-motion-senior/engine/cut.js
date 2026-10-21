/* ──────────────────────────────────────────────────────────────────────────
   OPTIONNEL — film construit sur un MONTAGE FILMÉ (une actrice, un présentateur, un tutoriel d'écran avec voix).
   Se charge APRÈS words.js et film.js, AVANT core.js. Sans window.WIZ_CUT, ne fait rien.

   Entrée : window.WIZ_CUT = { dur, fps: 30, w: 1080, h: 1920,
                               shots: [{ id, key, t0, t1, see?, say?, novideo: [[a, b], …] }] }   (secondes du MONTAGE PROPRE)
            window.WIZ_WORDS : instants des mots en secondes du montage propre (x: true = mot douteux, interdit à l'écran)
            WIZ_FILM.keep = [[a, b], …] : les intervalles GARDÉS du montage (resserrer : silences, respirations).
   Tout suit automatiquement : l'image (footage.js), les mots et leurs instants (remappés ici), la voix (tools/mix.py lit
   les mêmes intervalles dans out/timeline.json). On ne peut que RETIRER du temps. Retirer une réplique : NON.

   Sortie : window.KIT = { keep, seg, footDur, toCut(t film) -> t montage, toFilm(t montage), shots (temps du FILM),
            novideo (trous noirs à couvrir), fps, frames } ; WIZ_FILM.voAt = 0 (la voix est dans le montage), endHold 2,0 s.
   ────────────────────────────────────────────────────────────────────────── */
(() => {
  "use strict";
  const F = window.WIZ_FILM = window.WIZ_FILM || {}, CUT = window.WIZ_CUT, WD = window.WIZ_WORDS || {};
  if (!CUT) return;
  const EPS = 1e-6;
  const keep = (F.keep && F.keep.length ? F.keep : [[0, CUT.dur]])
    .map(([a, b]) => [Math.max(0, +a), Math.min(CUT.dur, +b)]).filter(([a, b]) => b > a + 0.02);
  for (let i = 1; i < keep.length; i++) if (keep[i][0] < keep[i - 1][1] - EPS) throw new Error("keep : intervalles qui se chevauchent ou dans le désordre");
  let acc = 0;
  const seg = keep.map(([a, b]) => { const s = { a, b, f: acc }; acc += b - a; return s; });
  const footDur = acc;
  const segOf = (tc) => seg.find((s) => tc >= s.a - EPS && tc <= s.b + EPS);
  const toFilm = (tc) => { const s = segOf(tc); return s ? s.f + (tc - s.a) : null; };
  const toCut = (t) => {
    if (t <= 0) return seg[0].a;
    for (const s of seg) if (t < s.f + (s.b - s.a)) return s.a + (t - s.f);
    return seg[seg.length - 1].b - 1 / 60;            // après la fin (carte de fin) : dernière image
  };
  /* mots : gardés si leur milieu est dans un intervalle gardé ; instants ramenés dans ce même intervalle */
  const lines = {}, words = {};
  for (const k of Object.keys(WD)) {
    const ws = [];
    for (const w of WD[k]) {
      const s = segOf((w.t + w.e) / 2);
      if (!s) continue;
      ws.push({ ...w, t: s.f + (Math.max(w.t, s.a) - s.a), e: s.f + (Math.min(w.e, s.b) - s.a), tc: w.t });
    }
    if (!ws.length) continue;
    words[k] = ws;
    lines[k] = { t: ws[0].t, e: ws[ws.length - 1].e };
  }
  window.WIZ_WORDS = words;
  window.WIZ_VO = { dur: footDur, lines };
  const mapRange = (a, b) => {
    const out = [];
    for (const s of seg) { const x = Math.max(a, s.a), y = Math.min(b, s.b); if (y > x + EPS) out.push([s.f + x - s.a, s.f + y - s.a]); }
    return out;
  };
  const shots = (CUT.shots || []).map((s) => {
    const r = mapRange(s.t0, s.t1);
    return r.length ? { id: s.id, key: s.key, t0: r[0][0], t1: r[r.length - 1][1], see: s.see, say: s.say,
      novideo: (s.novideo || []).flatMap(([a, b]) => mapRange(a, b)) } : null;
  }).filter(Boolean);
  F.voAt = F.voAt != null ? F.voAt : 0;
  F.endHold = F.endHold != null ? F.endHold : 2.0;
  const fps = CUT.fps || 30;
  window.KIT = { keep, seg, footDur, toCut, toFilm, shots, novideo: shots.flatMap((s) => s.novideo), fps,
    frames: CUT.frames || Math.round(CUT.dur * fps), w: CUT.w || 1080, h: CUT.h || 1920 };
})();
