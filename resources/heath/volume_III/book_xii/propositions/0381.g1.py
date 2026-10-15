"""Programmatic construction for Book XII, Proposition 2 Commentary (0381.g1).

Two concentric circles with center C and radii CA, CB, tangent DE at A,
inscribed side MN in outer circle, and circumscribed side PQ about inner circle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0381_g1() -> Model:
    """Construct the figure 0381.g1 using geometor.model."""
    model = Model("0381.g1")

    # Center C and radial points A (inner) and B (outer)
    C = model.set_point(114.0, -128.0, classes=["given"], label="C")
    A = model.set_point(114.0, -47.0, classes=["given"], label="A")
    B = model.set_point(114.0, -36.0, classes=["given"], label="B")

    # Tangent DE at A meeting outer circle in D and E
    D = model.set_point(70.38, -47.0, label="D")
    E = model.set_point(157.62, -47.0, label="E")

    # Chord MN on outer circle and intersections P, Q of CM, CN with DE
    M = model.set_point(81.85, -41.8, label="M")
    N = model.set_point(146.15, -41.8, label="N")
    P = model.set_point(83.79, -47.0, label="P")
    Q = model.set_point(144.21, -47.0, label="Q")

    # Concentric circles
    model.construct_circle(C, A)
    model.construct_circle(C, B)

    # Segments
    for p1, p2 in [
        (C, B), (C, A), (A, B),
        (D, E), (D, P), (P, A), (A, Q), (Q, E), (P, Q),
        (M, N),
        (C, M), (C, P), (P, M),
        (C, N), (C, Q), (Q, N),
    ]:
        model.set_segment(p1, p2)

    # Polygons
    model.set_polygon([C, M, N])
    model.set_polygon([C, P, Q])

    return model


if __name__ == "__main__":
    construct_0381_g1()
