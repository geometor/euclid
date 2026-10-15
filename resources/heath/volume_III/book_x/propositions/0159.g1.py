"""Programmatic construction for Book X, Proposition 72 (0159.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0159_g1() -> Model:
    """Construct the figure 0159.g1 using geometor.model."""
    model = Model("0159.g1")

    # Left area AD composed of two incommensurable medial areas AB, CD
    A = model.set_point(21.5, -16.5, classes=["given"], label="A")
    C = model.set_point(105.5, -16.5, classes=["given"], label="C")
    C_r = model.set_point(147.5, -16.5, label="C_r")
    A_b = model.set_point(21.5, -104.0, label="A_b")
    B = model.set_point(105.5, -104.0, classes=["given"], label="B")
    D = model.set_point(147.5, -104.0, classes=["given"], label="D")

    # Right rectangle EI applied to rational straight line EF
    E = model.set_point(274.5, -41.0, classes=["given"], label="E")
    F = model.set_point(478.0, -41.0, classes=["given"], label="F")
    H = model.set_point(274.5, -83.0, label="H")
    G = model.set_point(478.0, -83.0, label="G")
    K = model.set_point(274.5, -100.0, label="K")
    I = model.set_point(478.0, -100.0, label="I")

    # Base lines
    model.construct_line(A, C_r)
    model.construct_line(A_b, D)
    model.construct_line(A, A_b)
    model.construct_line(C, B)
    model.construct_line(C_r, D)

    model.construct_line(E, F)
    model.construct_line(H, G)
    model.construct_line(K, I)
    model.construct_line(E, K)
    model.construct_line(F, I)

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

    model.set_segment(E, F)
    model.set_segment(H, G)
    model.set_segment(K, I)
    model.set_segment(E, K)
    model.set_segment(E, H)
    model.set_segment(H, K)
    model.set_segment(F, I)
    model.set_segment(F, G)
    model.set_segment(G, I)

    # Sections
    model.set_section([E, H, K])
    model.set_section([F, G, I])

    # Polygons
    model.set_polygon([A, A_b, B, C])
    model.set_polygon([C, B, D, C_r])
    model.set_polygon([A, A_b, D, C_r])
    model.set_polygon([E, H, G, F])
    model.set_polygon([H, K, I, G])
    model.set_polygon([E, K, I, F])

    return model


if __name__ == "__main__":
    construct_0159_g1()
