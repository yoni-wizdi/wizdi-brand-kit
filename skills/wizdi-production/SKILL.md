---
name: wizdi-production
description: Règles de production Wizdi apprises projet après projet — Wizi et WizBuddy (armure, plastron, références), images générées (personnes israéliennes, école laïque, ordinateur jamais tablette, aucun texte), vidéo (3 formats 9:16 / 4:5 / 16:9, wizdi.school, −14 LUFS, règle d'Eyal pour l'interface), voix off hébreu (ElevenLabs, nikoud, Wiz Plène), textes et rôles, pages et RTL, interface WizPlan, directions refusées. À appliquer avec wizdi-brand dès qu'on produit une image, une vidéo, une voix, une page ou un texte Wizdi.
---

> Les chemins cités (`logos/`, `references/`…) sont relatifs au dépôt `wizdi-brand-kit`, cloné dans `~/wizdi-brand-kit`.

# Wizdi — règles de production

> **בעברית** — כאן כל הכללים שנצברו בעבודה עם יוני (מעודכן ל-17/11/2026): הינשוף ו-WizBuddy, תמונות,
> סרטונים, קריינות, טקסטים, דפים וממשק WizPlan. הם משלימים את `WIZDI-BRAND.md` (הזהות). Claude קורא את
> שניהם; אפשר לבקש ממנו להסביר כל כלל בעברית. במקרה של ספק או סתירה — שואלים את יוני, לא מחליטים לבד.

