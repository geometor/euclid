"""Programmatic construction for Book XIII, Proposition 13 (0472.g1).

Left: Semicircle ADB on diameter AB cut at C with AC = 2 CB, perpendicular CD,
and chord AD.
Right: Circle EFG with radius HE = CD, inscribed equilateral triangle EFG,
perpendicular axis KHL with HK = AC and HL = CB, forming regular pyramid KEFG.
"""

from __future__ import annotations

import math
from geometor.model import Model


def construct_0472_g1() -> Model:
    """Construct the figure 0472.g1 using geometor.model."""
    model = Model("0472.g1")

    # Left: Semicircle ADB on diameter AB (length 205, center (128.5, -122.0))
    A = model.set_point(26.0, -122.0, classes=["given"], label="A")
    B = model.set_point(231.0, -122.0, classes=["given"], label="B")
    C = model.set_point(162.7, -122.0, classes=["constructed"], label="C")
    D = model.set_point(162.7, -25.4, classes=["constructed"], label="D")
    O_left = model.set_point(128.5, -122.0, classes=["auxiliary"], label="O_left")
    model.construct_circle(O_left, A)

    # Right: Circle EFG with center H(426.0, -141.0) and radius r = 96.0
    cx, cy, r = 426.0, -141.0, 96.0
    H = model.set_point(cx, cy, classes=["given"], label="H")
    E = model.set_point(426.0, -45.0, classes=["given"], label="E")
    F = model.set_point(
        round(cx - r * math.cos(math.radians(30.0)), 1),
        round(cy - r * math.sin(math.radians(30.0)), 1),
        classes=["given"],
        label="F",
    )
    G = model.set_point(
        round(cx + r * math.cos(math.radians(30.0)), 1),
        round(cy - r * math.sin(math.radians(30.0)), 1),
        classes=["given"],
        label="G",
    )
    model.construct_circle(H, E)

    # Axis KHL (perspective)
    K = model.set_point(358.0, -62.0, classes=["constructed"], label="K")
    L = model.set_point(460.0, -180.5, classes=["constructed"], label="L")

    # Polygons, triangles, and pyramid
    model.set_polygon([A, C, D])
    model.set_polygon([E, F, G])
    model.set_polygon([K, E, F])
    model.set_polygon([K, F, G])
    model.set_polygon([K, E, G])
    model.set_polygon([K, E, F, G])
    model.set_polygon([K, H, E])
    model.set_polygon([K, H, F])
    model.set_polygon([K, H, G])
    model.set_polygon([E, K, L])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (A, D),
        (E, F), (F, G), (G, E),
        (H, E), (H, F), (H, G),
        (K, L), (K, H), (H, L),
        (K, E), (K, F), (K, G),
        (F, L), (L, G),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, C, B])
    model.set_section([K, H, L])

    # Angles (wedges)
    model.set_wedge(C, A, A, D)
    model.set_wedge(H, K, K, E)
    model.set_wedge(H, K, K, F)
    model.set_wedge(H, K, K, G)
    model.set_wedge(H, E, E, L)

    return model


if __name__ == "__main__":
    construct_0472_g1()
