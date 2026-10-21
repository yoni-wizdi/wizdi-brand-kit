# -*- coding: utf-8 -*-
"""Musique + bruitages SYNTHÉTISÉS (numpy / scipy) pour le style pop — libres de droits, aucun son téléchargé
(règle Wizdi : « musique et bruitages synthétisés, sans banque de sons »). Repris de la bande-son des films Wiz du 13/10.

Lit out/timeline-<fmt>.json (render.py timeline) : durée, repères sonores posés par la page (WZ.sfx), grille musicale
(marks.dive -> marks.final, bpm). La grille tombe pile entre la 2e phrase (`dive`) et le final : un nombre ENTIER de
mesures, les deux grands impacts sur un premier temps ; les coupes et volets de la page sont sur cette même grille.

  python tools/synth.py --timeline out/timeline-9x16.json [--key 0] [--out-dir build]   # -> build/stem-music.wav, build/stem-sfx.wav
Utilisé directement par tools/mix.py quand mix.json dit "music": "synth" / "sfx": "synth".

Musique pop : I–vi–IV–V, batterie complète (grosse caisse, claps 2 et 4, charleston, shaker), basse en croches, arpège
en écho, nappe d'ouverture, accord final + cloches. Tonalité par module (--key en demi-tons, défaut selon le slug)."""
import argparse, json, os, sys

import numpy as np
from scipy import signal
from scipy.io import wavfile

SR = 48000
KEYS = {"wizplay": 0, "wizbook": -2, "wizspace": 3, "wizbox": -3, "wizchat": 1, "wizplan": 2, "wizgen": -1, "wizmap": 4}


