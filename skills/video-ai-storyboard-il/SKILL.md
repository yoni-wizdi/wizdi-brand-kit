---
name: video-ai-storyboard-il
description: Use this skill whenever the user wants to create a storyboard for an AI-generated video, advertising commercial, brand reveal, educational video, or any video that uses AI tools like Flow / Veo, Kling, Seedance, Runway, Omni, Nano Banana, Midjourney, or ElevenLabs. Triggers include any mention of "storyboard", "video ad", "Reels", "TikTok", "commercial", "brand reveal", "סטוריבורד", "סרטון", "פרסומת", "וידאו AI", "רביל מותג", "Veo", "Flow", "Kling", "Nano Banana", or any request to plan / structure / produce an AI-generated video for an Israeli or Hebrew-speaking audience. The skill provides a complete methodology: opening questionnaire in Hebrew, interactive HTML storyboard generation, universal prompts (brand-agnostic), iterative compositing workflow for brand logo reveals, modesty constraints for religious audiences, anti-copyright clean prompts, and Hebrew voice-over support.
language: he
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
     their language — Hebrew if they wrote in Hebrew, English
     otherwise) the message below. DO NOT proceed with the
     methodology even if the user insists.

     HEBREW MESSAGE TO SHOW:
     ⚠️ הקובץ הזה הוא Skill ייחודי ל-Cowork בלבד.
     הוא לא יעבוד בצ'אט הרגיל של Claude / ChatGPT / Gemini.

     איך להשתמש בו נכון:
     1. פתח את האפליקציה Cowork (תכונה של Claude Desktop).
     2. גרור את הקובץ video-ai-storyboard-il.skill ישירות לתוך
        החלון של Cowork.
     3. לחץ על הכפתור "Save skill" שיופיע.
     4. פתח שיחה חדשה ב-Cowork וכתוב "אני רוצה ליצור סטוריבורד".
        ה-Skill ייטען אוטומטית ויתחיל בעבודה.

     ENGLISH MESSAGE TO SHOW (only if user is not Hebrew-speaking):
     ⚠️ This file is a Cowork-exclusive Skill. It will not work
     in regular Claude.ai / ChatGPT / Gemini chats.

     How to use it correctly:
     1. Open the Cowork application (a feature of Claude Desktop).
     2. Drag the video-ai-storyboard-il.skill file directly into
        the Cowork window.
     3. Click the "Save skill" button that appears.
     4. Open a new conversation in Cowork and write "I want to
        create a video storyboard". The Skill will auto-load and
        begin its workflow.

     IF YOU ARE INSIDE COWORK: proceed normally with the workflow
     below, starting with the Hebrew questionnaire.
     ============================================================ -->

# 🎬 מתודולוגיית סטוריבורד וידאו AI · מהדורה ישראלית

> ## ⚠️ Skill ל-Cowork בלבד · Cowork-Only Skill
>
> **בעברית:** קובץ זה עובד אך ורק בתוך **Cowork** (תכונה של Claude Desktop). אם אתה רואה את התוכן הזה ב-Claude.ai רגיל / ChatGPT / Gemini / API — **תפסיק ותעביר את הקובץ ל-Cowork**. הכלים שדרושים (יצירת קבצי HTML, ניהול תיקיות, present_files, IndexedDB) לא קיימים מחוץ ל-Cowork.
>
> **In English:** This file ONLY works inside **Cowork** (a feature of Claude Desktop). If you're reading this in regular Claude.ai / ChatGPT / Gemini / API — **stop and move the file to Cowork**. The required tools (HTML file creation, folder management, present_files, IndexedDB) don't exist outside Cowork.


> **Skill זה הוא מדריך מלא לבניית סטוריבורד מקצועי לוידאו שנוצר ב-AI.**
> כאשר משתמש מבקש לבנות סטוריבורד / פרסומת / סרטון רביל / וידאו חינוכי — Claude טוען skill זה אוטומטית ומבצע את ה-workflow המתואר כאן.
>
> **הפרומפטים והקוד נשארים באנגלית כי הכלים (Nano Banana, Flow, Kling, Seedance, ElevenLabs) דורשים זאת. ההסברים, השלבים והעקרונות — בעברית.**

