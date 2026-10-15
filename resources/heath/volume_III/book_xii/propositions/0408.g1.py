"""Programmatic construction for Book XII, Proposition 10 commentary (0408.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0408_g1() -> Model:
    """Construct the figure 0408.g1 using geometor.model."""
    model = Model("0408.g1")

    # Circle center O and top point C
    O = model.set_point(90.0, -92.0)
    C = model.set_point(90.0, -22.0, label="C")

    # Chord endpoints A, B and rectangle corners D, E
    A = model.set_point(52.33, -33.0, classes=["given"], label="A")
    B = model.set_point(127.67, -33.0, classes=["given"], label="B")
    D = model.set_point(52.33, -22.0, label="D")
    E = model.set_point(127.67, -22.0, label="E")

    # Circle
    model.construct_circle(O, C)

    # Segments
    model.set_segment(A, B)
    model.set_segment(D, E)
    model.set_segment(D, C)
    model.set_segment(C, E)
    model.set_segment(A, D)
    model.set_segment(B, E)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Polygons
    model.set_polygon([A, B, E, D])
    model.set_polygon([A, C, B])

    return model


if __name__ == "__main__":
    construct_0408_g1()
