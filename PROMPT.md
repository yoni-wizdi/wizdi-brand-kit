# Prompts prêts à coller dans Claude Code

Chaque prompt est en hébreu (à coller tel quel), suivi de sa traduction. Le kit est supposé cloné
dans `~/wizdi-brand-kit` (c'est ce que fait la section 1).

## 0. Le message d'accompagnement (WhatsApp / mail)

> היי, זה קיט המותג והעיצוב של Wizdi: הכללים, הצבעים, הפונטים, הלוגואים של ה-Wiz עם האנימציה שלהם,
> Wizi (הדמות) וה-skills של Claude Code — בדיוק כמו באתר studio-wizdi.com.
> שלחתי הזמנה למאגר ב-GitHub: https://github.com/yoni-wizdi/wizdi-brand-kit
> איך מתחילים: לאשר את ההזמנה ב-GitHub, לפתוח את Claude Code ולהדביק את הפרומפט מסעיף 1 ב-`PROMPT.md`
> (אפשר לראות אותו ישר באתר של GitHub). אחר כך כל עדכון שלי מגיע עם סעיף 2. שאלות — אני כאן.

*Traduction* : « Salut, voici le kit de marque et de design Wizdi : les règles, les couleurs, les
polices, les logos des Wiz avec leur animation, Wizi (le personnage) et les skills Claude Code,
exactement comme sur studio-wizdi.com. J'ai envoyé une invitation au dépôt GitHub (lien). Pour commencer :
accepter l'invitation, ouvrir Claude Code et coller le prompt de la section 1 de `PROMPT.md` (lisible
directement sur GitHub). Ensuite, chaque mise à jour passe par la section 2. Des questions, je suis là. »

## 1. Installer le kit (une seule fois)

```text
התקן לי את קיט המותג של Wizdi:
1. שכפל את https://github.com/yoni-wizdi/wizdi-brand-kit לתיקייה wizdi-brand-kit בתיקיית הבית שלי
   (~/wizdi-brand-kit). אם GitHub מבקש התחברות, תן לי להתחבר בעצמי בחלון שנפתח.
2. קרא את CLAUDE.md, WIZDI-BRAND.md ו-WIZDI-PRODUCTION.md של הקיט עד הסוף.
3. העתק כל תיקייה מ-skills/ אל ~/.claude/skills/ — להחליף תיקיות עם אותו שם, לא לגעת ב-skills אחרים.
4. בדוק אם יש במחשב את מה שצריך לסרטונים (Python 3.10+, playwright + Chromium, ffmpeg — לפי
   skills/wizdi-motion-senior/engine/README.md) ותציע להתקין מה שחסר. לא להתקין בלי אישור שלי.
5. סכם לי: כמה skills הותקנו, מה חסר, ושצריך להפעיל מחדש את Claude Code.
```

*Traduction* : « Installe-moi le kit de marque Wizdi : 1. clone le dépôt dans `~/wizdi-brand-kit`
(si GitHub demande une connexion, laisse-moi me connecter dans la fenêtre) ; 2. lis `CLAUDE.md`,
`WIZDI-BRAND.md` et `WIZDI-PRODUCTION.md` en entier ; 3. copie chaque dossier de `skills/` dans
`~/.claude/skills/` en remplaçant les dossiers du même nom, sans toucher aux autres ; 4. vérifie ce
qu'il faut pour les films (Python, playwright + Chromium, ffmpeg) et propose d'installer ce qui manque,
pas sans mon accord ; 5. résume : combien de skills installés, ce qui manque, et qu'il faut
redémarrer Claude Code. »

## 2. Mettre le kit à jour

```text
עדכן את קיט Wizdi: git pull בתיקייה ~/wizdi-brand-kit, ואז העתק מחדש כל תיקייה מ-skills/ אל
~/.claude/skills/ (להחליף תיקיות עם אותו שם). סכם לי מה השתנה מאז העדכון הקודם (git log),
ותזכיר לי להפעיל מחדש את Claude Code.
```

*Traduction* : « Mets à jour le kit Wizdi : `git pull` dans `~/wizdi-brand-kit`, puis recopie chaque
dossier de `skills/` dans `~/.claude/skills/`. Résume ce qui a changé depuis la dernière fois
(`git log`) et rappelle-moi de redémarrer Claude Code. »

## 3. Mettre un projet existant aux normes

