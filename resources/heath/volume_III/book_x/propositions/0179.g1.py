"""Programmatic construction for Book X, Proposition 84 (0179.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0179_g1() -> Model:
    """Construct the figure 0179.g1 using geometor.model."""
    model = Model("0179.g1")

    # Top straight line AD divided at B and C
    A = model.set_point(105.0, -20.5, classes=["given"], label="A")
    B = model.set_point(147.0, -20.5, classes=["given"], label="B")
    C = model.set_point(213.0, -20.5, classes=["given"], label="C")
    D = model.set_point(242.0, -20.5, classes=["given"], label="D")

    # Rectangle EFIN divided vertically by HL and MG
    E = model.set_point(16.0, -51.5, classes=["given"], label="E")
    H = model.set_point(36.5, -51.5, label="H")
    M = model.set_point(205.5, -51.5, label="M")
    N = model.set_point(303.5, -51.5, label="N")

    F = model.set_point(16.0, -145.5, classes=["given"], label="F")
    L = model.set_point(36.5, -145.5, label="L")
    G = model.set_point(205.5, -145.5, label="G")
    I = model.set_point(303.5, -145.5, label="I")

    # Base lines
    model.construct_line(A, D)
    model.construct_line(E, N)
    model.construct_line(F, I)
    model.construct_line(E, F)
    model.construct_line(H, L)
    model.construct_line(M, G)
    model.construct_line(N, I)

    # Segments on AD
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Vertical segments on rectangle EFIN
    model.set_segment(E, F)
    model.set_segment(H, L)
    model.set_segment(M, G)
    model.set_segment(N, I)

    # Horizontal segments on top side EN
    model.set_segment(E, N)
    model.set_segment(E, M)
    model.set_segment(E, H)
    model.set_segment(H, N)
    model.set_segment(H, M)
    model.set_segment(M, N)

    # Horizontal segments on bottom side FI
    model.set_segment(F, I)
    model.set_segment(F, G)
    model.set_segment(F, L)
    model.set_segment(L, I)
    model.set_segment(L, G)
    model.set_segment(G, I)

    # Sections
    model.set_section([A, B, C])
    model.set_section([A, B, D])
    model.set_section([A, C, D])
    model.set_section([B, C, D])
    model.set_section([E, H, M])
    model.set_section([E, H, N])
    model.set_section([E, M, N])
    model.set_section([H, M, N])
    model.set_section([F, L, G])
    model.set_section([F, L, I])
    model.set_section([F, G, I])
    model.set_section([L, G, I])

    # Polygons (rectangles)
    model.set_polygon([E, F, I, N])
    model.set_polygon([E, F, G, M])
    model.set_polygon([E, F, L, H])
    model.set_polygon([H, L, G, M])
    model.set_polygon([H, L, I, N])
    model.set_polygon([M, G, I, N])

    return model


if __name__ == "__main__":
    construct_0179_g1()
