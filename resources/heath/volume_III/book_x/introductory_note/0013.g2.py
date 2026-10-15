"""Programmatic construction for Book X Introductory Note (0013.g2)."""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0013_g2() -> Model:
    """Construct Pappus's two-semicircle figure for the binomial excess (0013.g2)."""
    model = Model("0013.g2")

    # Base line points A, H (left center), C (right center), D with radius R = 92
    A = model.set_point(17.0, -148.0, classes=["given"], label="A")
    H = model.set_point(109.0, -148.0, classes=["given"], label="H")
    C = model.set_point(201.0, -148.0, classes=["given"], label="C")
    D = model.set_point(293.0, -148.0, classes=["given"], label="D")

    # Base line AD and two semicircles (H, A) and (C, H)
    model.construct_line(A, D)
    model.construct_circle(H, A)
    model.construct_circle(C, H)

    # Intersection B of the two semicircles (tangent DB to left semicircle)
    B = model.set_point(155.0, -68.33, label="B")

    # Bisector DK of angle ADB (15 deg with DA) meeting left semicircle at F and right at K
    F = model.set_point(197.36, -122.37, label="F")
    K = model.set_point(121.33, -102.00, label="K")

    # Polygons
    model.set_polygon([H, B, D])
    model.set_polygon([H, B, C])

    # Collinear segments along AD
    model.set_segment(A, H)
    model.set_segment(H, C)
    model.set_segment(C, D)
    model.set_segment(A, C)
    model.set_segment(H, D)
    model.set_segment(A, D)
    model.set_section([A, H, C])
    model.set_section([H, C, D])

    # Segments HB, DB, and bisector segments DF, FK, DK
    model.set_segment(H, B)
    model.set_segment(D, B)
    model.set_segment(D, F)
    model.set_segment(F, K)
    model.set_segment(D, K)
    model.set_section([D, F, K])

    # Angle wedges at D
    model.set_wedge(A, D, D, B)
    model.set_wedge(A, D, D, F)
    model.set_wedge(F, D, D, B)

    return model


if __name__ == "__main__":
    construct_0013_g2()
