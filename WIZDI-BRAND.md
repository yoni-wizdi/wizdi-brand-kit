# כללי המותג והעיצוב של Wizdi

> wizdi-brand-kit · מקור האמת: studio-wizdi.com (דפי הנחיתה, דף הבית, מרכז ההדרכה).
> הקובץ נקרא אוטומטית על ידי Claude Code (דרך `CLAUDE.md` של הקיט ודרך ה-skill `wizdi-brand`).
> הגרסה הצרפתית המפורטת נמצאת בהמשך.

## 1. השם

- **Wizdi נכתב תמיד באותיות לטיניות.** לעולם לא `וויזדי`. תחיליות בעברית נפרדות במקף: `ב-Wizdi`, `ל-Wizdi`, `מ-Wizdi`.
- אף פעם לא באותיות גדולות (`WIZDI`): לא ב-CSS (`text-transform: uppercase` אסור על טקסט שמכיל Wizdi) ולא בעיצוב.
- שמות המודולים, תמיד כך: **WizPlay · WizPlan · WizChat · WizBook · WizBox · WizSpace · WizGen · WizMap · WizLab**.
- זכויות יוצרים, בכל מקום, מילה במילה: `Copyright © 2026 Wizdi. All rights reserved`.

## 2. הלוגו

- הלוגו = הינשוף השטוח + המילה **Wizdi** בכחול `#23A4D8` (קובץ: `logos/wizdi-wordmark.svg`, `logos/wizdi-owl.png`).
- **הינשוף השטוח משמש רק בלוגו.** בכל ויזואל אחר (הירו, כרטיסים, פוסטרים, תמונות שנוצרו ב-AI) מופיע **Wizi — הינשוף התלת-ממדי** בחליפת החלל, עם לוחית החזה של המודול (הדמות לבד וכל התנוחות: `references/wizi/`; לוחית החזה של כל מודול: `references/campaign/`).
- רווח בטיחות: לפחות גובה האות W מסביב. גובה מינימלי: 24px למילה Wizdi.
- על רקע כהה המילה נשארת כחולה (`#23A4D8`), לא לבנה.
- `מבית יבנה בונוס`: הלוגו של יבנה (`logos/yavne-bonus.png`) מופיע רק בפוטר, ליד המילה «מבית».

## 3. הלוגואים של ה-Wiz (WizPlay, WizBook…)

- בנייה: **«Wiz» בכחול `#23A4D8` + הסיומת בצבע המודול**, בפונט Baloo, מתוך תווי ה-SVG האמיתיים (`logos/wiz/*.svg`, `components/wizWordPaths.json`). לא טקסט רגיל, לא פונט אחר, לא אותיות גדולות, לא אותיות עבריות.
- אם אין SVG: גיבוי טקסט דו-צבעי ב-Baloo (`<b>Wiz</b><i>Play</i>`), `direction:ltr`.
- הגודל נקבע לפי `font-size` של ההורה (גובה 1em).

| מודול | צבע | כהה (כפתורים) | פסטל (רקעים) |
|---|---|---|---|
| WizPlay | `#FF5FA2` ורוד | `#E8467C` | `#FCD7E3` |
| WizPlan | `#F28C28` כתום | `#D9701A` | `#FFE3C8` |
| WizChat | `#7B5CF0` סגול | `#6246D6` | `#E8DCFA` |
| WizBook | `#15A19E` טורקיז | `#0F8684` | `#CFEEEA` |
| WizBox | `#C9742E` ברונזה | `#A85C1F` | `#F8DCCF` |
| WizSpace | `#C13BC9` מג'נטה (רקע זהוב) | `#A02FA7` | `#FDF0CF` |
| WizGen | `#3ED98A` ירוק | `#1FB86E` | `#D6F5E6` |
| WizMap | `#38C6FF` תכלת | `#1FA8E0` | `#D9F1FF` |
| WizLab | `#F06ABC` פוקסיה (בקרוב) | `#D44FA3` | `#FBDDEF` |

- הפוסטר של כל מודול (`references/campaign/`) הוא **ההפניה לסגנון ולצבע** של כל ויזואל של המודול.

## 4. צבעים כלליים

