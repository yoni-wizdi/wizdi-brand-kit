# Les skills Claude Code du design Wizdi

> **בעברית** — ה-skills הם «מדריכי שיטה» ש-Claude Code קורא לפני עבודה. ההתקנה נעשית עם הפרומפט
> מסעיף 1 ב-`PROMPT.md` (העתקה של כל תיקייה מכאן אל `~/.claude/skills/`). אחרי הפעלה מחדש של
> Claude Code הם מופיעים ברשימה ומופעלים לבד לפי ההקשר, או ידנית עם `/שם-ה-skill`.

Les 38 skills de design et de production de Yoni, ceux qui ont produit studio-wizdi.com et les films
Wizdi, en une seule version chacun. À copier dans `~/.claude/skills/` (Windows :
`%USERPROFILE%\.claude\skills\`). Aucun ne dépend de la machine de Yoni.

## Wizdi

| Skill | Pour quoi |
|---|---|
| `wizdi-brand` | les règles d'identité de `WIZDI-BRAND.md` : à appliquer sur tout projet, page, visuel ou vidéo Wizdi |
| `wizdi-production` | les règles de production de `WIZDI-PRODUCTION.md` : Wizi, WizBuddy, images, vidéo, voix, textes, pages, WizPlan |
| `wizdi-motion-senior` | **le motion designer senior confirmé** (réseaux sociaux et ed tech) : méthode de bout en bout, grammaire « pop » validée, barème du jury, mode concours de seniors, et le moteur de rendu portable (`engine/` : GSAP → Playwright → ffmpeg, 3 formats) |

## Le pack d'Emil Kowalski (design d'interface et mouvement)

| Skill | Pour quoi |
|---|---|
| `emil-design-eng` | la philosophie d'Emil : finition, composants, décisions d'animation, les détails invisibles |
| `animate` | construire une animation dans le bon ordre : faut-il animer, quoi, quel outil, quelle courbe, quelle durée, comment interrompre, comment sortir |
| `animation-vocabulary` | trouver le nom exact d'un effet décrit avec les mains (« le truc qui rebondit » → *pop in*) |
| `find-animation-opportunities` | repérer ce qui devrait bouger dans une interface, et écarter le reste |
| `improve-animations` | audit des animations d'un projet + plans de correction |
| `review-animations` | relire une animation existante |
| `apple-design` | l'approche d'Apple pour le web : mouvement fluide et physique, gestes, ressorts, matières, typographie |
| `ask-sonner` | Sonner, la bibliothèque de notifications React d'Emil |
| `pick-ui-library` | choisir une bibliothèque de composants |
| `prototype` | prototyper vite |

## Interface et design

| Skill | Pour quoi |
|---|---|
| `frontend-design` | interfaces distinctives, anti-« template IA » : direction esthétique, typographie, composition |
| `ui-ux-pro-max` | la grille de contrôle UX : cibles 44 px, contraste, RTL, mouvement réduit, mobile, pas d'emoji-icônes |
| `apple-hig` | relecture selon les Human Interface Guidelines d'Apple (Liquid Glass, accessibilité, navigation, mode sombre) — c'est l'`apple-design` des anciens zips, renommé pour ne pas heurter celui d'Emil |
| `design-system` | architecture des jetons primitif → sémantique → composant |
| `ui-styling` | shadcn/ui + Tailwind + canvas, catalogue de composants accessibles |
| `design`, `brand`, `banner-design`, `slides` | identité et déclinaisons, voix de marque, bannières et visuels de campagne, présentations HTML |
| `gsap-core`, `gsap-react`, `gsap-timeline`, `gsap-scrolltrigger`, `gsap-plugins`, `gsap-utils`, `gsap-performance`, `gsap-frameworks` | les skills officiels GSAP (DrawSVG pour les logos des Wiz) |

## Images, vidéo, personnage

| Skill | Pour quoi |
|---|---|
| `wizdi-visual-studio` | **le skill de référence** pour toute image ou vidéo Wizdi : blocs ART DIRECTION / SCENE / WIZI / HOLOGRAMS / TEXT / NEGATIVE, Wizi en référence 1, poster du module en référence 2, aucun texte généré |
| `premium-visual-prompts`, `video-ai-creator`, `video-ai-storyboard-il` | les versions précédentes, que `wizdi-visual-studio` réunit ; gardées parce qu'elles sont dans le Claude de Yoni |
| `wizdi-avatar-helper` | **le skill de référence** pour une vidéo où un personnage parle (lip-sync), scène par scène, une seule image de référence verrouillée |
| `avatar-video-creator`, `avatar-lipsync` | ses versions précédentes |
| `video-in-video` | incruster une interface animée dans l'écran d'une photo ou d'une vidéo (le cadre se trace à la main) |

Quand deux skills se recoupent, demander le skill de référence par son nom (`/wizdi-visual-studio`,
`/wizdi-avatar-helper`).

## L'ordre qui marche

1. `frontend-design` pour poser la direction, 2. `wizdi-brand` pour la contraindre à la marque,
3. `gsap-*` + `emil-design-eng` / `animate` pour le mouvement, 4. `ui-ux-pro-max` puis `apple-hig`
et `review-animations` pour relire avant livraison. Pour les visuels : `wizdi-visual-studio`, toujours.

## Ce qui n'est pas ici

- `skill-creator`, `docx`, `pptx`, `xlsx`, `pdf` : déjà intégrés à Claude.
- Les connecteurs (Higgsfield pour les images et vidéos, Figma, Adobe) : à connecter dans les
  réglages de Claude, ce ne sont pas des fichiers.
- `wizdi-film`, `wizdi-corrections`, `wizdi-codex-review` : ils pilotent le générateur de films
  (dépôt privé `wizdi-video-generator`) et ne servent qu'avec lui.
