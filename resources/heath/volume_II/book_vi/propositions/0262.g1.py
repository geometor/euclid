"""Programmatic construction for Book VI, Proposition 26 Extension (0262.g1).

Extension of VI.26 to two similar and similarly situated parallelograms AEFG,
ABCD placed outside one another with vertically opposite angles at A: their
diameters FA, AC are in a straight line.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0262_g1() -> Model:
    """Construct the figure for 0262.g1 (VI.26 extension) using geometor.model."""
    model = Model("0262.g1")

    # 1. Points of outer similar parallelograms AEFG and ABCD meeting at A
    F = model.set_point(25.0, -29.0, label="F")
    E = model.set_point(56.0, -29.0, label="E")
    G = model.set_point(20.0, -59.0, label="G")
    A = model.set_point(51.0, -59.0, classes=["given"], label="A")
    D = model.set_point(122.0, -59.0, classes=["given"], label="D")
    B = model.set_point(40.0, -129.0, classes=["given"], label="B")
    C = model.set_point(111.0, -129.0, classes=["given"], label="C")

    # 2. Construction lines
    model.construct_line(G, D)
    model.construct_line(E, B)
    model.construct_line(F, C)

    # 3. Segments
    model.set_segment(F, E)
    model.set_segment(G, A)
    model.set_segment(A, D)
    model.set_segment(G, D)
    model.set_segment(B, C)

    model.set_segment(F, G)
    model.set_segment(E, A)
    model.set_segment(A, B)
    model.set_segment(E, B)
    model.set_segment(D, C)

    model.set_segment(F, A)
    model.set_segment(A, C)
    model.set_segment(F, C)

    # 4. Collinear sections
    model.set_section([G, A, D])
    model.set_section([E, A, B])
    model.set_section([F, A, C])

    # 5. Parallelograms AEFG and ABCD
    model.set_polygon([A, E, F, G])
    model.set_polygon([A, B, C, D])

    return model


if __name__ == "__main__":
    construct_0262_g1()
