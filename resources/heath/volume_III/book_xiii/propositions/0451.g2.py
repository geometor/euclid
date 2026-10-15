"""Programmatic construction for Book XIII, Proposition 4 (0451.g2).

If a straight line be cut in extreme and mean ratio, the square on the whole
and the square on the lesser segment together are triple of the square on the
greater segment.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0451_g2() -> Model:
    """Construct the figure for Book XIII, Proposition 4 using geometor.model."""
    model = Model("0451.g2")

    # Straight line AB cut in extreme and mean ratio at C
    A = model.set_point(22.0, -23.0, classes=["given"], label="A")
    C = model.set_point(106.0, -23.0, classes=["given"], label="C")
    B = model.set_point(157.0, -23.0, classes=["given"], label="B")

    model.construct_line(A, B)
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(C, B)

    # Square ADEB on AB, divided through C and F
    H = model.set_point(22.0, -74.0, label="H")
    F = model.set_point(106.0, -74.0, label="F")
    K = model.set_point(157.0, -74.0, label="K")

    D = model.set_point(22.0, -158.0, label="D")
    G = model.set_point(106.0, -158.0, label="G")
    E = model.set_point(157.0, -158.0, label="E")

    # Horizontal segments
    model.set_segment(H, K)
    model.set_segment(H, F)
    model.set_segment(F, K)
    model.set_segment(D, E)
    model.set_segment(D, G)
    model.set_segment(G, E)

    # Vertical segments
    model.set_segment(A, D)
    model.set_segment(A, H)
    model.set_segment(H, D)
    model.set_segment(C, G)
    model.set_segment(C, F)
    model.set_segment(F, G)
    model.set_segment(B, E)
    model.set_segment(B, K)
    model.set_segment(K, E)

    # Diagonal BD
    model.set_segment(B, D)
    model.set_segment(B, F)
    model.set_segment(F, D)

    # Polygons (squares, rectangles, and gnomon LMN)
    model.set_polygon([A, D, E, B])
    model.set_polygon([H, F, G, D])
    model.set_polygon([C, B, K, F])
    model.set_polygon([A, C, F, H])
    model.set_polygon([F, K, E, G])
    model.set_polygon([A, B, K, H])
    model.set_polygon([C, B, E, G])
    model.set_polygon([H, A, B, E, G, F])

    return model


if __name__ == "__main__":
    construct_0451_g2()
