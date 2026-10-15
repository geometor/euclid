"""Programmatic construction for Book XIII, Proposition 14 (0478.g1).

Left: Semicircle ADB on diameter AB bisected at C, with perpendicular CD
and chord DB.
Right: Square EFGH with side equal to DB, diagonals EG, HF meeting at K,
and perpendicular axis LKM with KL = KM = EK, forming regular octahedron.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0478_g1() -> Model:
    """Construct the figure 0478.g1 using geometor.model."""
    model = Model("0478.g1")

    # Left: Semicircle ADB on diameter AB (centre C(110, -138), radius 92)
    A = model.set_point(18.0, -138.0, classes=["given"], label="A")
    B = model.set_point(202.0, -138.0, classes=["given"], label="B")
    C = model.set_point(110.0, -138.0, classes=["constructed"], label="C")
    D = model.set_point(110.0, -46.0, classes=["constructed"], label="D")
    model.construct_circle(C, A)

    # Right: Square EFGH and Octahedron vertices L, M, centre K
    E = model.set_point(259.0, -44.0, classes=["given"], label="E")
    F = model.set_point(259.0, -160.0, classes=["given"], label="F")
    G = model.set_point(375.0, -160.0, classes=["given"], label="G")
    H = model.set_point(375.0, -44.0, classes=["given"], label="H")
    K = model.set_point(317.0, -102.0, classes=["constructed"], label="K")
    L = model.set_point(297.0, -22.0, classes=["constructed"], label="L")
    M = model.set_point(337.0, -182.0, classes=["constructed"], label="M")

    # Polygons and faces
    model.set_polygon([C, D, B])
    model.set_polygon([E, F, G, H])
    model.set_polygon([L, E, H])
    model.set_polygon([L, E, F])
    model.set_polygon([L, F, G])
    model.set_polygon([L, G, H])
    model.set_polygon([M, E, H])
    model.set_polygon([M, E, F])
    model.set_polygon([M, F, G])
    model.set_polygon([M, G, H])
    model.set_polygon([L, E, M])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (A, C), (C, B), (C, D), (D, B),
        (E, F), (F, G), (G, H), (H, E),
        (E, G), (E, K), (K, G),
        (H, F), (H, K), (K, F),
        (L, M), (L, K), (K, M),
        (L, E), (L, F), (L, G), (L, H),
        (M, E), (M, F), (M, G), (M, H),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([A, C, B])
    model.set_section([E, K, G])
    model.set_section([H, K, F])
    model.set_section([L, K, M])

    # Angles (wedges)
    model.set_wedge(K, E, E, H)
    model.set_wedge(K, L, L, E)
    model.set_wedge(E, L, L, M)

    return model


if __name__ == "__main__":
    construct_0478_g1()
