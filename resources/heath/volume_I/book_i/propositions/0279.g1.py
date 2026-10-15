"""Programmatic construction for Book I, Proposition 9 Note — Proclus' Variation (0279.g1).

Proclus' construction for bisecting an angle when the equilateral triangle ADE
is constructed on DE with vertex at A, cutting off AF = AG and joining DG, EF
meeting in H, then joining AH.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0279_g1() -> Model:
    """Construct the figure for 0279.g1 using geometor.model."""
    model = Model("0279.g1")

    # 1. Angle BAC with equilateral triangle ADE
    A = model.set_point(82, -20, classes=["given"], label="A")
    B = model.set_point(4, -164, classes=["given"], label="B")
    C = model.set_point(160, -164, classes=["given"], label="C")
    D = model.set_point(24, -128, label="D")
    E = model.set_point(140, -128, label="E")

    # 2. Equal segments AF on AD and AG on AE, with DG and EF meeting at H
    F = model.set_point(53, -67, label="F")
    G = model.set_point(111, -67, label="G")
    H = model.set_point(82, -85, label="H")

    model.construct_line(A, B)
    model.construct_line(A, C)

    # Segments along ray A-F-D-B
    model.set_segment(A, F)
    model.set_segment(F, D)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(A, B)

    # Segments along ray A-G-E-C
    model.set_segment(A, G)
    model.set_segment(G, E)
    model.set_segment(A, E)
    model.set_segment(E, C)
    model.set_segment(A, C)

    # Cross segments and bisector AH
    model.set_segment(D, E)
    model.set_segment(F, G)
    model.set_segment(D, G)
    model.set_segment(E, F)
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(E, H)
    model.set_segment(H, F)
    model.set_segment(A, H)

    model.set_polygon([A, D, E])
    model.set_polygon([A, F, G])
    model.set_polygon([F, G, H])
    model.set_polygon([D, E, H])

    return model


if __name__ == "__main__":
    construct_0279_g1()
