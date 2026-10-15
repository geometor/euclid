"""Programmatic construction for Proposition 47 Commentary (0366.g1).

Isosceles right-angled triangle outward-squares dissection (Cantor & Allman)
and inscribed-square dissection (Bürk / Āpastamba-Śulba-Sūtra).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0366_g1() -> Model:
    """Construct the two figures of 0366.g1 using geometor.model."""
    model = Model("0366.g1")

    # Left Figure: Cantor and Allman outward squares on isosceles right triangle ABC
    A = model.set_point(88, -48, classes=["given"], label="A")
    B = model.set_point(50, -85, classes=["given"], label="B")
    C = model.set_point(126, -85, classes=["given"], label="C")
    D = model.set_point(50, -159, label="D")
    E = model.set_point(126, -159, label="E")
    F = model.set_point(13, -48, label="F")
    G = model.set_point(51, -10, label="G")
    H = model.set_point(125, -10, label="H")
    K = model.set_point(163, -48, label="K")
    M = model.set_point(88, -122, label="M")

    # Polygons (squares and triangles) of Left Figure
    model.set_polygon([A, B, C])
    model.set_polygon([B, D, E, C])
    model.set_polygon([B, A, G, F])
    model.set_polygon([A, C, K, H])
    model.set_polygon([B, C, M])
    model.set_polygon([B, D, M])
    model.set_polygon([D, E, M])
    model.set_polygon([C, E, M])
    model.set_polygon([A, B, F])
    model.set_polygon([A, F, G])
    model.set_polygon([A, C, K])
    model.set_polygon([A, K, H])

    # Segments of Left Figure
    for p1, p2 in [
        (A, B), (B, C), (A, C),
        (B, D), (D, E), (C, E),
        (B, F), (F, G), (G, A),
        (A, H), (H, K), (K, C),
        (F, K), (F, E), (D, K), (C, G), (B, H),
        (B, E), (C, D), (F, A), (A, K),
    ]:
        model.set_segment(p1, p2)

    # Right Figure: Bürk / Āpastamba-Śulba-Sūtra inscribed square
    P = model.set_point(220, -24, classes=["given"], label="P")
    Q = model.set_point(329, -24, classes=["given"], label="Q")
    R = model.set_point(329, -130, classes=["given"], label="R")
    S = model.set_point(220, -130, classes=["given"], label="S")
    T = model.set_point(275, -24, label="T")
    U = model.set_point(329, -77, label="U")
    V = model.set_point(275, -130, label="V")
    W = model.set_point(220, -77, label="W")
    X = model.set_point(275, -77, label="X")

    model.set_polygon([P, Q, R, S])
    model.set_polygon([T, U, V, W])
    model.set_polygon([T, U, X])
    model.set_polygon([U, V, X])
    model.set_polygon([V, W, X])
    model.set_polygon([W, T, X])
    model.set_polygon([P, T, W])
    model.set_polygon([T, Q, U])
    model.set_polygon([U, R, V])
    model.set_polygon([W, V, S])

    for p1, p2 in [
        (P, Q), (Q, R), (R, S), (S, P),
        (T, V), (W, U),
        (T, U), (U, V), (V, W), (W, T),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0366_g1()
