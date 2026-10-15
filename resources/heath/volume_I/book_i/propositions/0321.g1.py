"""Programmatic construction for Book I, Proposition 27 (0321.g1).

If a straight line falling on two straight lines make the alternate angles equal
to one another, the straight lines will be parallel to one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0321_g1() -> Model:
    """Construct the figure for Book I, Proposition 27 (0321.g1) using geometor.model."""
    model = Model("0321.g1")

    A = model.set_point(20, -29, classes=["given"], label="A")
    B = model.set_point(150, -29, classes=["given"], label="B")
    C = model.set_point(20, -77, classes=["given"], label="C")
    D = model.set_point(150, -77, classes=["given"], label="D")
    E = model.set_point(95, -29, classes=["given"], label="E")
    F = model.set_point(70, -77, classes=["given"], label="F")
    G = model.set_point(207, -51, label="G")

    # Lines and transversal
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)

    # Segments and collinear sub-segments
    model.set_segment(A, B)
    model.set_segment(A, E)
    model.set_segment(E, B)
    model.set_section([A, E, B])

    model.set_segment(C, D)
    model.set_segment(C, F)
    model.set_segment(F, D)
    model.set_section([C, F, D])

    model.set_segment(E, F)
    model.set_segment(B, G)
    model.set_segment(D, G)
    model.set_segment(E, G)
    model.set_segment(F, G)

    # Hypothetical triangle GEF in reductio proof
    model.set_polygon([G, E, F])

    # Alternate and exterior/interior angles: < A E F ), < E F D ), < E F G )
    model.set_wedge(E, A, A, F)
    model.set_wedge(F, E, E, D)
    model.set_wedge(F, E, E, G)

    return model


if __name__ == "__main__":
    construct_0321_g1()
