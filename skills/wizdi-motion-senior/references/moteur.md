# Aide-mémoire du moteur (pour écrire `film.js` et `style.js`)

Ordre de chargement (`film.html`) : gsap → DrawSVG → `assets/logos.js` → `build/media/manifest.js` → `words.js` → `film.js`
→ (`cut.js`) → `core.js` → (`footage.js`) → `pop.js` → `style.js`. Le format vient de `?format=9x16|4x5|16x9`.

## WIZ_FILM (film.js)

| Champ | Sens |
|---|---|
| `slug`, `logo` | nom des livrables ; clé du logo dans `WIZ_LOGOS` (`wizplay`, `wizplan`, `wizchat`, `wizbook`, `wizbox`, `wizspace`, `wizgen`, `wizmap`) |
| `color`, `sun` | couleur du module (tokens) ; jaune d'accent (défaut `#FFD23F`) |
| `owl`, `owlImg`, `owlImgs`, `flatOwl` | préfixe des séquences du hibou 3D ; image fixe 3D (défaut `assets/owl-3d.webp`) ; par pose ; hibou plat du logo |
| `voAt`, `endHold`, `dur` | début de la voix ; tenue de la carte de fin ; durée forcée (sinon voAt + voix + endHold) |
| `bpm` | tempo visé ; la grille réelle = nombre entier de mesures entre la 2e phrase et le final (`timeline.bpm`) |
| `popThemes`, `popDeco` | ordre des fonds (`mod navy cream sky sun`) ; stickers décoratifs (`+ * o x = v > c`) |
| `layout` | surcharges de mise en page par format : `{ "16x9": { wordsX: 1400, owl: { x: 1700, y: 860, h: 280 } } }` |
| `allowText` | inscriptions à nous permises par textscan (ex. `["1 · 2", "Word"]`) — à faire valider par Liad |
| `footage`, `keep` | personne filmée (`{ dir, n, w, h, fps }`) ; intervalles gardés d'un montage filmé (`cut.js`) |
| `scenes` | une entrée par clé de `words.js` (ci-dessous) |

