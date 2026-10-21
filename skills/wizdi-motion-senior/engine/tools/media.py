# -*- coding: utf-8 -*-
"""Les VRAIS médias du film -> séquences d'images que la page pose à l'instant exact (rien ne dépend du temps réel).
Uniquement de vraies captures / vrais enregistrements du produit : jamais une interface simulée ou recomposée.

  python tools/media.py add play-map  rec/wizplay.mp4 --from 52.4 --to 56.4      # vidéo -> build/media/play-map/0001.jpg … (30 i/s)
  python tools/media.py add box-hub   shots/hub.png --crop 0,180,930,445         # image fixe (recadrée : noms de personnes retirés)
  python tools/media.py add chat-quiz rec/chat.mp4 --from 23 --to 33 --autocrop  # bandes noires retirées automatiquement
  python tools/media.py footage take.mp4 [--from 0 --to 30] [--size 1080x1920]  # personne filmée -> build/footage/ (footage.js)
  python tools/media.py list | rm <nom>

Écrit build/media/manifest.json + manifest.js (window.WIZ_MEDIA = { nom: { n, w, h, fps } }).
Règles : capture HD montrée à 1x (une découpe ne s'agrandit jamais) ; les noms de personnes visibles se retirent par
recadrage (--crop) ; une page en portrait reste en portrait ; aucune provenance interne visible."""
import argparse, json, os, re, shutil, subprocess, sys
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
FPS = 30


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode:
        raise SystemExit(f"échec : {' '.join(map(str, cmd))}\n{r.stderr[-1500:]}")
    return r


def manifest(root):
    p = os.path.join(root, "build", "media", "manifest.json")
    return p, (json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {})