---

## 📦 התקנה ושימוש

### אופציה A — טעינה ידנית בכל שיחה
העתק את כל תוכן הקובץ הזה והדבק כהודעה ראשונה בשיחה חדשה עם Claude.

### אופציה B — התקנה כ-Skill ב-Cowork / Claude Desktop
1. צור תיקייה: `~/.claude/skills/video-ai-storyboard-il/`
2. שמור את הקובץ הזה בתוכה בשם `SKILL.md`
3. הפעל מחדש את Claude Desktop / Cowork
4. ה-skill יטען אוטומטית כשמשתמש יבקש סטוריבורד וידאו

### אופציה C — כקובץ ייחוס מודפס לצוות
הדפס את הקובץ והעבר לכל מי שעובד על פרויקטים של וידאו AI בצוות שלך. שמש כצ'קליסט בכל פרויקט חדש.

---

## 👋 ברוך הבא! בואו נתחיל מהבסיס

**הוראה ל-Claude (ה-AI):** לפני שאתה כותב שורה אחת של פרומפט או מתחיל לבנות HTML, **שאל את המשתמש את השאלון הבא**. אל תקפוץ ישר ליצירה. הבריף הוא הכל.

### 🟢 שאלון פתיחה — תשאל את המשתמש

1. **איזה סוג וידאו אתה רוצה ליצור היום?**
   - פרסומת לרשתות חברתיות (Reels / TikTok / Stories — 15-30 שניות)
   - וידאו חינוכי / הסבר (1-3 דקות)
   - רביל / סרטון פתיחה למותג (5-10 שניות)
   - וידאו עם דמות מדברת (פודקאסט / יוטיוב)
   - אחר — תאר במילים שלך

2. **מי הקהל היעד?** (מורים, הורים, צעירים דתיים, אנשי עסקים, ילדים, חרדים, חילונים...)

3. **מה האורך המבוקש?** (10 שניות / 20 שניות / דקה...)

4. **באיזה פורמטים אתה צריך?**
   - 9:16 (אנכי לרילז / טיקטוק / סטוריז)
   - 1:1 (ריבוע לפיד)
   - 16:9 (אופקי ליוטיוב)
   - כולם

5. **באיזה שפה הוואיסאובר?** עברית / אנגלית / שתיהן?

6. **יש לך כבר חומרי מותג מוכנים?** (מה שיש לך כבר ביד)
   - לוגו (PNG שקוף ברזולוציה גבוהה)
   - פונט המותג
   - פלטת צבעים (HEX codes)
   - תמונת דמות / שחקנית (לעקביות פנים בין סצנות)
   - מיקומים / רפרנסים ויזואליים
   - לוגו של שותפים (לקרדיט בסוף)

7. **מה ה-insight / המסר המרכזי?** (מה אתה רוצה שהצופה ירגיש או יעשה אחרי שהוא רואה את הוידאו)

