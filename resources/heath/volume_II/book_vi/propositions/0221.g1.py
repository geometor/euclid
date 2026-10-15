"""Programmatic construction for Book VI, Proposition 12 (0221.g1).

To three given straight lines to find a fourth proportional.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0221_g1() -> Model:
    """Construct the figure for 0221.g1 (VI.12) using geometor.model."""
    model = Model("0221.g1")

    # 1. Points
    # Standalone given straight lines A, B, C
    A1 = model.set_point(212.0, -64.0, classes=["given"], label="A")
    A2 = model.set_point(306.0, -64.0, classes=["given"])
    B1 = model.set_point(212.0, -86.0, classes=["given"], label="B")
    B2 = model.set_point(274.0, -86.0, classes=["given"])
    C1 = model.set_point(212.0, -108.0, classes=["given"], label="C")
    C2 = model.set_point(301.0, -108.0, classes=["given"])

    # Main triangle D, E, F, G, H
    D = model.set_point(19.0, -149.0, classes=["given"], label="D")
    G = model.set_point(113.64, -76.2, label="G")
    E = model.set_point(176.17, -28.1, label="E")
    H = model.set_point(108.0, -149.0, label="H")
    F = model.set_point(166.8, -149.0, label="F")

    # 2. Construction Lines
    model.construct_line(D, E)
    model.construct_line(D, F)

    # 3. Segments
    model.set_segment(A1, A2)
    model.set_segment(B1, B2)
    model.set_segment(C1, C2)

    model.set_segment(D, E)
    model.set_segment(D, G)
    model.set_segment(G, E)

    model.set_segment(D, F)
    model.set_segment(D, H)
    model.set_segment(H, F)

    model.set_segment(G, H)
    model.set_segment(E, F)

    # 4. Collinear Sections
    model.set_section([D, G, E])
    model.set_section([D, H, F])

    # 5. Polygons
    model.set_polygon([D, E, F])
    model.set_polygon([D, G, H])

    # 6. Angles / Wedges
    model.set_wedge(D, E, E, F)

    return model


if __name__ == "__main__":
    construct_0221_g1()
