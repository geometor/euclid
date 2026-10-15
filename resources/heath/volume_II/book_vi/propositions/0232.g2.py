"""Programmatic construction for Book VI, Proposition D note (0232.g2).

Dr Lachlan's second figure: Simson line XYZ when D lies on the circle
circumscribed about triangle ABC.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0232_g2() -> Model:
    """Construct the figure for 0232.g2 using geometor.model."""
    model = Model("0232.g2")

    # 1. Points
    O = model.set_point(114.0, -118.0, classes=["given"], label="O")
    A = model.set_point(178.71, -86.44, classes=["given"], label="A")
    B = model.set_point(181.66, -142.63, classes=["given"], label="B")
    C = model.set_point(46.34, -142.63, classes=["given"], label="C")
    D = model.set_point(60.49, -69.82, classes=["given"], label="D")

    # Feet of perpendiculars from D to BC, CA, AB produced
    X = model.set_point(60.49, -142.63, classes=["given"], label="X")
    Y = model.set_point(84.52, -126.42, classes=["given"], label="Y")
    Z = model.set_point(177.89, -70.70, classes=["given"], label="Z")

    # 2. Circle and Construction Lines
    model.construct_circle(O, A)
    model.construct_line(B, C)
    model.construct_line(C, A)
    model.construct_line(B, Z)
    model.construct_line(X, Z)

    # 3. Segments
    model.set_segment(B, C)
    model.set_segment(C, X)
    model.set_segment(X, B)

    model.set_segment(C, A)
    model.set_segment(C, Y)
    model.set_segment(Y, A)

    model.set_segment(B, Z)
    model.set_segment(B, A)
    model.set_segment(A, Z)

    model.set_segment(D, X)
    model.set_segment(D, Y)
    model.set_segment(D, Z)

    model.set_segment(X, Z)
    model.set_segment(X, Y)
    model.set_segment(Y, Z)

    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(C, D)

    # 4. Collinear Sections
    model.set_section([C, X, B])
    model.set_section([C, Y, A])
    model.set_section([B, A, Z])
    model.set_section([X, Y, Z])

    # 5. Polygons
    model.set_polygon([A, B, C])
    model.set_polygon([A, B, C, D])

    return model


if __name__ == "__main__":
    construct_0232_g2()
