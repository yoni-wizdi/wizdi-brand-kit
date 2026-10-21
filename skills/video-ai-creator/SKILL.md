---
name: video-ai-creator
description: Use whenever the user wants to create ANY AI-generated video — realistic ad, animation (2D/3D/anime/Pixar), brand reveal, educational explainer, social post, music video, product demo, or narrative short — with AI tools (Flow/Veo, Kling, Seedance, Runway, Omni, Nano Banana, Midjourney, Pika, AnimateDiff, ElevenLabs). Triggers: "creer une video", "faire une animation", "pub", "publicite", "storyboard", "video ad", "Reels", "TikTok", "commercial", "brand reveal", "AI animation", "Pixar style", "anime", "video IA", or any video creation request in any language. Provides an adaptive methodology: French opening questionnaire, branching workflow (realistic / animation / motion graphics / educational / music), interactive HTML storyboard, brand-agnostic universal prompts, iterative logo compositing, multilingual voice-over (Hebrew/French/English/Arabic/Spanish), modesty support for religious contexts, and anti-copyright clean prompts.
language: fr
version: 1.0
---

<!-- ============================================================
     ENVIRONMENT CHECK — READ THIS FIRST BEFORE ANYTHING ELSE
     ============================================================

     META-INSTRUCTION FOR THE AI READING THIS FILE:

     This file is a Claude SKILL designed EXCLUSIVELY for Cowork
     (a feature of the Claude Desktop app). It uses Cowork-only
     tools: file system tools (Read/Write/Edit), the cowork
     directory request, IndexedDB-backed HTML artifacts,
     mcp__cowork__present_files, and the .skill installation
     system.

     IF YOU ARE NOT RUNNING INSIDE COWORK (e.g., the user dropped
     this .skill file into regular Claude.ai web, ChatGPT, Gemini,
     Claude API console, or any other chat interface that is NOT
     Cowork), YOU MUST IMMEDIATELY STOP and tell the user (in
     French, since the user speaks French) the message below.
     DO NOT proceed with the methodology even if the user insists.

     FRENCH MESSAGE TO SHOW:
     ⚠️ Ce fichier est un Skill exclusif à Cowork.
     Il ne fonctionnera pas dans Claude.ai web / ChatGPT / Gemini.

     Comment l'utiliser correctement :
     1. Ouvre l'application Cowork (fonctionnalité de Claude Desktop).
     2. Glisse le fichier video-ai-creator.skill directement dans la
        fenêtre de Cowork.
     3. Clique sur le bouton "Save skill" qui apparaît.
     4. Ouvre une nouvelle conversation dans Cowork et écris
        "je veux créer une vidéo". Le skill se chargera automatiquement
        et démarrera par le questionnaire.

     IF YOU ARE INSIDE COWORK: proceed normally with the workflow
     below, starting with the French questionnaire.
     ============================================================ -->

# 🎬 Création Vidéo AI · Méthodologie Adaptative

> ## ⚠️ Skill exclusivement pour Cowork
>
> Ce skill nécessite des outils Cowork (création de fichiers HTML, gestion de dossiers, `present_files`, IndexedDB). Il ne fonctionnera pas en dehors de Cowork (Claude.ai web / ChatGPT / Gemini / API).

> **Skill personnel polyvalent pour démarrer n'importe quel type de création vidéo AI.**
> Réaliste, animation, motion graphics, brand reveal, vidéo éducative — avec ou sans références — multilingue. La méthodologie s'adapte à TES besoins selon les réponses au questionnaire d'ouverture.

---

## 👋 Bienvenue · Démarrons par le brief

**Instruction à Claude (toi qui lis ce skill)** :
Avant d'écrire UNE seule ligne de prompt ou de générer du HTML, **pose le questionnaire d'ouverture ci-dessous au user**. Une question à la fois, ou en groupe selon sa préférence. **Ne saute pas cette étape** — le bon brief est ce qui sépare une vidéo médiocre d'une vidéo professionnelle.

