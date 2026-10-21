# -*- coding: utf-8 -*-
"""Tracés des wordmarks Wiz depuis la police Baloo, avec le crénage de la police (HarfBuzz).
Même convention que src/assets/logos/wizWordPaths.ts du site : taille 300, ligne de base y=300,
viewBox = boîte englobante + 6 de marge. Sert aux noms que le site n'a pas tracés (WizBuddy, WizLab).
    python scripts/wordmarks.py --check      # recalcule les 8 noms du site et compare
Dépendances : pip install fonttools uharfbuzz"""
import json, pathlib, sys
import uharfbuzz as hb
from fontTools.ttLib import TTFont
from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen

KIT = pathlib.Path(__file__).resolve().parents[1]
FONT = KIT / "fonts/baloo-chettan-regular.ttf"
SIZE, BASE, PAD = 300, 300, 6


def _num(v):
    return ("%.1f" % v).rstrip("0").rstrip(".")


def wordmark(name, font=FONT):
    """{'wiz', 'suffix', 'vb'} pour un nom « Wiz… »."""
    data = font.read_bytes()
    tt = TTFont(font); gs = tt.getGlyphSet(); order = tt.getGlyphOrder()
    s = SIZE / tt["head"].unitsPerEm
    buf = hb.Buffer(); buf.add_str(name); buf.guess_segment_properties()
    hb.shape(hb.Font(hb.Face(data)), buf, {"kern": True, "liga": False})
    pens = {"wiz": SVGPathPen(gs, ntos=_num), "suffix": SVGPathPen(gs, ntos=_num)}
    bounds = BoundsPen(gs); x = 0
    for i, (info, pos) in enumerate(zip(buf.glyph_infos, buf.glyph_positions)):
        glyph = gs[order[info.codepoint]]
        t = (s, 0, 0, -s, s * (x + pos.x_offset), BASE - s * pos.y_offset)
        glyph.draw(TransformPen(pens["wiz" if info.cluster < 3 else "suffix"], t))
        glyph.draw(TransformPen(bounds, t))
        x += pos.x_advance
    x0, y0, x1, y1 = bounds.bounds
    vb = " ".join(_num(v) for v in (x0 - PAD, y0 - PAD, x1 - x0 + 2 * PAD, y1 - y0 + 2 * PAD))
    return {"wiz": pens["wiz"].getCommands(), "suffix": pens["suffix"].getCommands(), "vb": vb}


if __name__ == "__main__" and "--check" in sys.argv:
    site = json.loads((KIT / "components/wizWordPaths.json").read_text(encoding="utf-8"))
    for name, ref in site.items():
        if name == "Wizdi":
            continue
        mine = wordmark(name)
        print(f"{name:<9} vb site {ref['vb']:<28} vb ici {mine['vb']:<28} {'OK' if mine['vb'] == ref['vb'] else 'ÉCART'}")
