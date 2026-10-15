"""Programmatic construction for Book II, Proposition 14 (0423.g1).

To construct a square equal to a given rectilineal figure.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0423_g1() -> Model:
    """Construct the figure for Book II, Proposition 14 using geometor.model."""
    model = Model("0423.g1")

    # 1. Rectangular parallelogram BCDE (BD) equal to the given rectilineal figure A
    B = model.set_point(0, 0, classes=["given"], label="B")
    C = model.set_point(0, -1, classes=["given"], label="C")
    D = model.set_point(3, -1, classes=["given"], label="D")
    E = model.set_point(3, 0, classes=["given"], label="E")
    model.set_polygon([B, C, D, E])

    # 2. Produce BE to F with EF = ED
    model.construct_line(B, E)
    F = model.set_point(4, 0, label="F")

    # 3. Bisect BF at G
    G = model.set_point(2, 0, label="G")

    # 4. With centre G and distance GB or GF describe the semicircle BHF
    model.construct_circle(G, B)

    # 5. Produce DE to H on the semicircle, and join GH
    model.construct_line(D, E)
    H = model.set_point(3, sp.sqrt(3), label="H")

    # Right triangle GEH
    model.set_polygon([G, E, H])

    # Collinear sections
    model.set_section([B, G, F])
    model.set_section([B, E, F])
    model.set_section([D, E, H])

    # Segments
    for p1, p2 in [
        (B, C), (C, D), (D, E), (B, E),
        (E, F), (B, F), (G, B), (G, F), (G, E),
        (E, H), (D, H), (G, H),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0423_g1()
