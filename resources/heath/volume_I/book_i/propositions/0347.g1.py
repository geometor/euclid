"""Programmatic construction for Book I, I.38 (0347.g1).

Triangles which are on equal bases and in the same parallels are equal to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0347_g1() -> Model:
    """Construct the figure for 0347.g1 (I.38) using geometor.model."""
    model = Model("0347.g1")

    # 1. Points
    G = model.set_point(43.5, -31, label="G")
    A = model.set_point(128, -31, classes=["given"], label="A")
    D = model.set_point(150.5, -31, classes=["given"], label="D")
    H = model.set_point(234.5, -31, label="H")
    B = model.set_point(28, -101, classes=["given"], label="B")
    C = model.set_point(112, -101, classes=["given"], label="C")
    E = model.set_point(189, -101, classes=["given"], label="E")
    F = model.set_point(273, -101, classes=["given"], label="F")
    G0 = model.set_point(40, -31, label="G0")
    H0 = model.set_point(240, -31, label="H0")

    # 2. Infinite / Extended Construction Lines
    model.construct_line(G0, H0)

    # 3. Segments
    model.set_segment(G, H)
    model.set_segment(G, A)
    model.set_segment(A, D)
    model.set_segment(D, H)
    model.set_segment(B, F)
    model.set_segment(B, C)
    model.set_segment(C, E)
    model.set_segment(E, F)
    model.set_segment(B, G)
    model.set_segment(A, B)
    model.set_segment(C, A)
    model.set_segment(D, E)
    model.set_segment(D, F)
    model.set_segment(F, H)

    # 4. Collinear Sections
    model.set_section([G, A, D])
    model.set_section([A, D, H])
    model.set_section([B, C, E])
    model.set_section([C, E, F])

    # 5. Polygons (Triangles, Parallelograms, Trapezia, Squares)
    model.set_polygon([A, B, C])
    model.set_polygon([D, E, F])
    model.set_polygon([G, B, C, A])
    model.set_polygon([D, E, F, H])
    model.set_polygon([G, A, B])
    model.set_polygon([D, H, F])

    return model


if __name__ == "__main__":
    construct_0347_g1()
