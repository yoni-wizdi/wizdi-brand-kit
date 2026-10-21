# -*- coding: utf-8 -*-
"""Rendu image par image de la page du film (Playwright / Chromium headless -> ffmpeg). Tous les chemins sont relatifs
au dossier de la page ; les sorties vont dans <dossier de la page>/out/.

  python tools/render.py stills 1.2 5.5 [--format 9x16] [--scale 0.5]   # images fixes exactes -> out/stills-<fmt>/
  python tools/render.py sheet --step 0.5 [--format 4x5]                 # planche de contrôle -> out/sheet-<fmt>.jpg (À REGARDER)
  python tools/render.py timeline [--format 16x9]                        # -> out/timeline-<fmt>.json (durée, repères sonores, grille)
  python tools/render.py video [--from 0 --to 10] [--out …] [--blur 3]   # -> out/silent-<fmt>.mp4 (H.264, 30 i/s)
  python tools/render.py textscan [--step 0.1]                           # contrôle VERBATIM du texte visible -> out/textscan-<fmt>.txt

Options communes : --page film.html (défaut) · --format 9x16|4x5|16x9|1x1 · --fps 30.
La page expose window.__seek(t) : chaque image est posée à l'instant EXACT ; le rendu est identique d'une machine à l'autre.
Concours (plusieurs rendus sur la même machine) : RENDER_SLOT_DIR=<dossier partagé> RENDER_SLOTS=3 limite le nombre de
navigateurs ouverts en même temps (verrous de fichiers ; chacun attend son tour)."""
import argparse, asyncio, io, json, os, pathlib, re, subprocess, sys, time

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
SIZES = {"9x16": (1080, 1920), "4x5": (1080, 1350), "16x9": (1920, 1080), "1x1": (1080, 1080)}
PAGE, FMT, W, H = None, "9x16", 1080, 1920


