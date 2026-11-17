# Wizi, WizBuddy et les Wiz : les références de personnages

> **בעברית** — כאן כל הדמויות, בצבעים של פלטת מוצרי Wiz החדשה (28/10): Wizi לבד (REFERENCE 1 בפרומפטים),
> Wizi של כל מודול בחליפה בצבע המודול עם לוחית החזה האמיתית, ו-WizBuddy. לכל תמונה חדשה: REFERENCE 1 =
> הדמות לבד, REFERENCE 2 = Wizi של המודול. הינשופים בצבעים הישנים נמצאים רק ב-`../legacy/`.

| Fichier | Quoi | Usage |
|---|---|---|
| `wizi-reference.webp` | Wizi seul, combinaison bleue, plastron « WIZDI » | **RÉFÉRENCE 1** de tout prompt d'image avec Wizi |
| `wizi-poses.webp` | la planche de toutes ses poses (face, marche, salut, ordinateur, réflexion, rotation), fond transparent | choisir une pose, garder les proportions |
| `modules/<module>.webp` | Wizi de chaque module dans l'armure **recolorée à la nouvelle palette**, plastron au vrai logo : `wizbook` (bleu roi), `wizplan` (violet), `wizplay` (rose), `wizspace` (or), `wizchat` (orange), `wizbox` (vert) | **RÉFÉRENCE 2** pour le plastron et la couleur de l'armure |
| `modules/poses/*.webp` | les poses approuvées du kit général, détourées (fond transparent) | incrustation directe dans une page, une vignette ou un film |
| `wizbuddy/` | WizBuddy, le bot du centre de formation (combinaison blanche nacrée) : référence, plaque, avatar, planche, 3 poses détourées | RÉF 1 = `wizbuddy-reference.webp`, RÉF 2 = `wizbuddy-plate.webp` |

## Les poses de `modules/poses/` (liste du kit général, `kit.py`)

| Fichier | Module | Pose |
|---|---|---|
| `wizbook.webp` · `wizbook-wave.webp` · `wizbook-point.webp` | WizBook | salue (clip du film) · salue · désigne |
| `wizplan.webp` · `wizplan-joie.webp` | WizPlan | déploie un éventail de cartes et désigne · tourne de joie en l'air |
| `wizplay.webp` · `wizplay-joy.webp` · `wizplay-point.webp` | WizPlay | saute sur ses jambes à ressort · joie · désigne |
| `wizchat.webp` · `wizchat-wave.webp` | WizChat | explique comme un professeur particulier · salue |
| `wizspace.webp` · `wizspace-joy.webp` | WizSpace | fait tourner un anneau de tuiles · joie |
| `wizbox-joy.webp` · `wizbox-point.webp` | WizBox | joie · désigne |

**Écartées pour toujours** (yeux qui brillent, regard blasé) : `wizchat-point`, `wizspace-wave`, `wizbook-joy` ;
et le clip `owl-wizbox` (lueur olive après recoloriage). Ne pas les réintroduire.

Les animations de ces hiboux (clips à fond transparent, rafales), les fonds PopBG animés, les logos animés et les
personnages du film השבחה sont sur le kit général en ligne : **https://studio-wizdi.com/kit/** (trop lourds pour ce dépôt).
Les fonds PopBG en image fixe sont dans `../popbg/`.

Rappels (détail dans `WIZDI-PRODUCTION.md`) : toujours le hibou 3D, jamais le hibou plat ; jamais un hibou aux
anciennes couleurs dans une nouvelle création ; le plastron se lit et se vérifie lettre à lettre ; WizBuddy toujours
mignon, jamais d'yeux lumineux, casque toujours là, toujours en pied.

Ce dossier se met à jour à la main (il n'est pas régénéré par `scripts/sync-from-wizdi-price.py`) : les poses viennent
de `media/clips/owl-*/owl-*.png` du kit général (`ops/kit-wizdi-2026-10-29/`).
