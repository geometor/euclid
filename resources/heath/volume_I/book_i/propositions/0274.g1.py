"""Programmatic construction for Book I, Proposition 7 Note — Second Case (0274.g1).

Proclus' proof of the second case of I. 7, where the second pair of lines AD, DB
lies entirely within the triangle ABC, with AC produced to E and AD produced to F.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0274_g1() -> Model:
    """Construct the figure for 0274.g1 using geometor.model."""
    model = Model("0274.g1")

    # 1. Base AB and outer vertex C, inner vertex D
    A = model.set_point(18, -149, classes=["given"], label="A")
    B = model.set_point(126, -149, classes=["given"], label="B")
    C = model.set_point(39, -58, label="C")
    D = model.set_point(58, -98, label="D")

    # 2. Produced endpoints E on AC produced and F on AD produced
    E = model.set_point(48, -17, label="E")
    F = model.set_point(92, -53, label="F")

    model.construct_line(A, E)
    model.construct_line(A, F)

    # Segments along ray A-C-E and ray A-D-F
    model.set_section([A, C, E])
    model.set_segment(A, C)
    model.set_segment(C, E)
    model.set_segment(A, E)

    model.set_section([A, D, F])
    model.set_segment(A, D)
    model.set_segment(D, F)
    model.set_segment(A, F)

    # Base AB and segments BC, BD, CD
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(C, D)

    # Triangles ABC, ABD, ACD, BDC
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([B, D, C])

    return model


if __name__ == "__main__":
    construct_0274_g1()
