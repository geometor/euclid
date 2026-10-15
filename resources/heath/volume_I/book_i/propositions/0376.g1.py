"""Programmatic construction for Proposition 47 Commentary (0376.g1).

Āpastamba-Śulba-Sūtra transformation of a rectangle ABCD into the difference
between two squares LB and LF (a gnomon).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0376_g1() -> Model:
    """Construct the Āpastamba rectangle-to-gnomon figure (0376.g1) using geometor.model."""
    model = Model("0376.g1")

    A = model.set_point(47.5, -172.5, classes=["given"], label="A")
    B = model.set_point(141.5, -172.5, classes=["given"], label="B")
    C = model.set_point(141.5, -29.5, classes=["given"], label="C")
    D = model.set_point(47.5, -29.5, classes=["given"], label="D")

    E = model.set_point(141.5, -75.5, label="E")
    F = model.set_point(47.5, -75.5, label="F")
    G = model.set_point(141.5, -52.5, label="G")
    H = model.set_point(47.5, -52.5, label="H")
    K = model.set_point(22, -75.5, label="K")
    L = model.set_point(22, -52.5, label="L")
    M = model.set_point(22, -172.5, label="M")

    # Polygons: rectangle ABCD, square ABEF, remainder DE (DCEF), halves DG (DCGH) and HGFE,
    # moved rectangle AK (AFKM), completed square LB (LGBM), and corner square LF (LHFK)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, B, E, F])
    model.set_polygon([D, C, E, F])
    model.set_polygon([D, C, G, H])
    model.set_polygon([H, G, E, F])
    model.set_polygon([A, F, K, M])
    model.set_polygon([L, G, B, M])
    model.set_polygon([L, H, F, K])

    # Segments
    for p1, p2 in [
        (A, B), (M, A), (M, B),
        (B, C), (B, E), (E, G), (G, C), (E, C), (B, G),
        (D, C), (H, G), (F, E), (K, F), (K, E),
        (A, D), (A, F), (F, H), (H, D), (F, D), (A, H),
        (K, M), (L, K), (L, H), (L, G), (L, M),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0376_g1()
