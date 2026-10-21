# -*- coding: utf-8 -*-
"""MIXAGE du film : voix + musique + bruitages -> out/mix.wav, normalisé à −14 LUFS intégrés, crête vraie ≤ −1 dBTP.

  python tools/mix.py [--timeline out/timeline-9x16.json] [--config mix.json] [--out out/mix.wav] [--stems]

Réglages dans mix.json (dossier du film ; tout est facultatif — sans fichier : musique et bruitages synthétisés, sans voix) :
{
  "voice": "vo/narration.wav",   // la voix off (tools/el.py tts, ou un enregistrement) ; null = pas de voix
  "voice_at": null,              // instant de la voix dans le film (défaut : vo_at de la page = WIZ_FILM.voAt)
  "voice_keep": false,           // true : la voix est la piste d'un MONTAGE FILMÉ, resserrée selon keep (cut.js), posée à 0
  "voice_af": "highpass=f=85,…", // chaîne ffmpeg de la voix (passe-haut, égaliseur, compresseur, de-esser, limiteur)
  "music": "synth",              // "synth" | [["build/el/music-a.mp3", début dans le film, gain dB, entrée dans le fichier], …] | null
  "music_db": 0,                 // gain global de la musique (dB)
  "duck_db": -10,                // baisse de la musique quand la voix parle (ducking sur l'enveloppe de la voix)
  "sfx": "synth",                // "synth" | { "pop": ["build/el/pop.mp3", -8], … } (repères absents de la table -> synthétisés) | null
  "sfx_db": 0,
  "sfx_extra": [],               // [[t, "build/el/x.mp3", gain dB], …] bruitages posés à la main
  "lufs": -14, "tp": -1.5        // cible ; la crête vraie est visée à −1,5 pour rester ≤ −1 dBTP après l'encodage AAC
}
La voix doit rester parfaitement intelligible (musique ~10–14 dB dessous, bruitages ~5 dB dessous pendant qu'elle parle)."""
import argparse, json, os, re, subprocess, sys, wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
SR = 48000
VOICE_AF = ("highpass=f=85,equalizer=f=220:t=q:w=1.1:g=-2.5,equalizer=f=3200:t=q:w=1.3:g=2.5,equalizer=f=9000:t=h:w=1:g=1.5,"
            "acompressor=threshold=-21dB:ratio=3.2:attack=4:release=90:makeup=2.5,deesser=i=0.35:m=0.5:f=0.45,alimiter=limit=0.89")
DEFAULT = {"voice": None, "voice_at": None, "voice_keep": False, "voice_af": VOICE_AF, "music": "synth", "music_db": 0.0, "duck_db": -10.0,
           "sfx": "synth", "sfx_db": 0.0, "sfx_extra": [], "lufs": -14.0, "tp": -1.5, "key": None}


def strip_comments(txt):
    return re.sub(r"^\s*//.*$|(?<=[,\[{\s])//[^\n\"]*$", "", txt, flags=re.M)


def load(path, tmpdir):
    """N'importe quel fichier son -> float32 (n, 2) à 48 kHz."""
    tmp = os.path.join(tmpdir, "_tmp_load.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", path, "-ac", "2", "-ar", str(SR), "-c:a", "pcm_s16le", tmp], check=True)
    with wave.open(tmp) as w:
        a = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).reshape(-1, 2).astype(np.float32) / 32768
    os.remove(tmp)
    return a


