"""Programmatic construction for Book IV, Proposition 11 (0106.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0106_g1() -> Model:
    """Construct the figure 0106.g1 (Inscribed regular pentagon) using geometor.model."""
    model = Model("0106.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(79.00, -83.00, label="O")
    A = model.set_point(79.00, -28.00, classes=["given"], label="A")
    B = model.set_point(26.69, -66.00, label="B")
    C = model.set_point(46.67, -127.50, label="C")
    D = model.set_point(111.33, -127.50, label="D")
    E = model.set_point(131.31, -66.00, label="E")

    # Auxiliary golden triangle FGH
    F = model.set_point(205.00, -36.00, classes=["given"], label="F")
    G = model.set_point(182.75, -104.48, classes=["given"], label="G")
    H = model.set_point(227.25, -104.48, classes=["given"], label="H")

    # Given circle ABCDE
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, E)
    model.set_segment(E, A)
    model.set_segment(A, C)
    model.set_segment(A, D)
    model.set_segment(B, D)
    model.set_segment(C, E)
    model.set_segment(F, G)
    model.set_segment(G, H)
    model.set_segment(H, F)

    # Polygons
    model.set_polygon([A, B, C, D, E])
    model.set_polygon([A, C, D])
    model.set_polygon([F, G, H])

    # Angles (wedges)
    model.set_wedge(G, F, F, H)
    model.set_wedge(H, G, G, F)
    model.set_wedge(F, H, H, G)
    model.set_wedge(C, A, A, D)
    model.set_wedge(D, C, C, A)
    model.set_wedge(A, D, D, C)
    model.set_wedge(E, C, C, A)
    model.set_wedge(D, C, C, E)
    model.set_wedge(C, D, D, B)
    model.set_wedge(B, D, D, A)
    model.set_wedge(B, A, A, E)
    model.set_wedge(A, E, E, D)
    model.set_wedge(A, B, B, C)
    model.set_wedge(B, C, C, D)
    model.set_wedge(C, D, D, E)

    return model


if __name__ == "__main__":
    construct_0106_g1()
