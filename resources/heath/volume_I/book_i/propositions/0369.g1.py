"""Programmatic construction for Proposition 47 Commentary (0369.g1).

Bhāskara's dissection of the square on the hypotenuse c^2 into four right-angled
triangles of area ab/2 and a central square of side (a - b).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0369_g1() -> Model:
    """Construct Bhāskara's figure (0369.g1) using geometor.model."""
    model = Model("0369.g1")

    A = model.set_point(17, -7, classes=["given"], label="A")
    B = model.set_point(133, -7, classes=["given"], label="B")
    C = model.set_point(133, -122, classes=["given"], label="C")
    D = model.set_point(17, -122, classes=["given"], label="D")

    E = model.set_point(68, -42, label="E")
    F = model.set_point(101, -60, label="F")
    G = model.set_point(83, -88, label="G")
    H = model.set_point(51, -68, label="H")

    # Outer square ABCD, inner square EFGH, and 4 right-angled triangles
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G, H])
    model.set_polygon([A, B, F])
    model.set_polygon([B, C, G])
    model.set_polygon([C, D, H])
    model.set_polygon([D, A, E])

    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (A, F), (B, G), (C, H), (D, E),
        (A, E), (E, F), (B, F), (F, G), (C, G), (G, H), (D, H), (H, E),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0369_g1()
