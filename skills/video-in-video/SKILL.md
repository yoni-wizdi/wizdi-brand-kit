---
name: video-in-video
description: >
  Incruster une vidéo dans une zone d'une autre vidéo ou d'une photo (interface
  dans un écran de laptop/TV/projecteur, screen replacement, écran dans écran).
  Le POINT CLÉ : l'utilisateur délimite lui-même le quad (4 coins) avec un outil
  HTML interactif (loupe pixel-perfect + scrub vidéo) — on ne devine JAMAIS la
  zone automatiquement. Utiliser dès que : « vidéo dans une vidéo », « incruste
  l'interface dans l'écran », « mets la plateforme dans le laptop », « screen
  replacement », « la démo doit tourner dans l'écran de la photo/vidéo »,
  placement d'un contenu animé dans un écran filmé ou généré. PROPOSER ce skill
  spontanément dans tout cas similaire de placement vidéo-dans-vidéo.
---

# Vidéo dans vidéo — quad délimité par l'utilisateur

Technique rodée sur le projet Wizdi (hero /wizchat) après l'échec des détections
automatiques du quad (fits pollués par les reflets, bords sombres = trous,
« l'interface déborde du laptop »). **La leçon : l'humain marque les 4 coins,
la machine fait le reste.**

## Vue d'ensemble (5 étapes)

1. **Vidéo de base** — filmée OU générée depuis une photo (i2v, caméra verrouillée).
2. **Outil quad-picker** — page HTML autonome envoyée à l'utilisateur ; il marque
   les 4 coins de la dalle et me colle le JSON.
3. **Contrôle de stabilité** — vérifier que le quad reste valable sur toute la durée.
4. **Compositing** — warp perspective frame par frame (script fourni).
5. **Validation** — montrer le résultat AVANT toute intégration. Max 1 round.

## Étape 1 — Vidéo de base

- Si on part d'une **photo** (cas fréquent) : i2v avec `start_image`
  (Higgsfield : `seedance_2_0` — ⚠️ `seedance_2_5` refuse start_image en t2v ;
  un `preset_recommendation` peut s'interposer → relancer avec `declined_preset_id`).
- Prompt : **caméra verrouillée obligatoire** — « Locked-off static camera, no zoom,
  no pan, no drift » + « the screen content stays exactly as in the start frame » +
  l'appareil « stays perfectly still ». Les mouvements humains (taper au clavier,
  micro-mouvements de tête) sont OK : c'est l'ÉCRAN qui ne doit pas bouger.
  ⚠️ **La formule polie ne suffit pas toujours** (cas réel 2026-08-23 : push-in lent
  malgré « locked-off static camera », diff zone écran 3,5). Formule qui a tenu :
  « **Absolutely static locked-off tripod shot, CCTV-style fixed framing: zero camera
  movement of any kind - no push-in, no zoom, no pan, no tilt, no drift, no parallax,
  no reframing, no breathing. The composition stays pixel-identical from the first
  frame to the last frame.** » → diff 1,6-1,8. Mesurer AVANT de continuer (étape 3) :
  seuil ~2 sur la zone du futur quad, et bandes de bord constantes dans le temps.
- Idéal : l'écran de départ affiche une **couleur unie ou un contenu neutre**
  (facilite le contrôle visuel, aucun besoin de masque).

## Étape 2 — L'outil quad-picker (l'utilisateur délimite)

Templates dans `assets/` (autonomes, tout est embarqué en data URI) :
- `quad-picker-video-template.html` — pour marquer sur une **vidéo** : poignées +
  loupe ×8 + **barre de scrub** pour vérifier le cadre sur toute la durée.
  Placeholders : `__TITLE__`, `__KEY__` (clé localStorage), `__VIDEOSRC__`
  (data URI `data:video/mp4;base64,...` d'un proxy léger, ou chemin relatif).
- `quad-picker-image-template.html` — pour une **photo**. Placeholders :
  `__TITLE__`, `__KEY__`, `__IMGW__`, `__IMGH__`, `__IMGDATA__`.
- `overlay-picker-template.html` — **l'utilisateur choisit AUSSI le contenu** :
  quelle partie de l'overlay montrer (rectangle de crop verrouillé à l'aspect de
  la dalle, `__ASPECT__`), quel segment temporel (IN/OUT) et la vitesse (liée :
  `speed = (out−in)/durée_base`, menu vitesse qui cale OUT, aperçu en boucle à la
  vitesse réelle via playbackRate). Placeholders : `__TITLE__`, `__KEY__`,
  `__VIDEOSRC__`, `__ORIGW__`, `__ORIGH__`, `__ASPECT__`, `__BASEDUR__`.
  Le JSON rendu est en pixels de la vidéo ORIGINALE (conversion proxy→original
  faite par l'outil). À proposer dès que l'utilisateur dit « ce n'est pas la bonne
  partie de la vidéo » ou veut régler la vitesse lui-même.

Préparation (PowerShell) :
```powershell
# proxy léger pour l'outil vidéo (l'original peut être lourd)
ffmpeg -y -i base.mp4 -vf scale=960:-2 -crf 30 -an proxy.mp4
$b64 = [Convert]::ToBase64String([IO.File]::ReadAllBytes("proxy.mp4"))
$tpl = [IO.File]::ReadAllText("quad-picker-video-template.html")
$out = $tpl.Replace("__VIDEOSRC__","data:video/mp4;base64,$b64").Replace("__TITLE__","Délimitation écran").Replace("__KEY__","quad-monprojet")
[IO.File]::WriteAllText("quad-picker.html",$out,(New-Object System.Text.UTF8Encoding $false))
```
⚠️ Si le proxy est réduit (ex: 960px pour une base 1280px), **remultiplier les
coordonnées reçues par le facteur d'échelle** avant compositing.
Envoyer le fichier via SendUserFile (display attach) + mode d'emploi court :
molette = zoom, glisser = déplacer, flèches = ±1px, scrub = vérifier, bouton copier.

## Étape 3 — Contrôle de stabilité (avant de composer !)

```powershell
ffmpeg -y -i base.mp4 -vf "select='eq(n\,0)'" -frames:v 1 first.png
ffmpeg -y -sseof -0.2 -i base.mp4 -frames:v 1 last.png
```
Comparer la zone du quad entre first/mid/last (diff numpy sur le rect englobant).
- Diff moyenne < ~2 : quad fixe OK (réf. : 1,15 sur le hero David).
- Diff élevée : l'écran bouge → quad fixe interdit ; soit régénérer la base avec
  un prompt plus strict, soit tracking par frame (hors scope de ce skill).

## Étape 3 bis — L'OCCULTEUR (quelque chose passe DEVANT l'écran)

Dès qu'un objet masque une partie de la dalle (une tête, une main, une épaule), le
warp seul peint l'interface PAR-DESSUS. Même leçon que pour le quad : **l'utilisateur
peint l'occulteur, on ne le détecte pas.** (Cas réel : hero /wizchat 2026-08-18 — la
matte par seuil de luminance a été rejetée d'un mot, « la tête est mal découpée ».)

1. **`assets/mask-brush-template.html`** (construit par `assets/build_maskbrush.py`) :
   pinceau + gomme, taille au clavier `[` `]`, `E` = gomme, molette = zoom, Ctrl+Z,
   scrub pour vérifier sur toute la durée, contour du quad en pointillé (seul
   l'intérieur compte). Placeholders : `__VIDEOSRC__`, `__TITLE__`, `__KEY__`,
   `__W__`, `__H__`, `__QUAD__`. Le rendu est un JSON compact de **traits**
   (`{r, e, p:[[x,y],…]}`) et non un bitmap : quelques centaines de nombres,
   collables dans le chat.
2. Consignes à donner : déborder d'une dizaine de px (l'occulteur bouge), et
   **laisser libres les zones translucides** (verre de lunettes) — ce qui n'est pas
   peint laisse voir l'interface, et c'est ça qui rend le plan crédible.
3. **`assets/composite-quad-brush.py`** rejoue les traits (épaisseur 2r, bouts et
   jointures ronds, gomme = mise à zéro) puis **SUIT** le masque :
   - `--track N` : translation mesurée par écart absolu minimal sur la **bande de
     contour** du masque. ⚠️ NE PAS utiliser la corrélation de phase sur une fenêtre
     large : un écran lisse n'a pas de texture, la corrélation s'accroche au grain et
     sort des décalages fantaisistes. Vérifier que le suivi ne **sature pas** la limite
     (`dx` collé à `−N` → élargir) et que la courbe est lisse (saut ≤ 2-3 px entre
     frames consécutives ; au-delà = faux appariement).
   - `--grow N` : extension par la couleur, **purement additive** (n'ajoute que ce qui
     est plus sombre que le seuil appris sous le pinceau) → le tracé n'est jamais rogné.
     Indispensable : un occulteur n'est pas rigide (sur ce hero, cheveux 17 px contre
     joue 3 px, donc une seule translation ne peut pas coller partout).
   - `--protect-holes N` : les trous laissés volontairement dans le tracé (le verre)
     sont exclus de l'extension, sinon elle les referme (elle y attrape cils et sourcils).
4. **Contrôles chiffrés AVANT de montrer** (ne pas juger à l'œil sur une vignette —
   erreur commise puis corrigée dans ce chantier) :
   - écart base→composite **sur le tracé peint** = 0,00 (sinon l'interface déborde) ;
   - ⚠️ ce contrôle NE SUFFIT PAS : il ignore la bande entre le tracé et le bord du
     quad. **SCAN DE FUITE obligatoire sur TOUTE la durée** (pas la 1ʳᵉ frame) :
     extraire ~24 frames base+composite, et compter par frame les pixels sombres de
     la base (`luma<90`) devenus nettement plus clairs (`+35`) dans la zone
     occulteur↔bord du quad. Cas réel (hero /wizchat 19/08) : frame 1 propre,
     **fuite max 522 px à la frame 22** (le suivi décale le masque, un liseré
     d'interface apparaît sur les cheveux) → visible, rejeté par le client.
     Remède : élargir `--grow` (8→22 a suffi : fuite 0 px sur toute la durée) ;
   - taille du masque stable d'une frame à l'autre, sinon ça scintille.
   💡 Mieux : quand c'est possible, **régénérer une base où RIEN ne passe devant
   l'écran** (over-shoulder avec écart franc) — plus d'occulteur du tout, et les
   changements d'interface ultérieurs se font en une seule commande.

⚠️ Si le masque du quad porte un `--feather`, l'occulteur doit couvrir l'anneau de
fondu jusqu'à alpha quasi nul, sinon il reste **un liseré clair de 1-2 px qui trace le
contour du quad** en travers de l'occulteur.

## Étape 3 ter — LIVE COMPOSER : l'utilisateur règle en voyant le rendu final

Le plus gros gain de temps du chantier (créé 2026-08-19). Au lieu de choisir à
l'aveugle puis attendre 4 min un composite, l'utilisateur voit **l'overlay déjà
incrusté dans le quad, en temps réel**, et règle tout :

`assets/live-composer-template.html` + `assets/build_livecomposer.py`
```bash
python build_livecomposer.py base_proxy.mp4 ov_proxy.mp4 COMPOSER-<projet>-<date>.html   "titre" cle_localstorage 1248 1664 1920 1080 8.0417 164.27 '{"tl":[...],...}'
```
- Rendu : la base en fond + l'overlay dans un wrapper `overflow:hidden` transformé
  par **homographie → `matrix3d` CSS** (résolue en JS par Gauss-Jordan 8×8). Aucune
  peinture par frame, donc fluide.
- Réglages : IN/OUT, **vitesse de la base** (allonge la boucle donc ralentit
  l'overlay), luminosité de l'écran, cadrage (rect draggable verrouillé à l'aspect).
- Synchro : la base boucle à `playbackRate = baseRate` ; l'overlay suit à
  `playbackRate = (out−in)/(basedur/baseRate)` avec recalage si la dérive > 0,18 s.
- Sortie : un seul JSON `{in,out,speed,baseRate,screen,crop}` à recoller.

⚠️ **Cohérence des aspects, sinon le cadrage de l'utilisateur est trahi.** Bug réel :
le picker verrouillait le crop à l'aspect **moyenne des côtés opposés** (1,480)
tandis que `composite-quad.py` recadrait à **max/max** (1,352) → 68 px rognés de
chaque côté APRÈS son choix, deux rejets « ce n'est pas ce que j'ai choisi ».
Règle : même formule partout, ET **toujours passer `--screen-aspect` = aspect du
crop** au compositeur pour qu'il ne recadre plus rien.

⚠️ **Nommer les outils avec un nom UNIQUE ET DATÉ** (`COMPOSER-hero-19aout.html`).
Deux outils homonymes livrés le même jour ont fait régler l'utilisateur dans la
mauvaise vidéo — timecodes valides, contenu faux, une heure perdue.

## Étape 4 — Compositing

Script de référence : `assets/composite-quad.py` (pillow + numpy + ffmpeg).
```bash
python composite-quad.py --base base.mp4 --overlay interface.mp4 \
  --quad '{"tl":[64,77],"tr":[414,71],"br":[450,101],"bl":[112,115]}' \
  --out hero.mp4 --speed 6.5 --overlay-start 55 --overlay-end 150 \
  --white 235,245,255 --feather 1.0 --crf 23
```
Points durs encodés dans le script (leçons apprises) :
- **Warp perspective PIL** avec coefficients exacts vers le quad utilisateur —
  jamais de détection auto.
- **Aspect préservé** : l'overlay est recadré (crop centré) à l'aspect du quad,
  pas déformé.
- **Balance des blancs** : le blanc de l'overlay est ramené vers le blanc RÉEL
  de l'écran filmé (`--white R,G,B` échantillonné sur la base). Si l'écran de la
  base est très teinté, remonter la cible ~50 % vers le blanc pur, sinon tout
  l'overlay paraît teinté.
- **Plancher des noirs** (`--black-floor 16`) : un écran filmé n'affiche jamais
  de noir pur.
- **Feather ~1 px** sur le pourtour du masque (fondu naturel avec la dalle).
- Accélération de l'overlay (`--speed`) : une capture d'interface de plusieurs
  minutes devient vivante en ×5–×7 dans une boucle de 10–12 s.
- ⚠️ **`--speed` > ~4 : pré-accélérer via ffmpeg** (`setpts=(PTS-STARTPTS)/N,fps=<out_fps>`
  + crop utilisateur dans le même filtre) puis appeler le script avec `--speed 1` —
  sinon l'extraction à `out_fps × speed` duplique des dizaines de milliers de frames.
- Si la zone reste petite/pixelisée après l'anti-aliasing : **upscale de la vidéo de
  base** (ex. Higgsfield `upscale_video` bytedance 2K, preset aigc) puis multiplier
  les coordonnées du quad par le facteur d'échelle exact (2560/1280 = ×2).

## Étape 5 — Encode, validation, intégration

- Sortie : H.264 CRF 22-24, `yuv420p`, `+faststart`, **muet**, + poster jpg de la
  1ʳᵉ frame. Pour le web : ~900-1440px de large, viser < 1,5 Mo.
- **Montrer la vidéo composée à l'utilisateur (SendUserFile) AVANT de l'intégrer**
  où que ce soit. Max 1 round de propositions ; si rejet → demander une référence
  précise plutôt qu'itérer en aveugle.
- Intégration web type : `<video autoplay muted loop playsinline poster=...>`.

## Pièges connus (ne pas refaire)

1. Détection automatique du quad (masque couleur, fit de droites) → échecs répétés
   (reflets, bords sombres, particules). **Toujours l'outil + l'utilisateur.**
2. Zéro effet non demandé (étincelles, halos…) — rejet immédiat.
3. `git commit -m` multiligne PowerShell casse → `-F fichier`. Heredoc `<<` n'existe
   pas en PowerShell → générer les fichiers via .NET ou l'outil Write.
4. Les images collées dans le chat ne sont pas sur disque → presse-papiers
   (`[System.Windows.Forms.Clipboard]::GetImage()`) ou `Pictures\Screenshots`.
5. localStorage peut être bloqué (data: URL) → les templates l'enveloppent en
   try/catch ; ne pas retirer.
6. Si l'outil est réduit/proxifié : convertir les coordonnées vers la résolution
   de TRAVAIL avant le warp.
7. Overlay pleine résolution warpé directement dans un petit quad → **crénelage /
   scintillement** (« c'est pixelisé »). Le transform PIL point-sample : toujours
   **pré-réduire l'overlay à ~2× la taille du quad en LANCZOS** avant le warp
   (fait par le script). Si l'écran reste petit dans l'image, le texte ne sera
   jamais lisible — proposer un crop plus serré de l'interface et/ou un upscale
   de la vidéo de base.
