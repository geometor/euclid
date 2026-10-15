"""Programmatic construction for Book XIII, Proposition 8 (0457.g1).

An equilateral and equiangular pentagon ABCDE inscribed in circle ABCDE,
with diagonals AC and BE intersecting at H in extreme and mean ratio.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0457_g1() -> Model:
    """Construct the figure 0457.g1 using geometor.model."""
    model = Model("0457.g1")

    cx, cy, r = 108.0, -108.0, 86.0
    O = model.set_point(cx, cy, classes=["auxiliary"], label="O")

    # Regular pentagon vertices A (top), B (right), C (bottom-right), D (bottom-left), E (left)
    angles_deg = [90.0, 18.0, -54.0, -126.0, 162.0]
    labels = ["A", "B", "C", "D", "E"]
    pts = {}
    for lbl, deg in zip(labels, angles_deg):
        rad = math.radians(deg)
        pts[lbl] = model.set_point(
            round(cx + r * math.cos(rad), 1),
            round(cy + r * math.sin(rad), 1),
            classes=["given"],
            label=lbl,
        )

    A, B, C, D, E = pts["A"], pts["B"], pts["C"], pts["D"], pts["E"]

    # Circumscribed circle ABCDE
    model.construct_circle(O, A)

    # Intersection H of diagonals AC and BE
    H = model.set_point(127.3, -81.4, classes=["constructed"], label="H")

    # Pentagon and triangles
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, B, E])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, H])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (B, C), (C, D), (D, E), (E, A),
        (A, C), (A, H), (H, C),
        (B, E), (E, H), (H, B),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, H, C])
    model.set_section([E, H, B])

    # Angles (wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, A, A, E)
    model.set_wedge(H, A, A, E)
    model.set_wedge(A, E, E, C)
    model.set_wedge(E, A, A, B)
    model.set_wedge(A, B, B, E)
    model.set_wedge(H, A, A, B)

    return model


if __name__ == "__main__":
    construct_0457_g1()
