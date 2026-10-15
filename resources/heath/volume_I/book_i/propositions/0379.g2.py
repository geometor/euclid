"""Programmatic construction for Proposition 47 Commentary (0379.g2).

Leonardo da Vinci's proof of the Pythagorean theorem comparing the equal
hexagons ADEFGC and ABCHLK formed around the right-angled triangle ABC.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0379_g2() -> Model:
    """Construct Leonardo da Vinci's figure (0379.g2) using geometor.model."""
    model = Model("0379.g2")

    A = model.set_point(124, -85, classes=["given"], label="A")
    B = model.set_point(124, -185, classes=["given"], label="B")
    C = model.set_point(176, -185, classes=["given"], label="C")
    D = model.set_point(25, -85, label="D")
    E = model.set_point(25, -185, label="E")
    F = model.set_point(124, -239, label="F")
    G = model.set_point(176, -239, label="G")
    H = model.set_point(275, -128, label="H")
    K = model.set_point(224, -30, label="K")
    L = model.set_point(275, -30, label="L")

    # Squares ABED (AE), BCGF (CF), ACHK (CK)
    model.set_polygon([A, B, E, D])
    model.set_polygon([B, C, G, F])
    model.set_polygon([A, C, H, K])

    # Triangles ABC, EBF, HKL (HLK)
    model.set_polygon([A, B, C])
    model.set_polygon([E, B, F])
    model.set_polygon([H, K, L])

    # Four equal quadrilaterals ADGC, EDGF, ABLK, HLBC
    model.set_polygon([A, D, G, C])
    model.set_polygon([E, D, G, F])
    model.set_polygon([A, B, L, K])
    model.set_polygon([H, L, B, C])

    # Two equal hexagons ADEFGC and ABCHLK
    model.set_polygon([A, D, E, F, G, C])
    model.set_polygon([A, B, C, H, L, K])

    # Segments
    for p1, p2 in [
        (A, D), (D, E), (E, B), (A, B),
        (B, C), (C, G), (G, F), (F, B),
        (A, C), (C, H), (H, K), (K, A),
        (K, L), (L, H), (E, F),
        (D, G), (D, B), (B, G), (B, L),
    ]:
        model.set_segment(p1, p2)

    # Angles bisected by DB, BG
    model.set_wedge(B, A, A, E)  # < A B E )
    model.set_wedge(B, C, C, F)  # < C B F )

    return model


if __name__ == "__main__":
    construct_0379_g2()
