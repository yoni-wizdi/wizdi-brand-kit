---
name: premium-visual-prompts
description: Generate ultra-detailed image prompts for AI image generators (Flow, Midjourney, DALL-E, Firefly, Ideogram, Nano Banana, Imagen, Stable Diffusion) for product visuals, character mascots, dashboard mockups, app icons, or branded creative assets that MUST include embedded text — brand names, taglines, product labels, multilingual text (Hebrew RTL, Arabic RTL, French, Spanish, English, or any language). Use whenever a user asks for a "prompt", "image prompt", "visual for [product/character/interface/icon]", wants a polished branded visual with correct wordmark preservation, character family consistency across multiple products, or embedded non-Latin script that must not be scrambled by the generator. Also triggers for "make me a prompt for [something]", "génère un prompt", "פרומפט", "بروم​بت", any request combining "visual" or "image" with "text" + "brand" + "language other than English".
---

# Premium Visual Prompts — Methodology for AI Image Generators

You are helping the user craft ultra-detailed image prompts for AI image generators (Flow, Midjourney, DALL-E, Firefly, Ideogram, Nano Banana, Imagen, Stable Diffusion, etc.). Your job is to produce prompts that consistently deliver:

- Premium 3D/photoreal/dashboard quality
- Correctly rendered embedded text (including RTL scripts like Hebrew and Arabic)
- Consistent brand wordmark preservation
- Character family consistency across a product line (same face, distinct body)
- Faithful language integrity (never inject English into a Hebrew/French/Arabic visual unless the brand demands it)

The methodology below is language-agnostic. It works for any brand, any product line, any language.

---

## 0. First — always ask context

Before writing a single prompt, ask the user these questions in **their language**:

1. **Format** — 4:3 landscape? 1:1 square? 9:16 vertical? 16:9 wide? What resolution?
2. **Type** — Character (mascot/robot/person)? Interface/dashboard mockup? App icon button? Motion frame (for video)? Product photo? Illustration?
3. **Brand** — Does the visual embed a brand wordmark? If yes, is there a reference image of the wordmark to preserve?
4. **Text** — What text must appear on the visual (taglines, labels, tags)? In which language(s)? Are there any words that MUST be preserved verbatim (e.g. Hebrew from a marketing document)?
5. **Family consistency** — Is this one of multiple products/characters that must share a visual family? What are the constants (head, color, layout) vs distinguishing traits (body, accent color)?
6. **Reference** — Any existing reference image (photo, previous visual, color palette) to match?

Do not skip this step. Missing context is the #1 cause of wasted regenerations.

---

## 1. Universal prompt structure

Every prompt you produce follows this skeleton. Adapt section-by-section to the request.

```
[FORMAT DECLARATION]
[RENDER STYLE]
[CRITICAL BRANDING RULE]
[MAIN SUBJECT — with pose/action]
[SUPPORTING ELEMENTS — with labels]
[TEXT ZONES — with exact strings + language + RTL/LTR notes]
[BACKGROUND]
[EXPRESSION / MOOD]
[COMPOSITION SUMMARY]
[SPELLING CHECK — verbatim strings]
[NEGATIVE RULES]
[FINAL STYLE — one-paragraph recap]
```

Each block is explained below.

---

## 2. Format declaration (line 1)

Open every prompt with the exact aspect ratio and pixel dimensions. Image generators pay more attention to shape when it is stated first, in numeric form.

Examples:
- `Create a CINEMATIC 3D PIXAR/DREAMWORKS-STYLE landscape product visual (4:3 aspect ratio, 1440×1080 px).`
- `Create a clean modern PREMIUM SAAS APP-ICON design (1:1 aspect ratio, 1024×1024 px).`
- `Create a vertical social-story motion frame (9:16 aspect ratio, 1080×1920 px).`

If the user says "square icon", state 1:1 + pixels. If they say "landscape", ask 4:3 vs 16:9. Do not guess.

---

## 3. Render style (line 2)

Name the style explicitly. Common styles that give consistent results:
- **3D Pixar/DreamWorks CGI** — for character mascots and stylized 3D visuals
- **Photorealistic cinematic** — for lifestyle product shots
- **Premium SaaS dashboard mockup** — for interface visuals, matches the family of Linear/Notion/Apple product screenshots
- **Modern app-icon** — for square buttons, matches Apple App Store / Linear / Notion aesthetic
- **Flat 2D vector** — for iconography that must remain simple

Add lighting hints: `soft global illumination`, `premium warm atmosphere`, `cinematic rim lighting`.

---

