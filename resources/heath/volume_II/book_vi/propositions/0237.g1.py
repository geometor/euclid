"""Programmatic construction for Book VI, Proposition 18 note (0237.g1).

Extension of VI.18 to a pentagon CDEFG and similar pentagon ABHKL constructed
on AB by successive triangles ABL, LBK, KBH.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0237_g1() -> Model:
    """Construct the figure for 0237.g1 using geometor.model."""
    model = Model("0237.g1")

    # 1. Points of constructed pentagon ABHKL
    A = model.set_point(71.0, -148.0, classes=["given"], label="A")
    B = model.set_point(182.0, -148.0, classes=["given"], label="B")
    H = model.set_point(199.0, -71.0, classes=["given"], label="H")
    K = model.set_point(99.0, -28.0, classes=["given"], label="K")
    L = model.set_point(27.0, -76.0, classes=["given"], label="L")

    # 2. Points of given pentagon CDEFG
    C = model.set_point(289.0, -148.0, classes=["given"], label="C")
    D = model.set_point(355.0, -148.0, classes=["given"], label="D")
    E = model.set_point(366.0, -102.0, classes=["given"], label="E")
    F = model.set_point(306.0, -76.0, classes=["given"], label="F")
    G = model.set_point(262.0, -105.0, classes=["given"], label="G")

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(B, H)
    model.set_segment(H, K)
    model.set_segment(K, L)
    model.set_segment(L, A)
    model.set_segment(B, L)
    model.set_segment(B, K)

    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(G, C)
    model.set_segment(D, G)
    model.set_segment(D, F)

    # 4. Polygons
    model.set_polygon([A, B, H, K, L])
    model.set_polygon([A, B, L])
    model.set_polygon([L, B, K])
    model.set_polygon([K, B, H])

    model.set_polygon([C, D, E, F, G])
    model.set_polygon([C, D, G])
    model.set_polygon([G, D, F])
    model.set_polygon([F, D, E])

    return model


if __name__ == "__main__":
    construct_0237_g1()
