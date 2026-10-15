"""Programmatic construction for Book X, Proposition 59 Lemma (0135.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0135_g1() -> Model:
    """Construct the figure 0135.g1 using geometor.model."""
    model = Model("0135.g1")

    # Straight line AB bisected at D and cut into unequal parts at C
    A = model.set_point(17.0, -21.5, classes=["given"], label="A")
    D = model.set_point(117.0, -21.5, label="D")
    C = model.set_point(151.0, -21.5, classes=["given"], label="C")
    B = model.set_point(216.0, -21.5, classes=["given"], label="B")

    # Base line
    model.construct_line(A, B)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(C, B)

    # Sections
    model.set_section([A, C, B])
    model.set_section([A, D, B])
    model.set_section([A, D, C])
    model.set_section([D, C, B])

    return model


if __name__ == "__main__":
    construct_0135_g1()
