"""Programmatic construction for Book VI, Proposition 12, Alternative (0221.g2).

Alternative anti-parallel construction for the fourth proportional.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0221_g2() -> Model:
    """Construct the figure for 0221.g2 (VI.12 Alternative) using geometor.model."""
    model = Model("0221.g2")

    # 1. Points
    D = model.set_point(18.0, -110.0, classes=["given"], label="D")
    H = model.set_point(76.0, -110.0, label="H")
    E = model.set_point(152.0, -110.0, label="E")
    F = model.set_point(84.04, -61.12, label="F")
    G = model.set_point(92.93, -54.54, label="G")

    # 2. Construction Lines
    model.construct_line(D, G)
    model.construct_line(D, E)

    # 3. Segments
    model.set_segment(D, E)
    model.set_segment(D, H)
    model.set_segment(H, E)

    model.set_segment(D, G)
    model.set_segment(D, F)
    model.set_segment(F, G)

    model.set_segment(E, F)
    model.set_segment(G, H)

    # 4. Collinear Sections
    model.set_section([D, H, E])
    model.set_section([D, F, G])

    # 5. Polygons
    model.set_polygon([E, D, F])
    model.set_polygon([G, D, H])

    # 6. Angles / Wedges
    model.set_wedge(G, D, D, H)
    model.set_wedge(E, D, D, F)

    return model


if __name__ == "__main__":
    construct_0221_g2()