class Synth:
    def __init__(self, tl, key=None, seed=11):
        self.TL = tl
        self.DUR = float(tl["dur"])
        self.N = int(round(self.DUR * SR))
        self.rng = np.random.default_rng(seed)
        m = tl.get("marks") or {}
        bpm = float(tl.get("bpm") or 116)
        if not 60 <= bpm <= 190:
            bpm = 116
        self.T0 = float(m.get("dive", 0.5))
        self.TF = float(m.get("final", self.DUR - 1.5))
        bar0 = 240 / bpm
        span = self.TF - self.T0
        if span >= bar0 * 0.6:      # même règle que pop.js : nombre entier de mesures (au moins une)
            self.NBARS = max(1, round(span / bar0)); self.BAR = span / self.NBARS
        else:
            self.BAR = bar0; self.NBARS = 0
        self.BEAT = self.BAR / 4
        slug = (tl.get("slug") or "").lower()
        self.KEY = key if key is not None else KEYS.get(slug, 0)
        K = self.KEY
        self.CHORDS = [(r + K, [n + K for n in ns]) for r, ns in
                       [(38, [62, 66, 69, 74]), (47, [62, 66, 71, 74]), (43, [62, 67, 71, 74]), (45, [61, 64, 69, 73])]]  # I vi IV V
        self.IR = self.make_ir()

    # ── outils ──
    def t2i(self, t): return int(round(t * SR))
    def bus(self): return np.zeros((2, self.N))

    def place(self, buf, x, t, gain=1.0, pan=0.0):
        i = self.t2i(t)
        if i >= self.N:
            return
        if x.ndim == 1:
            l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
            x = np.vstack([x * l * 1.414, x * r * 1.414])
        if i < 0:
            x, i = x[:, -i:], 0
        n = min(x.shape[1], self.N - i)
        if n > 0:
            buf[:, i:i + n] += gain * x[:, :n]

    @staticmethod
    def env_ad(n, a, d):
        t = np.arange(n) / SR
        return np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / max(d, 1e-4))

    @staticmethod
    def lp(x, fc, order=2):
        b, a = signal.butter(order, min(fc / (SR / 2), 0.99), "low"); return signal.lfilter(b, a, x, axis=-1)

    @staticmethod
    def hp(x, fc, order=2):
        b, a = signal.butter(order, min(fc / (SR / 2), 0.99), "high"); return signal.lfilter(b, a, x, axis=-1)

    @staticmethod
    def bp(x, f1, f2, order=2):
        b, a = signal.butter(order, [f1 / (SR / 2), min(f2 / (SR / 2), 0.99)], "band"); return signal.lfilter(b, a, x, axis=-1)

    @staticmethod
    def note(m): return 440.0 * 2 ** ((m - 69) / 12)

    @staticmethod
    def saw(f, n, phase=0.0):
        t = np.arange(n) / SR; return 2 * ((t * f + phase) % 1.0) - 1

    def tri(self, f, n): return 2 * np.abs(self.saw(f, n)) - 1

    @staticmethod
    def sine(f, n): return np.sin(2 * np.pi * f * np.arange(n) / SR)

    def make_ir(self, sec=2.4, decay=0.6, seed=3):
        r = np.random.default_rng(seed); n = int(sec * SR); t = np.arange(n) / SR
        ir = self.lp(r.standard_normal((2, n)) * np.exp(-t / decay), 7500)
        ir[:, : int(0.015 * SR)] *= np.linspace(0, 1, int(0.015 * SR))
        return ir / np.sqrt((ir ** 2).sum(axis=1, keepdims=True))

    def reverb(self, x, mix=0.25):
        wet = np.vstack([signal.fftconvolve(x[0], self.IR[0])[:self.N], signal.fftconvolve(x[1], self.IR[1])[:self.N]])
        return x * (1 - mix * 0.5) + wet * mix

    def bar_t(self, b): return self.T0 + b * self.BAR

    # ── musique ──
    def pad_layer(self):
        out, K, saw, note = self.bus(), self.KEY, self.saw, self.note
        n0 = max(self.t2i(self.T0) + int(0.3 * SR), int(0.4 * SR))   # nappe d'ouverture, sombre, qui monte vers la plongée
        x = np.zeros(n0)
        for m in [50 + K, 57 + K, 62 + K, 66 + K]:
            for det in (-0.1, 0.0, 0.1):
                x += saw(note(m) * 2 ** (det / 12), n0, self.rng.random())
        t = np.arange(n0) / SR
        x = self.lp(x / 12, 700) * np.clip(t / 1.0, 0, 1) * (0.6 + 0.4 * t / (n0 / SR))
        self.place(out, np.vstack([x, np.roll(x, 500)]), 0, 0.55)
        for b in range(self.NBARS):
            _, ns = self.CHORDS[b % 4]
            n = int(self.BAR * SR) + int(1.0 * SR)
            x = np.zeros(n)
            for m in ns:
                for det in (-0.08, 0.0, 0.08):
                    x += saw(note(m) * 2 ** (det / 12), n, self.rng.random())
            x = self.lp(x / 12, 1400 if b >= 2 else 900)
            k = np.arange(n)
            e = np.minimum(1, k / (0.35 * SR)) * np.where(k > self.BAR * SR, np.exp(-(k - self.BAR * SR) / (0.3 * SR)), 1)
            self.place(out, np.vstack([x * e, np.roll(x * e, int(0.012 * SR))]), self.bar_t(b), 0.5)
        return out

    def pluck(self, f, dur=0.3, bright=4000):
        n = int((dur + 0.05) * SR)
        return self.lp(0.6 * self.tri(f, n) + 0.4 * self.sine(2 * f, n), bright) * self.env_ad(n, 0.003, dur * 0.4)

    def arp_layer(self):
        out, pat = self.bus(), [0, 2, 1, 3, 2, 1, 3, 2]
        for b in range(self.NBARS):
            _, ns = self.CHORDS[b % 4]
            ns = [m + 12 for m in ns]
            step = self.BEAT / 2 if b < 2 else self.BEAT / 4
            for k in range(int(round(self.BAR / step))):
                t = self.bar_t(b) + k * step
                if b == self.NBARS - 1 and t > self.TF - self.BEAT:   # silence avant le logo final
                    break
                self.place(out, self.pluck(self.note(ns[pat[k % 8]])), t, 0.13 * (0.9 if k % 4 == 0 else 0.6), pan=0.4 * np.sin(k * 0.8))
        d = max(1, int(self.BEAT * 0.75 * SR))
        echo = np.zeros_like(out)
        if d < self.N:
            echo[0, d:] += out[1, :-d] * 0.33
        if 2 * d < self.N:
            echo[1, 2 * d:] += out[0, :-2 * d] * 0.22
        return out + self.lp(echo, 3200)

    def kick(self):
        n = int(0.42 * SR); t = np.arange(n) / SR
        f = 46 + 90 * np.exp(-t / 0.032)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.15)
        x[: int(0.002 * SR)] += self.rng.standard_normal(int(0.002 * SR)) * 0.35
        return x

    def clap(self):
        n = int(0.3 * SR); t = np.arange(n) / SR
        e = sum(np.where(t >= o, np.exp(-(t - o) / 0.011), 0) * 0.5 for o in (0, 0.01, 0.021))
        e = e + np.where(t >= 0.03, np.exp(-(t - 0.03) / 0.08), 0)
        return self.bp(self.rng.standard_normal(n), 900, 5200) * e * 0.55 + self.sine(200, n) * np.exp(-t / 0.05) * 0.2

    def hat(self, open_=False):
        n = int((0.2 if open_ else 0.05) * SR); t = np.arange(n) / SR
        return self.hp(self.rng.standard_normal(n), 7600) * np.exp(-t / (0.06 if open_ else 0.016))

    def shaker(self):
        n = int(0.07 * SR); t = np.arange(n) / SR
        return self.bp(self.rng.standard_normal(n), 5000, 11000) * np.minimum(1, t / 0.012) * np.exp(-t / 0.025)

    def drums_bass(self):
        dr, bs, duck = self.bus(), self.bus(), np.ones(self.N)
        K_, C_, Hc, Ho, Sh = self.kick(), self.clap(), self.hat(), self.hat(True), self.shaker()
        for b in range(self.NBARS):
            root, _ = self.CHORDS[b % 4]
            for beat in range(4):
                t = self.bar_t(b) + beat * self.BEAT
                if b == self.NBARS - 1 and beat == 3:   # le temps suspendu avant le logo
                    continue
                full = b >= 1
                if beat in (0, 2) or full:
                    self.place(dr, K_, t, 0.85 if full else 0.6)
                    i = self.t2i(t); n = max(0, min(int(0.26 * SR), self.N - i))
                    duck[i:i + n] = np.minimum(duck[i:i + n], 1 - 0.5 * np.exp(-np.arange(n) / (0.08 * SR)))
                if full and beat in (1, 3):
                    self.place(dr, C_, t, 0.45, pan=0.05)
                if full:
                    self.place(dr, Ho if beat == 3 else Hc, t + self.BEAT / 2, 0.14, pan=0.3)
                    for s16 in range(4):
                        self.place(dr, Sh, t + s16 * self.BEAT / 4, 0.05 + (0.03 if s16 % 2 else 0), pan=-0.35)
                for e8 in range(2):
                    if not full and e8 == 1:
                        continue
                    f = self.note(root + (12 if (e8 == 1 and beat == 3) else 0))
                    n8 = int(self.BEAT / 2 * SR)
                    x = (0.7 * self.sine(f, n8) + 0.3 * self.lp(self.saw(f, n8), 650)) * self.env_ad(n8, 0.004, 0.15)
                    self.place(bs, x, t + e8 * self.BEAT / 2, 0.4)
        return dr, bs, duck

    def bell(self, m, dur=1.2):
        n = int(dur * SR); t = np.arange(n) / SR; f = self.note(m)
        x = np.sin(2 * np.pi * f * t + 1.6 * np.sin(2 * np.pi * f * 3.5 * t) * np.exp(-t / 0.14))
        return x * self.env_ad(n, 0.002, dur * 0.3)

    def final_music(self):
        out, K = self.bus(), self.KEY
        _, ns = self.CHORDS[0]
        n = max(int((self.DUR - self.TF + 0.2) * SR), int(0.3 * SR)); t = np.arange(n) / SR
        x = np.zeros(n)
        for m in ns + [m + 12 for m in ns] + [38 + K, 50 + K]:
            for det in (-0.07, 0.07):
                x += self.saw(self.note(m) * 2 ** (det / 12), n, self.rng.random())
        x = self.lp(x / 18, 2400) * np.minimum(1, t / 0.015) * (0.35 + 0.65 * np.exp(-t / 1.4))
        self.place(out, np.vstack([x, np.roll(x, 420)]), self.TF, 0.65)
        for i, m in enumerate([74 + K, 78 + K, 81 + K, 86 + K]):   # cellule de cloches qui « signe » le final
            self.place(out, self.bell(m + 12, 1.6), self.TF + 1.0 + i * self.BEAT / 2, 0.07, pan=-0.4 + 0.27 * i)
        return out

    def music(self):
        """Stem musique (2, N), avant ducking sous la voix ; s'arrête au final puis accord final."""
        t = np.arange(self.N) / SR
        pad, arp = self.pad_layer(), self.arp_layer()
        dr, bs, duck = self.drums_bass()
        m = (pad + bs) * duck + arp + dr * 0.8
        m = np.where(t < self.TF, m, 0) + self.final_music()
        m = self.reverb(m, 0.18)
        m *= np.clip(t / 0.4, 0, 1)
        return m * 0.62

    # ── bruitages ──
    def whoosh(self, dur=0.6, up=False, lo=300, hi=5200):
        n = int(dur * SR); t = np.linspace(0, 1, n); x = self.rng.standard_normal(n); out = np.zeros(n); seg = 256
        for s in range(0, n, seg):
            k = s / n
            fc = lo + (hi - lo) * (k ** 1.6 if up else np.sin(np.pi * k) ** 1.2)
            b, a = signal.butter(2, [max(fc * 0.6, 40) / (SR / 2), min(fc * 1.5 / (SR / 2), 0.99)], "band")
            out[s:s + seg] = signal.lfilter(b, a, x[s:s + seg])
        out *= (t ** 2.4 if up else np.sin(np.pi * t) ** 1.5)
        out /= np.abs(out).max() + 1e-9
        return np.vstack([out, np.interp(np.arange(n) - 160, np.arange(n), out)]) * 0.8

    def impact(self, low=38):
        n = int(1.4 * SR); t = np.arange(n) / SR
        f = low + 62 * np.exp(-t / 0.08)
        x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.42) + self.lp(self.rng.standard_normal(n), 1800) * np.exp(-t / 0.05) * 0.45
        return np.vstack([x, x]) * 0.8

    def crash(self):
        n = int(2.2 * SR); t = np.arange(n) / SR
        x = self.hp(self.rng.standard_normal(n), 4800) * np.exp(-t / 0.65)
        return np.vstack([x, np.roll(x, 300)]) * 0.45

    def pop(self, f0=880, f1=420, dur=0.09):
        n = int(dur * SR); t = np.arange(n) / SR
        f = f1 + (f0 - f1) * np.exp(-t / 0.02)
        return np.sin(2 * np.pi * np.cumsum(f) / SR) * self.env_ad(n, 0.002, dur * 0.35)

    def tick(self, f=2400, soft=False):
        n = int(0.05 * SR); t = np.arange(n) / SR
        x = (self.sine(f, n) * 0.5 + self.hp(self.rng.standard_normal(n), 3000) * 0.3) * np.exp(-t / 0.008)
        return self.lp(x, 2600) if soft else x

    def click(self):
        x = np.zeros(int(0.12 * SR))
        for o, g in ((0, 1.0), (0.055, 0.6)):
            n = int(0.03 * SR); t = np.arange(n) / SR
            c = (self.bp(self.rng.standard_normal(n), 1500, 6000) * 0.7 + self.sine(1800, n) * 0.4) * np.exp(-t / 0.004)
            i = self.t2i(o); x[i:i + n] += c * g
        return x

    def shimmer(self, buf, t0, base=86, count=6, step=0.05, gain=0.1):
        for i in range(count):
            self.place(buf, self.bell(base + [0, 4, 7, 12, 16, 19, 24, 28][i % 8]), t0 + i * step, gain * (1 - i * 0.07), pan=-0.6 + 1.2 * i / max(count - 1, 1))

    def riser(self, dur=0.9):
        n = int(dur * SR); t = np.linspace(0, 1, n); x = self.rng.standard_normal(n); out = np.zeros(n); seg = 512
        for s in range(0, n, seg):
            fc = 400 + 7000 * (s / n) ** 2
            b, a = signal.butter(2, [fc * 0.7 / (SR / 2), min(fc * 1.4 / (SR / 2), 0.99)], "band")
            out[s:s + seg] = signal.lfilter(b, a, x[s:s + seg])
        out = out / (np.abs(out).max() + 1e-9) * t ** 2.4
        return np.vstack([out, np.roll(out, 240)]) * 0.55

    def scribble(self, dur=0.45, seed=0):
        """feutre : bruit filtré modulé par le geste + petits crissements"""
        r = np.random.default_rng(seed); n = int(dur * SR); t = np.arange(n) / SR
        x = self.bp(r.standard_normal(n), 1800, 6500)
        strokes = np.abs(np.sin(2 * np.pi * (7 + 3 * r.random()) * t + r.random())) ** 0.6
        squeak = self.sine(2900 + 300 * np.sin(2 * np.pi * 9 * t), n) * 0.08 * (strokes > 0.95)
        env = np.minimum(1, t / 0.02) * np.minimum(1, (dur - t) / 0.05)
        return (x * strokes * 0.5 + squeak) * env

    def chord_ding(self, ms, dur=1.0):
        return sum(self.bell(m, dur) for m in ms) / len(ms)

    def sfx(self, only=None, skip=()):
        """Stem bruitages (2, N) depuis les repères de la page. only = ensemble de clés à synthétiser (None = toutes)."""
        fx, unknown = self.bus(), set()
        for ev in self.TL.get("sfx", []):
            t, k, g, p = ev["t"], ev["k"], ev.get("g", 1), ev.get("p", 0)
            if (only is not None and k not in only) or k in skip:
                continue
            if k == "whoosh": self.place(fx, self.whoosh(0.55), t - 0.25, 0.42 * g, p)
            elif k == "whooshUp": self.place(fx, self.whoosh(0.7, up=True, lo=200, hi=4200), t - 0.35, 0.45 * g, p)
            elif k == "swoosh": self.place(fx, self.whoosh(0.35, lo=900, hi=7000), t - 0.12, 0.35 * g, p)
            elif k == "slide": self.place(fx, self.lp(self.whoosh(0.5, lo=200, hi=2400), 3000), t - 0.1, 0.4 * g, p)
            elif k == "impact":
                self.place(fx, self.impact(), t, 0.55 * g); self.place(fx, self.crash(), t, 0.2 * g)
            elif k == "boom": self.place(fx, self.impact(32), t, 0.5 * g)
            elif k == "riser": self.place(fx, self.riser(0.45 if t < 5 else 1.0), t, 0.5 * g)
            elif k == "shimmer": self.shimmer(fx, t, base=86, count=6, step=0.05, gain=0.09 * g)
            elif k == "twinkle": self.shimmer(fx, t, base=93, count=4, step=0.04, gain=0.08 * g)
            elif k == "pop": self.place(fx, self.pop(820 + 60 * (p + 1), 420), t, 0.4 * g, p)
            elif k == "bubble": self.place(fx, self.pop(500, 1200, 0.08), t, 0.35 * g, p)
            elif k in ("tick", "tickSoft"): self.place(fx, self.tick(2400 if k == "tick" else 1900, soft=k == "tickSoft"), t, 0.35 * g, p)
            elif k == "click": self.place(fx, self.click(), t - 0.01, 0.5 * g, p)
            elif k == "flip":
                self.place(fx, self.whoosh(0.25, lo=800, hi=5000), t - 0.1, 0.3 * g, p)
                n = int(0.04 * SR)
                self.place(fx, self.bp(self.rng.standard_normal(n), 1200, 4000) * np.exp(-np.arange(n) / (0.008 * SR)), t + 0.12, 0.3 * g, p)
            elif k == "card":
                self.place(fx, self.whoosh(0.28, lo=700, hi=4500), t - 0.1, 0.22 * g, p); self.place(fx, self.tick(2000, soft=True), t + 0.1, 0.25 * g, p)
            elif k in ("scribble", "scribbleLong"): self.place(fx, self.scribble(0.45 if k == "scribble" else 0.62, seed=int(t * 10)), t, 0.32 * g, p)
            elif k == "success":
                self.place(fx, self.chord_ding([79, 83], 1.0), t, 0.22 * g); self.place(fx, self.chord_ding([86, 91], 1.2), t + 0.11, 0.18 * g)
            elif k == "ding": self.place(fx, self.bell(88, 0.8), t, 0.26 * g, p)
            elif k == "pillPop":
                self.place(fx, self.pop(700, 380, 0.12), t, 0.45 * g); self.shimmer(fx, t + 0.05, base=88, count=4, step=0.045, gain=0.07 * g)
            elif k == "finalChord":
                self.place(fx, self.crash(), t, 0.25 * g); self.shimmer(fx, t, base=86, count=7, step=0.06, gain=0.08 * g)
            else:
                unknown.add(k); self.place(fx, self.pop(), t, 0.3 * g, p)
        if unknown:
            print("  (bruitages inconnus, remplacés par un pop :", ", ".join(sorted(unknown)), ")")
        return self.reverb(fx, 0.2) * 0.85


def write(path, x):
    """(2, N) float -> WAV float32 stéréo 48 kHz (pas d'écrêtage : le mixage règle les niveaux)."""
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    wavfile.write(path, SR, np.ascontiguousarray(x.T).astype(np.float32))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--timeline", default="out/timeline-9x16.json")
    ap.add_argument("--key", type=int, default=None)
    ap.add_argument("--out-dir", default="build")
    a = ap.parse_args()
    S = Synth(json.load(open(a.timeline, encoding="utf-8")), a.key)
    print(f"  grille : {60 / S.BEAT:.1f} BPM, {S.NBARS} mesures de {S.BAR:.3f} s, de {S.T0:.2f} à {S.TF:.2f} s, tonalité {S.KEY:+d}")
    write(os.path.join(a.out_dir, "stem-music.wav"), S.music())
    write(os.path.join(a.out_dir, "stem-sfx.wav"), S.sfx())
    print("ok ->", os.path.join(a.out_dir, "stem-music.wav"), "+ stem-sfx.wav")
