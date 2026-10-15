"""Programmatic construction for Book I, Definitions Commentary (0202.g1).

The barb-like (ἀκιδοειδής) or hollow-angled (κοιλογώνιος) quadrilateral ABCD
with a re-entrant angle at C, cited by Proclus in his commentary on the
classification of triangles and quadrilaterals.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0202_g1() -> Model:
    """Construct the barb-like / hollow-angled quadrilateral (0202.g1)."""
    model = Model("0202.g1")

    # Four vertices of the non-convex quadrilateral ABCD (C is the re-entrant vertex)
    A = model.set_point(40, 79, classes=["given"], label="A")
    B = model.set_point(7, 17, classes=["given"], label="B")
    C = model.set_point(36, 43, classes=["given"], label="C")
    D = model.set_point(70, 14, classes=["given"], label="D")

    model.construct_line(A, B)
    model.construct_line(B, C)
    model.construct_line(C, D)
    model.construct_line(D, A)

    model.set_segment(A, B)
    model.set_segment(B, C)
    model.set_segment(C, D)
    model.set_segment(D, A)

    model.set_polygon([A, B, C, D])

    return model


if __name__ == "__main__":
    construct_0202_g1()
