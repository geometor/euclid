"""Programmatic construction for Book IV, Proposition 13 (0111.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0111_g1() -> Model:
    """Construct the figure 0111.g1 (Circle inscribed in regular pentagon) using geometor.model."""
    model = Model("0111.g1")

    # Points (y-inverted for standard mathematical coordinates)
    F = model.set_point(109.00, -114.00, label="F")
    A = model.set_point(109.00, -29.95, classes=["given"], label="A")
    B = model.set_point(29.06, -88.03, classes=["given"], label="B")
    C = model.set_point(59.60, -182.00, classes=["given"], label="C")
    D = model.set_point(158.40, -182.00, classes=["given"], label="D")
    E = model.set_point(188.94, -88.03, classes=["given"], label="E")

    G = model.set_point(69.03, -58.99, label="G")
    H = model.set_point(44.33, -135.01, label="H")
    K = model.set_point(109.00, -182.00, label="K")
    L = model.set_point(173.67, -135.01, label="L")
    M = model.set_point(148.97, -58.99, label="M")

    # Inscribed circle GHKLM
    model.construct_circle(F, K)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(F, A)
    model.set_segment(F, B)
    model.set_segment(F, C)
    model.set_segment(F, D)
    model.set_segment(F, E)
    model.set_segment(F, G)
    model.set_segment(F, H)
    model.set_segment(F, K)
    model.set_segment(F, L)
    model.set_segment(F, M)
    model.set_segment(C, H)
    model.set_segment(C, K)

    # Collinear sections
    model.set_section([A, G, B])
    model.set_section([B, H, C])
    model.set_section([C, K, D])
    model.set_section([D, L, E])
    model.set_section([E, M, A])

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([B, C, F])
    model.set_polygon([D, C, F])
    model.set_polygon([F, H, C])
    model.set_polygon([F, K, C])

    # Angles (wedges)
    model.set_wedge(B, C, C, D)
    model.set_wedge(C, D, D, E)
    model.set_wedge(B, C, C, F)
    model.set_wedge(D, C, C, F)
    model.set_wedge(C, B, B, F)
    model.set_wedge(C, D, D, F)
    model.set_wedge(A, B, B, C)
    model.set_wedge(A, B, B, F)
    model.set_wedge(B, A, A, E)
    model.set_wedge(A, E, E, D)
    model.set_wedge(F, H, H, C)
    model.set_wedge(F, K, K, C)
    model.set_wedge(F, G, G, B)
    model.set_wedge(F, L, L, D)
    model.set_wedge(F, M, M, E)

    return model


if __name__ == "__main__":
    construct_0111_g1()
