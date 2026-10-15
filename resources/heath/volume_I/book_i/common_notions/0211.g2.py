"""Programmatic construction for Book I, Postulate 2 Note — Saccheri's Proof (0211.g2).

Saccheri's five-stage proof that two straight lines cannot have a common segment AX,
using circular arc BMC (and BDFC) centered at X with radii XB, XM, XD, XF, XC.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0211_g2() -> Model:
    """Construct the figure for 0211.g2 using geometor.model."""
    model = Model("0211.g2")

    # Common segment AX
    A = model.set_point(110.0, -225.0, classes=["given"], label="A")
    X = model.set_point(110.0, -122.0, classes=["given"], label="X")
    model.set_segment(A, X)

    # Points B, M, D, F, C on circular arc centered at X with radius R = 93
    r = 93.0
    D = model.set_point(110.0, -29.0, label="D")
    B = model.set_point(
        round(110.0 - r * math.sin(math.radians(50.0)), 2),
        round(-122.0 + r * math.cos(math.radians(50.0)), 2),
        label="B",
    )
    C = model.set_point(
        round(110.0 + r * math.sin(math.radians(50.0)), 2),
        round(-122.0 + r * math.cos(math.radians(50.0)), 2),
        label="C",
    )
    M = model.set_point(
        round(110.0 - r * math.sin(math.radians(28.0)), 2),
        round(-122.0 + r * math.cos(math.radians(28.0)), 2),
        label="M",
    )
    F = model.set_point(
        round(110.0 + r * math.sin(math.radians(28.0)), 2),
        round(-122.0 + r * math.cos(math.radians(28.0)), 2),
        label="F",
    )

    model.construct_circle(X, D)

    # Point L on XB produced beyond B
    r_l = 112.0
    L = model.set_point(
        round(110.0 - r_l * math.sin(math.radians(50.0)), 2),
        round(-122.0 + r_l * math.cos(math.radians(50.0)), 2),
        label="L",
    )

    # Auxiliary points K, T, P on hypothetical lines from A to M
    K = model.set_point(79.42, -96.34, label="K")
    T = model.set_point(98.2, -175.0, label="T")
    P = model.set_point(70.6, -156.5, label="P")

    model.set_segment(X, B)
    model.set_segment(B, L)
    model.set_segment(X, M)
    model.set_segment(X, D)
    model.set_segment(X, F)
    model.set_segment(X, C)
    model.set_segment(A, M)
    model.set_segment(A, L)

    model.set_section([A, X, D])
    model.set_section([A, T, K])

    return model


if __name__ == "__main__":
    construct_0211_g2()
