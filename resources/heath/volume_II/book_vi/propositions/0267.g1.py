"""Programmatic construction for Book VI, Proposition 28 (0267.g1).

Application of a parallelogram equal to a given rectilineal figure C and deficient by a figure similar to D.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0267_g1() -> Model:
    """Construct the figure for 0267.g1 (VI.28) using geometor.model."""
    model = Model("0267.g1")

    # 1. Points - Main figure
    H = model.set_point(21, -44, label="H")
    G = model.set_point(100, -44, label="G")
    P = model.set_point(162, -44, label="P")
    F = model.set_point(190, -44, label="F")

    T = model.set_point(38, -132, label="T")
    O = model.set_point(117, -132, label="O")
    Q = model.set_point(179, -132, label="Q")
    R = model.set_point(207, -132, label="R")

    A = model.set_point(46, -171, classes=["given"], label="A")
    E = model.set_point(125, -171, label="E")
    S = model.set_point(187, -171, label="S")
    B = model.set_point(215, -171, classes=["given"], label="B")

    # Auxiliary figure C (given rectilineal figure)
    C1 = model.set_point(196, -16, label="C1")
    C2 = model.set_point(306, -26, label="C2")
    C3 = model.set_point(299, -75, label="C3")
    C4 = model.set_point(223, -88, label="C4")

    # Auxiliary figure D (given parallelogram)
    D1 = model.set_point(251, -100, label="D1")
    D2 = model.set_point(296, -100, label="D2")
    D3 = model.set_point(310, -170, label="D3")
    D4 = model.set_point(265, -170, label="D4")

    # Auxiliary parallelogram KLMN
    L = model.set_point(333, -80, label="L")
    M = model.set_point(394, -80, label="M")
    N = model.set_point(412, -170, label="N")
    K = model.set_point(351, -170, label="K")

    # 2. Construction Lines
    model.construct_line(A, B)
    model.construct_line(G, B)

    # 3. Segments
    model.set_segment(H, G)
    model.set_segment(G, P)
    model.set_segment(P, F)
    model.set_segment(H, P)
    model.set_segment(G, F)
    model.set_segment(H, F)

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

    model.set_segment(H, T)
    model.set_segment(T, A)
    model.set_segment(H, A)

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

    model.set_segment(K, L)
    model.set_segment(L, M)
    model.set_segment(M, N)
    model.set_segment(N, K)

    # 4. Collinear Sections
    model.set_section([A, E, B], classes=["golden"])
    model.set_section([A, S, B])
    model.set_section([G, Q, B])
    model.set_section([G, P, F])
    model.set_section([G, O, E])

    # 5. Polygons (Parallelograms, Rectilineal Figure C, Gnomon UWV)
    model.set_polygon([E, B, F, G])  # EBFG / GB / BG
    model.set_polygon([A, E, G, H])  # AG / HE
    model.set_polygon([A, B, F, H])  # AF
    model.set_polygon([O, G, P, Q])  # OGPQ / GQ
    model.set_polygon([P, Q, R, F])  # PR
    model.set_polygon([O, E, S, Q])  # OS
    model.set_polygon([Q, S, B, R])  # QB
    model.set_polygon([P, S, B, F])  # PB
    model.set_polygon([O, E, B, R])  # OB
    model.set_polygon([T, A, E, O])  # TE
    model.set_polygon([T, A, S, Q])  # TS / ST
    model.set_polygon([H, T, Q, P])  # HQ
    model.set_polygon([C1, C2, C3, C4])  # C
    model.set_polygon([D1, D2, D3, D4])  # D
    model.set_polygon([K, L, M, N])  # KLMN / KM
    model.set_polygon([O, E, B, F, P, Q])  # Gnomon UWV / VWU

    return model


if __name__ == "__main__":
    construct_0267_g1()
