# IMAGE LINE — Premium Visual Prompt Methodology

Craft ultra-detailed prompts for AI image generators (Flow, Midjourney, DALL-E, Firefly, Ideogram, Nano Banana, Imagen, Stable Diffusion) that consistently deliver: premium 3D/photoreal/dashboard quality, correctly rendered embedded text (including RTL), exact brand wordmark preservation, character family consistency, and faithful language integrity.

The methodology is language-agnostic — any brand, any product line, any language. The intake questionnaire (SKILL.md §2, image version) must be answered first. The golden rules (SKILL.md §3) apply throughout.

Also used by the VIDEO LINE whenever a scene's still needs embedded brand text or UI elements.

---

## 1. Universal prompt structure

Every prompt follows this skeleton, adapted section by section:

```
[FORMAT DECLARATION]
[RENDER STYLE]
[CRITICAL BRANDING RULE]
[MAIN SUBJECT — with pose/action]
[SUPPORTING ELEMENTS — with labels]
[TEXT ZONES — exact strings + language + RTL/LTR notes]
[BACKGROUND]
[EXPRESSION / MOOD]
[COMPOSITION SUMMARY]
[SPELLING CHECK — verbatim strings]
[NEGATIVE RULES]
[FINAL STYLE — one-paragraph recap]
```

## 2. Format declaration (line 1)

Open with the exact aspect ratio AND pixel dimensions — generators respect shape better when it comes first, in numbers:

- `Create a CINEMATIC 3D PIXAR/DREAMWORKS-STYLE landscape product visual (4:3 aspect ratio, 1440×1080 px).`
- `Create a clean modern PREMIUM SAAS APP-ICON design (1:1 aspect ratio, 1024×1024 px).`
- `Create a vertical social-story motion frame (9:16 aspect ratio, 1080×1920 px).`

If the user says "landscape", ask 4:3 vs 16:9. Don't guess.

## 3. Render style (line 2)

Name the style explicitly. Reliable styles:

- **3D Pixar/DreamWorks CGI** — character mascots, stylized 3D
- **Photorealistic cinematic** — lifestyle product shots
- **Premium SaaS dashboard mockup** — interfaces (Linear/Notion/Apple screenshot family)
- **Modern app-icon** — square buttons (App Store / Linear / Notion aesthetic)
- **Flat 2D vector** — simple iconography

Add lighting hints: `soft global illumination`, `premium warm atmosphere`, `cinematic rim lighting`.

## 4. Critical branding rule (the biggest lever)

Full detail of SKILL.md §3c. If a brand name is embedded, spend a whole paragraph on it:

1. **Spell out the exact form.** `Wiz Chat` → "TWO SEPARATE WORDS with a SPACE between them, each starting with a CAPITAL LETTER followed by lowercase."
2. **Reference the wordmark.** "the [Brand] portion uses the actual provided [Brand] WORDMARK typography EXACTLY (same font, same letter shapes)."
3. **Reject wrong forms explicitly.** `NOT "WIZCHAT" all caps, NOT "Wizchat" no space, NOT "Wiz-Chat" with hyphen` — this drastically reduces bad renders.
4. **Acronyms stay uppercase** (LMS, SEO, API) even inside a title-case brand (`Wiz LMS`).

## 5. Main subject block

### Character / mascot

Describe HEAD and BODY as visibly separate sections — that's what makes family consistency enforceable.

**Character family rule** — for multi-product lines: keep the HEAD identical, vary the BODY. Body variants:

- Flying propulsors / jet thrusters (soaring master)
- Rolling ball-wheel base (BB-8 / EVE style — mobile companion)
- Multi-armed stationary pedestal (precision worker)
- Bouncing spring-legs (playful/festive)
- Standard bipedal (default)
- Tank tracks (heavy-duty)
- Hover platform (glide)
- Wall-mounted (fixed sentinel)

Always state: `The head MUST be in the same [family] — same [helmet/hair/face design]. Head consistency is critical.`

### Interface / dashboard mockup

Describe LAYOUT ZONES as canvas percentages: header (top X%), main hero (X%), side cards (X%), bottom banner (X%). Name every card, its icon, its label. For RTL languages: `Card 1 (top-right in RTL reading = first card read)`.

### App icon (square button)

- Rounded-square filling 100% of canvas
- Solid gradient background (**no fake transparency** — see §11)
- Top ~30% = symbolic 3D element
- Middle ~40% = brand lockup text
- Bottom ~20% = tagline
- Safe padding ~10%

## 6. Supporting elements — labels and tags

Every supporting element (source icon, data card, floating tag, hologram, chart) gets a **label in the target language**, wrapped as a UI element ("small premium translucent tag", "chrome badge") so it doesn't render as free-floating text:

