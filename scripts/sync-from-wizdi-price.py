# -*- coding: utf-8 -*-
"""Met le kit à jour depuis le dépôt WIZDI-PRICE (studio-wizdi.com) et les skills du compte de Yoni.
    python scripts/sync-from-wizdi-price.py [--source <WIZDI-PRICE>] [--account-skills <dossier>]
Réservé à Yoni. Régénère logos/, fonts/, components/, references/campaign/, references/pastel/ et
les skills listés dans SKILLS et EMIL. Ne touche pas aux textes écrits à la main (WIZDI-BRAND.md, CLAUDE.md,
README.md, PROMPT.md, brand-sheet.html, tokens/), ni à references/wizi/, ni à skills/apple-hig
(Apple HIG, renommé pour ne pas heurter l'apple-design d'Emil), ni à skills/wizdi-motion-senior (écrit ici).
skills/wizdi-brand et skills/wizdi-production sont recopiés depuis WIZDI-BRAND.md et WIZDI-PRODUCTION.md.
Dépendances : pip install pillow fonttools uharfbuzz
Ensuite : git diff, puis commit + push ; Leead et Chahar font « mets à jour le kit » dans Claude."""
import argparse, glob, json, os, pathlib, re, shutil
from PIL import Image
from wordmarks import wordmark

KIT = pathlib.Path(__file__).resolve().parents[1]
HOME = pathlib.Path(os.path.expanduser("~"))

SKILLS = [
    # interface et design
    "frontend-design", "ui-ux-pro-max", "design-system", "ui-styling", "design", "brand", "banner-design", "slides",
    # mouvement
    "gsap-core", "gsap-react", "gsap-timeline", "gsap-scrolltrigger", "gsap-plugins", "gsap-utils", "gsap-performance",
    "gsap-frameworks",
    # images, vidéo, personnage (skills du compte de Yoni)
    "wizdi-visual-studio", "premium-visual-prompts", "video-ai-creator", "video-ai-storyboard-il",
    "wizdi-avatar-helper", "avatar-video-creator", "avatar-lipsync", "video-in-video",
]
# le pack d'Emil Kowalski, pris uniquement dans le compte claude.ai (un autre apple-design traîne sur une branche)
EMIL = ["emil-design-eng", "animate", "animation-vocabulary", "find-animation-opportunities", "improve-animations",
        "review-animations", "apple-design", "ask-sonner", "pick-ui-library", "prototype"]
FROZEN = ["apple-hig"]  # versionné ici, jamais écrasé

MODULES = {"WizPlay": "#FF5FA2", "WizPlan": "#F28C28", "WizChat": "#7B5CF0", "WizBook": "#15A19E", "WizBox": "#C9742E",
           "WizSpace": "#C13BC9", "WizGen": "#3ED98A", "WizMap": "#38C6FF", "WizLab": "#F06ABC",
           "WizBuddy": "#1E1B4B"}  # WizBuddy : « Buddy » bleu nuit sur fond clair, blanc sur sa plaque (films du centre)
EXTRA_WORDS = ["WizLab", "WizBuddy"]  # pas tracés sur le site : tracés ici depuis Baloo (scripts/wordmarks.py)
WIZ_BLUE = "#23A4D8"


def account_skills_dir():
    """Les skills téléversés sur claude.ai, en cache local du Claude desktop (le plus récent)."""
    found = glob.glob(str(HOME / "AppData/Local/Claude-Data/*/local-agent-mode-sessions/skills-plugin/*/*/skills"))
    return pathlib.Path(max(found, key=lambda p: os.path.getmtime(p))) if found else None


def fresh(d):
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    return d


ap = argparse.ArgumentParser()
ap.add_argument("--source", default=str(HOME / "Desktop/project-partner"), help="clone local de WIZDI-PRICE")
ap.add_argument("--account-skills", default=None, help="dossier des skills du compte claude.ai")
args = ap.parse_args()
ROOT = pathlib.Path(args.source)
if not (ROOT / "src/assets/logos/wizWordPaths.ts").exists():
    raise SystemExit(f"WIZDI-PRICE introuvable : {ROOT}")

