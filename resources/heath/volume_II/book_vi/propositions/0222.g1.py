"""Programmatic construction for Book VI, Proposition 13 (0222.g1).

To two given straight lines to find a mean proportional.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0222_g1() -> Model:
    """Construct the figure for 0222.g1 (VI.13) using geometor.model."""
    model = Model("0222.g1")

    # 1. Points
    A = model.set_point(18.0, -101.0, classes=["given"], label="A")
    B = model.set_point(131.0, -101.0, classes=["given"], label="B")
    C = model.set_point(175.0, -101.0, classes=["given"], label="C")
    O = model.set_point(96.5, -101.0, label="O")
    D = model.set_point(131.0, -30.49, label="D")

    # 2. Circle / Semicircle
    model.construct_circle(O, A)

    # 3. Segments
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(A, D)
    model.set_segment(D, C)

    # 4. Collinear Sections
    model.set_section([A, B, C])

    # 5. Polygons
    model.set_polygon([A, D, C])
    model.set_polygon([A, B, D])
    model.set_polygon([D, B, C])

    # 6. Angles / Wedges
    model.set_wedge(D, A, A, C)
    model.set_wedge(B, A, A, D)
    model.set_wedge(B, C, C, D)

    return model


if __name__ == "__main__":
    construct_0222_g1()
