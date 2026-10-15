"""Programmatic construction for Book XIII, Proposition 16 Commentary (0491.g1).

Heath's 3D perspective diagram of Euclid's icosahedron construction, showing the
parallel circular sections QRSTU (centre W) and EFGHK / LMNOP (centre V), poles
Z and X along axis XZ, and the semicircle ADB (with AC = 4 CB).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0491_g1() -> Model:
    """Construct the figure 0491.g1 using geometor.model."""
    model = Model("0491.g1")

    # Right sub-figure: Sphere diameter AB divided at C (AC = 4 CB) and semicircle ADB
    A = model.set_point(403.0, -24.0, classes=["given"], label="A")
    B = model.set_point(403.0, -378.0, classes=["given"], label="B")
    C = model.set_point(403.0, -308.0, classes=["constructed"], label="C")
    D = model.set_point(544.0, -308.0, classes=["constructed"], label="D")
    O_ab = model.set_point(403.0, -201.0, classes=["auxiliary"], label="O_ab")
    model.construct_circle(O_ab, A)

    # Left sub-figure: Axis XZ with centres W, V and midpoint A'
    Z = model.set_point(168.0, -12.0, classes=["constructed"], label="Z")
    W = model.set_point(168.0, -118.0, classes=["constructed"], label="W")
    A_prime = model.set_point(168.0, -197.0, classes=["constructed"], label="A'")
    V = model.set_point(168.0, -276.0, classes=["given"], label="V")
    X = model.set_point(168.0, -386.0, classes=["constructed"], label="X")

    # Upper circular section QRSTU
    S = model.set_point(28.0, -102.0, classes=["constructed"], label="S")
    R = model.set_point(177.0, -84.0, classes=["constructed"], label="R")
    Q = model.set_point(314.0, -105.0, classes=["constructed"], label="Q")
    U = model.set_point(226.0, -150.0, classes=["constructed"], label="U")
    T = model.set_point(77.0, -150.0, classes=["constructed"], label="T")

    # Lower circular section EFGHK and LMNOP
    G = model.set_point(28.0, -260.0, classes=["constructed"], label="G")
    F = model.set_point(177.0, -242.0, classes=["constructed"], label="F")
    E = model.set_point(314.0, -263.0, classes=["constructed"], label="E")
    K = model.set_point(226.0, -308.0, classes=["constructed"], label="K")
    H = model.set_point(77.0, -308.0, classes=["constructed"], label="H")

    N = model.set_point(21.0, -290.0, classes=["constructed"], label="N")
    M = model.set_point(95.0, -245.0, classes=["constructed"], label="M")
    L = model.set_point(248.0, -245.0, classes=["constructed"], label="L")
    P = model.set_point(292.0, -295.0, classes=["constructed"], label="P")
    O = model.set_point(149.0, -310.0, classes=["constructed"], label="O")

    # Polygons (Pentagons and Triangles)
    model.set_polygon([E, F, G, H, K])
    model.set_polygon([L, M, N, O, P])
    model.set_polygon([Q, R, S, T, U])
    model.set_polygon([Q, P, L])

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (B, D),
        (E, F), (F, G), (G, H), (H, K), (K, E),
        (L, M), (M, N), (N, O), (O, P), (P, L),
        (E, L), (L, F), (F, M), (M, G), (G, N), (N, H), (H, O), (O, K), (K, P), (P, E),
        (Q, R), (R, S), (S, T), (T, U), (U, Q),
        (E, Q), (F, R), (G, S), (H, T), (K, U),
        (Q, L), (L, R), (R, M), (M, S), (S, N), (N, T), (T, O), (O, U), (U, P), (P, Q),
        (Z, Q), (Z, R), (Z, S), (Z, T), (Z, U),
        (X, L), (X, M), (X, N), (X, O), (X, P),
        (X, Z), (V, Z), (V, W), (V, X), (W, Z), (A_prime, Z), (A_prime, W),
        (V, E), (W, Q),
    ]:
        model.set_segment(p1, p2)

    # Right angle ZWQ
    model.set_wedge(W, Z, Z, Q)

    return model


if __name__ == "__main__":
    construct_0491_g1()
