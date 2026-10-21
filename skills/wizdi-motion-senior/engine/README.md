# Moteur motion Wizdi — style « pop » (9:16 · 4:5 · 16:9)

Une page HTML par film, **une timeline GSAP en pause calée au mot de la narration**, rendue **image par image** par
Chromium (Playwright) puis encodée par ffmpeg. Rien ne dépend du temps réel : le rendu est identique sur tous les PC.
Musique et bruitages **synthétisés** (libres de droits) ; ElevenLabs en option. Mixage à −14 LUFS, crête ≤ −1 dBTP.
Trois formats composés chacun pour son cadre, couverture 0,2 s, version WhatsApp < 16 Mo, contrôles automatiques.

## Prérequis (une fois par PC)

| | Windows (PowerShell) | macOS (Terminal) |
|---|---|---|
| Python 3.10+ | `winget install Python.Python.3.12` (cocher « Add to PATH » si installeur python.org) | `brew install python@3.12` |
| Paquets Python | `py -m pip install playwright pillow numpy scipy` | `python3 -m pip install playwright pillow numpy scipy` |
| Chromium de Playwright | `py -m playwright install chromium` | `python3 -m playwright install chromium` |
| ffmpeg + ffprobe | `winget install Gyan.FFmpeg` (puis rouvrir le terminal) | `brew install ffmpeg` |
| Kit de marque | `git clone https://github.com/yoni-wizdi/wizdi-brand-kit $HOME\wizdi-brand-kit` | `git clone https://github.com/yoni-wizdi/wizdi-brand-kit ~/wizdi-brand-kit` |
| ElevenLabs (facultatif, payant) | `setx ELEVENLABS_API_KEY "<ta clé>"` puis nouveau terminal | `echo 'export ELEVENLABS_API_KEY="<ta clé>"' >> ~/.zshrc` |

Vérifier : `python -c "import playwright, PIL, numpy, scipy; print('ok')"` et `ffmpeg -version`
(sur macOS, `python3` à la place de `python` partout ; sur Windows `py` marche aussi).
Homebrew absent sur le Mac : https://brew.sh. La clé ElevenLabs ne s'écrit **jamais** dans un fichier du projet.

## Démarrage en 3 étapes

```bash
# 1) copier le moteur dans un dossier de film (chemin COURT : Windows refuse les dossiers trop longs)
#    Windows : mkdir $HOME\films -Force; Copy-Item -Recurse "$HOME\.claude\skills\wizdi-motion-senior\engine" "$HOME\films\mon-film"
#    macOS   : mkdir -p ~/films && cp -R ~/.claude/skills/wizdi-motion-senior/engine ~/films/mon-film
cd ~/films/mon-film

# 2) brancher le kit de marque : logos officiels, couleurs, hibou 3D, polices (ou --kit <chemin du kit>)
python tools/brand.py

# 3) fabriquer : repères -> son -> rendu -> livrables dans out/ ; puis contrôler
python tools/make.py --formats 9x16          # les 3 formats : sans --formats
python tools/check.py out/wizplay-9x16-HD.mp4
```

L'exemple livré (≈ 3,3 s : logo WizPlay tracé au mot, slogan en carte de fin) sort en ~15 s :
`out/wizplay-9x16-HD.mp4`, `out/wizplay-Cover.jpg`, `out/wizplay-9x16-WhatsApp.mp4`.
Aperçu interactif : ouvrir `film.html` dans Chrome (barre de lecture, choix du format, `?t=2.5` fige un instant).

## Les fichiers

