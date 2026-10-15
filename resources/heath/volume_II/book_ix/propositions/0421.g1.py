"""Programmatic construction for Book IX, Proposition 25 (0421.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0421_g1() -> Model:
    """Construct the figure 0421.g1 using geometor.model."""
    model = Model("0421.g1")

    # Horizontal number segment AB divided at C and D
    A = model.set_point(13.0, -30.0, classes=["given"], label="A")
    C = model.set_point(161.0, -30.0, label="C")
    D = model.set_point(178.0, -30.0, label="D")
    B = model.set_point(211.0, -30.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(C, D)
    model.set_segment(C, B)
    model.set_segment(D, B)

    # Collinear sections
    model.set_section([A, C, B])
    model.set_section([A, D, B])
    model.set_section([C, D, B])

    return model


if __name__ == "__main__":
    construct_0421_g1()
