"""Programmatic construction for Appendix I (Book XIV), Proposition 7 (0521.g2).

Circle AHB with centre C and radius CB divided in extreme and mean ratio at D,
together with straight lines E (side of icosahedron), F (side of dodecahedron),
and G (side of cube).
"""

from __future__ import annotations

from geometor.model import Model


def construct_0521_g2() -> Model:
    """Construct the figure 0521.g2 using geometor.model."""
    model = Model("0521.g2")

    # Circle AHB with centre C and radius CB divided at D
    C = model.set_point(94.0, -88.0, classes=["given"], label="C")
    A = model.set_point(94.0, -20.0, classes=["given"], label="A")
    H = model.set_point(94.0, -156.0, classes=["given"], label="H")
    D = model.set_point(136.0, -88.0, classes=["given"], label="D")
    B = model.set_point(162.0, -88.0, classes=["given"], label="B")
    model.construct_circle(C, B)

    # Single-letter magnitude lines E, F, G
    E1 = model.set_point(24.0, -175.0, classes=["auxiliary"], label="E1")
    E2 = model.set_point(138.0, -175.0, classes=["auxiliary"], label="E2")
    F1 = model.set_point(24.0, -194.0, classes=["auxiliary"], label="F1")
    F2 = model.set_point(110.0, -194.0, classes=["auxiliary"], label="F2")
    G1 = model.set_point(24.0, -213.0, classes=["auxiliary"], label="G1")
    G2 = model.set_point(144.0, -213.0, classes=["auxiliary"], label="G2")

    # Section CDB
    model.set_section([C, D, B])

    # Segments
    for p1, p2 in [
        (C, B), (C, D), (D, B),
        (E1, E2), (F1, F2), (G1, G2),
    ]:
        model.set_segment(p1, p2)

    return model


if __name__ == "__main__":
    construct_0521_g2()
