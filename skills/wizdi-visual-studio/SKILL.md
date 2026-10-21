---
name: wizdi-visual-studio
description: >-
  Unified creative studio for ALL AI-generated visuals — full VIDEO productions and standalone premium IMAGES. Use for (1) any AI video — storyboard, ad, commercial, brand reveal, Reels/TikTok, educational or explainer clip with Flow/Veo, Kling, Seedance, Omni, Runway, Nano Banana, Midjourney, ElevenLabs — interactive HTML storyboard, scene-by-scene image + motion prompts, iterative logo compositing, Hebrew/French voice-over; and (2) premium image prompts (Midjourney, DALL-E, Firefly, Ideogram, Imagen, Stable Diffusion) — product visuals, mascots, dashboard mockups, app icons, branded assets with embedded text: wordmarks, taglines, multilingual/RTL text (Hebrew, Arabic, French) that must not be scrambled. Triggers: storyboard, video ad, pub, publicité, "créer une vidéo", commercial, brand reveal, "סטוריבורד", "סרטון", "פרסומת", "פרומפט", "génère un prompt", image prompt, visual for a product/character/icon/dashboard, or ANY request to plan, prompt, or produce an AI video or branded visual in any language.
---

# Wizdi Visual Studio — AI Video & Premium Image Prompt Methodology

One methodology, two production lines sharing the same core rules:

- **VIDEO LINE** — plan and produce a complete AI-generated video: brief → concept → scene breakdown → interactive HTML storyboard → image prompts → motion prompts → compositing → post-production. Full workflow: `references/video-storyboard.md`
- **IMAGE LINE** — craft a single ultra-detailed prompt for an AI image generator, with embedded text (including RTL scripts), exact brand wordmark preservation, and character family consistency. Full workflow: `references/image-prompts.md`

The prompts and code stay in English because the generators require it. Everything else adapts to the user.

---

## 0. Language protocol

- **Talk to the user in their language** (Hebrew, French, English, Arabic, Spanish…). Detect it from their first message and stick to it.
- **All generator prompts are written in English** — Flow, Kling, Seedance, Nano Banana, Midjourney and ElevenLabs all perform best with English instructions.
- **Text embedded INSIDE a visual stays in the target audience's language, verbatim** — never translate the user's Hebrew tagline into English "for clarity", never inject decorative English words ("SPEED", "AI") into a Hebrew or French visual.

## 1. Route the request

Decide the mode from the user's request, then read the matching reference file before doing any real work:

| Signal | Mode | Read |
|---|---|---|
| Video, ad, commercial, Reels/TikTok, brand reveal, explainer, storyboard, anything with motion or duration | **VIDEO** | `references/video-storyboard.md` |
| One visual, "make me a prompt", mascot, app icon, dashboard mockup, product visual, embedded text/wordmark | **IMAGE** | `references/image-prompts.md` |
| A video whose scenes need branded stills with embedded text | **HYBRID** | Both — drive with the video workflow, build each scene's image prompts with the image methodology |

Ambiguous? Ask one short question ("Video or single visual?") rather than guessing.

## 2. Always start with the intake questionnaire

**Never jump straight to prompts or HTML.** The brief is everything — missing context is the #1 cause of wasted regenerations. Ask in the user's language, wait for complete answers, then confirm the concept before producing anything.

### Video intake (8 questions)

1. **Video type** — social ad (15-30s Reels/TikTok/Stories)? educational/explainer (1-3 min)? brand reveal (5-10s)? talking-head? other?
2. **Target audience** — teachers, parents, religious youth, business, kids, haredi, secular…
3. **Length** — 10s / 20s / 1 min…
4. **Formats** — 9:16 vertical, 1:1 square, 16:9 horizontal, or all?
5. **Voice-over language** — Hebrew / French / English / several?
6. **Existing brand assets** — logo (transparent high-res PNG), brand font, HEX palette, character/actress reference photo, location references, partner logos for end credits?
7. **Core insight / message** — what should the viewer feel or do afterwards?
8. **Special constraints** — religious audience = modesty, kids = safe content, competitor filtering…

### Image intake (6 questions)

