"""Programmatic construction for Book I, Proposition 29 (0325.g1).

A straight line falling on parallel straight lines makes the alternate angles
equal to one another, the exterior angle equal to the interior and opposite
angle, and the interior angles on the same side equal to two right angles.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0325_g1() -> Model:
    """Construct the figure for Book I, Proposition 29 (0325.g1) using geometor.model."""
    model = Model("0325.g1")

    A = model.set_point(20, -69.5, classes=["given"], label="A")
    B = model.set_point(180, -69.5, classes=["given"], label="B")
    C = model.set_point(20, -116.5, classes=["given"], label="C")
    D = model.set_point(180, -116.5, classes=["given"], label="D")
    E = model.set_point(64, -36, classes=["given"], label="E")
    F = model.set_point(134.5, -148, classes=["given"], label="F")
    G = model.set_point(85, -69.5, label="G")
    H = model.set_point(114.5, -116.5, label="H")

    model.construct_line(A, B)
    model.construct_line(C, D)
    model.construct_line(E, F)

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
    model.set_wedge(G, A, A, H)
    model.set_wedge(G, B, B, H)
    model.set_wedge(G, E, E, B)
    model.set_wedge(H, G, G, D)

    return model


if __name__ == "__main__":
    construct_0325_g1()
