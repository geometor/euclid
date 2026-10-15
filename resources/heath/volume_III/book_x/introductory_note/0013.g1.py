"""Programmatic construction for Book X Introductory Note (0013.g1)."""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0013_g1() -> Model:
    """Construct Pappus's semicircle figure for the minor irrational (0013.g1)."""
    model = Model("0013.g1")

    # Base line points A, F (center), B, C with radius R = 92
    A = model.set_point(16.0, -148.0, classes=["given"], label="A")
    F = model.set_point(108.0, -148.0, classes=["given"], label="F")
    B = model.set_point(200.0, -148.0, classes=["given"], label="B")
    C = model.set_point(292.0, -148.0, classes=["given"], label="C")

    # Semicircle on diameter AB (center F) and line AC
    model.construct_line(A, C)
    model.construct_circle(F, A)

    # Point D of tangency from C (angle BFD = 60 deg) and midpoint E of arc BD (30 deg)
    R = 92.0
    D = model.set_point(
        108.0 + R * math.cos(math.radians(60.0)),
        -148.0 + R * math.sin(math.radians(60.0)),
        label="D",
    )
    E = model.set_point(
        108.0 + R * math.cos(math.radians(30.0)),
        -148.0 + R * math.sin(math.radians(30.0)),
        label="E",
    )

    # Polygons
    model.set_polygon([F, D, C])
    model.set_polygon([F, E, C])

    # Collinear segments along AC
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(B, C)
    model.set_segment(A, B)
    model.set_segment(F, C)
    model.set_segment(A, C)
    model.set_section([A, B, C])

    # Radial and secant/tangent segments
    model.set_segment(F, D)
    model.set_segment(F, E)
    model.set_segment(C, D)
    model.set_segment(C, E)

    # Circular wedge / arc BD
    model.set_wedge(F, B, B, D)

    return model


if __name__ == "__main__":
    construct_0013_g1()
