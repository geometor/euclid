"""Programmatic construction for Book II, Proposition 11 — The Golden Section (0416.g1).

To cut a given straight line so that the rectangle contained by the whole and
one of the segments is equal to the square on the remaining segment.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0416_g1() -> Model:
    """Construct Euclid's Golden Section figure (Book II, Prop. 11) using geometor.model."""
    model = Model("0416.g1")

    # 1. Let AB be the given straight line (length 2 for clean midpoint E).
    A = model.set_point(0, 0, classes=["given"], label="A")
    B = model.set_point(2, 0, classes=["given"], label="B")
    model.set_segment(A, B)

    # 2. Let the square ABDC be described on AB [I. 46].
    C = model.set_point(0, -2, label="C")
    D = model.set_point(2, -2, label="D")
    model.set_polygon([A, B, D, C])

    # 3. Let AC be bisected at E, and let BE be joined.
    E = model.set_point(0, -1, label="E")
    model.set_segment(B, E)

    # 4. Let CA be drawn through to F, and let EF be made equal to BE (sqrt(5)).
    model.construct_line(C, A)
    phi_inv_2 = sp.sqrt(5) - 1  # AF = AH = sqrt(5) - 1 (for AB = 2)
    F = model.set_point(0, phi_inv_2, label="F")

    # 5. Let the square FH (FGHA) be described on AF, and let GH be drawn through to K.
    G = model.set_point(phi_inv_2, phi_inv_2, label="G")
    H = model.set_point(phi_inv_2, 0, classes=["golden"], label="H")
    K = model.set_point(phi_inv_2, -2, label="K")
    model.construct_line(G, K)

    # 6. Record the Golden Sections on AB and CF
    model.set_section([A, H, B], classes=["golden"])
    model.set_section([C, A, F], classes=["golden"])

    # 7. Explicitly add all referenced segments
    model.set_segment(A, H)
    model.set_segment(H, B)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)
    model.set_segment(A, F)
    model.set_segment(E, F)
    model.set_segment(C, F)
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, K)
    model.set_segment(G, K)
    model.set_segment(B, D)
    model.set_segment(C, K)
    model.set_segment(K, D)
    model.set_segment(C, D)

    # 8. Explicitly add all referenced squares, rectangles, triangles, and right angle
    model.set_polygon([F, G, H, A])  # Square FH on AF
    model.set_polygon([F, G, K, C])  # Rectangle FK (CF, FA)
    model.set_polygon([A, H, K, C])  # Common rectangle AK
    model.set_polygon([H, B, D, K])  # Remainder rectangle HD (AB, BH)
    model.set_polygon([A, B, E])     # Right triangle ABE
    model.set_wedge(A, B, B, E)      # Right angle at A

    return model


if __name__ == "__main__":
    construct_0416_g1()