```
- Small 3D PDF document icon labeled "PDF"
- Small 3D text page icon labeled "טקסט"
- Small 3D image/photo frame icon labeled "תמונה"
- Small 3D video play-button icon labeled "סרטון"
```

## 7. Text zones (the #2 highest-leverage section)

Text in AI images is fragile. Apply SKILL.md §3d in full:

- **7a. Only user-provided strings, verbatim.** No invented taglines, no "helpful" translations, no decorative English.
- **7b. Declare RTL** for Hebrew/Arabic/Urdu/Farsi: `(RTL, clean modern Hebrew typography in [color], glowing softly)` + closing SPELLING CHECK block:

```
HEBREW SPELLING CHECK (use ONLY these — no other Hebrew sentences, no English labels):
- "מחולל הפעילויות" exact, RTL
- "בתוך דקות בודדות" exact
- All Hebrew RTL, no flipping, no scrambling
```

- **7c. Preserve gershayim (״ U+05F4)** and diacritics — state fragile characters explicitly (tashkeel, é è à ç ï, ñ).
- **7d. Fallback fonts:** Hebrew → Heebo Bold / Frank Ruhl Libre; Arabic → Cairo / Tajawal; Devanagari → Noto Sans Devanagari; CJK → Noto Sans CJK; Cyrillic → Inter / Manrope; Latin premium → Söhne / Inter / Manrope. Write it into the prompt.
- **7e. Stubborn scrambling** → generate without the fragile text, composite it in Photoshop/Canva/Figma with the recommended font.

## 8. Background block

State color, depth, atmosphere: base gradient (`deep emerald-to-green gradient`), ambient particles (`subtle floating green sparkle particles drifting at varied depths`), volumetric light (`soft volumetric green light beams`), mood word (`premium calm AI workspace atmosphere`). Match the background to the product's brand color (§17).

## 9. Expression / mood block (characters)

```
BIG WIDE OPEN ALERT bright eyes sparkling with [emotion], raised eyebrows of [emotion], soft [smile] mouth, head slightly tilted in [engagement].
```

Kill default drift: `NO sleepy eyes — bright alert`, `NO scary AI vibe`, `NO stiff robot pose — natural warm energy`.

## 10. Composition summary

One paragraph near the end restating the entire scene as a single "final image" sentence, referencing every element. The redundancy is intentional — generators lock composition better when the whole scene is restated:

```
COMPOSITION 4:3 LANDSCAPE: robot hovering centered with jet thrusters glowing below, 4 input sources flowing in from the left with "מכל מקור תוכן" tag, "בתוך דקות בודדות" banner floating above his head, activity outputs fanning right, brand banner at the bottom.
```

## 11. Negative rules (checklist)

Close every prompt with `NEGATIVE RULES (CRITICAL):` preemptively killing the top failure modes:

```
NEGATIVE RULES (CRITICAL):
- ABSOLUTELY NO English words anywhere except the brand "[Brand Name]"
- The brand text MUST be "[Exact Form]" — NOT "[wrong 1]", NOT "[wrong 2]", NOT "[wrong 3]"
- The character body MUST be the [variant] — visually distinct from other family members
- The head MUST be in the same [family] design — head consistency is critical
- NO fake transparent-background checker pattern (app icons)
- NO scrambled Hebrew/Arabic letters
- NO photorealistic children (education products — use holograms/silhouettes)
- NO readable sentences on decorative page content (abstract writing patterns only)
- NO sleepy eyes — bright alert
- NO stiff robot pose — natural warm energy
```

## 12. Final style paragraph

End with a one-paragraph stylistic-brief recap — this double-locks the composition:

```
FINAL STYLE: a premium landscape 4:3 product visual for [Brand] — a [subject] with [head consistency note] but a UNIQUE [body variant]. [Action]. [Text zones summary]. [Palette]. [Mood].
```

---

## 13. App-icon template (solves the #1 icon failure: fake transparency)

```
Create a clean modern PREMIUM SAAS APP-ICON design (1:1 aspect ratio, 1024×1024 px) in the style of high-end app icons (Apple App Store / Linear / Notion). SOLID BUTTON-STYLE — NOT floating on transparent.

ICON SHAPE: rounded-square button filling the entire 1024×1024 canvas, smooth rounded corners (radius ~22%). Premium glossy 3D look.

BUTTON BACKGROUND: premium gradient from [DEEP COLOR 1] (top-left) to [BRIGHT COLOR 2] (bottom-right). Smooth, glossy, subtle 3D depth. NO transparent background — full solid gradient fill.

INSIDE THE BUTTON (top to bottom):

1. SYMBOLIC ELEMENT (top ~30%):
[One centered 3D icon — e.g. chrome key with glowing tips, generator orb with orbiting micro-icons, chat bubble with sparkle.]

2. BRAND LOCKUP TEXT (middle ~40%):
Centered, large and readable, displaying "[Brand Name]" with proper title-case + space (or acronym uppercase rules):
- "[Prefix]" in actual provided WORDMARK typography EXACTLY — WHITE with soft glow halo
- SPACE (if applicable)
- "[Suffix]" in IDENTICAL font style — also WHITE
- NOT "[wrong 1]", NOT "[wrong 2]", NOT "[wrong 3]"

3. TAGLINE (bottom ~20%):
"[Tagline in target language]" in clean modern [language] typography ([font recommendation]), medium-small, soft [color] with subtle glow, [RTL/LTR] aligned, centered.

4. SAFE PADDING ~10% around all edges.

STYLE: premium glossy 3D app-icon, subtle 3D depth, glass-morphism feel.

NEGATIVE RULES:
- NO transparent background, NO checkered pattern
- NO English labels anywhere except the brand
- NO scrambled non-Latin text
- NO mascot, NO floating elements outside the button
- NO wrong forms of the brand text
```