```text
קיט המותג של Wizdi נמצא ב-~/wizdi-brand-kit.
1. קרא את ~/wizdi-brand-kit/WIZDI-BRAND.md עד הסוף. אלה הכללים המחייבים לכל פרויקט Wizdi.
2. בצע ביקורת של הפרויקט הזה מול הכללים וכתוב רשימת פערים מסודרת לפי נושא:
   השם Wizdi (לטיני, תחיליות, אותיות גדולות), הלוגו (ינשוף שטוח רק בלוגו, Wizi תלת-ממדי בשאר),
   לוגואי ה-Wiz (SVG, Wiz כחול + סיומת בצבע המודול, האנימציה), צבעים (מול tokens/),
   טיפוגרפיה (עברית Fredoka, לטינית Baloo, סדר הערימה), אנימציה (משכים, ease, reduced-motion),
   תמונות (אין עברית בתמונות AI, אין צילומי מסך מזויפים), RTL, רכיבים, זכויות יוצרים.
   לכל פער: הקובץ, השורה, מה יש היום, מה צריך להיות.
3. חכה לאישור שלי על הרשימה, ואז תקן פער אחר פער:
   - העתק לפרויקט את tokens/, fonts/, logos/, components/ מהקיט וייבא את tokens/wizdi-tokens.css,
   - החלף כל לוגו של מודול בקומפוננטה components/WizWord.tsx (React) או wiz-word.js (HTML),
   - החלף את לוגו Wizdi בקובץ logos/wizdi-wordmark.svg,
   - אל תשנה אף טקסט של הלקוח (מילה במילה), אל תוסיף סימני קריאה.
4. בסוף: build, צילומי מסך לפני/אחרי ב-1440 וב-390, ובדיקה ש-
   document.fonts.check('16px Fredoka') ו-document.fonts.check('16px "Baloo Latin"') מחזירים true.
5. סכם מה שונה, מה נשאר פתוח, ומה דורש החלטה של יוני.
```

*Traduction* : « 1. Lis `WIZDI-BRAND.md` en entier. 2. Audite ce projet et liste les écarts par
thème (nom, logo, logos des Wiz, couleurs, typographie, animation, images, RTL, composants,
copyright), avec fichier, ligne, état actuel, état attendu. 3. Attends ma validation, puis corrige
écart par écart : jetons, polices, logos et composants du kit, aucun texte client modifié.
4. Build, captures avant/après à 1440 et 390, vérification des polices. 5. Résumé : ce qui a
changé, ce qui reste ouvert, ce qui demande une décision de Yoni. »

## 4. Une nouvelle page ou landing

```text
אני רוצה לבנות [תיאור הדף] לפי המותג של Wizdi.
- הכללים: ~/wizdi-brand-kit/WIZDI-BRAND.md ו-WIZDI-PRODUCTION.md (לקרוא עד הסוף לפני שמתחילים)
  וה-skills wizdi-brand ו-wizdi-production.
- סדר העבודה: frontend-design לכיוון, wizdi-brand כדי להצמיד אותו למותג, gsap-* ו-emil-design-eng
  לתנועה, ui-ux-pro-max ואחריו apple-hig ו-review-animations לבדיקה לפני מסירה.
- להעתיק לפרויקט את tokens/, fonts/, logos/, components/ מהקיט; לוגואים של מודולים רק דרך
  WizWord.tsx או wiz-word.js.
- RTL, עברית ב-Fredoka ולטינית ב-Baloo, בדיקה ב-1440, 1920 ו-390.
- טקסטים שאני נותן: מילה במילה.
- להראות לי כיוון לפני שבונים את כל הדף.
```

*Traduction* : « Je veux construire [la page] selon la marque Wizdi : règles de `WIZDI-BRAND.md` et
skill `wizdi-brand` ; ordre : `frontend-design` pour la direction, `wizdi-brand` pour la contraindre,
`gsap-*` + `emil-design-eng` pour le mouvement, `ui-ux-pro-max` puis `apple-hig` et `review-animations` pour relire ;
jetons, polices, logos et composants du kit ; RTL, Fredoka/Baloo, vérification à 1440, 1920 et 390 ;
mes textes mot pour mot ; montre-moi une direction avant de tout construire. »

## 5. Une image ou une vidéo générée avec Wizi ou WizBuddy

