# wizdi-brand-kit — instructions pour Claude Code

Ce dépôt est le kit de marque et de design de Wizdi (studio-wizdi.com) : règles, couleurs, polices,
logos, Wizi (le personnage), composants et skills Claude Code. Il est maintenu par Yoni.
Réponds dans la langue de la personne qui te parle (hébreu ou français).

## Avant tout travail Wizdi

Lis `WIZDI-BRAND.md` en entier : ce sont les règles d'identité obligatoires (hébreu, puis français
détaillé). Pour produire une image, une vidéo, une voix, une page ou un texte, lis aussi
`WIZDI-PRODUCTION.md` : les règles apprises projet après projet. Ce qui revient le plus souvent :

- « Wizdi » toujours en lettres latines, jamais en majuscules, jamais `וויזדי`.
- Logos des modules : « Wiz » en bleu `#23A4D8` + le suffixe dans la couleur du module, depuis
  `logos/wiz/*.svg` ou `components/` (`WizWord.tsx`, `wiz-word.js`), jamais retapés en texte.
- Couleurs : uniquement celles de `tokens/` ; rien d'inventé.
- Hébreu en Fredoka, latin en Baloo (`fonts/`, `tokens/wizdi-tokens.css`).
- Personnage : **Wizi en 3D, en combinaison spatiale**, avec le plastron du module au vrai logo
  (`references/wizi/`, `references/campaign/`). Le hibou plat ne sert que dans le logo.
- WizBuddy, le bot du centre de formation : combinaison blanche nacrée, toujours mignon, jamais d'yeux
  lumineux, casque toujours là (`references/wizi/wizbuddy/`, `logos/wiz/WizBuddy.svg`).
- Vidéo : toujours 3 formats (9:16, 4:5, 16:9), fin sur wizdi.school ; skill `wizdi-motion-senior`.
- Images IA : aucun texte hébreu généré, aucune fausse capture d'interface ; méthode du skill
  `wizdi-visual-studio`. Avant une vidéo, l'image de base se valide avec Yoni.
- Textes fournis par le client : recopiés mot pour mot.

## Plan du dépôt

| Chemin | Contenu |
|---|---|
| `WIZDI-BRAND.md` | les règles d'identité (hébreu puis français) |
| `WIZDI-PRODUCTION.md` | les règles de production : Wizi, WizBuddy, images, vidéo, voix, textes, pages, WizPlan, refus |
| `brand-sheet.html` | la planche de marque : logos animés, palette, polices, composants |
| `PROMPT.md` | les prompts prêts à coller (installer, mettre à jour, auditer, créer) |
| `tokens/` | `wizdi-tokens.css` / `.json` (marque), `wizdi-glass-tokens.css` (style « verre liquide » pastel du hub) |
| `fonts/` | Fredoka (hébreu), Baloo (latin) |
| `logos/` | wordmark Wizdi, hibou plat, logos des Wiz en SVG (les 9 modules + WizBuddy), favicons, Yavne |
| `components/` | `WizWord.tsx` (React + GSAP), `wiz-word.js` (sans dépendance), tracés SVG |
| `references/wizi/` | Wizi seul (`wizi-reference.webp`, la RÉFÉRENCE 1 des prompts), la planche de ses poses, Wizi de chaque module au vrai logo (`modules/`, poses détourées dans `modules/poses/`), WizBuddy (`wizbuddy/`), anciens Wiz (`legacy/`) — voir `references/wizi/README.md` |
| `references/campaign/` | les 6 posters officiels : style, couleur et plastron de chaque module |
| `references/pastel/` | les 12 scènes « pastel aérien » validées |
| `skills/` | les skills Claude Code du design Wizdi (voir `skills/README.md`) |
| `scripts/` | la synchronisation depuis le dépôt du site (Yoni seulement) |

## Installer ou mettre à jour (quand on te le demande)

1. `git pull` dans ce dépôt (ou `git clone https://github.com/yoni-wizdi/wizdi-brand-kit ~/wizdi-brand-kit`
   s'il n'est pas encore là). Si GitHub demande une connexion, laisse la personne se connecter
   elle-même dans la fenêtre qui s'ouvre.
2. Copie chaque dossier de `skills/` dans `~/.claude/skills/` (Windows : `%USERPROFILE%\.claude\skills\`),
   en remplaçant les dossiers du même nom. Ne touche pas aux autres skills déjà présents.
3. Pour les films (skill `wizdi-motion-senior`) : vérifie Python 3.10+, `playwright` + Chromium et
   ffmpeg (`skills/wizdi-motion-senior/engine/README.md`) ; propose d'installer ce qui manque, avec
   l'accord de la personne.
4. Dis combien de skills ont été installés, ce qui manque éventuellement, et qu'il faut redémarrer
   Claude Code pour charger les skills.

## Utiliser le kit dans un autre projet

- Copie `tokens/`, `fonts/`, `logos/`, `components/` dans le projet et importe
  `tokens/wizdi-tokens.css` (les polices y sont appelées en `../fonts/`).
- Dans le projet cible, ces fichiers ne se modifient pas : ils viennent d'ici.

## Ce qu'on ne fait pas dans ce dépôt

- Ne modifie ni les règles, ni les couleurs, ni les logos, ni les références de ta propre initiative.
  Une proposition de changement passe par Yoni : pull request si la personne a les droits,
  sinon un message qui décrit le changement.
- `logos/`, `fonts/`, `components/`, `references/campaign/`, `references/pastel/` et la plupart de
  `skills/` sont régénérés par `scripts/sync-from-wizdi-price.py` : une retouche à la main serait écrasée.
- Dépôt privé : aucun fichier du kit ne se publie ailleurs.
