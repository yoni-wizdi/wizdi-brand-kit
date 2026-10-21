# -*- coding: utf-8 -*-
"""Fabrique le film de bout en bout, depuis son dossier :
  repères (render.py timeline, chaque format) -> mixage (mix.py -> out/mix.wav, −14 LUFS) -> rendu image par image en
  morceaux parallèles -> assemblage + son -> couverture (la carte de fin) posée 0,2 s en première image -> livrables.

  python tools/make.py [--formats 9x16,4x5,16x9] [--jobs 3] [--name wizplay] [--cover-at 3.0] [--skip-mix] [--keep-chunks]

Livrables (out/, noms de WIZDI-PRODUCTION §4) :
  <nom>-9x16-HD.mp4          REEL 1080x1920 (Reels, Stories, Shorts, TikTok, statut WhatsApp) + <nom>-Cover.jpg
  <nom>-4x5-HD.mp4           FEED 1080x1350 (fil Instagram / Facebook)
  <nom>-4x5-WhatsApp.mp4     la version WhatsApp : le 4:5 allégé, < 16 Mo
  <nom>-16x9-YouTube-HD.mp4  YOUTUBE 1920x1080 + <nom>-16x9-Thumbnail.jpg (miniature)
Chaque format est COMPOSÉ pour son cadre par la page (?format=…), jamais recadré depuis un autre. Même son pour tous."""
import argparse, json, os, shutil, subprocess, sys
from concurrent.futures import ThreadPoolExecutor

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
TOOLS = os.path.dirname(os.path.abspath(__file__))
SIZES = {"9x16": (1080, 1920), "4x5": (1080, 1350), "16x9": (1920, 1080), "1x1": (1080, 1080)}
HOLD = 0.2          # couverture tenue en tête (s)
LIGHT_MB = 15.5     # version WhatsApp < 16 Mo


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        print(r.stdout[-3000:], r.stderr[-3000:]); raise SystemExit(f"échec : {' '.join(map(str, cmd))}")
    return r.stdout


def probe(p):
    j = json.loads(run(["ffprobe", "-v", "error", "-print_format", "json", "-show_streams", "-show_format", p]))
    v = next(s for s in j["streams"] if s["codec_type"] == "video")
    return v["width"], v["height"], float(j["format"]["duration"]), os.path.getsize(p) / 1e6


