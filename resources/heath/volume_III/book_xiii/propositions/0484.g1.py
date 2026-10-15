"""Programmatic construction for Book XIII, Proposition 15 Commentary (0484.g1).

Pappus' inscription of a cube ABCDEFGH in a sphere using two equal and parallel
circular sections ABCD and EFGH, face diagonal EG, and sphere diameter CE.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0484_g1() -> Model:
    """Construct the figure 0484.g1 using geometor.model."""
    model = Model("0484.g1")

    # Sphere centre and boundary point
    O = model.set_point(126.5, -116.0, classes=["auxiliary"], label="O")
    S_top = model.set_point(126.5, -11.0, classes=["auxiliary"], label="S_top")
    model.construct_circle(O, S_top)

    # Upper circular section vertices E, F, G, H (inscribed square EFGH)
    E = model.set_point(61.5, -76.0, classes=["given"], label="E")
    F = model.set_point(179.0, -76.0, classes=["given"], label="F")
    G = model.set_point(188.5, -43.0, classes=["given"], label="G")
    H = model.set_point(71.0, -43.0, classes=["given"], label="H")

    # Lower circular section vertices A, B, C, D (inscribed square ABCD)
    A = model.set_point(61.5, -193.0, classes=["given"], label="A")
    B = model.set_point(179.0, -193.0, classes=["given"], label="B")
    C = model.set_point(188.5, -161.0, classes=["given"], label="C")
    D = model.set_point(71.0, -161.0, classes=["given"], label="D")

    # Polygons (squares ABCD, EFGH, right triangle CGE, cube faces)
    model.set_polygon([A, B, C, D])
    model.set_polygon([E, F, G, H])
    model.set_polygon([C, G, E])
    model.set_polygon([A, B, F, E])
    model.set_polygon([B, C, G, F])
    model.set_polygon([C, D, H, G])
    model.set_polygon([D, A, E, H])

    # Cube edges, face diagonal EG, and sphere diameter CE
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (E, F), (F, G), (G, H), (H, E),
        (E, A), (F, B), (G, C), (H, D),
        (E, G), (C, E),
    ]:
        model.set_segment(p1, p2)

    # Right angle CGE
    model.set_wedge(G, C, C, E)

    return model


if __name__ == "__main__":
    construct_0484_g1()
