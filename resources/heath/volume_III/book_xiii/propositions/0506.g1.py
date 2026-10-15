"""Programmatic construction for Book XIII, Proposition 17 Commentary (0506.g1).

Pappus' inscription of a regular dodecahedron in a sphere using four parallel
circular sections ABCDE, FGHKL, MNOPQ, RSTUV, square LCOU, and auxiliary lines x and y.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0506_g1() -> Model:
    """Construct the figure 0506.g1 using geometor.model."""
    model = Model("0506.g1")

    # Sphere centre and boundary point
    O_sph = model.set_point(193.5, -185.0, classes=["auxiliary"], label="O_sph")
    S_top = model.set_point(193.5, -3.5, classes=["auxiliary"], label="S_top")
    model.construct_circle(O_sph, S_top)

    # Auxiliary segments x and y on the right
    x_top = model.set_point(401.5, -38.0, classes=["auxiliary"], label="x_top")
    x_bot = model.set_point(401.5, -343.0, classes=["auxiliary"], label="x")
    y_top = model.set_point(426.5, -95.0, classes=["auxiliary"], label="y_top")
    y_bot = model.set_point(426.5, -291.0, classes=["auxiliary"], label="y")
    model.set_segment(x_top, x_bot)
    model.set_segment(y_top, y_bot)

    # Top circular section ABCDE
    A = model.set_point(122.0, -71.0, classes=["given"], label="A")
    B = model.set_point(247.0, -75.0, classes=["given"], label="B")
    C = model.set_point(305.0, -46.0, classes=["given"], label="C")
    D = model.set_point(224.0, -27.0, classes=["given"], label="D")
    E = model.set_point(112.0, -35.0, classes=["given"], label="E")

    # Upper middle circular section FGHKL
    F = model.set_point(54.0, -132.0, classes=["given"], label="F")
    G = model.set_point(59.0, -188.0, classes=["given"], label="G")
    H = model.set_point(276.0, -195.0, classes=["given"], label="H")
    K = model.set_point(371.0, -151.0, classes=["given"], label="K")
    L = model.set_point(230.0, -111.0, classes=["given"], label="L")

    # Lower middle circular section MNOPQ
    M = model.set_point(108.0, -178.0, classes=["given"], label="M")
    N = model.set_point(327.0, -183.0, classes=["given"], label="N")
    O = model.set_point(352.0, -237.0, classes=["given"], label="O")
    P = model.set_point(177.0, -261.0, classes=["given"], label="P")
    Q = model.set_point(23.0, -219.0, classes=["given"], label="Q")

    # Bottom circular section RSTUV
    R = model.set_point(93.0, -325.0, classes=["given"], label="R")
    S = model.set_point(171.0, -344.0, classes=["given"], label="S")
    T = model.set_point(282.0, -333.0, classes=["given"], label="T")
    U = model.set_point(272.0, -297.0, classes=["given"], label="U")
    V = model.set_point(146.0, -296.0, classes=["given"], label="V")

    # Polygons (Pentagons and Square LCOU)
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([F, G, H, K, L])
    model.set_polygon([M, N, O, P, Q])
    model.set_polygon([R, S, T, U, V])
    model.set_polygon([L, C, O, U])

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A), (A, C),
        (F, G), (G, H), (H, K), (K, L), (L, F),
        (M, N), (N, O), (O, P), (P, Q), (Q, M),
        (R, S), (S, T), (T, U), (U, V), (V, R),
        (E, F), (A, G), (B, H), (C, K), (D, L),
        (F, Q), (G, Q), (G, P), (H, P), (H, O), (K, O), (K, N), (L, N), (L, M), (F, M),
        (Q, R), (P, S), (O, T), (N, U), (M, V),
        (P, A), (L, C), (C, O), (O, U), (U, L), (O, L), (O, F),
    ]:
        model.set_segment(p1, p2)

    # Right angle OLF
    model.set_wedge(L, O, O, F)

    return model


if __name__ == "__main__":
    construct_0506_g1()
