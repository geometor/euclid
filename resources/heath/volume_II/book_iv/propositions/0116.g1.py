"""Programmatic construction for Book IV, Proposition 16 (0116.g1)."""

from __future__ import annotations

from geometor.model import Model


def construct_0116_g1() -> Model:
    """Construct the figure 0116.g1 (Inscribed regular fifteen-angled figure) using geometor.model."""
    model = Model("0116.g1")

    # Points (y-inverted for standard mathematical coordinates)
    O = model.set_point(153.00, -156.00, label="O")
    A = model.set_point(153.00, -30.00, classes=["given"], label="A")
    B = model.set_point(33.17, -117.06, label="B")
    E = model.set_point(27.69, -169.17, label="E")
    C = model.set_point(43.88, -219.00, label="C")
    D = model.set_point(262.12, -219.00, label="D")

    P2 = model.set_point(204.25, -40.89, label="P2")
    P3 = model.set_point(246.64, -71.69, label="P3")
    P4 = model.set_point(272.83, -117.06, label="P4")
    P5 = model.set_point(278.31, -169.17, label="P5")
    P7 = model.set_point(227.06, -257.94, label="P7")
    P8 = model.set_point(179.20, -279.25, label="P8")
    P9 = model.set_point(126.80, -279.25, label="P9")
    P10 = model.set_point(78.94, -257.94, label="P10")
    P14 = model.set_point(59.36, -71.69, label="P14")
    P15 = model.set_point(101.75, -40.89, label="P15")

    # Given circle ABCD
    model.construct_circle(O, A)

    # Segments
    model.set_segment(A, C)
    model.set_segment(C, D)
    model.set_segment(D, A)
    model.set_segment(A, B)
    model.set_segment(B, E)
    model.set_segment(E, C)

    # Polygons
    model.set_polygon([A, C, D])
    model.set_polygon([A, P4, P7, P10, B])
    model.set_polygon([A, P2, P3, P4, P5, D, P7, P8, P9, P10, C, E, B, P14, P15])

    return model


if __name__ == "__main__":
    construct_0116_g1()