# ── 1. tracés des wordmarks → composants ────────────────────────────────────
comp = fresh(KIT / "components")
ts = (ROOT / "src/assets/logos/wizWordPaths.ts").read_text(encoding="utf-8")
paths = json.loads(re.search(r"=\s*(\{.*\});?\s*$", ts, flags=re.S).group(1))
w = (ROOT / "src/assets/logos/wizdiWordmarkPath.ts").read_text(encoding="utf-8")
wizdi_vb = re.search(r'WIZDI_VIEWBOX = "([^"]+)"', w).group(1)
wizdi_path = re.search(r'WIZDI_PATH = "([^"]+)"', w).group(1)
paths["Wizdi"] = {"wiz": wizdi_path, "suffix": "", "vb": wizdi_vb}
shutil.copy(ROOT / "src/assets/fonts/baloo-chettan-regular.ttf", comp / "_baloo.ttf")
for name in EXTRA_WORDS:
    if name not in paths:
        paths[name] = wordmark(name, font=comp / "_baloo.ttf")
(comp / "_baloo.ttf").unlink()
(comp / "wizWordPaths.json").write_text(json.dumps(paths, ensure_ascii=False), encoding="utf-8")
js = (KIT / "scripts/templates/wiz-word.template.js").read_text(encoding="utf-8")
(comp / "wiz-word.js").write_text(js.replace("/*__PATHS__*/{}/*__END__*/", json.dumps(paths, ensure_ascii=False)), encoding="utf-8")
shutil.copy(ROOT / "src/components/landing/WizWord.tsx", comp / "WizWord.tsx")
for f in ["wizWordPaths.ts", "wizdiWordmarkPath.ts"]:
    shutil.copy(ROOT / "src/assets/logos" / f, comp / f)

# ── 2. logos : wordmarks SVG bicolores, bitmaps, favicons ───────────────────
logos = fresh(KIT / "logos")
(logos / "wiz").mkdir()
for name, color in MODULES.items():
    d = paths[name]
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{d["vb"]}" role="img" aria-label="{name}">'
           f'<path fill="{WIZ_BLUE}" d="{d["wiz"]}"/><path fill="{color}" d="{d["suffix"]}"/></svg>')
    (logos / "wiz" / f"{name}.svg").write_text(svg, encoding="utf-8")
    if name == "WizBuddy":
        (logos / "wiz" / "WizBuddy-on-dark.svg").write_text(svg.replace(f'fill="{color}"', 'fill="#FFFFFF"'), encoding="utf-8")
