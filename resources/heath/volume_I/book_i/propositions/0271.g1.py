"""Programmatic construction for Book I, Proposition 6 Note — Converse of I. 5 Part 2 (0271.g1).

An-Nairīzī's proof of the converse of the second part of I. 5: if the angles
formed by producing two sides of a triangle beyond the base are equal, the
triangle is isosceles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0271_g1() -> Model:
    """Construct the figure for 0271.g1 using geometor.model."""
    model = Model("0271.g1")

    # 1. Triangle ABC with sides AB, AC produced to D and E
    A = model.set_point(63, -23, classes=["given"], label="A")
    B = model.set_point(36, -100, classes=["given"], label="B")
    C = model.set_point(97, -100, classes=["given"], label="C")
    D = model.set_point(18, -160, label="D")
    E = model.set_point(122, -160, label="E")

    model.construct_line(A, D)
    model.construct_line(A, E)

    # 2. Equal extensions BF and CG on BD and CE, and point H on FA such that FH = GA
    F = model.set_point(26, -136, label="F")
    G = model.set_point(111, -136, label="G")
    H = model.set_point(55, -46, label="H")

    # Segments along left ray A-H-B-F-D
    model.set_segment(A, H)
    model.set_segment(H, B)
    model.set_segment(A, B)
    model.set_segment(B, F)
    model.set_segment(F, D)
    model.set_segment(B, D)
    model.set_segment(H, F)
    model.set_segment(A, F)
    model.set_segment(A, D)

    # Segments along right ray A-C-G-E
    model.set_segment(A, C)
    model.set_segment(C, G)
    model.set_segment(G, E)
    model.set_segment(C, E)
    model.set_segment(A, G)
    model.set_segment(A, E)

    # Base BC and cross segments FC, GB, CH, FG
    model.set_segment(B, C)
    model.set_segment(F, C)
    model.set_segment(G, B)
    model.set_segment(C, H)
    model.set_segment(F, G)

    # Polygons compared in the proof
    model.set_polygon([A, B, C])
    model.set_polygon([B, F, C])
    model.set_polygon([C, G, B])
    model.set_polygon([H, F, C])
    model.set_polygon([A, G, B])
    model.set_polygon([H, B, C])

    return model


if __name__ == "__main__":
    construct_0271_g1()
