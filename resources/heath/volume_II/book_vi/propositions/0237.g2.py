"""Programmatic construction for Book VI, Proposition 18 note (0237.g2).

Clavius's construction of polygon CD'E'F'G' similar and similarly situated
to CDEFG on CD' = AB.
"""

from __future__ import annotations

from geometor.model import Model


def construct_0237_g2() -> Model:
    """Construct the figure for 0237.g2 using geometor.model."""
    model = Model("0237.g2")

    # 1. Points of CDEFG
    C = model.set_point(65.0, -147.0, classes=["given"], label="C")
    D = model.set_point(156.0, -147.0, classes=["given"], label="D")
    E = model.set_point(192.0, -112.0, classes=["given"], label="E")
    F = model.set_point(65.0, -69.0, classes=["given"], label="F")
    G = model.set_point(41.0, -95.0, classes=["given"], label="G")

    # 2. Points of CD'E'F'G' and given segment AB
    Dp = model.set_point(200.0, -147.0, classes=["given"], label="D'")
    Ep = model.set_point(253.0, -95.0, classes=["given"], label="E'")
    Fp = model.set_point(65.0, -31.0, classes=["given"], label="F'")
    Gp = model.set_point(28.0, -68.0, classes=["given"], label="G'")

    A = model.set_point(266.0, -147.0, classes=["given"], label="A")
    B = model.set_point(401.0, -147.0, classes=["given"], label="B")

    # 3. Construction Lines
    model.construct_line(C, Dp)
    model.construct_line(C, Ep)
    model.construct_line(C, Fp)
    model.construct_line(C, Gp)

    # 4. Segments
    model.set_segment(C, D)
    model.set_segment(D, Dp)
    model.set_segment(C, Dp)
    model.set_segment(D, E)
    model.set_segment(E, F)
    model.set_segment(F, G)
    model.set_segment(G, C)
    model.set_segment(G, Gp)
    model.set_segment(C, Gp)
    model.set_segment(C, E)
    model.set_segment(E, Ep)
    model.set_segment(C, Ep)
    model.set_segment(C, F)
    model.set_segment(F, Fp)
    model.set_segment(C, Fp)
    model.set_segment(Dp, Ep)
    model.set_segment(Ep, Fp)
    model.set_segment(Fp, Gp)
    model.set_segment(A, B)

    # 5. Sections
    model.set_section([C, D, Dp])
    model.set_section([C, E, Ep])
    model.set_section([C, F, Fp])
    model.set_section([C, G, Gp])

    # 6. Polygons
    model.set_polygon([C, D, E, F, G])
    model.set_polygon([C, Dp, Ep, Fp, Gp])

    return model


if __name__ == "__main__":
    construct_0237_g2()
