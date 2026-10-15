"""Programmatic construction for Book XIII, Proposition 13 Commentary (0477.g1).

Pappus' inscription of a regular tetrahedron ABCD in a sphere using two
parallel circular sections LM (centre K) and AB, with tangents EF and GH,
sphere diameter BL, and perpendicular MP.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0477_g1() -> Model:
    """Construct the figure 0477.g1 using geometor.model."""
    model = Model("0477.g1")

    # Sphere centre and boundary points
    O = model.set_point(120.0, -121.0, classes=["auxiliary"], label="O")
    S_top = model.set_point(120.0, -20.0, classes=["auxiliary"], label="S_top")
    model.construct_circle(O, S_top)

    # Upper circular section (LM, CD, centre K)
    L = model.set_point(31.0, -56.0, classes=["given"], label="L")
    M = model.set_point(205.0, -56.0, classes=["given"], label="M")
    K = model.set_point(118.0, -56.0, classes=["constructed"], label="K")
    D = model.set_point(112.0, -34.0, classes=["given"], label="D")
    C = model.set_point(124.0, -78.0, classes=["given"], label="C")

    # Tangent GH through D
    G = model.set_point(34.0, -34.0, classes=["constructed"], label="G")
    H = model.set_point(212.0, -34.0, classes=["constructed"], label="H")

    # Lower circular section diameter AB and tangent EF through A
    A = model.set_point(31.0, -177.0, classes=["given"], label="A")
    B = model.set_point(205.0, -177.0, classes=["given"], label="B")
    E = model.set_point(21.0, -141.0, classes=["constructed"], label="E")
    F = model.set_point(44.0, -224.0, classes=["constructed"], label="F")

    # Point P on LB such that MP is perpendicular to LB
    P = model.set_point(147.0, -136.7, classes=["constructed"], label="P")

    # Tetrahedron ABCD and triangles
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, C, D])
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([B, C, D])
    model.set_polygon([L, M, B])
    model.set_polygon([B, M, C])

    # Segments and collinear sub-segments
    for p1, p2 in [
        (A, B), (A, C), (A, D), (B, C), (B, D),
        (C, D), (C, K), (K, D),
        (L, M), (L, K), (K, M),
        (G, H), (G, D), (D, H),
        (E, F), (E, A), (A, F),
        (L, B), (L, P), (P, B),
        (M, B), (M, C), (M, P),
    ]:
        model.set_segment(p1, p2)

    # Sections
    model.set_section([L, K, M])
    model.set_section([C, K, D])
    model.set_section([L, P, B])

    # Angle LMB
    model.set_wedge(M, L, L, B)

    return model


if __name__ == "__main__":
    construct_0477_g1()
