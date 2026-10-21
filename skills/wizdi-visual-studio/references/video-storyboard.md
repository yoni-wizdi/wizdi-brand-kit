# VIDEO LINE — Full Storyboard Methodology (7 Steps)

Complete workflow for planning and producing an AI-generated video. The golden rules from SKILL.md (reference language, anti-copyright, modesty, NEGATIVE blocks, CHAR_DESC, filter workarounds, length limits) apply to every prompt below.

The intake questionnaire (SKILL.md §2, video version) must be answered before starting step 1.

---

## Step 1 — Brief & concept

From the questionnaire answers, formulate:

- **Core concept** in one sentence (e.g. "The teacher listens to her playlist in every daily situation — and in class too, teaching is a playlist")
- **Emotional arc** (scene 1 = energetic opening → scene 4 = conflict → scene 6 = resolution → scene 7 = CTA)
- **Tone** (warm / light / professional / funny / technical)
- **Cinematic references** (which ads/films carry the desired vibe)

**Present the concept to the user for approval before continuing.**

## Step 2 — Scene breakdown

Rules per scene:

- Each scene = 2-5 seconds (Reels) or 3-8 seconds (longer videos)
- Each scene needs a **clear purpose** (what the viewer should feel at that moment)
- Each scene needs a **transition** (hard cut, fade, push-in…) to the next

Standard structure for a 20-25s ad:

| # | Scene | Duration | Role |
|---|---|---|---|
| 1 | Opening / hook | 3s | Grab attention |
| 2 | Conflict / problem | 4s | "I know what you mean" |
| 3 | Escalation | 4s | "It really is frustrating" |
| 4 | Solution intro | 3s | "But there's a fix!" |
| 5 | Solution in action | 5s | "And it works great" |
| 6 | Emotional payoff | 3s | "How I feel now" |
| 7 | CTA + brand | 4s | "Try it too!" |

**Present the breakdown to the user for approval before writing any prompts.**

## Step 3 — Build the interactive HTML storyboard

**The HTML file is the main deliverable.** It lets the user navigate all scenes (sidebar), copy prompts in one click, upload generated images/videos (drag & drop), mark scenes done/collapsed, and track global progress.

### Scene data model (JS)

```javascript
const SCENES = [
  {
    n: 1,                                    // scene number
    time: "0:00 – 0:03",                     // timecode
    titre: "Short scene title",
    objectif: "What the viewer should feel here",
    visuel: "Visual description in the user's language",
    duration: "3s",
    tenue: "Wardrobe description for the character",
    device: "Smartphone / laptop / etc.",
    mood: "Energy / calm / strong",
    motionType: "i2v",                       // "i2v" or "f2f"
    imagePrompt: `English prompt for the image tool…`,
    motionPrompt: `English prompt for the video tool…`,
    voTextHe: "Voice-over text in the VO language",
    voTimingNote: "Timing notes",
    voiceoverFr: "Translation of the VO for reference",
    f916: "Framing description for 9:16",
    f11: "Framing description for 1:1",
    f169: "Framing description for 16:9",
    transition: "Transition instruction to next scene",
    bShot: { }                               // optional: complementary take
  }
];
```

### Two motion types

- **`i2v`** (image-to-video) — one image + one motion prompt → 2-5s clip. The standard.
- **`f2f`** (frame-to-frame) — START image + END image + interpolation prompt. For scenes with a significant state change. Extra fields:

```javascript
{
  motionType: "f2f",
  imagePromptStart: `Prompt for the start frame…`,
  imagePromptEnd: `Prompt for the end frame…`,
  motionPrompt: `Interpolation prompt…`,
}
```

### Required HTML components

1. CSS palette via CSS variables (color consistency)
2. Sidebar navigation with per-scene state in `localStorage`
3. Hero section with title + meta
4. Recap table of all scenes
5. Dynamic rendering of the `SCENES` array
6. Upload component storing user files in IndexedDB
7. "Copy" button per prompt
8. Lightbox preview
9. Stats banner with progress

### Full SCENE template (copy-adapt)

