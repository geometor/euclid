"""Programmatic construction for Book X, Proposition 79 (0171.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0171_g1() -> Model:
    """Construct the figure 0171.g1 using geometor.model."""
    model = Model("0171.g1")

    # Apotome AB with annexes BC and BD
    A = model.set_point(15.0, -21.0, classes=["given"], label="A")
    B = model.set_point(82.0, -21.0, classes=["given"], label="B")
    C = model.set_point(183.0, -21.0, classes=["given"], label="C")
    D = model.set_point(220.0, -21.0, classes=["given"], label="D")

    # Base line
    model.construct_line(A, D)

    # Segments
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(C, D)

    # Sections
    model.set_section([A, B, C])
    model.set_section([A, B, D])
    model.set_section([A, C, D])
    model.set_section([B, C, D])

    return model


if __name__ == "__main__":
    construct_0171_g1()
