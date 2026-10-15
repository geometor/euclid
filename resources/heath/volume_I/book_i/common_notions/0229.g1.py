"""Programmatic construction for Postulate 5 Commentary, Legendre (0229.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0229_g1() -> Model:
    """Construct the figure 0229.g1 (Legendre's successive triangles) using geometor.model."""
    model = Model("0229.g1")

    # Points (y negated for Cartesian coordinates)
    A = model.set_point(25, -110, classes=["given"], label="A")
    C = model.set_point(95, -23, classes=["given"], label="C")
    B = model.set_point(136, -110, classes=["given"], label="B")
    D = model.set_point(115.5, -66.5, label="D")
    C_prime = model.set_point(129.1, -60.0, label="C'")
    E = model.set_point(206, -23, label="E")
    K = model.set_point(123, -110, label="K")
    B_prime = model.set_point(226, -110, label="B'")
    D_prime = model.set_point(177.55, -85.0, label="D'")
    K_prime = model.set_point(182, -110, label="K'")
    C_second = model.set_point(223.3, -77.5, label="C''")
    B_second = model.set_point(340, -110, label="B''")

    # Construction lines
    model.construct_line(A, B_second)
    model.construct_line(A, C)
    model.construct_line(B, C)
    model.construct_line(A, E)
    model.construct_line(B, E)
    model.construct_line(C_prime, K)
    model.construct_line(C_prime, B_prime)
    model.construct_line(A, C_second)
    model.construct_line(C_second, K_prime)
    model.construct_line(C_second, B_second)

    # Segments
    model.set_segment(A, B)
    model.set_segment(A, C)
    model.set_segment(B, C)
    model.set_segment(B, D)
    model.set_segment(D, C)
    model.set_segment(A, D)
    model.set_segment(A, C_prime)
    model.set_segment(C_prime, E)
    model.set_segment(B, E)
    model.set_segment(A, K)
    model.set_segment(C_prime, K)
    model.set_segment(A, B_prime)
    model.set_segment(B_prime, C_prime)
    model.set_segment(A, D_prime)
    model.set_segment(A, C_second)
    model.set_segment(C_second, K_prime)
    model.set_segment(A, B_second)
    model.set_segment(B_second, C_second)

    # Collinear sections
    model.set_section([B, D, C])
    model.set_section([A, D, C_prime])
    model.set_section([A, K, B])
    model.set_section([A, B, B_prime])

    # Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, D])
    model.set_polygon([A, C, D])
    model.set_polygon([A, C_prime, K])
    model.set_polygon([B_prime, C_prime, K])
    model.set_polygon([A, B_prime, C_prime])
    model.set_polygon([A, E, B])
    model.set_polygon([A, B_second, C_second])

    # Angles (wedges)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, C, C, A)
    model.set_wedge(C, A, A, B)
    model.set_wedge(A, B_prime, B_prime, C_prime)
    model.set_wedge(B_prime, C_prime, C_prime, A)
    model.set_wedge(C_prime, A, A, B_prime)
    model.set_wedge(K, B_prime, B_prime, C_prime)
    model.set_wedge(K, C_prime, C_prime, A)
    model.set_wedge(D, C, C, A)
    model.set_wedge(D, A, A, B)
    model.set_wedge(A, B_second, B_second, C_second)
    model.set_wedge(B_second, C_second, C_second, A)

    return model


if __name__ == "__main__":
    construct_0229_g1()
