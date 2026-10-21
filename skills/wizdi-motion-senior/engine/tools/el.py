# -*- coding: utf-8 -*-
"""ElevenLabs (FACULTATIF, payant) : voix off horodatée, transcription, musique, bruitages, isolation de la voix.
La clé se lit UNIQUEMENT dans la variable d'environnement ELEVENLABS_API_KEY ; elle n'est jamais affichée ni écrite.
  Windows (PowerShell) : $env:ELEVENLABS_API_KEY = "…"      (ou setx ELEVENLABS_API_KEY "…" puis nouveau terminal)
  macOS (zsh)          : export ELEVENLABS_API_KEY="…"      (dans ~/.zshrc pour la garder)
Sans clé, le moteur marche quand même : musique et bruitages synthétisés (synth.py), voix fournie en fichier.
Ne génère RIEN avant validation des textes (Yoni, puis Liad) : ces appels coûtent des crédits.

  python tools/el.py tts --script vo-script.json [--take 1] [--seed 11]   # voix + instants de chaque caractère -> vo/
  python tools/el.py stt vo/voice.wav [--lang heb] [--out vo/stt.json]     # Scribe : mots horodatés d'une voix enregistrée
  python tools/el.py music "<prompt anglais>" --secs 40 --out build/el/music-a.mp3   # toujours instrumentale
  python tools/el.py sfx "<prompt anglais>" --secs 0.6 --out build/el/pop.mp3 [--influence 0.6]
  python tools/el.py isolate rush.wav --out vo/voice-iso.wav               # Voice Isolator (≥ 4,6 s : complété de silence)

vo-script.json : { "voice": "<voice_id>", "model": "eleven_v4", "language": "he",
                   "settings": { "stability": 0.5, "similarity_boost": 0.75, "speed": 1.0 },
                   "lines": { "s1": { "text": "<l'écran, VERBATIM>", "say": "<ce que lit la voix : Wiz Play, nikoud ciblé…>" }, … } }
Un fichier déjà généré (même --out) n'est pas refait. Registre des dépenses : build/el-ledger.jsonl."""
import argparse, base64, json, os, subprocess, sys, time, urllib.error, urllib.request, uuid

API = "https://api.elevenlabs.io"
sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")


def key():
    k = os.environ.get("ELEVENLABS_API_KEY", "").strip()
    if not k:
        raise SystemExit("ELEVENLABS_API_KEY absente de l'environnement (voir l'en-tête de tools/el.py). "
                         "Sans clé : musique/bruitages synthétisés et voix fournie en fichier.")
    return k


def request(path, body=None, files=None, fields=None, timeout=400):
    """POST -> (statut, en-têtes, octets). Réessaie sur 429/5xx."""
    h = {"xi-api-key": key()}
    if files:
        bd = uuid.uuid4().hex; parts = []
        for k, v in (fields or {}).items():
            parts.append(f'--{bd}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{v}\r\n'.encode())
        for k, (fn, blob, ct) in files.items():
            parts.append(f'--{bd}\r\nContent-Disposition: form-data; name="{k}"; filename="{fn}"\r\nContent-Type: {ct}\r\n\r\n'.encode() + blob + b"\r\n")
        data = b"".join(parts) + f"--{bd}--\r\n".encode(); h["Content-Type"] = f"multipart/form-data; boundary={bd}"
    else:
        data = json.dumps(body or {}).encode(); h["Content-Type"] = "application/json"
    for attempt in range(3):
        req = urllib.request.Request(API + path, data=data, headers=h, method="POST")
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.status, dict(r.headers), r.read()
        except urllib.error.HTTPError as e:
            msg = e.read().decode("utf-8", "replace")[:400]
            if e.code in (429, 500, 502, 503) and attempt < 2:
                time.sleep(8 * (attempt + 1)); continue
            raise SystemExit(f"ElevenLabs {e.code} : {msg}")


def ledger(kind, out, secs=None, cost=None, note=""):
    p = os.path.join("build", "el-ledger.jsonl"); os.makedirs("build", exist_ok=True)
    with open(p, "a", encoding="utf-8") as fh:
        fh.write(json.dumps({"t": time.strftime("%Y-%m-%d %H:%M:%S"), "kind": kind, "out": out, "secs": secs, "cost": cost, "note": note[:200]},
                            ensure_ascii=False) + "\n")


def stt(path, lang="heb"):
    """Scribe : renvoie le JSON (text, words[{text, start, end, type}])."""
    blob = open(path, "rb").read()
    code, _, raw = request("/v1/speech-to-text", files={"file": (os.path.basename(path), blob, "audio/wav")},
                           fields={"model_id": "scribe_v1", "language_code": lang, "timestamps_granularity": "word"})
    return json.loads(raw.decode("utf-8"))


