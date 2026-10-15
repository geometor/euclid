"""Programmatic construction for Proposition 47 Commentary (0381.g1).

Heron's first and second lemmas for the concurrency of the perpendicular and
diagonals in Book I, Proposition 47.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0381_g1() -> Model:
    """Construct Heron's first and second lemmas (0381.g1) using geometor.model."""
    model = Model("0381.g1")

    A = model.set_point(100, -62, classes=["given"], label="A")
    B = model.set_point(20, -140, classes=["given"], label="B")
    C = model.set_point(156, -140, classes=["given"], label="C")
    F = model.set_point(88, -140, label="F")

    D = model.set_point(50.77, -110, label="D")
    G = model.set_point(92.62, -110, label="G")
    E = model.set_point(134.46, -110, label="E")

    H = model.set_point(58.15, -62, label="H")
    K = model.set_point(141.85, -62, label="K")
    L = model.set_point(46.15, -140, label="L")
    M = model.set_point(129.85, -140, label="M")

    # Second lemma upper extension points
    Dp = model.set_point(140, -23, label="D'")
    Gp = model.set_point(106, -23, label="G'")
    Ep = model.set_point(72, -23, label="E'")

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, F])
    model.set_polygon([A, F, C])
    model.set_polygon([D, B, F])
    model.set_polygon([E, F, C])
    model.set_polygon([A, D, F])
    model.set_polygon([A, E, F])
    model.set_polygon([A, H, L, F])  # AL
    model.set_polygon([A, K, M, F])  # AM

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (B, C),
        (A, F), (A, G), (G, F),
        (D, E), (D, G), (G, E),
        (H, K), (H, A), (A, K),
        (H, L), (H, D), (D, L),
        (K, M), (K, E), (E, M),
        (L, M), (L, F), (F, M),
        (D, F), (E, F),
        (A, Dp), (A, Ep), (A, Gp), (Ep, Dp),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0381_g1()
