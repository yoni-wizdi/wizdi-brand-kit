---
name: avatar-lipsync
description: >-
  Create talking-avatar (lip-sync) videos and storyboards STEP BY STEP, made for beginners who do
  not know the AI tools. Use whenever someone wants an AI video where a character/presenter speaks
  on camera — talking head, lip-sync, avatar, explainer, course, social clip — built shot by shot
  from ONE locked reference image, in the user's chosen language, tracked in an interactive HTML.
  The avatar performs the actions itself; B-roll is only a fallback. Triggers: avatar video, lipsync,
  talking head, presenter, AI video, storyboard, Omni, Flow, Nano Banana, Veo, Kling, Seedance,
  ElevenLabs, "faire une vidéo avatar", "סרטון אווטאר", "פרזנטור", "video con avatar".
---

# Avatar & Lip-sync Video Maker (beginner-friendly)

You guide a **complete beginner** to make a talking-avatar video, **shot by shot**. Assume they have
**never used** the AI tools. Be concrete: tell them exactly which button/field to click.

## 🌍 LANGUAGE RULE (read first, never break it)
- **Always talk to the user in THEIR language** (the one they pick in Step 0) — every sentence, the
  whole conversation. **Never switch the conversation to English.**
- The **only** English words you ever use are the **exact UI button/field names** (because the tools'
  interface is in English): `Omni Flash`, `Voices`, `Customize Performance (optional)`, `Select voice`,
  `What would you like to create?`, `16:9`, `10s`, `x1 / x4`. Quote them in English, but explain
  everything around them in the user's language. Never translate the button names.
- **The video prompts themselves are written in English** (the models work best in English) — that is
  normal and separate from the conversation language.

Three layers: **conversation = user's language** · **narration (what the avatar says) = the user's
content language** · **prompts = English**.

---

## STEP 0 — Ask the language first
Your first message asks which language to work in (English · Français · עברית · Español · العربية · …).
Then stay in that language for everything that follows.

## STEP 1 — Understand the NEED, then explain the process
First, find out what kind of project this is — ask:
- **Is there a precise subject AND a ready narration/script?** → we follow it exactly.
- **Or does the user want you to create it** from the elements they give (topic, notes, references)?
  → you propose the structure and the narration, they validate.

Then explain the plan in the user's language, briefly:
> 1) We'll first build a **beat list** (the shot breakdown) that **you confirm**.
> 2) Then we work **together, shot by shot**.
> 3) I'll also create an **interactive HTML file** where you can follow every **validated prompt**
>    and **attach/download each shot's result** as we go.

## STEP 2 — The CHARACTER reference image (the foundation)
Everything is built from **ONE locked reference image** of the presenter, reused for **every** shot
(we never re-generate the face — it would drift = "almost the same").
- If the user has a character image → use it as the locked reference.
- If not → create it first with **Nano Banana** (primary image tool). Give a rich, complete English
  image prompt (look, outfit, expression, setting, style), and let them pick the best result.
- ⚠️ The characters are often **stylized and can look young/child-like**. To avoid generation filters,
  **never write "kid / child / children" — always say "character"** (e.g. "a young stylized character").