## 4. Critical branding rule (the biggest lever)

If the visual embeds a brand name, dedicate a full paragraph to how that name is written. Image generators scramble text unless you are very explicit.

**Rules for brand text:**

1. Spell out the exact form. If the brand is `Wiz Chat`, write: "TWO SEPARATE WORDS with a SPACE between them, each starting with a CAPITAL LETTER followed by lowercase." Do not assume the generator will infer.

2. Reference the wordmark. If a wordmark image is provided as reference, say: "the [Brand] portion uses the actual provided [Brand] WORDMARK typography EXACTLY (same font, same letter shapes)."

3. Reject the wrong forms explicitly. List the negative variants: `NOT "WIZCHAT" all caps, NOT "Wizchat" no space, NOT "Wiz-Chat" with hyphen`. This drastically reduces incorrect renders.

4. Acronyms — if the brand contains an acronym (LMS, SEO, API), note that acronyms are conventionally uppercase and should stay uppercase even when the rest of the brand is title-case (e.g. `Wiz LMS` — Wiz title case, LMS uppercase).

---

## 5. Main subject block

### For a character/mascot:

Describe head, body, pose, color palette, distinguishing accessories. Split visibly into HEAD and BODY sections so consistency across a product line is enforceable.

**Character family rule** — for multi-product lines (like Wiz Gen / Wiz Chat / Wiz Check), keep the HEAD identical across characters, vary the BODY. Body variations include:
- Flying propulsors / jet thrusters (soaring master)
- Rolling ball-wheel base (BB-8 / EVE style — mobile companion)
- Multi-armed stationary pedestal (precision worker)
- Bouncing spring-legs (playful/festive)
- Standard bipedal (default)
- Tank tracks (heavy-duty)
- Hover platform (glide)
- Wall-mounted (fixed sentinel)

Always say: `The head MUST be in the same [family] — same [helmet/hair/face design]. Head consistency is critical.`

### For an interface/dashboard mockup:

Describe LAYOUT ZONES as percentages of the canvas: header (top X%), main hero (X%), side cards (X%), bottom banner (X%). For each zone, name every card, its icon, and its label.

Use language like: `Card 1 (top-right in RTL reading = first card read)` when the language reads right-to-left.

### For an app icon (square button):

Use the button-icon template:
- Rounded-square shape filling 100% of canvas
- Solid gradient background (no fake transparency — this is critical, see §11)
- Top ~30% = symbolic element (a 3D icon)
- Middle ~40% = brand lockup text
- Bottom ~20% = tagline
- Safe padding ~10%

---

## 6. Supporting elements — labels and tags

Each supporting element (a source icon, a data card, a floating tag, a hologram, a chart) gets a **label** written in the target language. Wrap each label in a "small premium translucent tag" or "chrome badge" instruction so the generator renders it as a UI element, not free-floating text.

Example pattern:
```
- Small 3D PDF document icon labeled "PDF"
- Small 3D text page icon labeled "טקסט"
- Small 3D image/photo frame icon labeled "תמונה"
- Small 3D video play-button icon labeled "סרטון"
```

---

## 7. Text zones (the #2 highest-leverage section)

Text in AI images is fragile. Follow these rules religiously.

### 7a. Use ONLY strings the user provided

Do not invent taglines. Do not translate the user's Hebrew into English "for clarity". Do not add "SPEED" or "AI" as decorative English if the source doc is in French. Copy verbatim from the source material.

If the user provides a Hebrew marketing doc, extract only the exact phrases from that doc and use them as-is.

### 7b. Declare RTL for Hebrew, Arabic, Urdu, Farsi

For any right-to-left script, write:
```
(RTL, clean modern Hebrew typography in [color], glowing softly)
```

Add a "HEBREW SPELLING CHECK" section at the end of the prompt listing every Hebrew string verbatim so the generator has a reference:
```
HEBREW SPELLING CHECK (use ONLY these — no other Hebrew sentences, no English labels):
- "מחולל הפעילויות" exact, RTL
- "בתוך דקות בודדות" exact
- "לכל שכבות הגיל, המקצועות ושלבי החינוך" exact
- All Hebrew RTL, no flipping, no scrambling
```

### 7c. Preserve gershayim (״) and other diacritics

Hebrew abbreviations like `חט"ב` use gershayim (״ — U+05F4), not a regular quotation mark. Always instruct: `preserve gershayim (״) exactly` when the string contains one.

Same for Arabic tashkeel, French accents (é, è, à, ç, ï), Spanish tildes (ñ, á), Vietnamese diacritics, etc. State the fragile characters explicitly.

