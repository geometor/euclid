"""Programmatic construction for Book XIII, Proposition 9 (0459.g1).

Circle ABC with centre E, diameter BA, side of decagon BC, and side of
hexagon CD in a straight line with BC.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0459_g1() -> Model:
    """Construct the figure 0459.g1 using geometor.model."""
    model = Model("0459.g1")

    cx, cy, r = 114.0, -96.0, 82.0
    E = model.set_point(cx, cy, classes=["given"], label="E")
    B = model.set_point(cx - r, cy, classes=["given"], label="B")
    A = model.set_point(cx + r, cy, classes=["given"], label="A")

    # Circle ABC
    model.construct_circle(E, A)

    # C is 36 degrees below B on the circle
    c_rad = math.radians(-144.0)
    C = model.set_point(
        round(cx + r * math.cos(c_rad), 1),
        round(cy + r * math.sin(c_rad), 1),
        classes=["given"],
        label="C",
    )

    # CD is in a straight line with BC and has length r (side of hexagon)
    dir_rad = math.radians(-72.0)
    D = model.set_point(
        round(47.7 + r * math.cos(dir_rad), 1),
        round(-144.2 + r * math.sin(dir_rad), 1),
        classes=["constructed"],
        label="D",
    )

    # F is intersection of ED with the circle (at -108 degrees)
    f_rad = math.radians(-108.0)
    F = model.set_point(
        round(cx + r * math.cos(f_rad), 1),
        round(cy + r * math.sin(f_rad), 1),
        classes=["constructed"],
        label="F",
    )

    # Triangles
    model.set_polygon([E, B, C])
    model.set_polygon([E, B, D])
    model.set_polygon([E, C, D])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (B, A), (B, E), (E, A),
        (B, D), (B, C), (C, D),
        (E, C), (E, D), (E, F), (F, D),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([B, E, A])
    model.set_section([B, C, D])
    model.set_section([E, F, D])

    # Angles (wedges)
    model.set_wedge(E, A, A, C)
    model.set_wedge(E, C, C, B)
    model.set_wedge(B, E, E, C)
    model.set_wedge(C, E, E, B)
    model.set_wedge(E, C, C, D)
    model.set_wedge(D, C, C, E)
    model.set_wedge(E, B, B, D)

    return model


if __name__ == "__main__":
    construct_0459_g1()
