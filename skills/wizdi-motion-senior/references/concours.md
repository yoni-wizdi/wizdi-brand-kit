# Mode « concours de seniors » — N motion designers en parallèle + un jury

Généralisé des concours du 15/10/2026 (8 seniors sur les vidéos des actrices ; 3 seniors sur le film WizBox mapping).
Principe : **plusieurs versions complètes du même film**, même matière (narration, mots, vrais médias, règles), chacun
avec SON montage, SA musique, SES bruitages et SA lecture du pop. Un jury classe ; **Yoni tranche**.

## Quand le proposer

Film important (lancement, campagne, film d'un outil), direction pas encore figée, ou demande explicite (« concours »,
« plusieurs versions », « fais-les concourir »). Coût : N fois le temps de rendu ; sans ElevenLabs le coût monétaire est nul.

## 1. Préparer la base commune (la session principale, avant de lancer qui que ce soit)

- `<projet>/concours/_base/` = une copie du moteur (`engine/`) avec : `python tools/brand.py`, les vrais médias
  (`tools/media.py add …`), `words.js` validé (+ `vo/narration.wav` ou la piste du montage), et un `film.js` minimal.
- `_base/KIT.md` (gabarit ci-dessous) et un brief par senior `briefs/<x>.md`.
- Un dossier `_slots/` partagé pour les créneaux de rendu (`RENDER_SLOT_DIR`).
- Vérifier soi-même que la base rend (`python tools/make.py --formats 9x16` sur 3 s) avant de lancer les seniors.

## 2. Rendre les directions VRAIMENT différentes