Scène : `kind` (`brand` | `generic` | `end`, défaut : `end` pour la dernière) · `theme` · `wipe` (`iris diag rise split`) ·
`band` (couleur d'un double volet) · `emph` (indices des mots sur plaque) · `per` (mots par groupe) · `ys`, `wordsX`, `wordSize` ·
`words: false` · `brandAt` (indice du mot « WizX » remplacé par le logo) · `logoAt` · `owl` (`{ pose, at, until, x, y, h, from, hops, exit }` ou `false`) ·
`media: [{ name, at, until, x, y, w, rot, cam, speed, start, still, stopAt, shots, enter, leave, marks: [{ r, at, until, piece, back, frame }] }]` ·
`portal` (bulle : `{ name, at, until, d, fx, fy, zoom }`) · `count` (`{ to, at }` — un chiffre DIT) · `chips` (`[{ html, at }]` — une liste DITE) ·
`wizdi` (`{ at }` plaque du logo Wizdi) · `burst` (indices : confettis + éclat) · `extra(ctx)` (code libre) · `"9x16"|"4x5"|"16x9": { … }` (surcharges).
Valeurs `at`/`until` : un nombre = indice du mot (instant où il est dit) ; une chaîne `"0.8"` = secondes depuis le début de la scène.

## WZ (core.js)

`F W H FMT SAFE DUR VO_AT KEYS` · `words(k)` `shown(k)` (sans x) `chunks(k, n)` · `WT(k,i)` `WE(k,i)` (début/fin d'un mot dans le film) ·
`LS(k)` `LE(k)` `T0(k)` `T1(k)` (fenêtre d'une scène) · `tl` (LA timeline) · `sfx(t, clé, gain, pan)` ·
`$(tag, cls, parent, html)` `css` `box(el, cx, cy, w, h)` `clamp lerp prog ease rng kfEval rgba mix` ·
`panel({ name, layer, x, y, w, rot, t0, t1, cam: [[t, zoom, fx, fy, ease]], pose: [[t, x, y, s, rot, ease]], shots })` -> `{ pop, fr, ink, pt(t,x,y), at(t) }` ·
`pieceOut(panel, [x,y,w,h], t, tOut, { x, y, w, rot }, { back, frame, layer, deco })` · `loopPath(cx, cy, rx, ry, seed)` ·
`wordmark(parent, clé)` + `drawLogo(L, t, d)` · `owlCanvas(parent, pose, tIn, tOut)` · `mediaEl` `play(nom, t0, vitesse)` `mediaSize` ·
`confetti(t, x, y, { n, sp, ang, spread, life })` `pow(t, x, y, { r0, r1, n, col })` · `ambient.push(fn(t))` `media.push(fn(t))` · `run(build)`.

## POP (pop.js)

`TH.{mod,navy,cream,sky,sun}` (fond, trame, encre, plaque, ombres) · `LAY` (mise en page du format courant) ·
`wipe(t, th, kind, { at, d, quiet })` `band(t, th, accent)` · `decos(t0, t1, th, n, seed)` `starB(x, y, r, col, t, tOut)` ·
`kl({ words: [[mot, t, plaque?]], x, y, size, th, tOut, out: "up", rot, maxW })` · `sceneWords(k, th, { emph, per, ys, x, size })` ·
`sticker({ name, x, y, w, rot, t0, t1, cam })` `enter(s, t, rise|zoom|flip|right|left|drop)` `leave(s, t, punch|shrink|up|down|left|right|flip)` ·
`felt(s, r, t, tOut, couleur)` `piece(s, r, t, tOut, { x, y, w, rot }, { back })` · `bub({ name, x, y, w, tIn, tOut, blob })` ·
`owl(pose, x, y, h, tIn, tOut, pop|left|right|bottom, { hops, exit, mirror })` · `count(n, t, x, y, size, tOut, th)` · `tile(html, x, y, size, t, tOut, th)` ·
`wizdiPlate(x, y, w, t, tOut)` · `brand(k, sc, i)` `generic(k, sc, i)` `end(k, sc)` `build()` · `setBeat(beat, t0)`.

## Repères sonores (`WZ.sfx(t, clé, gain)`) synthétisés par `tools/synth.py`

`whoosh whooshUp swoosh slide` (mouvements) · `pop bubble tick tickSoft click card flip` (apparitions) · `impact boom riser`
(temps forts) · `shimmer twinkle pillPop finalChord success ding` (brillances, final) · `scribble scribbleLong` (feutre).
Une clé inconnue devient un pop (signalé). Dans `mix.json`, `"sfx": { "pop": ["build/el/pop.mp3", -8] }` remplace une clé par un fichier.

## Valeurs de la grammaire (pop.js)

Mot : apparaît 0,1 s avant d'être dit ; masque qui monte (yPercent 140→0, 0,18 s, power4.out) + échelle 0,5→1 (0,55 s,
back.out(3.4)) + petite secousse de la ligne ; ombre dure 0,045 em. Plaque (mot fort) : échelle 1,75→1, rotation −11°→−2,5°,
0,36 s, back.out(2.2). Corps : 230/190 px en 9:16, 200/170 en 4:5, 150/130 en 16:9 (réduits pour tenir dans la largeur).
Sticker : liseré blanc 14 px + ombre franche décalée 18 px, ±2° ; entrée 0,6 s back.out(1.55) ; sortie 0,2 s power2.in.
Feutre : tracé main levée en 0,26–0,3 s (power1.inOut), 12 px. Morceau qui sort : depuis sa place exacte, 0,5 s back.out(1.5),
liseré 12 px + ombre 18 px, flotte. Volets : 0,38–0,5 s power3.inOut, de droite à gauche. Hibou : entrée 0,62 s back.out(2.1),
sauts de 70 px (bounce.out), liseré blanc 5 px + ombre 16 px. Logo : contour 0,4 s power2.inOut, remplissage 0,2 s, élastique.
Rayons tournants 14°/s derrière le logo. Stickers décoratifs : élastique à l'entrée, flottent, pulsent sur le temps.
