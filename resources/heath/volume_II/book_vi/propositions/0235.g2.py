"""Programmatic construction for Book VI, Proposition 18 (0235.g2).

Constructed rectilinear figure AH (quadrilateral ABHG) on given straight line AB,
similar and similarly situated to CE (CDEF).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0235_g2() -> Model:
    """Construct the figure for 0235.g2 (VI.18, constructed figure AH) using geometor.model."""
    model = Model("0235.g2")

    # 1. Points
    A = model.set_point(21.0, -110.0, classes=["given"], label="A")
    B = model.set_point(113.0, -110.0, classes=["given"], label="B")
    H = model.set_point(98.0, -22.0, classes=["given"], label="H")
    G = model.set_point(40.0, -58.0, classes=["given"], label="G")

    # 2. Segments
    model.set_segment(A, B)
    model.set_segment(B, H)
    model.set_segment(H, G)
    model.set_segment(G, A)
    model.set_segment(B, G)

    # 3. Polygons
    model.set_polygon([A, B, H, G])
    model.set_polygon([G, A, B])
    model.set_polygon([G, B, H])

    # 4. Angles / Wedges
    model.set_wedge(A, G, G, B)
    model.set_wedge(B, A, A, G)
    model.set_wedge(G, A, A, B)
    model.set_wedge(B, G, G, H)
    model.set_wedge(G, B, B, H)
    model.set_wedge(H, G, G, B)
    model.set_wedge(G, A, A, H)
    model.set_wedge(B, A, A, H)

    return model


if __name__ == "__main__":
    construct_0235_g2()