def light(src, dst, w, h, dur):
    """Version légère : 720 de large, CRF 24 ; si > LIGHT_MB, deux passes au débit qui tient sous la limite."""
    lw, lh = 720, int(round(720 * h / w / 2) * 2)
    run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"scale={lw}:{lh}:flags=lanczos", "-c:v", "libx264", "-preset", "slow", "-crf", "24",
         "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", dst])
    if os.path.getsize(dst) / 1e6 > LIGHT_MB:
        kbps = int((LIGHT_MB * 8000 / dur - 128) * 0.95)
        log = dst + ".2pass"
        run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"scale={lw}:{lh}:flags=lanczos", "-c:v", "libx264", "-b:v", f"{kbps}k", "-pass", "1",
             "-passlogfile", log, "-an", "-f", "mp4", os.devnull])
        run(["ffmpeg", "-v", "error", "-y", "-i", src, "-vf", f"scale={lw}:{lh}:flags=lanczos", "-c:v", "libx264", "-b:v", f"{kbps}k", "-pass", "2",
             "-passlogfile", log, "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", dst])
        for f in os.listdir(os.path.dirname(dst)):
            if f.startswith(os.path.basename(log)):
                os.remove(os.path.join(os.path.dirname(dst), f))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--page", default="film.html")
    ap.add_argument("--formats", default="9x16,4x5,16x9")
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--jobs", type=int, default=3, help="navigateurs en parallèle (RAM : ~0,6 Go chacun)")
    ap.add_argument("--name", default=None, help="nom des livrables (défaut : WIZ_FILM.slug)")
    ap.add_argument("--cover-at", type=float, default=None, help="instant de la couverture (défaut : 0,4 s avant la fin = carte de fin)")
    ap.add_argument("--skip-mix", action="store_true", help="garder out/mix.wav tel quel")
    ap.add_argument("--keep-chunks", action="store_true")
    ap.add_argument("--crf", type=int, default=17)
    a = ap.parse_args()
    page = os.path.abspath(a.page)
    if not os.path.exists(page):
        raise SystemExit(f"page introuvable : {page}")
    root = os.path.dirname(page); out = os.path.join(root, "out"); os.makedirs(out, exist_ok=True)
    fmts = [f.strip() for f in a.formats.split(",") if f.strip()]
    for f in fmts:
        if f not in SIZES:
            raise SystemExit(f"format inconnu : {f} ({', '.join(SIZES)})")
    R = [sys.executable, os.path.join(TOOLS, "render.py")]

    # 1) repères de chaque format (la durée et les repères sonores doivent être les mêmes partout)
    tls = {}
    for f in fmts:
        print(run(R + ["timeline", "--page", page, "--format", f]).strip().splitlines()[-1])
        tls[f] = json.load(open(os.path.join(out, f"timeline-{f}.json"), encoding="utf-8"))
    ref = tls[fmts[0]]
    for f in fmts[1:]:
        if abs(tls[f]["dur"] - ref["dur"]) > 1e-3:
            raise SystemExit(f"durée différente en {f} ({tls[f]['dur']} s) et {fmts[0]} ({ref['dur']} s) : le son ne peut pas être commun")
        if len(tls[f]["sfx"]) != len(ref["sfx"]):
            print(f"  ⚠ {f} : {len(tls[f]['sfx'])} repères sonores contre {len(ref['sfx'])} en {fmts[0]} — le son suit {fmts[0]}")
    name = a.name or ref.get("slug") or "film"
    dur = ref["dur"]

    # 2) le son (un seul mixage pour tous les formats)
    mix = os.path.join(out, "mix.wav")
    if not a.skip_mix or not os.path.exists(mix):
        print(run([sys.executable, os.path.join(TOOLS, "mix.py"), "--root", root, "--timeline", os.path.join(out, f"timeline-{fmts[0]}.json")]).strip().splitlines()[-1])

    # 3) chaque format : rendu en morceaux parallèles -> assemblage -> son -> couverture en tête
    cover_t = a.cover_at if a.cover_at is not None else round(max(0.0, dur - 0.4), 2)
    done = []
    for f in fmts:
        w, h = SIZES[f]
        n = int(round(dur * a.fps)); jobs = max(1, min(a.jobs, n // 15 or 1))
        cuts = [round(i * n / jobs) for i in range(jobs + 1)]
        cdir = os.path.join(out, f"chunks-{f}"); os.makedirs(cdir, exist_ok=True)

        def chunk(i, f=f, cuts=cuts, cdir=cdir):
            p = os.path.join(cdir, f"c{i}.mp4")
            run(R + ["video", "--page", page, "--format", f, "--fps", str(a.fps), "--from", f"{cuts[i] / a.fps:.6f}", "--to", f"{cuts[i + 1] / a.fps:.6f}",
                     "--out", p, "--crf", "16"])
            return p
        print(f"  rendu {f} : {n} images en {jobs} morceaux…", flush=True)
        with ThreadPoolExecutor(jobs) as ex:
            parts = list(ex.map(chunk, range(jobs)))
        lst = os.path.join(cdir, "list.txt")
        open(lst, "w", encoding="utf-8").write("".join(f"file '{p.replace(os.sep, '/')}'\n" for p in parts))
        silent, body = os.path.join(cdir, "silent.mp4"), os.path.join(cdir, "body.mp4")
        run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", silent])
        run(["ffmpeg", "-v", "error", "-y", "-i", silent, "-i", mix, "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k",
             "-shortest", "-movflags", "+faststart", body])
        # couverture = la carte de fin, image nette, tenue 0,2 s en tête ; le son est décalé d'autant
        run(R + ["stills", str(cover_t), "--page", page, "--format", f, "--scale", "1", "--out", cdir])
        cover = os.path.join(cdir, f"t{cover_t:06.2f}.jpg")
        final = os.path.join(out, {"9x16": f"{name}-9x16-HD.mp4", "4x5": f"{name}-4x5-HD.mp4", "16x9": f"{name}-16x9-YouTube-HD.mp4"}.get(f, f"{name}-{f}-HD.mp4"))
        ms = int(HOLD * 1000)
        run(["ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", str(a.fps), "-t", str(HOLD), "-i", cover, "-i", body,
             "-filter_complex", f"[0:v]scale={w}:{h}:flags=lanczos,format=yuv420p,setsar=1,fps={a.fps}[c];[1:v]format=yuv420p,setsar=1,fps={a.fps}[m];"
             f"[c][m]concat=n=2:v=1:a=0[v];[1:a]adelay={ms}|{ms}[a]", "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-preset", "slow",
             "-crf", str(a.crf), "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "256k", "-movflags", "+faststart", final])
        if f == "9x16":
            shutil.copyfile(cover, os.path.join(out, f"{name}-Cover.jpg"))
        elif f == "16x9":
            shutil.copyfile(cover, os.path.join(out, f"{name}-16x9-Thumbnail.jpg"))
        elif f not in ("4x5",):
            shutil.copyfile(cover, os.path.join(out, f"{name}-{f}-Cover.jpg"))
        done.append((f, final))
        if not a.keep_chunks:
            shutil.rmtree(cdir, ignore_errors=True)

    # 4) la version légère WhatsApp (< 16 Mo) : le 4:5 s'il est rendu, sinon le premier format
    src_f, src = next(((f, p) for f, p in done if f == "4x5"), done[0])
    lw = os.path.join(out, f"{name}-{src_f}-WhatsApp.mp4")
    light(src, lw, *SIZES[src_f], dur + HOLD)
    done.append((src_f + " léger", lw))
    print("\nlivrables :")
    for f, p in done:
        w, h, d, mb = probe(p)
        print(f"  {os.path.relpath(p, root):38s} {w}x{h}  {d:6.2f} s  {mb:5.1f} Mo")
    print("contrôle : python tools/check.py out/<fichier>.mp4   (sonie, crête, planches, noirs)")


if __name__ == "__main__":
    main()