Ce fichier complète `WIZDI-BRAND.md` (l'identité) : ici, la façon de produire, apprise projet après
projet (à jour au 17/11/2026). En cas de doute ou de contradiction, demander à Yoni, ne pas trancher seul.
**Toute nouvelle création suit la nouvelle charte** (palette du 28/10, mondes PopBG, hiboux recolorés,
style pop) ; « comme avant » ne vaut que pour corriger un travail déjà fait dans l'ancien style.

## 1. Le hibou (Wizi en interne, « Wizdi » en public)

- **Dans tout texte public** (bulle, alt, aria-label, film, voix) le hibou s'appelle **« Wizdi »**
  (« היי! אני Wizdi. », « Wizdi, הינשוף הכחול »). « Wizi » n'est qu'un nom interne (fichiers `wizi*`).
- Anatomie constante : casque et armure complète, deux bras métalliques avec des mains, petites ailes
  dans le dos ; jamais une aile qui sert de bras. Debout plutôt qu'en vol.
- L'armure prend la couleur du module dans la **nouvelle palette du 28/10** : WizBook bleu roi ·
  WizPlan violet · WizPlay rose, jambes à ressorts · WizSpace or, plastron moutarde · WizChat orange ·
  WizBox vert. Un hibou bleu là où on attend la couleur du module se rejette ; un hibou aux anciennes
  couleurs (cuivre, teal, violet de WizChat) se remplace par le hibou recoloré du kit. Un visuel sans
  hibou reste tel quel.
- Poses recolorées approuvées : `references/wizi/modules/poses/` (animations : studio-wizdi.com/kit/).
  **Écartées pour toujours** : le clip `owl-wizbox` (lueur olive), les rafales `wizchat-point`
  (paupières violettes brillantes), `wizspace-wave` et `wizbook-joy` (yeux qui brillent, regard blasé) ;
  WizPlan « wave » au-delà de l'image 60 et « joy » au-delà de l'image 33. Le hibou WizBox vert garde
  des reflets brun-rouge : accepté, mais c'est un défaut connu.
- Expression chaleureuse, lumière claire : `friendly kind expression, never angry`, `NOT dark, no harsh
  shadows`. La variété passe par la pose et l'attitude, jamais par un visage durci ou une lumière dure.
  Trop enfantin : plan taille-buste centré sur le plastron, poses variées.
- Le plastron doit se lire : jamais de médaillon ou de recadrage qui le coupe. Son texte ne se décrit
  pas dans le prompt : on passe le wordmark rendu depuis `logos/wiz/*.svg` en image de référence (ou on
  corrige avec la plaque rendue). Zoomer sur chaque plastron avant de choisir (« WIZBOK », « EXRETLY »).
- Références : RÉF 1 = le hibou seul (`references/wizi/wizi-reference.webp`) — une scène en réf 1 fait
  dériver le personnage ; RÉF 2 = le hibou du module recoloré (`references/wizi/modules/<module>.webp`).
  Si l'image dérive vers le photoréalisme, remettre l'image de style en première référence comme
  `absolute style master`.
- Vrai mouvement seulement (vidéo générée, transfert, Kling Motion Control), jamais de pantin découpé ;
  ni greffe de bec, ni hibou ou WizBuddy en 3D Meshy / Blender. En vidéo, le hibou n'est jamais figé.
- Chaque personnage fait une action physique lisible avec un objet : contact, ombre portée, même
  lumière que le décor ; jamais d'autocollants qui flottent autour d'un écran.
- Hero de landing : scène photoréaliste (vraie enseignante ou vrai enfant qui utilise le produit) +
  le hibou officiel intégré en 3D. Refusés : un hibou réinventé, un poster réutilisé tel quel, une scène
  tout en 3D sans humain réel.
- Clip de personnage aux yeux blancs : réparer les yeux, puis contrôler image par image avant et après
  l'encodage.

## 2. WizBuddy

- WizBuddy est le bot de Wizdi : depuis le 08/11 (Eyal), une **bulle flottante en bas à gauche de
  chaque écran**, en plus du centre de formation (מרכז ההדרכה). Ne jamais poser la bulle là où le vrai
  produit ne la montre pas.
- Hibou 3D en combinaison blanche nacrée, casque à écouteurs blancs, petites ailes irisées ; plaque bleu
  nuit au liseré cyan, « Wiz » en bleu `#23A4D8` + « Buddy » en blanc. Hors de la plaque, sur fond clair :
  « Buddy » en bleu nuit `#1E1B4B` (`logos/wiz/WizBuddy.svg` ; sur fond sombre `WizBuddy-on-dark.svg`).
  Références : `references/wizi/wizbuddy/` (RÉF 1 = `wizbuddy-reference.webp`, RÉF 2 = `wizbuddy-plate.webp`).
- Voix du personnage : Amit `NbvR1eY6Q8ivACdEO8PV`. Dans la narration, « Wiz Buddy » en deux mots.
- Toujours mignon : jamais d'yeux lumineux, de reflet rétinien ni de regard « vision de nuit ».
  La nuit se raconte par des signes doux (bâillement, clin d'œil, lune).
- Toujours en pied, casque toujours présent, proportions de la référence. Zoomer sur chaque image :
  casque oublié, trous dans les mains, logo du plastron déformé. Poses écartées : `B2m-trampoline`,
  `B1m-appui` (corps troués). En Seedance, jamais de planche grise sous lui : magenta vif ou vert.
- Le lien avec l'enseignante passe par l'ordinateur portable : présent dans chaque plan commun,
  WizBuddy en sort ou est posé dessus ; l'écran se voit de dos. Tard le soir, c'est lui qui bâille.
- Il ne promet jamais ce qu'il ne fait pas : pas de מערך fabriqué, pas d'action dans le compte, pas
  de « 24/7 », pas de « מיד » (il répond en 3 à 20 secondes), pas d'usage par les élèves. Ses réponses à
  l'écran sont recopiées mot pour mot et revérifiées en ligne le jour même.
- Phrases de fin (Eyal, mot pour mot) : « הבוט החכם של מרכז ההדרכה של Wizdi » ·
  « מחכה לכם בלשונית מרכז ההדרכה, בתוך Wizdi ».

## 3. Images générées

**Avant de générer**
- Concept en 3 à 6 lignes, liste des images et coût estimé ; ensuite générer sans attendre si le
  budget est déjà autorisé. Toute dépense nouvelle : fournisseur, modèle, quantité et coût en une ligne,
  puis le feu vert. Une vidéo attend toujours le OUI sur ses images de départ.
- Réutiliser d'abord (kit général, hiboux, mondes, personnages), inventaire à l'appui.

**Qui et où**
- Toujours un ordinateur portable, jamais une tablette.
- Personnes israéliennes, décrites explicitement (sinon le résultat fait européen). Pour une enseignante :
  proposer d'abord les 3 profs validées (`references/personnes/`, GPT Image 2) ; recette :
  « Documentary-style candid photograph inside a real Israeli public elementary school classroom… No
  religious symbols. Eye level, 35mm lens ». Décor israélien : fenêtres en aluminium à moustiquaire,
  volets roulants, carrelage, chauffe-eau solaires, mobilier de salle des profs israélienne.
- École : bâtiments bas (1 à 3 étages), salle des profs au rez-de-chaussée ouverte sur la cour
  (enfants en t-shirt d'école, voiles d'ombrage, ficus), d'autres enseignants présents, de la vie dès
  la première image. Uniforme : t-shirt uni blanc ou bleu clair avec un petit emblème sans lettres.
- École publique laïque : aucun signe religieux chez les figurants ; dans le NEGATIVE :
  `no head scarf, no hijab`. Jambes couvertes, rien de « sexy ». Seule exception : une vidéo déjà
  publiée sur notre site (garçon à kippa de `wizplan-hw.mp4`) peut entrer dans un film.
- Selon le produit : WizPlan = l'outil de l'enseignante (elle au centre, aucun enfant sur
  ordinateur) ; WizPlay = un enfant seul, sans adulte, le monde des maths du jeu autour de lui ;
  couvertures de guides : un enfant pour les guides élèves, une enseignante ou un enseignant pour les
  guides profs, en train de faire l'action du guide.
- Cadrage : mettre en valeur l'outil ou l'écran, pas le visage ; la personne de côté ou de
  trois-quarts, en train d'utiliser.
- Continuité : mêmes figurants d'un plan à l'autre, un décor et un cadre stables par séquence, une
  image maîtresse par décor ; vérifier les visages de tous les plans en pleine résolution.
- Scène de classe : écran de projection déroulé devant le tableau blanc, projecteur au plafond ; jamais
  d'écran vide ; si les enfants regardent la caméra, le tableau est derrière la caméra ; décorations
  (fanions, dessins, plantes) et petit poster du hibou au mur, sans aucun faux mot. Couvertures du
  centre de formation : murs nus.

**Texte et éléments**
- Aucun texte lisible hors plastron : pictogrammes sans mots (`no words or labels inside the
  holograms`), vêtements unis, aucun logo tiers (pomme d'Apple, marques de vêtements).
- Un wordmark dans une image ne se décrit jamais en texte : on passe le wordmark rendu en référence,
  `reproduce EXACTLY the wordmark in the provided reference`.
- Réserver la place du titre : un tiers vide pour le titre en HTML ; en 9:16, le haut du cadre libre.
- Une rangée de cartes : scènes générées sans texte, le texte se pose en HTML.
- Éléments flottants : une tuile concrète par fonctionnalité (checklist = מערך, lecture + fraction =
  סרטונים, dés + puzzle = משחקים, ? → ✓ = משוב, maison = שיעורי בית), jamais d'icônes abstraites.
- L'IA ne compte pas : parts de pizza, fractions et nombres se posent en vectoriel par-dessus.

**Méthode et contrôle**
- Visuels de marque : blocs du skill `wizdi-visual-studio`. Scène photoréaliste : gabarit
  `Scene / Composition / Body language / Mood / Lighting / Environment / Logos / Style / High detail, 16:9`.
- Contrôler chaque image : bandes noires parasites, mauvais hibou, hibou en vol, logo Apple ajouté,
  faute sur le plastron.
- Retouche : dès qu'un montage demande plus d'un aller-retour, arrêter et générer 3 variantes ; le
  détourage n'est légitime que pour un placement au pixel près ; si un objet passe devant un écran,
  régénérer une base sans occlusion.
- Interface dans un écran : les 4 coins sont tracés par un humain avec le skill `video-in-video`.
- Faire valider avant de décliner un visuel (hero → piliers), en montrant 2 ou 3 candidates.
- Remplacer une image publiée = un NOUVEAU nom de fichier (WhatsApp et le CDN gardent l'ancienne).
- Recadrage : sujet dans le tiers central si l'image peut être repliée en bandeau ; vérifier un
  recadrage `cover` à 1440 et à 1920, ou mieux, donner au cadre le ratio de l'image.

## 4. Le style pop et les logos

- Chaque nouveau film ou visuel se pose sur le **monde PopBG du module** (`references/popbg/`, mode
  « normal » ou « calm » ; boucles vidéo sur studio-wizdi.com/kit/). Le style pop de Yoni : PopBG saturé
  de la couleur du Wiz, cartes à cadre blanc qui volent, mots en pilules qui claquent, coupes franches,
  pop à 120 BPM ; jamais le « bureau calme ».
- Hors productions השבחה : aucun ruban multicolore, aucun cube aux 5 couleurs (l'arc-en-ciel est la
  signature de השבחה).
- Sur de vrais rushes : habillage pop léger (liserés, ombres décalées, pastilles, formes) par-dessus des
  rushes en plein écran, jamais en fenêtres.
- Mondes clairs (or de WizSpace, orange de WizChat) : rayon court, voile et boutons foncés sous un texte
  blanc ; mesurer le contraste.
- Présenter un Wiz : apparition « פיצוץ » — le logo frappe avec une onde de choc, les objets jaillissent
  de derrière en arc, la description officielle monte mot à mot ; objets à 96 px au moins des bords,
  jamais sur le coin du QR, avec un liseré blanc ; dans une tuile de fin, objets au-dessus du logo ;
  réutiliser les 24 objets existants (`wizObjects.ts`), pas de nouveau dessin sans demande.
- Logos flottants : cycle aléatoire, environ 5 s par logo, une arrivée toutes les 2 à 2,6 s, 3 au plus
  sur ordinateur et 2 sur téléphone ; jamais de composition fixe, sauf sans animation.
- Le wordmark « Wizdi » se dessine toujours en vectoriel, jamais depuis une image ou une vidéo agrandie ;
  jamais d'ombre floue sur un logo. Plaques des logos claires sur les landings.
- Transitions « מעברי לוגו » (studio-wizdi.com/kit/#stings) : lettres du logo seules, très grandes,
  droites, contour blanc + filet + ombre ; le mot entier sur une ligne, du coin haut gauche au coin bas
  droit, jamais coupé ni vertical en 9:16 ; flash blanc et étoile bleu Wiz à 0,6 s, durée 1,5 s.
- Logos de la marque du film dès l'image 0 et pendant tout le film, en zone sûre, jamais sur un visage
  ni sur un cartouche (la marque du film, par exemple « יבנה בונוס | Wizdi »).

## 5. Vidéo : formats et livraison

- 3 formats : REEL 9:16 (1080×1920 : Reels, Stories, Shorts, TikTok, statut WhatsApp) · FEED 4:5
  (1080×1350 : fil Instagram et Facebook) · YOUTUBE 16:9 (1920×1080) + miniature ; plus une version
  WhatsApp légère de moins de 16 Mo. **On travaille d'abord le 9:16** ; le 4:5 et le 16:9 se lancent
  après le OUI de Yoni. Reels d'événement : ajouter une story.
- Chaque format est composé pour son cadre. En vertical, l'interface d'un produit garde ses
  proportions : écran 16:9 au milieu, titre en grand au-dessus, mot-clé dessous.
- **Couverture = image 0 de chaque fichier**, masters HD compris : une vraie mise en page (titre, hibou
  3D, vrai écran) déclinée par format ; logo, titre et hibou dans le carré central que WhatsApp garde en
  aperçu (9:16 : y 420 à 1500 ; 4:5 : y 135 à 1215 ; marge d'environ 40 px).
- Adresse affichée : **« www.wizdi.school »**, toujours avec www (la voix peut dire
  « הִיכָּנְסוּ לְwizdi דוֹט סְקוּל ») ; jamais studio-wizdi.com. Le QR peut mener ailleurs (par
  exemple un formulaire). Pub Meta pour des leads : l'appel à l'action est le bouton de la pub, pas
  d'URL à l'écran ; ne jamais évoquer le « דמו חי ».
- Zones sûres : Meta, 15 % en haut et 22 % en bas laissés vides ; télé, environ 5 % de marge
  (x 100–1820, y 70–1010 en 1080p). Contrôler image par image les 3 formats : aucun texte sur un visage
  ni sur le hibou.
- Reels de 5 s : 0–1,5 s accroche ; 1,5–4 s hibou en mouvement ; 4–5 s hibou + logo ; la première
  coupe à 1,5 s est sacrée ; MP4 H.264, AAC ; même police, même musique et même place du logo sur toute
  une série.
- Son : mixage à −14 LUFS en gain fixe (ebur128) ; bruitages de la bibliothèque CC0 Kenney ; musique
  ElevenLabs Music (phrases de 4 mesures, soit 7,5 s à 128 BPM : plan en sections de 7 500 ms, 3 prises
  mesurées) ; jamais de bruitage sur le mot d'appel ; fin sans silence.
- Pages de relecture : une page de corrections scène par scène à chaque livraison ; au-dessus de chaque
  lecteur, logo + nom de la plateforme + format (9:16 → Instagram · 4:5 → WhatsApp · 16:9 → YouTube).
- Message WhatsApp à copier pour chaque vidéo (en hébreu) : ouverture « מורות ומורים יקרים 👋 », une
  accroche-question, des étapes 1️⃣ à 4️⃣, contact 📱 050-2266380, clôture « מחכים לכם! 🦉💙 », sans
  lignes vides ; signature « שלכם צוות יבנה בונוס - Wizdi 🦉🩵 » puis « 📱 052-2881720 ». Le texte de
  Yoni s'il en donne un, mot pour mot.
- Rangement : Drive « WIZ PROJECT », dossier du produit (WizBuddy → « מרכז ההדרכה »), un sous-dossier
  par production nommé `AAAA-MM-JJ · <nom en hébreu>` ; la plus récente porte « ★ » (retiré de la
  précédente) ; les doublons vont dans `ארכיון · כפילויות`, jamais supprimés ; une ligne dans l'onglet
  `יומן שינויים` du tableur WIZ FEATURES. Noms : `<produit>-9x16-HD.mp4`, `<produit>-Cover.jpg`,
  `<produit>-4x5-WhatsApp.mp4`, `<produit>-16x9-YouTube-HD.mp4`.
- Après chaque création : l'ajouter au kit général (studio-wizdi.com/kit/) et à la page /links/ ;
  éléments réutilisables transparents en MOV ProRes 4444 alpha, WebM VP9 alpha, MP4 sur vert `#00B140`
  et PNG.

## 6. Vidéo : écriture, méthode, mise en scène

- La narration d'abord : texte → voix → instants des mots ; l'image et le son se calent dessus. Une
  phrase du script = une scène ; mots verbatim qui claquent.
- Méthode validée (09/11) : 1. réutiliser d'abord ; 2. devis, puis vrais clips ; 3. jury de 3 agents sur
  la VRAIE vidéo (rédacteur hébreu, DA/motion, ingénieur son qui mesure les pistes), avec instants et
  valeurs ; 4. appliquer tout de suite les corrections DA et son ; 5. deux scripts sur le même montage,
  page de choix en hébreu avec vote (👍/👎 par image et par direction) ; 6. Yoni puis Eyal choisissent ;
  7. ensuite seulement texte, lipsync, 3 formats. Le jury conseille, les humains choisissent.
- Jury avant tout envoi : DA senior et motion design senior, image par image, comparés au pilote
  validé, plus un juré « marque et logos » qui lit le kit ; un changement global repasse devant le
  jury ; jamais de « premier montage » envoyé pour voir ; une petite correction = un seul rendu.
- Pas d'essais en rafale : confier le film à un motion designer senior (skill `wizdi-motion-senior`)
  avec toutes les consignes ; Yoni ne voit qu'un résultat fini, en situation. Décider sur un test en
  mouvement de 10 s, pas sur des planches fixes. Jamais le modèle d'artifact « Motion » (rendu
  « slides ») pour un film Wizdi.
- Plusieurs directions = des mondes totalement différents (concept, décor, voix, genre musical,
  caméra), jamais le même moteur repeint.
- Ouverture : une image humaine comprise en 0,5 s ; jamais un document de travail en accroche. Le
  contexte annoncé se voit dès la première seconde.
- Rythme (Eyal) : seulement des contenus approuvés par la pédagogie ; un moment ne passe qu'une fois ;
  extraits accélérés ×1,3 à ×2 ; coupes sur les temps mesurés, musique vers 128 BPM, batterie dès la
  première image ; aucun plan fixe ; pas d'éclair blanc à chaque coupe, pas de secousse sur un plan réel.
- Montrer l'interface : écran entier → repère → le morceau sort vivant de sa place, dans sa vraie
  forme. Pour lire : caméra qui serre la zone utile (1× la source au plus) ; un petit élément important
  s'entoure au feutre puis se refait en grand en vectoriel ; texte de 28 px au moins sur téléphone, une
  zone utile à la fois, jamais l'écran entier en petit, aucune ligne coupée. Le vrai écran est un appui
  court, jamais la colonne du film.
- Données réelles seulement : libellés réels du produit, vraies captures ; un champ vide reçoit une
  valeur d'exemple marquée « à valider ».
- Aucune provenance interne à l'écran (« שאלה 1 », jamais « מההקלטה של אייל »), aucun nom de
  l'équipe ; les noms visibles dans les captures sont retirés par recadrage.
- Tutoriel d'écran fourni par l'équipe : parcours, voix et texte mot pour mot (seule exception :
  Wizdi en latin) ; couper ou accélérer seulement dans les silences de la voix.
- Pub Instagram ou réseau social : pop et « waouh » — mots géants sur la voix, zooms sur le vrai outil,
  apparition « פיצוץ », ouverture et fermeture écrites pour le sujet ; plus de style « sobre premium »
  ni « interface futuriste ».
- **Fermeture de cinéma**, écrite pour le sujet de chaque film (et passée au jury) : 1 ou 2 plans
  générés qui bouclent l'histoire avec un espace vide pour le logo ; le code ne pose que la marque
  par-dessus (éclat du logo : flash, rayons, dépassement d'échelle ; badge ; adresse et signature en bas
  sur un dégradé lisible) ; jamais de carton plat ni de dégradé plein écran ; vérifier les 3 formats.
- Toujours signer la fin : logo Wizdi dessiné, le hibou, « היכנסו ל-www.wizdi.school » (à l'écran et
  dit par la voix), les Wiz concernés, « Wizdi מבית Yavne Bonus », copyright. Exception : une vidéo
  d'événement finit sur son propre appel (« מחכים לכם בדוכן 15 »), sans la plaque www.
- Contrôle : une grille écrite, zéro chevauchement sur toute la durée, chaque scène en pleine
  résolution ; les objets qui volent passent sous les textes ; interface capturée en HD pour être
  montrée à 1x ; le mix final s'écoute par un humain et se transcrit mot à mot.

## 7. Modèles vidéo (constats mesurés)

- Kling 4.0 (1080p) : garde les visages et le badge ; en image-vers-vidéo seule l'image de départ passe ;
  début et fin imposés = bonnes transitions entre deux mondes (jouer jusqu'à la dernière image, faire
  repartir le monde suivant de 0).
- Seedance 2.5 : le meilleur pour plusieurs personnages et les gestes ; brouillon en 480p puis finale
  en 1080p depuis le brouillon ; contre le strabisme : « her gaze rests on the screen, both eyes
  parallel, never crossed » ; pas de « salle qui tourne » (affiches à faux texte) ; pour un clip à
  détourer : « Wide shot, full body … visible from head to feet at every moment, about 45% of the frame
  height … no zoom » ; refuser le préréglage « IN THE DARK ».
- Cinema Studio 4.0 : le plus beau mouvement de caméra, à réserver aux plans où les visages sont petits.
  Veo 3.1 : écarté. Jamais de symbole chimique ni de mot à afficher dans un prompt vidéo : décrire l'objet.
- Lipsync : Wan 2.7, avec un audio d'au moins 3,2 s ; Seedance 2.0 Mini refusé.
- Contrôle et rendu : 2 prises par plan ; contrôle par bandes de 4 images puis zoom sur les yeux ; clips
  IA joués ×1,3 ; jamais de ralenti non interpolé ; rendre à 24 i/s quand les clips sont à 24 i/s.

## 8. Voix off

- **Voix par défaut de tous les projets : HE Tamar** `p7J75VowGmxi3K0it9lN`, eleven_v4, langue `he`,
  stabilité 0,35, similarité 0,75, vitesse 1,0, une balise d'intonation par phrase. Un film déjà narré
  garde sa voix. Pubs Instagram et reels d'événement : Brittney `XiPS9cXxAVbaIWtGDHDh` (Tamar seule y a
  paru plate). Source de vérité des voix : studio-wizdi.com/kit/#voices (la recopier dans tout brief).
- Autres voix : Audrey `McVZB9hVxVSk3Equu8EH` · Amit `NbvR1eY6Q8ivACdEO8PV` (WizBuddy) · Charles,
  HE Shira, HE Dana.
- Dans le texte donné à la voix (jamais affiché) : « WizPlan » s'écrit « Wiz Plène » ; « Wizdi » reste
  en latin (jamais « ויזדי »). À l'écran, les noms restent en latin.
- Nikoud seulement sur les mots ambigus (לַמּוֹרֶה · לִצְפּוֹת · הַשְׁבָּחָה · אֶמְצְעֵי הַמְחָשָׁה ·
  אָלֶף עַד וָו · בְּמָה · הַדַּקּוֹת · הַשְׁעָרוֹת · מְחַכִּים · לְסַקְרֵן · לִמְדֻיָּק · הַשֶּׁנֶת), jamais sur
  tout le texte ; sans nikoud, Tamar dit « מחכים » comme « נחקים ». Orthographe phonétique permise.
- Doute de prononciation : un fichier par variante (le mot seul deux fois, puis la phrase) ; relire
  les homographes avant de générer ; c'est l'oreille de Yoni qui tranche (il choisit les prises dans son
  studio de voix local).
- Intonation : une balise devant chaque phrase (`[curious]` `[excited]` `[enthusiastically]`
  `[cheerfully]` `[warmly]` `[playfully]` `[proudly]`), mots et ponctuation inchangés, 2 prises ;
  éviter `[softly]` (elle chuchote), préférer `[gently]` ; mesurer le volume de chaque phrase. Le
  paramètre `speed` de la v4 ne fait rien : étirer la voix avec rubberband.
- La voix lit l'écran mot pour mot.

## 9. Textes, noms et rôles

- Descriptions officielles des Wiz, mot pour mot, pour présenter un Wiz :
  WizBook « ספרים אינטראקטיביים חכמים » · WizPlan « מערכי שיעור אינטראקטיביים מוכנים מראש » ·
  WizPlay « סביבות משחקים ללומד העצמאי » · WizBox « מחולל מבדקים ודפי עבודה » ·
  WizChat « סוכני הוראה מבוססי AI » · WizSpace « מאגר תכנים אינטראקטיביים ».
  Les slogans des posters (« מתמטיקה שתלמידים אוהבים! », « כל שיעור שלך מוכן! ») restent pour les films
  et visuels de campagne.
- « WizPlan 3 » est un nom interne : en public, « WizPlan ».
- Noms des modules en un seul mot (WizChat, jamais « Wiz Chat ») ; aucun mot anglais hors noms de marque.
- Qui décide : Eyal = verdict, structure, dates (son « non » est définitif) ; Yoni = arbitre ; Eden =
  retours produit et pédagogiques. Contradiction : la signaler à Yoni, appliquer la dernière demande,
  garder l'ancienne version. Ne rien demander à préparer à Eyal : trouver soi-même, noter les choix
  par défaut sur la page de relecture ; s'il le faut vraiment, une seule question, par Yoni.
- Textes fournis : mot pour mot, mais relire l'orthographe hébraïque (ע/א, כ/ח, ט/ת, ו/י) ; une faute
  évidente se corrige et se signale. Une consigne tapée vite qui n'a pas de sens se comprend, elle ne
  se recopie pas.
- Yavne Bonus est la maison mère des personnages, des livres et de Wizdi : aucun accord à demander.
- Pas de phrase construite sur une négation (sauf les accroches WizPlay et WizSpace) ; une accroche
  crée une tension ; « ואת? » est réservé à WizBook. Le mot-choc a son traitement.
- Public : enseignantes de 21 à 62 ans (campagnes autour de 45 ans) ; leur douleur : la charge de
  travail après les heures de cours.
- Le mot « חשיפה » est banni. CTA du formulaire : « טופס ליצירת קשר וקבלת מידע נוסף » ; bouton
  d'envoi : « שליחת טופס ».
- Pas de tiret long (—) dans le texte visible : un tiret court. Bidi : entourer les dates et les
  passages latins ou chiffrés d'isolats U+2066…U+2069 ; sur un titre avec voyelles, l'ombre se met sur
  les lettres seulement.
- Pages et documents destinés à l'équipe : en hébreu.
- « Réutiliser X » = exactement le même contenu, refait dans notre style.

## 10. Pages, og:image, Instagram

- Les landings et la page master /wiz/ sont en **style pop** (direction A « עולם פופ » pour /wiz/).
- Gabarit de landing : TopStrip · Hero · TrustBar · Pillars · VideoBand · LeadForm · FAQ · Footer.
  Pas de section témoignages.
- Formulaire : שם מלא, טלפון, תפקיד, שם בית הספר (requis), יישוב (requis), סמל מוסד (facultatif,
  numérique), אימייל. Champ téléphone en `dir="rtl"`.
- Pages outil : « סולידי נקי ברור », « נקי, יוקרתי, רגוע » : pas un document marketing, zéro décor,
  pas de mascotte semée partout, page courte.
- Pas de répétition : le wordmark d'un module une seule fois par carte, le nom une seule fois par
  zone ; sections séparées par l'espace (ni bandes grises, ni boîtes dans des boîtes).
- RTL : le premier enfant d'une grille ou d'un flex est à droite ; badges dans les coins droits ;
  filet d'accent en `border-s` ; flèche « suivant » = flèche gauche, en dernier ; ne jamais retourner
  l'universel (▶, logos, chiffres) ; vérifier dans le DOM.
- Survol réservé à la souris ; pas de flottement perpétuel. Jamais de bandes floues pour faire tenir
  une image : recadrage centré.
- Chaque page : un bouton de retour vers la page master et un lien vers www.wizdi.school sous le hero.
- **og:image sur chaque page dès sa mise en ligne** : `og:title`, `og:description`, `og:url`,
  `og:image` (+ largeur 1200, hauteur 630, type), `og:locale he_IL`, `twitter:card
  summary_large_image` ; URL absolues `https://studio-wizdi.com/...` ; image 1200×630 d'environ 100 Ko,
  tirée de la couverture 16:9 ou d'une carte au style pop ; nouveau nom de fichier à chaque refonte ;
  textes mot pour mot ; vérifier avec `curl -A "WhatsApp/2.23.20.0 A"`.
- Un HTML envoyé en fichier intègre Fredoka et Baloo en `data:` et porte `<meta charset>`.
- Noms de pages et de fichiers publiés en anglais ou en hébreu phonétique, jamais en français.
- Grille Instagram : des rangées d'une seule couleur, une rangée par Wiz, à la suite, jamais de
  couleurs mélangées ; titres des couvertures repris mot pour mot des légendes. Ordre de travail :
  vitrine d'abord (bio, lien, logo Wizdi seul, highlights, 3 publications épinglées), puis 30 jours à 3
  posts par semaine, puis seulement la pub Meta.
- Méthode : montrer une direction (référence + maquette) avant de produire ; faire exactement ce qui
  est demandé, ne pas refaire un travail validé ; propager une correction à toutes les pages concernées.

## 11. Interface WizPlan (invariants d'Eyal)

- Figés : les icônes des types de contenu (on change le fond, la taille ou le halo, jamais l'icône :
  « אייקונים חדשים לא ייכנסו למוצר ») ; les couleurs des 7 étapes et des 3 niveaux de maîtrise ; la
  maîtrise en disque de lune (pleine, demi, croissant), un tiret si non marquée, jamais de score
  pondéré ; une seule règle de couleur, celle de l'étape ; vert, ambre et rouge réservés à la maîtrise.
- Interdits : carte dans une carte, consigne répétée, faux succès d'envoi, texte pour l'enseignante
  sur l'écran de la classe, commande visible seulement au survol. Le vide reste visible.
- Valeurs : courbe `cubic-bezier(.45,0,.18,1)` ; échelle typographique 12·13·14·16·18·24·28·34 ;
  points de rupture 1440 / 1180 / 1024 ; cibles de 44 px ; menu 340 / 74 px ; 3 états par écran de
  données (données / démo marquée / vide).
- Vocabulaire : תוכן (pas פריט), סיכום הנושא הקודם, תרגול (א׳–ג׳) / משימות נוספות (ד׳–ו׳), סיום
  נושא ; ton neutre au pluriel. Tout changement passe par Eyal.
- Les notes des élèves se montrent depuis un vrai écran WizPlan (carte « משימה N נשלחה לכיתה »).

## 12. Personnages השבחה (productions השבחה seulement)

- Peau lisse et mate, façon figurine vinyle (« SMOOTH SKIN: absolutely no fur… ») ; jamais poilus.
- Noms officiels du livre : טופי, מנגו, לובי, שמש, גוגו, טיגי. Couleurs : מנגו `#F08518` / `#F2B076` /
  iris `#8C543E` · טופי `#EDADBF` / `#F6CFCF` / iris `#CD9EC8` · שמש `#E9CC1B` / `#F8ED9F`.
- Couleurs השבחה (logo et monde) réservées aux productions השבחה : cubes `#E35E71 #F6C856 #005880
  #3D99D4 #7BC143`, monde `#3C99D4` / `#035881` / `#D6ECFA` (`tokens/palette/tokens.css`).
- Les clips des personnages détourés sont sur studio-wizdi.com/kit/.

## 13. Déjà refusé (en plus de `WIZDI-BRAND.md` §11)

- **Les anciennes couleurs** des Wiz, et tout hibou aux anciennes armures, dans une nouvelle création.
- Pages : une image générée par groupe ; un index en colonne latérale ; un sommaire en colonnes de
  liens ; une carte par vidéo sur toute la page ; le style « quiet » façon Quizlet ; la page blanche
  « Apple » à bandes grises ; le livre ou le pop-up en papier comme concept.
- Hibou : menaçant (`cinematic, deep shadows… NOT cartoon-cute`) ; médaillon rond qui coupe le
  plastron ; pantin découpé ; « Wizi » ou « WizPlan 3 » dans un texte public.
- Films : typographie 3D extrudée façon Katana, objets 3D codés ; « Wiz Universe » ; documentaire
  animalier IA ; mots en 3D ; décor de ville, bureau en étage, saut cuisine → canapé ; ouverture sur
  un tableur ; fonds abstraits orange ou « couleurs de la leçon » ; nos images existantes posées en
  fond ; simulation codée à la place de vraies captures ; six écrans de texte dans un film de 45 s ;
  carton de fin plat, fermeture générique plaquée ; fond bleu étoilé à rayons ; style « interface
  premium futuriste » pour une pub réseau ; le modèle d'artifact « Motion ».
- Images : bougies en rangées dans le noir et flamme seule sur fond noir (rappel de יום הזיכרון ; une
  bougie se montre en plein jour, dans un contexte d'expérience) ; arc-en-ciel ou cubes השבחה hors
  השבחה ; planche grise sous WizBuddy ; montages et déformations de perspective faits à la main ;
  masque automatique ; interface WizPlan recomposée en 9:16.
- Outil WizPlan : le cadran ; les icônes en pâte à modeler 3D ; le hibou à côté du point ou dans le menu.
