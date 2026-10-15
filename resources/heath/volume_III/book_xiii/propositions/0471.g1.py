"""Programmatic construction for Book XIII, Proposition 12 (0471.g1).

Equilateral triangle ABC inscribed in circle ABC with centre D, diameter AE,
and chord BE.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0471_g1() -> Model:
    """Construct the figure 0471.g1 using geometor.model."""
    model = Model("0471.g1")

    cx, cy, r = 98.0, -114.0, 85.0
    D = model.set_point(cx, cy, classes=["given"], label="D")

    # Equilateral triangle vertices A (top), B (bottom-left), C (bottom-right)
    angles_deg = [90.0, -150.0, -30.0]
    labels = ["A", "B", "C"]
    pts = {}
    for lbl, deg in zip(labels, angles_deg):
        rad = math.radians(deg)
        pts[lbl] = model.set_point(
            round(cx + r * math.cos(rad), 1),
            round(cy + r * math.sin(rad), 1),
            classes=["given"],
            label=lbl,
        )

    A, B, C = pts["A"], pts["B"], pts["C"]

    # Circle ABC
    model.construct_circle(D, A)

    # Diameter endpoint E at bottom (-90 deg)
    E = model.set_point(98.0, -199.0, classes=["constructed"], label="E")

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, E])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (B, C), (C, A),
        (A, E), (A, D), (D, E),
        (B, E),
    ]:
        model.set_segment(p1, p2)

    # Section
    model.set_section([A, D, E])

    return model


if __name__ == "__main__":
    construct_0471_g1()
