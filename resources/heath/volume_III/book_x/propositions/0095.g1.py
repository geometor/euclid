"""Programmatic construction for Book X, Lemma before Proposition 42 (0095.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0095_g1() -> Model:
    """Construct the figure 0095.g1 using geometor.model."""
    model = Model("0095.g1")

    # Straight line AB divided at D, E (midpoint), C
    A = model.set_point(17.0, -21.0, classes=["given"], label="A")
    D = model.set_point(109.0, -21.0, classes=["given"], label="D")
    E = model.set_point(138.5, -21.0, label="E")
    C = model.set_point(182.0, -21.0, classes=["given"], label="C")
    B = model.set_point(260.0, -21.0, classes=["given"], label="B")

    model.construct_line(A, B)

    # Whole and all sub-segments on AB
    model.set_segment(A, B)
    model.set_segment(A, D)
    model.set_segment(A, E)
    model.set_segment(A, C)
    model.set_segment(D, E)
    model.set_segment(D, C)
    model.set_segment(D, B)
    model.set_segment(E, C)
    model.set_segment(E, B)
    model.set_segment(C, B)

    # Collinear sections on AB
    model.set_section([A, C, B])
    model.set_section([A, D, B])
    model.set_section([A, E, B])
    model.set_section([D, E, C])

    return model


if __name__ == "__main__":
    construct_0095_g1()
