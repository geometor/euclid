"""Programmatic construction for Book X, Proposition 103 (0233.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0233_g1() -> Model:
    """Construct the figure 0233.g1 using geometor.model."""
    model = Model("0233.g1")

    # Line AE divided at B
    A = model.set_point(31.0, -21.5, classes=["given"], label="A")
    B = model.set_point(92.0, -21.5, classes=["given"], label="B")
    E = model.set_point(149.0, -21.5, classes=["given"], label="E")

    # Line CF divided at D
    C = model.set_point(15.0, -51.0, classes=["given"], label="C")
    D = model.set_point(90.0, -51.0, classes=["given"], label="D")
    F = model.set_point(170.0, -51.0, classes=["given"], label="F")

    # Base lines
    model.construct_line(A, E)
    model.construct_line(C, F)

    # Segments
    model.set_segment(A, E)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(C, F)
    model.set_segment(C, D)
    model.set_segment(D, F)

    # Sections
    model.set_section([A, B, E])
    model.set_section([C, D, F])

    return model


if __name__ == "__main__":
    construct_0233_g1()
