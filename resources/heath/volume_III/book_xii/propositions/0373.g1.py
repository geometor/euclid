"""Programmatic construction for Book XII, Proposition 1 (0373.g1).

Similar polygons ABCDE and FGHKL inscribed in circles ABC and FGH with
diameters BM and GN.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0373_g1() -> Model:
    """Construct the figure 0373.g1 using geometor.model."""
    model = Model("0373.g1")

    # Left circle ABC (center O1 = (114, -111), radius 88)
    O1 = model.set_point(114.0, -111.0, label="O1")
    A = model.set_point(108.0, -23.2, classes=["given"], label="A")
    B = model.set_point(28.5, -90.0, classes=["given"], label="B")
    C = model.set_point(81.0, -192.6, classes=["given"], label="C")
    D = model.set_point(186.0, -161.6, classes=["given"], label="D")
    E = model.set_point(199.3, -89.2, classes=["given"], label="E")
    M = model.set_point(199.5, -132.0, label="M")

    # Right circle FGH (center O2 = (370, -113), radius 70)
    O2 = model.set_point(370.0, -113.0, label="O2")
    F = model.set_point(365.2, -43.2, classes=["given"], label="F")
    G = model.set_point(302.0, -96.3, classes=["given"], label="G")
    H = model.set_point(343.8, -177.9, classes=["given"], label="H")
    K = model.set_point(427.3, -153.2, classes=["given"], label="K")
    L = model.set_point(437.8, -95.6, classes=["given"], label="L")
    N = model.set_point(438.0, -129.7, label="N")

    # Circles
    model.construct_circle(O1, A)
    model.construct_circle(O2, F)

    # Left segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A),
        (B, E), (B, M), (A, M),
    ]:
        model.set_segment(p1, p2)

    # Right segments
    for p1, p2 in [
        (F, G), (G, H), (H, K), (K, L), (L, F),
        (G, L), (G, N), (F, N),
    ]:
        model.set_segment(p1, p2)

    # Polygons and triangles
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, G, H, K, L])
    model.set_polygon([A, B, E])
    model.set_polygon([F, G, L])
    model.set_polygon([A, B, M])
    model.set_polygon([F, G, N])

    # Angles (wedges)
    model.set_wedge(A, B, B, E)
    model.set_wedge(F, G, G, L)
    model.set_wedge(E, A, A, B)
    model.set_wedge(L, F, F, G)
    model.set_wedge(M, A, A, B)
    model.set_wedge(N, F, F, G)
    model.set_wedge(A, B, B, M)
    model.set_wedge(F, G, G, N)

    return model


if __name__ == "__main__":
    construct_0373_g1()