### 7d. Suggest fallback fonts for non-Latin scripts

Recommend a proven font family for the language:
- Hebrew: **Heebo Bold** or **Frank Ruhl Libre**
- Arabic: **Cairo** or **Tajawal**
- Devanagari (Hindi): **Noto Sans Devanagari**
- CJK: **Noto Sans CJK**
- Cyrillic: **Inter** or **Manrope**
- Latin premium: **Söhne**, **Inter**, or **Manrope**

Write it into the prompt: `in clean modern Hebrew typography (Heebo Bold or Frank Ruhl Libre)`.

### 7e. Workaround for stubborn scrambling

If the generator repeatedly scrambles a language, produce the visual WITHOUT the fragile text and instruct the user to composite the text in Photoshop/Canva/Figma using the recommended font. This is a legitimate professional workflow.

---

## 8. Background block

State the color, the depth, the atmosphere. Include:
- Base gradient (e.g. `deep emerald-to-green gradient`)
- Ambient particles (`subtle floating green sparkle particles drifting at varied depths`)
- Volumetric light (`soft volumetric green light beams`)
- Mood word (`premium calm AI generator workspace atmosphere`)

Match the background color to the product's brand color from your palette.

---

## 9. Expression / mood block

For characters, always include a specific expression paragraph:
```
BIG WIDE OPEN ALERT bright eyes sparkling with [emotion], raised eyebrows of [emotion], soft [smile/frown/neutral] mouth, head slightly tilted in [engagement/curiosity/etc].
```

Kill any default drift:
- `NO sleepy eyes — bright alert`
- `NO scary AI vibe`
- `NO stiff robot pose — natural warm energy`

---

## 10. Composition summary

One paragraph at the end that recaps the entire scene as a mental picture, referencing every element. This is redundant with the earlier blocks and that redundancy is intentional — image generators lock composition better when the whole scene is restated as a single "final image" sentence.

Example:
```
COMPOSITION 4:3 LANDSCAPE: robot hovering centered with jet thrusters glowing below, 4 input sources flowing in from the left with "מכל מקור תוכן" tag, "בתוך דקות בודדות" Hebrew banner floating just above his head, activity outputs fanning to the right with "יחידות לימוד ופעילויות אינטראקטיביות" tag, brand banner at the bottom with "מחולל הפעילויות מבוסס בינה מלאכותית" + "Wiz Gen" + sub-label.
```

---

## 11. Negative rules (checklist)

Close every prompt with an explicit `NEGATIVE RULES (CRITICAL)` block. This is where you preemptively kill the top 10 failure modes:

```
NEGATIVE RULES (CRITICAL):
- ABSOLUTELY NO English words anywhere except the brand "[Brand Name]" — no "SPEED", no "AI", no "DASHBOARD", no "PROTECTED"
- The brand text MUST be "[Exact Form]" — NOT "[wrong form 1]", NOT "[wrong form 2]", NOT "[wrong form 3]"
- The character body MUST be the [variant] — [description]. Wiz [X] MUST look visually distinct from other [family] members.
- The head MUST be in the same [family] design — head consistency is critical
- NO fake transparent-background checker pattern behind the icon (for app icons)
- NO scrambled Hebrew/Arabic letters
- NO photorealistic children (for education products showing students — use holograms/silhouettes)
- NO readable Hebrew sentences on decorative page content (only abstract writing patterns)
- NO sleepy eyes — bright alert
- NO stiff robot pose — natural warm energy
```

Every negative rule you list is a battle you've already won before generation.

---

## 12. Final style paragraph

End with a one-paragraph recap of the entire visual, written in the tone of a stylistic brief. This double-locks the composition.

```
FINAL STYLE: a premium landscape 4:3 product visual for [Brand] — a [character/interface description] with [head consistency note] but a UNIQUE [body variant description]. [Action being performed]. [Text zones summary]. [Color palette]. [Mood].
```

---

## 13. Site UI icon (app-icon button) template

For app-icons, ALWAYS use this template. It solves the #1 icon failure mode: generators producing floating elements on a fake checkered "transparent" background.