- דיו: `#2A2550` (כותרות, טקסט) · `#4A4573` (משני) · `#726F98` (מעומעם).
- רקע דף: `#FBFAFF` (או `#F4F2FF`), עם «זוהר» פסטלי: `#D9CFFD` לבנדר, `#C6E2FF` שמיים, `#C9F1E4` מנטה, `#FFE1CB` אפרסק, `#FFD5E4` ורוד.
- כחול Wiz `#23A4D8` · סגול פעולה `#7B6CF6` · גרדיאנט המותג `135deg #8F7DFF → #6FB9FF → #62DCC3`.
- כפתור ראשי («קבעו הדגמה»): גרדיאנט `135deg #FF8A3D → #FF5F7E`. בדף של מודול: גרדיאנט הצבע של המודול.
- ירוק אישור `#1A9E5C`.
- הכול ב-`tokens/wizdi-tokens.css` ו-`tokens/wizdi-tokens.json`.

## 5. טיפוגרפיה

- **עברית ב-Fredoka, לטינית ב-Baloo, בכל מקום.** המנגנון: `"Baloo Latin"` **ראשונה** בערימה עם `unicode-range` לטיני, `"Fredoka"` **מיד אחריה** עם `unicode-range` עברי. כך כל תו מגיע לפונט הנכון בלי לסמן טקסט. לעולם לא בסדר הפוך.
- הערימה: `"Baloo Latin", "Fredoka", ui-rounded, system-ui, sans-serif`. הקבצים ב-`fonts/` (Fredoka משתנה 300–700, תת-קבוצה עברית, 8.8KB).
- כותרות 600, טקסט 16–17px, `line-height 1.55`. Heebo / Rubik / Assistant / Suez One רק כגיבוי, לא לעבודה חדשה.
- מספרים ותאריכים ב-`direction:ltr` בתוך טקסט עברי.

## 6. אנימציה

**הופעת לוגו של מודול** (כמו באתר, `components/wiz-word.js` או `WizWord.tsx`):
1. מצב התחלה: קו מתאר בלבד (`stroke-width 3`), ללא מילוי.
2. טריגר: כניסה למסך (35 %), **פעם אחת**, השהיה 1.1 שניות (כדי לא לרוץ יחד עם הלוגו בכותרת).
3. הקו נמשך: 2.4 שניות, `power2.inOut`.
4. המילוי עולה: 1 שנייה, `power2.out`, מתחיל 0.5 שנייה לפני סוף הקו.
5. הקו נעלם: 0.7 שנייה, `power2.out`, מתחיל 0.6 שנייה לפני סוף המילוי.
6. לוגו Wizdi בכותרת: אותו רצף, מהר יותר ובלי השהיה — קו 1.6 שניות, מילוי 0.7 שנייה (מתחיל 0.3 לפני הסוף), הקו נעלם ב-0.45 שנייה (מתחיל 0.45 לפני הסוף), `stroke-width 1.6`.
7. `prefers-reduced-motion`: ללא אנימציה, לוגו מלא מיד.

**תנועה בממשק**: מעברים עד 300ms (ברירת מחדל 220ms), `ease-out`; לחיצה = `scale(0.985)`; לעולם לא `scale(0)`; הופעות בגלילה: `opacity 0→1` + `translateY 26px→0` ב-0.8 שניות, `ease-out`, עם מדרגות (stagger) של 70–110ms; כניסת דף: כותרת → טקסט → כפתורים → ויזואל, במדרגות. GSAP מותר (עם מידה). תמיד לכבד `prefers-reduced-motion`.

## 7. תמונות

- בכל ויזואל: **Wizi התלת-ממדי** עם לוחית החזה של המודול, בסגנון הפוסטרים ב-`references/campaign/`; דמויות אמיתיות (תלמידים, מורים) בסגנון ישראלי-ים-תיכוני, סצנה אחת לכל עמוד, בלי כפילויות.
- **אין טקסט עברי בתמונה שנוצרה ב-AI** (אי אפשר לאמת אות-אות). הטקסט נכתב ב-HTML מעל התמונה.
- **אין צילומי מסך מזויפים** של הממשק. אין צילום אמיתי? ויזואל ניטרלי + הערה.
- מייצרים מחדש, לא מרטשים: שלוש וריאציות עם הלוגואים כהפניה עדיפות על עריכה ידנית.
- פרומפטים לתמונות: לפי ה-skill `wizdi-visual-studio` (בלוקים ART DIRECTION / SCENE / WIZI / HOLOGRAMS / TEXT / NEGATIVE, REFERENCE 1 = Wizi `references/wizi/wizi-reference.webp`, REFERENCE 2 = הפוסטר של המודול).
- וידאו: ה-URL בסוף הוא תמיד `wizdi.school`, אף פעם לא studio-wizdi.com. לפני וידאו: לאשר את תמונת הבסיס עם יוני.

