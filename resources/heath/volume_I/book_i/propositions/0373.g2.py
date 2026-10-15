"""Programmatic construction for Proposition 47 Commentary (0373.g2).

Treutlein's double-row dot gnomon around a 3x3 square forming a 5x5 square.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0373_g2() -> Model:
    """Construct the double-row dot gnomon figure (0373.g2) using geometor.model."""
    model = Model("0373.g2")

    # Partition lines separating the 3x3 lower-right square from the double-row gnomon
    A = model.set_point(20, -42.5, classes=["given"], label="A")
    B = model.set_point(91, -42.5, classes=["given"], label="B")
    C = model.set_point(48.5, -12, classes=["given"], label="C")
    D = model.set_point(48.5, -88, classes=["given"], label="D")
    E = model.set_point(48.5, -42.5, label="E")

    model.set_segment(A, B)
    model.set_segment(C, D)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(C, E)
    model.set_segment(E, D)

    return model


if __name__ == "__main__":
    construct_0373_g2()
