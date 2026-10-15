"""Programmatic construction for Book VI, Proposition 16, Right Figure (0227.g3).

Rectangle DH (on base CD with height CH = E) and straight line F.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0227_g3() -> Model:
    """Construct the figure for 0227.g3 (VI.16 right) using geometor.model."""
    model = Model("0227.g3")

    # 1. Points of rectangle DH and straight line F
    H = model.set_point(28.0, -20.0, classes=["given"], label="H")
    L = model.set_point(120.0, -20.0, label="L")
    D = model.set_point(120.0, -80.0, classes=["given"], label="D")
    C = model.set_point(28.0, -80.0, classes=["given"], label="C")

    F1 = model.set_point(28.0, -113.0, classes=["given"], label="F")
    F2 = model.set_point(76.0, -113.0, classes=["given"], label="F'")

    # 2. Segments
    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, L)
    model.set_segment(D, L)
    model.set_segment(F1, F2)

    # 3. Polygons (Parallelogram / Rectangle DH)
    model.set_polygon([H, C, D, L])

    # 4. Right angle at C
    model.set_wedge(C, H, H, D)

    return model


if __name__ == "__main__":
    construct_0227_g3()