```javascript
const SCENE_TEMPLATE = {
  n: 1,
  time: "0:00 – 0:03",
  titre: "Opening — energetic hook",
  objectif: "Grab attention in the first 0.5s",
  visuel: "Description in the user's language of what happens",
  duration: "3s",
  tenue: "High crew neck, no exposure",
  device: "smartphone",
  mood: "High energy",
  motionType: "i2v",
  imagePrompt: `${MODESTY_PRIORITY}Cinematic editorial photograph of ${CHAR_DESC} on the Tel Aviv Tayelet at sunrise. [ACTION]. [WARDROBE]. [LANDMARKS]. Lighting: golden hour. Color grade: warm Mediterranean. Hyperrealistic, 8K. NEGATIVE: no readable text, no logos, no watermarks.`,
  motionPrompt: `3-second shot. CAMERA: smooth push-in 4%. TIMING BEATS: at 0.0-1.0s [action]; at 1.0-2.0s [action]; at 2.0-3.0s [resolution]. LAYER — HAIR: dynamic motion. LAYER — LIGHT: golden rim. MOOD: empowered active lifestyle.`,
  voTextHe: "Short VO text",
  voTimingNote: "Start at 0.5s, end by 2.8s",
  voiceoverFr: "Translation of VO for reference",
  f916: "Format Reels — face high, action center, ground low",
  f11: "Crop tight on action triangle",
  f169: "Wide composition, action center",
  transition: "Hard cut to scene 2"
};
```

## Step 4 — Image prompts (stills)

Recommended tools, in order: **Nano Banana** (multi-reference compositing, relatively faithful to logos), **Flow/Veo** (cinematic quality, image + video), **Midjourney** (great aesthetics, less reference control).

Structure of every image prompt:

1. **Style opener** ("Cinematic editorial photograph", "Hyperrealistic", "8K")
2. **Character** via the global `CHAR_DESC` constant (cross-scene consistency) + attached reference photo
3. **Environment with SPECIFIC landmarks** (not "city" — "Tel Aviv Tayelet wave-pattern tiles")
4. **Action** — what the character does at this exact moment
5. **Lighting** (golden hour / cathedral light / soft window light)
6. **Composition** (rule of thirds, framing)
7. **Color grade** (Mediterranean cinematic / A24 / Roger Deakins style)
8. **`NEGATIVE:`** closer — no text, no logos, no readable signs, no watermarks

Minimal valid example:

```
[MODESTY_PRIORITY constant] Cinematic editorial three-quarter front-angle photograph of a [CHAR_DESC], captured at sunrise golden hour on the Tel Aviv Tayelet (the iconic Mediterranean beach promenade with wave-pattern tiles and modern beachfront hotels). She is [ACTION DESCRIPTION]. She wears [WARDROBE]. Setting: [SPECIFIC LANDMARKS]. Lighting: golden hour rim light. Shot on cinema camera with anamorphic 35mm lens at T2.8. Color grade: warm Mediterranean cinematic. Composition: rule of thirds. Style: aspirational lifestyle. Hyperrealistic, 8K. NEGATIVE: no readable text, no logos, no watermarks.
```

If a scene's still needs embedded brand text, taglines or UI elements, build that image prompt with the IMAGE LINE methodology (`references/image-prompts.md`) — 12-block structure, spelling check, branding rule.

## Step 5 — Motion prompts (video)

Recommended tools: **Kling 2.0** (faithful to input image), **Seedance** (fast; harsh anti-copyright filter), **Omni** (harsh child-content filter), **Runway Gen-3** (high-end), **Flow/Veo** (complex cinematic scenes).

Structure of every motion prompt:

1. **CAMERA:** movement (locked / push-in / pan / orbit)
2. **PACING:** rhythm (energetic / calm / cinematic crescendo)
3. **TIMING BEATS:** precise beats (`at 0.0-0.7s — action A; at 0.7-1.3s — action B…`)
4. **LAYER — X:** separate elements (LAYER — HAIR, LAYER — SCREEN, LAYER — LIGHT)
5. **SOUND DESIGN:** note for the editor
6. **MOOD:** what the viewer should feel
7. **NEGATIVE:** what NOT to do

