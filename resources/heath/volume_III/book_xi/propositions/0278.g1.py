"""Programmatic construction for Book XI, Proposition 2 (0278.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0278_g1() -> Model:
    """Construct the figure 0278.g1 using geometor.model."""
    model = Model("0278.g1")

    # Endpoints of intersecting straight lines AB and CD
    A = model.set_point(55.0, -14.0, classes=["given"], label="A")
    B = model.set_point(199.0, -169.0, classes=["given"], label="B")
    C = model.set_point(13.0, -167.0, classes=["given"], label="C")
    D = model.set_point(173.0, -23.0, classes=["given"], label="D")

    # Intersection point E of AB and CD
    E = model.set_point(113.21, -76.66, label="E")

    # Random points F on EC, G on EB, and H, K on CB
    F = model.set_point(69.1, -116.5, label="F")
    G = model.set_point(160.4, -127.4, label="G")
    H = model.set_point(82.0, -167.8, label="H")
    K = model.set_point(146.0, -168.4, label="K")

    # Construction lines
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(C, B)

    # Segments along AB
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_segment(E, G)
    model.set_segment(G, B)

    # Segments along CD
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, C)
    model.set_segment(E, F)
    model.set_segment(F, C)

    # Segments along CB and interior
    model.set_segment(C, B)
    model.set_segment(C, H)
    model.set_segment(H, K)
    model.set_segment(K, B)
    model.set_segment(F, G)
    model.set_segment(F, H)
    model.set_segment(G, K)
    model.set_segment(A, D)

    # Sections
    model.set_section([A, E, B])
    model.set_section([C, E, D])
    model.set_section([E, F, C])
    model.set_section([E, G, B])

    # Polygons (triangles and quadrilateral)
    model.set_polygon([E, C, B])
    model.set_polygon([F, H, C])
    model.set_polygon([G, B, K])
    model.set_polygon([F, C, B, G])
    model.set_polygon([E, F, G])
    model.set_polygon([F, H, K, G])
    model.set_polygon([A, E, D])

    return model


if __name__ == "__main__":
    construct_0278_g1()
