# -*- coding: utf-8 -*-
"""Branche le film sur le kit de marque Wizdi (wizdi-brand-kit) — à lancer une fois par film, depuis le dossier du film.

  python tools/brand.py                      # cherche le kit : --kit, $WIZDI_BRAND_KIT, ~/wizdi-brand-kit, ~/Desktop/…, ~/Documents/…
  python tools/brand.py --kit "D:/wizdi-brand-kit"

Produit (rien n'est inventé, tout vient du kit) :
  assets/logos.js      window.WIZ_LOGOS = { wizplay: "<svg…>", …, wizdi: "<svg…>" }  — tracés Baloo officiels
                       (components/wizWordPaths.json) : « Wiz » en bleu #23A4D8 + suffixe dans la couleur du module
                       (tokens/wizdi-tokens.json) ; window.WIZ_BRAND = couleurs des modules, url, copyright
  assets/owl-3d.webp   le hibou 3D détouré (logos/wizdi-owl-3d.webp) — le seul hibou permis hors du logo
  assets/wizdi-owl.png le hibou PLAT : réservé au logo Wizdi (signature de fin), jamais seul
  assets/fonts/        Fredoka (hébreu) + Baloo (latin), rafraîchies depuis le kit
  build/media/manifest.js  créé vide s'il n'existe pas (les vrais écrans s'ajoutent avec tools/media.py)
"""
import argparse, json, os, shutil, sys

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
WIZ_BLUE = "#23A4D8"
COPYRIGHT = "Copyright © 2026 Wizdi. All rights reserved"


def find_kit(arg):
    home = os.path.expanduser("~")
    cands = [arg, os.environ.get("WIZDI_BRAND_KIT"), os.path.join(home, "wizdi-brand-kit"),
             os.path.join(home, "Desktop", "wizdi-brand-kit"), os.path.join(home, "Documents", "wizdi-brand-kit"),
             os.path.join(home, "OneDrive", "Desktop", "wizdi-brand-kit"), os.path.join(home, "OneDrive", "Bureau", "wizdi-brand-kit")]
    for c in cands:
        if c and os.path.isfile(os.path.join(c, "components", "wizWordPaths.json")):
            return os.path.abspath(c)
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--kit", default=None, help="dossier du kit wizdi-brand-kit")
    ap.add_argument("--root", default=".", help="dossier du film (défaut : dossier courant)")
    a = ap.parse_args()
    kit = find_kit(a.kit)
    if not kit:
        raise SystemExit("Kit de marque introuvable. Clone-le (git clone https://github.com/yoni-wizdi/wizdi-brand-kit ~/wizdi-brand-kit)\n"
                         "ou indique son chemin : python tools/brand.py --kit <chemin>  (ou variable WIZDI_BRAND_KIT).")
    root = os.path.abspath(a.root)
    assets = os.path.join(root, "assets")
    os.makedirs(os.path.join(assets, "fonts"), exist_ok=True)

    paths = json.load(open(os.path.join(kit, "components", "wizWordPaths.json"), encoding="utf-8"))
    tok = json.load(open(os.path.join(kit, "tokens", "wizdi-tokens.json"), encoding="utf-8"))
    mods = tok.get("color", {}).get("modules", {})
    blue = tok.get("color", {}).get("wizBlue", WIZ_BLUE)
    logos, brand = {}, {"wizBlue": blue, "url": "wizdi.school", "copyright": tok.get("copy", {}).get("copyright", COPYRIGHT), "modules": {}}
    for name, p in paths.items():
        key = name.lower()
        if name == "Wizdi":
            logos[key] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{p["vb"]}" role="img" aria-label="Wizdi">'
                          f'<path fill="{blue}" d="{p["wiz"]}"/></svg>')
            continue
        m = mods.get(name)
        if not m:
            print(f"  (couleur absente des tokens pour {name} : ignoré)")
            continue
        logos[key] = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{p["vb"]}" role="img" aria-label="{name}">'
                      f'<path fill="{blue}" d="{p["wiz"]}"/><path fill="{m["main"]}" d="{p["suffix"]}"/></svg>')
        brand["modules"][key] = {"name": name, "main": m["main"], "dark": m.get("dark"), "pastel": m.get("pastel")}
    for name, m in mods.items():   # modules sans tracé (ex. WizLab) : couleurs seulement, logo en repli texte
        brand["modules"].setdefault(name.lower(), {"name": name, "main": m["main"], "dark": m.get("dark"), "pastel": m.get("pastel")})
    with open(os.path.join(assets, "logos.js"), "w", encoding="utf-8") as fh:
        fh.write("/* GÉNÉRÉ par tools/brand.py depuis le kit de marque (components/wizWordPaths.json + tokens) — ne pas éditer. */\n")
        fh.write("window.WIZ_LOGOS = " + json.dumps(logos, ensure_ascii=False) + ";\n")
        fh.write("window.WIZ_BRAND = " + json.dumps(brand, ensure_ascii=False) + ";\n")

    copied = []
    for src, dst in [(("fonts", "fredoka-var-hebrew.woff2"), ("fonts", "fredoka-var-hebrew.woff2")),
                     (("fonts", "baloo-chettan-regular.ttf"), ("fonts", "baloo-chettan-regular.ttf")),
                     (("logos", "wizdi-owl-3d.webp"), ("owl-3d.webp",)),
                     (("logos", "wizdi-owl.png"), ("wizdi-owl.png",))]:
        s = os.path.join(kit, *src)
        if os.path.isfile(s):
            shutil.copyfile(s, os.path.join(assets, *dst)); copied.append("/".join(dst))
        else:
            print("  (absent du kit :", "/".join(src), ")")

    # Wizi de chaque module (combinaison + plastron au vrai logo) et WizBuddy, détourés : assets/owls/<nom>-<pose>.webp
    os.makedirs(os.path.join(assets, "owls"), exist_ok=True)
    for sub in [("references", "wizi", "modules", "poses"), ("references", "wizi", "wizbuddy", "poses")]:
        d = os.path.join(kit, *sub)
        for f in sorted(os.listdir(d)) if os.path.isdir(d) else []:
            if f.endswith(".webp"):
                shutil.copyfile(os.path.join(d, f), os.path.join(assets, "owls", f)); copied.append("owls/" + f)

    man = os.path.join(root, "build", "media", "manifest.js")
    if not os.path.exists(man):
        os.makedirs(os.path.dirname(man), exist_ok=True)
        open(man, "w", encoding="utf-8").write("/* GÉNÉRÉ par tools/media.py */\nwindow.WIZ_MEDIA = {};\n")
    print(f"kit : {kit}")
    print(f"ok -> assets/logos.js ({', '.join(sorted(logos))})")
    print(f"ok -> assets/{', assets/'.join(copied)}")


if __name__ == "__main__":
    main()
