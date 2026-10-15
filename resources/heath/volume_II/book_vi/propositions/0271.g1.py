"""Programmatic construction for Book VI, Proposition 29 (0271.g1).

Application of a parallelogram equal to a given rectilineal figure C and exceeding by a figure similar to D.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0271_g1() -> Model:
    """Construct the figure for 0271.g1 (VI.29) using geometor.model."""
    model = Model("0271.g1")

    # 1. Points - Auxiliary figure C
    C1 = model.set_point(16, -90, label="C1")
    C2 = model.set_point(52, -60, label="C2")
    C3 = model.set_point(109, -82, label="C3")
    C4 = model.set_point(96, -121, label="C4")
    C5 = model.set_point(45, -149, label="C5")

    # Auxiliary figure D
    D1 = model.set_point(147, -105, label="D1")
    D2 = model.set_point(158, -44, label="D2")
    D3 = model.set_point(195, -44, label="D3")
    D4 = model.set_point(184, -105, label="D4")

    # Main figure
    F = model.set_point(219, -28, label="F")
    L = model.set_point(281, -28, label="L")
    M = model.set_point(309, -28, label="M")

    A = model.set_point(136, -132, classes=["given"], label="A")
    E = model.set_point(198, -132, label="E")
    B = model.set_point(260, -132, classes=["given"], label="B")
    P = model.set_point(288, -132, label="P")

    A1 = model.set_point(128, -175, label="A1")
    N = model.set_point(190, -175, label="N")
    Q = model.set_point(252, -175, label="Q")
    O = model.set_point(280, -175, label="O")

    # Auxiliary parallelogram GH
    K = model.set_point(406, -28, label="K")
    H = model.set_point(498, -28, label="H")
    H1 = model.set_point(468, -174, label="H1")
    G = model.set_point(376, -174, label="G")

    # 2. Construction Lines
    model.construct_line(F, L)
    model.construct_line(F, E)
    model.construct_line(A, B)
    model.construct_line(F, O)

    # 3. Segments
    model.set_segment(F, L)
    model.set_segment(L, M)
    model.set_segment(F, M)

    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(B, P)
    model.set_segment(A, B)
    model.set_segment(E, P)
    model.set_segment(A, P)

    model.set_segment(A1, N)
    model.set_segment(N, Q)
    model.set_segment(Q, O)
    model.set_segment(A1, Q)
    model.set_segment(N, O)
    model.set_segment(A1, O)

    model.set_segment(A, A1)

    model.set_segment(F, E)
    model.set_segment(E, N)
    model.set_segment(F, N)

    model.set_segment(L, B)
    model.set_segment(B, Q)
    model.set_segment(L, Q)

    model.set_segment(M, P)
    model.set_segment(P, O)
    model.set_segment(M, O)

    model.set_segment(F, B)
    model.set_segment(B, O)
    model.set_segment(F, O)

    model.set_segment(K, H)
    model.set_segment(H, H1)
    model.set_segment(H1, G)
    model.set_segment(G, K)

    # 4. Collinear Sections
    model.set_section([A, E, B])
    model.set_section([A, B, P])
    model.set_section([F, L, M])
    model.set_section([F, E, N])
    model.set_section([F, B, O])

    # 5. Polygons (Parallelograms, Rectilineal Figure C, Gnomon XWV)
    model.set_polygon([F, E, B, L])  # BF / FB / EL
    model.set_polygon([F, N, O, M])  # MN
    model.set_polygon([A, A1, N, E])  # AN
    model.set_polygon([E, N, Q, B])  # NB
    model.set_polygon([L, B, P, M])  # LP
    model.set_polygon([E, N, O, P])  # EO
    model.set_polygon([B, Q, O, P])  # QP / PQ
    model.set_polygon([A, A1, O, P])  # AO
    model.set_polygon([E, N, O, M, L, B])  # Gnomon XWV / VWX
    model.set_polygon([C1, C2, C3, C4, C5])  # C
    model.set_polygon([D1, D2, D3, D4])  # D
    model.set_polygon([K, G, H1, H])  # GH

    return model


if __name__ == "__main__":
    construct_0271_g1()
