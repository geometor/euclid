"""Programmatic construction for Book XI, Proposition 2 Commentary (0279.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0279_g1() -> Model:
    """Construct the figure 0279.g1 using geometor.model."""
    model = Model("0279.g1")

    # Endpoints of the three straight lines PQ, RS, XY
    P = model.set_point(189.0, -22.0, classes=["given"], label="P")
    Q = model.set_point(27.0, -172.0, classes=["given"], label="Q")
    R = model.set_point(135.0, -22.0, classes=["given"], label="R")
    S = model.set_point(209.0, -178.0, classes=["given"], label="S")
    X = model.set_point(24.0, -132.0, classes=["given"], label="X")
    Y = model.set_point(226.0, -132.0, classes=["given"], label="Y")

    # Pairwise intersection points A, B, C
    A = model.set_point(151.48, -56.74, label="A")
    B = model.set_point(70.2, -132.0, label="B")
    C = model.set_point(187.18, -132.0, label="C")

    # Construction lines
    model.construct_line(P, Q)
    model.construct_line(R, S)
    model.construct_line(X, Y)

    # Segments
    model.set_segment(P, Q)
    model.set_segment(R, S)
    model.set_segment(X, Y)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(P, A)
    model.set_segment(B, Q)
    model.set_segment(R, A)
    model.set_segment(C, S)
    model.set_segment(X, B)
    model.set_segment(C, Y)

    # Triangle ABC
    model.set_polygon([A, B, C])

    return model


if __name__ == "__main__":
    construct_0279_g1()
