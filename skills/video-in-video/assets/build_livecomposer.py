"""Construit le LIVE COMPOSER : la scene complete avec l'overlay deja incruste
dans le quad, en temps reel, et des reglages (IN/OUT/vitesse/cadrage/luminosite).
L'utilisateur juge le RENDU FINAL au lieu d'imaginer, et colle un seul JSON.

Usage: python build_livecomposer.py <base_proxy.mp4> <ov_proxy.mp4> <out.html>
                                    <titre> <key> <BW> <BH> <OW> <OH>
                                    <basedur> <ovdur> <quad_json>
Le quad est en pixels de la BASE (le proxy doit etre a la meme resolution).
"""
import base64
import json
import pathlib
import sys

TPL = pathlib.Path(__file__).with_name("live-composer-template.html")

(_, base_mp4, ov_mp4, out_html, title, key,
 bw, bh, ow, oh, basedur, ovdur, quad) = sys.argv

q = json.loads(quad)
# Aspect du quad = moyenne des cotes opposes (meme formule que le content-picker).
# ⚠️ NE PAS utiliser max/max : le compositeur recadrerait differemment de l'outil
# et le cadrage choisi par l'utilisateur ne serait pas respecte (bug du 19/08).
import math
d = lambda a, b_: math.dist(q[a], q[b_])
aspect = round(((d("tl", "tr") + d("bl", "br")) / 2) / ((d("tl", "bl") + d("tr", "br")) / 2), 4)

b64 = lambda p: "data:video/mp4;base64," + base64.b64encode(pathlib.Path(p).read_bytes()).decode("ascii")

html = TPL.read_text(encoding="utf-8")
for token, value in (("__BASESRC__", b64(base_mp4)), ("__OVSRC__", b64(ov_mp4)),
                     ("__TITLE__", title), ("__KEY__", key),
                     ("__BW__", bw), ("__BH__", bh), ("__OW__", ow), ("__OH__", oh),
                     ("__BASEDUR__", basedur), ("__OVDUR__", ovdur),
                     ("__ASPECT__", str(aspect)), ("__QUAD__", json.dumps(q))):
    html = html.replace(token, value)

pathlib.Path(out_html).write_text(html, encoding="utf-8")
print(f"{out_html} ecrit ({len(html) / 1e6:.1f} Mo) | aspect quad = {aspect}")
