"""Programmatic construction for Book X, Proposition 2 commentary (0022.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0022_g1() -> Model:
    """Construct the extreme and mean ratio line DB for 0022.g1."""
    model = Model("0022.g1")

    # Collinear points D, A, C, B along DB
    D = model.set_point(15.0, -22.5, classes=["given"], label="D")
    A = model.set_point(75.0, -22.5, label="A")
    C = model.set_point(136.0, -22.5, label="C")
    B = model.set_point(175.0, -22.5, classes=["given"], label="B")

    # Base line DB
    model.construct_line(D, B)

    # Segments and sub-segments
    model.set_segment(D, A)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_segment(D, C)
    model.set_segment(A, B)
    model.set_segment(D, B)

    # Collinear sections
    model.set_section([D, A, C])
    model.set_section([A, C, B])
    model.set_section([D, A, B])

    return model


if __name__ == "__main__":
    construct_0022_g1()