## 8. פריסה ו-RTL

- `<html lang="he" dir="rtl">`. **הקריאה מתחילה מימין**: סרגל צד, אייקון כותרת, נקודות התקדמות, תגיות — בצד ימין. חצים הפוכים (`scaleX(-1)`).
- נייד (390px) ודסקטופ (1440 ו-1920): לבדוק את שלושתם. יעדי מגע 44px, ניגודיות 4.5:1, בלי אימוג'י במקום אייקונים (אייקוני קו, lucide).
- כרטיסים: אובייקט אחד לכל כרטיס, גובה שווה בשורה, צילום/ויזואל למעלה וטקסט למטה.

## 9. רכיבים (המתכונים ב-`tokens/wizdi-tokens.css`)

- כפתורים: ראשי = גרדיאנט כתום (`.btn-wizdi--cta`), מודול = גרדיאנט הצבע שלו (`.btn-wizdi--module`), משני = זכוכית (`.btn-wizdi--glass`). גלולה (`border-radius 999px`), גובה 52px, Baloo/Fredoka 600.
- תגיות מצב, מילה במילה: `קיים ועובד` (ירוק) · `🚀 ההשקה` (כתום) · `בקרוב` (סגול).
- כרטיס זכוכית (`.glass-wizdi`): לבן שקוף 58 %, טשטוש 18px, מסגרת סגולה עדינה, צל רך. פינות 24px (כרטיס) / 32px (פאנל).
- מצב פוקוס תמיד נראה (`outline 3px #8A7BFF`).

## 10. טקסטים

- טקסט שהלקוח סיפק (ליעד, איל, עדן) מועתק **מילה במילה**: בלי ניסוח מחדש, בלי סימני קריאה נוספים, בלי «שיפרתי את הניסוח».
- שתי הנחיות סותרות → מעלים ליוני, לא מחליטים לבד.
- כל גרסה נשארת ניתנת לשחזור (git).

## 11. אסור / נדחה

- רקע חשוך «קוסמי» עם כוכבים בדפי עבודה (מרכז ההדרכה): נדחה.
- תפריטים נפתחים ורשימות עם נקודות קטנות במקום כרטיסים: נדחה.
- רשת של עשרות תמונות ממוזערות: נדחה («לא יודעים איפה הראש»).
- ינשוף שטוח מחוץ ללוגו · `וויזדי` בעברית · Wizdi באותיות גדולות · עברית ב-Heebo/Rubik בעבודה חדשה.
- אסתטיקה גנרית של AI: Inter/Roboto/Arial, סגול-על-לבן בלי אופי, אימוג'י כאייקונים.
- אין קישורים ל-lovable.app ואין תת-דומיינים: כל דף Wizdi חי ב-`studio-wizdi.com/<path>`.

## 12. צ'ק-ליסט לפני מסירה

- [ ] Wizdi לטיני בכל מקום, גם בתמונות · [ ] עברית Fredoka, לטינית Baloo (לבדוק ב-`document.fonts.check`)
- [ ] לוגואי Wiz מ-SVG עם הצבע הנכון, אנימציה כמו באתר · [ ] Wizi תלת-ממדי, לא שטוח
- [ ] טקסט לקוח מילה במילה · [ ] 1440 / 1920 / 390 נבדקו · [ ] RTL: הכול מתחיל מימין
- [ ] מצב פוקוס, ניגודיות, `prefers-reduced-motion` · [ ] זכויות יוצרים מדויקות · [ ] אין טקסט עברי בתמונות AI

---

# Règles de marque et de design Wizdi (version française détaillée)

> wizdi-brand-kit · source de vérité : studio-wizdi.com (landings, page master, centre v2).
> Lu automatiquement par Claude Code (via le `CLAUDE.md` du kit et le skill `wizdi-brand`).

## 1. Le nom

- **« Wizdi » s'écrit toujours en lettres latines**, jamais `וויזדי`. Les préfixes hébreux se détachent par un tiret : `ב-Wizdi`, `ל-Wizdi`, `מ-Wizdi`.
- Jamais en majuscules : pas de `text-transform: uppercase` sur un texte qui contient Wizdi.
- Les modules, toujours ainsi : WizPlay · WizPlan · WizChat · WizBook · WizBox · WizSpace · WizGen · WizMap · WizLab.
- Copyright identique partout : `Copyright © 2026 Wizdi. All rights reserved`.

