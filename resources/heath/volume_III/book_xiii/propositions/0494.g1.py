"""Programmatic construction for Book XIII, Proposition 16 Commentary (0494.g1).

Pappus' inscription of a regular icosahedron in a sphere using four parallel
circular sections ABC, DEF, KGH, LMN, and auxiliary lines x and y.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0494_g1() -> Model:
    """Construct the figure 0494.g1 using geometor.model."""
    model = Model("0494.g1")

    # Sphere centre and boundary point
    O = model.set_point(237.0, -189.0, classes=["auxiliary"], label="O")
    S_top = model.set_point(237.0, -10.5, classes=["auxiliary"], label="S_top")
    model.construct_circle(O, S_top)

    # Auxiliary segments x and y on the left
    x_top = model.set_point(15.0, -40.0, classes=["auxiliary"], label="x_top")
    x_bot = model.set_point(15.0, -340.0, classes=["auxiliary"], label="x")
    y_top = model.set_point(35.0, -94.0, classes=["auxiliary"], label="y_top")
    y_bot = model.set_point(35.0, -291.0, classes=["auxiliary"], label="y")
    model.set_segment(x_top, x_bot)
    model.set_segment(y_top, y_bot)

    # Top circular section ABC
    A = model.set_point(147.0, -73.0, classes=["given"], label="A")
    B = model.set_point(226.0, -27.0, classes=["given"], label="B")
    C = model.set_point(327.0, -72.0, classes=["given"], label="C")

    # Upper middle circular section DEF
    D = model.set_point(204.0, -196.0, classes=["given"], label="D")
    E = model.set_point(95.0, -131.0, classes=["given"], label="E")
    F = model.set_point(391.0, -132.0, classes=["given"], label="F")

    # Lower middle circular section KGH
    G = model.set_point(269.0, -184.0, classes=["given"], label="G")
    H = model.set_point(380.0, -251.0, classes=["given"], label="H")
    K = model.set_point(86.0, -250.0, classes=["given"], label="K")

    # Bottom circular section LMN
    L = model.set_point(136.0, -307.0, classes=["given"], label="L")
    M = model.set_point(326.0, -302.0, classes=["given"], label="M")
    N = model.set_point(241.0, -351.0, classes=["given"], label="N")

    # Polygons (Pentagons and Triangles)
    model.set_polygon([A, C, F, G, E])
    model.set_polygon([K, E, B, C, D])
    model.set_polygon([D, H, F, B, A])
    model.set_polygon([A, K, L, G, B])
    model.set_polygon([A, K, N, H, C])
    model.set_polygon([C, H, M, G, B])
    model.set_polygon([L, K, D, H, M])
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([K, G, H])
    model.set_polygon([L, M, N])

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, A),
        (D, E), (E, F), (F, D),
        (K, G), (G, H), (H, K),
        (L, M), (M, N), (N, L),
        (B, E), (B, F), (B, G),
        (A, E), (A, D), (A, K),
        (C, D), (C, F), (C, H),
        (E, K), (E, G), (E, L),
        (F, G), (F, H), (F, M),
        (D, K), (D, H), (D, N),
        (K, L), (K, N),
        (H, M), (H, N),
        (G, L), (G, M),
        (F, K),
    ]:
        model.set_segment(p1, p2)

    # Right angle FEK
    model.set_wedge(E, F, F, K)

    return model


if __name__ == "__main__":
    construct_0494_g1()
