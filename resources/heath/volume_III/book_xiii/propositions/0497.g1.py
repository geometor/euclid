"""Programmatic construction for Book XIII, Proposition 17 (0497.g1).

Euclid's construction of the regular dodecahedron on two adjacent faces ABCD
and CBEF of a cube, showing the pentagonal face UBWCV (BUVCW) and sphere centre Z.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0497_g1() -> Model:
    """Construct the figure 0497.g1 using geometor.model."""
    model = Model("0497.g1")

    # Cube face ABCD and midpoints G, H, K, L, Q
    B = model.set_point(25.0, -140.5, classes=["given"], label="B")
    C = model.set_point(255.0, -140.5, classes=["given"], label="C")
    D = model.set_point(255.0, -372.0, classes=["given"], label="D")
    A = model.set_point(25.0, -372.0, classes=["given"], label="A")

    G = model.set_point(25.0, -255.5, classes=["constructed"], label="G")
    H = model.set_point(140.0, -140.5, classes=["constructed"], label="H")
    K = model.set_point(255.0, -255.5, classes=["constructed"], label="K")
    L = model.set_point(140.0, -372.0, classes=["constructed"], label="L")
    Q = model.set_point(140.0, -255.5, classes=["constructed"], label="Q")

    # Cube face CBEF and midpoints M, N, O, P
    E = model.set_point(55.5, -50.5, classes=["given"], label="E")
    F = model.set_point(288.5, -50.5, classes=["given"], label="F")
    M = model.set_point(172.0, -50.5, classes=["constructed"], label="M")
    N = model.set_point(40.0, -95.5, classes=["constructed"], label="N")
    O = model.set_point(272.0, -95.5, classes=["constructed"], label="O")
    P = model.set_point(157.0, -95.5, classes=["constructed"], label="P")

    # Extreme and mean ratio division points R, S, T and elevated vertices U, V, W, X, Z
    R = model.set_point(85.0, -95.5, classes=["constructed"], label="R")
    S = model.set_point(231.0, -95.5, classes=["constructed"], label="S")
    T = model.set_point(140.0, -183.0, classes=["constructed"], label="T")

    U = model.set_point(85.0, -23.0, classes=["constructed"], label="U")
    X = model.set_point(157.0, -23.0, classes=["constructed"], label="X")
    V = model.set_point(231.0, -23.0, classes=["constructed"], label="V")
    W = model.set_point(129.5, -211.0, classes=["constructed"], label="W")
    Z = model.set_point(157.0, -210.0, classes=["constructed"], label="Z")

    # Polygons (Cube faces ABCD, CBEF, Pentagon UBWCV, Triangles XPH, HTW)
    model.set_polygon([A, B, C, D])
    model.set_polygon([C, B, E, F])
    model.set_polygon([U, B, W, C, V])
    model.set_polygon([X, P, H])
    model.set_polygon([H, T, W])

    # Segments and Sub-segments
    for p1, p2 in [
        (A, B), (A, G), (G, B),
        (B, C), (B, H), (H, C),
        (C, D), (C, K), (K, D),
        (D, A), (D, L), (L, A),
        (E, F), (E, M), (M, F),
        (E, B), (E, N), (N, B),
        (F, C), (F, O), (O, C),
        (G, K), (G, Q), (Q, K),
        (H, L), (H, Q), (Q, L), (H, T), (T, Q),
        (M, H), (M, P), (P, H),
        (N, O), (N, P), (P, O), (N, R), (R, P), (P, S), (S, O), (R, S), (N, S),
        (R, U), (S, V), (T, W), (P, X),
        (U, B), (B, W), (W, C), (C, V), (V, U), (U, X), (X, V),
        (R, B), (S, B), (V, B),
        (X, H), (H, W), (X, W),
        (X, Z), (P, Z), (U, Z),
    ]:
        model.set_segment(p1, p2)

    # Angles VSB, BUV, BWC, UVC
    model.set_wedge(S, V, V, B)
    model.set_wedge(U, B, B, V)
    model.set_wedge(W, B, B, C)
    model.set_wedge(V, U, U, C)

    return model


if __name__ == "__main__":
    construct_0497_g1()
