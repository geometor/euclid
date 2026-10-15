"""Programmatic construction for Book XIII, Proposition 14 Commentary (0480.g1).

Heath's perspective diagram of the regular octahedron L-EFGH-M alongside
semicircle ADB on diameter AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0480_g1() -> Model:
    """Construct the figure 0480.g1 using geometor.model."""
    model = Model("0480.g1")

    # Left: Semicircle ADB on diameter AB (centre C(84, -128), radius 70)
    A = model.set_point(14.0, -128.0, classes=["given"], label="A")
    B = model.set_point(154.0, -128.0, classes=["given"], label="B")
    C = model.set_point(84.0, -128.0, classes=["constructed"], label="C")
    D = model.set_point(84.0, -58.0, classes=["constructed"], label="D")
    model.construct_circle(C, A)

    # Right: Perspective Square EFGH (centre K) and vertical axis LKM
    E = model.set_point(252.0, -88.0, classes=["given"], label="E")
    F = model.set_point(308.0, -118.0, classes=["given"], label="F")
    G = model.set_point(388.0, -88.0, classes=["given"], label="G")
    H = model.set_point(332.0, -58.0, classes=["given"], label="H")
    K = model.set_point(320.0, -88.0, classes=["constructed"], label="K")
    L = model.set_point(320.0, -20.0, classes=["constructed"], label="L")
    M = model.set_point(320.0, -156.0, classes=["constructed"], label="M")

    # Polygons and faces
    model.set_polygon([C, D, B])
    model.set_polygon([E, F, G, H])
    model.set_polygon([L, E, F])
    model.set_polygon([L, F, G])
    model.set_polygon([L, G, H])
    model.set_polygon([L, E, H])
    model.set_polygon([M, E, F])
    model.set_polygon([M, F, G])
    model.set_polygon([M, G, H])
    model.set_polygon([M, E, H])
    model.set_polygon([L, K, E])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (D, B),
        (E, F), (F, G), (G, H), (H, E),
        (E, G), (E, K), (K, G),
        (F, H), (F, K), (K, H),
        (L, M), (L, K), (K, M),
        (L, E), (L, F), (L, G), (L, H),
        (M, E), (M, F), (M, G), (M, H),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, C, B])
    model.set_section([E, K, G])
    model.set_section([F, K, H])
    model.set_section([L, K, M])

    return model


if __name__ == "__main__":
    construct_0480_g1()
