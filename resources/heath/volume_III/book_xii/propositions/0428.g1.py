"""Programmatic construction for Book XII, Proposition 16 (0428.g1).

Two concentric circles ABCD and EFGH about center K, with diameter BKD, tangent
chord AGC at G, and chord LMN parallel to AC with inscribed sides LD, DN.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0428_g1() -> Model:
    """Construct the figure 0428.g1 using geometor.model."""
    model = Model("0428.g1")

    K = model.set_point(112.0, -104.0, classes=["given"], label="K")
    B = model.set_point(28.0, -104.0, classes=["given"], label="B")
    D = model.set_point(196.0, -104.0, classes=["given"], label="D")
    E = model.set_point(48.0, -104.0, classes=["given"], label="E")
    G = model.set_point(176.0, -104.0, classes=["given"], label="G")
    H = model.set_point(112.0, -40.0, classes=["given"], label="H")
    F = model.set_point(112.0, -168.0, classes=["given"], label="F")

    A = model.set_point(176.0, -49.4, classes=["given"], label="A")
    C = model.set_point(176.0, -158.6, classes=["given"], label="C")

    M = model.set_point(190.0, -104.0, classes=["given"], label="M")
    L = model.set_point(190.0, -73.1, classes=["given"], label="L")
    N = model.set_point(190.0, -134.9, classes=["given"], label="N")

    # Concentric circles
    model.construct_circle(K, D)
    model.construct_circle(K, G)

    # Segments
    for p1, p2 in [
        (B, E), (E, K), (K, G), (G, M), (M, D),
        (B, K), (K, D), (B, D),
        (A, G), (G, C), (A, C),
        (L, M), (M, N), (L, N),
        (L, D), (D, N),
    ]:
        model.set_segment(p1, p2)

    # Collinear sections
    model.set_section([B, K, D])

    return model


if __name__ == "__main__":
    construct_0428_g1()
