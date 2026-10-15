"""Programmatic construction for Appendix I (Book XIV), Proposition 6 (0520.g1).

First proof that as the surface of the dodecahedron is to the surface of the
icosahedron, so is the side H of the cube to the side CD of the icosahedron.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0520_g1() -> Model:
    """Construct the figure 0520.g1 using geometor.model."""
    model = Model("0520.g1")

    # Cube side magnitude H (divided in extreme and mean ratio)
    H_top = model.set_point(24.0, -24.0, classes=["auxiliary"], label="H_top")
    H_div = model.set_point(24.0, -112.0, classes=["auxiliary"], label="H_div")
    H_bot = model.set_point(24.0, -152.0, classes=["auxiliary"], label="H_bot")

    # Circle centre E and points A, B, C, D on circumference
    E = model.set_point(114.0, -92.0, classes=["given"], label="E")
    D = model.set_point(54.0, -128.0, classes=["given"], label="D")
    C = model.set_point(174.0, -128.0, classes=["given"], label="C")
    A = model.set_point(96.0, -160.0, classes=["given"], label="A")
    B = model.set_point(148.0, -152.0, classes=["given"], label="B")
    model.construct_circle(E, C)

    # Perpendicular feet F (on CD) and G (on AC)
    F = model.set_point(114.0, -128.0, classes=["given"], label="F")
    G = model.set_point(141.9, -141.2, classes=["given"], label="G")

    # Polygons
    model.set_polygon([E, B, C])
    model.set_polygon([G, B, C])
    model.set_polygon([E, G, C])

    # Segments
    for p1, p2 in [
        (H_top, H_bot), (H_top, H_div), (H_div, H_bot),
        (C, D), (D, F), (F, C),
        (A, C), (A, G), (G, C),
        (E, F),
        (E, B), (E, G), (G, B),
        (B, C),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0520_g1()
