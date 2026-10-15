"""Programmatic construction for Book III, Proposition 13 (0038.g3).

A circle does not touch a circle at more points than one, whether it touch
it internally or externally.
"""

from __future__ import annotations

import sympy as sp
from geometor.model import Model


def construct_0038_g3() -> Model:
    """Construct the figure 0038.g3 using geometor.model."""
    model = Model("0038.g3")

    # Circle ABDC (true center O1) and line of hypothetical internal contacts BGHD
    O1 = model.set_point(0, 58, classes=["auxiliary"])
    B = model.set_point(-sp.sqrt(3036), 0, label="B")
    D = model.set_point(sp.sqrt(3036), 0, label="D")
    model.construct_circle(O1, B)

    # Assumed centres G and H on chord BD
    G = model.set_point(-20, 0, classes=["given"], label="G")
    H = model.set_point(20, 0, classes=["given"], label="H")
    model.construct_line(B, D)

    # Points E and F on inner oval EBFD
    E = model.set_point(0, 80, label="E")
    F = model.set_point(0, -14, label="F")
    model.construct_circle(H, D)

    # External circle ACK touching/cutting ABDC at A and C
    O2 = model.set_point(86, 146, classes=["auxiliary"])
    A = model.set_point(34, 130, label="A")
    C = model.set_point(71, 94, label="C")
    K = model.set_point(140, 146, label="K")
    model.construct_circle(O2, A)

    # Collinear segments along BGHD
    model.set_segment(B, G)
    model.set_segment(G, H)
    model.set_segment(H, D)
    model.set_segment(B, H)
    model.set_segment(G, D)
    model.set_segment(B, D)
    model.set_section([B, G, D])
    model.set_section([B, H, D])

    # Chord AC joining points of external contact A and C
    model.set_segment(A, C)

    return model


if __name__ == "__main__":
    construct_0038_g3()
