# -*- coding: utf-8 -*-
"""Mots de l'écran (VERBATIM) calés sur la voix -> words.js (window.WIZ_WORDS). La narration d'abord : texte validé ->
voix -> instants des mots ; l'image et le son se calent dessus.

  python tools/words.py --script vo-script.json --timing vo/take1.json [--out words.js]

--timing accepte :
  - la sortie de `el.py tts` (vo/take1.json : { text, alignment: { characters, character_start_times_seconds, … } }) ;
  - la sortie de `el.py stt` (Scribe : { words: [{ text, start, end, type }] }) — voix enregistrée, actrice, tutoriel ;
  - un calage manuel : { "s1": [{ "w": "…", "t": 0.10, "e": 0.62 }, …], … } (mots DITS, instants en secondes).
vo-script.json : lines.<clé>.text = l'écran mot pour mot (ponctuation comprise) ; .say = ce que lit la voix ; .hide = [indices]
des mots à NE PAS afficher (douteux) -> x: true. Les tirets « – » et points médians « · » de l'écran ne sont pas des mots :
ils marquent un saut de groupe (br: true). Mots non retrouvés dans la voix : instants interpolés et signalés (guess) —
à vérifier à l'oreille avant de livrer."""
import argparse, json, re, sys, unicodedata

sys.stdout.reconfigure(encoding="utf-8"); sys.stderr.reconfigure(encoding="utf-8")
NIK = re.compile(r"[֑-ׇ]")
SPOKEN = {"2": ["שתיים"], "3": ["שלוש"], "4": ["ארבעה"], "5": ["חמש"], "24/7": ["עשרים", "וארבע", "שבע"]}


def norm(w):
    """Normalise pour comparer écran et voix : sans nikoud ni ponctuation ; ו/י hors 1re lettre ignorés (כתיב מלא/חסר)."""
    w = NIK.sub("", unicodedata.normalize("NFC", w))
    w = re.sub(r"[^\wא-ת/]", "", w).lower()
    return w[:1] + re.sub("[וי]", "", w[1:])


def screen_tokens(text):
    toks = []
    for raw in text.split():
        if raw in ("–", "-", "·", "—"):
            if toks:
                toks[-1]["br"] = True
            continue
        toks.append({"w": raw})
    return toks


def merge_wiz(ws):
    """« Wiz Play » (deux mots pour la voix) = UN mot à l'écran (WizPlay)."""
    out = []
    for w in ws:
        if out and norm(out[-1]["w"]) == "wiz" and w["w"][:1].isupper():
            out[-1] = {"w": "Wiz" + w["w"].strip(".,!?"), "t": out[-1]["t"], "e": w["e"]}
        else:
            out.append(dict(w))
    return out


def align(text, said, j0=0):
    """said = mots dits [{w, t, e}] ; aligne les mots de l'écran à partir de said[j0]. Renvoie (mots, index suivant)."""
    toks = screen_tokens(text)
    S = [norm(w["w"]) for w in said]
    j = j0
    for tk in toks:
        n = norm(tk["w"].replace("(", "").replace(")", ""))
        keys = [norm(x) for x in SPOKEN.get(n, [n])]
        k = j
        while k < len(S) and k < j + 12 and S[k] != keys[0]:
            k += 1
        if k < len(S) and S[k] == keys[0]:
            last = min(k + len(keys) - 1, len(S) - 1)
            tk["t"], tk["e"] = round(said[k]["t"], 3), round(said[last]["e"], 3)
            j = last + 1
    for i, tk in enumerate(toks):   # non retrouvés : interpolés entre leurs voisins
        if "t" not in tk:
            prev = next((toks[p] for p in range(i - 1, -1, -1) if "t" in toks[p]), None)
            nxt = next((toks[p] for p in range(i + 1, len(toks)) if "t" in toks[p]), None)
            a = prev["e"] if prev else (said[j0]["t"] if j0 < len(said) else 0)
            b = nxt["t"] if nxt else (said[min(j, len(said) - 1)]["e"] if said else a + 0.3)
            tk["t"], tk["e"], tk["guess"] = round(a, 3), round(max(b, a + 0.05), 3), True
    return toks, j


def spoken_from_alignment(d):
    al, text = d["alignment"], d["text"]
    ch, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    text = "".join(ch) if len(ch) != len(text) else text
    out, cur, cs = [], "", None
    for j in range(len(text) + 1):
        c = text[j] if j < len(text) else " "
        if c.isspace():
            if cur:
                out.append({"w": cur, "t": st[cs], "e": en[j - 1]})
            cur, cs = "", None
        else:
            cs = j if cs is None else cs
            cur += c
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--script", default="vo-script.json")
    ap.add_argument("--timing", required=True)
    ap.add_argument("--out", default="words.js")
    a = ap.parse_args()
    sc = json.load(open(a.script, encoding="utf-8"))
    tm = json.load(open(a.timing, encoding="utf-8"))
    lines = sc["lines"]
    out = {}
    if isinstance(tm, dict) and "alignment" in tm:
        said = merge_wiz(spoken_from_alignment(tm))
    elif isinstance(tm, dict) and "words" in tm:
        said = merge_wiz([{"w": w["text"], "t": w["start"], "e": w["end"]} for w in tm["words"] if w.get("type", "word") == "word"])
    else:
        said = None
    j = 0
    for k, ln in lines.items():
        if said is None:
            toks, _ = align(ln["text"], merge_wiz(tm[k]))
        else:
            toks, j = align(ln["text"], said, j)
        for i in ln.get("hide", []):
            if 0 <= i < len(toks):
                toks[i]["x"] = True
        out[k] = toks
        g = [t["w"] for t in toks if t.get("guess")]
        print(f"  {k} {toks[0]['t']:6.2f} -> {toks[-1]['e']:6.2f}  {len(toks)} mots" + (f"   ⚠ interpolés : {' '.join(g)}" if g else ""))
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write("/* GÉNÉRÉ par tools/words.py — mots de l'écran (verbatim) calés sur la voix. Ne pas éditer à la main. */\n")
        fh.write("window.WIZ_WORDS = " + json.dumps(out, ensure_ascii=False) + ";\n")
    print("ok ->", a.out)


if __name__ == "__main__":
    main()
