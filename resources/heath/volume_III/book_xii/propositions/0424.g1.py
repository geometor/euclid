"""Programmatic construction for Book XII, Proposition 15 (0424.g1).

Equal cones and cylinders with circular bases ABCD (diameter AC, axis KL,
cylinder AO) and EFGH (diameter EG, axis MN cut at Q by plane TUS, cylinder EP
and partial cylinder ES).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0424_g1() -> Model:
    """Construct the figure 0424.g1 using geometor.model."""
    model = Model("0424.g1")

    # Left vertical cylinder AO and cone ABCD-L
    L = model.set_point(89.0, -34.0, classes=["given"], label="L")
    A2 = model.set_point(31.0, -34.0, label="A2")
    O = model.set_point(147.0, -34.0, classes=["given"], label="O")
    K = model.set_point(89.0, -134.0, classes=["given"], label="K")
    A = model.set_point(31.0, -134.0, classes=["given"], label="A")
    C = model.set_point(147.0, -134.0, classes=["given"], label="C")
    D = model.set_point(72.0, -118.7, classes=["given"], label="D")
    B = model.set_point(106.0, -149.3, classes=["given"], label="B")

    # Right horizontal cylinder EP and cones with vertex M
    M = model.set_point(206.0, -80.0, classes=["given"], label="M")
    P = model.set_point(206.0, -42.0, classes=["given"], label="P")
    R = model.set_point(206.0, -118.0, classes=["given"], label="R")

    Q = model.set_point(338.0, -80.0, classes=["given"], label="Q")
    S = model.set_point(338.0, -42.0, classes=["given"], label="S")
    U = model.set_point(338.0, -118.0, classes=["given"], label="U")
    T = model.set_point(350.0, -80.0, classes=["given"], label="T")

    N = model.set_point(434.0, -80.0, classes=["given"], label="N")
    G = model.set_point(434.0, -42.0, classes=["given"], label="G")
    E = model.set_point(434.0, -118.0, classes=["given"], label="E")
    F = model.set_point(446.0, -80.0, classes=["given"], label="F")
    H = model.set_point(422.0, -80.0, classes=["given"], label="H")

    # Circular bases and sections
    for center, rim in [
        (L, O), (K, C), (M, P), (Q, S), (N, G),
    ]:
        model.construct_circle(center, rim)

    # Segments
    for p1, p2 in [
        (A2, A), (O, C), (L, K), (A, C), (A, K), (K, C),
        (L, A), (L, C),
        (P, S), (S, G), (P, G),
        (R, U), (U, E), (R, E),
        (M, Q), (Q, N), (M, N),
        (S, U), (G, E),
        (M, S), (M, U), (M, G), (M, E),
    ]:
        model.set_segment(p1, p2)

    # Cylinders and cones
    model.set_polygon([A2, A, C, O])  # Cylinder AO
    model.set_polygon([P, R, E, G])   # Cylinder EP
    model.set_polygon([S, U, E, G])   # Cylinder ES
    model.set_polygon([A, C, L])      # Cone ABCD-L
    model.set_polygon([E, G, M])      # Cone EFGH-M

    return model


if __name__ == "__main__":
    construct_0424_g1()
