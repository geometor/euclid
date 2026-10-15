"""Programmatic construction for Book XII, Proposition 3 (0382.g1).

Pyramid ABCD with triangular base ABC and vertex D, bisected along its six
edges at E, F, G, H, K, L into two equal and similar pyramids AEGH, HKLD and
two equal prisms (EBFG, HK) and (GFC, HKL).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0382_g1() -> Model:
    """Construct the figure 0382.g1 using geometor.model."""
    model = Model("0382.g1")

    # Main vertices of pyramid ABCD
    D = model.set_point(128.0, -20.0, classes=["given"], label="D")
    A = model.set_point(24.0, -198.0, classes=["given"], label="A")
    B = model.set_point(210.0, -196.0, classes=["given"], label="B")
    C = model.set_point(100.0, -142.0, classes=["given"], label="C")

    # Midpoints of the 6 edges: E on AB, F on BC, G on CA, H on AD, K on DB, L on DC
    E = model.set_point(117.0, -197.0, label="E")
    F = model.set_point(155.0, -169.0, label="F")
    G = model.set_point(62.0, -170.0, label="G")
    H = model.set_point(76.0, -109.0, label="H")
    K = model.set_point(169.0, -108.0, label="K")
    L = model.set_point(114.0, -81.0, label="L")

    # Segments along main edges and sub-edges
    for p1, p2 in [
        (A, B), (A, E), (E, B),
        (B, C), (B, F), (F, C),
        (C, A), (C, G), (G, A),
        (A, D), (A, H), (H, D),
        (D, B), (D, K), (K, B),
        (D, C), (D, L), (L, C),
        (H, E), (E, G), (G, H),
        (H, K), (K, L), (L, H),
        (K, F), (F, G),
        (E, F), (E, K), (H, F),
    ]:
        model.set_segment(p1, p2)

    # Polygons (faces, bases, parallelograms, and solid outlines)
    for poly in [
        [A, B, C], [A, D, B], [D, B, C], [A, D, C],
        [A, E, H], [H, K, D], [A, H, G], [H, L, D],
        [E, H, G], [K, D, L], [A, E, G], [H, K, L],
        [G, F, C], [B, K, F], [E, B, F],
        [H, E, B, K], [E, B, F, G], [H, K, F, G], [K, F, C, L], [L, C, G, H],
    ]:
        model.set_polygon(poly)

    # Angles
    model.set_wedge(A, E, E, H)
    model.set_wedge(H, K, K, D)
    model.set_wedge(H, E, E, G)
    model.set_wedge(D, K, K, L)
    model.set_wedge(A, B, B, C)
    model.set_wedge(H, K, K, L)

    return model


if __name__ == "__main__":
    construct_0382_g1()
