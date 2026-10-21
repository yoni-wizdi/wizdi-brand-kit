#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
composite-quad-brush.py — incruste une video dans un quad FIXE, l'occulteur
(ce qui doit rester DEVANT) etant un masque PEINT PAR L'UTILISATEUR sur la
1re frame, puis SUIVI sur toute la duree.

Les deux entrees viennent de l'utilisateur, jamais d'une detection auto :
  --quad    : les 4 coins de la dalle (quad-picker)
  --strokes : les traits de pinceau (mask-brush)

Suivi du masque, en deux temps :
  1. TRANSLATION mesuree par correlation de phase (FFT) entre la frame t et la
     frame 0, sur une fenetre autour du masque -> le masque se deplace avec la tete.
  2. EXTENSION par la couleur, dans une bande autour du contour deplace : on
     ajoute au masque ce qui est nettement plus sombre que l'ecran (les teintes
     que l'utilisateur a peintes). Purement additif : le trace de l'utilisateur
     n'est JAMAIS rogne.

Usage:
  python composite-quad-brush.py --base b.mp4 --overlay ui.mp4 \
    --quad '{"tl":[..],"tr":[..],"br":[..],"bl":[..]}' --strokes strokes.json \
    --out hero.mp4 --speed 6 --overlay-start 176 --overlay-end 224 \
    --crop '{"x":229,"y":0,"w":1698,"h":1080}' --white 226,221,223
"""
import argparse, json, math, os, shutil, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from scipy import ndimage as ndi


def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        sys.exit(f"FFMPEG FAIL: {' '.join(cmd)}\n{r.stderr[-2000:]}")
    return r


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "quiet", "-print_format", "json",
                        "-show_streams", "-show_format", path], capture_output=True, text=True)
    d = json.loads(r.stdout)
    vs = next(s for s in d["streams"] if s["codec_type"] == "video")
    num, den = vs["r_frame_rate"].split("/")
    return float(num) / float(den), float(d["format"]["duration"]), int(vs["width"]), int(vs["height"])


def perspective_coeffs(src_quad, dst_quad):
    A, B = [], []
    for (sx, sy), (dx, dy) in zip(src_quad, dst_quad):
        A.append([dx, dy, 1, 0, 0, 0, -sx * dx, -sx * dy]); B.append(sx)
        A.append([0, 0, 0, dx, dy, 1, -sy * dx, -sy * dy]); B.append(sy)
    return np.linalg.solve(np.array(A, dtype=float), np.array(B, dtype=float))


def rasterize_strokes(data, W, H):
    """Rejoue les traits exactement comme le canvas de l'outil :
    epaisseur 2r, bouts et jointures ronds, gomme = mise a zero."""
    img = Image.new("L", (W, H), 0)
    d = ImageDraw.Draw(img)
    for s in data["strokes"]:
        r, col = float(s["r"]), (0 if s.get("e") else 255)
        pts = [(float(x), float(y)) for x, y in s["p"]]
        if len(pts) > 1:
            d.line(pts, fill=col, width=int(round(r * 2)), joint="curve")
        for (x, y) in pts:                      # bouts ronds
            d.ellipse([x - r, y - r, x + r, y + r], fill=col)
    return np.asarray(img) > 127


def shift_bool(m, dx, dy):
    """Translation entiere d'un masque booleen, remplissage a False."""
    out = np.zeros_like(m)
    H, W = m.shape
    sy0, sy1 = max(0, -dy), min(H, H - dy)
    sx0, sx1 = max(0, -dx), min(W, W - dx)
    if sy0 >= sy1 or sx0 >= sx1:
        return out
    out[sy0 + dy:sy1 + dy, sx0 + dx:sx1 + dx] = m[sy0:sy1, sx0:sx1]
    return out


def contour_samples(M0, W, H, band=10, maxpts=20000, seed=0):
    """Points d'echantillonnage sur la BANDE DE CONTOUR du masque peint.

    C'est la seule zone qui porte du contraste (occulteur sombre / ecran clair) :
    suivre sur toute la fenetre echouerait, l'ecran etant lisse et sans texture
    — la mise en correspondance s'accrocherait alors au grain.
    """
    k = np.ones((band * 2 + 1, band * 2 + 1))
    ring = ndi.binary_dilation(M0, k) & ~ndi.binary_erosion(M0, k)
    ys, xs = np.where(ring)
    # marge pour que le decalage ne sorte jamais de l'image
    keep = (ys > 20) & (ys < H - 21) & (xs > 20) & (xs < W - 21)
    ys, xs = ys[keep], xs[keep]
    if len(ys) > maxpts:
        idx = np.random.default_rng(seed).choice(len(ys), maxpts, replace=False)
        ys, xs = ys[idx], xs[idx]
    return ys, xs


