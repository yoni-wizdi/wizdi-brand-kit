"""Construit l'outil pinceau de masque (l'utilisateur peint l'occulteur lui-meme).

Usage: python build_maskbrush.py <proxy.mp4> <out.html> <titre> <key> <w> <h> <quad_json>
Le proxy doit etre a la resolution de TRAVAIL (sinon convertir les coords ensuite).
"""
import base64
import pathlib
import sys

TPL = pathlib.Path(__file__).with_name("mask-brush-template.html")

_, proxy, out_html, title, key, w, h, quad = sys.argv

b64 = base64.b64encode(pathlib.Path(proxy).read_bytes()).decode("ascii")
html = TPL.read_text(encoding="utf-8")
for token, value in (("__VIDEOSRC__", "data:video/mp4;base64," + b64),
                     ("__TITLE__", title), ("__KEY__", key),
                     ("__W__", w), ("__H__", h), ("__QUAD__", quad)):
    html = html.replace(token, value)
pathlib.Path(out_html).write_text(html, encoding="utf-8")
print(f"{out_html} ecrit ({len(html) / 1e6:.1f} Mo)")