### Questionnaire d'ouverture (en français)

**1. Quel type de vidéo veux-tu créer aujourd'hui ?**
- 🎥 **Pub réaliste** (acteur réel, lifestyle, cinéma)
- 🎨 **Animation 2D / 3D** (Pixar, Disney, anime, motion graphics)
- 🚀 **Reveal de marque** / intro logo
- 📚 **Vidéo éducative / explicative**
- 🎵 **Clip musical** / vidéo artistique
- 📦 **Démo produit**
- 🎬 **Court-métrage narratif**
- ❓ **Autre** — décris en quelques mots

**2. Quel style visuel exact ?**
- Cinéma photoréaliste (A24 / Roger Deakins / film prestige)
- Pub TV lifestyle premium (style Apple, Lululemon, Nike — sans nommer)
- Animation 3D Pixar / Disney / DreamWorks
- Animation 2D / anime japonais / Ghibli
- Motion graphics minimaliste (Apple keynote / Stripe)
- Vintage / rétro / Y2K
- Hyperréaliste / surréaliste / abstrait
- **Tu as une référence ?** (envoie une image ou un lien de vidéo)

**3. Format(s) et durée ?**
- 9:16 vertical (Reels / TikTok / Stories) — 15-30s
- 1:1 carré (feed Instagram / LinkedIn) — 30-60s
- 16:9 horizontal (YouTube / écran) — 1-3 min
- 4:5 (LinkedIn vertical)
- **Plusieurs formats à décliner ?**

**4. Le public cible ?**
- Âge approximatif
- Géographie (Israël ? France ? International ?)
- Contexte religieux / culturel (laïc, religieux, communautaire)
- Centres d'intérêt / persona

**5. La voix off ?**
- **Langue(s)** : hébreu, français, anglais, arabe, espagnol, autre
- **Ton** : chaleureux, dynamique, sérieux, ludique
- **Voix** : féminine, masculine, jeune, mature
- **Pas de voix off** si tu préfères

**6. Tu as déjà des assets ?**
- Logo (PNG transparent HD) — combien ?
- Photo de personnage / acteur (pour cohérence visage entre scènes)
- Photos de lieux / références ambiance
- Police de la marque
- Palette de couleurs (codes HEX)
- ⚠️ **Pas d'assets** — on part de zéro, on génère tout

**7. Quel insight / message central ?**
- Ce que le spectateur doit ressentir
- Ce qu'il doit faire après (CTA)
- Le punch / la révélation

**8. Contraintes spéciales ?**
- Modestie pour public religieux (couvrant, sans décolleté, sans ventre)
- Pas de marques concurrentes (anti-copyright)
- Pas de contenu enfants visible (problème de filtres sur Omni / Seedance)
- Délai serré ?
- Budget outils ?

---

## ⏸ Récap avant production

Après les 8 questions, **récapitule à l'utilisateur** :
1. Le type de vidéo + style visuel
2. La cible et le ton
3. Les formats et durée
4. Les assets dispo vs à générer
5. L'insight central
6. Les contraintes

**Attends son OK avant de commencer la production.**

---

## 🎯 Chemins de production adaptatifs

Selon les réponses, prends le bon chemin :

### 🔵 CHEMIN A — Pub réaliste avec acteur(rice)

