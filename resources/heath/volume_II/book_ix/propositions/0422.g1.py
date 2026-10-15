"""Programmatic construction for Book IX, Proposition 27 (0422.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0422_g1() -> Model:
    """Construct the figure 0422.g1 using geometor.model."""
    model = Model("0422.g1")

    # Horizontal number segment AB divided at D and C
    A = model.set_point(11.0, -29.0, classes=["given"], label="A")
    D = model.set_point(28.0, -29.0, label="D")
    C = model.set_point(92.0, -29.0, label="C")
    B = model.set_point(159.0, -29.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(C, B)

    # Collinear sections
    model.set_section([A, D, B])
    model.set_section([A, C, B])
    model.set_section([A, D, C])
    model.set_section([D, C, B])

    return model


if __name__ == "__main__":
    construct_0422_g1()
