"""Programmatic construction for Appendix I (Book XIV), Proposition 3 (0519.g1).

If ABCDE is an equilateral and equiangular pentagon inscribed in a circle with
centre F, and FG is perpendicular to CD, then 30 CD * FG equals the surface of
the dodecahedron (12 times the area of the pentagon).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0519_g1() -> Model:
    """Construct the figure 0519.g1 using geometor.model."""
    model = Model("0519.g1")

    # Circle centre F and inscribed regular pentagon ABCDE
    F = model.set_point(85.0, -89.0, classes=["given"], label="F")
    A = model.set_point(85.0, -19.0, classes=["given"], label="A")
    B = model.set_point(18.0, -67.0, classes=["given"], label="B")
    C = model.set_point(44.0, -146.0, classes=["given"], label="C")
    D = model.set_point(126.0, -146.0, classes=["given"], label="D")
    E = model.set_point(152.0, -67.0, classes=["given"], label="E")
    model.construct_circle(F, A)

    # Foot G of perpendicular from F to CD
    G = model.set_point(85.0, -146.0, classes=["given"], label="G")

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([C, D, F])
    model.set_polygon([C, F, G])
    model.set_polygon([D, F, G])

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (C, G), (G, D), (D, E), (E, A),
        (C, F), (F, D), (F, G),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0519_g1()