Plusieurs directions = des mondes différents (concept, rythme, genre musical, tempo, tonalité, palette sonore), jamais
le même moteur repeint. Imposer à chaque senior un **couloir musical** distinct, par exemple :
chiptune-pop 8-bit ~128 BPM majeur · house-pop four-on-the-floor ~122 BPM · funk-pop cuivres ~112 BPM ·
marimba/ukulélé ~106 BPM · électro pincée basse synthé ~118 BPM · pop orchestrale pizzicati ~100 BPM · hip-hop léger ~92 BPM ·
afro-pop percussions ~110 BPM. Et une **lecture du pop** distincte, par exemple : « pop cinétique » (fidèle, poussée au
meilleur) · « papier pop » (les vraies pages se comportent comme des feuilles : volent, s'empilent, tampon ✓) ·
« carte / grille » (le récit suit la grammaire de l'objet du produit). Interdit dans toutes : fausses données (jamais remplir
une vraie feuille avec de fausses notes), fausse interface, styles refusés (SKILL.md).

## 3. Gabarit de KIT.md (commun à tous les seniors)

```markdown
# Kit du concours — <film> (<date>)
Tu es l'un des <N> seniors du motion design (monteur, motion designer, sound designer, publicité de produits digitaux).
Tu livres UNE version complète et finie du film, en <format(s)>, dans le style pop Wizdi. Un jury classe ; Yoni tranche.
La démonstration qui marche est dans `../_base/` : lis-la d'abord, puis fais mieux.

## Déjà fait (base commune, NE PAS MODIFIER)
| Pièce | Où | Quoi |
| Mots validés | `../_base/words.js` | WIZ_WORDS : chaque mot du texte VALIDÉ avec son instant ; x: true = interdit à l'écran |
| Voix | `../_base/vo/narration.wav` | définitive |
| Vrais médias | `../_base/build/media/` + `manifest.json` | les seuls écrans permis (liste + ce qu'ils montrent) |
| Moteur | `../_base/` (core.js, pop.js, tools/) | copie-le dans ton dossier ; modifie TA copie |

## Ton dossier : `<x>/` (tu n'écris QUE là)
film.html · film.js · style.js · style.css · mix.json · NOTE.md (intention en 5–10 lignes, genre/BPM/tonalité, palette
sonore, instants de début de chaque scène) · build/ · out/

## Fabriquer
python tools/render.py sheet --step 0.5          # planche : tu la REGARDES (outil Read)
python tools/render.py stills 0.3 1.2 --scale 1  # images exactes
python tools/render.py textscan                  # 0 faute de verbatim exigée
python tools/make.py --jobs 2                    # au plus <3–4> rendus complets ; réglages sur planches
python tools/check.py out/<nom>-9x16-HD.mp4
Créneaux partagés : RENDER_SLOT_DIR=../_slots RENDER_SLOTS=3.

## Le son, partie intégrante de la note
Voix parfaitement intelligible ; musique de TON couloir, calée sur tes coupes (les coupes tombent sur les temps) et baissée
sous la voix ; bruitages calés sur les mots et les apparitions ; −14 LUFS, crête ≤ −1 dBTP.
<Si ElevenLabs autorisé : plafonds par senior, ex. musique 3 générations ≤ 60 s, bruitages 30 générations.>

## Les règles (sine qua non) — voir SKILL.md, à recopier ici en entier
## Ce que le jury notera (sur 10 chacun) — voir la grille ci-dessous, à recopier ici
## Interdits : écrire hors de ton dossier · git (ni commit, ni push) · déploiement · rien en ligne · générations non prévues
Ta réponse finale, en français, 15 lignes au plus : ce que tu as fait, tes choix forts, ce que tu sais imparfait.
```

Brief par senior (`briefs/<x>.md`) : l'outil cité et sa couleur, les plans/scènes (tableau : id · de → à · ce qu'on voit ·
ce qui est dit VERBATIM · à savoir), les vrais médias de l'outil (clé · quoi · taille · images), son couloir musical, sa
lecture du pop, les pièges connus (ex. « box-step1 affiche « שלושה צעדים » : ne pas l'utiliser »).

## 4. Lancer

Avec l'outil Agent : **un message, N appels en parallèle** (`subagent_type: "general-purpose"`), chacun avec un prompt
court : « Lis `<chemin>/_base/KIT.md` puis `<chemin>/briefs/<x>.md`. Tu es le senior <x>. Livre ta version finie dans
`<chemin>/<x>/`. » Ne pas recopier tout le kit dans le prompt : le senior le lit. Pendant qu'ils travaillent, ne rien
inventer de leurs résultats ; attendre les notifications.

## 5. Le jury (un agent, après la fin de TOUS les seniors)

Prompt : « Lis `<chemin>/_base/KIT.md` et `<chemin>/JURY.md`. Tu es le jury. Écris uniquement dans `<chemin>/jury/`. »

Gabarit de JURY.md :

```markdown
# Cahier du jury — <film>
Tu es le jury : directeur de création senior (motion design, montage, sound design, publicité de produits digitaux),
exigeant et juste. Tu classes les <N> versions ; Yoni tranche.

## Pour chaque version
- out/<nom>-9x16-HD.mp4 (la couverture tient 0,2 s en tête) et NOTE.md ;
- l'accroche : extrais toi-même des images de 0 à 2,2 s toutes les 0,1 s (ffmpeg) et regarde-les ;
- le film entier : une image toutes les 0,5 s + gros plans pleine taille sur chaque moment de texte et d'écran ;
- le son : python tools/check.py <mp4> (sonie, crête, noirs) ; transcription (--scribe si autorisé) comparée à words.js :
  la voix doit être intégralement intelligible ; stems (build/stem-*.wav : niveaux, présence, voix vs musique dans 1–4 kHz) ;
  les coupes tombent-elles sur les temps (BPM annoncé dans NOTE.md, instants des changements de plan) ?
- les règles une par une — texte à l'écran MOT À MOT (python tools/render.py textscan dans le dossier du senior + œil) ;
  Wizdi et noms d'outils en latin ; aucun écran hors des vrais médias ; règle d'Eyal ; fin = logo officiel + wizdi.school +
  Copyright © 2026 Wizdi. All rights reserved ; visage jamais caché pendant qu'on parle ; aucun noir non couvert ; RTL.

## Barème (sur 10 chacun, total sur 60)
1. Accroche des 2 premières secondes · 2. Mise en valeur du produit / clarté du parcours (vrais écrans, au bon mot,
règle d'Eyal) · 3. Montage et coupes (rythme, temps morts, raccords) · 4. Son et synchronisation musicale ·
5. Lisibilité (taille, contraste, temps de lecture, RTL) · 6. Respect des règles.
Une faute de verbatim, une fausse interface ou un noir non couvert PLAFONNE le film à 30/60 (dire où : instant et image).

## Ce que tu rends (dans jury/ uniquement)
- results.json : [{ "version": "<x>", "scores": {"hook", "product", "edit", "sound", "legibility", "rules"}, "total", "rank",
  "verdict": "une phrase", "strengths": [], "weaknesses": [], "fixes": ["correction précise, avec l'instant"],
  "violations": ["instant — ce qui ne va pas"] }] trié par rang ;
- RESULTATS.md : classement, une fiche par film (français), et en tête les 3 corrections qui feraient le plus monter chaque film.
Sois concret, cite des instants (« 0:07,4 »). Pas de complaisance : un 9/10 se mérite. Le son se juge sur mesures et
spectres (dis-le) ; un humain doit encore l'écouter.
Interdits : modifier les films ou les dossiers des seniors, git, mise en ligne, toute génération.
```

## 6. Après le jury

Présenter à Yoni : le classement, les 3 forces / 3 défauts de chaque film, les corrections qui feraient gagner, et une
page de relecture (lecteurs côte à côte, logo + nom de la plateforme + format au-dessus de chaque lecteur). Ne rien
publier : ce sont souvent de vraies personnes. Appliquer ensuite les corrections du jury au film choisi (ou fusionner les
meilleures idées) et refaire `check.py` + `textscan` avant livraison.
