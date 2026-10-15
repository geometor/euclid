"""Programmatic construction for Proposition 47 Commentary (0373.g1).

Pythagorean dot-gnomon representations of square numbers:
- Part 1: 4^2 + 9 = 5^2 (4x4 square with gnomon of 9 dots)
- Part 2: Successive odd gnomons 1 + 3 + 5 + 7 + 9 + 11 = 6^2
- Part 3: 12^2 + 25 = 13^2 (12x12 square with gnomon of 25 dots)
"""

from __future__ import annotations

from geometor.model import Model


def construct_0373_g1() -> Model:
    """Construct the Pythagorean dot-gnomon figures (0373.g1) using geometor.model."""
    model = Model("0373.g1")

    # Part 1: 5x5 dot grid with 4x4 inner square and 9-dot gnomon divider
    A1 = model.set_point(42, -41, classes=["given"], label="A1")
    B1 = model.set_point(101.5, -41, label="B1")
    C1 = model.set_point(101.5, -100.5, label="C1")
    D1 = model.set_point(42, -100.5, label="D1")
    model.set_segment(B1, C1)
    model.set_segment(C1, D1)
    model.set_polygon([A1, B1, C1, D1])

    # Part 2: 6x6 dot grid with 5 successive gnomon dividers
    for k in range(1, 6):
        x = 174 + 15 * k - 0.5
        y = -(41 + 15 * k - 0.5)
        pk_top = model.set_point(x, -41, label=f"P2_T{k}")
        pk_corner = model.set_point(x, y, label=f"P2_C{k}")
        pk_left = model.set_point(174, y, label=f"P2_L{k}")
        model.set_segment(pk_top, pk_corner)
        model.set_segment(pk_corner, pk_left)

    # Part 3: 13x13 dot grid with 12x12 inner square and 25-dot gnomon divider
    A3 = model.set_point(319.0, -41.0, classes=["given"], label="A3")
    B3 = model.set_point(499.6, -41.0, label="B3")
    C3 = model.set_point(499.6, -221.6, label="C3")
    D3 = model.set_point(319.0, -221.6, label="D3")
    model.set_segment(B3, C3)
    model.set_segment(C3, D3)
    model.set_polygon([A3, B3, C3, D3])

    return model


if __name__ == "__main__":
    construct_0373_g1()