(logos / "wizdi-wordmark.svg").write_text(
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{wizdi_vb}" role="img" aria-label="Wizdi"><path fill="{WIZ_BLUE}" d="{wizdi_path}"/></svg>', encoding="utf-8")
for f in ["wizdi-owl.png", "yavne-bonus.png", "wizdi-wordmark.png"]:
    shutil.copy(ROOT / "src/assets/logos" / f, logos / f)
owl3d = Image.open(ROOT / "src/assets/logos/wizdi-owl-3d.png").convert("RGBA"); owl3d.thumbnail((1024, 1024))
owl3d.save(logos / "wizdi-owl-3d.webp", quality=88, method=6)
shutil.copytree(ROOT / "public/favicons", logos / "favicons")

# ── 3. polices ──────────────────────────────────────────────────────────────
fonts = fresh(KIT / "fonts")
for f in ["fredoka-var-hebrew.woff2", "baloo-chettan-regular.ttf"]:
    shutil.copy(ROOT / "src/assets/fonts" / f, fonts / f)

# ── 4. références : posters CAMPAIGN réduits, scènes pastel ─────────────────
camp = fresh(KIT / "references/campaign")
for f in sorted((ROOT / "CAMPAIGN").iterdir()):
    if f.suffix.lower() != ".jpeg":
        continue
    im = Image.open(f).convert("RGB"); im.thumbnail((1400, 1400))
    im.save(camp / f"{f.name.split('_')[0]}.jpg", quality=82, optimize=True)
pastel = fresh(KIT / "references/pastel")
for f in sorted((ROOT / "public/wiz/assets/pastel").glob("*.webp")):
    shutil.copy(f, pastel / f.name)

# ── 5. skills : projet → ~/.claude/skills → compte claude.ai ────────────────
acct = pathlib.Path(args.account_skills) if args.account_skills else account_skills_dir()
sources = [ROOT / ".claude/skills", HOME / ".claude/skills"] + ([acct] if acct else [])
skills_dir = KIT / "skills"
missing = []
for s in SKILLS + EMIL:
    src = next((d / s for d in (([acct] if acct else []) if s in EMIL else sources) if (d / s / "SKILL.md").exists()), None)
    if src is None:
        missing.append(s); continue
    if (skills_dir / s).exists():
        shutil.rmtree(skills_dir / s)
    shutil.copytree(src, skills_dir / s, ignore=shutil.ignore_patterns("__pycache__", "*.pyc", ".git", "node_modules"))
rules = (KIT / "WIZDI-BRAND.md").read_text(encoding="utf-8")
fresh(skills_dir / "wizdi-brand")
(skills_dir / "wizdi-brand" / "SKILL.md").write_text(
    "---\nname: wizdi-brand\ndescription: Règles de marque et de design Wizdi — nom, logo, logos des Wiz et leurs couleurs, "
    "palette, typographie Fredoka/Baloo, animation des wordmarks, Wizi (le personnage 3D), images, RTL, composants. "
    "À appliquer sur tout projet, page, visuel ou vidéo Wizdi.\n---\n\n"
    "> Les chemins cités (`logos/`, `tokens/`, `references/`…) sont relatifs au dépôt `wizdi-brand-kit`, cloné dans `~/wizdi-brand-kit`.\n\n"
    + rules, encoding="utf-8")
prod = (KIT / "WIZDI-PRODUCTION.md").read_text(encoding="utf-8")
fresh(skills_dir / "wizdi-production")
(skills_dir / "wizdi-production" / "SKILL.md").write_text(
    "---\nname: wizdi-production\ndescription: Règles de production Wizdi apprises projet après projet — Wizi et WizBuddy "
    "(armure, plastron, références), images générées (personnes israéliennes, école laïque, ordinateur jamais tablette, "
    "aucun texte), vidéo (3 formats 9:16 / 4:5 / 16:9, wizdi.school, −14 LUFS, règle d'Eyal pour l'interface), voix off "
    "hébreu (ElevenLabs, nikoud, Wiz Plène), textes et rôles, pages et RTL, interface WizPlan, directions refusées. "
    "À appliquer avec wizdi-brand dès qu'on produit une image, une vidéo, une voix, une page ou un texte Wizdi.\n---\n\n"
    "> Les chemins cités (`logos/`, `references/`…) sont relatifs au dépôt `wizdi-brand-kit`, cloné dans `~/wizdi-brand-kit`.\n\n"
    + prod, encoding="utf-8")

# ── 6. bilan ────────────────────────────────────────────────────────────────
known = set(SKILLS) | set(EMIL) | set(FROZEN) | {"wizdi-brand", "wizdi-production", "wizdi-motion-senior"}
extra = sorted(d.name for d in skills_dir.iterdir() if d.is_dir() and d.name not in known)
print("source :", ROOT)
print("skills du compte :", acct or "introuvables")
for d in sorted(p for p in KIT.iterdir() if p.name not in {".git"}):
    files = [f for f in d.rglob("*") if f.is_file()] if d.is_dir() else [d]
    print(f"  {d.name:<20} {len(files):>4} fichiers  {sum(f.stat().st_size for f in files)/1e6:6.2f} Mo")
if missing:
    print("skills introuvables (copie existante gardée) :", missing)
if extra:
    print("skills hors liste (à retirer ou à ajouter à SKILLS) :", extra)
