"""Programmatic construction for Book IV, Proposition 10 Commentary (0104.g4)."""

from __future__ import annotations

from geometor.model import Model


def construct_0104_g4() -> Model:
    """Construct the figure 0104.g4 (Regular star-pentagon / pentagram) using geometor.model."""
    model = Model("0104.g4")

    # Vertices of regular star-pentagon (y-inverted)
    A = model.set_point(79.00, -14.00, classes=["given"], label="A")
    B = model.set_point(141.77, -59.60, classes=["given"], label="B")
    C = model.set_point(117.79, -133.40, classes=["given"], label="C")
    D = model.set_point(40.21, -133.40, classes=["given"], label="D")
    E = model.set_point(16.23, -59.60, classes=["given"], label="E")

    # Star diagonals
    model.set_segment(A, C)
    model.set_segment(C, E)
    model.set_segment(E, B)
    model.set_segment(B, D)
    model.set_segment(D, A)

    # Star polygon
    model.set_polygon([A, C, E, B, D])

    return model


if __name__ == "__main__":
    construct_0104_g4()
