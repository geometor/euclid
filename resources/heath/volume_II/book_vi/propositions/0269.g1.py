"""Programmatic construction for Book VI, Proposition 28 Commentary (0269.g1).

Algebraic interpretation of Euclid's solution of the quadratic equation using rectangles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0269_g1() -> Model:
    """Construct the figure for 0269.g1 (VI.28 commentary) using geometor.model."""
    model = Model("0269.g1")

    # 1. Points - Main rectangle
    A1 = model.set_point(18, -65, label="A1")
    G = model.set_point(107, -65, label="G")
    P = model.set_point(169, -65, label="P")
    F = model.set_point(196, -65, label="F")

    T = model.set_point(18, -133, label="T")
    O = model.set_point(107, -133, label="O")
    Q = model.set_point(169, -133, label="Q")
    R = model.set_point(196, -133, label="R")

    A = model.set_point(18, -163, classes=["given"], label="A")
    E = model.set_point(107, -163, label="E")
    S = model.set_point(169, -163, label="S")
    B = model.set_point(196, -163, classes=["given"], label="B")

    # Auxiliary figure C
    C1 = model.set_point(229, -86, label="C1")
    C2 = model.set_point(303, -42, label="C2")
    C3 = model.set_point(343, -87, label="C3")
    C4 = model.set_point(245, -109, label="C4")

    # Auxiliary rectangle D
    D1 = model.set_point(263, -125, label="D1")
    D2 = model.set_point(293, -125, label="D2")
    D3 = model.set_point(293, -161, label="D3")
    D4 = model.set_point(263, -161, label="D4")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(G, B)

    # 3. Segments
    model.set_segment(A1, G)
    model.set_segment(G, P)
    model.set_segment(P, F)
    model.set_segment(G, F)
    model.set_segment(A1, F)

    model.set_segment(T, O)
    model.set_segment(O, Q)
    model.set_segment(Q, R)
    model.set_segment(T, Q)
    model.set_segment(O, R)
    model.set_segment(T, R)

    model.set_segment(A, E)
    model.set_segment(E, S)
    model.set_segment(S, B)
    model.set_segment(A, S)
    model.set_segment(E, B)
    model.set_segment(A, B)

    model.set_segment(A1, T)
    model.set_segment(T, A)
    model.set_segment(A1, A)

    model.set_segment(G, O)
    model.set_segment(O, E)
    model.set_segment(G, E)

    model.set_segment(P, Q)
    model.set_segment(Q, S)
    model.set_segment(P, S)

    model.set_segment(F, R)
    model.set_segment(R, B)
    model.set_segment(F, B)

    model.set_segment(G, Q)
    model.set_segment(Q, B)
    model.set_segment(G, B)

    # 4. Collinear Sections
    model.set_section([A, E, B])
    model.set_section([A, S, B])
    model.set_section([G, O, E])
    model.set_section([G, Q, B])

    # 5. Polygons (Rectangles & Figure C)
    model.set_polygon([G, E, B, F])  # GEBF / GB
    model.set_polygon([G, O, Q, P])  # GQ
    model.set_polygon([A, E, G, A1])  # AG
    model.set_polygon([T, A, S, Q])  # TS / AQ
    model.set_polygon([Q, S, B, R])  # QB
    model.set_polygon([C1, C2, C3, C4])  # C
    model.set_polygon([D1, D2, D3, D4])  # D

    # 6. Angles (Wedges)
    model.set_wedge(G, F, F, E)

    return model


if __name__ == "__main__":
    construct_0269_g1()
