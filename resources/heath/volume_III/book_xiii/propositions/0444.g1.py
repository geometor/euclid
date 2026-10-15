"""Programmatic construction for Book XIII, Proposition 1 (0444.g1).

If a straight line be cut in extreme and mean ratio, the square on the greater
segment added to the half of the whole is five times the square on the half.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0444_g1() -> Model:
    """Construct the figure for Book XIII, Proposition 1 using geometor.model."""
    model = Model("0444.g1")

    # Straight line AB cut in extreme and mean ratio at C, with AD = 1/2 AB
    D = model.set_point(21.0, -172.0, classes=["given"], label="D")
    A = model.set_point(88.0, -172.0, classes=["given"], label="A")
    C = model.set_point(170.0, -172.0, classes=["given"], label="C")
    B = model.set_point(221.0, -172.0, classes=["given"], label="B")

    model.construct_line(D, B)
    model.set_segment(D, B)
    model.set_segment(D, C)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Square DLFC (DF) on DC, divided through A and H
    L = model.set_point(21.0, -23.0, label="L")
    R = model.set_point(88.0, -23.0, label="R")
    F = model.set_point(170.0, -23.0, label="F")
    P = model.set_point(21.0, -105.0, label="P")
    H = model.set_point(88.0, -105.0, label="H")
    Q = model.set_point(170.0, -105.0, label="Q")

    # Square ABEK (AE) on AB, divided by CG
    K = model.set_point(88.0, -305.0, label="K")
    G = model.set_point(170.0, -305.0, label="G")
    E = model.set_point(221.0, -305.0, label="E")

    # Horizontal segments in DF and AE
    model.set_segment(L, F)
    model.set_segment(L, R)
    model.set_segment(R, F)
    model.set_segment(P, Q)
    model.set_segment(P, H)
    model.set_segment(H, Q)
    model.set_segment(K, E)
    model.set_segment(K, G)
    model.set_segment(G, E)

    # Vertical segments in DF and AE
    model.set_segment(L, D)
    model.set_segment(L, P)
    model.set_segment(P, D)
    model.set_segment(R, K)
    model.set_segment(R, H)
    model.set_segment(H, A)
    model.set_segment(A, K)
    model.set_segment(F, G)
    model.set_segment(F, Q)
    model.set_segment(Q, C)
    model.set_segment(C, G)
    model.set_segment(B, E)

    # Diagonal DF
    model.set_segment(D, F)
    model.set_segment(D, H)
    model.set_segment(H, F)

    # Polygons (squares, rectangles, and gnomon MNO)
    model.set_polygon([D, L, F, C])
    model.set_polygon([A, B, E, K])
    model.set_polygon([D, P, H, A])
    model.set_polygon([H, R, F, Q])
    model.set_polygon([P, L, R, H])
    model.set_polygon([A, H, Q, C])
    model.set_polygon([A, C, G, K])
    model.set_polygon([C, B, E, G])
    model.set_polygon([P, L, F, C, A, H])

    return model


if __name__ == "__main__":
    construct_0444_g1()
