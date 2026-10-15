"""Programmatic construction for Book VI, Proposition D note (0232.g1).

Dr Lachlan's first figure: pedal triangle XYZ of any point D with respect
to triangle ABC inscribed in a circle.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0232_g1() -> Model:
    """Construct the figure for 0232.g1 using geometor.model."""
    model = Model("0232.g1")

    # 1. Given / Base Points
    O = model.set_point(93.0, -89.0, classes=["given"], label="O")
    A = model.set_point(133.26, -29.31, classes=["given"], label="A")
    B = model.set_point(27.22, -118.29, classes=["given"], label="B")
    C = model.set_point(158.78, -118.29, classes=["given"], label="C")
    D = model.set_point(120.0, -182.0, classes=["given"], label="D")

    # Feet of perpendiculars from D to BC, CA, AB
    X = model.set_point(120.0, -118.29, classes=["given"], label="X")
    Y = model.set_point(169.49, -155.65, classes=["given"], label="Y")
    Z = model.set_point(49.49, -99.60, classes=["given"], label="Z")

    # 2. Circle and Construction Lines
    model.construct_circle(O, A)
    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(A, C)

    # 3. Segments
    model.set_segment(A, B)
    model.set_segment(A, Z)
    model.set_segment(Z, B)

    model.set_segment(B, C)
    model.set_segment(B, X)
    model.set_segment(X, C)

    model.set_segment(C, A)
    model.set_segment(C, Y)
    model.set_segment(A, Y)

    model.set_segment(D, A)
    model.set_segment(B, D)
    model.set_segment(C, D)

    model.set_segment(D, X)
    model.set_segment(D, Y)
    model.set_segment(D, Z)

    model.set_segment(Y, Z)
    model.set_segment(Z, X)
    model.set_segment(X, Y)

    # 4. Collinear Sections
    model.set_section([A, Z, B])
    model.set_section([B, X, C])
    model.set_section([A, C, Y])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, Y, D, Z])

    # 6. Angles / Wedges
    model.set_wedge(A, B, B, C)
    model.set_wedge(Y, A, A, D)
    model.set_wedge(Z, A, A, D)

    return model


if __name__ == "__main__":
    construct_0232_g1()