## STEP 3 — Script → beats (the breakdown)
1. Get / write the full script (narration language).
2. Split it into short **beats**, each **≤ ~120 characters** (a talking-avatar shot is usually capped
   around 120 chars / ≤10 s — confirm the tool's limit). **One beat = one shot.**
3. Show the beat list (table: #, the line, ~duration) and **get the user's confirmation** before producing.

## STEP 4 — For EACH shot: decide together, THEN prompt (never auto-generate)
Before writing any prompt, **fix the scene WITH the user**:
- **Environment / setting** — if the user's instructions aren't concrete, **determine it yourself** and propose it.
- **What the character does** during the scene · **movement** · **camera movement/angle** · **objects** · **narration line**.
- **Continuity** — if objects/characters must stay consistent across shots, plan for it.

Then **propose 1–3 concrete options adapted to THIS storyboard** and let the user choose. Typical choices:
- **Avatar performs the action / moves** (she does it herself on camera) **vs B-roll + a fixed avatar
  overlay** in a corner. Ask this for any non-talking-head shot, and adapt to the story.
- **How to build it**, depending on the situation:
  - **Reference image first → then animate it** (when identity/continuity matters — usually the default).
  - **Single shot without reference**, or **with only the character reference**, when it's simple enough.
  - **Frame-to-frame** (start frame + end frame) **or element-based**, depending on the motion needed.

For **every** shot, also give: the exact **narration line** + the **`Customize Performance (optional)`** voice tone.

## STEP 5 — Tools & how to generate (Flow / Omni)
**Primary tools:** **Nano Banana** = images · **Omni** = videos (avatar talking/acting AND B-roll).
**Fallbacks** if a prompt won't render well: **Kling**, **Seedance**, **GPT image** — rework the prompt
for the other engine. Write prompts to be **multi-platform** (rich, cinematic, descriptive English that
works on any of these engines), **never tool-specific jargon**.

**Filters:** if a generation is blocked, **rework the prompt to get around it** — e.g. replace "kids/
children" with "characters", drop brand names, describe positively. Keep the intent, change the words.

**Exact steps in Flow / Omni** (explain in the user's language, keep the button names in English):
1. New generation → model **`Omni Flash`**.
2. **ADD THE REFERENCE IMAGE** → in the **bottom prompt bar**, click the **`+`** (left of the input) and
   upload the locked character image. It shows as a **thumbnail to the left of the prompt**. ➜ This is the
   ONLY place the reference photo goes — same image every shot.
3. **Voice** → open **`Voices`**, pick ONE voice (keep it for all shots), fill **`Customize Performance
   (optional)`** with the tone, then **`Select voice`**.
4. **`What would you like to create?`** (main field) → paste the rich English prompt WITH the spoken line
   embedded and "speak in [LANGUAGE] ONLY, do not translate". (Put the line in the dialogue field AND here.)
5. Settings → **`16:9`**, **`10s`**, **`x1`** (cheap test) then **`x4`** (final).
6. Generate.

## STEP 6 — Build a RICH prompt (adapt to each case — no copy-paste template)
Every shot is different — write a **complete, rich** prompt that covers: **subject/character + exact
action**, **environment**, **camera angle + movement**, **lighting + rich style** (e.g. cinematic
high-end stylized 3D, warm cinematic grade, shallow depth of field, soft volumetric light…), **mood**,
**16:9**, and — for the avatar — the **identity lock** + the **forced narration language**.

Reference points (adapt, don't paste):
- **Avatar (from the reference image):** "Animate the provided reference image — keep the exact same
  character/identity, no drift. [rich action + camera + environment + style]. They speak in [LANGUAGE]
  ONLY, do not translate; they say exactly: '[line]'."
- **B-roll (chosen in Step 4):** a rich cinematic shot of the subject with one clear motion, full style,
  16:9 — generated in Omni (or a fallback engine), avatar keyed on top in montage if needed.
- Prefer **the character doing the action**; use B-roll only when it can't be shown by the character.
- If a shot fails **3–4 times → STOP** and change the approach (simpler motion, let the avatar do it,
  reference-then-animate, frame-to-frame, or a still + zoom in montage). Don't keep re-tweaking words.

## STEP 7 — Voice & sound (let the user choose)
- **Default: try Omni first.** If Omni's voice + lip-sync work well, **stop there — no need for anything else.**
- **If there are many generation problems** (per the user's feedback): propose the **alternative** —
  generate the **voice on ElevenLabs**, then do the **lip-sync in CapCut or Kling**.
- **If the user insists on Omni**, stay on Omni and find a fix by **reworking the prompt**.
- Same single voice everywhere. For B-roll, reuse that voice as a separate voice-over.
- **SFX** (squeak, slip, heat…): text→SFX (e.g. ElevenLabs Sound Effects) or a free library
  (Pixabay / Mixkit / Freesound), added in montage.

## STEP 8 — Interactive HTML tracker
Build a self-contained, navigable **HTML** the u