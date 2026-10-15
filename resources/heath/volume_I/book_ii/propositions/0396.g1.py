"""Programmatic construction for Book II, Proposition 5 (0396.g1).

If a straight line be cut into equal and unequal segments, the rectangle
contained by the unequal segments of the whole together with the square on the
straight line between the points of section is equal to the square on the half.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0396_g1() -> Model:
    """Construct the figure for Book II, Proposition 5 using geometor.model."""
    model = Model("0396.g1")

    # Straight line AB bisected at C and cut unequally at D
    A = model.set_point(20.5, -28.5, classes=["given"], label="A")
    C = model.set_point(157.5, -28.5, classes=["given"], label="C")
    D = model.set_point(196.5, -28.5, classes=["given"], label="D")
    B = model.set_point(294.5, -28.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(A, D)
    model.set_segment(D, B)
    model.set_segment(C, D)

    # Square CEFB described on CB [I. 46], diagonal BE joined
    E = model.set_point(157.5, -166.5, label="E")
    F = model.set_point(294.5, -166.5, label="F")
    model.set_segment(C, E)
    model.set_segment(E, F)
    model.set_segment(B, F)
    model.set_polygon([C, E, F, B])

    model.construct_line(B, E)
    model.set_segment(B, E)

    # Parallel DG to CE/BF through D, meeting BE at H and EF at G [I. 31]
    H = model.set_point(196.5, -126.5, label="H")
    G = model.set_point(196.5, -166.5, label="G")
    model.construct_line(D, G)
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(E, G)
    model.set_segment(G, F)
    model.set_segment(B, H)
    model.set_segment(H, E)

    # Parallel KM to AB/EF through H, meeting CE at L, BF at M, and AK at K [I. 31]
    K = model.set_point(20.5, -126.5, label="K")
    L = model.set_point(157.5, -126.5, label="L")
    M = model.set_point(294.5, -126.5, label="M")
    model.construct_line(K, M)
    model.set_segment(K, M)
    model.set_segment(K, L)
    model.set_segment(L, H)
    model.set_segment(H, M)
    model.set_segment(K, H)
    model.set_segment(L, M)

    model.set_segment(A, K)
    model.set_segment(C, L)
    model.set_segment(L, E)
    model.set_segment(B, M)
    model.set_segment(M, F)

    # Squares about diameter: DBMH (DM) on DB and LGEH (LG) on CD
    model.set_polygon([D, B, M, H])
    model.set_polygon([L, H, G, E])

    # Complements CH (CDHL) and HF (HMGF), plus rectangles AL (ACLK), CM (CBML), DF (DBFG), AH (ADHK)
    model.set_polygon([C, D, H, L])
    model.set_polygon([H, M, F, G])
    model.set_polygon([A, C, L, K])
    model.set_polygon([C, B, M, L])
    model.set_polygon([D, B, F, G])
    model.set_polygon([A, D, H, K])

    # L-shaped Gnomon NOP around LG: C B F G H L
    model.set_polygon([C, B, F, G, H, L])

    return model


if __name__ == "__main__":
    construct_0396_g1()
