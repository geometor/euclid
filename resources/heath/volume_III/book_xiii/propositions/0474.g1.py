"""Programmatic construction for Book XIII, Proposition 13 Lemma (0474.g1).

Semicircle ADB on diameter AB with perpendicular DC, chords AD, DB,
square EC (AEFC) on AC, and completed parallelogram FB (CFGB).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0474_g1() -> Model:
    """Construct the figure 0474.g1 using geometor.model."""
    model = Model("0474.g1")

    A = model.set_point(22.0, -118.0, classes=["given"], label="A")
    B = model.set_point(232.0, -118.0, classes=["given"], label="B")
    C = model.set_point(162.0, -118.0, classes=["constructed"], label="C")
    D = model.set_point(162.0, -19.0, classes=["constructed"], label="D")
    E = model.set_point(22.0, -258.0, classes=["constructed"], label="E")
    F = model.set_point(162.0, -258.0, classes=["constructed"], label="F")
    G = model.set_point(232.0, -258.0, classes=["auxiliary"], label="G")
    O = model.set_point(127.0, -118.0, classes=["auxiliary"], label="O")

    # Semicircle ADB
    model.construct_circle(O, A)

    # Polygons and triangles
    model.set_polygon([A, C, F, E])
    model.set_polygon([C, B, G, F])
    model.set_polygon([A, B, G, E])
    model.set_polygon([D, A, B])
    model.set_polygon([D, A, C])
    model.set_polygon([D, B, C])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (A, C), (C, B),
        (A, D), (D, B), (C, D),
        (A, E), (C, F), (B, G),
        (E, F), (F, G), (E, G),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, C, B])
    model.set_section([D, C, F])

    # Angle ADB
    model.set_wedge(D, A, A, B)

    return model


if __name__ == "__main__":
    construct_0474_g1()
