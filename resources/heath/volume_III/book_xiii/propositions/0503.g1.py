"""Programmatic construction for Book XIII, Proposition 17 Commentary (0503.g1).

Heath's 3D perspective diagram of the regular dodecahedron constructed upon
all six faces of the cube, showing pentagonal face BUVCW, adjacent faces, and
sphere centre Z.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0503_g1() -> Model:
    """Construct the figure 0503.g1 using geometor.model."""
    model = Model("0503.g1")

    # Cube face ABCD and midpoints G, H, K, L, Q
    B = model.set_point(75.5, -128.0, classes=["given"], label="B")
    C = model.set_point(308.5, -128.0, classes=["given"], label="C")
    D = model.set_point(308.5, -361.0, classes=["given"], label="D")
    A = model.set_point(75.5, -361.0, classes=["given"], label="A")

    G = model.set_point(75.5, -246.0, classes=["constructed"], label="G")
    H = model.set_point(188.0, -128.0, classes=["constructed"], label="H")
    K = model.set_point(308.5, -246.0, classes=["constructed"], label="K")
    L = model.set_point(188.0, -361.0, classes=["constructed"], label="L")
    Q = model.set_point(188.0, -246.0, classes=["constructed"], label="Q")

    # Cube face CBEF and midpoints M, N, O, P
    E = model.set_point(137.0, -59.0, classes=["given"], label="E")
    F = model.set_point(371.5, -59.0, classes=["given"], label="F")
    M = model.set_point(254.0, -59.0, classes=["constructed"], label="M")
    N = model.set_point(106.0, -93.5, classes=["constructed"], label="N")
    O = model.set_point(340.0, -93.5, classes=["constructed"], label="O")
    P = model.set_point(223.0, -93.5, classes=["constructed"], label="P")

    # Division points R, S, T, cube centre Z, and dodecahedron vertices
    R = model.set_point(150.0, -93.5, classes=["constructed"], label="R")
    S = model.set_point(293.5, -93.5, classes=["constructed"], label="S")
    T = model.set_point(188.0, -173.0, classes=["constructed"], label="T")

    U = model.set_point(150.0, -23.5, classes=["constructed"], label="U")
    X = model.set_point(223.0, -23.5, classes=["constructed"], label="X")
    V = model.set_point(293.5, -23.5, classes=["constructed"], label="V")
    W = model.set_point(166.5, -198.0, classes=["constructed"], label="W")
    Y = model.set_point(166.5, -336.0, classes=["constructed"], label="Y")
    Z = model.set_point(223.0, -209.5, classes=["constructed"], label="Z")

    alpha = model.set_point(16.0, -231.0, classes=["constructed"], label="α")
    beta = model.set_point(59.0, -182.0, classes=["constructed"], label="β")
    alpha_prime = model.set_point(427.0, -187.0, classes=["constructed"], label="α'")
    beta_prime = model.set_point(384.0, -235.0, classes=["constructed"], label="β'")
    v_pt = model.set_point(146.5, -393.5, classes=["constructed"], label="v")
    u_pt = model.set_point(295.0, -393.5, classes=["constructed"], label="u")
    y_pt = model.set_point(276.0, -82.0, classes=["constructed"], label="y")
    w_pt = model.set_point(276.0, -224.0, classes=["constructed"], label="w")

    # Polygons
    model.set_polygon([A, B, C, D])
    model.set_polygon([C, B, E, F])
    model.set_polygon([B, U, V, C, W])
    model.set_polygon([B, W, Y, A, alpha])
    model.set_polygon([C, W, Y, D, beta_prime])
    model.set_polygon([H, P, X])
    model.set_polygon([W, T, H])
    model.set_polygon([U, B, V])
    model.set_polygon([W, B, C])

    # Segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, A),
        (E, F), (E, B), (F, C), (N, B),
        (G, K), (H, L), (M, H), (N, O),
        (N, P), (P, O), (N, R), (R, P), (P, S), (S, O), (R, S), (N, S),
        (H, Q), (H, T), (T, Q), (H, P),
        (R, U), (S, V), (T, W), (P, X),
        (B, U), (U, V), (V, C), (C, W), (W, B), (U, X), (X, V),
        (B, R), (B, S), (B, V),
        (X, H), (H, W), (X, W),
        (Z, X), (Z, P), (Z, U), (Z, B), (Z, V), (Z, W), (P, B),
        (W, Y), (Y, A), (Y, D),
        (B, alpha), (alpha, A), (V, F), (F, alpha_prime), (C, beta_prime), (beta_prime, D),
        (A, v_pt), (v_pt, u_pt), (u_pt, D), (y_pt, w_pt),
    ]:
        model.set_segment(p1, p2)

    # Angles BUV, BWC, CVU
    model.set_wedge(U, B, B, V)
    model.set_wedge(W, B, B, C)
    model.set_wedge(V, C, C, U)

    return model


if __name__ == "__main__":
    construct_0503_g1()