def cmd_tts(a):
    sc = json.load(open(a.script, encoding="utf-8"))
    text = " ".join(l["say"] for l in sc["lines"].values())
    os.makedirs(a.out_dir, exist_ok=True)
    mp3 = os.path.join(a.out_dir, f"take{a.take}.mp3")
    if os.path.exists(mp3):
        print("déjà là ->", mp3)
    else:
        body = {"text": text, "model_id": sc.get("model", "eleven_v4"), "voice_settings": sc.get("settings", {})}
        if sc.get("language"):
            body["language_code"] = sc["language"]
        if a.seed is not None:
            body["seed"] = a.seed
        _, hdr, raw = request(f"/v1/text-to-speech/{sc['voice']}/with-timestamps?output_format=mp3_44100_192", body)
        res = json.loads(raw.decode("utf-8"))
        open(mp3, "wb").write(base64.b64decode(res["audio_base64"]))
        json.dump({"text": text, "alignment": res.get("alignment"), "seed": a.seed, "voice": sc["voice"]},
                  open(os.path.join(a.out_dir, f"take{a.take}.json"), "w", encoding="utf-8"), ensure_ascii=False)
        ledger("tts", mp3, cost=hdr.get("character-cost"), note=f"{len(text)} caractères")
        print(f"ok -> {mp3} ({len(text)} caractères, coût annoncé {hdr.get('character-cost')})")
    wav = os.path.join(a.out_dir, "narration.wav")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", mp3, "-ac", "1", "-ar", "48000", wav], check=True)
    print(f"ok -> {wav}\nensuite : python tools/words.py --script {a.script} --timing {os.path.join(a.out_dir, f'take{a.take}.json')}")


def cmd_stt(a):
    out = a.out or os.path.splitext(a.audio)[0] + "-stt.json"
    res = stt(a.audio, a.lang)
    json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ledger("stt", out)
    print("ok ->", out, ":", res.get("text", "")[:200])


def cmd_music(a):
    if os.path.exists(a.out):
        print("déjà là ->", a.out); return
    secs = max(10, min(300, a.secs or 30))
    prompt = a.prompt.strip()
    if "no vocals" not in prompt.lower():
        prompt += ". Instrumental only, no vocals, no singing, no spoken words."
    _, hdr, raw = request("/v1/music", {"prompt": prompt, "music_length_ms": int(secs * 1000)})
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); open(a.out, "wb").write(raw)
    ledger("music", a.out, secs, hdr.get("character-cost"), a.prompt)
    print(f"ok -> {a.out} (musique {secs:.0f} s)")


def cmd_sfx(a):
    if os.path.exists(a.out):
        print("déjà là ->", a.out); return
    secs = max(0.5, min(22, a.secs or 1.0))
    body = {"text": a.prompt, "duration_seconds": secs}
    if a.influence is not None:
        body["prompt_influence"] = a.influence
    _, hdr, raw = request("/v1/sound-generation", body)
    os.makedirs(os.path.dirname(os.path.abspath(a.out)), exist_ok=True); open(a.out, "wb").write(raw)
    ledger("sfx", a.out, secs, hdr.get("character-cost"), a.prompt)
    print(f"ok -> {a.out} (bruitage {secs:.1f} s, coût annoncé {hdr.get('character-cost')})")


def cmd_isolate(a):
    src = a.audio
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", src],
                               capture_output=True, text=True).stdout.strip() or 0)
    tmp = a.out + ".in.wav"
    pad = ["-af", f"apad=whole_dur={max(4.8, dur)}"] if dur < 4.8 else []
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, *pad, "-ac", "1", "-ar", "44100", tmp], check=True)
    _, _, raw = request("/v1/audio-isolation", files={"audio": ("in.wav", open(tmp, "rb").read(), "audio/wav")})
    os.remove(tmp)
    iso = a.out + ".iso"
    open(iso, "wb").write(raw)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", iso, "-t", f"{dur:.3f}", "-ac", "1", "-ar", "48000", a.out], check=True)
    os.remove(iso)
    ledger("isolate", a.out, dur)
    print("ok ->", a.out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("tts"); s.add_argument("--script", default="vo-script.json"); s.add_argument("--take", default="1")
    s.add_argument("--seed", type=int, default=None); s.add_argument("--out-dir", default="vo")
    s = sub.add_parser("stt"); s.add_argument("audio"); s.add_argument("--lang", default="heb"); s.add_argument("--out", default=None)
    s = sub.add_parser("music"); s.add_argument("prompt"); s.add_argument("--secs", type=float, default=30); s.add_argument("--out", required=True)
    s = sub.add_parser("sfx"); s.add_argument("prompt"); s.add_argument("--secs", type=float, default=1.0); s.add_argument("--out", required=True)
    s.add_argument("--influence", type=float, default=None)
    s = sub.add_parser("isolate"); s.add_argument("audio"); s.add_argument("--out", required=True)
    a = ap.parse_args()
    {"tts": cmd_tts, "stt": cmd_stt, "music": cmd_music, "sfx": cmd_sfx, "isolate": cmd_isolate}[a.cmd](a)


if __name__ == "__main__":
    main()