## 2. Le logo

- Le logo = le hibou plat + le mot **Wizdi** en bleu `#23A4D8` (`logos/wizdi-wordmark.svg`, `logos/wizdi-owl.png`). Le tracé SVG du mot est généré depuis la police Baloo (`components/wizdiWordmarkPath.ts`).
- **Le hibou plat ne sert que dans le logo.** Partout ailleurs (hero, cartes, posters, images générées) c'est **Wizi, le hibou 3D** en combinaison spatiale, avec le plastron du module (le personnage seul et toutes ses poses : `references/wizi/` ; le plastron de chaque module : `references/campaign/`).
- Zone de protection : la hauteur du W tout autour. Taille minimale du mot : 24 px.
- Sur fond sombre le mot reste bleu, pas blanc.
- « מבית יבנה בונוס » : le logo Yavne n'apparaît qu'en pied de page, à côté du mot « מבית ».

## 3. Les logos des Wiz

- Construction : **« Wiz » en bleu `#23A4D8` + le suffixe dans la couleur du module**, en Baloo, à partir des vrais tracés SVG (`logos/wiz/*.svg`, données dans `components/wizWordPaths.json` et `wizWordPaths.ts`). Jamais en texte brut stylé, jamais une autre police, jamais en majuscules, jamais en lettres hébraïques.
- Repli sans SVG : texte bicolore en Baloo (`<b>Wiz</b><i>Play</i>`), `direction: ltr`, classe `.wiz-text`.
- La taille suit le `font-size` du parent (hauteur 1 em).
- Couleurs : voir le tableau hébreu ci-dessus (identique) et `tokens/wizdi-tokens.json` → `color.modules`. Chaque module a sa couleur, sa variante foncée pour les boutons, son pastel pour les fonds.
- Le poster CAMPAIGN du module (`references/campaign/`) est la référence de style et de couleur de tout visuel du module.

## 4. Couleurs générales

Encre `#2A2550` / `#4A4573` / `#726F98` · page `#FBFAFF` ou `#F4F2FF` · aurore pastel (lavande `#D9CFFD`, ciel `#C6E2FF`, menthe `#C9F1E4`, pêche `#FFE1CB`, rose `#FFD5E4`) · bleu Wiz `#23A4D8` · accent `#7B6CF6` · dégradé de marque `135deg #8F7DFF → #6FB9FF → #62DCC3` · bouton principal `135deg #FF8A3D → #FF5F7E` (sur une page de module : le dégradé de sa couleur) · succès `#1A9E5C`. Tout est dans `tokens/`.

## 5. Typographie

- **Hébreu en Fredoka, latin en Baloo, partout.** Mécanique : `"Baloo Latin"` en tête de pile avec une `unicode-range` latine, `"Fredoka"` juste derrière avec une `unicode-range` hébraïque. Chaque caractère part à la bonne police sans baliser un seul texte. Jamais l'inverse.
- Pile : `"Baloo Latin", "Fredoka", ui-rounded, system-ui, sans-serif`. Fichiers dans `fonts/` (Fredoka variable 300–700, sous-ensemble hébreu, 8,8 Ko ; Baloo Chettan regular).
- Titres 600, corps 16–17 px, interligne 1,55. Heebo, Rubik, Assistant, Suez One restent en repli, pas pour du travail nouveau.
- Chiffres et dates en `direction: ltr` dans le texte hébreu.

## 6. Animation

**Apparition d'un logo de module** (`components/wiz-word.js` sans dépendance, `WizWord.tsx` en React + GSAP DrawSVG) :
1. État de départ : contour seul (`stroke-width` 3 en unités du viewBox), remplissage à 0.
2. Déclenchement à l'entrée dans l'écran (seuil 35 %), **une seule fois**, délai 1,1 s pour ne pas jouer en même temps que le logo de l'en-tête.
3. Le contour se dessine : 2,4 s, `power2.inOut`.
4. Le remplissage monte : 1 s, `power2.out`, commence 0,5 s avant la fin du tracé.
5. Le trait s'efface : 0,7 s, `power2.out`, commence 0,6 s avant la fin du remplissage.
6. Logo Wizdi de l'en-tête : même séquence, plus rapide et sans délai : contour 1,6 s, remplissage 0,7 s (commence 0,3 s avant la fin), trait 0,45 s (commence 0,45 s avant la fin), `stroke-width` 1,6 (`data-fast="1"`, valeurs de `TopBar.tsx`).
7. `prefers-reduced-motion` : aucune animation, logo plein immédiatement. Sans JavaScript : plein aussi.

