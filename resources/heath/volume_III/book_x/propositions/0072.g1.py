"""Programmatic construction for Book X, Proposition 30 (0072.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0072_g1() -> Model:
    """Construct the figure 0072.g1 using geometor.model."""
    model = Model("0072.g1")

    # Diameter AB, center O, and point F on semicircle AFB
    A = model.set_point(19.0, -111.5, classes=["given"], label="A")
    B = model.set_point(224.0, -111.5, classes=["given"], label="B")
    O = model.set_point(121.5, -111.5, label="O")
    F = model.set_point(91.5, -13.5, label="F")

    # Number line CD divided at E
    C = model.set_point(46.0, -139.5, classes=["given"], label="C")
    E = model.set_point(92.0, -139.5, label="E")
    D = model.set_point(178.0, -139.5, classes=["given"], label="D")

    # Base lines and circle (semicircle AFB)
    model.construct_line(A, B)
    model.construct_circle(O, A)
    model.construct_line(A, F)
    model.construct_line(F, B)
    model.construct_line(C, D)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(C, D)
    model.set_segment(C, E)
    model.set_segment(E, D)
    model.set_section([C, E, D])

    # Inscribed right triangle AFB and right angle at F
    model.set_polygon([A, F, B])
    model.set_wedge(F, A, A, B)

    return model


if __name__ == "__main__":
    construct_0072_g1()
