"""Programmatic construction for Proposition 47 Commentary (0379.g1).

Thābit ibn Qurra's dissection proof of the Pythagorean theorem using two
adjacent squares ABDE (AD) and EFGH (EG) and four congruent right-angled
triangles BAC, CFG, KHG, BDK forming the tilted square BCGK.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0379_g1() -> Model:
    """Construct Thābit ibn Qurra's figure (0379.g1) using geometor.model."""
    model = Model("0379.g1")

    A = model.set_point(211, -238.5, classes=["given"], label="A")
    B = model.set_point(211, -182.5, classes=["given"], label="B")
    C = model.set_point(73, -238.5, classes=["given"], label="C")
    D = model.set_point(154.5, -182.5, label="D")
    E = model.set_point(154.5, -238.5, label="E")
    F = model.set_point(16.5, -238.5, label="F")
    G = model.set_point(16.5, -96.5, label="G")
    H = model.set_point(154.5, -96.5, label="H")
    K = model.set_point(154.5, -41, label="K")
    L = model.set_point(154.5, -205.4, label="L")

    # Polygons: squares ABDE (AD), EFGH (EG), BCGK; triangles BAC, CFG, KHG, BDK;
    # dissection regions GCLH and LDB
    model.set_polygon([A, B, D, E])
    model.set_polygon([E, F, G, H])
    model.set_polygon([B, C, G, K])
    model.set_polygon([B, A, C])
    model.set_polygon([C, F, G])
    model.set_polygon([K, H, G])
    model.set_polygon([B, D, K])
    model.set_polygon([G, C, L, H])
    model.set_polygon([L, D, B])

    # Segments
    for p1, p2 in [
        (F, A), (F, C), (C, E), (E, A), (A, C), (E, F),
        (F, G), (G, H), (K, E), (K, H), (H, D), (D, L), (L, E), (D, E), (D, K),
        (D, B), (B, A),
        (B, C), (C, L), (L, B), (C, G), (G, K), (K, B),
    ]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(B, D, D, K)  # < D B K )
    model.set_wedge(B, A, A, C)  # < A B C )
    model.set_wedge(B, D, D, C)  # < D B C )
    model.set_wedge(B, K, K, C)  # < K B C )
    model.set_wedge(B, A, A, D)  # < A B D )
    model.set_wedge(G, C, C, K)  # < C G K )

    return model


if __name__ == "__main__":
    construct_0379_g1()
