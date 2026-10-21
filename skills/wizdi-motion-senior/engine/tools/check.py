# -*- coding: utf-8 -*-
"""Auto-contrôle d'un film rendu (avant livraison, et par le jury d'un concours).

  python tools/check.py out/wizplay-9x16-HD.mp4 [--scribe] [--lang heb]

Vérifie : format (1080x1920 / 1080x1350 / 1920x1080), 30 i/s, H.264 + AAC, durée, poids (< 16 Mo pour « WhatsApp ») ;
sonie (−14 LUFS ±1) et crête vraie (≤ −1 dBTP) ; noirs non couverts (blackdetect) ;
planches -> out/check-<nom>-hook.jpg (0–2 s toutes les 0,25 s : l'ACCROCHE) et out/check-<nom>-sheet.jpg (toutes les 0,5 s).
--scribe : re-transcrit la voix (ElevenLabs Speech-to-Text, quelques crédits ; clé dans la variable ELEVENLABS_API_KEY)
           -> out/check-<nom>-transcript.txt, à comparer mot à mot au texte validé (la voix doit être intégralement intelligible).
Code de sortie 1 si un contrôle bloquant échoue."""
import argparse, json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
TOOLS = os.path.dirname(os.path.abspath(__file__))
FORMATS = {(1080, 1920): "9:16", (1080, 1350): "4:5", (1920, 1080): "16:9", (1080, 1080): "1:1"}


def frames(mp4, times, path, cols, tw, w, h):
    from PIL import Image, ImageDraw
    th = int(tw * h / w); rows = (len(times) + cols - 1) // cols
    S = Image.new("RGB", (cols * tw, rows * th), (20, 20, 20)); tmp = path + "._f.jpg"
    for i, t in enumerate(times):
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.3f}", "-i", mp4, "-frames:v", "1", "-vf", f"scale={tw}:{th}", tmp], check=True)
        im = Image.open(tmp).convert("RGB"); d = ImageDraw.Draw(im); d.rectangle([0, 0, 50, 16], fill=(0, 0, 0)); d.text((3, 2), f"{t:5.2f}", fill=(255, 230, 0))
        S.paste(im, ((i % cols) * tw, (i // cols) * th))
    if os.path.exists(tmp):
        os.remove(tmp)
    S.save(path, quality=86)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mp4")
    ap.add_argument("--scribe", action="store_true")
    ap.add_argument("--lang", default="heb")
    ap.add_argument("--no-sheets", action="store_true")
    a = ap.parse_args()
    mp4 = os.path.abspath(a.mp4); out = os.path.dirname(mp4); base = os.path.splitext(os.path.basename(mp4))[0]
    pr = json.loads(subprocess.run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", mp4],
                                   capture_output=True, text=True, encoding="utf-8").stdout)
    v = next(s for s in pr["streams"] if s["codec_type"] == "video")
    au = next((s for s in pr["streams"] if s["codec_type"] == "audio"), None)
    dur = float(pr["format"]["duration"]); mb = os.path.getsize(mp4) / 1e6
    w, h = v["width"], v["height"]
    fps = eval(v["r_frame_rate"]) if re.fullmatch(r"\d+/\d+", v["r_frame_rate"]) else 0
    fails = []
    ok = lambda c, msg: (print(("OK  " if c else "⛔  ") + msg), (None if c else fails.append(msg)))
    light = "whatsapp" in base.lower()
    ok((w, h) in FORMATS or light, f"image {w}x{h} ({FORMATS.get((w, h), 'version légère' if light else 'format inattendu')})")
    ok(abs(fps - 30) < 0.01, f"{v['r_frame_rate']} i/s, {v['codec_name']} {v.get('pix_fmt', '')}, {dur:.2f} s, {mb:.1f} Mo")
    ok(v["codec_name"] == "h264" and (au or {}).get("codec_name") == "aac", "codecs H.264 + AAC")
    if light:
        ok(mb < 16, f"version WhatsApp : {mb:.1f} Mo (< 16 Mo)")
    if au:
        ln = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp4, "-af", "ebur128=peak=true", "-f", "null", "-"],
                            capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
        I = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", ln)[-1]); TP = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", ln)[-1])
        ok(abs(I + 14) <= 1, f"sonie {I:.1f} LUFS (cible −14 ±1)")
        ok(TP <= -1.0, f"crête vraie {TP:.1f} dBTP (≤ −1)")
    else:
        ok(False, "pas de piste son")
    bd = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp4, "-vf", "blackdetect=d=0.15:pic_th=0.97:pix_th=0.06", "-an", "-f", "null", "-"],
                        capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    blacks = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", bd)
    ok(not blacks, "aucun noir non couvert" if not blacks else "NOIRS à couvrir : " + ", ".join(f"{float(s):.2f}–{float(e):.2f} s" for s, e in blacks))
    if not a.no_sheets:
        frames(mp4, [round(i * 0.25, 2) for i in range(9) if i * 0.25 < dur], os.path.join(out, f"check-{base}-hook.jpg"), 9, 216 if w < h else 300, w, h)
        frames(mp4, [round(i * 0.5, 2) for i in range(int(dur / 0.5) + 1) if i * 0.5 < dur - 0.02], os.path.join(out, f"check-{base}-sheet.jpg"),
               10 if w < h else 6, 162 if w < h else 288, w, h)
        print(f"planches -> out/check-{base}-hook.jpg (accroche 0–2 s), out/check-{base}-sheet.jpg (film entier) : À REGARDER")
    if a.scribe:
        sys.path.insert(0, TOOLS)
        import el
        wav = os.path.join(out, f"_{base}.wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp4, "-vn", "-ac", "1", "-ar", "16000", wav], check=True)
        res = el.stt(wav, a.lang)
        os.remove(wav)
        p = os.path.join(out, f"check-{base}-transcript.txt")
        open(p, "w", encoding="utf-8").write(res.get("text", ""))
        print("transcription ->", p, ":", res.get("text", ""))
    print("RÉSULTAT :", "OK" if not fails else f"{len(fails)} contrôle(s) bloquant(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
