"""Programmatic construction for Book XIII, Proposition 16 (0485.g1).

Euclid's construction of the regular icosahedron inscribed in a sphere of
diameter AB, showing the semicircle ADB (with AC = 4 CB) and the plan projection
of the circular section EFGHK (centre V), regular pentagons EFGHK, LMNOP, QRSTU,
and axis XZ with points V, A', W.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0485_g1() -> Model:
    """Construct the figure 0485.g1 using geometor.model."""
    model = Model("0485.g1")

    # Right sub-figure: Sphere diameter AB divided at C (AC = 4 CB) and semicircle ADB
    A = model.set_point(504.0, -28.0, classes=["given"], label="A")
    B = model.set_point(504.0, -333.0, classes=["given"], label="B")
    C = model.set_point(504.0, -271.0, classes=["constructed"], label="C")
    D = model.set_point(629.0, -271.0, classes=["constructed"], label="D")
    O_ab = model.set_point(504.0, -180.5, classes=["auxiliary"], label="O_ab")
    model.construct_circle(O_ab, A)

    # Left sub-figure: Centre V and concentric projection circles
    cx, cy = 216.0, -216.0
    r_in, r_out = 136.5, 206.0
    V = model.set_point(cx, cy, classes=["given"], label="V")

    # 10 vertices on inner circle EFGHK / LMNOP
    in_labels = ["L", "E", "P", "K", "O", "H", "N", "G", "M", "F"]
    in_pts = {}
    for i, name in enumerate(in_labels):
        ang = math.radians(-90.0 + i * 36.0)
        x = round(cx + r_in * math.cos(ang), 1)
        y = round(cy - r_in * math.sin(ang), 1)
        in_pts[name] = model.set_point(x, y, classes=["constructed"], label=name)

    L, E, P, K, O, H, N, G, M, F = (in_pts[k] for k in in_labels)
    model.construct_circle(V, L)

    # 5 vertices on outer circle QRSTU
    out_specs = [("Q", -54.0), ("U", 18.0), ("T", 90.0), ("S", 162.0), ("R", -126.0)]
    out_pts = {}
    for name, deg in out_specs:
        ang = math.radians(deg)
        x = round(cx + r_out * math.cos(ang), 1)
        y = round(cy - r_out * math.sin(ang), 1)
        out_pts[name] = model.set_point(x, y, classes=["constructed"], label=name)

    Q, U, T, S, R = (out_pts[k] for k, _ in out_specs)
    model.construct_circle(V, T)

    # Axis points X, A', W, Z
    X = model.set_point(180.0, -249.0, classes=["constructed"], label="X")
    A_prime = model.set_point(238.0, -195.8, classes=["constructed"], label="A'")
    W = model.set_point(260.0, -175.7, classes=["constructed"], label="W")
    Z = model.set_point(289.0, -149.1, classes=["constructed"], label="Z")

    # Polygons (Pentagons and Equilateral Triangles)
    model.set_polygon([E, F, G, H, K])
    model.set_polygon([L, M, N, O, P])
    model.set_polygon([Q, R, S, T, U])
    for tri in [
        (Q, P, U), (Q, L, R), (R, M, S), (S, N, T), (T, O, U),
        (Q, L, P), (L, R, M), (M, S, N), (N, T, O), (O, U, P),
        (Q, U, Z), (L, M, X), (X, E, Z), (V, E, Z),
    ]:
        model.set_polygon(list(tri))

    # Segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (D, B),
        (E, F), (F, G), (G, H), (H, K), (K, E),
        (L, M), (M, N), (N, O), (O, P), (P, L),
        (E, P), (P, K), (K, O), (O, H), (H, N), (N, G), (G, M), (M, F), (F, L), (L, E),
        (Q, R), (R, S), (S, T), (T, U), (U, Q),
        (E, Q), (F, R), (G, S), (H, T), (K, U),
        (Q, L), (L, R), (R, M), (M, S), (S, N), (N, T), (T, O), (O, U), (U, P), (P, Q),
        (V, E), (V, F), (V, L), (V, M), (V, K),
        (X, Z), (V, Z), (V, X), (V, W), (W, Z), (X, W),
        (V, A_prime), (A_prime, W), (Z, A_prime),
        (Q, Z), (Q, W), (U, Z), (W, U), (L, X), (X, M), (E, Z), (Q, X),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0485_g1()
