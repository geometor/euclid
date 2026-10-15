"""Programmatic construction for Book V, Proposition 19 Commentary / Simson's Prop. E (0181.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0181_g1() -> Model:
    """Construct the figure 0181.g1 (Simson's Proposition E) using geometor.model."""
    model = Model("0181.g1")

    # Left vertical magnitude AB divided at E
    A = model.set_point(22.00, -10.00, classes=["given"], label="A")
    E = model.set_point(22.00, -54.00, classes=["given"], label="E")
    B = model.set_point(22.00, -140.00, classes=["given"], label="B")

    # Right vertical magnitude CD divided at F
    C = model.set_point(76.00, -36.00, classes=["given"], label="C")
    F = model.set_point(76.00, -68.00, classes=["given"], label="F")
    D = model.set_point(76.00, -140.00, classes=["given"], label="D")

    # Base lines
    model.construct_line(A, B)
    model.construct_line(C, D)

    # Whole and subdivided segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)

    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)

    # Collinear sections
    model.set_section([A, E, B])
    model.set_section([C, F, D])

    return model


if __name__ == "__main__":
    construct_0181_g1()