def save_manifest(root, man):
    d = os.path.join(root, "build", "media"); os.makedirs(d, exist_ok=True)
    json.dump(man, open(os.path.join(d, "manifest.json"), "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    with open(os.path.join(d, "manifest.js"), "w", encoding="utf-8") as fh:
        fh.write("/* GÉNÉRÉ par tools/media.py — ne pas éditer */\nwindow.WIZ_MEDIA = " + json.dumps(man, ensure_ascii=False) + ";\n")


def cropdetect(src, t0, t1):
    r = subprocess.run(["ffmpeg", "-v", "info", "-ss", f"{t0 + 0.3:.2f}", "-i", src, "-t", f"{max(t1 - t0 - 0.6, 0.5):.2f}",
                        "-vf", "cropdetect=24:2:0", "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8", errors="replace").stderr
    c = re.findall(r"crop=(\d+):(\d+):(\d+):(\d+)", r)
    if not c:
        return None
    w, h, x, y = map(int, Counter(c).most_common(1)[0][0])
    return x, y, w, h


def probe(src):
    r = run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration", "-of", "json", src])
    j = json.loads(r.stdout)
    s = j["streams"][0]
    return s["width"], s["height"], float(j["format"].get("duration") or 0)


def is_image(src):
    return os.path.splitext(src)[1].lower() in (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".gif", ".tif", ".tiff")


def add(a):
    from PIL import Image
    root = os.path.abspath(a.root)
    d = os.path.join(root, "build", "media", a.name)
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    crop = tuple(int(v) for v in a.crop.split(",")) if a.crop else None
    p, man = manifest(root)
    if is_image(a.src) and not a.still_from_video:
        im = Image.open(a.src).convert("RGB")
        if crop:
            x, y, w, h = crop
            im = im.crop((x, y, x + w, y + h))
        im.save(os.path.join(d, "0001.jpg"), quality=93)
        man[a.name] = {"n": 1, "w": im.width, "h": im.height, "fps": 0}
    else:
        W, H, dur = probe(a.src)
        t0, t1 = a.t_from, (a.t_to if a.t_to is not None else dur)
        if not crop and a.autocrop:
            crop = cropdetect(a.src, t0, t1)
        x, y, w, h = crop or (0, 0, W, H)
        w, h = w - w % 2, h - h % 2
        vf = f"crop={w}:{h}:{x}:{y},fps={a.fps}"
        if a.still_from_video:
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-i", a.src, "-frames:v", "1", "-vf", f"crop={w}:{h}:{x}:{y}", "-q:v", "2", os.path.join(d, "0001.jpg")])
            man[a.name] = {"n": 1, "w": w, "h": h, "fps": 0}
        else:
            run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-i", a.src, "-t", f"{t1 - t0:.3f}", "-vf", vf, "-q:v", "3", os.path.join(d, "%04d.jpg")])
            n = len([f for f in os.listdir(d) if f.endswith(".jpg")])
            man[a.name] = {"n": n, "w": w, "h": h, "fps": a.fps}
    if a.note:
        man[a.name]["note"] = a.note
    save_manifest(root, man)
    print(f"ok -> build/media/{a.name}/  {man[a.name]}")


def footage(a):
    root = os.path.abspath(a.root)
    d = os.path.join(root, "build", "footage")
    if os.path.isdir(d):
        shutil.rmtree(d)
    os.makedirs(d)
    W, H = (int(v) for v in a.size.lower().split("x"))
    _, _, dur = probe(a.src)
    t0, t1 = a.t_from, (a.t_to if a.t_to is not None else dur)
    # ffmpeg redresse les vidéos de téléphone (rotation) ; recadrage « cover » au format demandé
    vf = f"scale={W}:{H}:force_original_aspect_ratio=increase:flags=lanczos,crop={W}:{H},fps={a.fps}"
    run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t0:.3f}", "-i", a.src, "-t", f"{t1 - t0:.3f}", "-vf", vf, "-q:v", "3", os.path.join(d, "%04d.jpg")])
    n = len([f for f in os.listdir(d) if f.endswith(".jpg")])
    info = {"dir": "build/footage/", "n": n, "w": W, "h": H, "fps": a.fps}
    json.dump(info, open(os.path.join(d, "info.json"), "w"), indent=1)
    print(f"ok -> build/footage/ ({n} images {W}x{H} à {a.fps} i/s)")
    print("dans film.js : footage: " + json.dumps(info))
    print("son de la prise (voix) : ffmpeg -i <clip> -ss … -t … -vn -ac 1 -ar 48000 vo/voice.wav  (puis mix.json : voice)")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in ("add", "footage"):
        s = sub.add_parser(name)
        if name == "add":
            s.add_argument("name")
        s.add_argument("src")
        s.add_argument("--from", dest="t_from", type=float, default=0.0)
        s.add_argument("--to", dest="t_to", type=float, default=None)
        s.add_argument("--fps", type=int, default=FPS)
        s.add_argument("--root", default=".")
        if name == "add":
            s.add_argument("--crop", default=None, help="x,y,w,h en px de la source")
            s.add_argument("--autocrop", action="store_true", help="retire les bandes noires (cropdetect)")
            s.add_argument("--still-from-video", action="store_true", help="une seule image prise à --from")
            s.add_argument("--note", default=None, help="ce que montre l'écran (aide-mémoire, jamais affiché)")
        else:
            s.add_argument("--size", default="1080x1920")
    s = sub.add_parser("list"); s.add_argument("--root", default=".")
    s = sub.add_parser("rm"); s.add_argument("name"); s.add_argument("--root", default=".")
    a = ap.parse_args()
    if a.cmd == "add":
        add(a)
    elif a.cmd == "footage":
        footage(a)
    elif a.cmd == "list":
        _, man = manifest(os.path.abspath(a.root))
        for k, v in sorted(man.items()):
            print(f"  {k:24s} {v['w']}x{v['h']}  {'fixe' if v['n'] <= 1 else str(v['n']) + ' images à ' + str(v['fps']) + ' i/s'}  {v.get('note', '')}")
    elif a.cmd == "rm":
        root = os.path.abspath(a.root)
        _, man = manifest(root)
        man.pop(a.name, None)
        shutil.rmtree(os.path.join(root, "build", "media", a.name), ignore_errors=True)
        save_manifest(root, man)
        print("supprimé :", a.name)


if __name__ == "__main__":
    main()