**Mouvement d'interface** : transitions ≤ 300 ms (220 ms par défaut), `ease-out` fort ; pression = `scale(0.985)` ; jamais `scale(0)` ; apparitions au défilement `opacity 0→1` + `translateY 26px→0` en 0,8 s avec cascade de 70–110 ms ; entrée de page orchestrée (titre → texte → boutons → visuel). GSAP autorisé, avec mesure. `prefers-reduced-motion` toujours respecté.

## 7. Images

- Tout visuel : **Wizi 3D** avec le plastron du module, dans le style des posters `references/campaign/` ; vraies personnes (élèves, enseignants) de type israélien méditerranéen, une scène par page, aucun doublon. Les scènes `references/pastel/` montrent la direction « pastel aérien » validée.
- **Aucun texte hébreu dans une image générée** : on ne peut pas le vérifier lettre à lettre. Le texte se pose en HTML par-dessus.
- **Jamais de fausse capture d'interface.** Pas de vraie capture ? Un visuel neutre et une note.
- Régénérer plutôt que retoucher : trois variantes générées avec les logos en référence battent toute retouche manuelle.
- Prompts d'images : méthode du skill `wizdi-visual-studio` (blocs ART DIRECTION / SCENE / WIZI / HOLOGRAMS / TEXT / NEGATIVE ; RÉFÉRENCE 1 = Wizi seul `references/wizi/wizi-reference.webp`, RÉFÉRENCE 2 = le poster du module).
- Vidéo : l'URL finale est toujours `wizdi.school`, jamais studio-wizdi.com ; la référence visuelle se valide avec Yoni avant toute génération.

## 8. Mise en page et RTL

- `<html lang="he" dir="rtl">`. **La lecture part de la droite** : barre latérale, icône de tête, pastilles de progression et étiquettes à droite ; flèches retournées (`scaleX(-1)`).
- Vérifier à 1440, 1920 et 390 px. Cibles tactiles 44 px, contraste 4,5:1, pas d'emoji en guise d'icône (icônes à trait, lucide).
- Cartes : un seul objet par carte, hauteurs égales par rangée, visuel en haut, texte en bas.

## 9. Composants (recettes dans `tokens/wizdi-tokens.css`)

- Boutons : principal = dégradé orange (`.btn-wizdi--cta`), module = dégradé de sa couleur (`.btn-wizdi--module`), secondaire = verre (`.btn-wizdi--glass`). Pilule, 52 px, graisse 600.
- Badges d'état, verbatim : `קיים ועובד` (vert) · `🚀 ההשקה` (orange) · `בקרוב` (violet).
- Carte de verre `.glass-wizdi` : blanc 58 %, flou 18 px, liseré violet léger, ombre douce. Rayons 24 px (carte) / 32 px (panneau).
- Focus visible toujours (`outline 3px #8A7BFF`).

## 10. Textes

- Un texte fourni par le client (Liad, Eyal, Eden) se recopie **tel quel** : pas de reformulation, pas de point d'exclamation ajouté.
- Deux retours contradictoires → remonter à Yoni, ne pas trancher.
- Chaque version reste récupérable (git).

## 11. Interdit / déjà rejeté

- Fond sombre « cosmique » étoilé sur des pages de travail (centre d'aide) : rejeté.
- Menus déroulants et listes à petits points à la place de cartes : rejeté.
- Grille de dizaines de vignettes : rejeté.
- Hibou plat hors logo · `וויזדי` · Wizdi en majuscules · hébreu en Heebo/Rubik sur du neuf.
- Esthétique « IA générique » : Inter/Roboto/Arial, violet-sur-blanc sans caractère, emoji-icônes.
- Pas de lien lovable.app, pas de sous-domaine : chaque page Wizdi vit sur `studio-wizdi.com/<chemin>`.

## 12. Check-list avant livraison

- [ ] Wizdi en latin partout, images comprises · [ ] hébreu en Fredoka, latin en Baloo (`document.fonts.check`)
- [ ] logos des Wiz en SVG, bonne couleur, animation du site · [ ] Wizi 3D, jamais le plat
- [ ] textes client verbatim · [ ] 1440 / 1920 / 390 vérifiés · [ ] RTL : tout part de la droite
- [ ] focus, contraste, `prefers-reduced-motion` · [ ] copyright exact · [ ] aucun texte hébreu dans les images générées
