#!/usr/bin/env python3
"""
Programmatic construction for Book XI, Proposition 38 (0365.g1)
using geometor.model.
"""
from geometor.model import Model


def build_model() -> Model:
    m = Model("0365.g1")

    # Top face CDFE (CF) of cube AF
    D = m.set_point(38, 24, classes=["given"], label="D")
    F = m.set_point(242, 24, classes=["given"], label="F")
    E = m.set_point(282, 108, classes=["given"], label="E")
    C = m.set_point(78, 108, classes=["given"], label="C")

    # Bottom face ABHG (AH) of cube AF
    B = m.set_point(38, 248, classes=["given"], label="B")
    H = m.set_point(242, 248, classes=["given"], label="H")
    G = m.set_point(282, 332, classes=["given"], label="G")
    A = m.set_point(78, 332, classes=["given"], label="A")

    # Midpoints of the sides of opposite planes CF, AH
    K = m.set_point(140, 24, classes=["constructed"], label="K")
    L = m.set_point(180, 108, classes=["constructed"], label="L")
    M = m.set_point(140, 248, classes=["constructed"], label="M")
    N = m.set_point(180, 332, classes=["constructed"], label="N")
    O = m.set_point(58, 66, classes=["constructed"], label="O")
    P = m.set_point(262, 66, classes=["constructed"], label="P")
    Q = m.set_point(58, 290, classes=["constructed"], label="Q")
    R = m.set_point(262, 290, classes=["constructed"], label="R")

    # Intersections of bisecting planes and cube diameter DG
    U = m.set_point(160, 66, classes=["constructed"], label="U")
    S = m.set_point(160, 290, classes=["constructed"], label="S")
    T = m.set_point(160, 178, classes=["constructed"], label="T")

    # Polygons (cube, planes, triangles)
    m.set_polygon([D, F, E, G, A, B])  # Cube < A F >
    m.set_polygon([C, D, F, E])        # Plane < C F >
    m.set_polygon([A, B, H, G])        # Plane < A H >
    m.set_polygon([K, L, N, M])        # Plane < K N >
    m.set_polygon([O, P, R, Q])        # Plane < O R >
    m.set_polygon([D, O, U])
    m.set_polygon([P, U, E])
    m.set_polygon([D, T, U])
    m.set_polygon([G, T, S])

    # Segments
    for p1, p2 in [
        (U, S), (U, T), (T, S),
        (D, G), (D, T), (T, G),
        (D, E), (D, U), (U, E),
        (B, G), (B, S), (S, G),
        (D, C), (D, O), (O, C),
        (F, E), (F, P), (P, E),
        (O, P), (O, U), (U, P),
        (C, A), (D, B), (E, G), (F, H),
        (D, F), (D, K), (K, F),
        (C, E), (C, L), (L, E),
        (K, L), (A, B), (M, N), (Q, R),
    ]:
        m.set_segment(p1, p2)

    return m


if __name__ == "__main__":
    model = build_model()
    print(f"Constructed {model.name} with {len(model)} elements.")
