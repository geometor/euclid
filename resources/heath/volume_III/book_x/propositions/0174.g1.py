"""Programmatic construction for Book X, Proposition 81 (0174.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0174_g1() -> Model:
    """Construct the figure 0174.g1 using geometor.model."""
    model = Model("0174.g1")

    # Top straight line AD divided at B and C
    A = model.set_point(16.0, -21.5, classes=["given"], label="A")
    B = model.set_point(80.0, -21.5, classes=["given"], label="B")
    C = model.set_point(122.0, -21.5, classes=["given"], label="C")
    D = model.set_point(154.0, -21.5, classes=["given"], label="D")

    # Rectangle FEIN divided horizontally by LH and GM
    F = model.set_point(29.0, -45.5, classes=["given"], label="F")
    E = model.set_point(121.0, -45.5, classes=["given"], label="E")

    L = model.set_point(29.0, -65.5, label="L")
    H = model.set_point(121.0, -65.5, label="H")

    G = model.set_point(29.0, -237.0, label="G")
    M = model.set_point(121.0, -237.0, label="M")

    I = model.set_point(29.0, -335.0, label="I")
    N = model.set_point(121.0, -335.0, label="N")

    # Base lines
    model.construct_line(A, D)
    model.construct_line(F, E)
    model.construct_line(L, H)
    model.construct_line(G, M)
    model.construct_line(I, N)
    model.construct_line(F, I)
    model.construct_line(E, N)

    # Segments on AD
    model.set_segment(A, D)
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, D)
    model.set_segment(B, C)
    model.set_segment(C, D)

    # Horizontal segments on rectangle FEIN
    model.set_segment(F, E)
    model.set_segment(L, H)
    model.set_segment(G, M)
    model.set_segment(I, N)

    # Vertical segments on left side FI
    model.set_segment(F, I)
    model.set_segment(F, G)
    model.set_segment(F, L)
    model.set_segment(L, I)
    model.set_segment(L, G)
    model.set_segment(G, I)

    # Vertical segments on right side EN
    model.set_segment(E, N)
    model.set_segment(E, M)
    model.set_segment(E, H)
    model.set_segment(H, N)
    model.set_segment(H, M)
    model.set_segment(M, N)

    # Sections
    model.set_section([A, B, C])
    model.set_section([A, B, D])
    model.set_section([A, C, D])
    model.set_section([B, C, D])
    model.set_section([F, L, G])
    model.set_section([F, L, I])
    model.set_section([F, G, I])
    model.set_section([L, G, I])
    model.set_section([E, H, M])
    model.set_section([E, H, N])
    model.set_section([E, M, N])
    model.set_section([H, M, N])

    # Polygons (rectangles)
    model.set_polygon([F, E, N, I])
    model.set_polygon([F, E, M, G])
    model.set_polygon([F, E, H, L])
    model.set_polygon([L, H, M, G])
    model.set_polygon([L, H, N, I])
    model.set_polygon([G, M, N, I])

    return model


if __name__ == "__main__":
    construct_0174_g1()
