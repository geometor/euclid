"""Programmatic construction for Book VI, Proposition 32 Commentary (0278.g1).

Counter-case showing triangles ABC and ECD placed at C with parallel sides
where angles BAC and CDE are supplementary rather than equal.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g1() -> Model:
    """Construct the figure for 0278.g1 (VI.32 counter-case) using geometor.model."""
    model = Model("0278.g1")

    # 1. Points
    A = model.set_point(103.0, -39.0, classes=["given"], label="A")
    B = model.set_point(41.0, -113.0, classes=["given"], label="B")
    C = model.set_point(139.0, -113.0, classes=["given"], label="C")
    E = model.set_point(154.0, -29.0, label="E")
    D = model.set_point(176.0, -71.0, label="D")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, A)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, C)

    # 3. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([E, C, D])

    return model


if __name__ == "__main__":
    construct_0278_g1()
