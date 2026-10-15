"""Programmatic construction for Book X, Proposition 71 (0156.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0156_g1() -> Model:
    """Construct the figure 0156.g1 using geometor.model."""
    model = Model("0156.g1")

    # Left area AD composed of rational area AB and medial area CD
    A = model.set_point(21.0, -18.5, classes=["given"], label="A")
    C = model.set_point(83.5, -18.5, classes=["given"], label="C")
    C_r = model.set_point(107.0, -18.5, label="C_r")
    A_b = model.set_point(21.0, -172.0, label="A_b")
    B = model.set_point(83.5, -172.0, classes=["given"], label="B")
    D = model.set_point(107.0, -172.0, classes=["given"], label="D")

    # Right rectangle EI applied to rational straight line EF
    E = model.set_point(221.5, -47.5, classes=["given"], label="E")
    H = model.set_point(312.5, -47.5, label="H")
    K = model.set_point(367.5, -47.5, label="K")
    F = model.set_point(221.5, -156.0, classes=["given"], label="F")
    G = model.set_point(312.5, -156.0, label="G")
    I = model.set_point(367.5, -156.0, label="I")

    # Base lines
    model.construct_line(A, C_r)
    model.construct_line(A_b, D)
    model.construct_line(A, A_b)
    model.construct_line(C, B)
    model.construct_line(C_r, D)

    model.construct_line(E, K)
    model.construct_line(F, I)
    model.construct_line(E, F)
    model.construct_line(H, G)
    model.construct_line(K, I)

    # Segments
    model.set_segment(A, C_r)
    model.set_segment(A, C)
    model.set_segment(C, C_r)
    model.set_segment(A_b, D)
    model.set_segment(A_b, B)
    model.set_segment(B, D)
    model.set_segment(A, A_b)
    model.set_segment(C, B)
    model.set_segment(C_r, D)

    model.set_segment(E, K)
    model.set_segment(E, H)
    model.set_segment(H, K)
    model.set_segment(F, I)
    model.set_segment(F, G)
    model.set_segment(G, I)
    model.set_segment(E, F)
    model.set_segment(H, G)
    model.set_segment(K, I)

    # Sections
    model.set_section([E, H, K])
    model.set_section([F, G, I])

    # Polygons
    model.set_polygon([A, A_b, B, C])
    model.set_polygon([C, B, D, C_r])
    model.set_polygon([A, A_b, D, C_r])
    model.set_polygon([E, F, G, H])
    model.set_polygon([H, G, I, K])
    model.set_polygon([E, F, I, K])

    return model


if __name__ == "__main__":
    construct_0156_g1()
