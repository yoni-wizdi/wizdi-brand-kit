# Prompt recipes for avatar & B-roll scenes

Prompts are always in **English** (models perform best in English), even when the conversation and the
narration are in another language. Write rich, cinematic, engine-agnostic prompts — no tool-specific
jargon — so the same prompt works on Omni, Flow/Veo, Kling or Seedance.

Every prompt should cover, in order: **subject/character + exact action → environment → camera angle +
movement → lighting + style → mood → aspect ratio**. For avatar scenes, add the **identity lock** and
the **forced narration language** at the end.

## Avatar scene (the character speaks — lip-sync)
Anchor on the locked reference image so the face never drifts:

> Animate the provided reference image of [CHARACTER] — [1-line design recap: colors, key features].
> Keep the EXACT same identity, proportions and colors as the reference, no drift. [Rich action +
> expression]. Environment: [setting]. Camera: [angle + movement]. Style: [rich style — see vocab].
> [Mood]. [ASPECT, e.g. 16:9 widescreen / 9:16 vertical]. He/She speaks in [LANGUAGE] ONLY, do not
> translate; he/she says exactly: '[NARRATION LINE]'.

Put the spoken line in the tool's dialogue field **and** inside the prompt, and always keep the
"speak in [LANGUAGE] ONLY, do not translate" clause — otherwise the model may dub it into English.

## B-roll scene (no character on screen — voice-over)
Use only when the character can't plausibly be in the shot (e.g. a crowd reacting). Generate without
lip-sync; the avatar's voice is laid over it in edit:

> A cinematic [style] shot, [ASPECT], [grade + light]. [Scene with ONE clear motion]. Camera:
> [movement]. No on-screen text. (Character VOICE-OVER narrates in [LANGUAGE] over this shot, do not
> translate: '[NARRATION LINE]'.)

## Style & camera vocabulary (mix to taste)
- **Style:** cinematic high-end stylized 3D animation (Pixar/Illumination quality), warm/cool color
  grade, soft volumetric light, god-rays, subtle bokeh, shallow depth of field, detailed texture.
- **Camera:** slow push-in, gentle pull-back, slow orbit, tracking shot, low/high angle, close-up,
  medium shot, wide establishing shot, intimate two-shot, slight handheld drift.
- **Mood:** warm & inviting, playful, awe/wonder, tender, triumphant, hushed, uplifting.

## Filters & fallbacks
- If a generation is blocked, **reword to get around it** — never "kid/child/children", use
  "character" or "young student"; drop real brand names; describe positively. Keep the intent, change
  the words.
- Primary: **Nano Banana** (images), **Omni** (video). Fallbacks if a shot won't render well: **Kling**,
  **Seedance**, **GPT image** — rework the same idea for the other engine.
- **If a scene fails 3–4 times, STOP tweaking words and change the approach:** simpler motion, let the
  avatar do it on camera, reference-then-animate, frame-to-frame (start + end frame), or a still image
  with a slow zoom added in edit. Don't keep re-rolling the same prompt.

## Aspect ratio
Use the format chosen in Step 4 in every prompt: `16:9 widescreen` (horizontal / TV / PC) or
`9:16 vertical` (mobile). Compose framing for that shape — vertical wants tighter, taller framing.