**Stack outils** :
- **Stills** : Nano Banana (priorité, meilleure adhérence aux refs) → Flow / Midjourney (alternatives)
- **Motion** : Kling 2.0 (le plus permissif, le plus fidèle à l'image input) → Runway Gen-3 → Seedance (rapide mais filtres anti-marque) → Omni (filtres enfants)
- **Voix** : ElevenLabs (multilingue, voix chaleureuses)
- **Édition** : CapCut / DaVinci Resolve

**Étapes** :
1. Définir `CHAR_DESC` constante (description précise de l'actrice : âge, couleur cheveux/yeux, type de peau, traits) — réutilisée dans chaque prompt
2. Obtenir une photo de référence du visage de l'actrice (image-input pour COHÉRENCE entre scènes — sinon le visage change à chaque génération)
3. Définir `MODESTY_PRIORITY` constante si contexte religieux (col rond haut, ventre couvert, etc.)
4. Pirouk en 5-7 scènes avec arc émotionnel clair
5. Pour chaque scène : prompt photo détaillé + prompt motion **uniquement de mouvement** (pas d'UI / éléments graphiques)
6. Itération scène par scène, validation visuelle avant motion

### 🔵 CHEMIN B — Animation (Pixar / Disney / Anime)

**Stack outils** :
- **Stills** : Midjourney `--style raw` ou avec `--sref` (style reference) → Flow / Nano Banana pour cohérence personnage
- **Motion** : Kling 2.0 → Runway Gen-3 → Pika Labs
- **Workflow custom** : AnimateDiff + ComfyUI si besoin total contrôle
- **Voix** : ElevenLabs avec voix expressives style "narration animation"

**Étapes** :
1. **Style guide précis** dans chaque prompt (ex: "in the style of modern 3D animation feature film, soft warm cinematic lighting, character with stylized geometric features but expressive eyes, smooth surfaces, rounded character design — Pixar / DreamWorks quality")
2. **Cohérence personnage** = description détaillée répétée dans chaque prompt (couleurs, formes, vêtements) — pas de photo de référence possible
3. **Color script** : définir la palette par scène (jour/nuit, intérieur/extérieur, ambiance)
4. **Cuts plus longs** que pub réaliste (animation = plus de patience visuelle)
5. **Mouvements expressifs** mais physiquement plausibles

### 🔵 CHEMIN C — Motion graphics / Brand reveal cinématique

**Stack outils** :
- **Stills** : Nano Banana en mode **compositing itératif** (5 étapes)
- **Motion** : Flow / Veo (meilleur pour particules + atmosphère) → Kling 2.0
- **Édition** : After Effects pour overlays propres

**Principe critique** : **AI ne peut PAS générer ton logo exact**. Il faut un workflow itératif :

```
Étape 1A : génération fond cinéma vide (particules + lumière, espace négatif au centre)
Étape 1B : prends le résultat 1A + ton logo PNG en référence → Nano Banana l'intègre au centre
Étape 1C : prends le résultat 1B + ton wordmark → Nano Banana l'ajoute en dessous
Étape 1D : prends le résultat 1C + logo partenaire 1 → ajoute en bas gauche
Étape 1E : prends le résultat 1D + logo partenaire 2 → ajoute en bas droite (FINAL FRAME)
```

Puis **f2f motion sur Flow / Kling** : START FRAME = 1A, END FRAME = 1E → l'IA crée l'animation de matérialisation.

**Langage des prompts** : **TOUJOURS universel** ("the brand mark from REFERENCE 2", JAMAIS "the Wizdi logo" car l'IA ne sait pas ce que c'est et inventera).

### 🔵 CHEMIN D — Vidéo éducative / explicative

**Stack outils** :
- **Stills** : Nano Banana / Midjourney pour les "scènes d'illustration"
- **Voix** : **ElevenLabs en priorité absolue** — la voix-off porte tout le sens
- **Motion** : peut être plus simple (slideshow, kenburns) car le visuel est secondaire
- **Édition** : CapCut suffit, captions auto

**Structure type** :
1. Hook (3s) — pose le problème
2. Promise (5s) — annonce ce qu'on va apprendre
3. Content (60-180s) — 3-5 points avec illustration AI
4. Recap (5s) — résumé
5. CTA (3s) — action concrète

### 🔵 CHEMIN E — Clip musical / vidéo artistique

**Stack outils** :
- **Stills** : Midjourney `--style raw` pour l'esthétique artistique
- **Motion** : Kling 2.0 (movement cinematic) → Runway pour effets stylisés
- **Synchro musique** : DaVinci Resolve pour beat-match précis

**Principes** :
- Le **rythme de la musique** dicte la durée des plans (pas l'inverse)
- Variation des angles / focales (close-up / wide / extreme / aerial)
- Couleurs + lumières expressives qui matchent le mood musical
- Transitions audacieuses (match cut, whip pan, dissolve)

---

## 🔑 Principes universels (à appliquer dans TOUS les chemins)

### 1. ✍️ Langage universel dans les prompts

**NE JAMAIS** nommer ton logo / marque dans un prompt : "the Wizdi owl logo", "the HASHBACHA brand mark" → l'IA invente.

**TOUJOURS** utiliser des références neutres : "the brand mark from REFERENCE 2", "the logo provided as PNG", "the central element from the attached reference".

### 2. 🎥 Motion prompts = mouvement + caméra UNIQUEMENT

**Règle absolue** : un prompt motion décrit **uniquement** :
- Les mouvements de la personne (subtle micro-movements, expressions faciales, gestes)
- Les mouvements de caméra (locked / push-in / pan / orbit)
- Les mouvements de la nature (cheveux qui bougent, tissu qui flotte, particules de poussière)

**NE JAMAIS** décrire :
- ❌ Des changements d'UI ("the button glows", "the screen activates")
- ❌ Des apparitions de logos
- ❌ Des "checkmarks" / "confirmation animations"
- ❌ Des éléments graphiques qui changent

**Pourquoi** : l'IA ne sait pas animer des éléments graphiques fidèlement, elle les déforme. Ces éléments doivent être **figés dans l'image input** ou ajoutés en post-production.

### 3. ⚖️ Modestie pour contexte religieux

Si public observant / religieux, **constante MODESTY_PRIORITY** au début de chaque prompt :

```
MODESTY CONSTRAINT — HIGHEST PRIORITY, NON-NEGOTIABLE:
The subject is dressed in modest attire adapted to the warm climate.
(1) NO cleavage — HIGH round neck / crew neck only, NO V-neck;
(2) NO bare midriff — stomach fully covered;
(3) The clothing CAN be fitted / sporty / chic — but NO sheer fabric, NO low-cut;
(4) NO turtleneck (climate inappropriate, except if explicitly needed);
(5) Modern modest Israeli style — fitted but covered, not frumpy.
```

### 4. 👤 Cohérence personnage entre scènes

**Problème** : l'IA crée une fille différente à chaque génération.

**Solution** :
1. Photo de référence de l'actrice (générée une fois)
2. `CHAR_DESC` constante : âge, couleur cheveux/yeux, type peau, traits
3. Image-input dans chaque prompt + mention explicite "(USE ATTACHED REFERENCE PHOTO for face consistency)"
4. Midjourney : `--cref` (character reference)

### 5. 🚫 Anti-copyright (filtres Seedance / Omni)

Marques à NE JAMAIS mentionner dans les prompts (sinon filtre auto bloque) :
- Apple, iPhone, AirPods, MacBook
- Nike, Adidas, Lululemon
- Spotify, YouTube
- Mercedes, Tesla, BMW
- Marques tierces du client (sauf si tu as les droits)

**Tableau de tradutions** :

| Marque | Tournure générique |
|--------|---------------------|
| iPhone | smartphone (latest generation) |
| AirPods | wireless earbuds |
| Spotify | music streaming app |
| Nike sneakers | athletic running sneakers |
| MacBook | silver laptop |
| Tesla | modern electric car |

### 6. 🛡 Filtres de contenu sensible

**Combos à éviter dans le même prompt** :
- ❌ "teacher" + "classroom" + "children" → Omni / Seedance bloquent (child safety)
- ❌ "nightclub" + "alcohol" + "young woman" → Seedance bloque
- ❌ "smoke" + "haze" + "darkness" → certains modèles bloquent

**Tournures sécurisées** :
- "teacher in classroom" → "young woman in warm room"
- "children" → "small seated figures" (ou complètement supprimé)
- "DJ booth nightclub" → "music event mixing booth"
- "smoke" → "warm atmospheric haze"

### 7. 🎨 Continuité palette entre scènes

Les scènes doivent **sembler venir du même univers visuel**. Si scène 5 est dans une classe chaude beige/cream, scène 7 (CTA) doit garder cette chaleur — **pas** virer subitement au cinéma gold sombre.

**Astuce** : utilise le **last frame de la scène précédente** comme image-input pour calibrer la palette de la suivante.

### 8. 📏 Mégalimites des outils

- **Seedance** : 4000 caractères max par prompt
- **Kling** : 2500 caractères environ
- **Flow / Veo** : flexible
- **Midjourney** : prompts courts > longs

### 9. 🏷 Logos → toujours en POST-PRODUCTION

**Principe pro** : AI ne peut PAS reproduire un logo exact. Universal / A24 / Marvel font tous pareil :
1. AI génère l'atmosphère cinématique (god-rays, particules, lumière, mood)
2. Logo exact ajouté en **After Effects / CapCut / DaVinci** en overlay

**Exception** : workflow itératif compositing (CHEMIN C) avec Nano Banana, qui respecte mieux les refs.

### 10. 🌍 Multilinguisme

ElevenLabs supporte **toutes les langues** avec qualité native :
- Hébreu : voix féminines warm (Bella, Rachel équivalents)
- Français : voix avec accent natif (pas accent étranger)
- Arabe : MSA ou dialectal selon cible
- Anglais : US / UK / Australian

**Astuce** : enregistre TOUTES les voix off en même temps (toutes langues), puis tu fais des variantes du même montage pour différents marchés.

---

## 💻 Structure HTML storyboard

### Modèle de données par scène

```javascript
const SCENES = [
  {
    n: 1,
    time: "0:00 – 0:03",
    titre: "Titre court de la scène",
    objectif: "Ce que le spectateur doit ressentir ici",
    visuel: "Description en français pour l'utilisateur",
    duration: "3s",
    tenue: "Description tenue (si applicable)",
    device: "Smartphone / laptop / etc.",
    mood: "Énergie / calme / fort",
    motionType: "i2v",                       // "i2v" ou "f2f"
    imagePrompt: `Prompt EN détaillé...`,    // pour i2v
    // OU pour f2f :
    // imagePromptStart: `...`,
    // imagePromptEnd: `...`,
    motionPrompt: `Prompt motion EN (mouvement + caméra uniquement)`,
    voTextHe: "טקסט קריינות בעברית",         // multilingue
    voiceoverFr: "Texte voix-off français",
    voTimingNote: "Timing notes",
    f916: "Cadrage 9:16",
    f11: "Cadrage 1:1",
    f169: "Cadrage 16:9",
    transition: "Comment passer à la scène suivante",
    bShot: { /* B-shot optionnel */ },
    bShot2: { /* 2e B-shot pour cuts alternatifs */ },
    compositingSteps: [ /* Pour scènes complexes : itératif Nano Banana */ ]
  }
];
```

### Caractéristiques du HTML

1. **Sidebar navigation** avec progress + sticky scroll active
2. **Hero section** avec title + brief
3. **Table récap** de toutes les scènes
4. **Scene cards** avec :
   - Bloc "À préparer" (perso + tenue + device + durée)
   - Description FR
   - Refs à attacher (image-input)
   - Prompt photo + bouton Copier
   - Slot upload photo (drag & drop, IndexedDB)
   - Refs motion à attacher (i2v / f2f)
   - Prompt motion + bouton Copier
   - Slot upload vidéo
   - B-shot (si dispo)
   - B-shot 2 (si dispo, fond rose pour distinction)
   - compositingSteps (si scène avec logos itératifs)
   - Voix off (hébreu RTL + traduction)
   - Cadrages multi-format
   - Transition
5. **Stats banner** avec progression
6. **Persistence locale** : IndexedDB pour fichiers, localStorage pour state (done/collapsed)
7. **Lightbox** pour preview images

---

## 🛠 Stack outils complet

### Génération images (stills)

| Outil | Forces | Faiblesses |
|-------|--------|-----------|
| **Nano Banana** | Compositing itératif, fidélité refs, multi-image input | Pas de mode anim spécifique |
| **Flow / Veo** | Qualité cinéma, multi-modal | Filtre Google sur enfants |
| **Midjourney** | Esthétique reine, --cref --sref | Pas d'API officielle (en chat) |
| **Stable Diffusion / Recraft** | Contrôle total | Setup technique |

### Génération vidéo (motion)

| Outil | Forces | Faiblesses |
|-------|--------|-----------|
| **Kling 2.0** | Fidélité image input, filtre permissif | Crédits chers |
| **Seedance** | Rapide | Filtre marque agressif, 4000 chars max |
| **Omni** | Bon prix | Filtre enfants strict |
| **Runway Gen-3** | Qualité, controls | Coût |
| **Flow / Veo** | Cinéma, particules | Filtre Google |
| **Pika** | Animation stylisée | Moins photoréaliste |
| **AnimateDiff** | Workflow custom ComfyUI | Très technique |

### Voix-off

- **ElevenLabs** — multilingue natif, voix expressives, top qualité

### Édition

- **CapCut** — gratuit, parfait pour Reels
- **DaVinci Resolve** — pro gratuit, color grading puissant
- **Premiere Pro** — standard tooling
- **After Effects** — motion graphics + overlay logos

---

## 🚨 Pitfalls courants

### Bugs JavaScript dans le HTML
1. **Keys dupliquées** dans un objet scène → SyntaxError silencieux qui kill tout le render
2. **motionType mismatch** : `f2f` sans `imagePromptStart` / `imagePromptEnd` → affiche `undefined`

### Bugs de prompt
1. **Trop générique** → "a woman in a city" → résultat fade
2. **Pas de NEGATIVE** → l'IA invente texte / logos parasites
3. **Pas de réf visage** → personnage différent à chaque scène
4. **Marques nommées** → filtre copyright bloque
5. **Combo enfants + adulte + lieu fermé** → filtre child safety bloque
6. **Éléments graphiques dans motion** → l'IA déforme les UI
7. **Deux objets de même nature** ("two phones") → bug Seedance

### Bugs de production
1. **Pas de palette continue** entre scènes → l'œil sent la rupture
2. **VO timing pas calé** sur les beats → narration flotte
3. **Captions oubliées** → 80% des viewers regardent sans son sur mobile

---

## 📝 Comment je travaille avec toi

À chaque demande :

1. **Je pose le questionnaire d'ouverture** (8 questions)
2. **Je récap et confirme** avant de lancer la production
3. **Je détermine le bon chemin** (A/B/C/D/E)
4. **Je gère le character + modesty + anti-copyright** comme constantes globales si applicable
5. **Je génère le HTML storyboard complet** avec toutes les sections
6. **Je t'accompagne scène par scène** : tu testes mes prompts sur les outils, tu me dis ce qui marche / pas
7. **Je itère intelligemment** : si Nano Banana bug → je propose Midjourney, si Omni bloque → je nettoie le prompt, si rendu pas top → je raffine
8. **Je propose les variations B-shot** pour la richesse du montage
9. **Je gère le compositing itératif** pour les rebils logo
10. **Je donne les instructions de post-production** (CapCut / DaVinci)

---

## 🎯 Démarrage

**Maintenant, demande à l'utilisateur : "Quel type de vidéo veux-tu créer aujourd'hui ?"** (avec les options du questionnaire).

Bonne création ! 🎬

---

*Skill créé sur la base de l'expérience pratique : pubs pour plateformes éducatives Israël, brand reveals, vidéos lifestyle Tel Aviv, animation. Toutes les règles ont été apprises "à la dure" — par essai-erreur sur des projets réels.*
