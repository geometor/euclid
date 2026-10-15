"""Programmatic construction for Book II, Proposition 3 Note Figure (0393.g2).

Constructs the straight line AB with internal division point C illustrating
Lardner's proof of the difference of two squares from II. 1, 2, 3.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0393_g2() -> Model:
    """Construct the straight line AB cut at C on folio 0393 (0393.g2)."""
    model = Model("0393.g2")

    A = model.set_point(27.0, -24.5, classes=["given"], label="A")
    C = model.set_point(77.0, -24.5, classes=["given"], label="C")
    B = model.set_point(151.0, -24.5, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)
    model.set_section([A, C, B])

    return model


if __name__ == "__main__":
    construct_0393_g2()