## 14. Interface / dashboard mockup template

```
Create a CINEMATIC PREMIUM 3D DASHBOARD MOCKUP UI design ([aspect ratio], [pixels]) — a premium SaaS-product interface mockup. [Reference existing family style if applicable]. Same dark deep background, same glossy glass-morphism card panels, same modern [language] RTL/LTR layout, same premium SaaS aesthetic. This is a PRODUCT INTERFACE MOCKUP, NOT a character icon. NO robot, NO mascot.

LAYOUT ZONES (top to bottom):

HEADER ZONE (~12% top):
- Top corner: small premium pill badge "[label]" with icon
- Center: brand name "[Brand X]" with exact wordmark spec
- Below brand: main tagline + small subtitle

DESCRIPTION ZONE (~8%):
Short description sentence (target language, RTL if applicable).

MAIN DASHBOARD ZONE — [N] cards in a balanced grid (~60-70%):
Per card: title, icon, contents (chart / table / meter / grid), realistic demo data with labels in the target language.

SIDE / BOTTOM ZONES (~20-30%):
Benefit cards, live indicators, per-user tables.

BOTTOM BANNER STRIP (~10%):
Line 1: main tagline · Line 2: brand lockup with exact wordmark spec · Line 3: sub-label (availability/scope)

OVERALL STYLE:
- Dark deep [product color] gradient background, subtle glowing UI grid lines
- Premium glassy chrome card edges with subtle inner [color] glow
- Soft 3D rendered chart elements
- Clean modern [language] typography ([font recommendation])

[SPELLING CHECK block]
[NEGATIVE RULES block]
FINAL STYLE: [one-paragraph recap]
```

## 15. Video / motion frame prompts

For frames feeding a video tool (Kling, Runway, Veo, Sora):

- Add motion cues: `slight forward motion`, `soft camera dolly`, `subject moves left to right`
- Never freeze a character mid-air across frames — describe continuous movement
- For frame-to-frame consistency, describe every constant element identically (clothing, lighting, background)
- End with: `matches previous frame identically except [what changes]`

For the full scene/motion workflow (i2v vs f2f, TIMING BEATS, compositing), switch to `references/video-storyboard.md`.

## 16. Working across languages

| Element | English | French | Hebrew | Arabic | Spanish |
|---|---|---|---|---|---|
| Direction | LTR | LTR | **RTL** | **RTL** | LTR |
| Fonts | Inter, Söhne | Inter, Manrope | Heebo, Frank Ruhl Libre | Cairo, Tajawal | Inter, Manrope |
| Fragile chars | — | é è à ç ï ù | ״ (gershayim), ׳ | tashkeel ـَ ـِ ـُ | ñ á é í ó ú |
| Spelling check | optional | recommended | **required** | **required** | recommended |

When the brief is in one language but the visual targets another audience: embedded text in the visual's target language, conversation in the brief's language.

## 17. Color palettes (starter set — adapt per brand)

Two gradient stops each, for smooth premium backgrounds:

- Master/hero product → `deep green to emerald` OR `deep violet to gold`
- Dialogue / social → `deep violet to magenta`
- Evaluation / feedback → `deep emerald to teal-mint`
- Insights / analytics → `deep cyan-teal to turquoise`
- Management / core → `deep navy to sky-blue`
- Books / reading → `deep teal to turquoise`
- Lesson-plans / creativity → `deep amber to bright orange`
- Play / games → `bright yellow to festive pink`
- Toolkit / utility → `deep copper to bronze-amber`
- Security / trust → `deep navy to steel silver`
- Health / wellness → `deep mint to sage green`

## 18. Full worked example — character in action, multilingual

Real-world pattern (Hebrew + French brief, English generator language):

