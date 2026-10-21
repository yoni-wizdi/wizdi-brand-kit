#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
composite-quad.py — incruste une vidéo (ex: capture d'interface) dans un quad
(4 coins) d'une vidéo de base (ex: écran d'un laptop filmé). Quad FIXE fourni
par l'utilisateur via l'outil quad-picker (jamais deviné automatiquement).

Usage:
  python composite-quad.py --base base.mp4 --overlay ui.mp4 \
      --quad '{"tl":[x,y],"tr":[x,y],"br":[x,y],"bl":[x,y]}' \
      --out out.mp4 [--speed 6.5] [--overlay-start 55] [--overlay-end 150] \
      [--white 235,245,255] [--feather 1.0] [--fps 30] [--crf 23]

Pipeline: ffmpeg extrait les frames de base → PIL warp l'overlay dans le quad
frame par frame → ffmpeg ré-encode. Nécessite: pip install pillow numpy ; ffmpeg dans le PATH.
"""
import argparse, json, math, os, shutil, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageFilter

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"FFMPEG FAIL: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r

def probe_fps_duration(path):
    r = subprocess.run(["ffprobe","-v","quiet","-print_format","json","-show_streams","-show_format",path],
                       capture_output=True, text=True)
    d = json.loads(r.stdout)
    vs = next(s for s in d["streams"] if s["codec_type"]=="video")
    num, den = vs["r_frame_rate"].split("/")
    return float(num)/float(den), float(d["format"]["duration"]), int(vs["width"]), int(vs["height"])

def perspective_coeffs(src_quad, dst_quad):
    """Coefficients PIL pour transformer dst→src (PIL veut l'inverse)."""
    A, B = [], []
    for (sx, sy), (dx, dy) in zip(src_quad, dst_quad):
        A.append([dx, dy, 1, 0, 0, 0, -sx*dx, -sx*dy]); B.append(sx)
        A.append([0, 0, 0, dx, dy, 1, -sy*dx, -sy*dy]); B.append(sy)
    return np.linalg.solve(np.array(A, dtype=float), np.array(B, dtype=float))

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", required=True)
    p.add_argument("--overlay", required=True)
    p.add_argument("--quad", required=True, help='JSON {"tl":[x,y],"tr":..,"br":..,"bl":..} en pixels de la vidéo de base')
    p.add_argument("--out", required=True)
    p.add_argument("--speed", type=float, default=1.0, help="accélération de l'overlay (ex: 6.5)")
    p.add_argument("--overlay-start", type=float, default=0.0, help="début (s) dans l'overlay source")
    p.add_argument("--overlay-end", type=float, default=None, help="fin (s) dans l'overlay source")
    p.add_argument("--screen-aspect", type=float, default=None,
                   help="aspect PHYSIQUE de la dalle (ex: 1.6 pour un MacBook 16:10). Défaut = aspect 2D du quad. "
                        "Pour un écran vu en perspective, TOUJOURS donner l'aspect physique : l'homographie gère le raccourci, "
                        "recadrer au quad 2D compresserait l'interface.")
    p.add_argument("--white", default=None, help="R,G,B : blanc cible (balance) échantillonné sur l'écran de la base ; défaut = pas de correction")
    p.add_argument("--black-floor", type=int, default=16, help="plancher des noirs (un écran filmé n'a jamais de noir pur)")
    p.add_argument("--feather", type=float, default=1.0, help="flou du bord du masque en px")
    p.add_argument("--fps", type=int, default=None, help="fps de sortie (défaut: fps de la base)")
    p.add_argument("--crf", type=int, default=23)
    args = p.parse_args()

    quad = json.loads(args.quad)
    dst = [tuple(quad[k]) for k in ("tl","tr","br","bl")]

    base_fps, base_dur, W, H = probe_fps_duration(args.base)
    out_fps = args.fps or round(base_fps)
    n_frames = int(round(base_dur * out_fps))

    tmp = tempfile.mkdtemp(prefix="quadcomp_")
    bdir, odir, cdir = [os.path.join(tmp, d) for d in ("base","ovl","comp")]
    for d in (bdir, odir, cdir): os.makedirs(d)

    # 1) frames de la base
    run(["ffmpeg","-y","-i",args.base,"-vf",f"fps={out_fps}",os.path.join(bdir,"f%05d.png")])
    base_frames = sorted(os.listdir(bdir))

    # 2) frames de l'overlay : fenêtre temporelle + accélération → autant de frames que la base
    ss = ["-ss", str(args.overlay_start)] if args.overlay_start else []
    to = ["-to", str(args.overlay_end)] if args.overlay_end else []
    # durée utile / speed doit couvrir base_dur ; on échantillonne à la cadence nécessaire
    ovl_fps = out_fps * args.speed
    run(["ffmpeg","-y",*ss,*to,"-i",args.overlay,"-vf",f"fps={ovl_fps}",os.path.join(odir,"f%05d.png")])
    ovl_frames = sorted(os.listdir(odir))
    if len(ovl_frames) < len(base_frames):
        # boucle si l'overlay est trop court
        k = len(ovl_frames)
        ovl_frames = [ovl_frames[i % k] for i in range(len(base_frames))]

    # dimensions du quad cible (pour recadrer l'overlay au bon aspect, sans distorsion)
    wq = max(math.dist(dst[0],dst[1]), math.dist(dst[3],dst[2]))
    hq = max(math.dist(dst[0],dst[3]), math.dist(dst[1],dst[2]))
    quad_aspect = args.screen_aspect if args.screen_aspect else wq/hq

    ov0 = Image.open(os.path.join(odir, ovl_frames[0]))
    ow, oh = ov0.size
    if ow/oh > quad_aspect:   # overlay trop large → crop horizontal centré
        cw = int(oh*quad_aspect); box = ((ow-cw)//2, 0, (ow+cw)//2, oh)
    else:                     # trop haut → crop vertical
        ch = int(ow/quad_aspect); box = (0, (oh-ch)//2, ow, (oh+ch)//2)

    white = tuple(int(v) for v in args.white.split(",")) if args.white else None

    # masque du quad (anti-aliasé + feather) — calculé UNE fois (quad fixe)
    SS = 4
    mask_hi = Image.new("L", (W*SS, H*SS), 0)
    from PIL import ImageDraw
    ImageDraw.Draw(mask_hi).polygon([(x*SS, y*SS) for x,y in dst], fill=255)
    mask = mask_hi.resize((W, H), Image.LANCZOS)
    if args.feather > 0:
        mask = mask.filter(ImageFilter.GaussianBlur(args.feather))

    # ANTI-ALIASING : pré-réduire l'overlay à ~2× la taille du quad AVANT le warp
    # (le transform PIL point-sample : réduire ×5-7 directement = crénelage/scintillement)
    box_w, box_h = box[2]-box[0], box[3]-box[1]
    s = min(1.0, (wq*2.0)/box_w)
    tw, th = max(2,int(round(box_w*s))), max(2,int(round(box_h*s)))

    src_rect = [(0,0),(tw,0),(tw,th),(0,th)]
    coeffs = perspective_coeffs(src_rect, dst)

    for i, bf in enumerate(base_frames):
        base = Image.open(os.path.join(bdir, bf)).convert("RGB")
        ov = Image.open(os.path.join(odir, ovl_frames[min(i, len(ovl_frames)-1)])).convert("RGB").crop(box)
        if (tw, th) != (box_w, box_h):
            ov = ov.resize((tw, th), Image.LANCZOS)

        arr = np.asarray(ov).astype(np.float32)
        if white:  # balance des blancs : blanc overlay → blanc réel de l'écran filmé
            arr *= np.array(white, dtype=np.float32)/255.0
        if args.black_floor:  # un noir projeté/affiché n'est jamais noir
            arr = args.black_floor + arr*(255.0-args.black_floor)/255.0
        ov = Image.fromarray(np.clip(arr,0,255).astype(np.uint8))

        warped = ov.transform((W,H), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
        base.paste(warped, (0,0), mask)
        base.save(os.path.join(cdir, bf))
        if i % 50 == 0: print(f"  frame {i}/{len(base_frames)}")

    # 3) encode (muet, web-ready)
    run(["ffmpeg","-y","-framerate",str(out_fps),"-i",os.path.join(cdir,"f%05d.png"),
         "-c:v","libx264","-pix_fmt","yuv420p","-crf",str(args.crf),"-movflags","+faststart","-an",args.out])
    # poster de la 1re frame composée
    poster = os.path.splitext(args.out)[0] + "-poster.jpg"
    Image.open(os.path.join(cdir, base_frames[0])).save(poster, quality=85)

    shutil.rmtree(tmp, ignore_errors=True)
    print(f"OK -> {args.out} + {poster}")

if __name__ == "__main__":
    main()