```text
אני רוצה ליצור [תמונה / סרטון] של Wizi עבור [WizPlay / WizPlan / WizChat / WizBook / WizBox / WizSpace]
(או של WizBuddy): [תיאור הסצנה].
- להשתמש ב-skills wizdi-visual-studio ו-wizdi-production (לסרטון עם דמות מדברת: wizdi-avatar-helper).
- REFERENCE 1 = ~/wizdi-brand-kit/references/wizi/wizi-reference.webp (Wizi לבד).
  לתנוחה אחרת: references/wizi/wizi-poses.webp. ל-WizBuddy: references/wizi/wizbuddy/wizbuddy-reference.webp.
- REFERENCE 2 = Wizi של המודול עם הלוגו האמיתי: references/wizi/modules/<module>.webp, או הפוסטר
  ב-references/campaign/ (לוחית החזה וצבע השריון). ל-WizBuddy: wizbuddy/wizbuddy-plate.webp.
- סגנון «פסטל אוורירי» כמו ב-references/pastel/.
- Wizi תלת-ממדי בחליפת חלל, אף פעם לא הינשוף השטוח. בלי טקסט עברי בתמונה, בלי צילומי מסך מזויפים.
- לכתוב לי את הפרומפטים באנגלית לפי הבלוקים של ה-skill, ולחכות לאישור שלי לפני כל יצירה.
- סרטון: תמונת הבסיס מאושרת קודם עם יוני; ה-URL בסוף הוא תמיד wizdi.school.
```

*Traduction* : « Je veux créer [une image / une vidéo] de Wizi pour [module] (ou de WizBuddy) :
[la scène]. Skills `wizdi-visual-studio` et `wizdi-production` (vidéo avec personnage qui parle :
`wizdi-avatar-helper`). RÉFÉRENCE 1 = Wizi seul (`references/wizi/wizi-reference.webp`, autre pose :
`wizi-poses.webp` ; WizBuddy : `wizbuddy/wizbuddy-reference.webp`) ; RÉFÉRENCE 2 = le Wizi du module
au vrai logo (`references/wizi/modules/`) ou son poster (`references/campaign/`) ; WizBuddy : sa
plaque. Style « pastel aérien » (`references/pastel/`). Wizi 3D
en combinaison spatiale, jamais le hibou plat ; aucun texte hébreu dans l'image, aucune fausse
capture. Prompts en anglais selon les blocs du skill, validation avant chaque génération. Vidéo :
image de base validée avec Yoni d'abord ; l'URL finale est toujours wizdi.school. »

## 6. Un film en motion design (réseaux sociaux, ed tech)

```text
אני רוצה סרטון מושן של [משך] שניות על [המוצר / הפיצ'ר] ל-[רשתות חברתיות / מרכז ההדרכה].
- להשתמש ב-skill wizdi-motion-senior (מעצב מושן בכיר) יחד עם wizdi-brand ו-wizdi-production.
- קודם הקריינות: לכתוב לי את הטקסט ולחכות לאישור שלי (ואחריי ליעד), ורק אז קול, תמונה וסאונד.
- רק מסכים אמיתיים של המוצר (החוק של אייל: מסך מלא → סימון → החלק יוצא בצורתו האמיתית),
  Wizi תלת-ממדי מהקיט, טקסט על המסך מילה במילה מהקריינות.
- 3 פורמטים: 9:16, 4:5, 16:9 (+ גרסה קלה לוואטסאפ), סיום על wizdi.school, ‎−14 LUFS.
- לפני כל הוצאה (קול, מוזיקה, תמונות): להגיד לי מה ובכמה, ולחכות לאישור.
- לבדוק את הסרט לפי טבלת השופטים של ה-skill לפני שמראים לי.
```

*Traduction* : « Je veux un film motion de [durée] sur [le produit / la fonction] pour [réseaux
sociaux / centre de formation]. Skill `wizdi-motion-senior` avec `wizdi-brand` et `wizdi-production`.
La narration d'abord : écris le texte et attends ma validation (puis celle de Liad), seulement ensuite
voix, image et son. Seulement de vrais écrans (règle d'Eyal), Wizi 3D du kit, texte à l'écran mot
pour mot. 3 formats + version WhatsApp légère, fin sur wizdi.school, −14 LUFS. Avant toute dépense :
dis-moi quoi et combien, et attends mon accord. Note le film avec la grille du jury avant de me le
montrer. »