| Fichier | Rôle | On le modifie ? |
|---|---|---|
| `film.html` | la page : ordre des scripts | rarement (activer `cut.js` / `footage.js`) |
| `words.js` | mots VERBATIM + instants (généré par `tools/words.py`) | non, on le régénère |
| `film.js` | le film : couleur, logo, scènes, médias, repères (`r` en px de la source) | **oui** |
| `style.js` / `style.css` | ta chorégraphie et ton habillage (par-dessus `POP.build()`) | **oui** |
| `core.js` | le cœur (WZ) : timeline, mots, vrais médias, panneau + caméra, morceau qui sort, hibou, logos, particules, rendu | non |
| `pop.js` / `pop.css` / `base.css` | la grammaire pop validée (POP) et ses mises en page par format | non (copie-les si tu dois les changer) |
| `cut.js` / `footage.js` | option : film sur un montage filmé (resserrer avec `keep`) / personne filmée comme calque | non |
| `vendor/` | GSAP 3.15 + DrawSVGPlugin (gratuits, licence GreenSock dans l'en-tête) | non |
| `assets/` | polices (livrées) ; `logos.js`, `owls/<module>-<pose>.webp` (Wizi de chaque module et WizBuddy, détourés), `owl-3d.webp`, `wizdi-owl.png` (créés par `brand.py`) | non |
| `examples/film-wizplay.js` | un film complet de 7 scènes (13/10) comme modèle de `film.js` | à copier |
| `build/`, `out/`, `vo/` | médias préparés, rendus, voix (créés par les outils) | — |

## Les outils (`python tools/<outil>.py -h` pour tout le détail)

| Commande | Ce qu'elle fait |
|---|---|
| `brand.py [--kit …]` | kit -> `assets/logos.js` (tracés officiels + couleurs des modules), hibou 3D, hibou plat (logo), polices |
| `media.py add <nom> <fichier> [--from --to] [--crop x,y,w,h] [--autocrop]` | un VRAI écran / enregistrement -> `build/media/<nom>/` (30 i/s) + `manifest.js` |
| `media.py footage <clip>` | une prise filmée -> `build/footage/` 1080x1920 (pour `footage.js`) |
| `words.py --script vo-script.json --timing <json>` | texte validé + horodatage de la voix (TTS, Scribe ou manuel) -> `words.js` |
| `render.py sheet --step 0.5 [--format 4x5]` | planche de contrôle -> `out/sheet-<fmt>.jpg` (à regarder à chaque réglage) |
| `render.py stills 1.2 3.4 --scale 1` | images exactes pleine résolution -> `out/stills-<fmt>/` |
| `render.py textscan [--format …]` | contrôle VERBATIM : tout mot visible doit venir de `words.js` (code 1 sinon) |
| `render.py timeline` / `video` | repères sonores / rendu muet d'un format |
| `synth.py` | musique + bruitages synthétisés (utilisé par `mix.py`) |
| `mix.py [--stems]` | voix + musique + bruitages -> `out/mix.wav` à −14 LUFS, crête ≤ −1 dBTP (réglages : `mix.json`) |
| `make.py [--formats …] [--jobs 3] [--cover-at t]` | tout : repères -> mix -> rendu parallèle -> couverture -> livrables |
| `check.py <mp4> [--scribe]` | format, 30 i/s, codecs, sonie, crête, noirs, poids, planches d'accroche et du film, transcription |
| `el.py tts / stt / music / sfx / isolate` | ElevenLabs (clé dans `ELEVENLABS_API_KEY`) : voix horodatée, transcription, musique, bruitages, voix isolée |

## Un vrai film, dans l'ordre

1. **Narration** : `vo-script.json` (`text` = l'écran mot pour mot ; `say` = ce que lit la voix : « Wiz Plène », nikoud
   ciblé, chiffres en lettres). Textes validés (Yoni, puis Liad) **avant** toute génération.
2. **Voix** : `python tools/el.py tts` (ElevenLabs v4, horodatage au caractère) ou une voix enregistrée
   (`python tools/el.py stt vo/voice.wav` pour ses instants, ou un calage manuel), puis
   `python tools/words.py --script vo-script.json --timing vo/take1.json` -> `words.js`.
3. **Vrais médias** : `python tools/media.py add …` pour chaque écran / enregistrement réel (noms de personnes retirés
   par `--crop`). Jamais d'interface simulée.
4. **Scènes** : `film.js` (une scène par phrase : `kind`, `emph`, `media` + `marks` [feutre -> morceau qui sort], `portal`,
   `owl`, `count`, `chips`…). Modèle : `examples/film-wizplay.js`. Surcharges par format : `"16x9": { … }`.
5. **Réglage sur planches** : `render.py sheet` et `render.py stills` dans les 3 formats ; `render.py textscan`.
6. **Son** : `mix.json` (voix, musique `synth` ou fichiers, bruitages `synth` ou table de fichiers, ducking).
7. **Fabrication** : `python tools/make.py` ; **contrôle** : `check.py` sur chaque livrable, planches regardées, mix écouté.

Exemple de `mix.json` :
```json
{ "voice": "vo/narration.wav", "music": "synth", "duck_db": -11, "sfx": { "pop": ["build/el/pop.mp3", -8] }, "lufs": -14, "tp": -1.5 }
```

## Bon à savoir

- **Concours** (plusieurs rendus sur la même machine) : `RENDER_SLOT_DIR=<dossier partagé>` et `RENDER_SLOTS=3` limitent
  le nombre de navigateurs ouverts (chaque rendu attend son tour). Compter ~0,6 Go de RAM par navigateur (`--jobs`).
- Une position négative dans la timeline (`tl.to(…, -0.1)`) est ramenée à 0 avec un avertissement : sans ce garde-fou,
  GSAP décalerait tout le film et casserait la synchro au mot.
- Le hibou animé (séquences WebP détourées `build/owl/<owl>-<pose>/001.webp` + `window.WIZ_OWLS`) est pris s'il existe ;
  sinon le hibou 3D fixe du kit, animé par le style. Jamais le hibou plat hors du logo.
- `assets/logos.js` absent = logos en repli texte bicolore (avertissement dans la console) : à corriger avant livraison.
- Windows : si « path longer than allowed » s'affiche, rapprocher le dossier du film de la racine (`C:\films\…`).
- Le détourage d'une personne filmée (`build/matte/*.png`) n'est pas fourni : outil de matting au choix (ex. Robust Video Matting).