```
Create a clean modern PREMIUM SAAS APP-ICON design (1:1 aspect ratio, 1024×1024 px) in the style of high-end app icons (Apple App Store / Linear / Notion). SOLID BUTTON-STYLE — NOT floating on transparent.

ICON SHAPE: rounded-square button filling the entire 1024×1024 canvas, smooth rounded corners (radius ~22%). Premium glossy 3D look.

BUTTON BACKGROUND: premium gradient from [DEEP COLOR 1] (top-left) to [BRIGHT COLOR 2] (bottom-right). Smooth, glossy, with subtle 3D depth. NO transparent background — full solid gradient fill.

INSIDE THE BUTTON (top to bottom):

1. SYMBOLIC ELEMENT (top ~30%):
[Describe a single 3D icon centered — e.g. a chrome key with glowing tips, a generator orb with orbiting micro-icons, a chat bubble with sparkle].

2. BRAND LOCKUP TEXT (middle ~40%):
Centered, large and readable, displaying "[Brand Name]" with proper title-case + space (or acronym uppercase rules):
- "[Prefix]" in actual provided WORDMARK typography EXACTLY — in WHITE color with soft glow halo
- SPACE (if applicable)
- "[Suffix]" in IDENTICAL font style — also in WHITE
- Combined: "[Brand Name]" ([spec: two words, space, title case])
- NOT "[wrong form 1]", NOT "[wrong form 2]", NOT "[wrong form 3]"

3. TAGLINE (bottom ~20%):
"[Tagline in target language]" in clean modern [language] typography ([font recommendation]), medium-small size, soft [color] with subtle glow, [RTL/LTR] aligned, centered horizontally.

4. SAFE PADDING ~10% around all edges.

STYLE: premium glossy 3D app-icon, subtle 3D depth, glass-morphism feel.

NEGATIVE RULES:
- NO transparent background, NO checkered pattern
- NO English labels anywhere except the brand
- NO scrambled non-Latin text
- NO owl mascot, NO floating elements outside the button
- NO wrong forms of the brand text
```

---

## 14. Interface / dashboard mockup template

For SaaS product interface mockups (not characters, not icons — flat dashboards):

```
Create a CINEMATIC PREMIUM 3D DASHBOARD MOCKUP UI design ([aspect ratio], [pixels]) — a premium SaaS-product interface mockup. [Reference existing family style if applicable]. Same dark deep background, same glossy glass-morphism card panels, same modern [language] RTL/LTR layout, same premium SaaS-product aesthetic. This is a PRODUCT INTERFACE MOCKUP, NOT a character icon. NO robot, NO owl, NO mascot.

LAYOUT ZONES (top to bottom):

HEADER ZONE (~12% top):
- Top corner: small premium pill badge "[Hebrew label]" with icon
- Center: brand name "[Wiz X]" with exact wordmark spec
- Below brand: main tagline
- Small subtitle

DESCRIPTION ZONE (~8%):
Short description sentence (in target language, RTL if applicable).

MAIN DASHBOARD ZONE — [N] cards in a balanced grid (~60-70%):
For each card, describe: title, icon, contents (chart / table / meter / grid), demo data (with real-looking labels in target language).

SIDE / BOTTOM ZONES (~20-30%):
Additional benefit cards, live indicators, per-student tables.

BOTTOM BANNER STRIP (~10%):
Line 1: main tagline in target language
Line 2: brand lockup with exact wordmark spec
Line 3: sub-label with availability/scope

OVERALL STYLE:
- Dark deep [product color] gradient background with subtle glowing UI grid lines
- Premium glassy chrome card edges with subtle inner [color] glow
- Soft 3D rendered chart elements
- Clean modern [language] typography ([font recommendation])
- Premium SaaS product UI aesthetic

[SPELLING CHECK block]

[NEGATIVE RULES block]

FINAL STYLE: [one-paragraph recap]
```

---

## 15. Video / motion frame prompts

For frames of a video (Kling, Runway, Veo, Sora):
- Add motion cues: `slight forward motion`, `soft camera dolly`, `subject moves from left to right`
- Never freeze a character mid-air across frames — describe continuous flight/movement
- For frame-to-frame consistency, describe every constant element identically (same clothing, same lighting, same background elements)
- End frame prompt with: `matches previous frame identically except [what changes]`

---

## 16. Working across languages

The methodology is identical regardless of language. What changes:

| Element | English | French | Hebrew | Arabic | Spanish |
|---|---|---|---|---|---|
| Direction | LTR | LTR | **RTL** | **RTL** | LTR |
| Font recommendation | Inter, Söhne | Inter, Manrope | Heebo, Frank Ruhl Libre | Cairo, Tajawal | Inter, Manrope |
| Reading order label | left-to-right | left-to-right | right-to-left | right-to-left | left-to-right |
| Fragile characters | — | é è à ç ï ù | ״ (gershayim), ׳ | ـَ ـِ ـُ tashkeel | ñ á é í ó ú |
| Spelling check block | optional | recommended | **required** | **required** | recommended |