```
Create a CINEMATIC 3D PIXAR/DREAMWORKS-STYLE landscape product visual (4:3 aspect ratio, 1440×1080 px). Full Pixar-quality 3D CGI render — soft global illumination, premium futuristic atmosphere. Use the provided [Brand] wordmark EXACTLY for the brand text.

CRITICAL BRANDING RULE:
The product name is "Wiz Gen" — TWO SEPARATE WORDS with a SPACE between them, each starting with a CAPITAL LETTER followed by lowercase. "Wiz" uses the actual provided Wizdi WORDMARK typography EXACTLY. "Gen" uses the IDENTICAL font style. Combined: "Wiz Gen" with a space. NOT "WIZGEN" all caps, NOT "Wizgen" no space, NOT "Wiz-Gen" hyphen.

CHARACTER — Wiz Gen ROBOT, FLYING BODY VARIANT:
HEAD (family-consistent):
- Glass dome helmet showing cute blue owl face inside
- Big wide open alert eyes, soft beak, eyebrow tufts
- Chrome antennas with green LED tips
BODY (distinct — flying architect):
- Compact chrome torso in chrome-and-green armor
- NO standard legs — CHROME ROCKET-PROPULSOR BASE with two angled jet-thruster nozzles emitting soft glowing green energy plumes downward (the robot HOVERS)
- Mechanical wing-arms
- Chest LED nameplate reads: "Wiz Gen" (title case with space)

POSE: hovering centered, generator orb in one wingtip, other wing directing output flow.

LEFT SIDE — 4 CONTENT SOURCES FLOWING IN, each with Hebrew label:
- 3D PDF icon "PDF"
- 3D text page "טקסט"
- 3D image frame "תמונה"
- 3D video play-button "סרטון"
Above: small Hebrew tag "מכל מקור תוכן"

CENTER — TRANSFORMATION FLOW: green particle streams from inputs into the robot's orb, exiting to the right output side.

Small Hebrew banner above robot's head: "בתוך דקות בודדות" (no English "SPEED" word).

RIGHT SIDE — activity output cards fanning out, above: "יחידות לימוד ופעילויות אינטראקטיביות"

BOTTOM BANNER:
Line 1 (RTL Hebrew, white-green gradient): מחולל הפעילויות מבוסס בינה מלאכותית
Line 2 (brand lockup): "Wiz Gen" (Wizdi wordmark + space + matching font)
Line 3 (small sub-label): לכל שכבות הגיל, המקצועות ושלבי החינוך

BACKGROUND: deep green-to-emerald gradient ambient, floating green sparkle particles, glowing neural-grid bokeh.

EXPRESSION: big wide open alert bright eyes sparkling with focused creator energy, soft confident smile.

HEBREW SPELLING CHECK:
- "מכל מקור תוכן" exact
- "טקסט" / "תמונה" / "סרטון" / "PDF" exact
- "בתוך דקות בודדות" exact
- "יחידות לימוד ופעילויות אינטראקטיביות" exact
- "מחולל הפעילויות מבוסס בינה מלאכותית" exact
- "לכל שכבות הגיל, המקצועות ושלבי החינוך" exact
- All Hebrew RTL, no flipping, no scrambling

NEGATIVE RULES:
- NO English words anywhere except the brand "Wiz Gen"
- Brand MUST be "Wiz Gen" with space and title case — NOT "WIZGEN", NOT "Wizgen", NOT "Wiz-Gen"
- Body MUST be flying propulsors — NO standard legs
- Head MUST match Wiz family — glass dome + cute owl face
- NO scrambled Hebrew, NO sleepy eyes

FINAL STYLE: a premium landscape 4:3 product visual for Wiz Gen — cute cyborg with owl-head glass dome but unique flying propulsor body, hovering centered, generating activities from 4 content sources on the left into interactive learning outputs on the right, with "בתוך דקות בודדות" Hebrew banner above head and brand banner at the bottom. Deep green premium atmosphere. NO English labels except brand.
```

## 19. Quick-start cheat sheet (minimum viable prompt)

```
Create a [FORMAT: aspect ratio + pixels] [STYLE] visual.

BRAND: "[Exact Name]" — [spelling rule + wrong forms rejected]. Use provided wordmark exactly.

SUBJECT: [character: head + body + pose] OR [interface: N cards + layout]

TEXT ZONES (target language, RTL/LTR):
- "[String 1]" — where, size, color
- "[String 2]" — where, size, color

BACKGROUND: [gradient + particles + mood]

NEGATIVE:
- NO English (except brand)
- NO wrong brand forms
- NO [other failure modes]

FINAL STYLE: [one-paragraph recap]
```

Adapt every block from §1–§18 as needed; skip sections that don't apply.

---

## Notes

- Developed through iterative refinement across a full EdTech product line (9 products, multilingual, multi-character). Each rule fixed a specific real-world failure — don't skip the ones that seem redundant.
- Update the palette and font tables per project.
- Keep the negative-rules block generous. It's the most cost-effective section of the entire prompt.
