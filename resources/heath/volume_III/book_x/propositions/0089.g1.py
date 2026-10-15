"""Programmatic construction for Book X, Proposition 38 (0089.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0089_g1() -> Model:
    """Construct the figure 0089.g1 using geometor.model."""
    model = Model("0089.g1")

    # Straight line AC divided into medial straight lines AB, BC
    A = model.set_point(70.0, -17.5, classes=["given"], label="A")
    B = model.set_point(148.5, -17.5, classes=["given"], label="B")
    C = model.set_point(202.0, -17.5, classes=["given"], label="C")

    # Parallelogram DF (D, H, G on top; E, H_b, F on bottom)
    D = model.set_point(19.5, -48.0, classes=["given"], label="D")
    H = model.set_point(148.5, -48.0, label="H")
    G = model.set_point(249.5, -48.0, label="G")
    E = model.set_point(19.5, -125.0, classes=["given"], label="E")
    H_b = model.set_point(148.5, -125.0, label="H_b")
    F = model.set_point(249.5, -125.0, label="F")

    # Base lines
    model.construct_line(A, C)
    model.construct_line(D, G)
    model.construct_line(E, F)
    model.construct_line(D, E)
    model.construct_line(H, H_b)
    model.construct_line(G, F)

    # Segments
    model.set_segment(A, C)
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(D, E)
    model.set_segment(D, G)
    model.set_segment(D, H)
    model.set_segment(H, G)
    model.set_segment(E, F)
    model.set_segment(E, H_b)
    model.set_segment(H_b, F)
    model.set_segment(H, H_b)
    model.set_segment(G, F)

    # Sections
    model.set_section([A, B, C])
    model.set_section([D, H, G])

    # Polygons: whole parallelogram DF and constituent rectangles EH, HF
    model.set_polygon([D, E, F, G])
    model.set_polygon([D, E, H_b, H])
    model.set_polygon([H, H_b, F, G])

    return model


if __name__ == "__main__":
    construct_0089_g1()
