# Wizdi — règles de production

> **בעברית** — כאן כל הכללים שנצברו בעבודה עם יוני: Wizi ו-WizBuddy, תמונות, סרטונים, קריינות,
> טקסטים, דפים וממשק WizPlan. הם משלימים את `WIZDI-BRAND.md` (הזהות). Claude קורא את שניהם; אפשר
> לבקש ממנו להסביר כל כלל בעברית. במקרה של ספק או סתירה — שואלים את יוני, לא מחליטים לבד.

Ce fichier complète `WIZDI-BRAND.md` (l'identité) : ici, la façon de produire, apprise projet après
projet. En cas de doute ou de contradiction, demander à Yoni, ne pas trancher seul.

## 1. Wizi, le personnage

- Anatomie constante : casque et armure complète, deux bras métalliques avec des mains, petites ailes
  dans le dos ; jamais une aile qui sert de bras. Debout plutôt qu'en vol.
- L'armure prend la couleur du module : un hibou bleu là où on attend la couleur du module se rejette.
  Armures des posters : WizPlan cuivre-orange · WizPlay argent-jaune, jambes à ressorts · WizBook
  argent-teal · WizChat argent-violet néon, jets aux pieds · WizBox bronze-cuivre · WizSpace blanc-or.
- Expression chaleureuse, lumière claire : `friendly kind expression, never angry`, `NOT dark, no harsh
  shadows`. La variété passe par la pose et l'attitude, jamais par un visage durci ou une lumière dure.
  Trop enfantin : plan taille-buste centré sur le plastron, poses variées.
- Le plastron doit se lire : jamais de médaillon ou de recadrage qui le coupe.
- Le texte du plastron ne se décrit pas dans le prompt : on passe le wordmark rendu depuis
  `logos/wiz/*.svg` en image de référence (ou on corrige avec la plaque rendue). Zoomer sur chaque
  plastron avant de choisir (déjà vu : « WIZBOK », « EXRETLY »).
- Références : RÉF 1 = Wizi seul (`references/wizi/wizi-reference.webp`) — une scène en réf 1 fait
  dériver le personnage ; RÉF 2 = la source du plastron : le Wizi du module au vrai logo
  (`references/wizi/modules/<module>.webp`) ou son poster (`references/campaign/`). Poses détourées
  prêtes à l'emploi : `references/wizi/modules/poses/`. Si l'image dérive vers
  le photoréalisme, remettre l'image de style en première référence comme `absolute style master`.
- En vidéo, Wizi n'est jamais figé : il est animé ; réutiliser d'abord ses animations existantes.
- Hero de landing : scène photoréaliste (vraie enseignante ou vrai enfant qui utilise le produit) +
  le Wizi officiel intégré en 3D. Refusés : un hibou réinventé, le poster réutilisé tel quel, une
  scène tout en 3D sans humain réel.

## 2. WizBuddy

- WizBuddy est le bot du centre de formation (מרכז ההדרכה), pas un module : hibou 3D en combinaison
  blanche nacrée, casque à écouteurs blancs, petites ailes irisées ; plaque bleu nuit au liseré cyan,
  « Wiz » en bleu `#23A4D8` + « Buddy » en blanc. Hors de la plaque, sur fond clair : « Buddy » en bleu
  nuit `#1E1B4B` (`logos/wiz/WizBuddy.svg` ; sur fond sombre `WizBuddy-on-dark.svg`). Références :
  `references/wizi/wizbuddy/` (RÉF 1 = `wizbuddy-reference.webp`, RÉF 2 = `wizbuddy-plate.webp`).
- Prononciation dans la voix : « Wiz Buddy », en deux mots.
- Toujours mignon : jamais d'yeux lumineux, de reflet rétinien ni de regard « vision de nuit ».
  La nuit se raconte par des signes doux (bâillement, clin d'œil, lune).
- Toujours en pied, casque toujours présent, proportions de la référence. Zoomer sur chaque image :
  casque oublié, trous dans les mains, logo du plastron déformé.
- Le lien avec l'enseignante passe par l'ordinateur portable : présent dans chaque plan commun,
  WizBuddy en sort ou est posé dessus ; l'écran se voit de dos.
- Tard le soir, c'est WizBuddy qui bâille, pas l'enseignante.
- Il ne promet jamais ce qu'il ne fait pas : pas de מערך fabriqué, pas d'action dans le compte, pas
  de « 24/7 », pas de « מיד » (il répond en 3 à 20 secondes), pas d'usage par les élèves. Ses
  réponses à l'écran sont recopiées mot pour mot et revérifiées en ligne le jour même.
- Phrases de fin, mot pour mot : « הבוט החכם של מרכז ההדרכה של Wizdi » ·
  « מחכה לכם בלשונית מרכז ההדרכה, בתוך Wizdi ».

## 3. Images générées

**Qui et où**
- Toujours un ordinateur portable, jamais une tablette.
- Personnes israéliennes, décrites explicitement (sinon le résultat fait européen) ; une vraie photo
  d'enseignante en référence quand c'est possible. Décor israélien : fenêtres en aluminium à
  moustiquaire, volets roulants, carrelage, chauffe-eau solaires, mobilier de salle des profs israélienne.
- École : bâtiments bas (1 à 3 étages), salle des profs au rez-de-chaussée ouverte sur la cour
  (enfants en t-shirt d'école, voiles d'ombrage, ficus), d'autres enseignants présents, de la vie dès
  la première image. Uniforme : t-shirt uni blanc ou bleu clair avec un petit emblème sans lettres
  (un arbre dans un cercle).
- École publique laïque : aucun signe religieux chez les figurants ; dans le NEGATIVE :
  `no head scarf, no hijab`. Jambes couvertes, rien de « sexy ».
- Selon le produit : WizPlan = l'outil de l'enseignante (elle au centre, aucun enfant sur
  ordinateur) ; WizPlay = un enfant seul, sans adulte, le monde des maths du jeu matérialisé autour de
  lui ; couvertures de guides : un enfant pour les guides élèves, une enseignante ou un enseignant
  pour les guides profs, en train de faire l'action du guide.
- Cadrage : mettre en valeur l'outil ou l'écran, pas le visage ; la personne de côté ou de
  trois-quarts, en train d'utiliser.
- Continuité : mêmes figurants d'un plan à l'autre, un décor et un cadre stables par séquence, une
  image maîtresse par décor ; vérifier les visages de tous les plans en pleine résolution.
- Scène de classe : écran de projection déroulé devant le tableau blanc, projecteur au plafond (pas
  d'écran plasma) ; jamais d'écran vide blanc ou gris ; si les enfants regardent la caméra, le tableau
  est derrière la caméra ; décorations (fanions, dessins, plantes) et petit poster de Wizi au mur,
  sans aucun faux mot. Couvertures du centre de formation : murs nus.

**Texte et éléments**
- Aucun texte lisible hors plastron : pictogrammes sans mots (`no words or labels inside the
  holograms` — un nom d'icône écrit dans le prompt finit écrit dans l'image), vêtements unis, aucun
  logo tiers (pomme d'Apple sur l'ordinateur, marques de vêtements).
- Un wordmark dans une image (sticker, écran) ne se décrit jamais en texte : on passe le wordmark
  rendu en référence, `reproduce EXACTLY the wordmark in the provided reference`.
- Réserver la place du titre : un tiers vide pour le titre en HTML ; en 9:16, le haut du cadre libre.
- Une rangée de cartes : scènes générées sans texte, le texte se pose en HTML.
- Éléments flottants : une tuile concrète par fonctionnalité (checklist = מערך, lecture + fraction =
  סרטונים, dés + puzzle = משחקים, ? → ✓ = משוב, maison = שיעורי בית), jamais d'icônes abstraites.
- L'IA ne compte pas : parts de pizza, fractions et nombres se posent en vectoriel par-dessus.

**Méthode**
- Visuels de marque : blocs du skill `wizdi-visual-studio`. Scène photoréaliste : gabarit
  `Scene / Composition / Body language / Mood / Lighting / Environment / Logos / Style / High detail, 16:9`.
- Contrôler chaque image : bandes noires parasites, mauvais hibou, hibou en vol, logo Apple ajouté,
  faute sur le plastron.
- Retouche : dès qu'un montage demande plus d'un aller-retour, arrêter et générer 3 variantes ; le
  détourage n'est légitime que pour un placement au pixel près ; si un objet passe devant un écran,
  régénérer une base sans occlusion.
- Interface dans un écran : les 4 coins sont tracés par un humain avec le skill `video-in-video`,
  jamais devinés, jamais de masque automatique.
- Faire valider avant de décliner un visuel (hero → piliers), en montrant 2 ou 3 candidates. Avant
  toute dépense : annoncer en une ligne le fournisseur, le modèle, la quantité et le coût, et attendre
  le feu vert.
- Remplacer une image publiée = un NOUVEAU nom de fichier (WhatsApp et le CDN gardent l'ancienne en
  cache plusieurs jours).
- Recadrage : sujet dans le tiers central si l'image peut être repliée en bandeau ; vérifier un
  recadrage `cover` à 1440 et à 1920, ou mieux, donner au cadre le ratio de l'image.

## 4. Vidéo : formats et livraison

- Toujours 3 formats, sans demander le canal : REEL 9:16 (1080×1920 : Reels, Stories, Shorts,
  TikTok, statut WhatsApp) · FEED 4:5 (1080×1350 : fil Instagram et Facebook, et c'est la version
  WhatsApp) · YOUTUBE 16:9 (1920×1080) + miniature 16:9 ; plus une version légère de moins de 16 Mo.
- Chaque format est composé pour son cadre, jamais recadré depuis un autre ; en 9:16, chaque décor est
  réinventé par génération (même lieu, même personne, même lumière).
- En vertical, l'interface d'un produit garde ses proportions : écran 16:9 au milieu du cadre, titre
  en grand au-dessus, mot-clé dessous, la caméra zoome dans l'écran. L'ouverture et la fin (hibou,
  logo) se composent en vertical.
- Couverture = la carte de fin, posée en première image pendant 0,2 s.
- L'URL de fin, le QR code et le lien de pied de page mènent toujours à wizdi.school, y compris pour
  un film du centre de formation.
- Zones sûres : Meta, 15 % en haut et 22 % en bas laissés vides ; télé, environ 5 % de marge
  (x 100–1820, y 70–1010 en 1080p).
- Reels de 5 s : 0–1,5 s accroche ; 1,5–4 s hibou en mouvement ; 4–5 s hibou + logo ; la première
  coupe à 1,5 s est sacrée ; MP4 H.264, AAC, 30 i/s ; texte entre y=300 et y=1200 ; même police, même
  musique et même place du logo sur toute une série.
- Mixage à −14 LUFS. Musique et bruitages synthétisés, sans banque de sons.
- Pages de relecture : au-dessus de chaque lecteur, logo + nom de la plateforme + format
  (9:16 → Instagram · 4:5 → WhatsApp · 16:9 → YouTube), petit logo sur chaque bouton de
  téléchargement et chaque onglet ; sous le 9:16 : « לוואטסאפ שולחים רק את גרסת 4:5 ».
- Rangement : Drive « WIZ PROJECT », dossier du produit (WizBuddy → « מרכז ההדרכה »), et une ligne
  dans l'onglet `יומן שינויים` du tableur WIZ FEATURES. Noms : `<produit>-9x16-HD.mp4`,
  `<produit>-Cover.jpg`, `<produit>-4x5-WhatsApp.mp4`, `<produit>-16x9-YouTube-HD.mp4`.

## 5. Vidéo : écriture et mise en scène

- La narration d'abord : texte → voix → instants des mots ; l'image et le son se calent dessus.
- Ordre de validation : textes de la voix (Yoni, puis Liad) → hiboux → décors → voix. Rien ne se
  génère avant.
- Plusieurs directions = des mondes totalement différents (concept, décor, voix, genre musical,
  caméra), jamais le même moteur repeint.
- Une proposition se montre en mouvement : film ou aperçu narré (vraie voix, musique, vrais écrans),
  jamais des images fixes ou des animatiques muets.
- Ouverture : une image humaine comprise en 0,5 s ; jamais un document de travail (tableur) en
  accroche. Le contexte annoncé (« un groupe WhatsApp ») se voit dès la première seconde.
- Montrer l'interface : écran entier → repère → le morceau sort vivant de sa place, dans sa vraie
  forme ; jamais de zoom ou de recadrage isolé (« לא מבינים מה רואים ») ; écran entier et
  rectangulaire, haut non coupé ; un livre en portrait ; pour agrandir, un accordéon plutôt qu'un
  zoom. Montrer le chemin complet (question → réponse → clic sur la source → la bonne page), lisible
  sur téléphone.
- Le réel n'est qu'un aperçu en quelques plans ; le corps du film, c'est l'outil en motion design.
- Grammaire validée : couleurs de texte de la marque, hibou 3D, animations GSAP en 2D, vraie interface
  qui sort de l'écran ; style « pop ».
- Données réelles seulement : libellés réels du produit, vraies captures (jamais une simulation
  codée) ; un champ vide reçoit une valeur d'exemple marquée « à valider ».
- Aucune provenance interne à l'écran (« שאלה 1 », jamais « מההקלטה של אייל »), aucun nom de
  l'équipe ; les noms visibles dans les captures sont retirés par recadrage.
- Tutoriel d'écran fourni par l'équipe : parcours, voix et texte mot pour mot (seule exception :
  Wizdi en latin) ; couper ou accélérer seulement dans les silences de la voix.
- Contrôle : une grille écrite, des zones qui ne se croisent jamais (zéro chevauchement sur toute la
  durée), chaque scène regardée en pleine résolution ; les objets qui volent passent sous les textes.
  Interface capturée en HD pour être montrée à 1x ; une découpe n'est jamais agrandie. Le mix final
  s'écoute par un humain et se transcrit mot à mot.

## 6. Voix off

- Dans le texte donné à la voix (jamais affiché) : « WizPlan » s'écrit « Wiz Plène » ; « Wizdi » reste
  en latin. À l'écran, les noms restent en latin.
- Nikoud seulement sur les mots ambigus (לַמּוֹרֶה · לִצְפּוֹת · הַשְׁבָּחָה · אֶמְצְעֵי הַמְחָשָׁה ·
  אָלֶף עַד וָו · בְּמָה · הַדַּקּוֹת · הַשְׁעָרוֹת · מְחַכִּים), jamais sur tout le texte. Orthographe
  phonétique permise.
- Doute de prononciation : un fichier par variante (le mot seul deux fois, puis la phrase) ; relire
  les homographes avant de générer ; c'est l'oreille de Yoni qui tranche.
- Voix promo (ElevenLabs v4) : une balise d'intonation devant chaque phrase (`[curious]` `[excited]`
  `[enthusiastically]` `[cheerfully]` `[warmly]` `[playfully]` `[proudly]`), stabilité 0,3, mots et
  ponctuation inchangés, 2 prises ; éviter `[softly]` (elle chuchote), préférer `[gently]` ; mesurer
  le volume de chaque phrase.
- La voix lit l'écran mot pour mot ; une phrase du script = une scène.
- Voix utilisées (compte ElevenLabs de Yoni) : Brittney `XiPS9cXxAVbaIWtGDHDh` (eleven_v4,
  stabilité 0,5, similarité 0,75, vitesse 1 ; il y a trois « Brittney », prendre celle-là) · Audrey
  `McVZB9hVxVSk3Equu8EH` · HE Tamar `p7J75VowGmxi3K0it9lN` (ouvertures WizPlan) · Charles, HE Shira,
  HE Dana.

## 7. Textes et rôles

- Qui décide : Eyal = verdict, structure, dates (son « non » est définitif) ; Liad = contenu
  (arborescence, titres, slogans, textes, vidéos) ; Eden = retours produit et pédagogiques ; Yoni =
  arbitre. Contradiction : la signaler à Yoni, appliquer la dernière demande, garder l'ancienne version.
- Tout texte ajouté par nous (étiquette, phrase de fin) est une proposition à faire valider par Liad.
- Noms des modules en un seul mot (WizChat, jamais « Wiz Chat ») ; aucun mot anglais hors noms de marque.
- Pas de phrase construite sur une négation (sauf les accroches WizPlay et WizSpace) ; une accroche
  crée une tension ; « ואת? » est réservé à WizBook. Le mot-choc a son traitement (plus gros, autre
  couleur ou sa propre ligne).
- Public : enseignantes de 21 à 62 ans (campagnes autour de 45 ans) ; leur douleur : la charge de
  travail après les heures de cours.
- Le mot « חשיפה » est banni. CTA du formulaire : « טופס ליצירת קשר וקבלת מידע נוסף » ; bouton
  d'envoi : « שליחת טופס ».
- Pas de tiret long (—) dans le texte visible : un tiret court.
- « Réutiliser X » = exactement le même contenu, refait dans notre style.

## 8. Pages

- Gabarit de landing : TopStrip · Hero · TrustBar · Pillars · VideoBand · LeadForm · FAQ · Footer.
  Pas de section témoignages.
- Formulaire : שם מלא, טלפון, תפקיד, שם בית הספר (requis), יישוב (requis), סמל מוסד (facultatif,
  numérique), אימייל. Champ téléphone en `dir="rtl"`.
- Pages outil : « סולידי נקי ברור », « נקי, יוקרתי, רגוע » : pas un document marketing, zéro décor,
  pas de mascotte semée partout, page courte.
- Fond de l'identité : dégradé violet très clair (la page blanche « Apple » est refusée) ; ne jamais
  retirer les couleurs des Wiz. « Appliquer un skill » = appliquer sa méthode, pas son look.
- Pas de répétition : le wordmark d'un module une seule fois par carte, le nom une seule fois par
  zone (pas de surtitre au-dessus du h1) ; sections séparées par l'espace (ni bandes grises, ni boîtes
  dans des boîtes) ; texte des cartes centré.
- RTL : le premier enfant d'une grille ou d'un flex est à droite ; badges dans les coins droits ;
  filet d'accent en `border-s` ; flèche « suivant » = flèche gauche, en dernier ; ne jamais retourner
  l'universel (▶, logos, chiffres) ; vérifier dans le DOM ; un élément fixe ne recouvre jamais une
  colonne collante.
- Survol réservé à la souris ; pas de flottement perpétuel (« calme »).
- Jamais de bandes floues pour faire tenir une image : recadrage centré.
- Chaque page : un bouton de retour vers la page master et un lien vers wizdi.school sous le hero.
- Carte de partage (og:image) 1200×630 : aurore teintée par la page, visuel dans un cadre de verre à
  gauche, texte à droite, logotypes, slogan, pastilles « מאושר משרד החינוך » / studio-wizdi.com ;
  og:title et og:description mot pour mot.
- Un HTML envoyé en fichier intègre Fredoka et Baloo en `data:` (sinon les relecteurs voient de
  l'Arial) et porte `<meta charset>`.
- Noms de pages et de fichiers publiés en anglais ou en hébreu phonétique, jamais en français.
- Méthode : montrer une direction (référence + maquette) avant de produire ; faire exactement ce qui
  est demandé, ne pas refaire un travail validé ; propager une correction à toutes les pages concernées.

## 9. Interface WizPlan (invariants d'Eyal)

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

## 10. Déjà refusé (en plus de `WIZDI-BRAND.md` §11)

- Pages : une image générée par groupe ; un index en colonne latérale ; un sommaire en colonnes de
  liens ; une carte par vidéo sur toute la page ; le style « quiet » façon Quizlet ; la page blanche
  « Apple » à bandes grises.
- Wizi : hibou menaçant (`cinematic, deep shadows… NOT cartoon-cute`) ; médaillon rond qui coupe le plastron.
- Films : typographie 3D extrudée façon Katana, objets 3D codés ; « Wiz Universe » ; documentaire
  animalier IA ; mots en 3D ; décor de ville, bureau en étage, saut cuisine → canapé ; ouverture sur
  un tableur ; fonds abstraits orange ou « couleurs de la leçon » ; nos images existantes posées en
  fond ; simulation codée à la place de vraies captures.
- Images : montages et déformations de perspective faits à la main ; masque automatique ; interface
  WizPlan recomposée en 9:16.
- Outil WizPlan : le cadran ; les icônes en pâte à modeler 3D ; le hibou à côté du point ou dans le menu.