class Slot:
    """Créneau de rendu partagé (facultatif) : actif seulement si RENDER_SLOT_DIR est défini. Verrou périmé après 40 min."""
    def __enter__(self):
        self.p = None
        d = os.environ.get("RENDER_SLOT_DIR")
        if not d:
            return self
        n = int(os.environ.get("RENDER_SLOTS", "3"))
        os.makedirs(d, exist_ok=True)
        t0, said = time.time(), False
        while True:
            for i in range(n):
                p = os.path.join(d, f"slot-{i}.lock")
                try:
                    if os.path.exists(p) and time.time() - os.path.getmtime(p) > 2400:
                        os.remove(p)
                    fd = os.open(p, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
                    os.write(fd, f"{os.getpid()} {PAGE}".encode()); os.close(fd); self.p = p
                    if said:
                        print(f"  créneau obtenu après {time.time() - t0:.0f} s", flush=True)
                    return self
                except (FileExistsError, PermissionError):
                    continue
            if not said:
                print("  tous les créneaux de rendu sont pris, on attend son tour…", flush=True); said = True
            time.sleep(3)

    def touch(self):
        if self.p:
            try: os.utime(self.p, None)
            except OSError: pass

    def __exit__(self, *a):
        if self.p:
            try: os.remove(self.p)
            except OSError: pass


def root():
    return os.path.dirname(os.path.abspath(PAGE))


def out_path(*p):
    q = os.path.join(root(), "out", *p)
    os.makedirs(os.path.dirname(q), exist_ok=True)
    return q


def page_url():
    return pathlib.Path(PAGE).resolve().as_uri() + f"?render&format={FMT}"   # file:///C:/… (Windows) ou file:///Users/… (macOS)


async def open_page(pw):
    browser = await pw.chromium.launch(args=["--force-color-profile=srgb", "--disable-gpu-vsync", "--font-render-hinting=none",
                                             "--allow-file-access-from-files", "--autoplay-policy=no-user-gesture-required"])
    page = await browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
    page.on("console", lambda m: print("  [console]", m.text) if m.type in ("error", "warning") else None)
    page.on("pageerror", lambda e: print("  [pageerror]", e))
    await page.goto(page_url())
    await page.wait_for_function("window.__ready === true", timeout=240000)
    return browser, page


async def shot(page, t, q=95):
    await page.evaluate(f"window.__seek({t:.5f})")
    await page.evaluate("new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)))")
    return await page.screenshot(type="jpeg", quality=q, clip={"x": 0, "y": 0, "width": W, "height": H})


async def stills(times, scale, outdir):
    from PIL import Image
    from playwright.async_api import async_playwright
    out = outdir or os.path.join(root(), "out", f"stills-{FMT}")
    os.makedirs(out, exist_ok=True)
    with Slot():
        async with async_playwright() as pw:
            browser, page = await open_page(pw)
            for t in times:
                im = Image.open(io.BytesIO(await shot(page, t)))
                if scale != 1:
                    im = im.resize((int(W * scale), int(H * scale)), Image.LANCZOS)
                p = os.path.join(out, f"t{t:06.2f}.jpg"); im.save(p, quality=90); print("  ", p)
            await browser.close()


async def sheet(step, t0, t1, cols, name):
    from PIL import Image, ImageDraw
    from playwright.async_api import async_playwright
    with Slot():
        async with async_playwright() as pw:
            browser, page = await open_page(pw)
            dur = await page.evaluate("window.__dur")
            t1 = min(t1 or dur, dur); times, t = [], t0
            while t <= t1 + 1e-6:
                times.append(round(t, 2)); t += step
            tw = 216 if W < H else 384
            th = int(tw * H / W); rows = (len(times) + cols - 1) // cols
            S = Image.new("RGB", (cols * tw, rows * th), (20, 20, 20))
            for i, t in enumerate(times):
                im = Image.open(io.BytesIO(await shot(page, t, q=85))).resize((tw, th), Image.LANCZOS)
                d = ImageDraw.Draw(im); d.rectangle([0, 0, 52, 16], fill=(0, 0, 0)); d.text((3, 2), f"{t:5.2f}", fill=(255, 230, 0))
                S.paste(im, ((i % cols) * tw, (i // cols) * th))
            await browser.close()
    p = out_path(name or f"sheet-{FMT}.jpg"); S.save(p, quality=86); print("ok ->", p)


async def timeline(out):
    from playwright.async_api import async_playwright
    with Slot():
        async with async_playwright() as pw:
            browser, page = await open_page(pw)
            tlj = await page.evaluate("window.__timeline")
            await browser.close()
    out = out or out_path(f"timeline-{FMT}.json")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    json.dump(tlj, open(out, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print("ok ->", out, f"({tlj['dur']} s, {len(tlj['sfx'])} repères sonores, {FMT})")


async def video(fps, blur, t_from, t_to, out, crf):
    import numpy as np
    from PIL import Image
    from playwright.async_api import async_playwright
    out = out or out_path(f"silent-{FMT}.mp4")
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    with Slot() as slot:
        async with async_playwright() as pw:
            browser, page = await open_page(pw)
            dur = await page.evaluate("window.__dur")
            t_to = min(t_to or dur, dur); n = int(round((t_to - t_from) * fps))
            ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-framerate", str(fps), "-i", "-",
                                   "-c:v", "libx264", "-preset", "medium", "-crf", str(crf), "-pix_fmt", "yuv420p", "-movflags", "+faststart", out],
                                  stdin=subprocess.PIPE)
            start = time.time()
            for i in range(n):
                t = t_from + i / fps
                if blur > 1:   # obturateur à 180° : N sous-images fondues (flou de mouvement réel, N fois plus long)
                    acc = None
                    for k in range(blur):
                        sub = t + (k / blur - 0.25) * (0.5 / fps)
                        a = np.asarray(Image.open(io.BytesIO(await shot(page, max(sub, 0), q=96))).convert("RGB"), dtype=np.float32)
                        acc = a if acc is None else acc + a
                    frame = (acc / blur + 0.5).astype(np.uint8)
                else:
                    frame = np.asarray(Image.open(io.BytesIO(await shot(page, t, q=96))).convert("RGB"))
                ff.stdin.write(frame.tobytes())
                if i % 90 == 0:
                    slot.touch(); el = time.time() - start
                    print(f"  image {i}/{n}  t={t:6.2f}s  {el:6.1f}s, reste ~{el / max(i, 1) * (n - i):5.0f}s", flush=True)
            ff.stdin.close(); ff.wait()
            await browser.close()
    if ff.returncode:
        raise SystemExit("ffmpeg a échoué")
    print("ok ->", out)


HEB = re.compile(r"[֐-׿]")
LAT = re.compile(r"[A-Za-z]")
STRIP = re.compile(r"^[\s\"'“”„()\[\]!?.,:;־–—-]+|[\s\"'“”„()\[\]!?.,:;־–—-]+$")


async def textscan(step, out):
    """Chaque texte visible, toutes les `step` s : chaque mot hébreu doit être un mot de WIZ_WORDS (pas x: true),
    chaque mot latin un nom de marque, un mot de WIZ_WORDS, wizdi.school, le copyright ou WIZ_FILM.allowText."""
    from playwright.async_api import async_playwright
    with Slot():
        async with async_playwright() as pw:
            browser, page = await open_page(pw)
            dur = await page.evaluate("window.__dur")
            info = await page.evaluate("""() => ({ words: window.WIZ_WORDS || {}, vo: (window.WZ || {}).VO_AT || 0,
                allow: (window.WIZ_FILM || {}).allowText || [] })""")
            seen, sizes, t = {}, [], 0.0
            while t <= dur + 1e-6:
                await page.evaluate(f"window.__seek({t:.4f})")
                for it in await page.evaluate("window.__visibleText()"):
                    for raw in it["text"].split():
                        seen.setdefault(raw, []).append(round(t, 2))
                    if HEB.search(it["text"]):
                        sizes.append((it["size"], round(t, 2), it["text"]))
                t += step
            await browser.close()
    ok_w, bad_w, said_at = set(), set(), {}
    for k, ws in info["words"].items():
        for w in ws:
            s = STRIP.sub("", w["w"])
            (bad_w if w.get("x") else ok_w).add(s)
            if not w.get("x"):
                said_at[s] = min(said_at.get(s, 1e9), info["vo"] + w["t"])
    bad_w -= ok_w
    ok_lat = {"Wiz", "Wizdi", "wizdi.school", "Copyright", "©", "2026", "Wizdi.", "All", "rights", "reserved"}
    for m in ("Play", "Plan", "Chat", "Book", "Box", "Space", "Gen", "Map", "Lab"):
        ok_lat |= {m, "Wiz" + m}
    for a in info["allow"]:
        ok_lat |= {STRIP.sub("", x) for x in a.split()}; ok_w |= {STRIP.sub("", x) for x in a.split()}
    lines, viol = [], 0
    for raw, ts in sorted(seen.items(), key=lambda kv: kv[1][0]):
        s = STRIP.sub("", raw)
        if not s:
            continue
        if s in bad_w:
            viol += 1; lines.append(f"⛔ {ts[0]:6.2f} s  « {raw} » est marqué x: true (mot douteux) : interdit à l'écran")
        elif HEB.search(s) and s not in ok_w:
            viol += 1; lines.append(f"⛔ {ts[0]:6.2f} s  « {raw} » n'est pas un mot du texte validé (WIZ_WORDS)")
        elif LAT.search(s) and not HEB.search(s) and s not in ok_lat and s not in ok_w:
            viol += 1; lines.append(f"⛔ {ts[0]:6.2f} s  « {raw} » (latin) n'est ni une marque ni un mot du texte validé")
        elif s in said_at and ts[0] < said_at[s] - 0.35:
            lines.append(f"⚠  {ts[0]:6.2f} s  « {raw} » affiché {said_at[s] - ts[0]:.2f} s avant d'être dit")
    if sizes:
        mn = min(sizes)
        lines.append(f"plus petit texte hébreu : {mn[0]} px à {mn[1]:.2f} s (« {mn[2][:30]} ») — viser ≥ {int(0.045 * min(W, H))} px")
    out = out or out_path(f"textscan-{FMT}.txt")
    open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("\n".join(lines) or "rien à signaler")
    print(("OK" if not viol else f"{viol} FAUTE(S) DE VERBATIM") + f" -> {out}")
    return viol


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("mode", choices=["stills", "sheet", "video", "timeline", "textscan"])
    ap.add_argument("times", nargs="*", type=float)
    ap.add_argument("--page", default="film.html")
    ap.add_argument("--format", default="9x16", choices=list(SIZES))
    ap.add_argument("--fps", type=int, default=30)
    ap.add_argument("--blur", type=int, default=1)
    ap.add_argument("--from", dest="t_from", type=float, default=0)
    ap.add_argument("--to", dest="t_to", type=float, default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--crf", type=int, default=16)
    ap.add_argument("--scale", type=float, default=0.5)
    ap.add_argument("--step", type=float, default=None)
    ap.add_argument("--cols", type=int, default=None)
    ap.add_argument("--name", default=None)
    a = ap.parse_args()
    PAGE, FMT = a.page, a.format
    W, H = SIZES[FMT]
    if not os.path.exists(PAGE):
        raise SystemExit(f"page introuvable : {os.path.abspath(PAGE)}")
    if a.mode == "stills":
        asyncio.run(stills(a.times, a.scale, a.out))
    elif a.mode == "sheet":
        asyncio.run(sheet(a.step or 0.5, a.t_from, a.t_to, a.cols or (8 if W < H else 5), a.name))
    elif a.mode == "timeline":
        asyncio.run(timeline(a.out))
    elif a.mode == "textscan":
        sys.exit(1 if asyncio.run(textscan(a.step or 0.1, a.out)) else 0)
    else:
        asyncio.run(video(a.fps, a.blur, a.t_from, a.t_to, a.out, a.crf))
