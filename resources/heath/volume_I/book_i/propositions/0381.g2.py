"""Programmatic construction for Proposition 47 Commentary (0381.g2).

Heron's third lemma (converse of Book I, Proposition 43).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0381_g2() -> Model:
    """Construct Heron's third lemma (0381.g2) using geometor.model."""
    model = Model("0381.g2")

    A = model.set_point(36, -31, classes=["given"], label="A")
    TR = model.set_point(170, -31, label="TR")
    B = model.set_point(144, -116, classes=["given"], label="B")
    BL = model.set_point(10, -116, label="BL")

    D = model.set_point(73.84, -31, label="D")
    E = model.set_point(28.66, -55, label="E")
    G = model.set_point(66.49, -55, label="G")
    F = model.set_point(162.66, -55, label="F")
    C = model.set_point(47.84, -116, label="C")

    K = model.set_point(51.25, -43, label="K")
    H = model.set_point(105.25, -85.5, label="H")

    # Polygons
    model.set_polygon([A, TR, B, BL])  # Parallelogram AB
    model.set_polygon([A, D, G, E])    # ADGE
    model.set_polygon([D, TR, F, G])   # DF
    model.set_polygon([E, G, C, BL])   # CE / EC
    model.set_polygon([F, G, C, B])    # FGCB
    model.set_polygon([D, G, F])
    model.set_polygon([E, C, G])
    model.set_polygon([G, C, F])
    model.set_polygon([E, C, F])
    model.set_polygon([D, C, F])
    model.set_polygon([A, K, E])
    model.set_polygon([G, K, D])
    model.set_polygon([F, H, B])
    model.set_polygon([C, H, G])

    # Segments
    for p1, p2 in [
        (A, TR), (TR, B), (B, BL), (BL, A),
        (E, F), (D, C),
        (E, D), (E, K), (K, D),
        (C, F), (C, H), (H, F),
        (D, F), (E, C),
        (A, B), (A, G), (A, H), (H, B),
        (B, F), (G, C),
    ]:
        model.set_segment(p1, p2)

    # Angles
    model.set_wedge(F, B, B, H)  # < B F H )
    model.set_wedge(C, G, G, H)  # < G C H )
    model.set_wedge(H, B, B, F)  # < B H F )
    model.set_wedge(H, G, G, C)  # < G H C ) / < C H G )
    model.set_wedge(H, G, G, F)  # < G H F ) / < F H G )

    return model


if __name__ == "__main__":
    construct_0381_g2()