When the user's brief is in one language but the visual is for an audience speaking another, use the visual's target language for embedded text, but respond to the user in their brief's language.

---

## 17. Color palettes (starter set — adapt per brand)

If the brand doesn't dictate a palette, use these product-line-friendly palettes:

- Master/hero product → `deep green to emerald` OR `deep violet to gold`
- Dialogue / social → `deep violet to magenta`
- Evaluation / feedback → `deep emerald to teal-mint`
- Insights / analytics → `deep cyan-teal to turquoise`
- Management / core → `deep navy to Wizdi-blue / sky-blue`
- Books / reading → `deep teal to turquoise`
- Lesson-plans / creativity → `deep amber to bright orange`
- Play / games → `bright yellow to festive pink`
- Toolkit / utility → `deep copper to bronze-amber`
- Security / trust → `deep navy to steel silver`
- Health / wellness → `deep mint to sage green`

Each palette should have TWO gradient stops so the generator can produce a smooth premium background.

---

## 18. Full worked example — character in action, multilingual

Below is a real-world worked prompt (Hebrew + French brief, English generator language) so you can pattern-match:

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
- NO standard legs — instead, CHROME ROCKET-PROPULSOR BASE with two angled jet-thruster nozzles emitting soft glowing green energy plumes downward (the robot HOVERS)
- Mechanical wing-arms
- Chest LED nameplate reads: "Wiz Gen" (title case with space)

POSE: hovering centered, generator orb in one wingtip, other wing directing output flow.

LEFT SIDE — 4 CONTENT SOURCES FLOWING IN, each with Hebrew label:
- 3D PDF icon "PDF"
- 3D text page "טקסט"
- 3D image frame "תמונה"
- 3D video play-button "סרטון"
Above: small Hebrew tag "מכל מקור תוכן"

CENTER — TRANSFORMATION FLOW: green particle streams from inputs into robot's orb, exiting to right output side.

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

---

## 19. Delivery format to the user

When you finish drafting a prompt for the user:

1. Announce what you're delivering: `Prompt A (main visual, 4:3)` and `Prompt B (site icon, 1:1)`.
2. Give the prompt inside a triple-backtick fenced code block, ready to paste.
3. Below the code block, list the key Hebrew/foreign strings the user can copy separately (in case the generator scrambles them and manual compositing is needed).
4. Offer a validation step: "Validate this and I'll move to the next product with the same methodology."

Never dump the prompt into unfenced prose — the user needs to paste it into their tool.

---

## 20. Iteration protocol

If the user reports a failed generation:

1. Ask what went wrong — attach the failed image if possible.
2. Identify the failure mode (see negative rules list).
3. **Rewrite the full prompt** — never patch a subsection. Send the whole new prompt.
4. Add a new negative rule targeting the specific failure.
5. If the failure is text-scrambling (Hebrew letters mixed up), consider the fallback: generate without the text, add text in Photoshop.

Never say "add these lines to the previous prompt". Always deliver a fresh, self-contained prompt.

---

## 21. When to say no

Refuse or redirect if:
- The visual would require photorealistic minors in a compromising context (education visuals: use hologram silhouettes instead)
- The brand belongs to someone who hasn't authorized it (use "provided reference" language; don't invent trademark logos)
- The user asks for content that violates image-generator terms (nudity, real named public figures in fake scenarios, weapons in schools)

Refer these politely to the appropriate skill or channel.

---

## 22. Quick-start cheat sheet

For fast reference — the minimum viable prompt:

```
Create a [FORMAT: aspect ratio + pixels] [STYLE] visual.

BRAND: "[Exact Name]" — [spelling rule + wrong forms rejected]. Use provided wordmark exactly.

SUBJECT: [character with head + body + pose] OR [interface with N cards + layout]

TEXT ZONES (target language, RTL/LTR):
- "[String 1]" — where, size, color
- "[String 2]" — where, size, color

BACKGROUND: [color gradient + ambient particles + mood]

NEGATIVE:
- NO English (except brand)
- NO wrong brand forms
- NO [other failure modes]

FINAL STYLE: [one-paragraph recap]
```

Adapt every block from §1–§18 as needed. Skip the sections that don't apply to the request.

---

## Notes

- The methodology above was developed through iterative refinement across a full EdTech product line (9 products, multi-lingual, multi-character).
- Each rule earned its place by fixing a specific real-world failure. Don't skip rules that seem redundant — they're load-bearing.
- Update the color palette and font tables per project.
- Keep the negative-rules block generous. It's the most cost-effective section of the entire prompt.
