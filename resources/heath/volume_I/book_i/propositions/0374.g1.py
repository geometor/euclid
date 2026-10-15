"""Programmatic construction for Proposition 47 Commentary (0374.g1).

Platonic dot-gnomon figure comparing a 9x9 square minus a single-row gnomon (8x8)
with a 9x9 square plus a single-row gnomon (10x10): 36 + 8^2 = 10^2.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0374_g1() -> Model:
    """Construct the Platonic dot-gnomon figure (0374.g1) using geometor.model."""
    model = Model("0374.g1")

    O = model.set_point(18, -20, classes=["given"], label="O")

    # 8x8 gnomon boundary
    A8 = model.set_point(138, -20, label="A8")
    B8 = model.set_point(138, -137, label="B8")
    C8 = model.set_point(18, -137, label="C8")
    model.set_segment(A8, B8)
    model.set_segment(B8, C8)
    model.set_polygon([O, A8, B8, C8])

    # 9x9 gnomon boundary
    A9 = model.set_point(153, -16, label="A9")
    B9 = model.set_point(153, -152, label="B9")
    C9 = model.set_point(18, -152, label="C9")
    model.set_segment(A9, B9)
    model.set_segment(B9, C9)
    model.set_polygon([O, A9, B9, C9])

    # 10x10 gnomon boundary
    A10 = model.set_point(168, -14, label="A10")
    B10 = model.set_point(168, -165, label="B10")
    C10 = model.set_point(18, -165, label="C10")
    model.set_segment(A10, B10)
    model.set_segment(B10, C10)
    model.set_polygon([O, A10, B10, C10])

    return model


if __name__ == "__main__":
    construct_0374_g1()