def track_shift(ref, cur, ys, xs, maxshift):
    """Decalage entier (dx,dy) minimisant l'ecart absolu sur la bande de contour."""
    r = ref[ys, xs]
    best, bdx, bdy = None, 0, 0
    for dy in range(-maxshift, maxshift + 1):
        for dx in range(-maxshift, maxshift + 1):
            c = float(np.abs(r - cur[ys + dy, xs + dx]).mean())
            if best is None or c < best:
                best, bdx, bdy = c, dx, dy
    return bdx, bdy


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", required=True)
    p.add_argument("--overlay", required=True)
    p.add_argument("--quad", required=True)
    p.add_argument("--strokes", required=True, help="JSON de l'outil mask-brush")
    p.add_argument("--out", required=True)
    p.add_argument("--speed", type=float, default=1.0)
    p.add_argument("--overlay-start", type=float, default=0.0)
    p.add_argument("--overlay-end", type=float, default=None)
    p.add_argument("--crop", default=None)
    p.add_argument("--screen-aspect", type=float, default=None)
    p.add_argument("--white", default=None)
    p.add_argument("--black-floor", type=int, default=16)
    p.add_argument("--feather", type=float, default=1.0)
    p.add_argument("--mask-feather", type=float, default=1.4)
    p.add_argument("--track", type=int, default=14, help="amplitude max du suivi en px (0 = masque fige)")
    p.add_argument("--grow", type=int, default=8, help="bande d'extension par la couleur (0 = aucune)")
    p.add_argument("--protect-holes", type=int, default=200,
                   help="aire mini (px) d'un trou laisse volontairement dans le trace : "
                        "l'extension par la couleur n'y entrera jamais (0 = pas de protection)")
    p.add_argument("--fps", type=int, default=None)
    p.add_argument("--crf", type=int, default=23)
    args = p.parse_args()

    quad = json.loads(args.quad)
    dst = [tuple(quad[k]) for k in ("tl", "tr", "br", "bl")]

    base_fps, base_dur, W, H = probe(args.base)
    out_fps = args.fps or round(base_fps)

    sdata = json.load(open(args.strokes, encoding="utf-8"))
    if (sdata.get("w"), sdata.get("h")) != (W, H):
        sys.exit(f"Le masque a ete peint en {sdata.get('w')}x{sdata.get('h')} "
                 f"mais la base est en {W}x{H} — convertir les coordonnees d'abord.")
    M0 = rasterize_strokes(sdata, W, H)
    if not M0.any():
        sys.exit("Masque vide.")

    # Trous laisses VOLONTAIREMENT dans le trace (typiquement le verre des lunettes) :
    # l'extension par la couleur ne doit jamais les refermer, sinon on perd la
    # transparence que l'utilisateur a choisie.
    holes = np.zeros_like(M0)
    if args.protect_holes > 0:
        h = ndi.binary_fill_holes(M0) & ~M0
        lab, n = ndi.label(h)
        if n:
            sizes = ndi.sum(h, lab, range(1, n + 1))
            keep = np.arange(1, n + 1)[sizes >= args.protect_holes]
            if len(keep):
                holes = np.isin(lab, keep)
        print(f"trous proteges : {int(holes.sum())} px")

    tmp = tempfile.mkdtemp(prefix="quadbrush_")
    bdir, odir, cdir = [os.path.join(tmp, d) for d in ("base", "ovl", "comp")]
    for d in (bdir, odir, cdir):
        os.makedirs(d)

    run(["ffmpeg", "-y", "-i", args.base, "-vf", f"fps={out_fps}", os.path.join(bdir, "f%05d.png")])
    base_frames = sorted(os.listdir(bdir))

    vf = []
    if args.crop:
        c = json.loads(args.crop)
        vf.append(f"crop={int(c['w'])}:{int(c['h'])}:{int(c['x'])}:{int(c['y'])}")
    if args.speed != 1.0:
        vf.append(f"setpts=(PTS-STARTPTS)/{args.speed}")
    vf.append(f"fps={out_fps}")
    ss = ["-ss", str(args.overlay_start)] if args.overlay_start else []
    to = ["-to", str(args.overlay_end)] if args.overlay_end else []
    run(["ffmpeg", "-y", *ss, *to, "-i", args.overlay, "-vf", ",".join(vf), os.path.join(odir, "f%05d.png")])
    ovl_frames = sorted(os.listdir(odir))
    if not ovl_frames:
        sys.exit("Aucune frame d'overlay extraite.")
    if len(ovl_frames) < len(base_frames):
        k = len(ovl_frames)
        ovl_frames = [ovl_frames[i % k] for i in range(len(base_frames))]

    # masque du quad (fixe)
    SS = 4
    mh = Image.new("L", (W * SS, H * SS), 0)
    ImageDraw.Draw(mh).polygon([(x * SS, y * SS) for x, y in dst], fill=255)
    qimg = mh.resize((W, H), Image.LANCZOS)
    if args.feather > 0:
        qimg = qimg.filter(ImageFilter.GaussianBlur(args.feather))
    quad_mask = np.asarray(qimg, dtype=np.float32) / 255.0

    # geometrie de l'overlay
    wq = max(math.dist(dst[0], dst[1]), math.dist(dst[3], dst[2]))
    hq = max(math.dist(dst[0], dst[3]), math.dist(dst[1], dst[2]))
    quad_aspect = args.screen_aspect or wq / hq
    ov0 = Image.open(os.path.join(odir, ovl_frames[0])); ow, oh = ov0.size
    if ow / oh > quad_aspect:
        cw = int(oh * quad_aspect); box = ((ow - cw) // 2, 0, (ow + cw) // 2, oh)
    else:
        ch = int(ow / quad_aspect); box = (0, (oh - ch) // 2, ow, (oh + ch) // 2)
    box_w, box_h = box[2] - box[0], box[3] - box[1]
    s = min(1.0, (wq * 2.0) / box_w)
    tw, th = max(2, int(round(box_w * s))), max(2, int(round(box_h * s)))
    coeffs = perspective_coeffs([(0, 0), (tw, 0), (tw, th), (0, th)], dst)
    white = tuple(int(v) for v in args.white.split(",")) if args.white else None

    # points de suivi + seuil de couleur, appris sur la frame 0 SOUS le pinceau
    tys, txs = contour_samples(M0, W, H)
    ref0 = np.asarray(Image.open(os.path.join(bdir, base_frames[0])).convert("L"), dtype=np.float32)
    in_quad = quad_mask > 0.5
    occ_luma = float(np.median(ref0[M0 & in_quad])) if (M0 & in_quad).any() else float(np.median(ref0[M0]))
    scr = in_quad & ~ndi.binary_dilation(M0, np.ones((25, 25)))
    scr_luma = float(np.median(ref0[scr])) if scr.any() else 255.0
    T = (occ_luma + scr_luma) / 2.0
    print(f"masque peint : {M0.sum()} px | {len(tys)} points de suivi sur le contour")
    print(f"luminance sous le pinceau = {occ_luma:.0f}, ecran = {scr_luma:.0f} "
          f"-> seuil d'extension par la couleur = {T:.0f}")

    shifts, log = [], []
    for i, bf in enumerate(base_frames):
        base = Image.open(os.path.join(bdir, bf)).convert("RGB")
        luma = np.asarray(base.convert("L"), dtype=np.float32)

        dx, dy = (0, 0)
        if args.track > 0 and i > 0:
            dx, dy = track_shift(ref0, luma, tys, txs, args.track)
        shifts.append((dx, dy))
        Mt = shift_bool(M0, dx, dy)

        Ht = shift_bool(holes, dx, dy) if holes.any() else None
        if args.grow > 0:
            k = np.ones((args.grow * 2 + 1, args.grow * 2 + 1))
            Mt = Mt | (ndi.binary_dilation(Mt, k) & (luma < T))   # additif uniquement
            Mt = ndi.binary_closing(Mt, np.ones((5, 5)))
        if Ht is not None:
            Mt = Mt & ~Ht                                          # les trous restent ouverts

        occ = np.asarray(Image.fromarray((Mt * 255).astype(np.uint8))
                         .filter(ImageFilter.GaussianBlur(args.mask_feather)), dtype=np.float32) / 255.0

        ov = Image.open(os.path.join(odir, ovl_frames[min(i, len(ovl_frames) - 1)])).convert("RGB").crop(box)
        if (tw, th) != (box_w, box_h):
            ov = ov.resize((tw, th), Image.LANCZOS)
        arr = np.asarray(ov).astype(np.float32)
        if white:
            arr *= np.array(white, dtype=np.float32) / 255.0
        if args.black_floor:
            arr = args.black_floor + arr * (255.0 - args.black_floor) / 255.0
        warped = Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8)) \
                      .transform((W, H), Image.PERSPECTIVE, coeffs, Image.BICUBIC)

        m = quad_mask * (1.0 - occ)
        before = np.asarray(base, dtype=np.float32)
        base.paste(warped, (0, 0), Image.fromarray((m * 255).astype(np.uint8)))
        after = np.asarray(base, dtype=np.float32)
        # controle : l'occulteur doit rester intact
        core = ndi.binary_erosion(Mt, np.ones((7, 7)))
        log.append(float(np.abs(before[core] - after[core]).mean()) if core.any() else 0.0)

        base.save(os.path.join(cdir, bf))
        if i % 50 == 0:
            print(f"  frame {i}/{len(base_frames)}  suivi=({dx:+d},{dy:+d})")

    dxs = [s[0] for s in shifts]; dys = [s[1] for s in shifts]
    print(f"suivi : dx de {min(dxs):+d} a {max(dxs):+d}, dy de {min(dys):+d} a {max(dys):+d}")
    print(f"controle occulteur : ecart max sur toutes les frames = {max(log):.2f} "
          f"(0 = l'interface n'a jamais debordé sur le trace peint)".encode("ascii", "replace").decode())

    run(["ffmpeg", "-y", "-framerate", str(out_fps), "-i", os.path.join(cdir, "f%05d.png"),
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", str(args.crf),
         "-movflags", "+faststart", "-an", args.out])
    poster = os.path.splitext(args.out)[0] + "-poster.jpg"
    Image.open(os.path.join(cdir, base_frames[0])).save(poster, quality=85)
    shutil.rmtree(tmp, ignore_errors=True)
    print(f"OK -> {args.out} + {poster}")


if __name__ == "__main__":
    main()