def save(path, a):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    a = np.clip(a, -1, 1)
    with wave.open(path, "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((a * 32767).astype(np.int16).tobytes())


def remap(a, keep):
    """Garde les intervalles `keep` (temps du montage), raccords fondus sur 8 ms."""
    if not keep:
        return a
    parts, f = [], int(0.008 * SR)
    for x, y in keep:
        p = a[int(x * SR):int(y * SR)].copy()
        if len(p) > 2 * f:
            r = np.linspace(0, 1, f)[:, None]; p[:f] *= r; p[-f:] *= r[::-1]
        parts.append(p)
    return np.concatenate(parts) if parts else a[:0]


def place(dst, x, i0):
    if i0 >= len(dst):
        return
    if i0 < 0:
        x, i0 = x[-i0:], 0
    k = min(len(x), len(dst) - i0)
    if k > 0:
        dst[i0:i0 + k] += x[:k]


def envelope(v):
    """Enveloppe de la voix (0..1), attaque 30 ms, relâche 300 ms : sert au ducking."""
    m = np.abs(v).mean(axis=1); hop = int(SR * 0.01); n = len(m) // hop
    if not n:
        return np.zeros(len(v))
    rms = np.sqrt((m[:n * hop].reshape(n, hop) ** 2).mean(axis=1) + 1e-12)
    on = (20 * np.log10(rms) > -42).astype(np.float32); env = np.zeros_like(on); g = 0.0
    for i, x in enumerate(on):
        g = g + (x - g) * (0.33 if x > g else 0.033); env[i] = g
    e = np.repeat(env, hop)
    return np.concatenate([e, np.full(len(v) - len(e), e[-1] if len(e) else 0)])[:len(v)]


def measure(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", path, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", r)[-1])
    return I, TP


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="dossier du film")
    ap.add_argument("--timeline", default=None, help="défaut : out/timeline-9x16.json (ou le premier out/timeline-*.json)")
    ap.add_argument("--config", default="mix.json")
    ap.add_argument("--out", default="out/mix.wav")
    ap.add_argument("--stems", action="store_true", help="écrit aussi build/stem-{voice,music,sfx}.wav")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    rel = lambda p: p if os.path.isabs(p) else os.path.join(root, p)
    tlp = a.timeline
    if not tlp:
        cands = [os.path.join(root, "out", "timeline-9x16.json")] + sorted(
            os.path.join(root, "out", f) for f in os.listdir(os.path.join(root, "out")) if f.startswith("timeline-")) if os.path.isdir(os.path.join(root, "out")) else []
        tlp = next((c for c in cands if os.path.exists(c)), None)
        if not tlp:
            raise SystemExit("timeline introuvable : python tools/render.py timeline")
    TL = json.load(open(rel(tlp), encoding="utf-8"))
    cfg = dict(DEFAULT)
    if os.path.exists(rel(a.config)):
        cfg.update(json.loads(strip_comments(open(rel(a.config), encoding="utf-8").read())))
    build = os.path.join(root, "build"); os.makedirs(build, exist_ok=True)
    n = int(round(TL["dur"] * SR))

    # 1) la VOIX
    voice = np.zeros((n, 2), np.float32)
    if cfg["voice"]:
        v = load(rel(cfg["voice"]), build)
        at = 0.0
        if cfg["voice_keep"]:
            v = remap(v, TL.get("keep"))
        else:
            at = cfg["voice_at"] if cfg["voice_at"] is not None else float(TL.get("vo_at", 0))
        pre, post = os.path.join(build, "voice-pre.wav"), os.path.join(build, "voice-post.wav")
        save(pre, v)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pre, "-af", cfg["voice_af"], "-ar", str(SR), post], check=True)
        place(voice, load(post, build), int(round(at * SR)))
    env = envelope(voice) if cfg["voice"] else np.zeros(n)

    # 2) la MUSIQUE
    mus = np.zeros((n, 2), np.float32)
    S = None
    if cfg["music"] == "synth" or cfg["sfx"]:
        import synth   # même dossier (tools/)
        S = synth.Synth(TL, cfg.get("key"))
    if cfg["music"] == "synth":
        mus += S.music().T.astype(np.float32)
        print(f"  musique synthétisée : {60 / S.BEAT:.1f} BPM, {S.NBARS} mesures, tonalité {S.KEY:+d}")
    elif isinstance(cfg["music"], list):
        for path, t0, gdb, src0 in cfg["music"]:
            m = load(rel(path), build)[int(src0 * SR):]
            i0 = int(t0 * SR)
            while len(m) and len(m) < n - i0:
                m = np.concatenate([m, m])
            m = m[:max(0, n - i0)] * 10 ** (gdb / 20)
            fi = min(len(m), int(0.25 * SR))
            if fi:
                m[:fi] *= np.linspace(0, 1, fi)[:, None]
            place(mus, m, i0)
        fo = min(n, int(1.2 * SR)); mus[-fo:] *= np.linspace(1, 0, fo)[:, None]
    mus *= 10 ** (cfg["music_db"] / 20)
    if cfg["voice"]:
        mus *= (10 ** (cfg["duck_db"] * env / 20))[:, None]

    # 3) les BRUITAGES : fichiers de la table, sinon synthétisés
    fx = np.zeros((n, 2), np.float32)
    table = cfg["sfx"] if isinstance(cfg["sfx"], dict) else {}
    if cfg["sfx"]:
        cache = {}
        for c in TL.get("sfx", []):
            if c["k"] not in table:
                continue
            path, gdb = table[c["k"]]
            s = cache.get(path)
            if s is None:
                s = cache[path] = load(rel(path), build)
            place(fx, s * 10 ** ((gdb + 20 * np.log10(max(1e-3, c.get("g", 1)))) / 20), int(c["t"] * SR))
        fx += S.sfx(skip=set(table)).T.astype(np.float32)
    for t, path, gdb in cfg["sfx_extra"]:
        place(fx, load(rel(path), build) * 10 ** (gdb / 20), int(t * SR))
    fx *= 10 ** (cfg["sfx_db"] / 20)
    if cfg["voice"]:
        fx *= (1 - 0.45 * env)[:, None]   # ~ −5 dB sous la voix

    # 4) somme, fondu de fin, normalisation en deux passes
    tt = np.arange(n) / SR
    mixd = voice + mus + fx
    mixd *= np.where(tt > TL["dur"] - 0.7, np.clip((TL["dur"] - tt) / 0.7, 0, 1), 1)[:, None]
    peak = float(np.abs(mixd).max()) or 1.0
    pm = os.path.join(build, "premaster.wav"); save(pm, mixd * (0.5 / peak))
    lufs, tp = float(cfg["lufs"]), float(cfg["tp"])
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", pm, "-af", f"loudnorm=I={lufs}:TP={tp}:LRA=11:print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    st = json.loads(r.stderr[r.stderr.rindex("{"):r.stderr.rindex("}") + 1])
    af = (f"loudnorm=I={lufs}:TP={tp}:LRA=11:measured_I={st['input_i']}:measured_TP={st['input_tp']}:measured_LRA={st['input_lra']}"
          f":measured_thresh={st['input_thresh']}:offset={st['target_offset']}:linear=true")
    out = rel(a.out); os.makedirs(os.path.dirname(out), exist_ok=True)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pm, "-af", af, "-ar", str(SR), "-c:a", "pcm_s16le", out], check=True)
    I, TP = measure(out)
    for _ in range(4):   # loudnorm rate souvent la cible sur un film court sous contrainte de crête : gain + limiteur suréchantillonné
        if abs(I - lufs) <= 0.25 and TP <= tp + 0.3:
            break
        g = lufs - I + (0.1 if I < lufs else 0)
        tmp = out + ".tmp.wav"; os.replace(out, tmp)
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af",
                        f"volume={g:.2f}dB,aresample=192000,alimiter=limit={10 ** ((tp - 0.2) / 20):.4f}:attack=2:release=60:level=false:latency=true,aresample={SR}",
                        "-c:a", "pcm_s16le", out], check=True)
        os.remove(tmp)
        I, TP = measure(out)
    if a.stems:
        for name, x in (("voice", voice), ("music", mus), ("sfx", fx)):
            save(os.path.join(build, f"stem-{name}.wav"), x * (0.5 / peak) * 10 ** ((lufs - float(st["input_i"])) / 20))
    ok = abs(I - lufs) <= 1 and TP <= -1.0
    print(f"{'ok' if ok else '⚠'} -> {os.path.relpath(out, root)} ({TL['dur']:.2f} s, {I:.1f} LUFS, crête vraie {TP:.1f} dBTP"
          f"{', voix ' + cfg['voice'] if cfg['voice'] else ', sans voix'}, {len(TL.get('sfx', []))} repères)")


if __name__ == "__main__":
    main()
