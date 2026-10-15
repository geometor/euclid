"""Programmatic construction for Book IV, Proposition 8 (0100.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0100_g1() -> Model:
    """Construct the figure 0100.g1 using geometor.model."""
    model = Model("0100.g1")

    # Points (y-inverted for standard mathematical coordinates)
    A = model.set_point(26.00, -29.00, classes=["given"], label="A")
    B = model.set_point(26.00, -169.00, classes=["given"], label="B")
    C = model.set_point(166.00, -169.00, classes=["given"], label="C")
    D = model.set_point(166.00, -29.00, classes=["given"], label="D")
    E = model.set_point(96.00, -29.00, label="E")
    F = model.set_point(26.00, -99.00, label="F")
    G = model.set_point(96.00, -99.00, label="G")
    H = model.set_point(96.00, -169.00, label="H")
    K = model.set_point(166.00, -99.00, label="K")

    # Inscribed circle EFHK
    model.construct_circle(G, E)

    # Construction lines
    model.construct_line(E, H)
    model.construct_line(F, K)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(E, H)
    model.set_segment(F, K)
    model.set_segment(A, E)
    model.set_segment(E, D)
    model.set_segment(A, F)
    model.set_segment(F, B)
    model.set_segment(B, H)
    model.set_segment(H, C)
    model.set_segment(C, K)
    model.set_segment(K, D)
    model.set_segment(G, E)
    model.set_segment(G, F)
    model.set_segment(G, H)
    model.set_segment(G, K)

    # Collinear sections
    model.set_section([A, E, D])
    model.set_section([A, F, B])
    model.set_section([B, H, C])
    model.set_section([D, K, C])
    model.set_section([E, G, H])
    model.set_section([F, G, K])

    # Polygons (square and sub-parallelograms)
    model.set_polygon([A, B, C, D])
    model.set_polygon([A, F, K, D])
    model.set_polygon([F, B, C, K])
    model.set_polygon([A, B, H, E])
    model.set_polygon([E, H, C, D])
    model.set_polygon([A, F, G, E])
    model.set_polygon([G, H, C, K])
    model.set_polygon([F, B, H, G])
    model.set_polygon([E, G, K, D])

    return model


if __name__ == "__main__":
    construct_0100_g1()
