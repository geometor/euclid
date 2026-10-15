"""Programmatic construction for Book IV, Proposition 10 Commentary (0104.g3)."""

from __future__ import annotations

from geometor.model import Model


def construct_0104_g3() -> Model:
    """Construct the figure 0104.g3 (Regular pentagon divided into 30 elementary triangles) using geometor.model."""
    model = Model("0104.g3")

    # Vertices of regular pentagon (y-inverted)
    A = model.set_point(78.00, -16.00, classes=["given"], label="A")
    B = model.set_point(138.87, -60.22, classes=["given"], label="B")
    C = model.set_point(115.62, -131.78, classes=["given"], label="C")
    D = model.set_point(40.38, -131.78, classes=["given"], label="D")
    E = model.set_point(17.13, -60.22, classes=["given"], label="E")

    # Midpoints of opposite sides
    M1 = model.set_point(78.00, -131.78, label="M1")
    M2 = model.set_point(28.76, -96.00, label="M2")
    M3 = model.set_point(47.57, -38.11, label="M3")
    M4 = model.set_point(108.43, -38.11, label="M4")
    M5 = model.set_point(127.24, -96.00, label="M5")
    O = model.set_point(78.00, -80.00, label="O")

    # Pentagon sides
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)

    # Pentagram diagonals
    model.set_segment(A, C)
    model.set_segment(B, D)
    model.set_segment(C, E)
    model.set_segment(D, A)
    model.set_segment(E, B)

    # Medians / axes of symmetry
    model.set_segment(A, M1)
    model.set_segment(B, M2)
    model.set_segment(C, M3)
    model.set_segment(D, M4)
    model.set_segment(E, M5)

    # Pentagon polygon
    model.set_polygon([A, B, C, D, E])

    return model


if __name__ == "__main__":
    construct_0104_g3()
