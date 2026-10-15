"""Programmatic construction for Book X, Proposition 106 (0237.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0237_g1() -> Model:
    """Construct the figure 0237.g1 using geometor.model."""
    model = Model("0237.g1")

    # Line AE divided at B
    A = model.set_point(35.0, -22.5, classes=["given"], label="A")
    B = model.set_point(103.0, -22.5, classes=["given"], label="B")
    E = model.set_point(149.0, -22.5, classes=["given"], label="E")

    # Line CF divided at D
    C = model.set_point(17.0, -52.5, classes=["given"], label="C")
    D = model.set_point(101.0, -52.5, classes=["given"], label="D")
    F = model.set_point(176.0, -52.5, classes=["given"], label="F")

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
    construct_0237_g1()
