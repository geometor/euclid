"""Programmatic construction for Book XII, Proposition 2 Commentary (0381.g2).

Circle with center C and radius CA, and concentric circles with center O and
radii OD, OB, with similar regular octagons inscribed in circles CA and OB.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0381_g2() -> Model:
    """Construct the figure 0381.g2 using geometor.model."""
    model = Model("0381.g2")

    # Left circle center C and top point A (radius 68)
    C = model.set_point(78.0, -108.0, classes=["given"], label="C")
    A = model.set_point(78.0, -40.0, classes=["given"], label="A")

    # Right concentric circles center O, inner top D (r=74), outer top B (r=90)
    O = model.set_point(336.0, -110.0, classes=["given"], label="O")
    D = model.set_point(336.0, -36.0, label="D")
    B = model.set_point(336.0, -20.0, classes=["given"], label="B")

    # Circles
    model.construct_circle(C, A)
    model.construct_circle(O, D)
    model.construct_circle(O, B)

    # Radial segments
    model.set_segment(C, A)
    model.set_segment(O, B)
    model.set_segment(O, D)
    model.set_segment(D, B)

    # Inscribed regular octagons
    left_oct = []
    right_oct = []
    for k in range(8):
        theta = math.radians(22.5 + 45.0 * k)
        lx = round(78.0 + 68.0 * math.sin(theta), 2)
        ly = round(-108.0 + 68.0 * math.cos(theta), 2)
        rx = round(336.0 + 90.0 * math.sin(theta), 2)
        ry = round(-110.0 + 90.0 * math.cos(theta), 2)
        left_oct.append(model.set_point(lx, ly, label=f"L{k+1}"))
        right_oct.append(model.set_point(rx, ry, label=f"R{k+1}"))

    for k in range(8):
        model.set_segment(left_oct[k], left_oct[(k + 1) % 8])
        model.set_segment(right_oct[k], right_oct[(k + 1) % 8])

    model.set_polygon(left_oct)
    model.set_polygon(right_oct)

    return model


if __name__ == "__main__":
    construct_0381_g2()
