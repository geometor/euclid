"""Programmatic construction for Book I, Proposition 28 (0324.g1).

If a straight line falling on two straight lines make the exterior angle equal
to the interior and opposite angle on the same side, or the interior angles on
the same side equal to two right angles, the straight lines will be parallel to
one another.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0324_g1() -> Model:
    """Construct the figure for Book I, Proposition 28 (0324.g1) using geometor.model."""
    model = Model("0324.g1")

    A = model.set_point(26, -64, classes=["given"], label="A")
    B = model.set_point(215, -64, classes=["given"], label="B")
    C = model.set_point(26, -116, classes=["given"], label="C")
    D = model.set_point(215, -116, classes=["given"], label="D")
    E = model.set_point(94, -41, classes=["given"], label="E")
    F = model.set_point(174, -145, classes=["given"], label="F")
    G = model.set_point(112, -64, label="G")
    H = model.set_point(151.5, -116, label="H")

    # Parallel lines and transversal
    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)

    # Segments and collinear sub-segments
    model.set_segment(A, B)
    model.set_segment(A, G)
    model.set_segment(G, B)
    model.set_section([A, G, B])

    model.set_segment(C, D)
    model.set_segment(C, H)
    model.set_segment(H, D)
    model.set_section([C, H, D])

    model.set_segment(E, F)
    model.set_segment(E, G)
    model.set_segment(G, H)
    model.set_segment(H, F)
    model.set_section([E, G, H])
    model.set_section([G, H, F])

    model.set_polygon([A, G, H, C])
    model.set_polygon([B, G, H, D])

    # Angles at G and H
    model.set_wedge(G, E, E, B)
    model.set_wedge(G, A, A, H)
    model.set_wedge(G, B, B, H)
    model.set_wedge(H, G, G, D)

    return model


if __name__ == "__main__":
    construct_0324_g1()
