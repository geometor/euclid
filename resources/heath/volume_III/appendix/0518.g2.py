"""Programmatic construction for Appendix I (Book XIV), Proposition 2 (0518.g2).

Proof that the same circle circumscribes both the pentagon CDEFG of the
dodecahedron and the triangle KLH of the icosahedron inscribed in the same
sphere of diameter AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0518_g2() -> Model:
    """Construct the figure 0518.g2 using geometor.model."""
    model = Model("0518.g2")

    # Left circle and inscribed regular pentagon CDEFG
    O1 = model.set_point(116.0, -106.0, classes=["auxiliary"], label="O1")
    C = model.set_point(116.0, -44.0, classes=["given"], label="C")
    D = model.set_point(57.0, -87.0, classes=["given"], label="D")
    E = model.set_point(80.0, -156.0, classes=["given"], label="E")
    F = model.set_point(152.0, -156.0, classes=["given"], label="F")
    G = model.set_point(175.0, -87.0, classes=["given"], label="G")
    model.construct_circle(O1, C)

    # Sphere diameter AB and extreme-and-mean ratio line MON
    A = model.set_point(170.0, -26.0, classes=["given"], label="A")
    B = model.set_point(372.0, -26.0, classes=["given"], label="B")
    M = model.set_point(232.0, -60.0, classes=["given"], label="M")
    O = model.set_point(288.0, -60.0, classes=["given"], label="O")
    N = model.set_point(320.0, -60.0, classes=["given"], label="N")

    # Right circle and inscribed equilateral triangle KLH
    O2 = model.set_point(442.0, -102.0, classes=["auxiliary"], label="O2")
    K = model.set_point(442.0, -38.0, classes=["given"], label="K")
    L = model.set_point(387.0, -134.0, classes=["given"], label="L")
    H = model.set_point(497.0, -134.0, classes=["given"], label="H")
    model.construct_circle(O2, K)

    # Polygons
    model.set_polygon([C, D, E, F, G])
    model.set_polygon([C, D, G])
    model.set_polygon([D, E, F, G])
    model.set_polygon([K, L, H])

    # Section MON
    model.set_section([M, O, N])

    # Segments
    for p1, p2 in [
        (C, D), (D, E), (E, F), (F, G), (G, C), (D, G),
        (A, B),
        (M, N), (M, O), (O, N),
        (K, L), (L, H), (H, K),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0518_g2()