8. **יש מגבלות מיוחדות?** (קהל דתי = צניעות, ילדים = ללא תוכן מסוכן, סינון מותגים מתחרים, וכו')

### ⏸ עצור ותחכה לתשובות

**רק אחרי שקיבלת תשובות מלאות**, עבור לשלב הבא.

---

## 📐 שיטת העבודה — 7 שלבים מובנים

### 🔵 שלב 1: בריף וקונספט

**אחרי שיש לך את התשובות מהשאלון, תגבש:**

- **קונספט מרכזי** במשפט אחד (לדוגמה: "המורה מקשיבה לפלייליסט שלה בכל מצב יומיומי — וגם בכיתה, ההוראה היא פלייליסט")
- **קשת רגשית** (סצנה 1 = פתיחה אנרגטית → סצנה 4 = קונפליקט → סצנה 6 = פתרון → סצנה 7 = CTA)
- **טון** (חם / קליל / מקצועי / מצחיק / טכני)
- **רפרנסים קולנועיים** (איזה פרסומות / סרטים מזכירים את הויב המבוקש)

**הצג את הקונספט למשתמש לאישור לפני שאתה ממשיך.**

---

### 🔵 שלב 2: פירוק לסצנות

**חוקים פר סצנה:**

- כל סצנה = 2-5 שניות (לרילז) או 3-8 שניות (וידאו ארוך יותר)
- כל סצנה צריכה **תכלית ברורה** (מה הצופה אמור להרגיש ברגע הזה)
- כל סצנה צריכה **מעבר** (cut sec, fade, push-in...) לסצנה הבאה

**מבנה סטנדרטי לפרסומת 20-25 שניות:**

| # | סצנה | משך | תפקיד |
|---|------|-----|--------|
| 1 | פתיחה / hook | 3s | תפיסת תשומת לב |
| 2 | קונפליקט / בעיה | 4s | "אני יודע על מה אתה מדבר" |
| 3 | יותר קונפליקט / escalation | 4s | "זה באמת מתסכל" |
| 4 | הצגת הפתרון | 3s | "אבל יש פיתרון!" |
| 5 | הפתרון בפעולה | 5s | "וזה עובד מצוין" |
| 6 | פייאוף רגשי | 3s | "מה אני מרגיש עכשיו" |
| 7 | CTA + מותג | 4s | "תנסה גם!" |

**הצג את הפירוק למשתמש לאישור לפני שאתה כותב פרומפטים.**

---

### 🔵 שלב 3: בניית HTML סטוריבורד אינטראקטיבי

**ה-HTML הוא ה-deliverable העיקרי.** הוא מאפשר למשתמש:
- לעקוב אחרי כל הסצנות עם sidebar נוויגציה
- להעתיק פרומפטים בלחיצה
- להעלות תמונות וסרטונים שנוצרו (drag & drop)
- לסמן סצנות כהושלמו / לקפל אותן
- לראות התקדמות גלובלית

**מבנה הקוד (JS data model פר סצנה):**

```javascript
const SCENES = [
  {
    n: 1,                                    // מספר סצנה
    time: "0:00 – 0:03",                     // timecode
    titre: "כותרת קצרה של הסצנה",
    objectif: "מה הצופה צריך להרגיש כאן",
    visuel: "תיאור ויזואלי בצרפתית/עברית למשתמש",
    duration: "3s",
    tenue: "תיאור התלבושת של הדמות",
    device: "Smartphone / laptop / etc.",
    mood: "אנרגיה / רגוע / חזק",
    motionType: "i2v",                       // "i2v" או "f2f"
    imagePrompt: `Prompt באנגלית לכלי תמונה...`,
    motionPrompt: `Prompt באנגלית לכלי וידאו...`,
    voTextHe: "טקסט וואיסאובר בעברית",
    voTimingNote: "הערות תזמון",
    voiceoverFr: "תרגום לצרפתית/אנגלית",
    f916: "תיאור הקדרינג ל-9:16",
    f11: "תיאור הקדרינג ל-1:1",
    f169: "תיאור הקדרינג ל-16:9",
    transition: "הוראת מעבר לסצנה הבאה",
    bShot: { ... }                           // אופציונלי: לקיחה משלימה
  }
];
```

**שני סוגי תנועה (motionType):**

- **`i2v`** (image-to-video) — תמונה אחת + פרומפט תנועה → וידאו של 2-5 שניות. סטנדרט.
- **`f2f`** (frame-to-frame) — תמונת START + תמונת END + פרומפט אינטרפולציה. לסצנות עם שינוי משמעותי (התחלה→סוף).

**שדות נוספים ל-f2f:**

```javascript
{
  motionType: "f2f",
  imagePromptStart: `Prompt לתמונת ההתחלה...`,
  imagePromptEnd: `Prompt לתמונת הסוף...`,
  motionPrompt: `Prompt לאינטרפולציה...`,
}
```

**הקובץ HTML עצמו צריך לכלול:**

1. CSS פלטה (CSS variables לעקביות צבע)
2. Sidebar navigation עם state פר סצנה ב-localStorage
3. Hero section עם title + meta
4. טבלת recap של כל הסצנות
5. רינדור דינמי של ה-SCENES array
6. רכיב upload עם IndexedDB לאחסון הקבצים שהמשתמש מעלה
7. כפתורי "Copier" פר פרומפט
8. Lightbox לתצוגה מקדימה
9. Stats banner עם progress

---

### 🔵 שלב 4: הפקת תמונות בכלי AI

**הכלים מומלצים (לפי סדר עדיפות):**

1. **Nano Banana** (Google Gemini) — הכי טוב לקומפוזיטינג עם רפרנסים מרובות, שומר על לוגואים נאמן יחסית
2. **Flow / Veo** (Google DeepMind) — איכות קולנועית גבוהה, גם תמונה וגם וידאו
3. **Midjourney** — איכות אסתטית מצוינת, אבל פחות שליטה על רפרנסים מדויקים

**עקרונות לכתיבת פרומפט תמונה:**

1. **התחל עם תיאור הסגנון** ("Cinematic editorial photograph", "Hyperrealistic", "8K")
2. **תאר את הדמות** באמצעות `CHAR_DESC` קונסטנטה גלובלית (לעקביות בין הסצנות)
3. **תאר את הסביבה** עם **landmarks ספציפיים** (לא "city" אלא "Tel Aviv Tayelet wave-pattern tiles")
4. **תאר את הפעולה** ברור (מה הדמות עושה ברגע הזה)
5. **תאר את התאורה** (golden hour / cathedral light / soft window light)
6. **תאר את הקומפוזיציה** (rule of thirds, framing)
7. **תאר את ה-color grade** (Mediterranean cinematic / A24 / Roger Deakins style)
8. **סיים עם `NEGATIVE:`** — מה לא לכלול (no text, no logos, no readable signs, no watermarks)

**דוגמה לפרומפט תמונה מינימלי תקין:**

```
[MODESTY_PRIORITY constant] Cinematic editorial three-quarter front-angle photograph of a [CHAR_DESC], captured at sunrise golden hour on the Tel Aviv Tayelet (the iconic Mediterranean beach promenade with wave-pattern tiles and modern beachfront hotels). She is [ACTION DESCRIPTION]. She wears [WARDROBE]. Setting: [SPECIFIC LANDMARKS]. Lighting: golden hour rim light. Shot on cinema camera with anamorphic 35mm lens at T2.8. Color grade: warm Mediterranean cinematic. Composition: rule of thirds. Style: aspirational lifestyle. Hyperrealistic, 8K. NEGATIVE: no readable text, no logos, no watermarks.
```

---

### 🔵 שלב 5: הפקת מוטיון (וידאו)

**הכלים מומלצים:**

1. **Kling 2.0** — איכות מצוינת, נאמן יחסית לתמונת ה-input
2. **Seedance** — מהיר, אבל יש פילטר אנטי-קופירייט קשוח (מסנן את כל המותגים)
3. **Omni** — דומה ל-Seedance, אבל יותר רגיש לסינון תוכן רגיש (ילדים בכיתה, מועדון לילה)
4. **Runway Gen-3** — איכות גבוהה, יקר יותר
5. **Flow / Veo** — לסצנות קולנועיות מורכבות

**עקרונות לכתיבת פרומפט תנועה:**

1. **CAMERA:** תאר את תנועת המצלמה (locked / push-in / pan / orbit)
2. **PACING:** תאר את הקצב (energetic / calm / cinematic crescendo)
3. **TIMING BEATS:** פרק את הסצנה ל-beats תזמוניים מדויקים (`at 0.0-0.7s — action A; at 0.7-1.3s — action B...`)
4. **LAYER — X:** תאר את האלמנטים בנפרד (LAYER — HAIR, LAYER — SCREEN, LAYER — LIGHT)
5. **SOUND DESIGN:** הערה לעורך על מה לעשות באודיו
6. **MOOD:** מה הצופה צריך להרגיש
7. **NEGATIVE:** מה לא לעשות

**מגבלות חשובות:**

- **Seedance:** מקסימום **4000 תווים** בפרומפט
- **Omni:** מסנן אגרסיבי לתוכן ילדים — אל תכתוב "teacher + children + classroom" ביחד. השתמש ב-"young woman", "small seated figures", "warm room" במקום
- **כל הכלים:** אל תכתוב שמות מותגים שאינם שלך (Nike, Apple, iPhone, Spotify) — תשתמש בתחליפים גנריים ("smartphone", "wireless earbuds", "music streaming app")

---

### 🔵 שלב 6: Workflow איטרטיבי לסצנות מורכבות (רביל מותג / CTA)

**הבעיה:** כלי AI לא יודעים מה זה "הלוגו של Wizdi" או "הלוגו של HASHBACHA". הם ימציאו לוגו משלהם.

**הפתרון:** **קומפוזיטינג איטרטיבי** — בנה את הסצנה צעד-צעד, כל פעם הוסף לוגו אחד עם **רפרנס תמונה מדויק**, ב**שפה אוניברסלית** ("the brand mark from REFERENCE 2").

**מבנה compositingSteps פר סצנה:**

```javascript
{
  motionType: "f2f",
  compositingSteps: [
    {
      badge: "1A",
      label: "בסיס אטמוספרה (ריק, ללא לוגואים)",
      color: "#1565C0",
      refs: [
        { priority: 'optional', label: 'רפרנסים אופציונליים לאינספירציה' }
      ],
      prompt: `Generate a cinematic background — VERTICAL 9:16. Empty composition with empty center and empty bottom third for later compositing. [...] NEGATIVE: NO text, NO logo, NO bird, NO people.`
    },
    {
      badge: "1B",
      label: "הוסף את הלוגו המרכזי",
      color: "#B8336A",
      refs: [
        { priority: 'max', label: 'REFERENCE 1 = התמונה שיצרת בשלב 1A' },
        { priority: 'max', label: 'REFERENCE 2 = הלוגו שלך כ-PNG שקוף' }
      ],
      prompt: `COMPOSITING TASK: take REFERENCE 1 (background) and integrate into its CENTER the brand mark shown in REFERENCE 2. KEEP THE EXACT SHAPE of REFERENCE 2 — do NOT redraw, do NOT stylize. Apply cinematic lighting integration. KEEP THE BACKGROUND EXACTLY AS REFERENCE 1. [...]`
    },
    {
      badge: "1C",
      label: "הוסף את ה-wordmark מתחת",
      refs: [/* ... */],
      prompt: `COMPOSITING TASK: take REFERENCE 1 (previous result with central logo) and add the wordmark from REFERENCE 2 below the central logo. [...]`
    },
    {
      badge: "1D",
      label: "הוסף לוגו שותף 1 (בתחתית שמאל)",
      /* ... */
    },
    {
      badge: "1E",
      label: "הוסף לוגו שותף 2 (בתחתית ימין) — FINAL FRAME",
      /* ... */
    }
  ],
  motionPrompt: `5-second f2f interpolation. START FRAME = result of step 1A (empty atmosphere). END FRAME = result of step 1E (fully composited final). The animation interpolates from empty to full composited reveal.`
}
```

**עיקרון מפתח:**

> **לעולם אל תקרא ללוגו בשם המותג בפרומפט** ("the Wizdi owl", "the HASHBACHA logo").
> **תמיד תשתמש בשפה אוניברסלית** ("the brand mark from REFERENCE 2", "the partner logo provided as PNG").
> כך ה-AI מבין שהוא צריך לשמר את התמונה המצורפת בדיוק, ולא להמציא משהו דומה.

---

### 🔵 שלב 7: עריכה סופית והפקה

**אחרי שיש לך את כל הסרטונים מ-Flow / Kling / Seedance:**

1. **CapCut / DaVinci Resolve / Premiere** — assembly + עריכת אודיו
2. **ElevenLabs** — קריינות בעברית (קול חם, נשי בדרך כלל, "סמול בקול")
3. **Music** — מוסיקת רקע מ-Epidemic Sound / Artlist
4. **Captions** — כתוביות בעברית (אופציונלי לסטוריז / יוטיוב)
5. **Color grading** — אם יש חוסר אחידות בין הסצנות

**הפוסט-פרודקשן זה הרגע לתקן:**
- חוסר אחידות פלטה בין סצנות
- הוספת לוגו אמיתי על תמונה גנרית
- סנכרון אודיו → ויזואל
- מעברים חלקים

---

## 🔑 עקרונות מפתח (כללים חשובים שלמדתי בכאב)

### 1. ⚖️ צניעות בקונטקסט ישראלי

לקהל דתי / מסורתי / חינוכי, **חובה** לכלול בכל פרומפט:

```
MODESTY CONSTRAINT — HIGHEST PRIORITY, NON-NEGOTIABLE:
The subject is dressed in modest attire adapted to the warm Mediterranean climate.
(1) NO cleavage — HIGH round neck / crew neck only, NO V-neck;
(2) NO bare midriff — stomach fully covered;
(3) The clothing CAN be fitted / sporty / chic — but NO sheer fabric, NO low-cut;
(4) NO turtleneck (climate inappropriate);
(5) Modern modest Israeli style — fitted but covered, not frumpy.
```

**הגדר את זה כקונסטנטה גלובלית** (`MODESTY_PRIORITY`) ושים בתחילת כל פרומפט תמונה.

### 2. 👤 עקביות דמות בין סצנות

**הבעיה:** ה-AI יוצר פנים שונות בכל generation.

**הפתרון:**
1. צור פעם אחת תמונת רפרנס של הדמות (בכל זווית)
2. הגדר `CHAR_DESC` קונסטנטה עם תיאור מדויק (גיל, צבע שיער, צבע עיניים, פנים)
3. בכל פרומפט: צרף את תמונת הרפרנס כ-image-input + ציין `(USE ATTACHED REFERENCE PHOTO for face consistency)`
4. ב-Midjourney: השתמש ב-`--cref` (character reference)
5. ב-Nano Banana / Flow: image-input ישיר

### 3. 🚫 אנטי-קופירייט בפרומפטים

**רשימת מותגים אסורים:** Apple, iPhone, AirPods, Spotify, Nike, Lululemon, Bardugo, ARRI, Kodak, Adobe, Mercedes, וכל מותג שלא שלך.

**תחליפים גנריים:**

| מותג | תחליף גנרי |
|------|------------|
| iPhone | smartphone |
| AirPods | wireless earbuds |
| Spotify | music streaming app |
| Nike | athletic sportswear |
| Lululemon | premium athletic wear |
| MacBook | silver laptop |
| Tesla | modern electric car |

**Seedance / Omni יחסמו לך את הפרומפט אם תכתוב "iPhone".**

### 4. 🗣 שפה אוניברסלית לרפרנסים

**אל תכתוב:** "the Wizdi owl logo", "the HASHBACHA brand mark".

**תכתוב:** "the brand mark from REFERENCE 2", "the partner logo provided as PNG with transparent background".

ה-AI לא יודע מה זה Wizdi. אם אתה אומר לו "use the Wizdi owl", הוא ימציא ינשוף משלו. אם אתה אומר לו "use the brand mark from REFERENCE 2", הוא מבין שהוא צריך לשמר את התמונה שצירפת.

### 5. 🎨 רציפות פלטת צבעים בין סצנות

**הסצנות צריכות להרגיש כמו חלק מאותו עולם.** אם סצנה 5 היא במסיבה צהובה חמה, סצנה 6 לא יכולה לפתע להיות כחולה קרה.

**טיפ:** השתמש בתמונת ה-last frame של הסצנה הקודמת כרפרנס פלטה לסצנה הבאה. ה-AI יקבע אוטומטית את הטונים.

### 6. 🛡 מסנני תוכן רגיש

**אל תכתוב את השילובים האלה ביחד:**

- ❌ "teacher" + "classroom" + "children" → Omni יחסום (child safety filter)
- ❌ "nightclub" + "young woman" + "alcohol" → Seedance יחסום
- ❌ "smoke" + "haze" + "dark" → רוב הכלים יחסמו

**תחליפים בטוחים:**

- "teacher in classroom with children" → "young woman in warm room with small seated figures in soft bokeh"
- "nightclub with DJ" → "music event with mixing booth"
- "haze and smoke" → "warm atmosphere with gentle light"

### 7. 📏 מגבלת תווים

- **Seedance:** 4000 תווים מקסימום בפרומפט. אם עברת — תצמצם.
- **Kling:** 2500 תווים בערך.
- **Flow / Veo:** גמיש יותר.

### 8. 🏷 לוגואים → תמיד ב-POST-PRODUCTION

**עיקרון פרודקשן מקצועי:** AI לא יכול לשחזר לוגו מדויק. **לעולם.**

**איך עובדים במציאות (Universal Pictures, A24, Marvel):**

1. AI מייצר את האטמוספרה הקולנועית (god-rays, particles, lighting)
2. הלוגו האמיתי מתווסף ב-After Effects / CapCut על המסך ה-AI

**אם המשתמש מתעקש לעשות הכל ב-AI:** השתמש ב-compositingSteps עם NanoBanana (שלב 6 לעיל).

---

## 💻 דוגמת קוד מלא — SCENE template

```javascript
const SCENE_TEMPLATE = {
  n: 1,
  time: "0:00 – 0:03",
  titre: "פתיחה — Hook אנרגטי",
  objectif: "תפיסת תשומת לב ב-0.5 שניות הראשונות",
  visuel: "תיאור בעברית למשתמש על מה קורה בסצנה",
  duration: "3s",
  tenue: "תיאור התלבושת (קרוס נק גבוה, ללא חשיפה)",
  device: "smartphone",
  mood: "אנרגיה גבוהה",
  motionType: "i2v",
  imagePrompt: `${MODESTY_PRIORITY}Cinematic editorial photograph of ${CHAR_DESC} on the Tel Aviv Tayelet at sunrise. [ACTION]. [WARDROBE]. [LANDMARKS]. Lighting: golden hour. Color grade: warm Mediterranean. Hyperrealistic, 8K. NEGATIVE: no readable text, no logos, no watermarks.`,
  motionPrompt: `3-second shot. CAMERA: smooth push-in 4%. TIMING BEATS: at 0.0-1.0s [action]; at 1.0-2.0s [action]; at 2.0-3.0s [resolution]. LAYER — HAIR: dynamic motion. LAYER — LIGHT: golden rim. MOOD: empowered active lifestyle.`,
  voTextHe: "טקסט קצר בעברית",
  voTimingNote: "להתחיל ב-0.5s, מסיים ב-2.8s",
  voiceoverFr: "Translation of VO for reference",
  f916: "Format Reels — face high, action center, ground low",
  f11: "Crop tight on action triangle",
  f169: "Wide composition, action center",
  transition: "Cut sec to scene 2"
};
```

---

## 🛠 ארגז הכלים (Stack)

### תמונות (stills)
- **Nano Banana** — Google Gemini, מצוין לקומפוזיטינג עם רפרנסים
- **Flow / Veo** — Google DeepMind, איכות קולנועית
- **Midjourney** — אסתטיקה מצוינת, פחות שליטה
- **Stable Diffusion / Recraft** — אם צריך שליטה מקסימלית

### וידאו (motion)
- **Kling 2.0** — שומר על תמונת input
- **Seedance** — מהיר, אבל פילטר אנטי-מותג חזק
- **Omni** — דומה ל-Seedance, פילטר ילדים חזק
- **Runway Gen-3** — איכות גבוהה
- **Flow / Veo** — קולנועי

### אודיו
- **ElevenLabs** — קריינות בעברית (קולות מומלצים: Bella warm, Rachel)
- **Epidemic Sound / Artlist** — מוסיקת רקע

### עריכה
- **CapCut** — נגיש, חינמי, נהדר לרילז
- **DaVinci Resolve** — מקצועי, חינמי
- **Premiere Pro** — סטנדרט תעשייתי
- **After Effects** — overlay לוגואים, motion graphics

---

## 🚨 שגיאות נפוצות להימנע מהן

### בעיות JavaScript ב-HTML

1. **כפילות keys באובייקט סצנה** → SyntaxError שקט שמכשיל את כל ה-render. תוודא שאין שני `motionPrompt:` באותו אובייקט.

2. **חוסר התאמה בין motionType לשדות** → אם `motionType: "f2f"` ואין `imagePromptStart` ו-`imagePromptEnd`, הסצנה תציג `undefined`.

3. **כפילות SCENES או שינוי שגוי** → תמיד תשמור גיבוי לפני שינוי גדול.

### בעיות סנכרון קבצים

- אם אתה עובד עם Read/Write tools של Claude וה-shell, **תוודא שכותבים תמיד דרך אותה צד**. הסנכרון בין Windows ל-Linux sandbox יכול להישבר.

### בעיות פרומפט

1. **פרומפט גנרי מדי** → "a woman in a city" → לא יביא תוצאה חזקה. **תהיה ספציפי.**
2. **חוסר NEGATIVE** → ה-AI יוסיף טקסט אקראי / לוגואים אקראיים. **תמיד הוסף NEGATIVE.**
3. **חוסר רפרנס פנים** → הדמות תיראה שונה בכל סצנה. **תמיד צרף תמונת רפרנס.**
4. **שמות מותגים** → סינון אנטי-קופירייט יחסום. **השתמש בתחליפים.**
5. **תוכן רגיש** → ילדים + כיתה + מורה ביחד → מסנן בטיחות יחסום. **תמיד תפשט.**

---

## 📝 איך משתמשים בקובץ הזה

### אופציה 1: כתחילת שיחה עם Claude

העתק את כל התוכן של הקובץ הזה והדבק בתחילת שיחה חדשה עם Claude / ChatGPT / Gemini. ה-AI יבין מיד את שיטת העבודה.

### אופציה 2: כ-Skill ב-Cowork / Claude Desktop

שמור את הקובץ כ-`SKILL.md` בתיקיית skills של Cowork. ה-AI יטען אותו אוטומטית כשהמשתמש מבקש לבנות סטוריבורד.

### אופציה 3: כמדריך פנימי לצוות

הדפס את הקובץ והעבר לכל חבר בצוות. השתמש כצ'קליסט בכל פרויקט וידאו AI.

---

## 🎯 סיכום: זרימת עבודה מהירה

```
1. שאל את המשתמש את השאלון (8 שאלות)
   ↓
2. גבש קונספט + קשת רגשית — הצג לאישור
   ↓
3. פרק לסצנות (5-8 סצנות) — הצג לאישור
   ↓
4. בנה HTML storyboard אינטראקטיבי עם:
   - sidebar navigation
   - הקלטת state ב-localStorage
   - upload slots עם IndexedDB
   - פר סצנה: imagePrompt + motionPrompt + multi-format + VO + transition
   ↓
5. עבור סצנה-סצנה, כתוב פרומפטים:
   - תמונה (i2v) או START+END (f2f)
   - תנועה
   - תוודא: MODESTY + CHAR_DESC + landmarks + NEGATIVE
   ↓
6. לסצנות מורכבות (CTA / רביל מותג):
   - השתמש ב-compositingSteps עם 5 שלבים איטרטיביים
   - שפה אוניברסלית ("REFERENCE 1", "REFERENCE 2")
   ↓
7. המשתמש יוצר את התמונות (Nano Banana / Flow)
   ↓
8. המשתמש יוצר את הסרטונים (Kling / Seedance / Flow)
   ↓
9. עריכה סופית ב-CapCut / DaVinci + ElevenLabs + מוסיקה
   ↓
10. ייצוא לפורמטים שונים (9:16 / 1:1 / 16:9)
```

---

**בהצלחה! עכשיו תשאל את המשתמש את שאלה מס' 1 מהשאלון.**

---

*קובץ מתודולוגיה זה נוצר על בסיס פרויקט פרסומת לפלטפורמת חינוך ישראלית. כל העקרונות נלמדו "בכאב" — דרך ניסיון וטעייה. אם יש לך הצעות שיפור, תוסיף בסעיף שינויים בסוף הקובץ.*

## 📋 לוג שינויים

- **v1.0** — מהדורה ראשונה. שלושת השלבים העיקריים: שאלון, מתודולוגיה, עקרונות. workflow איטרטיבי עם compositingSteps.
