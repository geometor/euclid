"""Programmatic construction for Book IX, Proposition 24 (0420.g3)."""

from __future__ import annotations

from geometor.model import Model


def construct_0420_g3() -> Model:
    """Construct the figure 0420.g3 using geometor.model."""
    model = Model("0420.g3")

    # Subdivided horizontal number segment AB (divided at C)
    A = model.set_point(14.0, -30.0, classes=["given"], label="A")
    C = model.set_point(118.0, -30.0, label="C")
    B = model.set_point(163.0, -30.0, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Whole and subdivided segments on AB
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Collinear section
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0420_g3()