Hard limits: Seedance **4000 chars**, Kling ~2500. Omni: never combine "teacher + children + classroom" — write "young woman", "small seated figures", "warm room". No third-party brand names anywhere (see SKILL.md §3b).

## Step 6 — Iterative compositing (brand reveal / CTA scenes)

The problem: AI tools don't know your logo and will invent one. The solution: build the scene step by step — **one logo per step, each with an exact image reference, in universal language** ("the brand mark from REFERENCE 2").

```javascript
{
  motionType: "f2f",
  compositingSteps: [
    {
      badge: "1A",
      label: "Atmosphere base (empty, no logos)",
      color: "#1565C0",
      refs: [
        { priority: 'optional', label: 'Optional inspiration references' }
      ],
      prompt: `Generate a cinematic background — VERTICAL 9:16. Empty composition with empty center and empty bottom third for later compositing. [...] NEGATIVE: NO text, NO logo, NO bird, NO people.`
    },
    {
      badge: "1B",
      label: "Add the central logo",
      color: "#B8336A",
      refs: [
        { priority: 'max', label: 'REFERENCE 1 = image generated in step 1A' },
        { priority: 'max', label: 'REFERENCE 2 = your logo as transparent PNG' }
      ],
      prompt: `COMPOSITING TASK: take REFERENCE 1 (background) and integrate into its CENTER the brand mark shown in REFERENCE 2. KEEP THE EXACT SHAPE of REFERENCE 2 — do NOT redraw, do NOT stylize. Apply cinematic lighting integration. KEEP THE BACKGROUND EXACTLY AS REFERENCE 1. [...]`
    },
    {
      badge: "1C",
      label: "Add the wordmark below",
      refs: [ /* … */ ],
      prompt: `COMPOSITING TASK: take REFERENCE 1 (previous result with central logo) and add the wordmark from REFERENCE 2 below the central logo. [...]`
    },
    {
      badge: "1D",
      label: "Add partner logo 1 (bottom left)"
      /* … */
    },
    {
      badge: "1E",
      label: "Add partner logo 2 (bottom right) — FINAL FRAME"
      /* … */
    }
  ],
  motionPrompt: `5-second f2f interpolation. START FRAME = result of step 1A (empty atmosphere). END FRAME = result of step 1E (fully composited final). The animation interpolates from empty to full composited reveal.`
}
```

Best tool for compositing steps: **Nano Banana** (multi-reference input). Remember: the professional default is still adding real logos in post-production (After Effects / CapCut) — compositing is the all-AI fallback.

## Step 7 — Final edit & production

Once all clips exist:

1. **CapCut / DaVinci Resolve / Premiere** — assembly + audio edit
2. **ElevenLabs** — VO (Hebrew: warm voice, usually female — "smile in the voice")
3. **Music** — Epidemic Sound / Artlist
4. **Captions** — subtitles in the VO language (optional for Stories/YouTube)
5. **Color grading** — fix palette inconsistencies between scenes

Post-production is where you fix: palette mismatches between scenes, real logo overlay on generic footage, audio-visual sync, smooth transitions. Then export per format (9:16 / 1:1 / 16:9).

---

## Common mistakes to avoid

### JavaScript issues in the HTML

1. **Duplicate keys in a scene object** → silent SyntaxError that kills the whole render. Never two `motionPrompt:` in the same object.
2. **motionType/field mismatch** → `motionType: "f2f"` without `imagePromptStart`/`imagePromptEnd` renders `undefined`.
3. **Duplicated SCENES or bad edits** → always keep a backup before a big change.

### File sync

When mixing Claude file tools and shell writes, always write through the same side — Windows/Linux sandbox sync can break.

### Prompt issues

1. **Too generic** ("a woman in a city") → weak output. Be specific.
2. **Missing NEGATIVE** → random text/logos appear. Always add it.
3. **Missing face reference** → different face every scene. Always attach the reference.
4. **Third-party brand names** → anti-copyright filter blocks. Use substitutes.
5. **Sensitive combos** (children + classroom + teacher) → safety filter blocks. Simplify per SKILL.md §3h.
