"""Programmatic construction for Book V, Proposition 14 (0168.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0168_g1() -> Model:
    """Construct the figure 0168.g1 (Book V, Prop. 14 magnitudes A, B, C, D) using geometor.model."""
    model = Model("0168.g1")

    # Magnitude A: (25, 24) to (132, 24)
    A1 = model.set_point(25.00, -24.00, classes=["given"], label="A")
    A2 = model.set_point(132.00, -24.00, classes=["given"], label="A2")
    model.set_segment(A1, A2)

    # Magnitude B: (25, 51) to (106, 51)
    B1 = model.set_point(25.00, -51.00, classes=["given"], label="B")
    B2 = model.set_point(106.00, -51.00, classes=["given"], label="B2")
    model.set_segment(B1, B2)

    # Magnitude C: (209, 24) to (290, 24)
    C1 = model.set_point(209.00, -24.00, classes=["given"], label="C")
    C2 = model.set_point(290.00, -24.00, classes=["given"], label="C2")
    model.set_segment(C1, C2)

    # Magnitude D: (209, 51) to (272, 51)
    D1 = model.set_point(209.00, -51.00, classes=["given"], label="D")
    D2 = model.set_point(272.00, -51.00, classes=["given"], label="D2")
    model.set_segment(D1, D2)

    return model


if __name__ == "__main__":
    construct_0168_g1()
