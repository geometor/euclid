"""Programmatic construction for Book VI, Proposition 3 Commentary (0203.g1).

Combined figure for Proposition 3 (internal bisector) and Simson's Proposition A (external bisector).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0203_g1() -> Model:
    """Construct the figure for 0203.g1 (VI.3 commentary) using geometor.model."""
    model = Model("0203.g1")

    # 1. Points - Left Figure (Internal Bisector)
    A = model.set_point(172, -69, classes=["given"], label="A")
    B = model.set_point(44, -134, classes=["given"], label="B")
    C = model.set_point(182, -134, classes=["given"], label="C")
    D = model.set_point(138.64, -134, classes=["given"], label="D")
    E = model.set_point(230.64, -39.22, label="E")
    F = model.set_point(115.68, -97.60, label="F")

    # Points - Right Figure (External Bisector)
    A2 = model.set_point(442, -69, classes=["given"], label="A")
    B2 = model.set_point(314, -134, classes=["given"], label="B")
    C2 = model.set_point(451, -134, classes=["given"], label="C")
    D2 = model.set_point(566.35, -134, label="D")
    E2 = model.set_point(383.49, -98.71, label="E")
    F2 = model.set_point(484.80, -47.27, label="F")

    # 2. Construction Lines
    model.construct_line(B, E)
    model.construct_line(B2, F2)
    model.construct_line(B2, D2)

    # 3. Segments - Left Figure
    model.set_segment(B, F)
    model.set_segment(F, A)
    model.set_segment(A, E)
    model.set_segment(B, A)
    model.set_segment(B, E)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(B, C)
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(C, E)

    # Segments - Right Figure
    model.set_segment(B2, E2)
    model.set_segment(E2, A2)
    model.set_segment(A2, F2)
    model.set_segment(B2, A2)
    model.set_segment(B2, F2)
    model.set_segment(B2, C2)
    model.set_segment(C2, D2)
    model.set_segment(B2, D2)
    model.set_segment(A2, C2)
    model.set_segment(A2, D2)
    model.set_segment(C2, E2)

    # 4. Collinear Sections
    model.set_section([B, F, A])
    model.set_section([B, A, E])
    model.set_section([B, D, C])
    model.set_section([B2, E2, A2])
    model.set_section([B2, A2, F2])
    model.set_section([B2, C2, D2])

    # 5. Polygons (Triangles)
    model.set_polygon([A, B, C])
    model.set_polygon([B, C, E])
    model.set_polygon([A, B, D])
    model.set_polygon([A, D, C])
    model.set_polygon([A, C, E])
    model.set_polygon([A2, B2, C2])
    model.set_polygon([B2, C2, E2])
    model.set_polygon([A2, C2, E2])
    model.set_polygon([A2, C2, D2])
    model.set_polygon([A2, B2, D2])

    # 6. Angles (Wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, D)
    model.set_wedge(A, C, C, D)
    model.set_wedge(A2, F2, F2, C2)
    model.set_wedge(A2, F2, F2, D2)
    model.set_wedge(A2, C2, C2, D2)
    model.set_wedge(A2, B2, B2, C2)

    return model


if __name__ == "__main__":
    construct_0203_g1()