1. **Format** — 4:3 / 1:1 / 9:16 / 16:9? What resolution?
2. **Type** — character/mascot? interface/dashboard mockup? app icon? motion frame? product photo? illustration?
3. **Brand** — is a wordmark embedded? Is there a reference image of it to preserve?
4. **Text** — exact strings that must appear, in which language(s)? Any words that must be preserved verbatim (e.g. Hebrew from a marketing doc)?
5. **Family consistency** — one of several products/characters sharing a visual family? What are the constants (head, colors, layout) vs the distinguishing traits?
6. **References** — existing photo, previous visual, color palette to match?

---

## 3. Golden rules — shared core

These rules apply to **every prompt in both modes**. Each one earned its place by fixing a real-world failure; the ones that look redundant are load-bearing.

### 3a. Universal reference language for logos and brands

The generator has no idea what "the Wizdi owl" or "the HASHBACHA logo" is — name it and it will invent its own. Always describe attachments functionally:

> "the brand mark from REFERENCE 2", "the partner logo provided as PNG with transparent background", "the wordmark shown in the attached reference — keep its EXACT shape, do NOT redraw, do NOT stylize"

### 3b. Anti-copyright substitutions

Third-party brand names get prompts blocked (Seedance and Omni filter hard) or produce trademark problems. Substitute generically:

| Brand | Generic substitute |
|---|---|
| iPhone | smartphone |
| AirPods | wireless earbuds |
| Spotify | music streaming app |
| Nike / Lululemon | athletic sportswear / premium athletic wear |
| MacBook | silver laptop |
| Tesla | modern electric car |

Same logic for any brand that isn't the user's own.

### 3c. Exact branding rule (for the user's OWN brand)

When a brand name is embedded, dedicate a full paragraph to how it is written: spell out the exact form ("TWO SEPARATE WORDS with a SPACE, each Title-case"), reference the provided wordmark ("uses the actual provided WORDMARK typography EXACTLY"), and **explicitly reject the wrong forms** (`NOT "WIZCHAT" all caps, NOT "Wizchat" no space, NOT "Wiz-Chat" hyphen`). Acronyms (LMS, SEO, API) stay uppercase even inside a title-case brand.

### 3d. Text integrity (embedded text, all languages)

- Use **only strings the user provided**, verbatim. Never invent taglines.
- Declare direction for RTL scripts: `(RTL, clean modern Hebrew typography, glowing softly)`.
- End the prompt with a **SPELLING CHECK block** listing every non-Latin string verbatim (`- "מחולל הפעילויות" exact, RTL — no flipping, no scrambling`). Required for Hebrew/Arabic, recommended for French/Spanish.
- Call out fragile characters explicitly: gershayim ״ (U+05F4) in Hebrew abbreviations like `חט"ב`, Arabic tashkeel, French accents (é è à ç ï), Spanish ñ.
- Recommend a proven font: Hebrew → Heebo Bold / Frank Ruhl Libre; Arabic → Cairo / Tajawal; Latin premium → Inter / Söhne / Manrope.
- If the generator keeps scrambling, generate WITHOUT the fragile text and have the user composite it in Photoshop/Canva/Figma — a legitimate professional workflow.

### 3e. NEGATIVE rules block — always

Close every prompt with an explicit `NEGATIVE:` / `NEGATIVE RULES (CRITICAL):` block killing the known failure modes: no unwanted text, no invented logos, no watermarks, no wrong brand forms, no scrambled RTL, no sleepy eyes / stiff pose (characters), no checkered fake-transparency (icons). Every negative rule listed is a battle won before generation.

### 3f. Character consistency

AI generates a different face every run. Fix it: create one reference image of the character, define a global `CHAR_DESC` constant (age, hair, eyes, face), attach the reference to every generation (`USE ATTACHED REFERENCE PHOTO for face consistency`; Midjourney: `--cref`). For product families: **same head, different body** — head consistency is critical, the body variant is what distinguishes each family member.

### 3g. Modesty constraint (religious / educational Israeli audiences)

Define once as a global constant and prepend to every image prompt when the audience requires it:

```
MODESTY CONSTRAINT — HIGHEST PRIORITY, NON-NEGOTIABLE:
The subject is dressed in modest attire adapted to the warm Mediterranean climate.
(1) NO cleavage — HIGH round neck / crew neck only, NO V-neck;
(2) NO bare midriff — stomach fully covered;
(3) The clothing CAN be fitted / sporty / chic — but NO sheer fabric, NO low-cut;
(4) NO turtleneck (climate inappropriate);
(5) Modern modest Israeli style — fitted but covered, not frumpy.
```

