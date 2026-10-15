"""Programmatic construction for Book III, Proposition 24 (0060.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0060_g1() -> Model:
    """Construct the figure 0060.g1 using geometor.model."""
    model = Model("0060.g1")

    # Left segment AEB and right segments CFD, CGD (y-inverted)
    A = model.set_point(28.00, -68.00, classes=["given"], label="A")
    B = model.set_point(158.00, -68.00, classes=["given"], label="B")
    E = model.set_point(93.00, -29.37, label="E")
    O1 = model.set_point(93.00, -103.37, label="O1")

    C = model.set_point(252.00, -68.00, classes=["given"], label="C")
    D = model.set_point(382.00, -68.00, classes=["given"], label="D")
    F = model.set_point(294.00, -33.04, label="F")
    G = model.set_point(332.00, -30.91, label="G")
    O2 = model.set_point(317.00, -103.37, label="O2")

    # Circles for segments AEB and CFD
    model.construct_circle(O1, A)
    model.construct_circle(O2, C)

    # Base segments AB and CD
    model.set_segment(A, B)
    model.set_segment(C, D)

    return model


if __name__ == "__main__":
    construct_0060_g1()
