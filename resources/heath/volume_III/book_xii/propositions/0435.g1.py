"""Programmatic construction for Book XII, Proposition 17 Commentary (0435.g1).

Heath's perspective diagram of the octant O-ABE of two concentric spheres with
center A, showing quadrants BE, GF, BO, KO, facets BPSK, PQTS, QRUT, ORU, and
perpendiculars PV, SW, KZ, AX.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0435_g1() -> Model:
    """Construct the figure 0435.g1 using geometor.model."""
    model = Model("0435.g1")

    A = model.set_point(265.0, -273.0, classes=["given"], label="A")
    O = model.set_point(265.0, -28.5, classes=["given"], label="O")
    B = model.set_point(20.5, -273.0, classes=["given"], label="B")
    D = model.set_point(509.5, -273.0, classes=["given"], label="D")

    # Inner quadrant GF
    G = model.set_point(104.0, -273.0, classes=["given"], label="G")
    F = model.set_point(309.0, -370.0, classes=["given"], label="F")

    # Quadrant BE points
    K = model.set_point(75.0, -350.0, classes=["given"], label="K")
    L = model.set_point(155.0, -391.0, classes=["given"], label="L")
    M = model.set_point(242.0, -411.0, classes=["given"], label="M")
    E = model.set_point(331.0, -419.0, classes=["given"], label="E")

    # Quadrant BO points
    P = model.set_point(38.0, -181.0, classes=["given"], label="P")
    Q = model.set_point(92.1, -100.1, classes=["given"], label="Q")
    R = model.set_point(173.0, -46.5, classes=["given"], label="R")

    # Quadrant KO points
    S = model.set_point(82.0, -222.0, classes=["given"], label="S")
    T = model.set_point(125.0, -128.0, classes=["given"], label="T")
    U = model.set_point(185.0, -65.0, classes=["given"], label="U")

    # Auxiliary points Z, V, W, X
    Z = model.set_point(38.0, -273.0, classes=["given"], label="Z")
    V = model.set_point(46.0, -273.0, classes=["given"], label="V")
    W = model.set_point(90.0, -344.0, classes=["given"], label="W")
    X = model.set_point(56.0, -258.0, classes=["given"], label="X")
    X2 = model.set_point(82.0, -155.0, label="X2")

    # Circles
    model.construct_circle(A, B)
    model.construct_circle(A, G)

    # Segments
    for p1, p2 in [
        (A, O), (B, D), (A, B), (A, D), (A, E), (A, F), (A, G), (A, K),
        (B, Z), (Z, V), (V, G), (G, A), (B, V), (A, Z), (A, V), (D, Z),
        (K, W), (W, A),
        (B, K), (K, L), (L, M), (M, E),
        (B, P), (P, Q), (Q, R), (R, O),
        (K, S), (S, T), (T, U), (U, O),
        (P, S), (Q, T), (R, U),
        (P, V), (P, Z), (S, W), (V, W), (Z, W), (K, Z), (K, V), (K, D),
        (A, P), (A, S),
        (A, X), (B, X), (K, X), (P, X), (S, X),
        (A, X2), (P, X2), (S, X2), (Q, X2), (T, X2),
    ]:
        model.set_segment(p1, p2)

    # Facets and triangles
    model.set_polygon([B, P, S, K])
    model.set_polygon([P, Q, T, S])
    model.set_polygon([Q, R, U, T])
    model.set_polygon([O, R, U])
    model.set_polygon([P, A, V])
    model.set_polygon([S, A, W])
    model.set_polygon([A, B, E])
    model.set_polygon([O, A, B])

    # Angles
    model.set_wedge(A, P, P, V)
    model.set_wedge(A, S, S, W)
    model.set_wedge(V, P, P, A)
    model.set_wedge(W, S, S, A)
    model.set_wedge(X, B, B, K)

    return model


if __name__ == "__main__":
    construct_0435_g1()