### 3h. Sensitive-content filter workarounds

Some safe combinations trip safety filters. Rephrase preemptively:

- "teacher + classroom + children" → "young woman in warm room with small seated figures in soft bokeh" (Omni child-safety filter)
- "nightclub + young woman + alcohol" → "music event with mixing booth"
- "smoke + haze + dark" → "warm atmosphere with gentle light"

Never depict photorealistic minors in education visuals — use hologram silhouettes instead.

### 3i. Prompt length limits

Seedance: **4000 characters max**. Kling: ~2500. Flow/Veo: flexible. Trim before delivering if over.

### 3j. Palette continuity

Scenes of a video — and products of a family — must feel like one world. Use the previous scene's last frame as a palette reference for the next; match backgrounds to the product's brand color.

### 3k. Real logos belong in post-production

AI cannot reproduce an exact logo. Ever. The professional workflow (Universal, A24, Marvel): AI generates the cinematic atmosphere, the real logo is added in After Effects / CapCut. If the user insists on all-AI, use the **iterative compositing workflow** (`references/video-storyboard.md`, step 6) — one logo per step, each with an exact image reference.

---

## 4. Delivery format

- **Every prompt goes in a fenced code block**, ready to paste — never in loose prose.
- Image mode: announce what you deliver (`Prompt A — main visual 4:3`, `Prompt B — app icon 1:1`), list the non-Latin strings separately below the block (for manual compositing if needed), and offer validation: "Validate this and I'll move to the next one with the same methodology."
- Video mode: the main deliverable is the **interactive HTML storyboard file** (see reference). Building it requires file-creation tools — available in Cowork. If you are in a plain chat without file tools, say so in the user's language and deliver the storyboard scene-by-scene in chat instead.

## 5. Iteration protocol

When a generation fails: ask what went wrong (with the failed image if possible), identify the failure mode, **rewrite the FULL prompt** — never say "add these lines to the previous prompt" — and add a new negative rule targeting that specific failure. If it's RTL scrambling, fall back to compositing the text manually.

## 6. When to say no

Refuse or redirect: photorealistic minors in compromising contexts (use holograms/silhouettes), brands the user doesn't own (use "provided reference" language, never invent trademark logos), content violating generator terms (nudity, real named public figures in fake scenarios, weapons in schools).

---

## Tool stack

| Stage | Tools (preference order) |
|---|---|
| Images | Nano Banana (best for multi-reference compositing) · Flow/Veo (cinematic) · Midjourney (aesthetics, less control) · Stable Diffusion/Recraft (max control) |
| Video | Kling 2.0 (faithful to input image) · Seedance (fast, harsh brand filter) · Omni (harsh child filter) · Runway Gen-3 (high-end) · Flow/Veo (cinematic) |
| Audio | ElevenLabs (Hebrew VO — warm voices: Bella, Rachel) · Epidemic Sound / Artlist (music) |
| Edit | CapCut (free, great for Reels) · DaVinci Resolve (pro, free) · Premiere (industry) · After Effects (logo overlays, motion graphics) |

---

## Quick flow summary

```
1. Detect language + route (VIDEO / IMAGE / HYBRID) → read the matching reference file
2. Intake questionnaire → wait for answers
3. VIDEO: concept → scene breakdown → HTML storyboard → per-scene image + motion prompts
   IMAGE: build the 12-block prompt (format → style → branding → subject → text zones →
   background → mood → composition → spelling check → negatives → final style)
4. Apply golden rules everywhere: reference language, anti-copyright, text integrity,
   NEGATIVE block, CHAR_DESC, modesty, filter workarounds, length limits
5. Deliver in fenced code blocks → user generates → iterate with full rewrites
6. VIDEO: compositing for logo scenes → post-production (edit, VO, music, captions)
```

---

## Changelog

- **v2.0** — Merger of `video-ai-storyboard-il` (v1.0) and `premium-visual-prompts` into one unified skill: shared golden rules extracted, adaptive language protocol, two reference files (video / image).
