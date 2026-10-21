# Wizi, WizBuddy et les Wiz : les références de personnages

> **בעברית** — כאן כל הדמויות: Wizi לבד (REFERENCE 1 בפרומפטים), Wizi של כל מודול עם לוחית החזה
> האמיתית, WizBuddy, והגרסאות הישנות. לכל תמונה חדשה: REFERENCE 1 = הדמות לבד, REFERENCE 2 = הלוחית של המודול.

| Fichier | Quoi | Usage |
|---|---|---|
| `wizi-reference.webp` | Wizi seul, combinaison bleue, plastron « WIZDI » | **RÉFÉRENCE 1** de tout prompt d'image avec Wizi |
| `wizi-poses.webp` | la planche de toutes ses poses (face, marche, salut, ordinateur, réflexion, rotation), fond transparent | choisir une pose, garder les proportions |
| `modules/<module>.webp` | Wizi de chaque module dans son armure, **plastron au vrai logo** (Wiz bleu + suffixe en couleur, Baloo) : `wizplay`, `wizplan`, `wizchat`, `wizbook`, `wizbox`, `wizspace` | **RÉFÉRENCE 2** pour le plastron et la couleur de l'armure du module |
| `modules/poses/<module>-<wave\|point\|joy>.webp` | les mêmes, détourés (fond transparent), trois poses : salut, désigne, joie — sauf WizPlan | incrustation directe dans une page, une vignette ou un film |
| `wizbuddy/wizbuddy-reference.webp` | WizBuddy, le bot du centre de formation : combinaison blanche nacrée, casque à écouteurs blancs, petites ailes irisées, plaque bleu nuit au liseré cyan | RÉFÉRENCE 1 de tout visuel WizBuddy |
| `wizbuddy/wizbuddy-plate.webp` | la plaque « WizBuddy » seule (Wiz bleu, Buddy blanc) | RÉFÉRENCE 2 pour la plaque |
| `wizbuddy/wizbuddy-avatar.webp`, `wizbuddy-sheet.webp` | l'avatar du centre et la planche des trois variantes (la C est retenue) | style et proportions |
| `wizbuddy/poses/wizbuddy-<wave\|point\|joy>.webp` | WizBuddy détouré, trois poses | incrustation directe |
| `legacy/` | anciens visuels de WizGen, WizMap et WizLab, avec des plaques LED en majuscules (« WIZGEN ») : **pas au vrai logo** | ambiance seulement ; ne jamais les publier tels quels, régénérer avec le vrai logo |

Les posters officiels par module sont dans `../campaign/`, les scènes « pastel aérien » dans `../pastel/`.

Rappels (détail dans `WIZDI-PRODUCTION.md` §1–2) : toujours le hibou 3D, jamais le hibou plat ; le
plastron se lit et se vérifie lettre à lettre ; WizBuddy toujours mignon, jamais d'yeux lumineux,
casque toujours là, toujours en pied.

Ce dossier se met à jour à la main (il n'est pas régénéré par `scripts/sync-from-wizdi-price.py`).
