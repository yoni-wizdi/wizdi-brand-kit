# Wizdi — קיט המותג והעיצוב

> **בעברית** — כל מה שצריך כדי לעבוד כמו ב-studio-wizdi.com: הכללים, הצבעים, הפונטים, הלוגואים,
> Wizi ו-WizBuddy (הדמויות), כל הכללים של הפקת תמונות, סרטונים וקריינות, וכל ה-skills של Claude Code.
> מאגר אחד, תמיד מעודכן, עובד בכל מחשב.
>
> - **התקנה (פעם אחת, בלי לדעת git):** לפתוח את Claude Code ולהדביק את פרומפט ההתקנה מ-`PROMPT.md`
>   (סעיף 1). Claude מוריד את הקיט, מתקין את ה-skills ובודק מה חסר במחשב. בפעם הראשונה ייתכן שייפתח
>   חלון התחברות ל-GitHub.
> - **עדכון:** להדביק את סעיף 2 מ-`PROMPT.md`. כשיוני מעדכן את הקיט, זה כל מה שצריך.
> - **לראות איך זה אמור להיראות:** לפתוח את `brand-sheet.html` בדפדפן.
> - **לעבוד:** הפרומפטים ב-`PROMPT.md` — פרויקט קיים, דף חדש, תמונה עם Wizi, סרטון מושן.
> - **לא משנים את הכללים לבד:** הצעה לשינוי עוברת דרך יוני.

## Ce que c'est

Le kit de marque et de production de Wizdi, en un seul dépôt privé : les règles d'identité, les
règles de production apprises projet après projet, les couleurs, les polices, les logos animés des
Wiz (WizBuddy compris), les personnages (Wizi par module, WizBuddy) et les 38 skills Claude Code qui
ont produit studio-wizdi.com et les films Wizdi. Il remplace les zips envoyés jusqu'ici (kit d'Eden du
08/10, kit d'Eyal du 07/10), fusionnés et complétés. Tout fonctionne depuis n'importe quel PC qui a
cloné le dépôt : aucun chemin ne dépend de la machine de Yoni.

## Sur un nouveau PC

Indispensable :
1. **Claude Code** (application de bureau ou terminal) et **git** (sous Windows, Git for Windows,
   déjà requis par Claude Code).
2. Un **compte GitHub invité** sur ce dépôt (demander à Yoni).

Puis coller le prompt d'installation de `PROMPT.md` (section 1). Claude clone le kit dans
`~/wizdi-brand-kit`, copie les skills dans `~/.claude/skills/` et vérifie le reste. Redémarrer
Claude Code : les skills apparaissent et se déclenchent seuls selon le contexte (ou `/nom-du-skill`).

Pour fabriquer des films (skill `wizdi-motion-senior`) : Python 3.10+, `playwright` + Chromium,
ffmpeg ; commandes exactes dans `skills/wizdi-motion-senior/engine/README.md`. Pour générer des
images, des vidéos ou des voix : les comptes Higgsfield et ElevenLabs (connecteurs à brancher dans
les réglages de Claude, ou clé dans la variable d'environnement `ELEVENLABS_API_KEY`), avec l'accord
de Yoni avant toute dépense.

Mise à jour : section 2 de `PROMPT.md`. Travail au quotidien : sections 3 à 6.

## Contenu

| Dossier / fichier | Contenu |
|---|---|
| `CLAUDE.md` | les consignes que Claude lit en ouvrant ce dépôt |
| `WIZDI-BRAND.md` | **les règles d'identité** (hébreu, puis français détaillé) : nom, logo, logos des Wiz et couleurs, palette, typographie, animation, images, RTL, composants, textes, interdits, check-list |
| `WIZDI-PRODUCTION.md` | **les règles de production** : Wizi et WizBuddy, images générées, vidéo (formats, écriture, contrôle), voix off, textes et rôles, pages, interface WizPlan, directions déjà refusées |
| `brand-sheet.html` | la planche de marque en une page : logos animés dans leur couleur (WizBuddy compris), palette, polices, composants, à faire / à ne pas faire |
| `PROMPT.md` | les prompts prêts à coller : installer, mettre à jour, auditer un projet, nouvelle page, image avec Wizi, film motion |
| `tokens/` | `wizdi-tokens.css` + `.json` (marque : couleurs des modules et de WizBuddy, boutons, chips, carte de verre, `@font-face`) ; `wizdi-glass-tokens.css` (style « verre liquide » pastel du hub) |
| `fonts/` | `fredoka-var-hebrew.woff2` (hébreu, variable 300–700), `baloo-chettan-regular.ttf` (latin) |
| `logos/` | `wizdi-wordmark.svg`, `wizdi-owl.png` (hibou plat, logo seulement), `wizdi-owl-3d.webp`, `yavne-bonus.png`, `wiz/*.svg` (les wordmarks bicolores des 9 modules + `WizBuddy.svg` et `WizBuddy-on-dark.svg`), `favicons/` |
| `components/` | `WizWord.tsx` (React + GSAP, celui du site), `wiz-word.js` (sans dépendance, `data-wiz-word="WizPlay"`), tracés SVG de tous les noms |
| `references/wizi/` | **les personnages** : Wizi seul (RÉFÉRENCE 1 des prompts) et la planche de ses poses ; Wizi de chaque module au vrai logo + poses détourées ; WizBuddy (référence, plaque, avatar, poses détourées) ; anciens WizGen / WizMap / WizLab — détail dans `references/wizi/README.md` |
| `references/campaign/` | les 6 posters officiels, un par module : la référence de style, de couleur et de plastron |
| `references/pastel/` | les 12 scènes « pastel aérien » validées (vraies personnes + Wizi avec le plastron du module) |
| `skills/` | les 38 skills de design et de production (dont le pack complet d'Emil Kowalski, `wizdi-brand`, `wizdi-production` et `wizdi-motion-senior`), à copier dans `~/.claude/skills/` — détail dans `skills/README.md` |
| `scripts/` | la mise à jour depuis le dépôt du site (Yoni seulement) et le traçage des wordmarks depuis Baloo |

## Mettre le kit à jour (Yoni)

Les logos, polices, composants, posters, scènes pastel et la plupart des skills viennent du dépôt
WIZDI-PRICE (studio-wizdi.com) et du compte claude.ai de Yoni :

```bash
pip install pillow fonttools uharfbuzz
python scripts/sync-from-wizdi-price.py --source ~/Desktop/project-partner
```

Puis `git diff`, commit et push. Se modifient à la main ici : les textes (`WIZDI-BRAND.md`,
`WIZDI-PRODUCTION.md`, `CLAUDE.md`, `README.md`, `PROMPT.md`, `brand-sheet.html`, `tokens/`),
`references/wizi/`, `skills/apple-hig/` et `skills/wizdi-motion-senior/`. `skills/wizdi-brand` et
`skills/wizdi-production` sont recopiés depuis les deux fichiers de règles par le script. Les noms que
le site n'a pas tracés (WizBuddy, WizLab) sont tracés depuis Baloo par `scripts/wordmarks.py`, avec la
même convention que le site (`python scripts/wordmarks.py --check` le vérifie sur les 8 autres).

Dépôt privé : il contient les fichiers de la marque, les personnages et des extraits de documentation
tiers (Apple HIG dans `skills/apple-hig`). Ne pas le rendre public.
