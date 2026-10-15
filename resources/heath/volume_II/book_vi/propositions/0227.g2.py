"""Programmatic construction for Book VI, Proposition 16, Left Figure (0227.g2).

Rectangle BG (on base AB with height AG = F) and straight line E.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0227_g2() -> Model:
    """Construct the figure for 0227.g2 (VI.16 left) using geometor.model."""
    model = Model("0227.g2")

    # 1. Points of rectangle BG and straight line E
    G = model.set_point(27.0, -20.0, classes=["given"], label="G")
    K = model.set_point(142.0, -20.0, label="K")
    B = model.set_point(142.0, -74.0, classes=["given"], label="B")
    A = model.set_point(27.0, -74.0, classes=["given"], label="A")

    E1 = model.set_point(27.0, -113.0, classes=["given"], label="E")
    E2 = model.set_point(87.0, -113.0, classes=["given"], label="E'")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, K)
    model.set_segment(B, K)
    model.set_segment(E1, E2)

    # 3. Polygons (Parallelogram / Rectangle BG)
    model.set_polygon([G, A, B, K])

    # 4. Right angle at A
    model.set_wedge(A, G, G, B)

    return model


if __name__ == "__main__":
    construct_0227_g2()
